import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';
import { QuestionService } from '../../../../core/services/question.service';
import { ProgressService } from '../../../../core/services/progress.service';
import { Question } from '../../../../core/models';
import { IconComponent } from '../../../../shared/components/icon/icon.component';
import { ImageClickDirective } from '../../../../shared/directives/image-click.directive';

type QuizState = 'config' | 'running' | 'review';

@Component({
  selector: 'app-quiz',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterLink, IconComponent, ImageClickDirective],
  templateUrl: './quiz.component.html',
})
export class QuizComponent implements OnInit {
  allTopics: string[] = [];
  allQuestions: Question[] = [];
  quizQuestions: Question[] = [];
  configTopic = '';
  configCount = 10;
  state: QuizState = 'config';
  currentIndex = 0;
  selectedOption: number | null = null;
  answers: (number | null)[] = [];
  score = 0;

  constructor(
    private questionService: QuestionService,
    private progressService: ProgressService
  ) {}

  ngOnInit(): void {
    this.questionService.getAll().subscribe(qs => {
      this.allQuestions = qs;
      this.allTopics = [...new Set(qs.map(q => q.topic))];
    });
  }

  get currentQuestion(): Question | undefined {
    return this.quizQuestions[this.currentIndex];
  }

  get hasEnoughQuestions(): boolean {
    const pool = this.configTopic
      ? this.allQuestions.filter(q => q.topic === this.configTopic)
      : this.allQuestions;
    return pool.length >= this.configCount;
  }

  startQuiz(): void {
    const pool = this.configTopic
      ? this.allQuestions.filter(q => q.topic === this.configTopic)
      : this.allQuestions;
    this.quizQuestions = this.questionService.shuffle(pool).slice(0, this.configCount);
    this.answers = new Array(this.configCount).fill(null);
    this.currentIndex = 0;
    this.selectedOption = null;
    this.score = 0;
    this.state = 'running';
  }

  startAgain(): void {
    this.startQuiz();
  }

  selectOption(idx: number): void {
    if (this.selectedOption !== null || !this.currentQuestion) return;
    this.selectedOption = idx;
    this.answers[this.currentIndex] = idx;
    const correct = idx === this.currentQuestion.answerIndex;
    this.progressService.saveResult({
      questionId: this.currentQuestion.id,
      selectedIndex: idx,
      correct,
      timestamp: Date.now()
    });
    if (correct) this.score++;
  }

  nextQuestion(): void {
    if (this.currentIndex < this.quizQuestions.length - 1) {
      this.currentIndex++;
      this.selectedOption = null;
    } else {
      this.state = 'review';
    }
  }

  isBookmarked(id: string): boolean {
    return this.progressService.isBookmarked(id);
  }

  toggleBookmark(id: string): void {
    this.progressService.toggleBookmark(id);
  }

  topicCount(topic: string): number {
    return this.allQuestions.filter(q => q.topic === topic).length;
  }
}
