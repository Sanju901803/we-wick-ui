import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ContractorStateService } from '../../services/contractor-state.service';
import { ContractorCalculatorService } from '../../services/contractor-calculator.service';
import { CPP_MAX_2026, EI_MAX_2026 } from '../../services/tax-engine.service';

@Component({
  selector: 'app-full-time',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './full-time.component.html',
})
export class FullTimeComponent {
  readonly cppMax = CPP_MAX_2026;
  readonly eiMax = EI_MAX_2026;

  private nextExpenseId = 2;
  breakdownVisible = false;

  constructor(
    public readonly state: ContractorStateService,
    private readonly calculator: ContractorCalculatorService,
  ) {
    this.nextExpenseId = this.state.inputs.expenses.length + 1;
  }

  recalculate(): void {
    this.state.recalculate();
  }

  /** Annual Gross Salary changed — hide the contractor-equivalent sections until recalculated. */
  onGrossSalaryChange(): void {
    this.state.recalculate();
    this.breakdownVisible = false;
  }

  calculateBreakdown(): void {
    // Seed a sensible default split (100% salary, $0 dividend) the first time
    // this is calculated. Further field edits reuse whatever split the user
    // has customized instead of resetting it.
    const { salaryDraw } = this.calculator.calculateAllSalaryEquivalent(
      this.state.inputs,
      this.state.result.hoursBillable,
      this.state.result.employeeNet,
    );
    this.state.inputs.annualDividendAmount = 0;
    this.state.inputs.salaryDraw = salaryDraw;
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
