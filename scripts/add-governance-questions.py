#!/usr/bin/env python3
"""
Add new 'How Canadians Govern Themselves' questions (q256–q305).
"""
import json, os

DATA_FILE = os.path.join(os.path.dirname(__file__), '../src/assets/data/questions.json')

NEW_QUESTIONS = [
  {
    "id": "q256",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "System of Government",
    "question": "What does it mean that Canada is a constitutional monarchy?",
    "options": [
      "The monarch makes all laws in Canada",
      "Canada is ruled by a king or queen who has absolute power",
      "The King or Queen is the head of state, but their powers are limited by the Constitution and exercised through elected representatives",
      "Canada's constitution requires a vote before any royal decisions"
    ],
    "answerIndex": 2,
    "explanation": "In a constitutional monarchy, the monarch (King or Queen) is the head of state, but their powers are defined and limited by the Constitution. In practice, democratic elected governments exercise power, with the monarch playing a ceremonial role."
  },
  {
    "id": "q257",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "System of Government",
    "question": "What does it mean that Canada is a federal state?",
    "options": [
      "All political power rests with the federal government in Ottawa",
      "Canada is divided into military regions each governed by a general",
      "Powers are divided between the federal government and provincial/territorial governments",
      "Each province operates as an independent nation"
    ],
    "answerIndex": 2,
    "explanation": "Canada is a federal state, meaning power is divided between a central (federal) government in Ottawa and provincial/territorial governments. Each level has its own area of jurisdiction as defined by the Constitution."
  },
  {
    "id": "q258",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "System of Government",
    "question": "What does it mean that Canada is a parliamentary democracy?",
    "options": [
      "Citizens vote directly on all laws",
      "The President governs with a Cabinet appointed by Parliament",
      "The government is elected by the people through Parliament, and must maintain the confidence of the House of Commons",
      "All provinces are governed by a national parliament with no provincial legislatures"
    ],
    "answerIndex": 2,
    "explanation": "In a parliamentary democracy, citizens elect representatives to Parliament. The government (Cabinet/Prime Minister) must maintain the support (confidence) of the elected House of Commons. If it loses a confidence vote, the government must resign or call an election."
  },
  {
    "id": "q259",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "The Crown",
    "question": "What are the three levels of government in Canada?",
    "options": [
      "Municipal, provincial, and federal",
      "Local, regional, and national",
      "City, county, and national",
      "Municipal, district, and federal"
    ],
    "answerIndex": 0,
    "explanation": "Canada has three main levels of government: federal (national), provincial/territorial, and municipal (local — cities, towns, and counties). Each level has different responsibilities and powers."
  },
  {
    "id": "q260",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "Parliament",
    "question": "What is the role of the House of Commons?",
    "options": [
      "To appoint the Prime Minister",
      "To review and approve the federal budget only",
      "The elected lower house of Parliament — it debates, amends, and passes federal legislation and holds the government accountable",
      "To supervise provincial governments"
    ],
    "answerIndex": 2,
    "explanation": "The House of Commons is the elected lower house of the Canadian Parliament. MPs debate and vote on legislation, approve government spending, and hold the government accountable through questions and votes. The government must maintain the confidence of the House."
  },
  {
    "id": "q261",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "Parliament",
    "question": "What is the Speaker of the House of Commons?",
    "options": [
      "The leader of the governing party in Parliament",
      "An MP elected by fellow MPs to preside over House debates and maintain order",
      "The person who reads the Speech from the Throne",
      "A Senator who acts as a liaison between the Senate and House"
    ],
    "answerIndex": 1,
    "explanation": "The Speaker of the House of Commons is an MP elected by their fellow MPs to preside over debates in the House, maintain order, and ensure the rules of Parliament are followed. The Speaker acts in a neutral, non-partisan manner."
  },
  {
    "id": "q262",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "Parliament",
    "question": "What is the Speech from the Throne?",
    "options": [
      "A speech by the Prime Minister at the start of each Parliament outlining the government's priorities",
      "A speech delivered by the Governor General, written by the government, outlining its legislative priorities for the new Parliament or session",
      "An annual address by the Sovereign to all Canadians",
      "A formal declaration of war or national emergency"
    ],
    "answerIndex": 1,
    "explanation": "The Speech from the Throne is delivered by the Governor General (on behalf of the government) at the opening of each new Parliament or session of Parliament. It outlines the government's legislative priorities and agenda. It is written by the governing party."
  },
  {
    "id": "q263",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "Senate",
    "question": "How many Senators are in the Canadian Senate?",
    "options": [
      "50",
      "75",
      "105",
      "338"
    ],
    "answerIndex": 2,
    "explanation": "The Canadian Senate has 105 seats. Senators are appointed by the Governor General on the advice of the Prime Minister and represent Canada's regions: Ontario (24), Quebec (24), the Maritime provinces (24), and Western Canada (24), plus Newfoundland and the territories."
  },
  {
    "id": "q264",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "Senate",
    "question": "Until what age may Canadian Senators serve?",
    "options": [
      "65",
      "70",
      "75",
      "80"
    ],
    "answerIndex": 2,
    "explanation": "Canadian Senators are appointed until the mandatory retirement age of 75. They are appointed by the Governor General on the advice of the Prime Minister. Before 1965, Senators served for life."
  },
  {
    "id": "q265",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "Cabinet",
    "question": "What is the Cabinet?",
    "options": [
      "All elected MPs from the governing party",
      "A group of senior Ministers chosen by the Prime Minister to head government departments and advise on policy",
      "A committee of all party leaders in Parliament",
      "A permanent group of senior civil servants who run the government"
    ],
    "answerIndex": 1,
    "explanation": "The Cabinet consists of senior ministers chosen by the Prime Minister from among MPs (usually). Each Cabinet minister is responsible for a government department (e.g., Finance, Health, Justice). The Cabinet collectively sets government policy."
  },
  {
    "id": "q266",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "Cabinet",
    "question": "What is Cabinet solidarity?",
    "options": [
      "The requirement that all Cabinet ministers vote together in Parliament",
      "The tradition that Cabinet ministers must publicly support all Cabinet decisions — or resign from Cabinet",
      "The requirement that the Cabinet includes members from every province",
      "The practice of Cabinet ministers attending each other's public events"
    ],
    "answerIndex": 1,
    "explanation": "Cabinet solidarity (or collective responsibility) is the tradition that all Cabinet ministers must publicly support Cabinet decisions, even if they privately disagreed. If a minister cannot support a decision, they are expected to resign from Cabinet."
  },
  {
    "id": "q267",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "Legislation",
    "question": "What is a 'confidence vote' in Parliament?",
    "options": [
      "A vote where MPs assess the public popularity of the Prime Minister",
      "A key vote (such as a budget vote) where if the government loses, it must resign or call an election",
      "A vote to appoint a new Governor General",
      "A referendum held by the people on a major issue"
    ],
    "answerIndex": 1,
    "explanation": "A confidence vote is a parliamentary vote on which the government's ability to continue governing depends. Key votes — like the budget, the Speech from the Throne, or explicit non-confidence motions — are confidence votes. If the government loses one, it must resign or request the GG to dissolve Parliament."
  },
  {
    "id": "q268",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "Legislation",
    "question": "What is 'Royal Assent'?",
    "options": [
      "The vote in the Senate that passes a bill",
      "The Prime Minister's signature required on all new laws",
      "The Governor General's (or Sovereign's) formal approval of a bill passed by Parliament, making it law",
      "A public referendum required before major legislation is enacted"
    ],
    "answerIndex": 2,
    "explanation": "Royal Assent is the final step in the legislative process. After a bill has passed both the House of Commons and the Senate, it is presented to the Governor General (representing the Sovereign) for Royal Assent — their formal approval — which makes it law."
  },
  {
    "id": "q269",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "Legislation",
    "question": "What is a 'bill' in the Canadian Parliament?",
    "options": [
      "A list of government expenses submitted to Parliament",
      "A proposed law introduced in Parliament for debate, amendment, and voting",
      "An emergency decree issued by the Prime Minister",
      "A formal complaint against the government"
    ],
    "answerIndex": 1,
    "explanation": "A bill is a proposed law introduced in Parliament. It must pass three readings in the House of Commons, three readings in the Senate, and then receive Royal Assent before it becomes law. Bills can originate in either House."
  },
  {
    "id": "q270",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "Federal vs Provincial",
    "question": "Which of the following is a federal (national) government responsibility?",
    "options": [
      "Building local roads",
      "Regulating hospitals",
      "Managing immigration and citizenship",
      "Running provincial universities"
    ],
    "answerIndex": 2,
    "explanation": "Immigration and citizenship are federal (national) government responsibilities, as are national defence, foreign policy, criminal law, banking, trade, and postal service. Education, health care, and highways are provincial responsibilities."
  },
  {
    "id": "q271",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "Federal vs Provincial",
    "question": "What is 'Peace, Order, and Good Government' (POGG)?",
    "options": [
      "The motto of the Royal Canadian Mounted Police",
      "A general power granted to the federal Parliament to make laws for Canada's peace, order, and good government — the basis of federal legislative authority",
      "The three principles of the Canadian judiciary",
      "The principles listed in the preamble to the Charter of Rights"
    ],
    "answerIndex": 1,
    "explanation": "'Peace, Order, and Good Government' (POGG) is the general grant of legislative power to the federal Parliament under the Constitution Act, 1867. It reflects Canada's distinct approach to government compared to the American emphasis on 'life, liberty, and the pursuit of happiness.'"
  },
  {
    "id": "q272",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "Provincial Government",
    "question": "What is the head of a provincial government called?",
    "options": [
      "The Provincial Prime Minister",
      "The Premier",
      "The Governor",
      "The Lieutenant Governor"
    ],
    "answerIndex": 1,
    "explanation": "The head of a provincial government is called the Premier (or in French, Premier ministre). The Premier leads the party with the most seats in the provincial legislature and is the head of the provincial executive."
  },
  {
    "id": "q273",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "Provincial Government",
    "question": "What is a Lieutenant Governor?",
    "options": [
      "The second-in-command to the Premier in each province",
      "The representative of the Sovereign (King/Queen) in each province",
      "A military officer in charge of provincial security",
      "The head of a provincial Supreme Court"
    ],
    "answerIndex": 1,
    "explanation": "The Lieutenant Governor is the representative of the Sovereign (King/Queen) in each Canadian province. Like the Governor General at the federal level, the Lieutenant Governor performs constitutional and ceremonial functions in the province."
  },
  {
    "id": "q274",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "Provincial Government",
    "question": "What are provincial legislators called in most provinces?",
    "options": [
      "Members of Parliament (MPs)",
      "Members of the Provincial Assembly (MPAs)",
      "Members of the Legislative Assembly (MLAs) — or MPPs in Ontario, MNAs in Quebec, MHAs in Newfoundland",
      "Provincial Senators"
    ],
    "answerIndex": 2,
    "explanation": "Elected members of provincial legislatures are most commonly called Members of the Legislative Assembly (MLAs). However, Ontario calls them MPPs (Members of Provincial Parliament), Quebec calls them MNAs (Members of the National Assembly), and Newfoundland calls them MHAs (Members of the House of Assembly)."
  },
  {
    "id": "q275",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "Municipal Government",
    "question": "What is the head of a municipal (city or town) government typically called?",
    "options": [
      "Premier",
      "Governor",
      "Mayor (or Reeve for smaller municipalities)",
      "District Councillor"
    ],
    "answerIndex": 2,
    "explanation": "The head of a municipal government is typically called a Mayor (in cities and larger towns). In smaller municipalities and rural areas, the elected head may be called a Reeve. Mayors/Reeves work with councils of elected councillors or aldermen."
  },
  {
    "id": "q276",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "First Nations Government",
    "question": "Do First Nations in Canada have their own forms of government?",
    "options": [
      "No — First Nations are governed exclusively by municipal governments",
      "Yes — First Nations communities have band councils and other traditional governing structures recognized under the Indian Act and self-government agreements",
      "No — the federal government directly manages all First Nations communities",
      "Yes, but only for cultural and ceremonial purposes"
    ],
    "answerIndex": 1,
    "explanation": "First Nations communities have their own forms of government. Under the Indian Act, most have elected band councils with a chief and councillors. Many First Nations are also negotiating or have achieved self-government agreements with the federal and provincial governments."
  },
  {
    "id": "q277",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "Separation of Powers",
    "question": "What are the three branches of government in Canada?",
    "options": [
      "Federal, provincial, and municipal",
      "Legislative, executive, and judicial",
      "Senate, House of Commons, and Supreme Court",
      "Prime Minister, Cabinet, and Parliament"
    ],
    "answerIndex": 1,
    "explanation": "Canada's government is organized into three branches: the Legislative branch (Parliament — makes laws), the Executive branch (Governor General, Prime Minister, and Cabinet — implements laws), and the Judicial branch (courts — interprets laws). These branches provide checks and balances."
  },
  {
    "id": "q278",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "Legislation",
    "question": "What is the difference between a public bill and a private member's bill?",
    "options": [
      "There is no difference — all bills are identical in process",
      "A public bill is introduced by a Cabinet minister on behalf of the government; a private member's bill is introduced by a backbench MP who is not a Cabinet minister",
      "A public bill applies to all Canadians; a private member's bill only applies to one person",
      "A public bill must be voted on by citizens; a private member's bill only requires a Senate vote"
    ],
    "answerIndex": 1,
    "explanation": "A government bill (public bill) is introduced by a Cabinet minister on behalf of the government and has priority in Parliament. A private member's bill is introduced by any MP who is not a Cabinet minister. Private members' bills rarely become law but can raise important issues."
  },
  {
    "id": "q279",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "System of Government",
    "question": "What is the 'Privy Council' in Canada?",
    "options": [
      "Canada's highest court",
      "A formal body that advises the Governor General; in practice, the Cabinet acts as its active committee",
      "A committee of provincial premiers",
      "The administrative body that runs Canada's prison system"
    ],
    "answerIndex": 1,
    "explanation": "The Privy Council of Canada is a formal body that advises the Governor General. In practice, only the active members — the Cabinet (sworn in as Privy Councillors) — exercise real power. The Privy Council Office (PCO) supports the Prime Minister and Cabinet."
  },
  {
    "id": "q280",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "Federal vs Provincial",
    "question": "Is immigration a shared (concurrent) responsibility in Canada?",
    "options": [
      "No — immigration is exclusively a federal responsibility",
      "Yes — immigration is a shared responsibility between federal and provincial governments",
      "No — immigration is exclusively a provincial responsibility",
      "Immigration is managed by municipalities"
    ],
    "answerIndex": 1,
    "explanation": "Immigration is one of the areas of shared (concurrent) jurisdiction in Canada — both federal and provincial governments have authority over it. Agriculture is also shared. However, federal law prevails where there is a conflict with provincial law on immigration."
  },
  {
    "id": "q281",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "System of Government",
    "question": "What is the role of the civil service (public service) in Canada?",
    "options": [
      "To elect Members of Parliament",
      "To design and pass laws",
      "To implement government policies and programs, providing non-partisan expertise and service delivery",
      "To advise the Governor General on appointments"
    ],
    "answerIndex": 2,
    "explanation": "The civil service (public service) consists of government employees who implement government policies and deliver public services. Civil servants are non-partisan — they serve whatever government is in power. They provide expertise, continuity, and administrative support."
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
    topic = "How Canadians Govern Themselves"
    count = len([q for q in existing if q['topic'] == topic])
    print(f"Added {added} questions. '{topic}' now has {count} questions. Total: {len(existing)}")

if __name__ == '__main__':
    main()
