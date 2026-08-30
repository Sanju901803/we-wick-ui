export type ToolKey = 'citizenship' | 'contractor' | 'dividend-calculator';

export interface ToolAccessPolicy {
  toolKey: ToolKey;
  displayName: string;
  guestPreviewPaths: string[];
  trialDurationMs: number;
}

export interface ToolEntitlement {
  trialStartedAt?: number;
  trialExpiresAt?: number;
  trialConsumedAt?: number;
  trialFingerprint?: string;
  trialAttemptedAt?: number;
  subscribedAt?: number;
}

export interface AccessState {
  registeredAt?: number;
  lastSeenAt: number;
  clockRollbackDetected: boolean;
  entitlements: Record<ToolKey, ToolEntitlement>;
}

export type BlockingReason =
  | 'register-required'
  | 'trial-required'
  | 'trial-expired'
  | 'security-check';

export interface AccessSnapshot {
  toolKey: ToolKey;
  toolName: string;
  isRegistered: boolean;
  isSubscribed: boolean;
  isGuestPreview: boolean;
  trialActive: boolean;
  trialExpired: boolean;
  trialAvailable: boolean;
  trialEndsAt?: number;
  blockingReason: BlockingReason | null;
}

export interface TrialStartResult {
  success: boolean;
  message: string;
}

