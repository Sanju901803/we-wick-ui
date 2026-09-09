import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ContractorStateService } from '../../services/contractor-state.service';

/**
 * Educational "ideal payout & investment strategy" tab. Uses the live
 * scenario from ContractorStateService (same inputs as the Billing
 * Calculator tab) to show how much money is spendable today vs retained
 * in the corporation for later investment.
 */
@Component({
  selector: 'app-strategy',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './strategy.component.html',
})
export class StrategyComponent {
  constructor(public readonly state: ContractorStateService) {}

  /** Money actually paid out to you personally today (dividend + reimbursement + salary, after tax). */
  get personalMoneyToSpend(): number {
    return this.state.result.personalNet + this.state.result.salaryNet;
  }

  /** Money left inside the corporation, available for future investment/payout. */
  get retainedForInvestment(): number {
    return this.state.result.netInCorporation;
  }
}
