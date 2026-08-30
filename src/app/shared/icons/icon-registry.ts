export type IconUsageContext =
  | 'global-nav'
  | 'citizenship-subnav'
  | 'topic-browser'
  | 'learning-flow'
  | 'status-feedback'
  | 'feature-card'
  | 'coming-soon';

export interface IconDefinition {
  fileName: string;
  assetPath: string;
  label: string;
  meaning: string;
  contexts: IconUsageContext[];
}

export type IconKey =
  | 'home'
  | 'citizenshipExam'
  | 'contractorVsFullTimer'
  | 'dividendCalculator'
  | 'disclaimer'
  | 'topics'
  | 'flashcards'
  | 'practiceQuiz'
  | 'mockExam'
  | 'bookmarksFilled'
  | 'bookmarksOutline'
  | 'progress'
  | 'applyingForCitizenship'
  | 'oathOfCitizenship'
  | 'rightsAndResponsibilities'
  | 'whoWeAre'
  | 'canadasHistory'
  | 'modernCanada'
  | 'governance'
  | 'federalElections'
  | 'justiceSystem'
  | 'canadianSymbols'
  | 'canadasEconomy'
  | 'canadasRegions'
  | 'timer'
  | 'success'
  | 'error'
  | 'celebrate'
  | 'studyMode'
  | 'comingSoon'
  | 'features'
  | 'outputAnalytics'
  | 'scenarioPlay'
  | 'incomeView'
  | 'canadaAware'
  | 'ideaTip';

export const ICON_REGISTRY: Record<IconKey, IconDefinition> = {
  home: {
    fileName: 'home.svg',
    assetPath: 'assets/icons/home.svg',
    label: 'Home',
    meaning: 'Navigate to application home/dashboard.',
    contexts: ['global-nav'],
  },
  citizenshipExam: {
    fileName: 'citizenship-exam.svg',
    assetPath: 'assets/icons/citizenship-exam.svg',
    label: 'Citizenship Exam',
    meaning: 'Canadian citizenship exam preparation tool entry point.',
    contexts: ['global-nav', 'feature-card'],
  },
  contractorVsFullTimer: {
    fileName: 'contractor-vs-full-timer.svg',
    assetPath: 'assets/icons/contractor-vs-full-timer.svg',
    label: 'Contractor vs Full-Timer',
    meaning: 'Compare contractor and employee compensation paths.',
    contexts: ['global-nav', 'feature-card', 'coming-soon'],
  },
  dividendCalculator: {
    fileName: 'dividend-calculator.svg',
    assetPath: 'assets/icons/dividend-calculator.svg',
    label: 'Dividend Calculator',
    meaning: 'Portfolio and dividend income calculator.',
    contexts: ['global-nav', 'feature-card', 'coming-soon'],
  },
  disclaimer: {
    fileName: 'disclaimer.svg',
    assetPath: 'assets/icons/disclaimer.svg',
    label: 'Disclaimer',
    meaning: 'Important caution and official-source guidance.',
    contexts: ['citizenship-subnav'],
  },
  topics: {
    fileName: 'topics.svg',
    assetPath: 'assets/icons/topics.svg',
    label: 'Topics',
    meaning: 'Browse all study topics.',
    contexts: ['citizenship-subnav'],
  },
  flashcards: {
    fileName: 'flashcards.svg',
    assetPath: 'assets/icons/flashcards.svg',
    label: 'Flashcards',
    meaning: 'Review content using flashcards.',
    contexts: ['citizenship-subnav', 'learning-flow'],
  },
  practiceQuiz: {
    fileName: 'practice-quiz.svg',
    assetPath: 'assets/icons/practice-quiz.svg',
    label: 'Practice Quiz',
    meaning: 'Launch configurable quiz practice.',
    contexts: ['citizenship-subnav', 'learning-flow'],
  },
  mockExam: {
    fileName: 'mock-exam.svg',
    assetPath: 'assets/icons/mock-exam.svg',
    label: 'Mock Exam',
    meaning: 'Timed exam simulation.',
    contexts: ['citizenship-subnav', 'learning-flow'],
  },
  bookmarksFilled: {
    fileName: 'bookmarks-filled.svg',
    assetPath: 'assets/icons/bookmarks-filled.svg',
    label: 'Bookmarked',
    meaning: 'Saved/bookmarked state is active.',
    contexts: ['citizenship-subnav', 'learning-flow', 'status-feedback'],
  },
  bookmarksOutline: {
    fileName: 'bookmarks-outline.svg',
    assetPath: 'assets/icons/bookmarks-outline.svg',
    label: 'Not Bookmarked',
    meaning: 'Saved/bookmarked state is inactive.',
    contexts: ['learning-flow', 'status-feedback'],
  },
  progress: {
    fileName: 'progress.svg',
    assetPath: 'assets/icons/progress.svg',
    label: 'Progress',
    meaning: 'Progress dashboard and study analytics.',
    contexts: ['citizenship-subnav', 'status-feedback'],
  },
  applyingForCitizenship: {
    fileName: 'applying-for-citizenship.svg',
    assetPath: 'assets/icons/applying-for-citizenship.svg',
    label: 'Applying for Citizenship',
    meaning: 'Application process and checklist content.',
    contexts: ['topic-browser'],
  },
  oathOfCitizenship: {
    fileName: 'oath-of-citizenship.svg',
    assetPath: 'assets/icons/oath-of-citizenship.svg',
    label: 'Oath of Citizenship',
    meaning: 'Pledge and oath study content.',
    contexts: ['topic-browser'],
  },
  rightsAndResponsibilities: {
    fileName: 'rights-and-responsibilities.svg',
    assetPath: 'assets/icons/rights-and-responsibilities.svg',
    label: 'Rights and Responsibilities',
    meaning: 'Rights, duties, and civic obligations.',
    contexts: ['topic-browser'],
  },
  whoWeAre: {
    fileName: 'who-we-are.svg',
    assetPath: 'assets/icons/who-we-are.svg',
    label: 'Who We Are',
    meaning: 'Canadian identity and people.',
    contexts: ['topic-browser'],
  },
  canadasHistory: {
    fileName: 'canadas-history.svg',
    assetPath: 'assets/icons/canadas-history.svg',
    label: 'Canada\'s History',
    meaning: 'Historical events and heritage.',
    contexts: ['topic-browser'],
  },
  modernCanada: {
    fileName: 'modern-canada.svg',
    assetPath: 'assets/icons/modern-canada.svg',
    label: 'Modern Canada',
    meaning: 'Contemporary Canadian society and development.',
    contexts: ['topic-browser'],
  },
  governance: {
    fileName: 'governance.svg',
    assetPath: 'assets/icons/governance.svg',
    label: 'Governance',
    meaning: 'Government and institutions.',
    contexts: ['topic-browser'],
  },
  federalElections: {
    fileName: 'federal-elections.svg',
    assetPath: 'assets/icons/federal-elections.svg',
    label: 'Federal Elections',
    meaning: 'Voting and federal election process.',
    contexts: ['topic-browser'],
  },
  justiceSystem: {
    fileName: 'justice-system.svg',
    assetPath: 'assets/icons/justice-system.svg',
    label: 'Justice System',
    meaning: 'Law, courts, and legal framework.',
    contexts: ['topic-browser'],
  },
  canadianSymbols: {
    fileName: 'canadian-symbols.svg',
    assetPath: 'assets/icons/canadian-symbols.svg',
    label: 'Canadian Symbols',
    meaning: 'National symbols and emblems.',
    contexts: ['topic-browser'],
  },
  canadasEconomy: {
    fileName: 'canadas-economy.svg',
    assetPath: 'assets/icons/canadas-economy.svg',
    label: 'Canada\'s Economy',
    meaning: 'Work, trade, and economy topics.',
    contexts: ['topic-browser'],
  },
  canadasRegions: {
    fileName: 'canadas-regions.svg',
    assetPath: 'assets/icons/canadas-regions.svg',
    label: 'Canada\'s Regions',
    meaning: 'Geography and regional overview.',
    contexts: ['topic-browser'],
  },
  timer: {
    fileName: 'timer.svg',
    assetPath: 'assets/icons/timer.svg',
    label: 'Timer',
    meaning: 'Countdown and remaining time indicator.',
    contexts: ['learning-flow', 'status-feedback'],
  },
  success: {
    fileName: 'success.svg',
    assetPath: 'assets/icons/success.svg',
    label: 'Success',
    meaning: 'Correct answer or successful completion.',
    contexts: ['status-feedback'],
  },
  error: {
    fileName: 'error.svg',
    assetPath: 'assets/icons/error.svg',
    label: 'Error',
    meaning: 'Incorrect answer or failed condition.',
    contexts: ['status-feedback'],
  },
  celebrate: {
    fileName: 'celebrate.svg',
    assetPath: 'assets/icons/celebrate.svg',
    label: 'Celebrate',
    meaning: 'Achievement, pass, or completion celebration.',
    contexts: ['status-feedback'],
  },
  studyMode: {
    fileName: 'study-mode.svg',
    assetPath: 'assets/icons/study-mode.svg',
    label: 'Study Mode',
    meaning: 'Learning mode or continue studying prompt.',
    contexts: ['learning-flow', 'status-feedback'],
  },
  comingSoon: {
    fileName: 'coming-soon.svg',
    assetPath: 'assets/icons/coming-soon.svg',
    label: 'Coming Soon',
    meaning: 'Feature not yet released.',
    contexts: ['coming-soon', 'status-feedback'],
  },
  features: {
    fileName: 'features.svg',
    assetPath: 'assets/icons/features.svg',
    label: 'Features',
    meaning: 'Feature list or capabilities section.',
    contexts: ['feature-card', 'coming-soon'],
  },
  outputAnalytics: {
    fileName: 'output-analytics.svg',
    assetPath: 'assets/icons/output-analytics.svg',
    label: 'Output Analytics',
    meaning: 'Results, reports, and output metrics.',
    contexts: ['feature-card', 'status-feedback'],
  },
  scenarioPlay: {
    fileName: 'scenario-play.svg',
    assetPath: 'assets/icons/scenario-play.svg',
    label: 'Scenario Play',
    meaning: 'Scenario simulation and configuration.',
    contexts: ['feature-card', 'coming-soon'],
  },
  incomeView: {
    fileName: 'income-view.svg',
    assetPath: 'assets/icons/income-view.svg',
    label: 'Income View',
    meaning: 'Income-focused result visualization.',
    contexts: ['feature-card', 'coming-soon'],
  },
  canadaAware: {
    fileName: 'canada-aware.svg',
    assetPath: 'assets/icons/canada-aware.svg',
    label: 'Canada Aware',
    meaning: 'Canada-specific tax and policy context.',
    contexts: ['feature-card', 'coming-soon'],
  },
  ideaTip: {
    fileName: 'idea-tip.svg',
    assetPath: 'assets/icons/idea-tip.svg',
    label: 'Tip',
    meaning: 'Hint, explanation, or study guidance callout.',
    contexts: ['learning-flow', 'status-feedback'],
  },
};

export const ICON_ASSET_BASE_PATH = 'assets/icons';

export function iconPath(iconKey: IconKey): string {
  return ICON_REGISTRY[iconKey].assetPath;
}
