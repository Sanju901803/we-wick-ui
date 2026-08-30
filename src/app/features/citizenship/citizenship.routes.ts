import { Routes } from '@angular/router';

export const citizenshipRoutes: Routes = [
  {
    path: '',
    loadComponent: () =>
      import('./citizenship.component').then(m => m.CitizenshipComponent),
    children: [
      { path: '', redirectTo: 'disclaimer', pathMatch: 'full' },
      {
        path: 'disclaimer',
        loadComponent: () =>
          import('./components/disclaimer/disclaimer.component').then(m => m.DisclaimerComponent)
      },
      {
        path: 'topics',
        loadComponent: () =>
          import('./components/topic-browser/topic-browser.component').then(m => m.TopicBrowserComponent),
        loadChildren: () =>
          import('./components/topic-browser/topic-browser.routes').then(m => m.topicBrowserRoutes)
      },
      {
        path: 'flashcards',
        loadComponent: () =>
          import('./components/flashcard/flashcard.component').then(m => m.FlashcardComponent)
      },
      {
        path: 'quiz',
        loadComponent: () =>
          import('./components/quiz/quiz.component').then(m => m.QuizComponent)
      },
      {
        path: 'mock-exam',
        loadComponent: () =>
          import('./components/mock-exam/mock-exam.component').then(m => m.MockExamComponent)
      },
      {
        path: 'bookmarks',
        loadComponent: () =>
          import('./components/bookmarks/bookmarks.component').then(m => m.BookmarksComponent)
      },
      {
        path: 'progress',
        loadComponent: () =>
          import('./components/progress-dashboard/progress-dashboard.component').then(m => m.ProgressDashboardComponent)
      }
    ]
  }
];
