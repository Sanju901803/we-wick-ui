import { Directive, ElementRef, HostListener, inject } from '@angular/core';
import { ImageModalService } from '../services/image-modal.service';

@Directive({
  selector: 'img[appImageClick]',
  standalone: true,
  host: {
    style: 'cursor: pointer',
    '[attr.tabindex]': '0',
    '[attr.role]': '"button"',
  }
})
export class ImageClickDirective {
  private readonly modal = inject(ImageModalService);
  private readonly el = inject<ElementRef<HTMLImageElement>>(ElementRef);

  @HostListener('click')
  onClick(): void {
    const img = this.el.nativeElement;
    if (img.src) {
      this.modal.open(img.src, img.alt);
    }
  }

  @HostListener('keydown.enter')
  onEnter(): void {
    this.onClick();
  }
}
