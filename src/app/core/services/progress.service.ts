import { Injectable } from '@angular/core';
import { QuizResult } from '../models';

const RESULTS_KEY = 'ww_quiz_results';
const BOOKMARKS_KEY = 'ww_bookmarks';

@Injectable({ providedIn: 'root' })
export class ProgressService {

  // --- Quiz results ---

  saveResult(result: QuizResult): void {
    const results = this.getAllResults();
    results.push(result);
    localStorage.setItem(RESULTS_KEY, JSON.stringify(results));
  }

  getAllResults(): QuizResult[] {
    const raw = localStorage.getItem(RESULTS_KEY);
    return raw ? JSON.parse(raw) : [];
  }

  getResultsForQuestion(questionId: string): QuizResult[] {
    return this.getAllResults().filter(r => r.questionId === questionId);
  }

  getLatestResultForQuestion(questionId: string): QuizResult | null {
    const results = this.getResultsForQuestion(questionId);
    return results.length ? results[results.length - 1] : null;
  }

  /** Returns map of questionId -> latest result */
  getLatestResultsMap(): Record<string, QuizResult> {
    const all = this.getAllResults();
    const map: Record<string, QuizResult> = {};
    all.forEach(r => { map[r.questionId] = r; });
    return map;
  }

  getCorrectCount(): number {
    return this.getAllResults().filter(r => r.correct).length;
  }

  getAttemptedQuestionIds(): Set<string> {
    return new Set(this.getAllResults().map(r => r.questionId));
  }

  /** Stats per topic: { topic: { correct, total } } */
  getTopicStats(allResults: QuizResult[], topicMap: Record<string, string>): Record<string, { correct: number; total: number }> {
    const stats: Record<string, { correct: number; total: number }> = {};
    const seen: Record<string, boolean> = {};

    // latest result per question
    const latest: Record<string, QuizResult> = {};
    allResults.forEach(r => { latest[r.questionId] = r; });

    Object.values(latest).forEach(r => {
      const topic = topicMap[r.questionId] || 'Unknown';
      if (!stats[topic]) stats[topic] = { correct: 0, total: 0 };
      stats[topic].total++;
      if (r.correct) stats[topic].correct++;
    });

    return stats;
  }

  resetProgress(): void {
    localStorage.removeItem(RESULTS_KEY);
  }

  // --- Bookmarks ---

  getBookmarks(): string[] {
    const raw = localStorage.getItem(BOOKMARKS_KEY);
    return raw ? JSON.parse(raw) : [];
  }

  isBookmarked(questionId: string): boolean {
    return this.getBookmarks().includes(questionId);
  }

  toggleBookmark(questionId: string): boolean {
    const bookmarks = this.getBookmarks();
    const idx = bookmarks.indexOf(questionId);
    if (idx === -1) {
      bookmarks.push(questionId);
    } else {
      bookmarks.splice(idx, 1);
    }
    localStorage.setItem(BOOKMARKS_KEY, JSON.stringify(bookmarks));
    return idx === -1;
  }

  clearBookmarks(): void {
    localStorage.removeItem(BOOKMARKS_KEY);
  }
}
