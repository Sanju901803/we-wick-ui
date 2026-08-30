import { ToolAccessPolicy, ToolKey } from './access.models';

const DAY_MS = 24 * 60 * 60 * 1000;

export const TOOL_ACCESS_POLICIES: Record<ToolKey, ToolAccessPolicy> = {
  citizenship: {
    toolKey: 'citizenship',
    displayName: 'Canada Citizenship Exam',
    guestPreviewPaths: ['/citizenship', '/citizenship/disclaimer'],
    trialDurationMs: DAY_MS,
  },
  contractor: {
    toolKey: 'contractor',
    displayName: 'Contractor vs Full-Timer',
    guestPreviewPaths: ['/contractor'],
    trialDurationMs: DAY_MS,
  },
  'dividend-calculator': {
    toolKey: 'dividend-calculator',
    displayName: 'Dividend Calculator',
    guestPreviewPaths: ['/dividend-calculator'],
    trialDurationMs: DAY_MS,
  },
};

export function getToolPolicy(toolKey: ToolKey): ToolAccessPolicy {
  return TOOL_ACCESS_POLICIES[toolKey];
}

