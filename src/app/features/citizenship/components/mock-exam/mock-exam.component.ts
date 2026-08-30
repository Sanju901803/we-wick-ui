import { Component, OnDestroy, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { QuestionService } from '../../../../core/services/question.service';
import { ExamService } from '../../../../core/services/exam.service';
import { ProgressService } from '../../../../core/services/progress.service';
import { Question } from '../../../../core/models';
import { IconComponent } from '../../../../shared/components/icon/icon.component';
import { ImageClickDirective } from '../../../../shared/directives/image-click.directive';

type ExamState = 'intro' | 'running' | 'review';

@Component({
  selector: 'app-mock-exam',
  standalone: true,
  imports: [CommonModule, RouterLink, IconComponent, ImageClickDirective],
  templateUrl: './mock-exam.component.html',
})
export class MockExamComponent implements OnInit, OnDestroy {
  state: ExamState = 'intro';
  currentIndex = 0;
  timeRemaining = 0;
  allQuestions: Question[] = [];

  constructor(
    public examService: ExamService,
    private questionService: QuestionService,
    private progressService: ProgressService
  ) {}

  ngOnInit(): void {
    this.questionService.getAll().subscribe(qs => this.allQuestions = qs);
    if (this.examService.session && !this.examService.session.submitted) {
      this.state = 'running';
      this.timeRemaining = this.examService.secondsRemaining;
      this.resumeTimer();
    } else if (this.examService.session?.submitted) {
      this.state = 'review';
    }
  }

  ngOnDestroy(): void {
    this.examService.stopTimer();
  }

  get currentQuestion(): Question {
    return this.examService.session!.questions[this.currentIndex];
  }

  get answeredPct(): number {
    if (!this.examService.session) return 0;
    const answered = this.examService.session.answers.filter(a => a !== null).length;
    return (answered / 20) * 100;
  }

  startExam(): void {
    const shuffled = this.questionService.shuffle(this.allQuestions);
    this.examService.startSession(shuffled);
    this.timeRemaining = this.examService.secondsRemaining;
    this.currentIndex = 0;
    this.state = 'running';
    this.resumeTimer();
  }

  resumeTimer(): void {
    this.examService.startTimer(
      s => this.timeRemaining = s,
      () => this.submitExam()
    );
  }

  selectAnswer(optionIndex: number): void {
    this.examService.recordAnswer(this.currentIndex, optionIndex);
  }

  nextQ(): void {
    if (this.currentIndex < 19) this.currentIndex++;
  }

  prevQ(): void {
    if (this.currentIndex > 0) this.currentIndex--;
  }

  goTo(i: number): void {
    this.currentIndex = i;
  }

  submitExam(): void {
    this.examService.submit();
    this.state = 'review';
  }

  resetExam(): void {
    this.examService.clearSession();
    this.state = 'intro';
    this.currentIndex = 0;
  }
}
