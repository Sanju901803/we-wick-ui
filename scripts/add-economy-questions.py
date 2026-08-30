#!/usr/bin/env python3
"""
Add new "Canada's Economy" questions (q337–q372).
"""
import json, os

DATA_FILE = os.path.join(os.path.dirname(__file__), '../src/assets/data/questions.json')

NEW_QUESTIONS = [
  {
    "id": "q337",
    "topic": "Canada's Economy",
    "subtopic": "Economic Overview",
    "question": "What is Canada's largest economic sector?",
    "options": [
      "Manufacturing",
      "Agriculture",
      "The service sector",
      "Natural resources"
    ],
    "answerIndex": 2,
    "explanation": "The service sector is the largest part of Canada's economy, employing the majority of Canadians. It includes banking, retail, health care, education, transportation, and hospitality. Canada has a mixed economy that balances services, manufacturing, and natural resources."
  },
  {
    "id": "q338",
    "topic": "Canada's Economy",
    "subtopic": "Natural Resources",
    "question": "Canada is one of the world's largest producers of which natural resource?",
    "options": [
      "Diamonds and gold only",
      "A wide variety of natural resources including petroleum, natural gas, minerals, forest products, and fish",
      "Tropical fruits and spices",
      "Coal only"
    ],
    "answerIndex": 1,
    "explanation": "Canada is one of the world's largest and most diversified producers of natural resources: oil and gas (especially Alberta's oil sands), minerals (gold, nickel, potash), forest products (pulp and paper, lumber), hydroelectric power, and fish. Natural resources drive exports and regional economies."
  },
  {
    "id": "q339",
    "topic": "Canada's Economy",
    "subtopic": "Trade",
    "question": "Who is Canada's largest trading partner?",
    "options": [
      "China",
      "The United Kingdom",
      "The United States of America",
      "Mexico"
    ],
    "answerIndex": 2,
    "explanation": "The United States is by far Canada's largest trading partner, accounting for the majority of Canada's exports and imports. The two countries share the world's largest bilateral trading relationship. The Canada-United States-Mexico Agreement (CUSMA/USMCA) governs trade between the three countries."
  },
  {
    "id": "q340",
    "topic": "Canada's Economy",
    "subtopic": "Trade",
    "question": "What does CUSMA (or USMCA) stand for?",
    "options": [
      "Canadian-US-Mexico Alliance",
      "Canada-United States-Mexico Agreement — the free trade agreement between the three countries",
      "Continental US-Mexico-Canada Agreement",
      "Canadian Union of Small and Medium Agribusinesses"
    ],
    "answerIndex": 1,
    "explanation": "CUSMA (Canada-United States-Mexico Agreement) — known as USMCA in the US and T-MEC in Mexico — replaced NAFTA in 2020. It governs free trade between Canada, the United States, and Mexico. Free trade has significantly shaped Canada's manufacturing sector, particularly in Ontario."
  },
  {
    "id": "q341",
    "topic": "Canada's Economy",
    "subtopic": "Manufacturing",
    "question": "Which province is the centre of Canada's manufacturing industry?",
    "options": [
      "British Columbia",
      "Alberta",
      "Ontario",
      "Quebec"
    ],
    "answerIndex": 2,
    "explanation": "Ontario is the centre of Canada's manufacturing industry. It produces automobiles, steel, pharmaceuticals, chemicals, and electronics. The 'auto belt' around southern Ontario (Windsor, Oshawa, Cambridge) is particularly important. Quebec also has significant manufacturing."
  },
  {
    "id": "q342",
    "topic": "Canada's Economy",
    "subtopic": "Natural Resources",
    "question": "What is the 'oil sands' and where are they located?",
    "options": [
      "Underwater oil deposits off the coast of Newfoundland",
      "Tar sand deposits containing oil in northern Alberta, one of the largest proven oil reserves in the world",
      "Natural oil seeps found along the Pacific coast of BC",
      "Underground oil fields beneath the Prairies of Saskatchewan"
    ],
    "answerIndex": 1,
    "explanation": "The Alberta oil sands (also called tar sands) are deposits of bitumen (a semi-solid form of petroleum) mixed with sand, clay, and water in northern Alberta. They represent one of the largest proven oil reserves in the world and are a major part of Canada's energy sector."
  },
  {
    "id": "q343",
    "topic": "Canada's Economy",
    "subtopic": "Natural Resources",
    "question": "Which Canadian province is the largest producer of hydroelectric power?",
    "options": [
      "Ontario",
      "Alberta",
      "British Columbia",
      "Quebec"
    ],
    "answerIndex": 3,
    "explanation": "Quebec is Canada's largest producer of hydroelectric power. Hydro-Québec operates an extensive system of dams and generating stations, particularly in northern Quebec. Canada overall is one of the world's leading producers of hydroelectric energy."
  },
  {
    "id": "q344",
    "topic": "Canada's Economy",
    "subtopic": "International Organizations",
    "question": "Canada is a member of which major international economic organizations?",
    "options": [
      "The European Union (EU) and OPEC",
      "The G7, the G20, the WTO, and the IMF",
      "ASEAN and the Pacific Economic Cooperation forum only",
      "The Commonwealth Economic Forum only"
    ],
    "answerIndex": 1,
    "explanation": "Canada is a member of the G7 (Group of Seven leading economies), the G20 (Group of Twenty), the World Trade Organization (WTO), and the International Monetary Fund (IMF). Canada's economy is one of the largest in the world, ranking in the top 10 by GDP."
  },
  {
    "id": "q345",
    "topic": "Canada's Economy",
    "subtopic": "Agriculture",
    "question": "Which part of Canada is known as the breadbasket — the primary wheat and grain producing region?",
    "options": [
      "The Great Lakes region of Ontario",
      "The Fraser Valley in British Columbia",
      "The Prairie provinces (Manitoba, Saskatchewan, Alberta)",
      "The St. Lawrence Valley in Quebec"
    ],
    "answerIndex": 2,
    "explanation": "The Prairie provinces — Manitoba, Saskatchewan, and Alberta — are Canada's primary wheat and grain producing region, known as the 'breadbasket.' Saskatchewan in particular is one of the world's largest producers and exporters of wheat, canola, and potash."
  },
  {
    "id": "q346",
    "topic": "Canada's Economy",
    "subtopic": "Natural Resources",
    "question": "Which province has a major offshore oil industry?",
    "options": [
      "Prince Edward Island",
      "Nova Scotia",
      "Newfoundland and Labrador",
      "New Brunswick"
    ],
    "answerIndex": 2,
    "explanation": "Newfoundland and Labrador has a significant offshore oil industry, particularly the Hibernia, Terra Nova, and White Rose oil fields off the Grand Banks. The discovery of offshore oil has transformed Newfoundland's economy since the 1990s."
  },
  {
    "id": "q347",
    "topic": "Canada's Economy",
    "subtopic": "Economic Overview",
    "question": "What is the role of the Bank of Canada?",
    "options": [
      "To provide personal loans and mortgages to Canadian citizens",
      "Canada's central bank — responsible for monetary policy, setting the key interest rate, and issuing currency to promote economic stability",
      "To manage the federal government's budget",
      "To regulate the stock market and all financial institutions"
    ],
    "answerIndex": 1,
    "explanation": "The Bank of Canada is Canada's central bank. Its main responsibilities include setting monetary policy (including the key interest rate), issuing Canadian bank notes, and promoting a safe and sound financial system. It aims to keep inflation low and stable (typically 2%)."
  },
  {
    "id": "q348",
    "topic": "Canada's Economy",
    "subtopic": "Economic Overview",
    "question": "What is a Crown corporation?",
    "options": [
      "A private company that holds a royal warrant",
      "A company owned by the federal or provincial government, operated at arm's length, to deliver goods or services",
      "A corporation run by the Governor General's office",
      "A chartered bank approved by Parliament"
    ],
    "answerIndex": 1,
    "explanation": "A Crown corporation is a company owned wholly or partly by a federal or provincial government, but operated at arm's length from the government. Examples include Canada Post, CBC/Radio-Canada, and VIA Rail (federal), and Hydro-Québec and LCBO (provincial). They serve public policy goals."
  },
  {
    "id": "q349",
    "topic": "Canada's Economy",
    "subtopic": "Trade",
    "question": "What is Canada's main stock exchange?",
    "options": [
      "The New York Stock Exchange (NYSE)",
      "The Montreal Exchange",
      "The Toronto Stock Exchange (TSX)",
      "The Vancouver Stock Exchange"
    ],
    "answerIndex": 2,
    "explanation": "The Toronto Stock Exchange (TSX) is Canada's main stock exchange and one of the largest in North America. It is operated by TMX Group. The TSX Venture Exchange handles smaller companies. Major Canadian banks, energy companies, and mining companies are listed on the TSX."
  },
  {
    "id": "q350",
    "topic": "Canada's Economy",
    "subtopic": "Natural Resources",
    "question": "Which industry is particularly important to the economies of Nova Scotia, New Brunswick, PEI, and Newfoundland?",
    "options": [
      "The aerospace industry",
      "Oil sands extraction",
      "Fishing and the seafood industry",
      "Automobile manufacturing"
    ],
    "answerIndex": 2,
    "explanation": "Fishing and the seafood industry are particularly important to the Atlantic provinces (Nova Scotia, New Brunswick, PEI, and Newfoundland and Labrador). Products include lobster, snow crab, shrimp, and groundfish. The Grand Banks off Newfoundland were historically one of the world's richest fishing grounds."
  },
  {
    "id": "q351",
    "topic": "Canada's Economy",
    "subtopic": "Natural Resources",
    "question": "What is the forestry industry's role in the Canadian economy?",
    "options": [
      "It has no significant role; Canada imports most of its wood products",
      "Forestry is a major industry, particularly in BC, Ontario, and Quebec — producing lumber, pulp, paper, and wood products for export",
      "Forestry is limited to national parks and is not commercially significant",
      "Canada only produces softwood for the domestic market"
    ],
    "answerIndex": 1,
    "explanation": "Canada's forestry industry is one of the world's largest. British Columbia, Ontario, and Quebec are major forestry provinces. Canada exports lumber, pulp, paper, and other wood products globally. The industry is a significant employer in rural and northern communities."
  },
  {
    "id": "q352",
    "topic": "Canada's Economy",
    "subtopic": "Economic Overview",
    "question": "What does GDP stand for, and what does it measure?",
    "options": [
      "Government Development Plan — the federal budget plan",
      "Gross Domestic Product — the total value of all goods and services produced in a country in a year",
      "General Distribution of Profits — how government distributes tax revenue",
      "Gross Distribution of Petroleum — the national oil output"
    ],
    "answerIndex": 1,
    "explanation": "GDP stands for Gross Domestic Product. It measures the total monetary value of all goods and services produced within a country in a given period (usually a year). GDP is the most commonly used measure of the size and health of an economy."
  },
  {
    "id": "q353",
    "topic": "Canada's Economy",
    "subtopic": "Economic Overview",
    "question": "What is Canada's currency?",
    "options": [
      "The US dollar",
      "The pound sterling",
      "The Canadian dollar",
      "The Commonwealth dollar"
    ],
    "answerIndex": 2,
    "explanation": "Canada's currency is the Canadian dollar (CAD), also known informally as the 'loonie' (after the loon on the one-dollar coin). Canadian bank notes are issued by the Bank of Canada in denominations of $5, $10, $20, $50, and $100."
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
    topic = "Canada's Economy"
    count = len([q for q in existing if q['topic'] == topic])
    print(f"Added {added} questions. '{topic}' now has {count} questions. Total: {len(existing)}")

if __name__ == '__main__':
    main()
