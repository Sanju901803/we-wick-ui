import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, map } from 'rxjs';
import { Question, TopicSummary } from '../models';

@Injectable({ providedIn: 'root' })
export class QuestionService {
  private readonly dataUrl = 'assets/data/questions.json';

  constructor(private http: HttpClient) {}

  getAll(): Observable<Question[]> {
    return this.http.get<Question[]>(this.dataUrl);
  }

  getByTopic(topic: string): Observable<Question[]> {
    return this.getAll().pipe(
      map(qs => qs.filter(q => q.topic === topic))
    );
  }

  getTopics(): Observable<TopicSummary[]> {
    const ALL_SECTIONS: { name: string; icon: string; iconKey: string }[] = [
      { name: 'Applying for Citizenship',                   icon: '📋', iconKey: 'applyingForCitizenship' },
      { name: 'Oath of Citizenship',                        icon: '🤝', iconKey: 'oathOfCitizenship' },
      { name: 'Rights and Responsibilities of Citizenship', icon: '⚖️', iconKey: 'rightsAndResponsibilities' },
      { name: 'Who We Are',                                 icon: '🧭', iconKey: 'whoWeAre' },
      { name: "Canada's History",                           icon: '🍁', iconKey: 'canadasHistory' },
      { name: 'Modern Canada',                              icon: '🏙️', iconKey: 'modernCanada' },
      { name: 'How Canadians Govern Themselves',            icon: '🏛️', iconKey: 'governance' },
      { name: 'Federal Elections',                          icon: '🗳️', iconKey: 'federalElections' },
      { name: 'The Justice System',                         icon: '🔨', iconKey: 'justiceSystem' },
      { name: 'Canadian Symbols',                           icon: '🇨🇦', iconKey: 'canadianSymbols' },
      { name: "Canada's Economy",                           icon: '💼', iconKey: 'canadasEconomy' },
      { name: "Canada's Regions",                           icon: '🗺️', iconKey: 'canadasRegions' },
    ];

    return this.getAll().pipe(
      map(qs => {
        const counts: Record<string, number> = {};
        qs.forEach(q => { counts[q.topic] = (counts[q.topic] || 0) + 1; });
        return ALL_SECTIONS.map(s => ({
          name: s.name,
          icon: s.icon,
          iconKey: s.iconKey,
          count: counts[s.name] || 0
        }));
      })
    );
  }

  shuffle<T>(arr: T[]): T[] {
    const copy = [...arr];
    for (let i = copy.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [copy[i], copy[j]] = [copy[j], copy[i]];
    }
    return copy;
  }
}
