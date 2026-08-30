import { Injectable, signal } from '@angular/core';

export interface ImageModalState {
  src: string;
  alt: string;
}

@Injectable({ providedIn: 'root' })
export class ImageModalService {
  readonly state = signal<ImageModalState | null>(null);

  open(src: string, alt: string): void {
    this.state.set({ src, alt });
  }

  close(): void {
    this.state.set(null);
  }
}
