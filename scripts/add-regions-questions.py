#!/usr/bin/env python3
"""
Add new "Canada's Regions" questions (q354–q410).
"""
import json, os

DATA_FILE = os.path.join(os.path.dirname(__file__), '../src/assets/data/questions.json')

NEW_QUESTIONS = [
  {
    "id": "q354",
    "topic": "Canada's Regions",
    "subtopic": "Provinces and Capitals",
    "question": "What is the capital of British Columbia?",
    "options": [
      "Vancouver",
      "Victoria",
      "Kelowna",
      "Surrey"
    ],
    "answerIndex": 1,
    "explanation": "Victoria is the capital city of British Columbia. It is located on Vancouver Island. Although Vancouver is BC's largest city, Victoria has been the provincial capital since BC joined Confederation in 1871."
  },
  {
    "id": "q355",
    "topic": "Canada's Regions",
    "subtopic": "Provinces and Capitals",
    "question": "What is the capital of Alberta?",
    "options": [
      "Calgary",
      "Lethbridge",
      "Red Deer",
      "Edmonton"
    ],
    "answerIndex": 3,
    "explanation": "Edmonton is the capital city of Alberta. It is located in central Alberta and is known as the 'Gateway to the North.' Calgary is Alberta's largest city, but Edmonton has been the provincial capital since Alberta became a province in 1905."
  },
  {
    "id": "q356",
    "topic": "Canada's Regions",
    "subtopic": "Provinces and Capitals",
    "question": "What is the capital of Saskatchewan?",
    "options": [
      "Saskatoon",
      "Regina",
      "Moose Jaw",
      "Prince Albert"
    ],
    "answerIndex": 1,
    "explanation": "Regina is the capital city of Saskatchewan. Saskatoon is the province's largest city, but Regina has been the provincial capital since Saskatchewan became a province in 1905. Regina was previously named 'Pile O'Bones' before being renamed by Princess Louise Caroline Alberta."
  },
  {
    "id": "q357",
    "topic": "Canada's Regions",
    "subtopic": "Provinces and Capitals",
    "question": "What is the capital of Manitoba?",
    "options": [
      "Brandon",
      "Thompson",
      "Winnipeg",
      "Portage la Prairie"
    ],
    "answerIndex": 2,
    "explanation": "Winnipeg is the capital and largest city of Manitoba. Located at the confluence of the Red and Assiniboine rivers, it has been an important trading and cultural hub since the fur trade era. Winnipeg has been Manitoba's capital since 1870."
  },
  {
    "id": "q358",
    "topic": "Canada's Regions",
    "subtopic": "Provinces and Capitals",
    "question": "What is the capital of Ontario?",
    "options": [
      "Ottawa",
      "Toronto",
      "Hamilton",
      "London"
    ],
    "answerIndex": 1,
    "explanation": "Toronto is the capital city of Ontario and Canada's largest city. It is a major financial, business, and cultural centre. Ottawa, while the national capital of Canada, is also in Ontario but is not the provincial capital — Toronto is."
  },
  {
    "id": "q359",
    "topic": "Canada's Regions",
    "subtopic": "Provinces and Capitals",
    "question": "What is the capital of Quebec?",
    "options": [
      "Montreal",
      "Quebec City",
      "Laval",
      "Gatineau"
    ],
    "answerIndex": 1,
    "explanation": "Quebec City is the capital of the province of Quebec. It is one of the oldest cities in North America and the only remaining walled city north of Mexico. Montreal is Quebec's largest city, but Quebec City is the seat of the provincial government."
  },
  {
    "id": "q360",
    "topic": "Canada's Regions",
    "subtopic": "Provinces and Capitals",
    "question": "What is the capital of New Brunswick?",
    "options": [
      "Moncton",
      "Saint John",
      "Fredericton",
      "Miramichi"
    ],
    "answerIndex": 2,
    "explanation": "Fredericton is the capital city of New Brunswick. Moncton is the largest city and Saint John is the oldest incorporated city in Canada, but Fredericton has been the provincial capital since New Brunswick became a province in 1784."
  },
  {
    "id": "q361",
    "topic": "Canada's Regions",
    "subtopic": "Provinces and Capitals",
    "question": "What is the capital of Nova Scotia?",
    "options": [
      "Dartmouth",
      "Sydney",
      "Truro",
      "Halifax"
    ],
    "answerIndex": 3,
    "explanation": "Halifax is the capital and largest city of Nova Scotia. It is one of the largest natural harbours in the world and has been a major port city since 1749. Halifax served as a vital staging port during both World Wars."
  },
  {
    "id": "q362",
    "topic": "Canada's Regions",
    "subtopic": "Provinces and Capitals",
    "question": "What is the capital of Prince Edward Island (PEI)?",
    "options": [
      "Summerside",
      "Charlottetown",
      "Stratford",
      "Georgetown"
    ],
    "answerIndex": 1,
    "explanation": "Charlottetown is the capital and largest city of Prince Edward Island. Often called the 'Birthplace of Confederation,' Charlottetown hosted the 1864 Charlottetown Conference, which began the process leading to Canadian Confederation in 1867."
  },
  {
    "id": "q363",
    "topic": "Canada's Regions",
    "subtopic": "Provinces and Capitals",
    "question": "What is the capital of Newfoundland and Labrador?",
    "options": [
      "Corner Brook",
      "Happy Valley-Goose Bay",
      "St. John's",
      "Gander"
    ],
    "answerIndex": 2,
    "explanation": "St. John's is the capital and largest city of Newfoundland and Labrador. It is the easternmost city in North America and one of the oldest European settlements in the Americas. Newfoundland and Labrador joined Confederation as the 10th province in 1949."
  },
  {
    "id": "q364",
    "topic": "Canada's Regions",
    "subtopic": "Territories",
    "question": "What are Canada's three territories, and what are their capitals?",
    "options": [
      "Yukon (Whitehorse), Northwest Territories (Yellowknife), Nunavut (Iqaluit)",
      "Yukon (Dawson City), Northwest Territories (Yellowknife), Nunavut (Resolute Bay)",
      "Yukon (Whitehorse), Northwest Territories (Inuvik), Nunavut (Iqaluit)",
      "Labrador (Happy Valley), Northwest Territories (Yellowknife), Nunavut (Rankin Inlet)"
    ],
    "answerIndex": 0,
    "explanation": "Canada's three territories are: Yukon (capital: Whitehorse), Northwest Territories (capital: Yellowknife), and Nunavut (capital: Iqaluit). Nunavut is Canada's newest and largest territory, created in 1999 as an Inuit homeland. The territories differ from provinces — their powers come from the federal government."
  },
  {
    "id": "q365",
    "topic": "Canada's Regions",
    "subtopic": "Geography",
    "question": "Which mountain range runs along Canada's west coast?",
    "options": [
      "The Laurentians",
      "The Appalachians",
      "The Rocky Mountains (and Coast Mountains)",
      "The Canadian Shield highlands"
    ],
    "answerIndex": 2,
    "explanation": "The Rocky Mountains and Coast Mountains run along Canada's west coast, primarily in British Columbia and Alberta. The Rockies form a dramatic natural boundary between BC and Alberta and are home to iconic national parks like Banff, Jasper, and Yoho."
  },
  {
    "id": "q366",
    "topic": "Canada's Regions",
    "subtopic": "Geography",
    "question": "What is the Canadian Shield?",
    "options": [
      "Canada's national military defence system",
      "A vast area of ancient rock that covers about half of Canada, surrounding Hudson Bay",
      "The protected marine area off Canada's Pacific coast",
      "A mountain range in central Canada"
    ],
    "answerIndex": 1,
    "explanation": "The Canadian Shield is a vast geological formation of ancient rock covering about half of Canada, stretching from Labrador west to the Northwest Territories and south around Hudson Bay into the northern United States. Rich in minerals, it is covered by boreal forest and lakes in the south."
  },
  {
    "id": "q367",
    "topic": "Canada's Regions",
    "subtopic": "Geography",
    "question": "What are the five Great Lakes that border Ontario?",
    "options": [
      "Superior, Michigan, Huron, Erie, Ontario",
      "Superior, Huron, Erie, Ontario, and Winnipeg",
      "Ontario, Huron, Erie, Superior, and Georgian Bay",
      "Champlain, Ontario, Erie, Huron, Superior"
    ],
    "answerIndex": 0,
    "explanation": "The five Great Lakes are Superior, Michigan, Huron, Erie, and Ontario (use the acronym 'HOMES'). Four of the five (all except Michigan) border Ontario. The Great Lakes form the largest system of fresh surface water on Earth and are important for transportation and the environment."
  },
  {
    "id": "q368",
    "topic": "Canada's Regions",
    "subtopic": "Geography",
    "question": "What is the St. Lawrence River's significance to Canada?",
    "options": [
      "It is the border between Canada and the United States",
      "A major river that connects the Great Lakes to the Atlantic Ocean, forming a vital transportation route and trade corridor",
      "It supplies drinking water exclusively to Quebec City",
      "It is significant only as a recreational waterway"
    ],
    "answerIndex": 1,
    "explanation": "The St. Lawrence River connects the Great Lakes to the Atlantic Ocean, forming the heart of Canada's most populated region. It has been a vital transportation corridor since Indigenous peoples used it, and later for European explorers, fur traders, and settlers. The St. Lawrence Seaway allows ocean ships to reach the Great Lakes."
  },
  {
    "id": "q369",
    "topic": "Canada's Regions",
    "subtopic": "Pacific Region",
    "question": "What is British Columbia best known for economically?",
    "options": [
      "Wheat farming and cattle ranching",
      "Forestry, mining, fishing, natural gas, and a growing technology sector",
      "Automobile manufacturing and steel production",
      "Petrochemical refining and oil sands"
    ],
    "answerIndex": 1,
    "explanation": "British Columbia's economy is built on forestry (lumber and pulp), mining (coal, copper, gold), fishing (salmon), natural gas, and increasingly, a technology and film industry centred in Vancouver. Tourism, particularly mountain and eco-tourism, is also significant."
  },
  {
    "id": "q370",
    "topic": "Canada's Regions",
    "subtopic": "Prairie Provinces",
    "question": "Which province is Canada's largest oil and natural gas producer?",
    "options": [
      "Saskatchewan",
      "Manitoba",
      "British Columbia",
      "Alberta"
    ],
    "answerIndex": 3,
    "explanation": "Alberta is Canada's largest producer of oil and natural gas, anchored by the oil sands in the northeast (Fort McMurray area) and conventional oil and gas fields. The energy sector dominates Alberta's economy and generates significant royalty revenues for the province."
  },
  {
    "id": "q371",
    "topic": "Canada's Regions",
    "subtopic": "Ontario and Quebec",
    "question": "What are the largest cities in Canada by population?",
    "options": [
      "Toronto, Vancouver, Ottawa",
      "Toronto, Montreal, Vancouver",
      "Montreal, Toronto, Calgary",
      "Toronto, Ottawa, Montreal"
    ],
    "answerIndex": 1,
    "explanation": "The three largest cities in Canada by population are Toronto (Ontario), Montreal (Quebec), and Vancouver (British Columbia). Toronto is the largest, with a Greater Toronto Area population of over 6 million. These three cities are Canada's major metropolitan and economic hubs."
  },
  {
    "id": "q372",
    "topic": "Canada's Regions",
    "subtopic": "Atlantic Canada",
    "question": "What are the four Atlantic provinces?",
    "options": [
      "Nova Scotia, New Brunswick, PEI, and Newfoundland and Labrador",
      "Nova Scotia, New Brunswick, Quebec, and PEI",
      "Newfoundland, New Brunswick, Nova Scotia, and Cape Breton",
      "The Maritimes only: Nova Scotia, New Brunswick, and PEI"
    ],
    "answerIndex": 0,
    "explanation": "The four Atlantic provinces are Nova Scotia, New Brunswick, Prince Edward Island (PEI), and Newfoundland and Labrador. The first three are often called the 'Maritime provinces.' Newfoundland and Labrador joined Confederation in 1949, after the other three. The Atlantic provinces share a coastal, resource-based economy."
  },
  {
    "id": "q373",
    "topic": "Canada's Regions",
    "subtopic": "Ontario and Quebec",
    "question": "Why are Ontario and Quebec sometimes called the 'heartland' of Canada?",
    "options": [
      "Because they are located in the geographic centre of Canada",
      "Because they are home to the largest populations, the federal capital (Ottawa), and produce the most manufactured goods",
      "Because both provinces were founding nations before Confederation",
      "Because the two provinces have the most natural resources"
    ],
    "answerIndex": 1,
    "explanation": "Ontario and Quebec are called Canada's 'heartland' because together they are home to more than 60% of Canada's population, the national capital (Ottawa), the largest cities (Toronto and Montreal), Parliament, and the bulk of Canada's manufacturing and service industries."
  },
  {
    "id": "q374",
    "topic": "Canada's Regions",
    "subtopic": "North",
    "question": "What is the significance of Nunavut?",
    "options": [
      "It is Canada's newest province, created in 2005",
      "It is Canada's largest territory and was created in 1999 as a homeland for the Inuit people",
      "It is a territory created in 1867 as part of the original Confederation",
      "It is an autonomous region with full provincial status"
    ],
    "answerIndex": 1,
    "explanation": "Nunavut ('Our Land' in Inuktitut) was created on April 1, 1999 as Canada's newest and largest territory. It was carved from the Northwest Territories and established as a homeland for the Inuit people, who make up about 85% of its population. Its capital is Iqaluit."
  },
  {
    "id": "q375",
    "topic": "Canada's Regions",
    "subtopic": "Geography",
    "question": "What is unique about Quebec's distinct society?",
    "options": [
      "Quebec has its own military and currency",
      "Quebec is the only province in Canada with a predominantly French-speaking population and its own civil law system (based on French law)",
      "Quebec operates independently and negotiates directly with the United Nations",
      "Quebec has a fully separate immigration system not shared with Canada"
    ],
    "answerIndex": 1,
    "explanation": "Quebec is Canada's only province with a predominantly French-speaking (francophone) population and a distinct French-Canadian culture. It also has its own legal system — the Civil Code of Quebec — based on French civil law, unlike the other provinces which use common law (based on British law)."
  },
  {
    "id": "q376",
    "topic": "Canada's Regions",
    "subtopic": "Prairie Provinces",
    "question": "What is Saskatchewan most famous for producing?",
    "options": [
      "Automobiles and electronics",
      "Wheat, canola, and potash — making it one of the world's most important agricultural exporters",
      "Oil sands and bitumen",
      "Salmon and forest products"
    ],
    "answerIndex": 1,
    "explanation": "Saskatchewan is world-renowned for wheat, canola, and potash production. It is one of the world's largest exporters of wheat and potash (a key fertilizer ingredient). Agriculture dominates Saskatchewan's flat prairies, and the province is sometimes called Canada's 'breadbasket.'"
  },
  {
    "id": "q377",
    "topic": "Canada's Regions",
    "subtopic": "Atlantic Canada",
    "question": "What is the Cabot Trail?",
    "options": [
      "A historic trade route used by John Cabot in 1497",
      "A scenic highway in Cape Breton Island, Nova Scotia, known for its dramatic coastal scenery",
      "A railway line connecting Halifax to Charlottetown",
      "A hiking trail through the Saint John River valley in New Brunswick"
    ],
    "answerIndex": 1,
    "explanation": "The Cabot Trail is a famous scenic highway that loops around the northern tip of Cape Breton Island in Nova Scotia. It passes through Cape Breton Highlands National Park and is renowned for its stunning coastal and mountain scenery. It is one of Canada's top tourist destinations."
  },
  {
    "id": "q378",
    "topic": "Canada's Regions",
    "subtopic": "Geography",
    "question": "Which river flows through the Canadian Prairies to Hudson Bay?",
    "options": [
      "The Saskatchewan River system",
      "The Ottawa River",
      "The St. Lawrence River",
      "The Mackenzie River"
    ],
    "answerIndex": 0,
    "explanation": "The Saskatchewan River system (the North and South Saskatchewan Rivers) drains much of the Prairie provinces, eventually flowing into Lake Winnipeg and then the Nelson River to Hudson Bay. The Mackenzie River drains into the Arctic Ocean in the Northwest Territories."
  },
  {
    "id": "q379",
    "topic": "Canada's Regions",
    "subtopic": "North",
    "question": "What is the Mackenzie River?",
    "options": [
      "A river in British Columbia that drains into the Pacific Ocean",
      "Canada's longest river, flowing from Great Slave Lake northwest to the Arctic Ocean through the Northwest Territories",
      "The main river of the Yukon Territory",
      "A river that forms the boundary between Yukon and Alaska"
    ],
    "answerIndex": 1,
    "explanation": "The Mackenzie River is Canada's longest river and the second longest in North America. It flows from Great Slave Lake northwest through the Northwest Territories to the Mackenzie Delta and the Beaufort Sea (Arctic Ocean). It was a major route for Indigenous peoples and fur traders."
  },
  {
    "id": "q380",
    "topic": "Canada's Regions",
    "subtopic": "Pacific Region",
    "question": "What is the population of the Greater Vancouver area relative to British Columbia?",
    "options": [
      "About 10% of BC's population lives in Greater Vancouver",
      "About a quarter of BC's population lives in Greater Vancouver",
      "Over half of BC's population lives in the Greater Vancouver region",
      "Greater Vancouver's population is roughly equal to the rest of BC combined"
    ],
    "answerIndex": 2,
    "explanation": "More than half of British Columbia's total population lives in the Metro Vancouver (Greater Vancouver) area, making it one of Canada's most concentrated metropolitan regions. The region's mild climate, mountains, and ocean attract immigrants and migrants from across Canada and around the world."
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
    topic = "Canada's Regions"
    count = len([q for q in existing if q['topic'] == topic])
    print(f"Added {added} questions. '{topic}' now has {count} questions. Total: {len(existing)}")

if __name__ == '__main__':
    main()
