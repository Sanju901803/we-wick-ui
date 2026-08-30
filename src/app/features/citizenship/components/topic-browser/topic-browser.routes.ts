import { Routes } from '@angular/router';

export const topicBrowserRoutes: Routes = [
  {
    path: '',
    redirectTo: 'applying-for-citizenship',
    pathMatch: 'full'
  },
  {
    path: 'applying-for-citizenship',
    loadComponent: () =>
      import('./topics/applying-for-citizenship/applying-for-citizenship.component')
        .then(m => m.ApplyingForCitizenshipComponent)
  },
  {
    path: 'oath-of-citizenship',
    loadComponent: () =>
      import('./topics/oath-of-citizenship/oath-of-citizenship.component')
        .then(m => m.OathOfCitizenshipComponent)
  },
  {
    path: 'rights-and-responsibilities',
    loadComponent: () =>
      import('./topics/rights-and-responsibilities/rights-and-responsibilities.component')
        .then(m => m.RightsAndResponsibilitiesComponent)
  },
  {
    path: 'who-we-are',
    loadComponent: () =>
      import('./topics/who-we-are/who-we-are.component')
        .then(m => m.WhoWeAreComponent)
  },
  {
    path: 'canadas-history',
    loadComponent: () =>
      import('./topics/canadas-history/canadas-history.component')
        .then(m => m.CanadasHistoryComponent)
  },
  {
    path: 'modern-canada',
    loadComponent: () =>
      import('./topics/modern-canada/modern-canada.component')
        .then(m => m.ModernCanadaComponent)
  },
  {
    path: 'how-canadians-govern-themselves',
    loadComponent: () =>
      import('./topics/how-canadians-govern-themselves/how-canadians-govern-themselves.component')
        .then(m => m.HowCanadiansGovernThemselvesComponent)
  },
  {
    path: 'federal-elections',
    loadComponent: () =>
      import('./topics/federal-elections/federal-elections.component')
        .then(m => m.FederalElectionsComponent)
  },
  {
    path: 'the-justice-system',
    loadComponent: () =>
      import('./topics/the-justice-system/the-justice-system.component')
        .then(m => m.TheJusticeSystemComponent)
  },
  {
    path: 'canadian-symbols',
    loadComponent: () =>
      import('./topics/canadian-symbols/canadian-symbols.component')
        .then(m => m.CanadianSymbolsComponent)
  },
  {
    path: 'canadas-economy',
    loadComponent: () =>
      import('./topics/canadas-economy/canadas-economy.component')
        .then(m => m.CanadasEconomyComponent)
  },
  {
    path: 'canadas-regions',
    loadComponent: () =>
      import('./topics/canadas-regions/canadas-regions.component')
        .then(m => m.CanadasRegionsComponent)
  }
];
