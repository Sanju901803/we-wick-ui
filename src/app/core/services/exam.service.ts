import { Injectable } from '@angular/core';
import { ExamSession, Question } from '../models';

const EXAM_DURATION_SECONDS = 45 * 60; // 45 minutes
const PASS_SCORE = 15; // 15/20

@Injectable({ providedIn: 'root' })
export class ExamService {
  session: ExamSession | null = null;
  private timerInterval: ReturnType<typeof setInterval> | null = null;
  secondsRemaining = 0;

  get passMark(): number { return PASS_SCORE; }
  get totalQuestions(): number { return 20; }

  startSession(questions: Question[]): void {
    this.session = {
      questions: questions.slice(0, 20),
      answers: new Array(20).fill(null),
      startTime: Date.now(),
      submitted: false
    };
    this.secondsRemaining = EXAM_DURATION_SECONDS;
  }

  recordAnswer(index: number, choiceIndex: number): void {
    if (!this.session || this.session.submitted) return;
    this.session.answers[index] = choiceIndex;
  }

  submit(): void {
    if (!this.session) return;
    this.session.submitted = true;
    this.session.endTime = Date.now();
    this.stopTimer();
  }

  getScore(): number {
    if (!this.session) return 0;
    return this.session.questions.reduce((score, q, i) => {
      return score + (this.session!.answers[i] === q.answerIndex ? 1 : 0);
    }, 0);
  }

  passed(): boolean {
    return this.getScore() >= PASS_SCORE;
  }

  clearSession(): void {
    this.session = null;
    this.stopTimer();
    this.secondsRemaining = 0;
  }

  startTimer(onTick: (s: number) => void, onExpire: () => void): void {
    this.stopTimer();
    this.timerInterval = setInterval(() => {
      this.secondsRemaining--;
      onTick(this.secondsRemaining);
      if (this.secondsRemaining <= 0) {
        this.stopTimer();
        onExpire();
      }
    }, 1000);
  }

  stopTimer(): void {
    if (this.timerInterval !== null) {
      clearInterval(this.timerInterval);
      this.timerInterval = null;
    }
  }

  formatTime(seconds: number): string {
    const m = Math.floor(seconds / 60).toString().padStart(2, '0');
    const s = (seconds % 60).toString().padStart(2, '0');
    return `${m}:${s}`;
  }
}
