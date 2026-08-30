import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ImageClickDirective } from '@app/shared/directives/image-click.directive';

@Component({
  selector: 'app-the-justice-system',
  standalone: true,
  imports: [CommonModule, ImageClickDirective],
  templateUrl: './the-justice-system.component.html',
})
export class TheJusticeSystemComponent {
  readonly title = 'The Justice System';
  readonly officialSectionUrl =
    'https://www.canada.ca/en/immigration-refugees-citizenship/corporate/publications-manuals/discover-canada/read-online/justice-system.html';
}
