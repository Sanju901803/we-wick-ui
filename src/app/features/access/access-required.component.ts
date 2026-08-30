import { CommonModule, DatePipe } from '@angular/common';
import { Component, DestroyRef, OnInit, inject } from '@angular/core';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';
import { ToolKey } from '../../core/access/access.models';
import { getToolPolicy } from '../../core/access/access-policy';
import { AccessControlService } from '../../core/services/access-control.service';

@Component({
  selector: 'app-access-required',
  standalone: true,
  imports: [CommonModule, RouterLink, DatePipe],
  template: `
    <div class="container py-5">
      <div class="row justify-content-center">
        <div class="col-lg-7">
          <div class="card border-0 shadow-sm">
            <div class="card-body p-4 p-md-5">
              <p class="small text-uppercase text-muted mb-2">Access Control</p>
              <h1 class="h3 fw-bold mb-3">Unlock {{ toolName }}</h1>
              <p class="text-muted mb-4">
                This section is locked. Register first, then activate your free 1-day trial.
                For continuous access, subscribe to the tool.
              </p>

              <div class="alert alert-secondary" *ngIf="snapshot.trialActive && snapshot.trialEndsAt">
                Trial is active until {{ snapshot.trialEndsAt | date : 'medium' }}.
              </div>

              <div class="alert alert-warning" *ngIf="blockingReasonText">
                {{ blockingReasonText }}
              </div>

              <div class="d-grid gap-2 d-md-flex">
                <button
                  class="btn btn-primary"
                  type="button"
                  (click)="register()"
                  [disabled]="snapshot.isRegistered"
                >
                  {{ snapshot.isRegistered ? 'Registered' : 'Register' }}
                </button>

                <button
                  class="btn btn-outline-primary"
                  type="button"
                  (click)="startTrial()"
                  [disabled]="!snapshot.trialAvailable"
                >
                  Start Free Day
                </button>

                <button class="btn btn-success" type="button" (click)="subscribe()">
                  Subscribe
                </button>
              </div>

              <p class="small text-muted mt-3 mb-0">
                Anti-abuse safeguards are enabled: one trial per tool, clock rollback detection,
                and attempt throttling. Server-side enforcement is still required in production.
              </p>

              <div class="mt-4 d-flex gap-2">
                <button class="btn btn-dark" type="button" (click)="continueToTarget()">
                  Continue to Requested Page
                </button>
                <a class="btn btn-link" routerLink="/">Back to Home</a>
              </div>

              <p *ngIf="feedback" class="small mt-3 mb-0" [class.text-success]="feedbackIsSuccess" [class.text-danger]="!feedbackIsSuccess">
                {{ feedback }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  `,
})
export class AccessRequiredComponent implements OnInit {
  private readonly route = inject(ActivatedRoute);
  private readonly router = inject(Router);
  private readonly accessControlService = inject(AccessControlService);
  private readonly destroyRef = inject(DestroyRef);

  toolKey: ToolKey = 'citizenship';
  toolName = getToolPolicy('citizenship').displayName;
  targetUrl = '/';

  blockingReasonText = '';
  feedback = '';
  feedbackIsSuccess = false;

  snapshot = this.accessControlService.getSnapshot(this.toolKey, this.targetUrl);

  ngOnInit(): void {
    this.route.queryParamMap.pipe(takeUntilDestroyed(this.destroyRef)).subscribe(params => {
      const requestedTool = params.get('tool');
      this.toolKey = this.asToolKey(requestedTool) ?? 'citizenship';
      this.toolName = getToolPolicy(this.toolKey).displayName;

      const requestedTarget = params.get('target');
      this.targetUrl = requestedTarget?.startsWith('/') ? requestedTarget : '/';
      this.blockingReasonText = this.getReasonText(params.get('reason'));
      this.refreshSnapshot();
    });
  }

  register(): void {
    this.accessControlService.markRegistered();
    this.feedback = 'Registration complete. You can now start your free day.';
    this.feedbackIsSuccess = true;
    this.refreshSnapshot();
  }

  startTrial(): void {
    this.accessControlService
      .startTrial$(this.toolKey)
      .pipe(takeUntilDestroyed(this.destroyRef))
      .subscribe(result => {
        this.feedback = result.message;
        this.feedbackIsSuccess = result.success;
        this.refreshSnapshot();

        if (result.success) {
          void this.router.navigateByUrl(this.targetUrl);
        }
      });
  }

  subscribe(): void {
    this.accessControlService.subscribe(this.toolKey);
    this.feedback = 'Subscription activated for this tool.';
    this.feedbackIsSuccess = true;
    this.refreshSnapshot();
    void this.router.navigateByUrl(this.targetUrl);
  }

  continueToTarget(): void {
    void this.router.navigateByUrl(this.targetUrl);
  }

  private refreshSnapshot(): void {
    this.accessControlService
      .getSnapshot$(this.toolKey, this.targetUrl)
      .pipe(takeUntilDestroyed(this.destroyRef))
      .subscribe(snapshot => {
        this.snapshot = snapshot;
      });
  }

  private getReasonText(reason: string | null): string {
    switch (reason) {
      case 'register-required':
        return 'Please register to unlock the free 1-day trial.';
      case 'trial-required':
        return 'Start your free 1-day trial to continue.';
      case 'trial-expired':
        return 'Your free trial has ended. Subscribe for uninterrupted access.';
      case 'security-check':
        return 'A security check is required before trial access can continue.';
      default:
        return '';
    }
  }

  private asToolKey(value: string | null): ToolKey | null {
    if (value === 'citizenship' || value === 'contractor' || value === 'dividend-calculator') {
      return value;
    }
    return null;
  }
}


