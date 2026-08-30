import { Component, Input } from '@angular/core';

import { IconKey, iconPath } from '../../icons/icon-registry';

@Component({
  selector: 'app-icon',
  standalone: true,
  template: `
    <span
      class="ww-icon"
      [style.width.px]="size"
      [style.height.px]="size"
    >
      <img
        [src]="src"
        [alt]="alt"
        [style.width.px]="size"
        [style.height.px]="size"
        [style.display]="showFallback ? 'none' : 'block'"
        loading="lazy"
        decoding="async"
        (error)="onError()"
      />
      <span [style.display]="showFallback ? 'inline' : 'none'" aria-hidden="true">{{ fallbackEmoji }}</span>
    </span>
  `,
  styles: [
    `
      :host {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        line-height: 1;
      }

      .ww-icon {
        display: inline-flex;
        align-items: center;
        justify-content: center;
      }

      img {
        display: block;
        object-fit: contain;
      }
    `,
  ],
})
export class IconComponent {
  @Input() iconKey: IconKey = 'home';
  @Input() fallbackEmoji = '';
  @Input() size = 18;
  @Input() alt = '';

  showFallback = false;

  get src(): string {
    return iconPath(this.iconKey);
  }

  onError(): void {
    this.showFallback = true;
  }
}
