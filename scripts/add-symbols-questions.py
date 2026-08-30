#!/usr/bin/env python3
"""
Add new 'Canadian Symbols' questions (q319–q355).
"""
import json, os

DATA_FILE = os.path.join(os.path.dirname(__file__), '../src/assets/data/questions.json')

NEW_QUESTIONS = [
  {
    "id": "q319",
    "topic": "Canadian Symbols",
    "subtopic": "Flags and Emblems",
    "question": "What is depicted on the Canadian flag?",
    "options": [
      "A beaver and maple leaves",
      "A red maple leaf on a white background, with red vertical bars on each side",
      "The Union Jack and the fleur-de-lys",
      "A red maple leaf on a blue background"
    ],
    "answerIndex": 1,
    "explanation": "The National Flag of Canada (the Maple Leaf flag) features a single red maple leaf on a white square background, with red vertical bands on each side. It was adopted on February 15, 1965, replacing the Canadian Red Ensign."
  },
  {
    "id": "q320",
    "topic": "Canadian Symbols",
    "subtopic": "Flags and Emblems",
    "question": "What animal is on the Canadian coat of arms?",
    "options": [
      "A moose and a beaver",
      "A lion and a unicorn as supporters, with a beaver as the crest",
      "A polar bear and an eagle",
      "A loon and a maple leaf"
    ],
    "answerIndex": 1,
    "explanation": "Canada's coat of arms features a lion (representing England) and a unicorn (representing Scotland) as supporters. A lion wearing a crown tops the shield as the crest, and a beaver holds the Royal Crown. The motto is 'A Mari Usque Ad Mare' (From Sea to Sea)."
  },
  {
    "id": "q321",
    "topic": "Canadian Symbols",
    "subtopic": "Flags and Emblems",
    "question": "What does 'A Mari Usque Ad Mare' mean, and where does it appear?",
    "options": [
      "'True North, Strong and Free' — on Canada's flag",
      "'From Sea to Sea' — Canada's official motto, found on the coat of arms",
      "'One Country, One People' — inscribed on Parliament buildings",
      "'Land of Opportunity' — on the Great Seal of Canada"
    ],
    "answerIndex": 1,
    "explanation": "'A Mari Usque Ad Mare' is Latin for 'From Sea to Sea' — Canada's official motto. It appears on the Canadian coat of arms and reflects Canada's geography stretching from the Atlantic to the Pacific (and Arctic) oceans."
  },
  {
    "id": "q322",
    "topic": "Canadian Symbols",
    "subtopic": "National Symbols",
    "question": "What is the national animal of Canada?",
    "options": [
      "The moose",
      "The loon",
      "The beaver",
      "The polar bear"
    ],
    "answerIndex": 2,
    "explanation": "The beaver (Castor canadensis) is Canada's national animal. It was declared the national animal of Canada in 1975. The beaver has a long history as a symbol of Canada, particularly through the fur trade that drove early exploration and settlement."
  },
  {
    "id": "q323",
    "topic": "Canadian Symbols",
    "subtopic": "National Symbols",
    "question": "What bird is on the Canadian one-dollar coin (the 'loonie')?",
    "options": [
      "A Canada goose",
      "An eagle",
      "A common loon",
      "A snowy owl"
    ],
    "answerIndex": 2,
    "explanation": "The Canadian one-dollar coin is nicknamed the 'loonie' because it features a common loon (a bird native to Canada) on its reverse side. The loon is a well-known Canadian symbol. The coin was introduced in 1987."
  },
  {
    "id": "q324",
    "topic": "Canadian Symbols",
    "subtopic": "National Symbols",
    "question": "What animal appears on the reverse of the Canadian two-dollar coin (the 'toonie')?",
    "options": [
      "A beaver",
      "A moose",
      "A polar bear",
      "A caribou"
    ],
    "answerIndex": 2,
    "explanation": "The Canadian two-dollar coin ('toonie') features a polar bear on its reverse side. The coin was introduced in 1996. Its nickname 'toonie' is a combination of 'two' and 'loonie' (the one-dollar coin)."
  },
  {
    "id": "q325",
    "topic": "Canadian Symbols",
    "subtopic": "National Symbols",
    "question": "What is the national sport of Canada in summer?",
    "options": [
      "Hockey",
      "Baseball",
      "Lacrosse",
      "Soccer"
    ],
    "answerIndex": 2,
    "explanation": "Lacrosse is Canada's official national summer sport. It originated with Indigenous peoples of North America and was played long before European contact. It was declared the national sport in 1859 by the National Lacrosse Association. Hockey is the national winter sport."
  },
  {
    "id": "q326",
    "topic": "Canadian Symbols",
    "subtopic": "National Symbols",
    "question": "What is the national winter sport of Canada?",
    "options": [
      "Curling",
      "Ice hockey",
      "Speed skating",
      "Skiing"
    ],
    "answerIndex": 1,
    "explanation": "Ice hockey is Canada's official national winter sport. It is widely regarded as Canada's most popular sport. The Stanley Cup, awarded to the NHL champion, is the oldest professional sports trophy in North America."
  },
  {
    "id": "q327",
    "topic": "Canadian Symbols",
    "subtopic": "Buildings and Landmarks",
    "question": "Where is Canada's Parliament located?",
    "options": [
      "Toronto, Ontario",
      "Montreal, Quebec",
      "Ottawa, Ontario",
      "Gatineau, Quebec"
    ],
    "answerIndex": 2,
    "explanation": "Canada's Parliament buildings are located in Ottawa, Ontario, on Parliament Hill overlooking the Ottawa River. Ottawa is the national capital. Parliament Hill includes the Centre Block (with the Peace Tower), East Block, West Block, and the Senate of Canada Building."
  },
  {
    "id": "q328",
    "topic": "Canadian Symbols",
    "subtopic": "Buildings and Landmarks",
    "question": "What is the Peace Tower?",
    "options": [
      "A monument commemorating Canada's peacekeeping contributions",
      "The central clock tower of the Centre Block on Parliament Hill, built as a memorial to Canadians who died in World War I",
      "A tower at the Canadian War Museum",
      "A landmark at the National Capital at the edge of the Ottawa River"
    ],
    "answerIndex": 1,
    "explanation": "The Peace Tower is the central tower of the Centre Block on Parliament Hill in Ottawa. Standing 92 metres tall, it was built as a memorial to the Canadians who died in World War I. It features a carillon of 53 bells and a Memorial Chamber."
  },
  {
    "id": "q329",
    "topic": "Canadian Symbols",
    "subtopic": "Anthem and Holidays",
    "question": "In what year was 'O Canada' officially adopted as Canada's national anthem?",
    "options": [
      "1867",
      "1927",
      "1965",
      "1980"
    ],
    "answerIndex": 3,
    "explanation": "'O Canada' was composed by Calixa Lavallée with French lyrics by Sir Adolphe-Basile Routhier in 1880, and English words were added later. It was officially proclaimed Canada's national anthem on July 1, 1980 — more than a century after Confederation."
  },
  {
    "id": "q330",
    "topic": "Canadian Symbols",
    "subtopic": "Anthem and Holidays",
    "question": "What national holiday is celebrated on July 1?",
    "options": [
      "Victoria Day",
      "Thanksgiving",
      "Canada Day",
      "Remembrance Day"
    ],
    "answerIndex": 2,
    "explanation": "Canada Day, celebrated on July 1, marks the anniversary of Confederation — the day the British North America Act, 1867 came into force, creating the Dominion of Canada. Canadians celebrate with parades, fireworks, and festivities across the country."
  },
  {
    "id": "q331",
    "topic": "Canadian Symbols",
    "subtopic": "Anthem and Holidays",
    "question": "What is Remembrance Day and when is it observed?",
    "options": [
      "A day to remember Canada's founding fathers, celebrated on October 17",
      "November 11 — a national day to honour Canadians who served and died in wars and military operations",
      "The last Monday of October, honouring veterans of all conflicts",
      "December 11 — marking the anniversary of the Statute of Westminster"
    ],
    "answerIndex": 1,
    "explanation": "Remembrance Day is observed on November 11 — the anniversary of the armistice that ended World War I in 1918. Canadians observe a moment of silence at 11 a.m. to honour those who served and sacrificed their lives in wars and military service. The poppy is the symbol of Remembrance."
  },
  {
    "id": "q332",
    "topic": "Canadian Symbols",
    "subtopic": "Anthem and Holidays",
    "question": "What is the significance of the poppy as a Canadian symbol?",
    "options": [
      "It is the national flower of Canada",
      "It symbolizes Canadian peacekeeping efforts abroad",
      "It is the symbol of Remembrance — honouring Canadians who died in wars, inspired by the poem 'In Flanders Fields'",
      "It represents the agricultural heritage of the Prairie provinces"
    ],
    "answerIndex": 2,
    "explanation": "The red poppy is the symbol of Remembrance in Canada. It was inspired by Lieutenant-Colonel John McCrae's famous poem 'In Flanders Fields,' written in 1915 during World War I. Canadians wear poppies in the days leading up to Remembrance Day (November 11)."
  },
  {
    "id": "q333",
    "topic": "Canadian Symbols",
    "subtopic": "Sports Trophies",
    "question": "What is the Stanley Cup?",
    "options": [
      "The trophy awarded to Canada's best lacrosse team",
      "The trophy awarded annually to the champion team of the National Hockey League (NHL)",
      "The prize for the winner of the annual Canada vs. USA hockey tournament",
      "A trophy given to Canada's most valuable Olympic athlete"
    ],
    "answerIndex": 1,
    "explanation": "The Stanley Cup is the oldest professional sports trophy in North America. It is awarded annually to the playoff champion of the National Hockey League (NHL). It was donated by Lord Stanley, Governor General of Canada, in 1892. Players who win have their name engraved on the Cup."
  },
  {
    "id": "q334",
    "topic": "Canadian Symbols",
    "subtopic": "Sports Trophies",
    "question": "What is the Grey Cup?",
    "options": [
      "The championship trophy for Canadian Football League (CFL) champions",
      "An award for the most valuable player in the NHL",
      "The trophy for the winner of the Canadian Soccer Championship",
      "An award for Canada's Olympic team"
    ],
    "answerIndex": 0,
    "explanation": "The Grey Cup is the championship trophy of the Canadian Football League (CFL). It was donated by Governor General Earl Grey in 1909. The Grey Cup Game is one of Canada's largest annual sporting events, bringing together fans from across the country."
  },
  {
    "id": "q335",
    "topic": "Canadian Symbols",
    "subtopic": "Flags and Emblems",
    "question": "What does the maple leaf symbolize in Canada?",
    "options": [
      "Canada's forest industry and timber trade",
      "A longstanding symbol of Canada, representing the country's natural heritage, used since the 1700s",
      "The influence of French culture on Canadian identity",
      "Canada's commitment to environmental conservation"
    ],
    "answerIndex": 1,
    "explanation": "The maple leaf has been a symbol of Canada since at least the 1700s. It has been used on coins, military insignia, and in art long before it appeared on the national flag. It appears on Canada's coat of arms and flag, and represents the country's natural heritage and identity."
  },
  {
    "id": "q336",
    "topic": "Canadian Symbols",
    "subtopic": "Royal Symbols",
    "question": "What is 'Royal Canadian' a title that often precedes?",
    "options": [
      "Crown corporations only",
      "Major national institutions such as the Royal Canadian Mounted Police, Royal Canadian Air Force, and Royal Canadian Navy",
      "Any national sports team that has won an Olympic gold medal",
      "Institutions established in the pre-Confederation era only"
    ],
    "answerIndex": 1,
    "explanation": "The prefix 'Royal Canadian' (or simply 'Royal') is bestowed by the Crown and denotes institutions of national significance. Examples include the Royal Canadian Mounted Police (RCMP), Royal Canadian Air Force (RCAF), Royal Canadian Navy (RCN), and Royal Canadian Legion."
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
    topic = "Canadian Symbols"
    count = len([q for q in existing if q['topic'] == topic])
    print(f"Added {added} questions. '{topic}' now has {count} questions. Total: {len(existing)}")

if __name__ == '__main__':
    main()
