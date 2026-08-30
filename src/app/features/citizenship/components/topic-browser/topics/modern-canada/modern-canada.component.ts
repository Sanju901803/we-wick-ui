import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ImageClickDirective } from '@app/shared/directives/image-click.directive';

@Component({
  selector: 'app-modern-canada',
  standalone: true,
  imports: [CommonModule, ImageClickDirective],
  templateUrl: './modern-canada.component.html',
})
export class ModernCanadaComponent {
  readonly title = 'Modern Canada';
  readonly officialSectionUrl =
    'https://www.canada.ca/en/immigration-refugees-citizenship/corporate/publications-manuals/discover-canada/read-online/modern-canada.html';

  readonly pages = [
    { number: 1, label: 'Trade & Economic Growth' },
    { number: 2, label: 'International Engagement & Canada and Quebec' },
    { number: 3, label: 'A Changing Society' },
    { number: 4, label: 'Arts and Culture in Canada' },
    { number: 5, label: 'Great Canadian Discoveries and Inventions' },
  ];

  currentPage = 1;

  goToPage(page: number): void {
    this.currentPage = page;
  }
}
