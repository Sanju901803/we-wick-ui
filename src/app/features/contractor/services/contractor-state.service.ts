import { Injectable } from '@angular/core';
import { ContractorCalculatorService } from './contractor-calculator.service';
import { ContractorInputs, ContractorResult, DEFAULT_CONTRACTOR_INPUTS } from '../models/contractor.model';

/**
 * Holds the current ContractorInputs/ContractorResult so all four contractor
 * tabs (Billing Calculator, Contractor Taxes, Full-Time, Tax Info) share the
 * same live scenario instead of recomputing independently.
 */
@Injectable({ providedIn: 'root' })
export class ContractorStateService {
  inputs: ContractorInputs = { ...DEFAULT_CONTRACTOR_INPUTS };
  result: ContractorResult;

  constructor(private readonly calculator: ContractorCalculatorService) {
    this.result = this.calculator.calculate(this.inputs);
  }

  recalculate(): void {
    this.result = this.calculator.calculate(this.inputs);
  }
}
