import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';
import { QuestionService } from '../../../../core/services/question.service';
import { ProgressService } from '../../../../core/services/progress.service';
import { Question } from '../../../../core/models';
import { IconComponent } from '../../../../shared/components/icon/icon.component';
import { ImageClickDirective } from '../../../../shared/directives/image-click.directive';

@Component({
  selector: 'app-flashcard',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterLink, IconComponent, ImageClickDirective],
  templateUrl: './flashcard.component.html',
})
export class FlashcardComponent implements OnInit {
  allCards: Question[] = [];
  cards: Question[] = [];
  allTopics: string[] = [];
  selectedTopic = '';
  currentIndex = 0;
  flipped = false;
  knownIds = new Set<string>();

  constructor(
    private questionService: QuestionService,
    private progressService: ProgressService
  ) {}

  ngOnInit(): void {
    this.questionService.getAll().subscribe(qs => {
      this.allCards = this.questionService.shuffle(qs);
      this.allTopics = [...new Set(qs.map(q => q.topic))];
      this.cards = [...this.allCards];
      this.currentIndex = 0;
      this.flipped = false;
    });
  }

  get currentCard(): Question {
    return this.cards[this.currentIndex];
  }

  get progressPct(): number {
    return this.cards.length ? (this.knownIds.size / this.cards.length) * 100 : 0;
  }

  get knownCount(): number {
    return this.knownIds.size;
  }

  flip(): void {
    this.flipped = !this.flipped;
  }

  next(): void {
    if (this.currentIndex < this.cards.length - 1) {
      this.currentIndex++;
      this.flipped = false;
    }
  }

  prev(): void {
    if (this.currentIndex > 0) {
      this.currentIndex--;
      this.flipped = false;
    }
  }

  onTopicChange(): void {
    this.cards = this.selectedTopic
      ? this.allCards.filter(q => q.topic === this.selectedTopic)
      : [...this.allCards];
    this.currentIndex = 0;
    this.flipped = false;
  }

  markResult(correct: boolean): void {
    if (!this.currentCard) return;
    if (correct) {
      this.knownIds.add(this.currentCard.id);
    } else {
      this.knownIds.delete(this.currentCard.id);
    }
    this.progressService.saveResult({
      questionId: this.currentCard.id,
      selectedIndex: correct ? this.currentCard.answerIndex : -1,
      correct,
      timestamp: Date.now()
    });
    this.next();
  }

  isBookmarked(): boolean {
    return this.currentCard ? this.progressService.isBookmarked(this.currentCard.id) : false;
  }

  toggleBookmark(): void {
    if (this.currentCard) this.progressService.toggleBookmark(this.currentCard.id);
  }
}
