import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ContractorStateService } from '../../services/contractor-state.service';
import { TAX_BRACKETS_2026_ON, CPP_MAX_2026, EI_MAX_2026 } from '../../services/tax-engine.service';

interface DeductionCategory {
  name: string;
  description: string;
}

@Component({
  selector: 'app-fulltime-taxes',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './fulltime-taxes.component.html',
})
export class FulltimeTaxesComponent {
  readonly brackets = TAX_BRACKETS_2026_ON;
  readonly cppMax = CPP_MAX_2026;
  readonly eiMax = EI_MAX_2026;

  readonly deductionCategories: DeductionCategory[] = [
    { name: 'RRSP Contributions', description: 'Contributions to a Registered Retirement Savings Plan reduce taxable income dollar-for-dollar, up to your available room.' },
    { name: 'Union / Professional Dues', description: 'Mandatory union dues or professional association membership fees required to earn employment income.' },
    { name: 'Home Office Expenses (T2200)', description: 'If your employer requires you to work from home, a signed T2200 lets you deduct a portion of home office costs.' },
    { name: 'Child Care Expenses', description: 'Daycare, camps, and caregiver costs incurred so you (and a spouse) can work or study.' },
    { name: 'Moving Expenses', description: 'Eligible moving costs when relocating 40km+ closer to a new work location.' },
    { name: 'Professional Development', description: 'Courses, certifications, and licensing fees required to maintain your professional status.' },
    { name: 'Employment Insurance / CPP Overpayment', description: 'If you had multiple employers, excess CPP/EI withheld beyond the annual max is refunded at tax time.' },
    { name: 'Charitable Donations', description: 'Donations to registered charities generate a non-refundable tax credit that reduces tax payable.' },
  ];

  isInfinite(value: number): boolean {
    return !Number.isFinite(value);
  }

  constructor(public readonly state: ContractorStateService) {}
}

