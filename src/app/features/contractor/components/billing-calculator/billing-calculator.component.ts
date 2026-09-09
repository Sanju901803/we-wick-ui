import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ContractorStateService } from '../../services/contractor-state.service';

@Component({
  selector: 'app-billing-calculator',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './billing-calculator.component.html',
})
export class BillingCalculatorComponent {
  private nextExpenseId = 2;
  breakdownVisible = false;

  constructor(public readonly state: ContractorStateService) {
    this.nextExpenseId = this.state.inputs.expenses.length + 1;
  }

  recalculate(): void {
    this.state.recalculate();
    this.breakdownVisible = false;
  }

  calculateBreakdown(): void {
    this.state.recalculate();
    this.breakdownVisible = true;
  }

  addExpense(): void {
    this.state.inputs.expenses.push({ id: this.nextExpenseId++, description: '', amount: 0 });
    this.recalculate();
  }

  removeExpense(index: number): void {
    this.state.inputs.expenses.splice(index, 1);
    this.recalculate();
  }
}
