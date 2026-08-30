#!/usr/bin/env python3
"""
Add new Rights and Responsibilities of Citizenship questions (q136–q175).
"""
import json, os

DATA_FILE = os.path.join(os.path.dirname(__file__), '../src/assets/data/questions.json')

NEW_QUESTIONS = [
  {
    "id": "q136",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Magna Carta",
    "question": "What is the Magna Carta and why is it important to Canada?",
    "options": [
      "A French law establishing Quebec's civil code",
      "A 1215 English document that established the principle that everyone, including the king, is subject to the law — the foundation of Canadian rights",
      "The first Canadian Constitution signed in 1867",
      "A UN declaration adopted by Canada in 1948"
    ],
    "answerIndex": 1,
    "explanation": "The Magna Carta, signed in England in 1215, established the principle that everyone is subject to the law — including rulers. This 800-year-old tradition of rights and freedoms is the foundation of Canada's democratic values and legal system."
  },
  {
    "id": "q137",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Charter",
    "question": "When was the Canadian Charter of Rights and Freedoms added to the Constitution?",
    "options": [
      "1867",
      "1931",
      "1982",
      "1999"
    ],
    "answerIndex": 2,
    "explanation": "The Canadian Charter of Rights and Freedoms was entrenched in the Constitution on April 17, 1982, as part of the Constitution Act, 1982. It guarantees fundamental rights and freedoms to all people in Canada."
  },
  {
    "id": "q138",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Charter",
    "question": "Who does the Canadian Charter of Rights and Freedoms apply to?",
    "options": [
      "Only Canadian citizens",
      "Only permanent residents and citizens",
      "Everyone in Canada, including visitors and non-citizens",
      "Only people born in Canada"
    ],
    "answerIndex": 2,
    "explanation": "The Canadian Charter of Rights and Freedoms protects everyone in Canada — citizens, permanent residents, visitors, and others — from government actions that violate their rights. Some rights, like voting, apply only to citizens."
  },
  {
    "id": "q139",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Fundamental Freedoms",
    "question": "What is 'freedom of expression' as protected by the Charter?",
    "options": [
      "The right to say anything without any consequences",
      "The right to hold and express opinions, including through the press and media, without government censorship",
      "The right to express oneself only in English",
      "Freedom from having to explain one's actions to the government"
    ],
    "answerIndex": 1,
    "explanation": "Freedom of expression protects the right to hold opinions and express them through speech, writing, art, and the press without government censorship. It does not protect hate speech, incitement to violence, or other harmful expression."
  },
  {
    "id": "q140",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Fundamental Freedoms",
    "question": "What does 'freedom of peaceful assembly' mean?",
    "options": [
      "The right to own property and live quietly",
      "The right to gather peacefully with others, such as at demonstrations or meetings",
      "The right to attend religious services without interference",
      "The right to live without being disturbed by neighbours"
    ],
    "answerIndex": 1,
    "explanation": "Freedom of peaceful assembly means Canadians have the right to gather peacefully with others — at protests, demonstrations, meetings, or other events — without government interference, as long as the gathering is peaceful."
  },
  {
    "id": "q141",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Fundamental Freedoms",
    "question": "What does 'freedom of association' protect?",
    "options": [
      "The right to live wherever you choose in Canada",
      "The right to form and join organizations such as political parties, trade unions, and religious groups",
      "The right to remain anonymous in public",
      "The right not to associate with those you dislike"
    ],
    "answerIndex": 1,
    "explanation": "Freedom of association protects the right to form or join organizations of your choosing — including political parties, trade unions, professional associations, religious groups, and other groups — without undue government interference."
  },
  {
    "id": "q142",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Democratic Rights",
    "question": "What is the right of every Canadian citizen with respect to voting?",
    "options": [
      "The right to vote once in a lifetime in a federal election",
      "The right to vote in federal, provincial, and territorial elections if 18 or older",
      "The right to vote only if they have lived in Canada for 10 years",
      "The right to vote in federal elections only"
    ],
    "answerIndex": 1,
    "explanation": "Every Canadian citizen aged 18 and over has the right to vote in federal, provincial, and territorial elections. This democratic right is protected by the Charter and is one of the most important rights of citizenship."
  },
  {
    "id": "q143",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Democratic Rights",
    "question": "What is the right to run for elected office?",
    "options": [
      "The right of any resident of Canada to become a politician",
      "The right of any Canadian citizen 18 or older to seek election to Parliament or a provincial/territorial legislature",
      "The right of any citizen with a university degree to seek office",
      "The right reserved only for those who have lived in Canada for 10 years"
    ],
    "answerIndex": 1,
    "explanation": "Canadian citizens aged 18 and older have the right to run for elected office — in federal, provincial, or territorial elections. This right is protected by the Charter and is exclusive to Canadian citizens."
  },
  {
    "id": "q144",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Mobility Rights",
    "question": "What are mobility rights under the Charter?",
    "options": [
      "The right of all Canadians to own and operate a vehicle",
      "The right of citizens to enter, remain in, and leave Canada, and to move between provinces for work",
      "The right to move between countries without a passport",
      "The right to live in any country as a Canadian citizen"
    ],
    "answerIndex": 1,
    "explanation": "Mobility rights under the Charter give Canadian citizens the right to enter, remain in, and leave Canada. They also give citizens and permanent residents the right to move to and earn a livelihood in any province or territory."
  },
  {
    "id": "q145",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Legal Rights",
    "question": "What does the right to 'life, liberty and security of the person' mean?",
    "options": [
      "The government must provide housing and food to all Canadians",
      "Canadians are protected from arbitrary government actions that threaten their physical or psychological wellbeing",
      "Canadians have the right to carry weapons for self-defence",
      "The government must guarantee employment to all citizens"
    ],
    "answerIndex": 1,
    "explanation": "The Charter protects the right to life, liberty, and security of the person. This means the government cannot arbitrarily deprive people of their life, freedom, or bodily integrity — it is a foundational protection against state overreach."
  },
  {
    "id": "q146",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Legal Rights",
    "question": "What does the right 'not to be arbitrarily detained or imprisoned' mean?",
    "options": [
      "Police can never arrest anyone without consent",
      "No one can be held by police or the government without a lawful reason",
      "Citizens can only be detained if a judge is present",
      "Canadians cannot be deported"
    ],
    "answerIndex": 1,
    "explanation": "The Charter protects everyone from arbitrary detention or imprisonment. Police must have legal grounds (e.g., reasonable cause to suspect a crime) to detain someone. Random stops and searches without cause are not permitted."
  },
  {
    "id": "q147",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Equality Rights",
    "question": "What does Section 15 (Equality Rights) of the Charter guarantee?",
    "options": [
      "Equal pay for all government employees",
      "Equal benefit and protection of the law without discrimination based on race, national origin, colour, religion, sex, age, or disability",
      "Equality of outcomes in all economic situations",
      "The right of all Canadians to access the same services"
    ],
    "answerIndex": 1,
    "explanation": "Section 15 of the Charter (Equality Rights) guarantees that every individual is equal before and under the law and has equal benefit and protection of the law without discrimination based on race, national or ethnic origin, colour, religion, sex, age, or mental or physical disability."
  },
  {
    "id": "q148",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Language Rights",
    "question": "What are official language rights in Canada?",
    "options": [
      "The right of all immigrants to have government services in their native language",
      "The right to use English or French in Parliament, federal courts, and federal government services",
      "The right to receive education in any language of one's choice",
      "The requirement for all Canadians to be bilingual"
    ],
    "answerIndex": 1,
    "explanation": "Official language rights protect the right to use English or French in Parliament, federal courts, and to receive federal government services in either official language. These rights reflect Canada's bilingual character."
  },
  {
    "id": "q149",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Aboriginal Rights",
    "question": "What does Section 35 of the Constitution Act, 1982 do?",
    "options": [
      "Creates the Canadian Charter of Rights and Freedoms",
      "Establishes the Senate as part of Parliament",
      "Recognizes and affirms the existing Aboriginal and treaty rights of Indigenous peoples of Canada",
      "Grants women the right to vote"
    ],
    "answerIndex": 2,
    "explanation": "Section 35 of the Constitution Act, 1982 recognizes and affirms the existing Aboriginal and treaty rights of the Indigenous peoples of Canada — the First Nations, Inuit, and Métis peoples. This is a distinct set of rights outside of the Charter."
  },
  {
    "id": "q150",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Responsibilities",
    "question": "What does it mean to 'help keep Canada strong and free'?",
    "options": [
      "Serving in the Canadian military",
      "Paying the highest possible taxes",
      "Contributing to the community through volunteering, voting, obeying the law, and participating in civic life",
      "Never criticizing the government"
    ],
    "answerIndex": 2,
    "explanation": "Helping to keep Canada strong and free means contributing positively to Canadian society — by obeying the law, voting, volunteering, protecting the environment, and participating actively in democratic life. It's a shared responsibility of all citizens."
  },
  {
    "id": "q151",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Responsibilities",
    "question": "Is military service compulsory (required) in Canada?",
    "options": [
      "Yes, all citizens must serve 2 years",
      "Yes, but only citizens between 18 and 30",
      "No, serving in the Canadian Armed Forces is voluntary",
      "Yes, in times of war all citizens must serve"
    ],
    "answerIndex": 2,
    "explanation": "Military service is not compulsory in Canada. Serving in the Canadian Armed Forces is voluntary. However, if Canada is attacked, citizens may be called upon to help defend the country."
  },
  {
    "id": "q152",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Responsibilities",
    "question": "Why is voting considered both a right AND a responsibility?",
    "options": [
      "Because it is legally mandatory in Canada",
      "Because every citizen should participate in democracy to shape their government and community",
      "Because it is required to maintain permanent residency",
      "Because failing to vote results in a fine"
    ],
    "answerIndex": 1,
    "explanation": "While voting is not legally mandatory in Canada, it is considered a civic responsibility — a way for citizens to shape their government and ensure democracy works. Citizens who do not vote give up their voice in how their country is run."
  },
  {
    "id": "q153",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Responsibilities",
    "question": "What is the responsibility of Canadians toward the environment?",
    "options": [
      "To avoid using public parks",
      "To protect and preserve Canada's natural environment for future generations",
      "To leave environmental decisions entirely to the government",
      "To pay special environmental taxes"
    ],
    "answerIndex": 1,
    "explanation": "Canadian citizens are responsible for protecting and preserving Canada's natural environment. This is a duty to future generations — to keep Canada's lakes, rivers, forests, and wildlife healthy and intact."
  },
  {
    "id": "q154",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Charter",
    "question": "What is the 'notwithstanding clause' (Section 33) in the Charter?",
    "options": [
      "A clause that guarantees the right to bear arms",
      "A clause that allows Parliament or a provincial legislature to temporarily override certain Charter rights",
      "A clause that makes all laws subject to United Nations approval",
      "A clause that grants the Supreme Court power to make laws"
    ],
    "answerIndex": 1,
    "explanation": "The notwithstanding clause (Section 33) allows Parliament or a provincial legislature to pass a law that operates 'notwithstanding' (in spite of) certain Charter rights. It can override some rights for up to 5 years and must be explicitly invoked."
  },
  {
    "id": "q155",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Multiculturalism",
    "question": "What does the Canadian Multiculturalism Act of 1988 do?",
    "options": [
      "It requires all immigrants to give up their cultural heritage",
      "It prohibits the use of languages other than English and French in public",
      "It affirms Canada's commitment to a multicultural society where all cultural heritages are valued",
      "It makes multiculturalism a recommendation, not a legal commitment"
    ],
    "answerIndex": 2,
    "explanation": "The Canadian Multiculturalism Act of 1988 was the world's first national multiculturalism law. It affirms that multiculturalism is a fundamental characteristic of Canadian heritage and commits the government to preserving and enhancing this diversity."
  },
  {
    "id": "q156",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Rule of Law",
    "question": "Which of the following best illustrates the 'rule of law' in Canada?",
    "options": [
      "A judge who dismisses charges against a politician because of their status",
      "Police ignoring a crime committed by a wealthy person",
      "A Prime Minister who is investigated and charged for breaking the law",
      "A law that only applies to certain ethnic groups"
    ],
    "answerIndex": 2,
    "explanation": "The rule of law means everyone, including the most powerful people in government, is equally subject to the law. If a Prime Minister breaks the law, they can be investigated and charged just like any other person — no one is above the law."
  },
  {
    "id": "q157",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Responsibilities",
    "question": "What is the responsibility of supporting oneself and one's family?",
    "options": [
      "A requirement only for immigrants in their first 3 years",
      "A core responsibility of citizenship — working to be self-sufficient and supporting family members where possible",
      "A legal obligation enforced by the courts for everyone",
      "A recommendation that applies only to wealthy Canadians"
    ],
    "answerIndex": 1,
    "explanation": "Supporting oneself and one's family is a fundamental responsibility of Canadian citizenship. Citizens are expected to work toward being self-sufficient and to support their family members as best they can."
  },
  {
    "id": "q158",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Legal Rights",
    "question": "What is the right against 'unreasonable search and seizure'?",
    "options": [
      "Police cannot enter private property under any circumstances",
      "Canadians are protected from being searched by police without proper legal authority (e.g., a warrant)",
      "The government cannot audit anyone's tax returns",
      "Citizens can refuse to cooperate with any police request"
    ],
    "answerIndex": 1,
    "explanation": "Section 8 of the Charter protects against unreasonable search and seizure. Police generally need a warrant (court authorization) to search a person's property or seize their belongings. Evidence obtained illegally may be excluded from court."
  },
  {
    "id": "q159",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Responsibilities",
    "question": "What does 'respecting the rights of others' mean as a civic responsibility?",
    "options": [
      "Agreeing with everything other people say",
      "Recognizing that other people also have Charter rights and freedoms that must not be violated",
      "Giving money to charities",
      "Avoiding any disagreement in public"
    ],
    "answerIndex": 1,
    "explanation": "Respecting the rights of others means recognizing that every person in Canada has the same Charter rights and freedoms. Citizens must not infringe on others' rights — for example, not engaging in hate speech, discrimination, or harassment."
  },
  {
    "id": "q160",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Charter",
    "question": "What are 'minority language education rights' in the Charter?",
    "options": [
      "The right of any minority to receive education in their heritage language",
      "The right of French-speaking minorities outside Quebec and English-speaking minorities in Quebec to have their children educated in their official language",
      "The right of immigrants to receive bilingual education",
      "The right of Inuit children to be educated in Inuktitut"
    ],
    "answerIndex": 1,
    "explanation": "Section 23 of the Charter protects minority language education rights — specifically, the right of French-speaking Canadians living outside Quebec, and English-speaking Canadians in Quebec, to have their children educated in their official language where numbers warrant."
  },
  {
    "id": "q161",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "History of Rights",
    "question": "What was the Canadian Bill of Rights (1960)?",
    "options": [
      "Canada's first constitution",
      "A federal statute passed under John Diefenbaker that was a precursor to the Charter, protecting basic rights at the federal level",
      "A provincial law in Ontario protecting language rights",
      "An international treaty signed by Canada"
    ],
    "answerIndex": 1,
    "explanation": "The Canadian Bill of Rights was a federal statute introduced by Prime Minister John Diefenbaker in 1960. It was a precursor to the Charter, protecting basic rights and freedoms at the federal level. Unlike the Charter, it was not entrenched in the Constitution."
  },
  {
    "id": "q162",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Responsibilities",
    "question": "Why is it important for citizens to participate in community life and volunteering?",
    "options": [
      "It is legally required to maintain citizenship",
      "It strengthens communities and supports those in need, contributing to Canada's social fabric",
      "It earns tax credits",
      "It is only important for recent immigrants"
    ],
    "answerIndex": 1,
    "explanation": "Participating in community life and volunteering strengthens Canadian communities, helps those in need, and contributes to the social fabric of Canada. Canada has a strong tradition of volunteerism and community service."
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
    topic = "Rights and Responsibilities of Citizenship"
    count = len([q for q in existing if q['topic'] == topic])
    print(f"Added {added} questions. '{topic}' now has {count} questions. Total: {len(existing)}")

if __name__ == '__main__':
    main()
