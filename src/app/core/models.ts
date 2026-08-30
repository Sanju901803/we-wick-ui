export interface Question {
  id: string;
  topic: string;
  subtopic?: string;
  question: string;
  options: string[];
  answerIndex: number;
  explanation: string;
  imagePath?: string;
}

export interface TopicSummary {
  name: string;
  icon: string;
  iconKey: string;
  count: number;
}

export interface QuizResult {
  questionId: string;
  selectedIndex: number;
  correct: boolean;
  timestamp: number;
}

export interface ExamSession {
  questions: Question[];
  answers: (number | null)[];
  startTime: number;
  endTime?: number;
  submitted: boolean;
}
