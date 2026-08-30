import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ImageClickDirective } from '@app/shared/directives/image-click.directive';

@Component({
  selector: 'app-canadas-regions',
  standalone: true,
  imports: [CommonModule, ImageClickDirective],
  templateUrl: './canadas-regions.component.html',
})
export class CanadasRegionsComponent {
  readonly title = "Canada's Regions";
  readonly officialSectionUrl =
    'https://www.canada.ca/en/immigration-refugees-citizenship/corporate/publications-manuals/discover-canada/read-online/canadas-regions.html';

  readonly pages = [
    { number: 1, label: 'The Regions of Canada, Provinces and Territories' },
    { number: 2, label: 'The National Capital, Population' },
    { number: 3, label: 'The Atlantic Provinces' },
    { number: 4, label: 'Central Canada' },
    { number: 5, label: 'The Prairie Provinces' },
    { number: 6, label: 'West Coast' },
    { number: 7, label: 'The Northern Territories' },
  ];

  currentPage = 1;

  goToPage(page: number): void {
    this.currentPage = page;
  }
}
