import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, catchError, map, of } from 'rxjs';
import {
  AccessSnapshot,
  AccessState,
  BlockingReason,
  ToolEntitlement,
  ToolKey,
  TrialStartResult,
} from '../access/access.models';
import { getToolPolicy } from '../access/access-policy';

const STORAGE_KEY = 'ww-access-state-v1';
const MAX_CLOCK_ROLLBACK_MS = 5 * 60 * 1000;
const TRIAL_ATTEMPT_COOLDOWN_MS = 30 * 1000;
const ACCESS_API_BASE = '/api/access';

interface ApiToolEntitlement {
  toolKey: ToolKey;
  accessLevel: 'NONE' | 'TRIAL' | 'SUBSCRIBED' | 'GRANTED';
  hasAccess: boolean;
  trialActive: boolean;
  trialExpired: boolean;
  trialAvailable: boolean;
  subscribed: boolean;
  accessExpiresAt: string | null;
}

interface ApiAccessOverview {
  entitlements: ApiToolEntitlement[];
}

interface ApiCanAccessResponse {
  toolKey: ToolKey;
  path: string;
  canAccess: boolean;
  reason: BlockingReason | null;
}

interface ApiTrialStartResponse {
  toolKey: ToolKey;
  message: string;
  trialExpiresAt: string | null;
}

@Injectable({ providedIn: 'root' })
export class AccessControlService {
  constructor(private readonly http: HttpClient) {}

  getSnapshot(toolKey: ToolKey, targetUrl: string): AccessSnapshot {
    const state = this.readState();
    const policy = getToolPolicy(toolKey);
    const entitlement = state.entitlements[toolKey];
    const now = Date.now();

    const isGuestPreview = this.isGuestPreviewPath(policy.guestPreviewPaths, targetUrl);
    const isSubscribed = Boolean(entitlement.subscribedAt);
    const trialActive = this.isTrialActive(entitlement, now, state.clockRollbackDetected);
    const trialExpired = Boolean(entitlement.trialExpiresAt) && !trialActive;
    const trialAvailable = this.canStartTrialInternal(state, toolKey, now);

    return {
      toolKey,
      toolName: policy.displayName,
      isRegistered: Boolean(state.registeredAt),
      isSubscribed,
      isGuestPreview,
      trialActive,
      trialExpired,
      trialAvailable,
      trialEndsAt: entitlement.trialExpiresAt,
      blockingReason: this.getBlockingReasonForState(state, toolKey, targetUrl, now),
    };
  }

  getBlockingReason(toolKey: ToolKey, targetUrl: string): BlockingReason | null {
    return this.getSnapshot(toolKey, targetUrl).blockingReason;
  }

  getSnapshot$(toolKey: ToolKey, targetUrl: string): Observable<AccessSnapshot> {
    const token = this.getAuthToken();
    if (!token) {
      return of(this.getSnapshot(toolKey, targetUrl));
    }

    return this.http
      .get<ApiAccessOverview>(`${ACCESS_API_BASE}/me`, { headers: this.getAuthHeaders(token) })
      .pipe(
        map(response => this.mapApiSnapshot(toolKey, targetUrl, response.entitlements)),
        catchError(() => of(this.getSnapshot(toolKey, targetUrl))),
      );
  }

  getBlockingReason$(toolKey: ToolKey, targetUrl: string): Observable<BlockingReason | null> {
    const token = this.getAuthToken();
    if (!token) {
      return of(this.getBlockingReason(toolKey, targetUrl));
    }

    return this.http
      .get<ApiCanAccessResponse>(`${ACCESS_API_BASE}/${toolKey}/can-access`, {
        headers: this.getAuthHeaders(token),
        params: { path: this.normalizePath(targetUrl) },
      })
      .pipe(
        map(response => (response.canAccess ? null : response.reason ?? 'trial-required')),
        catchError(() => of(this.getBlockingReason(toolKey, targetUrl))),
      );
  }

  markRegistered(): void {
    const state = this.readState();
    if (!state.registeredAt) {
      state.registeredAt = Date.now();
      this.writeState(state);
    }
  }

  subscribe(toolKey: ToolKey): void {
    const state = this.readState();
    state.entitlements[toolKey].subscribedAt = Date.now();
    this.writeState(state);
  }

  startTrial(toolKey: ToolKey): TrialStartResult {
    const state = this.readState();
    const now = Date.now();
    const entitlement = state.entitlements[toolKey];

    if (!state.registeredAt) {
      return { success: false, message: 'Please register before starting your free 1-day trial.' };
    }

    if (state.clockRollbackDetected) {
      return {
        success: false,
        message: 'Security check triggered due to clock mismatch. Please contact support.',
      };
    }

    if (entitlement.subscribedAt) {
      return { success: false, message: 'You are already subscribed to this tool.' };
    }

    if (entitlement.trialAttemptedAt && now - entitlement.trialAttemptedAt < TRIAL_ATTEMPT_COOLDOWN_MS) {
      return { success: false, message: 'Please wait a few seconds before trying again.' };
    }

    entitlement.trialAttemptedAt = now;

    if (entitlement.trialConsumedAt) {
      this.writeState(state);
      return { success: false, message: 'Your free trial was already used for this tool.' };
    }

    const trialDurationMs = getToolPolicy(toolKey).trialDurationMs;
    entitlement.trialStartedAt = now;
    entitlement.trialExpiresAt = now + trialDurationMs;
    entitlement.trialConsumedAt = now;
    entitlement.trialFingerprint = this.getDeviceFingerprint();

    this.writeState(state);
    return { success: true, message: 'Your 1-day free trial is active now.' };
  }

  startTrial$(toolKey: ToolKey): Observable<TrialStartResult> {
    const token = this.getAuthToken();
    if (!token) {
      return of(this.startTrial(toolKey));
    }

    return this.http
      .post<ApiTrialStartResponse>(`${ACCESS_API_BASE}/${toolKey}/start-trial`, {}, {
        headers: this.getAuthHeaders(token),
      })
      .pipe(
        map(response => {
          const trialExpiresAt = response.trialExpiresAt;
          const success = Boolean(trialExpiresAt);
          if (trialExpiresAt) {
            this.applyRemoteTrial(toolKey, trialExpiresAt);
          }
          return { success, message: response.message };
        }),
        catchError(() => of(this.startTrial(toolKey))),
      );
  }

  private getBlockingReasonForState(
    state: AccessState,
    toolKey: ToolKey,
    targetUrl: string,
    now: number,
  ): BlockingReason | null {
    const entitlement = state.entitlements[toolKey];
    const policy = getToolPolicy(toolKey);

    if (this.isGuestPreviewPath(policy.guestPreviewPaths, targetUrl)) {
      return null;
    }

    if (entitlement.subscribedAt) {
      return null;
    }

    if (state.clockRollbackDetected) {
      return 'security-check';
    }

    if (!state.registeredAt) {
      return 'register-required';
    }

    if (this.isTrialActive(entitlement, now, state.clockRollbackDetected)) {
      return null;
    }

    if (entitlement.trialConsumedAt) {
      return 'trial-expired';
    }

    return 'trial-required';
  }

  private canStartTrialInternal(state: AccessState, toolKey: ToolKey, now: number): boolean {
    const entitlement = state.entitlements[toolKey];

    if (!state.registeredAt || state.clockRollbackDetected || entitlement.subscribedAt) {
      return false;
    }

    if (entitlement.trialConsumedAt) {
      return false;
    }

    if (entitlement.trialAttemptedAt && now - entitlement.trialAttemptedAt < TRIAL_ATTEMPT_COOLDOWN_MS) {
      return false;
    }

    return true;
  }

  private isTrialActive(entitlement: ToolEntitlement, now: number, blockedByClockTamper: boolean): boolean {
    if (blockedByClockTamper) {
      return false;
    }

    if (!entitlement.trialExpiresAt) {
      return false;
    }

    if (entitlement.trialFingerprint && entitlement.trialFingerprint !== this.getDeviceFingerprint()) {
      return false;
    }

    return now < entitlement.trialExpiresAt;
  }

  private isGuestPreviewPath(guestPreviewPaths: string[], targetUrl: string): boolean {
    const path = this.normalizePath(targetUrl);
    return guestPreviewPaths.some(previewPath => {
      const normalizedPreviewPath = this.normalizePath(previewPath);
      if (normalizedPreviewPath.endsWith('/*')) {
        const prefix = normalizedPreviewPath.slice(0, -2);
        return path === prefix || path.startsWith(`${prefix}/`);
      }

      return path === normalizedPreviewPath;
    });
  }

  private normalizePath(url: string): string {
    const [pathOnly] = url.split('?');
    const withoutHash = pathOnly.split('#')[0] || '/';
    if (withoutHash.length > 1 && withoutHash.endsWith('/')) {
      return withoutHash.slice(0, -1);
    }
    return withoutHash;
  }

  private readState(): AccessState {
    const fallback = this.getDefaultState();

    if (typeof window === 'undefined') {
      return fallback;
    }

    const raw = window.localStorage.getItem(STORAGE_KEY);
    if (!raw) {
      this.writeState(fallback);
      return fallback;
    }

    try {
      const parsed = JSON.parse(raw) as Partial<AccessState>;
      const merged = this.mergeWithDefaults(parsed);
      return this.guardAgainstClockRollback(merged);
    } catch {
      this.writeState(fallback);
      return fallback;
    }
  }

  private writeState(state: AccessState): void {
    if (typeof window === 'undefined') {
      return;
    }

    const now = Date.now();
    state.lastSeenAt = now;
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
  }

  private guardAgainstClockRollback(state: AccessState): AccessState {
    const now = Date.now();
    if (state.lastSeenAt - now > MAX_CLOCK_ROLLBACK_MS) {
      state.clockRollbackDetected = true;
    }

    if (state.lastSeenAt < now) {
      state.lastSeenAt = now;
    }

    this.writeState(state);
    return state;
  }

  private mergeWithDefaults(parsed: Partial<AccessState>): AccessState {
    const defaults = this.getDefaultState();
    const entitlements =
      (parsed.entitlements as Partial<Record<ToolKey, ToolEntitlement>> | undefined) ?? {};

    return {
      registeredAt: parsed.registeredAt,
      lastSeenAt: typeof parsed.lastSeenAt === 'number' ? parsed.lastSeenAt : defaults.lastSeenAt,
      clockRollbackDetected: Boolean(parsed.clockRollbackDetected),
      entitlements: {
        citizenship: { ...defaults.entitlements.citizenship, ...(entitlements.citizenship ?? {}) },
        contractor: { ...defaults.entitlements.contractor, ...(entitlements.contractor ?? {}) },
        'dividend-calculator': {
          ...defaults.entitlements['dividend-calculator'],
          ...(entitlements['dividend-calculator'] ?? {}),
        },
      },
    };
  }

  private getDefaultState(): AccessState {
    const now = Date.now();
    return {
      lastSeenAt: now,
      clockRollbackDetected: false,
      entitlements: {
        citizenship: {},
        contractor: {},
        'dividend-calculator': {},
      },
    };
  }

  private getDeviceFingerprint(): string {
    if (typeof window === 'undefined') {
      return 'server';
    }

    const tz = Intl.DateTimeFormat().resolvedOptions().timeZone ?? 'unknown';
    const source = [navigator.userAgent, navigator.language, navigator.platform, tz].join('|');

    let hash = 0;
    for (let index = 0; index < source.length; index++) {
      hash = ((hash << 5) - hash + source.charCodeAt(index)) | 0;
    }

    return `fp-${Math.abs(hash)}`;
  }

  private mapApiSnapshot(
    toolKey: ToolKey,
    targetUrl: string,
    entitlements: ApiToolEntitlement[],
  ): AccessSnapshot {
    const entitlement = entitlements.find(item => item.toolKey === toolKey);
    if (!entitlement) {
      return this.getSnapshot(toolKey, targetUrl);
    }

    const policy = getToolPolicy(toolKey);
    const isGuestPreview = this.isGuestPreviewPath(policy.guestPreviewPaths, targetUrl);
    const trialEndsAt = entitlement.accessExpiresAt ? Date.parse(entitlement.accessExpiresAt) : undefined;

    return {
      toolKey,
      toolName: policy.displayName,
      isRegistered: true,
      isSubscribed: entitlement.subscribed,
      isGuestPreview,
      trialActive: entitlement.trialActive,
      trialExpired: entitlement.trialExpired,
      trialAvailable: entitlement.trialAvailable,
      trialEndsAt,
      blockingReason: isGuestPreview
        ? null
        : entitlement.hasAccess
          ? null
          : entitlement.trialExpired
            ? 'trial-expired'
            : 'trial-required',
    };
  }

  private applyRemoteTrial(toolKey: ToolKey, trialExpiresAtIso: string): void {
    const state = this.readState();
    const entitlement = state.entitlements[toolKey];
    const now = Date.now();

    entitlement.trialStartedAt = now;
    entitlement.trialExpiresAt = Date.parse(trialExpiresAtIso);
    entitlement.trialConsumedAt = now;
    entitlement.trialFingerprint = this.getDeviceFingerprint();

    this.writeState(state);
  }

  private getAuthToken(): string | null {
    if (typeof window === 'undefined') {
      return null;
    }

    const knownKeys = ['ww-access-token', 'accessToken', 'token'];
    for (const key of knownKeys) {
      const token = window.localStorage.getItem(key);
      if (token) {
        return token;
      }
    }

    return null;
  }

  private getAuthHeaders(token: string): HttpHeaders {
    return new HttpHeaders({ Authorization: `Bearer ${token}` });
  }
}



