import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-contractor',
  standalone: true,
  imports: [RouterLink],
  template: `
    <div class="container py-5">
      <div class="row justify-content-center">
        <div class="col-md-8 text-center">
          <div class="card shadow-sm border-0 p-5">
            <div class="mb-4" style="font-size: 4rem;">💼</div>
            <h1 class="display-5 fw-bold mb-3">Contractor vs Full-Timer Pay Compare</h1>
            <p class="lead text-muted mb-4">
              This tool will help you compare the true take-home value of a contractor (T4A) role
              versus a full-time employee (T4) role in Canada — factoring in taxes, benefits,
              vacation, CPP, EI, and more.
            </p>
            <div class="row g-3 mb-4 text-start">
              <div class="col-sm-6">
                <div class="p-3 bg-light rounded">
                  <h6 class="fw-bold">🔢 Planned Features</h6>
                  <ul class="mb-0 small text-muted">
                    <li>Hourly/annual rate inputs</li>
                    <li>Province-based tax calculation</li>
                    <li>Benefits value estimator</li>
                    <li>RRSP & CPP impact</li>
                    <li>Side-by-side comparison</li>
                  </ul>
                </div>
              </div>
              <div class="col-sm-6">
                <div class="p-3 bg-light rounded">
                  <h6 class="fw-bold">📊 Output</h6>
                  <ul class="mb-0 small text-muted">
                    <li>Net annual income both paths</li>
                    <li>Break-even rate calculator</li>
                    <li>Visual comparison chart</li>
                    <li>Shareable summary</li>
                  </ul>
                </div>
              </div>
            </div>
            <div class="alert alert-warning d-inline-block">
              🚧 Coming Soon — Currently building the Citizenship Exam tool first.
            </div>
          </div>
        </div>
      </div>
    </div>
  `
})
export class ContractorComponent {}
