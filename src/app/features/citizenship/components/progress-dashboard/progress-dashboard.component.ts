import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { QuestionService } from '../../../../core/services/question.service';
import { ProgressService } from '../../../../core/services/progress.service';
import { QuizResult, Question } from '../../../../core/models';
import { IconComponent } from '../../../../shared/components/icon/icon.component';

interface TopicStat {
  topic: string;
  correct: number;
  total: number;
  pct: number;
}

@Component({
  selector: 'app-progress-dashboard',
  standalone: true,
  imports: [CommonModule, RouterLink, IconComponent],
  templateUrl: './progress-dashboard.component.html',
})
export class ProgressDashboardComponent implements OnInit {
  topicStats: TopicStat[] = [];
  totalAttempted = 0;
  totalCorrect = 0;
  overallPct = 0;
  bookmarkCount = 0;
  hasData = false;

  constructor(
    private questionService: QuestionService,
    private progressService: ProgressService
  ) {}

  ngOnInit(): void {
    this.loadStats();
  }

  loadStats(): void {
    const results = this.progressService.getAllResults();
    this.bookmarkCount = this.progressService.getBookmarks().length;
    const latest: Record<string, QuizResult> = {};
    results.forEach(r => { latest[r.questionId] = r; });
    const latestList = Object.values(latest);
    this.totalAttempted = latestList.length;
    this.totalCorrect = latestList.filter(r => r.correct).length;
    this.overallPct = this.totalAttempted
      ? Math.round((this.totalCorrect / this.totalAttempted) * 100)
      : 0;
    this.hasData = this.totalAttempted > 0;

    if (!this.hasData) return;

    this.questionService.getAll().subscribe(all => {
      const topicMap: Record<string, string> = {};
      all.forEach(q => topicMap[q.id] = q.topic);

      const stats: Record<string, { correct: number; total: number }> = {};
      latestList.forEach(r => {
        const topic = topicMap[r.questionId] || 'Unknown';
        if (!stats[topic]) stats[topic] = { correct: 0, total: 0 };
        stats[topic].total++;
        if (r.correct) stats[topic].correct++;
      });

      this.topicStats = Object.entries(stats).map(([topic, s]) => ({
        topic,
        correct: s.correct,
        total: s.total,
        pct: Math.round((s.correct / s.total) * 100)
      })).sort((a, b) => a.topic.localeCompare(b.topic));
    });
  }

  resetProgress(): void {
    if (confirm('This will clear all your quiz history. Are you sure?')) {
      this.progressService.resetProgress();
      this.loadStats();
    }
  }
}
