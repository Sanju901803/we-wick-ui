import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

interface StudySection {
  title: string;
  points: string[];
}

@Component({
  selector: 'app-applying-for-citizenship',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './applying-for-citizenship.component.html',
})
export class ApplyingForCitizenshipComponent {
  readonly title = 'Applying for Citizenship';
  readonly sections: StudySection[] = [
    {
      title: 'About the Citizenship Test',
      points: [
        'The test is usually for applicants aged 18 to 54. Applicants outside this age range are generally not required to write the test.',
        'You are tested on Canada\'s history, values, institutions, symbols, and rights and responsibilities of citizenship.',
        'The test is usually 20 questions. You need at least 15 correct answers to pass (75%).',
        'Questions can be multiple choice and true/false, and the test is usually completed in about 30 minutes.',
        'You can take the test in English or French. Bring the documents listed in your invitation and review official study materials before test day.'
      ]
    },
    {
      title: 'After the Test',
      points: [
        'After your test, IRCC reviews your result and your application details before making a final decision.',
        'If additional information is needed, you may be contacted for follow-up steps.',
        'If approved, you will receive an invitation to attend a citizenship ceremony.',
        'At the ceremony, you take the Oath of Citizenship and officially become a Canadian citizen.',
        'After taking the oath, you receive your citizenship certificate. Use official IRCC updates for timelines and next actions.'
      ]
    }
  ];

  readonly officialSectionUrl =
    'https://www.canada.ca/en/immigration-refugees-citizenship/corporate/publications-manuals/discover-canada/read-online/applying-citizenship.html';
}
