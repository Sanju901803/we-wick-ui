import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ImageClickDirective } from '../../../../../../shared/directives/image-click.directive';

@Component({
  selector: 'app-rights-and-responsibilities',
  standalone: true,
  imports: [CommonModule, ImageClickDirective],
  templateUrl: './rights-and-responsibilities.component.html',
})
export class RightsAndResponsibilitiesComponent {
  readonly title = 'Rights and Responsibilities of Citizenship';
  readonly officialSectionUrl =
    'https://www.canada.ca/en/immigration-refugees-citizenship/corporate/publications-manuals/discover-canada/read-online/rights-resonsibilities-citizenship.html';

  readonly pages = [
    { number: 1, label: 'Rights of Citizenship' },
    { number: 2, label: 'Responsibilities of Citizenship' },
    { number: 3, label: 'The Equality of Women and Men' },
    { number: 4, label: 'Defending Canada' },
  ];

  currentPage = 1;

  readonly charteredRights = [
    {
      id: 'mobility',
      label: 'Mobility Rights',
      description: 'Canadians can live and work anywhere they choose in Canada, enter and leave the country freely, and apply for a passport.',
      image: 'assets/images/rights-and-responsibilities/mobility-rights.png',
      imageAlt: 'Mobility Rights — Canadians living and working freely',
    },
    {
      id: 'aboriginal',
      label: "Aboriginal Peoples' Rights",
      description: "The rights guaranteed in the Charter will not adversely affect any treaty or other rights or freedoms of Aboriginal peoples.",
      image: 'assets/images/rights-and-responsibilities/aboriginal-peoples-rights.png',
      imageAlt: "Aboriginal Peoples' Rights",
    },
    {
      id: 'language',
      label: 'Official Language Rights and Minority Language Educational Rights',
      description: 'French and English have equal status in Parliament and throughout the government.',
      image: 'assets/images/rights-and-responsibilities/official-language-rights.png',
      imageAlt: 'Official Language Rights and Minority Language Educational Rights',
    },
    {
      id: 'multiculturalism',
      label: 'Multiculturalism',
      description: "A fundamental characteristic of the Canadian heritage and identity. Canadians celebrate the gift of one another's presence and work hard to respect pluralism and live in harmony.",
      image: 'assets/images/rights-and-responsibilities/multiculturalism.png',
      imageAlt: 'Multiculturalism in Canada',
    },
  ];

  expandedRights = new Set<string>();

  readonly citizenshipResponsibilities = [
    {
      id: 'obeying-law',
      label: 'Obeying the law',
      description: "One of Canada's founding principles is the rule of law. Individuals and governments are regulated by laws and not by arbitrary actions. No person or group is above the law.",
      image: 'assets/images/rights-and-responsibilities/obeying-the-law.png',
      imageAlt: 'Obeying the law in Canada',
    },
    {
      id: 'responsibility-family',
      label: 'Taking responsibility for oneself and one\'s family',
      description: "Getting a job, taking care of one's family and working hard in keeping with one's abilities are important Canadian values. Work contributes to personal dignity and self-respect, and to Canada's prosperity.",
      image: 'assets/images/rights-and-responsibilities/responsibility-for-family.png',
      imageAlt: 'Taking responsibility for oneself and family',
    },
    {
      id: 'jury',
      label: 'Serving on a jury',
      description: 'When called to do so, you are legally required to serve. Serving on a jury is a privilege that makes the justice system work, as it depends on impartial juries made up of citizens.',
      image: 'assets/images/rights-and-responsibilities/serving-on-a-jury.png',
      imageAlt: 'Serving on a jury',
    },
    {
      id: 'voting',
      label: 'Voting in elections',
      description: 'The right to vote comes with a responsibility to vote in federal, provincial or territorial and local elections.',
      image: 'assets/images/rights-and-responsibilities/voting-in-elections.png',
      imageAlt: 'Voting in elections',
    },
    {
      id: 'helping-others',
      label: 'Helping others in the community',
      description: "Millions of volunteers freely donate their time to help others without pay — helping people in need, assisting at your child's school, volunteering at a food bank or other charity, or encouraging newcomers to integrate. Volunteering is an excellent way to gain useful skills and develop friends and contacts.",
      image: 'assets/images/rights-and-responsibilities/helping-others.png',
      imageAlt: 'Helping others in the community',
    },
    {
      id: 'heritage',
      label: 'Protecting and enjoying our heritage and environment',
      description: "Every citizen has a role to play in avoiding waste and pollution while protecting Canada's natural, cultural and architectural heritage for future generations.",
      image: 'assets/images/rights-and-responsibilities/protecting-heritage.png',
      imageAlt: 'Protecting Canadian heritage and environment',
    },
  ];

  expandedResponsibilities = new Set<string>();

  toggleRight(id: string): void {
    if (this.expandedRights.has(id)) {
      this.expandedRights.delete(id);
    } else {
      this.expandedRights.add(id);
    }
  }

  expandAll(): void {
    this.charteredRights.forEach(r => this.expandedRights.add(r.id));
  }

  collapseAll(): void {
    this.expandedRights.clear();
  }

  isExpanded(id: string): boolean {
    return this.expandedRights.has(id);
  }

  toggleResponsibility(id: string): void {
    if (this.expandedResponsibilities.has(id)) {
      this.expandedResponsibilities.delete(id);
    } else {
      this.expandedResponsibilities.add(id);
    }
  }

  expandAllResponsibilities(): void {
    this.citizenshipResponsibilities.forEach(r => this.expandedResponsibilities.add(r.id));
  }

  collapseAllResponsibilities(): void {
    this.expandedResponsibilities.clear();
  }

  isResponsibilityExpanded(id: string): boolean {
    return this.expandedResponsibilities.has(id);
  }

  goToPage(page: number): void {
    this.currentPage = page;
  }
}
