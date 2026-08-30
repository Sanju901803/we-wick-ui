import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { NavbarComponent } from './shared/components/navbar/navbar.component';
import { ImageModalComponent } from './shared/components/image-modal/image-modal.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, NavbarComponent, ImageModalComponent],
  template: `
    <app-navbar></app-navbar>
    <main>
      <router-outlet></router-outlet>
    </main>
    <app-image-modal />
  `,
  styles: [`main { min-height: calc(100vh - 56px); }`]
})
export class AppComponent {
  title = 'we-wick-tools';
}
