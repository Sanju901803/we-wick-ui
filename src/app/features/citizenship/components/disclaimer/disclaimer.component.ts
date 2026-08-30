import { Component } from '@angular/core';

@Component({
  selector: 'app-citizenship-disclaimer',
  standalone: true,
  template: `
    <div class="container py-4 py-md-5">
      <div class="row justify-content-center">
        <div class="col-lg-9 col-xl-8">
          <div class="card border-0 shadow-sm">
            <div class="card-body p-4 p-md-5">
              <h1 class="h3 fw-bold mb-3">Citizenship Study Disclaimer</h1>
              <p class="text-muted mb-3">
                This tool is designed to help with your preparation for the Canadian citizenship test,
                and we work to keep it up to date.
              </p>
              <p class="mb-3">
                Please do not rely only on this tool. Use the official Government of Canada study
                guide as your primary source of truth.
              </p>
              <div class="alert alert-secondary py-3 px-3 mb-4" style="line-height:1.8;">
                The illustrations in this study tool are AI-generated visual depictions created for
                learning and memory support. They are not original historical photographs, official
                Government of Canada images, or exact reconstructions of historical events. Please
                use the official Discover Canada study guide as the authoritative source for
                citizenship test preparation.
              </div>

              <a
                class="btn btn-primary fw-semibold"
                href="https://www.canada.ca/en/immigration-refugees-citizenship/corporate/publications-manuals/discover-canada.html"
                target="_blank"
                rel="noopener noreferrer"
              >
                Open Official Study Guide
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  `
})
export class DisclaimerComponent {}
