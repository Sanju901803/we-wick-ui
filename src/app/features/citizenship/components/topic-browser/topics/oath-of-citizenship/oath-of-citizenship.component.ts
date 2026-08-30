import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ImageClickDirective } from '../../../../../../shared/directives/image-click.directive';

@Component({
  selector: 'app-oath-of-citizenship',
  standalone: true,
  imports: [CommonModule, ImageClickDirective],
  templateUrl: './oath-of-citizenship.component.html',
  styles: [
    `
      .oath-text {
        line-height: 1.8;
        font-size: 1.02rem;
        text-align: center;
      }

      .oath-divider {
        width: 1px;
        height: 120px;
        background: var(--bs-border-color);
      }
    `
  ]
})
export class OathOfCitizenshipComponent {
  readonly title = 'Oath of Citizenship';
  readonly officialSectionUrl =
    'https://www.canada.ca/en/immigration-refugees-citizenship/corporate/publications-manuals/discover-canada/read-online/oath-citizenship.html';

  readonly contentBlocks = [
    {
      text: 'In Canada, we profess our loyalty to a person who represents all Canadians — not to a document such as a constitution, a banner such as a flag, or a geopolitical entity such as a country.',
      src: 'assets/images/oath-of-citizenship/ChatGPT%20Image%20May%202%2C%202026%2C%2001_04_50%20AM%20%281%29.png',
      alt: 'Loyalty to the Sovereign',
      caption: 'Loyalty to a person who represents all Canadians',
      layout: 'stacked' as const
    },
    {
      text: 'In our constitutional monarchy, these elements are all encompassed by the Sovereign (Queen or King).',
      src: 'assets/images/oath-of-citizenship/ChatGPT%20Image%20May%202%2C%202026%2C%2001_04_50%20AM%20%282%29.png',
      alt: "Canada's Constitutional Monarchy",
      caption: "Canada's Constitutional Monarchy",
      layout: 'side-by-side' as const,
      imageOnRight: true
    },
    {
      text: 'It is a remarkably simple yet powerful principle.',
      src: 'assets/images/oath-of-citizenship/ChatGPT%20Image%20May%202%2C%202026%2C%2001_04_51%20AM%20%283%29.png',
      alt: 'More Than Symbols',
      caption: 'More than flags, documents, or borders',
      layout: 'side-by-side' as const,
      imageOnRight: false
    },
    {
      text: 'Canada is personified by the Sovereign just as the Sovereign is personified by Canada.',
      src: 'assets/images/oath-of-citizenship/ChatGPT%20Image%20May%202%2C%202026%2C%2001_04_51%20AM%20%284%29.png',
      alt: 'Canada and the Sovereign',
      caption: 'Canada and the Sovereign — each symbolizes the other',
      layout: 'side-by-side' as const,
      imageOnRight: true
    }
  ];
}
