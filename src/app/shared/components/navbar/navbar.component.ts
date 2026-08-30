import { Component } from '@angular/core';
import { RouterLink, RouterLinkActive } from '@angular/router';
import { NgbCollapseModule } from '@ng-bootstrap/ng-bootstrap';
import { IconComponent } from '../../../shared/components/icon/icon.component';

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [RouterLink, RouterLinkActive, NgbCollapseModule, IconComponent],
  templateUrl: './navbar.component.html',
})
export class NavbarComponent {
  isCollapsed = true;
}
