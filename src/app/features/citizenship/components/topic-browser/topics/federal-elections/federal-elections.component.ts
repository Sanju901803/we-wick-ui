import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ImageClickDirective } from '@app/shared/directives/image-click.directive';

@Component({
  selector: 'app-federal-elections',
  standalone: true,
  imports: [CommonModule, ImageClickDirective],
  templateUrl: './federal-elections.component.html',
})
export class FederalElectionsComponent {
  readonly title = 'Federal Elections';
  readonly officialSectionUrl =
    'https://www.canada.ca/en/immigration-refugees-citizenship/corporate/publications-manuals/discover-canada/read-online/federal-elections.html';

  readonly pages = [
    { number: 1, label: 'How Elections Work' },
    { number: 2, label: 'Voting' },
    { number: 3, label: 'After an Election' },
    { number: 4, label: 'Other Levels of Government in Canada' },
    { number: 5, label: 'How Much Do You Know About Your Government?' },
  ];

  currentPage = 1;

  goToPage(page: number): void {
    this.currentPage = page;
  }
}
