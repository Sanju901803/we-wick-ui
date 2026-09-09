import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path: '',
    loadComponent: () =>
      import('./features/home/home.component').then(m => m.HomeComponent)
  },
  {
    path: 'citizenship',
    loadChildren: () =>
      import('./features/citizenship/citizenship.routes').then(m => m.citizenshipRoutes)
  },
  {
    path: 'contractor',
    loadChildren: () =>
      import('./features/contractor/contractor.routes').then(m => m.contractorRoutes)
  },
  {
    path: 'dividend-calculator',
    loadComponent: () =>
      import('./features/dividend-calculator/dividend-calculator.component').then(m => m.DividendCalculatorComponent)
  },
  {
    path: 'access-required',
    pathMatch: 'full',
    redirectTo: ''
  },
  {
    path: '**',
    redirectTo: ''
  }
];
