import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ContractorStateService } from '../../services/contractor-state.service';
import {
  CAPITAL_GAINS_TAX_NON_REFUNDABLE_RATE,
  CAPITAL_GAINS_TAX_TOTAL_RATE,
  CORPORATE_TAX_RATE,
  HST_QUICK_METHOD_CREDIT,
  HST_QUICK_METHOD_RATE,
  HST_RATE,
  RDTOH_REFUND_RATE,
} from '../../services/tax-engine.service';

interface ExpenseCategory {
  name: string;
  description: string;
}

@Component({
  selector: 'app-contractor-taxes',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './contractor-taxes.component.html',
})
export class ContractorTaxesComponent {
  readonly hstRate = HST_RATE;
  readonly hstQuickMethodRate = HST_QUICK_METHOD_RATE;
  readonly hstQuickMethodCredit = HST_QUICK_METHOD_CREDIT;
  readonly corporateTaxRate = CORPORATE_TAX_RATE;
  readonly capitalGainsTaxTotalRate = CAPITAL_GAINS_TAX_TOTAL_RATE;
  readonly capitalGainsTaxNonRefundableRate = CAPITAL_GAINS_TAX_NON_REFUNDABLE_RATE;
  readonly rdtohRefundRate = RDTOH_REFUND_RATE;

  readonly expenseCategories: ExpenseCategory[] = [
    { name: 'Home Office', description: 'Proportional rent/mortgage interest, utilities, and internet based on office square footage.' },
    { name: 'Equipment & Software', description: 'Laptop, monitors, ergonomic furniture, and business software subscriptions.' },
    { name: 'Professional Fees', description: 'Accounting, bookkeeping, and legal fees for the corporation.' },
    { name: 'Business Insurance', description: 'Professional liability / errors & omissions insurance.' },
    { name: 'Mileage & Travel', description: 'Vehicle use and travel costs for client meetings (CRA per-km rate or actual costs).' },
    { name: 'Professional Development', description: 'Courses, certifications, conferences, and memberships related to the contract work.' },
    { name: 'Phone & Internet', description: 'Business-use portion of mobile and internet bills.' },
    { name: 'Bank & Payment Fees', description: 'Business bank account fees and payment processor charges.' },
  ];

  constructor(public readonly state: ContractorStateService) {}
}
