import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ImageClickDirective } from '@app/shared/directives/image-click.directive';

@Component({
  selector: 'app-how-canadians-govern-themselves',
  standalone: true,
  imports: [CommonModule, ImageClickDirective],
  templateUrl: './how-canadians-govern-themselves.component.html',
})
export class HowCanadiansGovernThemselvesComponent {
  readonly title = 'How Canadians Govern Themselves';
  readonly officialSectionUrl =
    'https://www.canada.ca/en/immigration-refugees-citizenship/corporate/publications-manuals/discover-canada/read-online/how-canadians-govern-themselves.html';

  readonly pages = [
    { number: 1, label: 'Federal State' },
    { number: 2, label: 'Parliamentary Democracy' },
    { number: 3, label: 'Constitutional Monarchy' },
    { number: 4, label: "Canada's System of Government" },
  ];

  currentPage = 1;

  goToPage(page: number): void {
    this.currentPage = page;
  }
}
