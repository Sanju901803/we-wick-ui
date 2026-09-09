import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';
import { IconComponent } from '../../../../shared/components/icon/icon.component';
import { IconKey } from '../../../../shared/icons/icon-registry';
import { QuestionService } from '../../../../core/services/question.service';
import { TopicSummary } from '../../../../core/models';

const TOPIC_ROUTES: Record<string, string> = {
  'Applying for Citizenship':                   'applying-for-citizenship',
  'Oath of Citizenship':                        'oath-of-citizenship',
  'Rights and Responsibilities of Citizenship': 'rights-and-responsibilities',
  'Who We Are':                                 'who-we-are',
  "Canada's History":                           'canadas-history',
  'Modern Canada':                              'modern-canada',
  'How Canadians Govern Themselves':            'how-canadians-govern-themselves',
  'Federal Elections':                          'federal-elections',
  'The Justice System':                         'the-justice-system',
  'Canadian Symbols':                           'canadian-symbols',
  "Canada's Economy":                           'canadas-economy',
  "Canada's Regions":                           'canadas-regions',
};

@Component({
  selector: 'app-topic-browser',
  standalone: true,
  imports: [CommonModule, RouterLink, RouterLinkActive, RouterOutlet, IconComponent],
  templateUrl: './topic-browser.component.html',
})
export class TopicBrowserComponent implements OnInit {
  topics: TopicSummary[] = [];

  @ViewChild('topicNavList') topicNavList?: ElementRef<HTMLDivElement>;

  constructor(private questionService: QuestionService) {}

  ngOnInit(): void {
    this.questionService.getTopics().subscribe(t => {
      this.topics = t;
    });
  }

  getRoute(topicName: string): string {
    return TOPIC_ROUTES[topicName] ?? '';
  }

  asIconKey(key: string): IconKey {
    return key as IconKey;
  }

  /** Scrolls the mobile horizontal topic strip left/right by roughly one item's width. */
  scrollTopics(direction: -1 | 1): void {
    const el = this.topicNavList?.nativeElement;
    if (!el) {
      return;
    }
    el.scrollBy({ left: direction * 160, behavior: 'smooth' });
  }
}
