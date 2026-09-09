import { Component, ElementRef, ViewChild } from '@angular/core';
import { RouterOutlet, RouterLink, RouterLinkActive } from '@angular/router';

/** Sub-navigation shell for the "Contractor" main tab's three child pages. */
@Component({
  selector: 'app-contractor-main',
  standalone: true,
  imports: [RouterOutlet, RouterLink, RouterLinkActive],
  templateUrl: './contractor-main.component.html',
})
export class ContractorMainComponent {
  @ViewChild('navList') navList?: ElementRef<HTMLDivElement>;

  /** Scrolls the mobile horizontal nav strip left/right by roughly one item's width. */
  scrollNav(direction: -1 | 1): void {
    const el = this.navList?.nativeElement;
    if (!el) {
      return;
    }
    el.scrollBy({ left: direction * 160, behavior: 'smooth' });
  }
}

