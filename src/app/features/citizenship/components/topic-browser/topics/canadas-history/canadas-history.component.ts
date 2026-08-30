import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ImageClickDirective } from '@app/shared/directives/image-click.directive';

@Component({
  selector: 'app-canadas-history',
  standalone: true,
  imports: [CommonModule, ImageClickDirective],
  templateUrl: './canadas-history.component.html',
})
export class CanadasHistoryComponent {
  readonly title = "Canada's History";
  readonly officialSectionUrl =
    'https://www.canada.ca/en/immigration-refugees-citizenship/corporate/publications-manuals/discover-canada/read-online/canadas-history.html';

  readonly pages = [
    { number: 1, label: 'Aboriginal Peoples & First Europeans',          timeline: '~1000 AD – 1542' },
    { number: 2, label: 'New France & Struggle for a Continent',         timeline: '1604 – 1783' },
    { number: 3, label: 'United Empire Loyalists & Abolition of Slavery', timeline: '1776 – 1833' },
    { number: 4, label: 'The Fight for Canada & A Growing Economy',       timeline: '1812 – 1832' },
    { number: 5, label: 'Rebellions & Governance',                        timeline: '1830 – 1867' },
    { number: 6, label: 'Moving Westward',                               timeline: '1837 – 1905' },
    { number: 7, label: 'The First World War',                           timeline: '1914 – 1921' },
    { number: 8, label: 'Between the Wars',                              timeline: '1922 – 1939' },
    { number: 9, label: 'The Second World War',                          timeline: '1939 – 1945' },
  ];

  currentPage = 1;

  goToPage(page: number): void {
    this.currentPage = page;
  }
}
