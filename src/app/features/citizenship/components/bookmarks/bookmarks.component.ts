import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { QuestionService } from '../../../../core/services/question.service';
import { ProgressService } from '../../../../core/services/progress.service';
import { Question } from '../../../../core/models';
import { IconComponent } from '../../../../shared/components/icon/icon.component';
import { ImageClickDirective } from '../../../../shared/directives/image-click.directive';

@Component({
  selector: 'app-bookmarks',
  standalone: true,
  imports: [CommonModule, RouterLink, IconComponent, ImageClickDirective],
  templateUrl: './bookmarks.component.html',
})
export class BookmarksComponent implements OnInit {
  bookmarkedQuestions: Question[] = [];

  constructor(
    private questionService: QuestionService,
    private progressService: ProgressService
  ) {}

  ngOnInit(): void {
    this.loadBookmarks();
  }

  loadBookmarks(): void {
    const ids = this.progressService.getBookmarks();
    if (!ids.length) {
      this.bookmarkedQuestions = [];
      return;
    }
    this.questionService.getAll().subscribe(all => {
      this.bookmarkedQuestions = all.filter(q => ids.includes(q.id));
    });
  }

  removeBookmark(id: string): void {
    this.progressService.toggleBookmark(id);
    this.bookmarkedQuestions = this.bookmarkedQuestions.filter(q => q.id !== id);
  }

  clearAll(): void {
    if (confirm('Remove all bookmarks?')) {
      this.progressService.clearBookmarks();
      this.bookmarkedQuestions = [];
    }
  }
}
