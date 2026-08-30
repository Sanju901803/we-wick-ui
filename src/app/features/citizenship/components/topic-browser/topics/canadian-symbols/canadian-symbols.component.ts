import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ImageClickDirective } from '@app/shared/directives/image-click.directive';

@Component({
  selector: 'app-canadian-symbols',
  standalone: true,
  imports: [CommonModule, ImageClickDirective],
  templateUrl: './canadian-symbols.component.html',
})
export class CanadianSymbolsComponent {
  readonly title = 'Canadian Symbols';
  readonly officialSectionUrl =
    'https://www.canada.ca/en/immigration-refugees-citizenship/corporate/publications-manuals/discover-canada/read-online/canadian-symbols.html';

  readonly pages = [
    { number: 1, label: 'Canadian Symbols' },
    { number: 2, label: "Canada's Official Languages and Anthems" },
      { number: 3, label: 'The Victoria Cross, The Order of Canada' },
    { number: 4, label: 'National Public Holidays and Other Important Dates' },
  ];

  currentPage = 1;

  goToPage(page: number): void {
    this.currentPage = page;
  }
}
