import { Injectable } from '@angular/core';
import { ContractorInputs, ContractorResult } from '../models/contractor.model';
import {
  CALENDAR_DAYS_PER_YEAR,
  CAPITAL_GAINS_TAX_NON_REFUNDABLE_RATE,
  CAPITAL_GAINS_TAX_TOTAL_RATE,
  CORPORATE_TAX_RATE,
  CPP_MAX_2026,
  EI_MAX_2026,
  HST_QUICK_METHOD_CREDIT,
  HST_QUICK_METHOD_RATE,
  HST_RATE,
  RDTOH_REFUND_RATE,
  TaxEngineService,
  WEEKS_PER_YEAR,
} from './tax-engine.service';

/**
 * Orchestrates the full Contractor vs Full-Timer calculation, translating the
 * source spreadsheet (documentation/Fulltime vs Contract v0.5.xlsx) into pure
 * TypeScript. See documentation/ui/CONTRACTOR-SOLUTION.md for the full model.
 */
@Injectable({ providedIn: 'root' })
export class ContractorCalculatorService {
  constructor(private readonly taxEngine: TaxEngineService) {}

  calculate(inputs: ContractorInputs): ContractorResult {
    // 1. Time off -> billable days/hours
    const weekendDaysOffTotal = inputs.weekendDaysOff ? inputs.weekendDaysCount * WEEKS_PER_YEAR : 0;
    const daysOff = inputs.statHolidays + inputs.furloughDays + inputs.vacationDays + weekendDaysOffTotal;
    const daysBillable = CALENDAR_DAYS_PER_YEAR - daysOff;
    const hoursBillable = daysBillable * inputs.hoursPerDay;

    // 2. Corporation - billing, HST, corporate tax
    const subtotalBilled = inputs.hourlyRate * hoursBillable;
    const hstBilled = subtotalBilled * HST_RATE;
    const totalBilled = subtotalBilled + hstBilled;
    const payoutMonthly = totalBilled / 12;
    const payoutBiweekly = totalBilled / 26;
    const payoutWeekly = totalBilled / 52;
    const payoutDaily = daysBillable > 0 ? totalBilled / daysBillable : 0;
    const totalExpenses = inputs.expenses.reduce((sum, item) => sum + (item.amount || 0), 0);
    const expense = totalExpenses * (1 + HST_RATE);
    const hstPayable = totalBilled * HST_QUICK_METHOD_RATE - HST_QUICK_METHOD_CREDIT;
    // Salary drawn is a deductible corporate expense, unlike dividends which are paid post-tax
    const taxableAmount = totalBilled - expense - hstPayable - inputs.salaryDraw;
    const corporateTaxPayable = taxableAmount * CORPORATE_TAX_RATE;
    const totalCorpPayable = corporateTaxPayable + hstPayable;

    // 3. Corporation - investment income (capital gains + RDTOH refund)
    const totalInvestmentIncome = inputs.interestIncome + inputs.realizedGains;
    const investmentTaxTotal = totalInvestmentIncome * CAPITAL_GAINS_TAX_TOTAL_RATE;
    const investmentTaxNonRefundable = totalInvestmentIncome * CAPITAL_GAINS_TAX_NON_REFUNDABLE_RATE;
    const maxRefundable = investmentTaxTotal - investmentTaxNonRefundable;
    const investmentDividendPayable = maxRefundable / RDTOH_REFUND_RATE;
    const investmentTaxPayable = investmentTaxTotal - maxRefundable;

    // 4. Cash paid out of the corporation (dividend draw + salary draw + RDTOH dividend + expense reimbursement)
    const nonTaxableReimbursement = expense;
    const totalCashOutOfCorp =
      inputs.annualDividendAmount + inputs.salaryDraw + investmentDividendPayable + nonTaxableReimbursement;

    // 5. Corporation - net result
    const netInCorporation =
      totalBilled -
      totalCorpPayable +
      totalInvestmentIncome -
      investmentTaxPayable -
      totalCashOutOfCorp;

    // 6. Personal tax on the dividend portion
    const taxablePersonalIncome = inputs.annualDividendAmount + investmentDividendPayable;
    const personalTaxOwed = this.taxEngine.calculateDividendIncomeTax(taxablePersonalIncome);
    const personalNet = nonTaxableReimbursement + taxablePersonalIncome - personalTaxOwed;

    // 7. Personal tax on the salary portion (regular income tax + CPP + EI)
    const salaryTax = this.taxEngine.calculateRegularIncomeTax(inputs.salaryDraw);
    const salaryCpp = this.taxEngine.calculateCpp(inputs.salaryDraw);
    const salaryEi = this.taxEngine.calculateEi(inputs.salaryDraw);
    const salaryNet = inputs.salaryDraw - salaryTax - salaryCpp - salaryEi;

    // 7b. Personal tax on the dividend draw alone, for the "paying yourself" comparison
    const dividendTax = this.taxEngine.calculateDividendIncomeTax(inputs.annualDividendAmount);
    const dividendNet = inputs.annualDividendAmount - dividendTax;

    // 8. Combined contractor result (retained corp net + dividend net + salary net)
    const combinedNet = netInCorporation + personalNet + salaryNet;
    const effectiveTaxRate = totalBilled > 0 ? 1 - combinedNet / totalBilled : 0;

    // 9. Full-time employee comparison
    const employeeTax = this.taxEngine.calculateRegularIncomeTax(inputs.fullTimeGrossSalary);
    const employeeCpp = CPP_MAX_2026;
    const employeeEi = EI_MAX_2026;
    const employeeNet = inputs.fullTimeGrossSalary - employeeTax - employeeCpp - employeeEi;
    const ratio = employeeNet !== 0 ? combinedNet / employeeNet : 0;

    // 10. Gross T4 salary needed to net the same as this contractor scenario,
    // worked backwards: net + tax + CPP + EI = gross
    const requiredSalaryForContractorNet = this.taxEngine.calculateRequiredGrossSalary(combinedNet);
    const requiredSalaryTax = this.taxEngine.calculateRegularIncomeTax(requiredSalaryForContractorNet);
    const requiredSalaryCpp = this.taxEngine.calculateCpp(requiredSalaryForContractorNet);
    const requiredSalaryEi = this.taxEngine.calculateEi(requiredSalaryForContractorNet);

    // 11. Hourly rate needed, worked backwards from the Full-Time gross salary:
    // what rate would this contractor need to charge (at the current time-off,
    // expense, investment-income, and salary/dividend-draw assumptions) to net
    // the same take-home pay as the full-time employee nets today?
    const requiredHourlyRateForEmployeeNet = this.calculateRequiredHourlyRate(inputs, hoursBillable, employeeNet);
    const requiredRateModel = this.modelForRate(inputs, hoursBillable, requiredHourlyRateForEmployeeNet);

    return {
      weekendDaysOffTotal,
      daysOff,
      daysBillable,
      hoursBillable,
      subtotalBilled,
      hstBilled,
      totalBilled,
      payoutMonthly,
      payoutBiweekly,
      payoutWeekly,
      payoutDaily,
      totalExpenses,
      hstPayable,
      taxableAmount,
      corporateTaxPayable,
      totalCorpPayable,
      totalInvestmentIncome,
      investmentTaxTotal,
      investmentTaxNonRefundable,
      maxRefundable,
      investmentDividendPayable,
      investmentTaxPayable,
      nonTaxableReimbursement,
      totalCashOutOfCorp,
      netInCorporation,
      taxablePersonalIncome,
      personalTaxOwed,
      personalNet,
      salaryTax,
      salaryCpp,
      salaryEi,
      salaryNet,
      dividendTax,
      dividendNet,
      combinedNet,
      effectiveTaxRate,
      employeeTax,
      employeeCpp,
      employeeEi,
      employeeNet,
      ratio,
      requiredSalaryForContractorNet,
      requiredSalaryTax,
      requiredSalaryCpp,
      requiredSalaryEi,
      requiredHourlyRateForEmployeeNet,
      requiredHourlyRateTotalBilled: requiredRateModel.totalBilled,
      requiredHourlyRateHstPayable: requiredRateModel.hstPayable,
      requiredHourlyRateCorporateTaxPayable: requiredRateModel.corporateTaxPayable,
      requiredHourlyRateSalaryDraw: requiredRateModel.salaryDraw,
      requiredHourlyRateSalaryTax: requiredRateModel.salaryTax,
      requiredHourlyRateSalaryCpp: requiredRateModel.salaryCpp,
      requiredHourlyRateSalaryEi: requiredRateModel.salaryEi,
      requiredHourlyRateSalaryNet: requiredRateModel.salaryNet,
      requiredHourlyRateDividendAmount: requiredRateModel.dividendAmount,
      requiredHourlyRateNonTaxableReimbursement: requiredRateModel.nonTaxableReimbursement,
      requiredHourlyRateTaxablePersonalIncome: requiredRateModel.taxablePersonalIncome,
      requiredHourlyRatePersonalTaxOwed: requiredRateModel.personalTaxOwed,
      requiredHourlyRatePersonalNet: requiredRateModel.personalNet,
      requiredHourlyRateNetInCorporation: requiredRateModel.netInCorporation,
      requiredHourlyRateCombinedNet: requiredRateModel.combinedNet,
    };
  }

  /**
   * Full contractor-model breakdown for a given hourly rate, holding every
   * other input (time off, expenses, investment income) fixed. Mirrors
   * steps 2-8 of `calculate()` above but only returns the fields needed for
   * the Full-Time tab's reverse hourly-rate lookup, so it can be evaluated
   * cheaply many times during the binary search. When `allSalary` is true,
   * the entire post-expense/HST corporate income is drawn out as salary
   * (dividend $0) instead of using the fixed `salaryDraw` /
   * `annualDividendAmount` inputs — used only once, to seed a sensible
   * default split when the Full-Time tab's "Calculate Contractor Equivalent"
   * button is first pressed.
   */
  private modelForRate(inputs: ContractorInputs, hoursBillable: number, hourlyRate: number, allSalary = false) {
    const subtotalBilled = hourlyRate * hoursBillable;
    const hstBilled = subtotalBilled * HST_RATE;
    const totalBilled = subtotalBilled + hstBilled;
    const totalExpenses = inputs.expenses.reduce((sum, item) => sum + (item.amount || 0), 0);
    const expense = totalExpenses * (1 + HST_RATE);
    const hstPayable = totalBilled * HST_QUICK_METHOD_RATE - HST_QUICK_METHOD_CREDIT;

    const salaryDraw = allSalary ? Math.max(totalBilled - expense - hstPayable, 0) : inputs.salaryDraw;
    const dividendAmount = allSalary ? 0 : inputs.annualDividendAmount;

    const taxableAmount = totalBilled - expense - hstPayable - salaryDraw;
    const corporateTaxPayable = taxableAmount * CORPORATE_TAX_RATE;
    const totalCorpPayable = corporateTaxPayable + hstPayable;

    const totalInvestmentIncome = inputs.interestIncome + inputs.realizedGains;
    const investmentTaxTotal = totalInvestmentIncome * CAPITAL_GAINS_TAX_TOTAL_RATE;
    const investmentTaxNonRefundable = totalInvestmentIncome * CAPITAL_GAINS_TAX_NON_REFUNDABLE_RATE;
    const maxRefundable = investmentTaxTotal - investmentTaxNonRefundable;
    const investmentDividendPayable = maxRefundable / RDTOH_REFUND_RATE;
    const investmentTaxPayable = investmentTaxTotal - maxRefundable;

    const nonTaxableReimbursement = expense;
    const totalCashOutOfCorp = dividendAmount + salaryDraw + investmentDividendPayable + nonTaxableReimbursement;

    const netInCorporation =
      totalBilled - totalCorpPayable + totalInvestmentIncome - investmentTaxPayable - totalCashOutOfCorp;

    const taxablePersonalIncome = dividendAmount + investmentDividendPayable;
    const personalTaxOwed = this.taxEngine.calculateDividendIncomeTax(taxablePersonalIncome);
    const personalNet = nonTaxableReimbursement + taxablePersonalIncome - personalTaxOwed;

    const salaryTax = this.taxEngine.calculateRegularIncomeTax(salaryDraw);
    const salaryCpp = this.taxEngine.calculateCpp(salaryDraw);
    const salaryEi = this.taxEngine.calculateEi(salaryDraw);
    const salaryNet = salaryDraw - salaryTax - salaryCpp - salaryEi;

    const combinedNet = netInCorporation + personalNet + salaryNet;

    return {
      totalBilled,
      hstPayable,
      corporateTaxPayable,
      salaryDraw,
      dividendAmount,
      nonTaxableReimbursement,
      taxablePersonalIncome,
      personalTaxOwed,
      personalNet,
      salaryTax,
      salaryCpp,
      salaryEi,
      salaryNet,
      netInCorporation,
      combinedNet,
    };
  }

  /**
   * Binary-searches for the hourly rate a contractor would need to charge
   * (at the current time-off/expense/draw assumptions) to net `targetNet`.
   * Combined net rises monotonically with hourly rate, so this converges
   * the same way `TaxEngineService.calculateRequiredGrossSalary` does.
   */
  private calculateRequiredHourlyRate(inputs: ContractorInputs, hoursBillable: number, targetNet: number): number {
    if (targetNet <= 0 || hoursBillable <= 0) {
      return 0;
    }
    let lo = 0;
    let hi = Math.max(inputs.hourlyRate * 2, 100);
    let guard = 0;
    while (this.modelForRate(inputs, hoursBillable, hi).combinedNet < targetNet && hi < 1_000_000 && guard < 60) {
      hi *= 2;
      guard++;
    }
    for (let i = 0; i < 60; i++) {
      const mid = (lo + hi) / 2;
      if (this.modelForRate(inputs, hoursBillable, mid).combinedNet < targetNet) {
        lo = mid;
      } else {
        hi = mid;
      }
    }
    return hi;
  }

  /**
   * Solves for the "100% salary, $0 dividend" hourly rate that nets
   * `targetNet`, and returns the implied salary draw alongside it. Used only
   * once — when the Full-Time tab's "Calculate Contractor Equivalent" button
   * is first pressed — to seed a sensible default salary/dividend split
   * before the user starts customizing the Paying Yourself Options fields by
   * hand. Subsequent edits reuse the plain (non-forced) reverse lookup above.
   */
  calculateAllSalaryEquivalent(
    inputs: ContractorInputs,
    hoursBillable: number,
    targetNet: number,
  ): { hourlyRate: number; salaryDraw: number } {
    if (targetNet <= 0 || hoursBillable <= 0) {
      return { hourlyRate: 0, salaryDraw: 0 };
    }
    let lo = 0;
    let hi = Math.max(inputs.hourlyRate * 2, 100);
    let guard = 0;
    while (this.modelForRate(inputs, hoursBillable, hi, true).combinedNet < targetNet && hi < 1_000_000 && guard < 60) {
      hi *= 2;
      guard++;
    }
    for (let i = 0; i < 60; i++) {
      const mid = (lo + hi) / 2;
      if (this.modelForRate(inputs, hoursBillable, mid, true).combinedNet < targetNet) {
        lo = mid;
      } else {
        hi = mid;
      }
    }
    return { hourlyRate: hi, salaryDraw: this.modelForRate(inputs, hoursBillable, hi, true).salaryDraw };
  }
}
