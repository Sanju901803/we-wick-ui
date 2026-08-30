import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ImageClickDirective } from '@app/shared/directives/image-click.directive';

@Component({
  selector: 'app-canadas-economy',
  standalone: true,
  imports: [CommonModule, ImageClickDirective],
  templateUrl: './canadas-economy.component.html',
})
export class CanadasEconomyComponent {
  readonly title = "Canada's Economy";
  readonly officialSectionUrl =
    'https://www.canada.ca/en/immigration-refugees-citizenship/corporate/publications-manuals/discover-canada/read-online/canadas-economy.html';

  readonly pages = [
    { number: 1, label: 'A Trading Nation' },
    { number: 2, label: 'Three Industries & Trade with the USA' },
  ];

  currentPage = 1;

  goToPage(page: number): void {
    this.currentPage = page;
  }
}
