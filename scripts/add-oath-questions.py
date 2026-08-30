#!/usr/bin/env python3
"""
Add new Oath of Citizenship questions (q121–q135).
"""
import json, os

DATA_FILE = os.path.join(os.path.dirname(__file__), '../src/assets/data/questions.json')

NEW_QUESTIONS = [
  {
    "id": "q121",
    "topic": "Oath of Citizenship",
    "subtopic": "The Oath",
    "question": "What are the two options for making the Oath of Citizenship?",
    "options": [
      "Signing a document or making a verbal declaration",
      "Swearing an oath (religious) or making a solemn affirmation (non-religious)",
      "Swearing in English or swearing in French",
      "Taking the oath privately or publicly"
    ],
    "answerIndex": 1,
    "explanation": "New citizens can either 'swear' the oath (a religious affirmation) or 'affirm' it (a solemn non-religious declaration). Both are legally equal and the choice is the applicant's."
  },
  {
    "id": "q122",
    "topic": "Oath of Citizenship",
    "subtopic": "The Oath",
    "question": "Who administers the Oath of Citizenship at a ceremony?",
    "options": [
      "The Prime Minister of Canada",
      "The Governor General of Canada",
      "A Citizenship Judge or Citizenship Commissioner",
      "A member of the RCMP"
    ],
    "answerIndex": 2,
    "explanation": "The Oath of Citizenship is administered by a Citizenship Judge or a Citizenship Commissioner, who presides over the citizenship ceremony on behalf of the Government of Canada."
  },
  {
    "id": "q123",
    "topic": "Oath of Citizenship",
    "subtopic": "The Oath",
    "question": "What does 'bearing true allegiance' in the Oath mean?",
    "options": [
      "Serving in the Canadian military",
      "Paying all taxes on time",
      "Being loyal and faithful to Canada and its Sovereign",
      "Learning to speak English or French perfectly"
    ],
    "answerIndex": 2,
    "explanation": "Bearing true allegiance means being loyal and faithful to Canada, its values, and its Sovereign (the King or Queen). It is a commitment to put Canada's interests and well-being at heart."
  },
  {
    "id": "q124",
    "topic": "Oath of Citizenship",
    "subtopic": "Ceremony",
    "question": "What typically happens at a citizenship ceremony after the Oath is taken?",
    "options": [
      "New citizens immediately receive a Canadian passport",
      "New citizens receive their citizenship certificate and often sing O Canada",
      "New citizens are assigned to a province of residence",
      "New citizens must immediately register to vote"
    ],
    "answerIndex": 1,
    "explanation": "After taking the Oath, new citizens typically receive their citizenship certificate and often sing O Canada together. The ceremony is a formal and celebratory occasion marking their official entry into Canadian citizenship."
  },
  {
    "id": "q125",
    "topic": "Oath of Citizenship",
    "subtopic": "Ceremony",
    "question": "Children under what age do NOT have to take the Oath of Citizenship?",
    "options": [
      "10",
      "14",
      "16",
      "18"
    ],
    "answerIndex": 1,
    "explanation": "Children under 14 years of age are not required to take the Oath of Citizenship. They are still granted citizenship, but the oath requirement applies to those who are 14 and older."
  },
  {
    "id": "q126",
    "topic": "Oath of Citizenship",
    "subtopic": "Ceremony",
    "question": "What is the Canadian flag's role at a citizenship ceremony?",
    "options": [
      "It is not present at citizenship ceremonies",
      "It is signed by the new citizens as part of the ceremony",
      "It is displayed prominently as a symbol of Canada and the new citizens' commitment",
      "It is given to each new citizen as a gift"
    ],
    "answerIndex": 2,
    "explanation": "The Canadian flag is displayed prominently at every citizenship ceremony. It serves as a symbol of Canada and the values and identity that new citizens are committing to uphold."
  },
  {
    "id": "q127",
    "topic": "Oath of Citizenship",
    "subtopic": "The Oath",
    "question": "Which of the following phrases is part of the Oath of Citizenship?",
    "options": [
      "'I will defend Canada against all enemies, foreign and domestic'",
      "'I will faithfully observe the laws of Canada'",
      "'I renounce all prior allegiances and citizenships'",
      "'I will serve Canada in its military forces if called upon'"
    ],
    "answerIndex": 1,
    "explanation": "The Oath of Citizenship includes the phrase 'I will faithfully observe the laws of Canada and fulfil my duties as a Canadian citizen.' There is no requirement to renounce other citizenships or serve in the military."
  },
  {
    "id": "q128",
    "topic": "Oath of Citizenship",
    "subtopic": "Significance",
    "question": "What document is sometimes given to new citizens at or after the citizenship ceremony as a symbol of their rights?",
    "options": [
      "A copy of the Constitution Act, 1867",
      "A copy of the Canadian Charter of Rights and Freedoms",
      "A copy of the Income Tax Act",
      "A copy of the Criminal Code of Canada"
    ],
    "answerIndex": 1,
    "explanation": "New citizens are often presented with a copy of the Canadian Charter of Rights and Freedoms at or around the citizenship ceremony, symbolizing the rights and freedoms they now enjoy as Canadian citizens."
  },
  {
    "id": "q129",
    "topic": "Oath of Citizenship",
    "subtopic": "Significance",
    "question": "Can a person become a Canadian citizen without taking the Oath of Citizenship?",
    "options": [
      "Yes, if they are a permanent resident for more than 10 years",
      "Yes, but only if they are born to a Canadian parent",
      "No — taking the Oath is the final and essential step in becoming a citizen (for those 14+)",
      "Yes, if they have a Canadian spouse"
    ],
    "answerIndex": 2,
    "explanation": "For applicants aged 14 and over, taking the Oath of Citizenship is the final and mandatory step in becoming a Canadian citizen. Without taking the Oath at a ceremony, citizenship is not granted."
  },
  {
    "id": "q130",
    "topic": "Oath of Citizenship",
    "subtopic": "Significance",
    "question": "What does taking the Oath of Citizenship represent for a new citizen?",
    "options": [
      "A promise to live in Canada permanently and never leave",
      "A formal acceptance of Canada's values, laws, and the responsibilities of citizenship",
      "A legal requirement to give up their original language",
      "An agreement to pay taxes for life"
    ],
    "answerIndex": 1,
    "explanation": "Taking the Oath of Citizenship represents a new citizen's formal commitment to Canada's values — including democracy, the rule of law, and respect for rights — and their acceptance of the responsibilities of citizenship."
  },
  {
    "id": "q131",
    "topic": "Oath of Citizenship",
    "subtopic": "The Oath",
    "question": "In the Oath of Citizenship, what does the phrase 'His/Her Majesty, King/Queen of Canada, His/Her Heirs and Successors' refer to?",
    "options": [
      "The Prime Minister and future Prime Ministers",
      "The Governor General and future Governors General",
      "The reigning Sovereign and all future monarchs of Canada",
      "The founding fathers of Confederation"
    ],
    "answerIndex": 2,
    "explanation": "This phrase refers to the current Sovereign (King or Queen of Canada) and all future monarchs who will succeed to the throne. Canada is a constitutional monarchy and the Sovereign is the head of state."
  },
  {
    "id": "q132",
    "topic": "Oath of Citizenship",
    "subtopic": "Ceremony",
    "question": "How are new citizens typically notified that they are approved for the citizenship ceremony?",
    "options": [
      "By a telephone call from the Prime Minister's office",
      "They are sent a Notice to Appear for the citizenship ceremony by Immigration, Refugees and Citizenship Canada (IRCC)",
      "By seeing their name in a newspaper",
      "By receiving an email from Elections Canada"
    ],
    "answerIndex": 1,
    "explanation": "Once a citizenship application is approved, Immigration, Refugees and Citizenship Canada (IRCC) sends a Notice to Appear for the citizenship ceremony, telling the applicant when and where to attend."
  },
  {
    "id": "q133",
    "topic": "Oath of Citizenship",
    "subtopic": "The Oath",
    "question": "Which of the following best describes what 'fulfilling duties as a Canadian citizen' means?",
    "options": [
      "Only paying taxes",
      "Living in Canada for at least 6 months per year",
      "Responsibilities such as obeying laws, voting, serving on juries, and defending Canada if needed",
      "Speaking English or French in all public situations"
    ],
    "answerIndex": 2,
    "explanation": "Fulfilling duties as a Canadian citizen means obeying the laws, participating in democracy (such as voting), serving on juries when called, protecting Canada's heritage and environment, and helping keep Canada strong and free."
  },
  {
    "id": "q134",
    "topic": "Oath of Citizenship",
    "subtopic": "History",
    "question": "Has the Oath of Citizenship always been the same since Confederation?",
    "options": [
      "Yes, it has been unchanged since 1867",
      "No, the oath has been updated over time — notably in 2021 to include a reference to the rights of Aboriginal peoples",
      "No, it was only introduced in 1982 with the Charter",
      "Yes, the oath has always referenced the King or Queen"
    ],
    "answerIndex": 1,
    "explanation": "The Oath of Citizenship has been updated over time. Most recently, in 2021, the oath was amended to include a commitment to uphold the treaties with Indigenous peoples — recognizing Canada's relationship with its First Nations, Métis, and Inuit peoples."
  },
  {
    "id": "q135",
    "topic": "Oath of Citizenship",
    "subtopic": "History",
    "question": "What was added to the Oath of Citizenship in 2021?",
    "options": [
      "A promise to learn both English and French",
      "A commitment to uphold the treaties with Indigenous peoples of Canada",
      "A pledge to serve in the Canadian Armed Forces",
      "A reference to the Canadian Charter of Rights and Freedoms"
    ],
    "answerIndex": 1,
    "explanation": "In 2021, the Oath of Citizenship was updated to include a commitment to 'faithfully observe the laws of Canada including the Constitution, which recognizes and affirms the Aboriginal and treaty rights of First Nations, Inuit and Métis peoples.' This was a historic change recognizing Indigenous rights."
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
    topic = "Oath of Citizenship"
    count = len([q for q in existing if q['topic'] == topic])
    print(f"Added {added} questions. '{topic}' now has {count} questions. Total: {len(existing)}")

if __name__ == '__main__':
    main()
