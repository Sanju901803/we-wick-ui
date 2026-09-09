import { Component, ElementRef, ViewChild } from '@angular/core';
import { RouterOutlet, RouterLink, RouterLinkActive } from '@angular/router';

/** Sub-navigation shell for the "Fulltime" main tab's three child pages. */
@Component({
  selector: 'app-fulltime-main',
  standalone: true,
  imports: [RouterOutlet, RouterLink, RouterLinkActive],
  templateUrl: './fulltime-main.component.html',
})
export class FulltimeMainComponent {
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

