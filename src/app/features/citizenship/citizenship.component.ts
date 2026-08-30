import { Component } from '@angular/core';
import { NgIf } from '@angular/common';
import { Router, RouterOutlet, RouterLink, RouterLinkActive } from '@angular/router';
import { IconComponent } from '../../shared/components/icon/icon.component';

@Component({
  selector: 'app-citizenship',
  standalone: true,
  imports: [NgIf, RouterOutlet, RouterLink, RouterLinkActive, IconComponent],
  templateUrl: './citizenship.component.html',
})
export class CitizenshipComponent {
  constructor(private readonly router: Router) {}

  isActive(path: string): boolean {
    return this.router.url.startsWith(path);
  }

  isLocked(path: string): boolean {
    return false;
  }
}
