import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ImageClickDirective } from '../../../../../../shared/directives/image-click.directive';

@Component({
  selector: 'app-who-we-are',
  standalone: true,
  imports: [CommonModule, ImageClickDirective],
  templateUrl: './who-we-are.component.html',
})
export class WhoWeAreComponent {
  readonly title = 'Who We Are';
  readonly officialSectionUrl =
    'https://www.canada.ca/en/immigration-refugees-citizenship/corporate/publications-manuals/discover-canada/read-online/who-are-canadians.html';

  readonly pages = [
    { number: 1, label: 'Introduction' },
    { number: 2, label: 'Aboriginal Peoples' },
    { number: 3, label: 'English and French' },
    { number: 4, label: 'Diversity in Canada' },
  ];

  currentPage = 1;

  readonly aboriginalGroups = [
    {
      id: 'first-nations',
      label: 'First Nations',
      description: 'Indian refers to all Aboriginal people who are not Inuit or Métis. In the 1970s, the term First Nations began to be used. Today, about half of First Nations people live on reserve land in about 600 communities while the other half live off-reserve, mainly in urban centres.',
      image: 'assets/images/who-we-are/first-nations.png',
      imageAlt: 'First Nations peoples of Canada',
    },
    {
      id: 'inuit',
      label: 'Inuit',
      description: 'The Inuit, which means "the people" in the Inuktitut language, live in small, scattered communities across the Arctic. Their knowledge of the land, sea and wildlife enabled them to adapt to one of the harshest environments on earth.',
      image: 'assets/images/who-we-are/inuit.png',
      imageAlt: 'Inuit peoples of the Canadian Arctic',
    },
    {
      id: 'metis',
      label: 'Métis',
      description: 'The Métis are a distinct people of mixed Aboriginal and European ancestry, the majority of whom live in the Prairie provinces. They come from both French- and English-speaking backgrounds and speak their own dialect, Michif.',
      image: 'assets/images/who-we-are/metis.png',
      imageAlt: 'Métis peoples of Canada',
    },
  ];

  expandedGroups = new Set<string>();

  toggleGroup(id: string): void {
    if (this.expandedGroups.has(id)) {
      this.expandedGroups.delete(id);
    } else {
      this.expandedGroups.add(id);
    }
  }

  expandAll(): void {
    this.aboriginalGroups.forEach(g => this.expandedGroups.add(g.id));
  }

  collapseAll(): void {
    this.expandedGroups.clear();
  }

  isExpanded(id: string): boolean {
    return this.expandedGroups.has(id);
  }

  goToPage(page: number): void {
    this.currentPage = page;
  }
}
