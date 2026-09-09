import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { CommonModule } from '@angular/common';

interface Tool {
  title: string;
  description: string;
  icon: string;
  route: string;
  status: 'live' | 'coming-soon';
  badge?: string;
  gated?: boolean;
  highlights: string[];
  color: string;
}

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, RouterLink],
  template: `
    <div class="container py-5">

      <!-- Hero -->
      <div class="text-center mb-5">
        <div style="font-size:3rem">🍁</div>
        <h1 class="display-5 fw-bold mt-2">We-Wick Tools</h1>
        <p class="lead text-muted">A growing collection of practical tools for Canadians.</p>
      </div>

      <!-- Tools Grid -->
      <div class="row g-4 justify-content-center">
        <div class="col-md-6 col-lg-4" *ngFor="let tool of tools">
          <div class="card h-100 border-0 shadow-sm tool-card position-relative overflow-hidden"
            [class.opacity-75]="tool.status === 'coming-soon'">

            <!-- Top color bar -->
            <div class="card-color-bar" [style.background]="tool.color"></div>

            <div class="card-body p-4">
              <div class="d-flex align-items-start justify-content-between mb-3">
                <span style="font-size:2.5rem">{{tool.icon}}</span>
                <span *ngIf="tool.status === 'live'"
                  class="badge bg-success-subtle text-success border border-success-subtle">
                  Live
                </span>
                <span *ngIf="tool.status === 'coming-soon'"
                  class="badge bg-warning-subtle text-warning border border-warning-subtle">
                  Coming Soon
                </span>
              </div>

              <h4 class="fw-bold mb-1">{{tool.title}}</h4>
              <p class="text-muted small mb-3">{{tool.description}}</p>

              <ul class="list-unstyled mb-4">
                <li class="small text-muted mb-1" *ngFor="let h of tool.highlights">
                  <span class="me-2">›</span>{{h}}
                </li>
              </ul>

              <a *ngIf="tool.status === 'live'"
                [routerLink]="tool.route"
                class="btn btn-sm w-100 fw-semibold"
                [style.background]="tool.color"
                style="color:#fff; border:none">
                Open Tool →
              </a>
              <button *ngIf="tool.status === 'coming-soon'"
                class="btn btn-sm btn-outline-secondary w-100" disabled>
                Coming Soon
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Footer note -->
      <p class="text-center text-muted small mt-5">
        More tools on the way. Suggestions? Just ask! 🛠️
      </p>
    </div>
  `,
  styles: [`
    .tool-card {
      transition: transform 0.2s, box-shadow 0.2s;
      cursor: default;
    }
    .tool-card:hover {
      transform: translateY(-5px);
      box-shadow: 0 12px 32px rgba(0,0,0,0.12) !important;
    }
    .card-color-bar {
      height: 5px;
      width: 100%;
    }
  `]
})
export class HomeComponent {
  tools: Tool[] = [
    {
      title: 'Canada Citizenship Exam',
      description: 'Prepare for the Canadian citizenship test with flashcards, quizzes, a timed mock exam, and progress tracking.',
      icon: '🇨🇦',
      route: '/citizenship',
      status: 'live',
      gated: false,
      color: '#3d7a6f',
      highlights: [
        'Topic-based study browser',
        'Interactive flip flashcards',
        'Configurable practice quiz',
        'Timed 45-min mock exam (pass at 75%)',
        'Bookmarks & progress dashboard'
      ]
    },
    {
      title: 'Contractor vs Full-Timer',
      description: 'Compare the true take-home value of a contractor (T4A) role vs a permanent employee (T4) role in Canada — plus payout, investment and tax reduction strategies for both.',
      icon: '💼',
      route: '/contractor',
      status: 'live',
      gated: false,
      color: '#c8832a',
      highlights: [
        'Contractor ↔ Full-Time net pay comparison',
        'Corporate taxes & deductible expenses',
        'Personal taxes & deductions (T4)',
        'Payout & investment strategy for corporations',
        'RRSP/TFSA tax reduction strategy for employees'
      ]
    },
    {
      title: 'Dividend Calculator',
      description: 'Model your investment portfolio and see how much dividend income you could earn — play with multiple scenarios.',
      icon: '📈',
      route: '/dividend-calculator',
      status: 'coming-soon',
      color: '#7a9e8e',
      highlights: [
        'Enter holdings by ticker or manually',
        'Annual & monthly dividend income',
        'Scenario comparison (DRIP vs cash)',
        'Yield-on-cost tracking',
        'Portfolio growth projection'
      ]
    }
  ];
}
