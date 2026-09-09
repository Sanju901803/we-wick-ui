import { Injectable } from '@angular/core';

export interface TaxBracket {
  from: number;
  to: number;
  regularRate: number;
  dividendRate: number;
}

/** Combined Federal + Ontario marginal tax brackets, 2026 tax year. */
export const TAX_BRACKETS_2026_ON: TaxBracket[] = [
  { from: 0, to: 53891, regularRate: 0.1905, dividendRate: 0.0809 },
  { from: 53891, to: 58523, regularRate: 0.2315, dividendRate: 0.128 },
  { from: 58523, to: 94907, regularRate: 0.2965, dividendRate: 0.2028 },
  { from: 94907, to: 107785, regularRate: 0.3148, dividendRate: 0.2238 },
  { from: 107785, to: 111814, regularRate: 0.3389, dividendRate: 0.2516 },
  { from: 111814, to: 117045, regularRate: 0.3791, dividendRate: 0.2978 },
  { from: 117045, to: 150000, regularRate: 0.4341, dividendRate: 0.361 },
  { from: 150000, to: 181440, regularRate: 0.4497, dividendRate: 0.379 },
  { from: 181440, to: 220000, regularRate: 0.4826, dividendRate: 0.4168 },
  { from: 220000, to: 258482, regularRate: 0.4982, dividendRate: 0.4347 },
  { from: 258482, to: Infinity, regularRate: 0.5353, dividendRate: 0.4774 },
];

export const HST_RATE = 0.13;
export const HST_QUICK_METHOD_RATE = 0.088;
export const HST_QUICK_METHOD_CREDIT = 300;
export const CORPORATE_TAX_RATE = 0.122; // small business rate (9% federal + 3.2% Ontario)
export const CAPITAL_GAINS_TAX_TOTAL_RATE = 0.5017;
export const CAPITAL_GAINS_TAX_NON_REFUNDABLE_RATE = 0.195;
export const RDTOH_REFUND_RATE = 0.3833; // refund per $1 of dividend paid
export const CPP_MAX_2026 = 4230.45 + 416.0; // base CPP + CPP2 enhancement
export const EI_MAX_2026 = 1123.07;
export const STAT_HOLIDAYS_ON_2026 = 12;
export const HOURS_PER_DAY_DEFAULT = 7.5;
export const WEEKS_PER_YEAR = 52;
export const CALENDAR_DAYS_PER_YEAR = 52 * 7;

// Proportional CPP/EI parameters (2026) — used for salary amounts that may
// fall below the maximum contribution caps (unlike the flat CPP_MAX_2026 /
// EI_MAX_2026 used for the Full-Time Pay tab's high-salary assumption).
export const CPP_EMPLOYEE_RATE_2026 = 0.0595;
export const CPP_BASIC_EXEMPTION_2026 = 3500;
export const CPP_YMPE_2026 = 74600;
export const EI_EMPLOYEE_RATE_2026 = 0.0163;
export const EI_MIE_2026 = 68900;

// Personal registered-account reference figures (2026 estimates) — used on
// the Full-Time tab's "Investment & Tax Reduction Strategy" page.
export const RRSP_CONTRIBUTION_RATE = 0.18; // 18% of prior-year earned income
export const RRSP_DOLLAR_LIMIT_2026 = 33810; // approx annual dollar limit, whichever is lower
export const TFSA_ANNUAL_LIMIT_2026 = 7000; // annual TFSA contribution room

/**
 * Pure tax-calculation helpers shared by both the contractor (dividend income)
 * and full-time employee (regular income) paths. No HTTP/state — safe to
 * later lift into a backend service unchanged.
 */
@Injectable({ providedIn: 'root' })
export class TaxEngineService {
  /**
   * Progressive marginal-bracket tax calculation. Only the portion of
   * `income` that falls within each bracket is taxed at that bracket's rate.
   */
  calculateProgressiveTax(
    income: number,
    brackets: TaxBracket[],
    rateKey: 'regularRate' | 'dividendRate'
  ): number {
    if (income <= 0) {
      return 0;
    }
    let tax = 0;
    for (const bracket of brackets) {
      if (income <= bracket.from) {
        continue;
      }
      const taxableInBracket = Math.min(income, bracket.to) - bracket.from;
      if (taxableInBracket > 0) {
        tax += taxableInBracket * bracket[rateKey];
      }
    }
    return tax;
  }

  calculateRegularIncomeTax(income: number, brackets: TaxBracket[] = TAX_BRACKETS_2026_ON): number {
    return this.calculateProgressiveTax(income, brackets, 'regularRate');
  }

  calculateDividendIncomeTax(income: number, brackets: TaxBracket[] = TAX_BRACKETS_2026_ON): number {
    return this.calculateProgressiveTax(income, brackets, 'dividendRate');
  }

  /** Proportional employee CPP contribution, capped at the 2026 maximum. */
  calculateCpp(income: number): number {
    if (income <= 0) {
      return 0;
    }
    const pensionableEarnings = Math.max(
      0,
      Math.min(income, CPP_YMPE_2026) - CPP_BASIC_EXEMPTION_2026
    );
    return Math.min(pensionableEarnings * CPP_EMPLOYEE_RATE_2026, CPP_MAX_2026);
  }

  /** Proportional employee EI premium, capped at the 2026 maximum. */
  calculateEi(income: number): number {
    if (income <= 0) {
      return 0;
    }
    const insurableEarnings = Math.min(income, EI_MIE_2026);
    return Math.min(insurableEarnings * EI_EMPLOYEE_RATE_2026, EI_MAX_2026);
  }

  /** Net pay for a T4 salary after regular income tax, CPP, and EI. */
  calculateEmployeeNetForGross(gross: number): number {
    return gross - this.calculateRegularIncomeTax(gross) - this.calculateCpp(gross) - this.calculateEi(gross);
  }

  /**
   * Binary-searches for the gross T4 salary required to net `targetNet`
   * after regular income tax, CPP, and EI. Used to answer "how much salary
   * would I need to match my contractor take-home?".
   */
  calculateRequiredGrossSalary(targetNet: number): number {
    if (targetNet <= 0) {
      return 0;
    }
    let lo = 0;
    let hi = Math.max(targetNet * 2, 10000);
    while (this.calculateEmployeeNetForGross(hi) < targetNet && hi < 10_000_000) {
      hi *= 2;
    }
    for (let i = 0; i < 60; i++) {
      const mid = (lo + hi) / 2;
      if (this.calculateEmployeeNetForGross(mid) < targetNet) {
        lo = mid;
      } else {
        hi = mid;
      }
    }
    return hi;
  }
}
