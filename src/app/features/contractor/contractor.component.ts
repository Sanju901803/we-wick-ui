import { Component } from '@angular/core';
import { NgIf } from '@angular/common';
import { Router, RouterOutlet, RouterLink, RouterLinkActive } from '@angular/router';

@Component({
  selector: 'app-contractor',
  standalone: true,
  imports: [NgIf, RouterOutlet, RouterLink, RouterLinkActive],
  templateUrl: './contractor.component.html',
})
export class ContractorComponent {
  constructor(private readonly router: Router) {}

  isActive(path: string): boolean {
    return this.router.url.startsWith(path);
  }
}
