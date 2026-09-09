export interface ExpenseItem {
  id: number;
  description: string;
  amount: number;
}

export interface ContractorInputs {
  // Time off
  furloughDays: number;
  vacationDays: number;
  statHolidays: number;
  weekendDaysOff: boolean;
  weekendDaysCount: number;

  // Billing
  hourlyRate: number;
  hoursPerDay: number;

  // Expenses (dynamic line items, pre-HST)
  expenses: ExpenseItem[];

  // Corp investment income
  interestIncome: number;
  realizedGains: number;

  // Paying yourself: split the draw between salary (T4, deductible to corp,
  // taxed as regular income + CPP/EI) and dividend (T4A, taxed at dividend rates)
  salaryDraw: number;
  annualDividendAmount: number;

  // Full-time comparison
  fullTimeGrossSalary: number;
}

export interface ContractorResult {
  // Time off / billing
  weekendDaysOffTotal: number;
  daysOff: number;
  daysBillable: number;
  hoursBillable: number;
  subtotalBilled: number;
  hstBilled: number;
  totalBilled: number;

  // Payout cadence (annual totalBilled split across common payment schedules)
  payoutMonthly: number;
  payoutBiweekly: number;
  payoutWeekly: number;
  payoutDaily: number;

  // Expenses
  totalExpenses: number; // pre-HST, sum of all expense line items

  // Corporation
  hstPayable: number;
  taxableAmount: number;
  corporateTaxPayable: number;
  totalCorpPayable: number;

  // Investment income (capital gains + RDTOH refund)
  totalInvestmentIncome: number;
  investmentTaxTotal: number;
  investmentTaxNonRefundable: number;
  maxRefundable: number;
  investmentDividendPayable: number;
  investmentTaxPayable: number;

  // Dividends paid out of corp
  nonTaxableReimbursement: number;
  totalCashOutOfCorp: number;

  // Corp net
  netInCorporation: number;

  // Personal tax on the dividend portion
  taxablePersonalIncome: number;
  personalTaxOwed: number;
  personalNet: number;

  // Personal tax on the salary portion (regular income tax + CPP + EI)
  salaryTax: number;
  salaryCpp: number;
  salaryEi: number;
  salaryNet: number;

  // Personal tax on the dividend draw alone (isolated, excludes RDTOH investment dividend)
  dividendTax: number;
  dividendNet: number;

  // Combined contractor result (salary net + dividend net + retained corp net)
  combinedNet: number;
  effectiveTaxRate: number;

  // Full-time employee comparison
  employeeTax: number;
  employeeCpp: number;
  employeeEi: number;
  employeeNet: number;

  // Ratio of contractor net to employee net
  ratio: number;

  // Gross T4 salary a full-time employee would need to net the same amount
  // as this contractor scenario's combined net (worked backwards: net + tax + CPP + EI = gross)
  requiredSalaryForContractorNet: number;
  requiredSalaryTax: number;
  requiredSalaryCpp: number;
  requiredSalaryEi: number;

  // Hourly rate a contractor would need to charge (at the current time-off,
  // expense, and salary/dividend-draw assumptions) to net the same take-home
  // pay as the Full-Time gross salary above nets after tax, CPP, and EI.
  requiredHourlyRateForEmployeeNet: number;
  requiredHourlyRateTotalBilled: number;
  requiredHourlyRateHstPayable: number;
  requiredHourlyRateCorporateTaxPayable: number;
  requiredHourlyRateSalaryDraw: number;
  requiredHourlyRateSalaryTax: number;
  requiredHourlyRateSalaryCpp: number;
  requiredHourlyRateSalaryEi: number;
  requiredHourlyRateSalaryNet: number;
  requiredHourlyRateDividendAmount: number;
  requiredHourlyRateNonTaxableReimbursement: number;
  requiredHourlyRateTaxablePersonalIncome: number;
  requiredHourlyRatePersonalTaxOwed: number;
  requiredHourlyRatePersonalNet: number;
  requiredHourlyRateNetInCorporation: number;
  requiredHourlyRateCombinedNet: number;
}

export const DEFAULT_CONTRACTOR_INPUTS: ContractorInputs = {
  furloughDays: 7,
  vacationDays: 15,
  statHolidays: 12,
  weekendDaysOff: true,
  weekendDaysCount: 2,
  hourlyRate: 100,
  hoursPerDay: 7.5,
  expenses: [{ id: 1, description: 'General business expenses', amount: 10000 }],
  interestIncome: 5000,
  realizedGains: 5000,
  salaryDraw: 0,
  annualDividendAmount: 55000,
  fullTimeGrossSalary: 120000,
};
