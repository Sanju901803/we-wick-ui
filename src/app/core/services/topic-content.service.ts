import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, map, shareReplay } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class TopicContentService {
  private readonly dataUrl = 'assets/data/topics-content.json';
  private cache$?: Observable<Record<string, string>>;

  constructor(private http: HttpClient) {}

  private load(): Observable<Record<string, string>> {
    if (!this.cache$) {
      this.cache$ = this.http.get<Record<string, string>>(this.dataUrl).pipe(
        shareReplay(1)
      );
    }
    return this.cache$;
  }

  getContent(topicName: string): Observable<string> {
    return this.load().pipe(
      map(data => data[topicName] || '')
    );
  }
}
