import { Component, HostListener, inject } from '@angular/core';
import { ImageModalService } from '../../services/image-modal.service';

@Component({
  selector: 'app-image-modal',
  standalone: true,
  template: `
    @if (modal.state(); as img) {
      <div
        class="ww-lightbox-backdrop"
        (click)="modal.close()"
        role="dialog"
        aria-modal="true"
        [attr.aria-label]="img.alt || 'Image preview'"
      >
        <div class="ww-lightbox-content" (click)="$event.stopPropagation()">
          <button
            class="ww-lightbox-close"
            (click)="modal.close()"
            aria-label="Close image preview"
            type="button"
          >
            &times;
          </button>
          <img
            [src]="img.src"
            [alt]="img.alt"
            class="ww-lightbox-img"
          />
          @if (img.alt) {
            <p class="ww-lightbox-caption">{{ img.alt }}</p>
          }
        </div>
      </div>
    }
  `,
  styles: [`
    .ww-lightbox-backdrop {
      position: fixed;
      inset: 0;
      z-index: 1080;
      background: rgba(0, 0, 0, 0.82);
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1rem;
      animation: ww-fade-in 0.18s ease;
    }

    @keyframes ww-fade-in {
      from { opacity: 0; }
      to   { opacity: 1; }
    }

    .ww-lightbox-content {
      position: relative;
      max-width: min(90vw, 900px);
      max-height: 90vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      border-radius: 0.5rem;
      overflow: hidden;
      background: #1a1a1a;
      box-shadow: 0 8px 40px rgba(0, 0, 0, 0.6);
    }

    .ww-lightbox-img {
      display: block;
      max-width: 100%;
      max-height: calc(90vh - 4rem);
      object-fit: contain;
    }

    .ww-lightbox-close {
      position: absolute;
      top: 0.5rem;
      right: 0.5rem;
      z-index: 1;
      background: rgba(0, 0, 0, 0.55);
      color: #fff;
      border: none;
      border-radius: 50%;
      width: 2rem;
      height: 2rem;
      font-size: 1.25rem;
      line-height: 1;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: background 0.15s;

      &:hover {
        background: var(--ww-primary, #356861);
      }
    }

    .ww-lightbox-caption {
      margin: 0;
      padding: 0.5rem 1rem;
      font-size: 0.85rem;
      color: #ccc;
      text-align: center;
      background: #1a1a1a;
      width: 100%;
    }
  `]
})
export class ImageModalComponent {
  readonly modal = inject(ImageModalService);

  @HostListener('document:keydown.escape')
  onEscape(): void {
    this.modal.close();
  }
}
