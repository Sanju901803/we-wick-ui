import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ContractorStateService } from '../../services/contractor-state.service';
import {
  TAX_BRACKETS_2026_ON,
  RRSP_CONTRIBUTION_RATE,
  RRSP_DOLLAR_LIMIT_2026,
  TFSA_ANNUAL_LIMIT_2026,
} from '../../services/tax-engine.service';

/**
 * Educational "ideal investment & tax reduction strategy" tab for a full-time
 * (T4) employee. Uses the live scenario from ContractorStateService (same
 * gross salary as the Fulltime-to-Contractor tab) to estimate RRSP
 * contribution room and the resulting tax savings for the current scenario.
 */
@Component({
  selector: 'app-fulltime-strategy',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './fulltime-strategy.component.html',
})
export class FulltimeStrategyComponent {
  readonly rrspDollarLimit = RRSP_DOLLAR_LIMIT_2026;
  readonly tfsaAnnualLimit = TFSA_ANNUAL_LIMIT_2026;

  constructor(public readonly state: ContractorStateService) {}

  /** 18% of gross salary, capped at the annual dollar limit. */
  get rrspContributionRoom(): number {
    const gross = this.state.inputs.fullTimeGrossSalary;
    return Math.min(gross * RRSP_CONTRIBUTION_RATE, RRSP_DOLLAR_LIMIT_2026);
  }

  /** Marginal tax rate at the top of the current gross salary. */
  get marginalTaxRate(): number {
    const gross = this.state.inputs.fullTimeGrossSalary;
    const bracket = TAX_BRACKETS_2026_ON.find(b => gross > b.from && gross <= b.to)
      ?? TAX_BRACKETS_2026_ON[TAX_BRACKETS_2026_ON.length - 1];
    return bracket.regularRate;
  }

  /** Estimated tax refund/savings if you max out RRSP room this year. */
  get estimatedRrspTaxSavings(): number {
    return this.rrspContributionRoom * this.marginalTaxRate;
  }

  /** Take-home pay after accounting for the RRSP tax refund. */
  get netAfterRrspSavings(): number {
    return this.state.result.employeeNet + this.estimatedRrspTaxSavings;
  }
}

