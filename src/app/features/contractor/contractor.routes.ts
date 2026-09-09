import { Routes } from '@angular/router';

/**
 * Two main tabs — "Contractor" and "Fulltime" — each with three child pages,
 * mirroring the Citizenship tool's tab structure.
 */
export const contractorRoutes: Routes = [
  {
    path: '',
    loadComponent: () =>
      import('./contractor.component').then(m => m.ContractorComponent),
    children: [
      { path: '', redirectTo: 'contractor', pathMatch: 'full' },
      {
        path: 'contractor',
        loadComponent: () =>
          import('./components/contractor-main/contractor-main.component').then(
            m => m.ContractorMainComponent
          ),
        children: [
          { path: '', redirectTo: 'to-fulltime', pathMatch: 'full' },
          {
            path: 'to-fulltime',
            loadComponent: () =>
              import('./components/billing-calculator/billing-calculator.component').then(
                m => m.BillingCalculatorComponent
              )
          },
          {
            path: 'contractor-taxes',
            loadComponent: () =>
              import('./components/contractor-taxes/contractor-taxes.component').then(
                m => m.ContractorTaxesComponent
              )
          },
          {
            path: 'strategy',
            loadComponent: () =>
              import('./components/strategy/strategy.component').then(m => m.StrategyComponent)
          }
        ]
      },
      {
        path: 'fulltime',
        loadComponent: () =>
          import('./components/fulltime-main/fulltime-main.component').then(
            m => m.FulltimeMainComponent
          ),
        children: [
          { path: '', redirectTo: 'to-contractor', pathMatch: 'full' },
          {
            path: 'to-contractor',
            loadComponent: () =>
              import('./components/full-time/full-time.component').then(m => m.FullTimeComponent)
          },
          {
            path: 'personal-taxes',
            loadComponent: () =>
              import('./components/fulltime-taxes/fulltime-taxes.component').then(
                m => m.FulltimeTaxesComponent
              )
          },
          {
            path: 'investment-strategy',
            loadComponent: () =>
              import('./components/fulltime-strategy/fulltime-strategy.component').then(
                m => m.FulltimeStrategyComponent
              )
          }
        ]
      }
    ]
  }
];
