#!/usr/bin/env python3
"""
Add new Federal Elections questions (q282–q315).
"""
import json, os

DATA_FILE = os.path.join(os.path.dirname(__file__), '../src/assets/data/questions.json')

NEW_QUESTIONS = [
  {
    "id": "q282",
    "topic": "Federal Elections",
    "subtopic": "Voting",
    "question": "What is the minimum age to vote in a Canadian federal election?",
    "options": [
      "16",
      "17",
      "18",
      "21"
    ],
    "answerIndex": 2,
    "explanation": "A Canadian citizen must be at least 18 years old on Election Day to vote in a federal election. This age requirement also applies to provincial and territorial elections."
  },
  {
    "id": "q283",
    "topic": "Federal Elections",
    "subtopic": "Voting",
    "question": "What is a secret ballot?",
    "options": [
      "A ballot that is sealed and only opened after all votes are counted",
      "A voting method where citizens write their vote privately, and no one else can know how they voted",
      "A ballot used only in Senate elections",
      "A ballot where only politicians can see the results before the public"
    ],
    "answerIndex": 1,
    "explanation": "A secret ballot means that how a person votes is private — no one else can know how you voted. This protects voters from pressure, intimidation, or retaliation. The secret ballot is a cornerstone of democracy in Canada."
  },
  {
    "id": "q284",
    "topic": "Federal Elections",
    "subtopic": "Voting",
    "question": "What must a person do before they can vote in a federal election?",
    "options": [
      "Apply to Elections Canada six months before the election",
      "Be on the voters' list (National Register of Electors) or register on Election Day",
      "Pay a registration fee to Elections Canada",
      "Show proof of employment or tax returns"
    ],
    "answerIndex": 1,
    "explanation": "To vote, a person must be on the voters' list. Eligible voters are automatically registered if Elections Canada has their information, but anyone can also register at their polling station on Election Day. The voters' list is maintained by Elections Canada."
  },
  {
    "id": "q285",
    "topic": "Federal Elections",
    "subtopic": "Electoral System",
    "question": "What is a 'majority government' in Canada?",
    "options": [
      "A government where the Prime Minister's party won more than 75% of seats",
      "A government where the ruling party holds at least half (50%+1) of the seats in the House of Commons",
      "A government supported by the majority of the public in opinion polls",
      "A government coalition of two or more parties"
    ],
    "answerIndex": 1,
    "explanation": "A majority government is one where the governing party holds more than half of the seats (at least 170 of 338) in the House of Commons. A majority government can pass legislation without needing support from opposition parties."
  },
  {
    "id": "q286",
    "topic": "Federal Elections",
    "subtopic": "Electoral System",
    "question": "What happens if no party wins a majority of seats in a federal election?",
    "options": [
      "A new election is immediately called",
      "The Governor General appoints a coalition government",
      "The party with the most seats forms a minority government and must seek support from other parties to pass legislation",
      "The outgoing government continues indefinitely"
    ],
    "answerIndex": 2,
    "explanation": "When no party wins a majority of seats, the party with the most seats typically forms a minority government. A minority government must negotiate with other parties to pass legislation and can fall if it loses a confidence vote."
  },
  {
    "id": "q287",
    "topic": "Federal Elections",
    "subtopic": "Campaign",
    "question": "What is the role of political parties in a federal election?",
    "options": [
      "To appoint Senators and judges",
      "To organize campaigns, present platforms, and field candidates in ridings across Canada to compete for seats in the House of Commons",
      "To set election dates and manage polling stations",
      "To review and certify the election results"
    ],
    "answerIndex": 1,
    "explanation": "Political parties organize election campaigns, develop policy platforms, raise funds, and field candidates in ridings across Canada. The party that wins the most seats is invited to form the government."
  },
  {
    "id": "q288",
    "topic": "Federal Elections",
    "subtopic": "Campaign",
    "question": "What is a 'platform' in an election campaign?",
    "options": [
      "The stage where party leaders give speeches",
      "A party's written set of policies and commitments that it promises to implement if elected",
      "The podium used in televised debates",
      "A fundraising document distributed to party donors"
    ],
    "answerIndex": 1,
    "explanation": "An election platform (or party platform) is the official set of policies and commitments a political party promises to implement if elected. Voters compare platforms to decide which party's vision for the country best matches their priorities."
  },
  {
    "id": "q289",
    "topic": "Federal Elections",
    "subtopic": "Campaign",
    "question": "What is a party leader's debate?",
    "options": [
      "A formal meeting of party leaders to set legislative priorities before an election",
      "A televised event during an election campaign where leaders of the major parties discuss their platforms and challenge each other's policies",
      "A debate held in the House of Commons before Parliament dissolves",
      "A secret negotiation between party leaders about forming a coalition"
    ],
    "answerIndex": 1,
    "explanation": "Leaders' debates are televised events during election campaigns where the leaders of the major parties debate their platforms directly. They give voters a chance to compare leaders' visions, communication styles, and ability to handle scrutiny."
  },
  {
    "id": "q290",
    "topic": "Federal Elections",
    "subtopic": "Electoral System",
    "question": "What is 'vote splitting' in Canadian elections?",
    "options": [
      "Dividing your ballot between two candidates",
      "When multiple parties with similar views compete in the same riding, splitting the vote between them and potentially allowing a less-preferred party to win",
      "The process of counting votes in different polling stations",
      "When a tied race requires a second vote"
    ],
    "answerIndex": 1,
    "explanation": "Vote splitting occurs when two or more parties with similar platforms compete in the same riding, splitting the votes between them. This can allow a party with different views to win the seat even with fewer total votes than the combined total of its opponents."
  },
  {
    "id": "q291",
    "topic": "Federal Elections",
    "subtopic": "Voting",
    "question": "Can a Canadian citizen living outside Canada vote in a federal election?",
    "options": [
      "No — citizens must live in Canada to vote",
      "Yes — Canadian citizens living abroad can vote by special ballot",
      "Only if they have lived outside Canada for less than 1 year",
      "Only if they are government employees working abroad"
    ],
    "answerIndex": 1,
    "explanation": "Canadian citizens living outside Canada can vote in federal elections by special ballot. They vote in the riding where they last lived in Canada. The right to vote is tied to citizenship, not current residency."
  },
  {
    "id": "q292",
    "topic": "Federal Elections",
    "subtopic": "Electoral System",
    "question": "What is redistribution (redistricting) and why does it happen?",
    "options": [
      "The process of redistributing federal funds to provinces",
      "Redrawing the boundaries of federal electoral districts (ridings) to reflect population changes",
      "Redistributing votes to ensure proportional representation",
      "The process of reallocating Senate seats after an election"
    ],
    "answerIndex": 1,
    "explanation": "Redistribution (or electoral redistricting) is the periodic redrawing of federal riding boundaries by independent electoral boundaries commissions. It ensures that ridings reflect population changes as determined by the census, so each riding represents a roughly equal number of people."
  },
  {
    "id": "q293",
    "topic": "Federal Elections",
    "subtopic": "Political Parties",
    "question": "What are the three major federal political parties in Canada?",
    "options": [
      "Conservative, Liberal, and Green",
      "Liberal, NDP, and Bloc Québécois",
      "Conservative Party of Canada, Liberal Party of Canada, and New Democratic Party (NDP)",
      "Liberal, Reform, and Progressive Conservative"
    ],
    "answerIndex": 2,
    "explanation": "The three major federal political parties in Canada are: the Conservative Party of Canada (centre-right), the Liberal Party of Canada (centre to centre-left), and the New Democratic Party or NDP (left). Other parties including the Green Party and Bloc Québécois also hold seats."
  },
  {
    "id": "q294",
    "topic": "Federal Elections",
    "subtopic": "Political Parties",
    "question": "What is the Bloc Québécois?",
    "options": [
      "A federal party that promotes Quebec independence and runs candidates only in Quebec",
      "Quebec's provincial governing party",
      "A federal party representing Western Canadian interests",
      "An alliance of all francophone parties in Canada"
    ],
    "answerIndex": 0,
    "explanation": "The Bloc Québécois is a federal political party that advocates for Quebec's interests and, historically, Quebec independence (sovereignty). It runs candidates only in Quebec ridings. Despite being a separatist party, it participates in federal Parliament."
  },
  {
    "id": "q295",
    "topic": "Federal Elections",
    "subtopic": "Voting",
    "question": "What identification must a voter bring to the polling station?",
    "options": [
      "Only a voter information card is required",
      "Acceptable government-issued photo ID showing name and address, or two pieces of ID with name and address",
      "A passport only",
      "A tax return for the previous year"
    ],
    "answerIndex": 1,
    "explanation": "To vote, Canadians must prove their identity and address. Acceptable options include one piece of government-issued photo ID showing name and address, or two pieces of ID that together show name and address. Voters without ID can have someone vouch for them."
  },
  {
    "id": "q296",
    "topic": "Federal Elections",
    "subtopic": "Campaign",
    "question": "When is Election Day held for scheduled federal elections?",
    "options": [
      "The first Monday in October every 4 years",
      "The third Monday in October every 4 years",
      "July 1 every 4 years",
      "The first Tuesday in November every 4 years"
    ],
    "answerIndex": 1,
    "explanation": "Under Canada's fixed election date law (2007), scheduled federal elections are held on the third Monday in October, every four years. However, the Governor General can dissolve Parliament earlier on the Prime Minister's advice, triggering an earlier election."
  },
  {
    "id": "q297",
    "topic": "Federal Elections",
    "subtopic": "Voting",
    "question": "What is the purpose of advance polls in a federal election?",
    "options": [
      "To give special groups an early look at election results",
      "To allow eligible voters who cannot attend on Election Day to vote early",
      "To test voting equipment before Election Day",
      "To allow non-citizens to vote before citizenship requirements take effect"
    ],
    "answerIndex": 1,
    "explanation": "Advance polls are held several days before Election Day to allow eligible voters who may be away, working, or otherwise unable to vote on Election Day to cast their ballot early. Advance voting typically takes place over 4 days."
  },
  {
    "id": "q298",
    "topic": "Federal Elections",
    "subtopic": "Electoral System",
    "question": "What does the Chief Electoral Officer (CEO) do?",
    "options": [
      "The CEO is the leader of Elections Canada and presides over citizenship ceremonies",
      "The CEO is an independent officer of Parliament who administers federal elections and reports to Parliament, not to the government",
      "The CEO is appointed by the Prime Minister to organize election campaigns",
      "The CEO supervises campaign spending for all political parties"
    ],
    "answerIndex": 1,
    "explanation": "The Chief Electoral Officer is the independent head of Elections Canada and an Officer of Parliament. They are responsible for administering federal elections and referendums, maintaining the voters' list, and reporting to Parliament — not to the government."
  },
  {
    "id": "q299",
    "topic": "Federal Elections",
    "subtopic": "Campaign",
    "question": "Are there limits on how much money political parties and candidates can spend on election campaigns?",
    "options": [
      "No — there are no spending limits in Canadian elections",
      "Yes — there are strict limits on campaign spending by political parties and individual candidates, enforced by Elections Canada",
      "Only candidates must follow spending limits; parties have no restrictions",
      "Only parties with seats in Parliament face spending limits"
    ],
    "answerIndex": 1,
    "explanation": "Yes — Canadian election law sets strict limits on how much political parties and individual candidates can spend during an election campaign. These limits are enforced by Elections Canada and must be publicly disclosed, to help ensure fairness and transparency."
  },
  {
    "id": "q300",
    "topic": "Federal Elections",
    "subtopic": "Electoral System",
    "question": "What is a 'riding' (or 'constituency')?",
    "options": [
      "A section of the federal budget allocated to a region",
      "A geographic electoral district that elects one Member of Parliament to the House of Commons",
      "A political zone administered by a Senator",
      "A municipal district in a major Canadian city"
    ],
    "answerIndex": 1,
    "explanation": "A riding (also called a constituency or electoral district) is a geographic area that elects one Member of Parliament (MP) to the House of Commons. Canada currently has 338 ridings. Each riding elects one MP using the first-past-the-post system."
  }
]

def main():
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        existing = json.load(f)
    existing_ids = {q['id'] for q in existing}
    added = 0
    for q in NEW_QUESTIONS:
        if q['id'] not in existing_ids:
            existing.append(q)
            added += 1
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)
    topic = "Federal Elections"
    count = len([q for q in existing if q['topic'] == topic])
    print(f"Added {added} questions. '{topic}' now has {count} questions. Total: {len(existing)}")

if __name__ == '__main__':
    main()
