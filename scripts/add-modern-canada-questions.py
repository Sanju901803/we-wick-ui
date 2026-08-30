#!/usr/bin/env python3
"""
Add new Modern Canada questions (q233–q270).
"""
import json, os

DATA_FILE = os.path.join(os.path.dirname(__file__), '../src/assets/data/questions.json')

NEW_QUESTIONS = [
  {
    "id": "q233",
    "topic": "Modern Canada",
    "subtopic": "International Role",
    "question": "What is Canada's reputation in international peacekeeping?",
    "options": [
      "Canada has never participated in international peacekeeping",
      "Canada is recognized as a pioneer and leader in United Nations peacekeeping missions around the world",
      "Canada only participates in NATO military operations",
      "Canada's international role is limited to trade negotiations"
    ],
    "answerIndex": 1,
    "explanation": "Canada is internationally recognized as a pioneer in UN peacekeeping. Canadian diplomat Lester B. Pearson proposed the first modern UN peacekeeping force in 1956. Canada has contributed to more than 50 UN peacekeeping missions and the blue beret is closely associated with Canadian soldiers."
  },
  {
    "id": "q234",
    "topic": "Modern Canada",
    "subtopic": "International Organizations",
    "question": "Canada is a member of the Commonwealth of Nations. What is this organization?",
    "options": [
      "A military alliance of English-speaking countries",
      "An organization of 54 member countries, mostly former British colonies, that promotes democracy, human rights, and development",
      "A trade bloc limited to Canada, the UK, and Australia",
      "A secret organization of the world's wealthiest nations"
    ],
    "answerIndex": 1,
    "explanation": "The Commonwealth of Nations is an association of 54 member countries, most of which are former British colonies. It promotes democracy, human rights, the rule of law, and economic development. Canada is a founding member."
  },
  {
    "id": "q235",
    "topic": "Modern Canada",
    "subtopic": "International Organizations",
    "question": "What is La Francophonie and what is Canada's role?",
    "options": [
      "Quebec's provincial language authority",
      "An international organization of French-speaking nations of which Canada is a member",
      "A treaty requiring all Canadian schools to teach French",
      "A French-Canadian political party"
    ],
    "answerIndex": 1,
    "explanation": "La Francophonie (Organisation internationale de la Francophonie) is an international organization of countries that use French as an official or common language. Canada is a member, reflecting its French-speaking population and commitment to French-language culture."
  },
  {
    "id": "q236",
    "topic": "Modern Canada",
    "subtopic": "Military",
    "question": "What are the three branches of the Canadian Armed Forces?",
    "options": [
      "Army, Navy, and Air Force",
      "Infantry, Cavalry, and Artillery",
      "RCMP, Border Services, and Coast Guard",
      "Regular Force, Reserve Force, and Rangers"
    ],
    "answerIndex": 0,
    "explanation": "The Canadian Armed Forces consist of three environmental commands: the Royal Canadian Navy, the Canadian Army, and the Royal Canadian Air Force. Together they defend Canada and contribute to international peace and security."
  },
  {
    "id": "q237",
    "topic": "Modern Canada",
    "subtopic": "Military",
    "question": "What is NORAD?",
    "options": [
      "Canada's national search and rescue agency",
      "A joint Canada-US aerospace defence command that monitors and defends North American airspace",
      "The international organization that oversees Arctic sovereignty",
      "Canada's domestic spy agency"
    ],
    "answerIndex": 1,
    "explanation": "NORAD (North American Aerospace Defense Command) is a joint Canada-United States organization that provides aerospace warning, air sovereignty, and defence for North America. It was established in 1958 and reflects the close defence relationship between Canada and the US."
  },
  {
    "id": "q238",
    "topic": "Modern Canada",
    "subtopic": "Social Programs",
    "question": "What is the Canada Pension Plan (CPP)?",
    "options": [
      "A private retirement savings plan available to government employees only",
      "A mandatory contributory retirement plan that provides income support to retired, disabled, or deceased Canadians and their families",
      "A program that provides free housing to retired Canadians",
      "A fund managed by provinces to support low-income seniors"
    ],
    "answerIndex": 1,
    "explanation": "The Canada Pension Plan (CPP) is a mandatory contributory retirement plan that most working Canadians contribute to through payroll deductions. It provides retirement income, disability benefits, and survivor benefits."
  },
  {
    "id": "q239",
    "topic": "Modern Canada",
    "subtopic": "Social Programs",
    "question": "What is Employment Insurance (EI)?",
    "options": [
      "A private insurance plan employees must purchase",
      "A government program providing temporary income support to Canadians who are unemployed or unable to work for certain reasons",
      "A program providing long-term social assistance to low-income Canadians",
      "A union benefit paid by employers to laid-off workers"
    ],
    "answerIndex": 1,
    "explanation": "Employment Insurance (EI) is a government-administered program that provides temporary financial assistance to eligible Canadians who have lost their jobs, are sick, or are caring for a newborn or seriously ill family member. Workers and employers both contribute to EI."
  },
  {
    "id": "q240",
    "topic": "Modern Canada",
    "subtopic": "Environment",
    "question": "What are some of Canada's major environmental challenges?",
    "options": [
      "Canada has no significant environmental challenges",
      "Climate change, pollution, deforestation, and the protection of freshwater and Arctic ecosystems",
      "Only air pollution in major cities",
      "Soil erosion in the Prairie provinces only"
    ],
    "answerIndex": 1,
    "explanation": "Canada faces significant environmental challenges including climate change (especially in the Arctic), pollution of air and water, deforestation, and the protection of its vast freshwater resources and fragile ecosystems. Environmental stewardship is a shared responsibility of all Canadians."
  },
  {
    "id": "q241",
    "topic": "Modern Canada",
    "subtopic": "Environment",
    "question": "Why is Canada's Arctic sovereignty important to modern Canada?",
    "options": [
      "The Arctic has no strategic value for Canada",
      "Canada claims sovereignty over vast Arctic territories and waterways; as the climate warms and ice melts, it becomes increasingly strategic for trade, resources, and security",
      "Arctic sovereignty is a concern only for Nunavut, not Canada as a whole",
      "Canada has already settled all Arctic sovereignty disputes"
    ],
    "answerIndex": 1,
    "explanation": "Canada's Arctic sovereignty is a significant modern issue. Canada claims the Arctic Archipelago and the Northwest Passage as internal waters. As climate change melts Arctic ice, the region is becoming increasingly important for shipping, natural resources, and military security."
  },
  {
    "id": "q242",
    "topic": "Modern Canada",
    "subtopic": "Science and Technology",
    "question": "What is the Canadarm?",
    "options": [
      "A type of military weapon developed in Canada",
      "A Canadian-built robotic arm used on NASA Space Shuttle missions and the International Space Station",
      "A Canadian oil pipeline in Alberta",
      "A mechanical device used in the construction of the CN Tower"
    ],
    "answerIndex": 1,
    "explanation": "The Canadarm is a Canadian-built robotic arm first used on NASA Space Shuttle missions beginning in 1981. Canada also built Canadarm2, which operates on the International Space Station. The Canadarms are icons of Canadian technological achievement."
  },
  {
    "id": "q243",
    "topic": "Modern Canada",
    "subtopic": "Science and Technology",
    "question": "What Canadian invention has saved more than 16 million lives worldwide?",
    "options": [
      "The telephone",
      "The cardiac pacemaker",
      "Insulin — discovered by Sir Frederick Banting and Charles Best at the University of Toronto in 1921",
      "The BlackBerry smartphone"
    ],
    "answerIndex": 2,
    "explanation": "Insulin was discovered by Sir Frederick Banting and Charles Best at the University of Toronto in 1921. It transformed type 1 diabetes from a fatal disease into a manageable condition and has saved more than 16 million lives worldwide. Banting received the Nobel Prize in Physiology or Medicine in 1923."
  },
  {
    "id": "q244",
    "topic": "Modern Canada",
    "subtopic": "Science and Technology",
    "question": "Who invented the telephone?",
    "options": [
      "Reginald Fessenden",
      "Alexander Graham Bell",
      "Thomas Edison",
      "Guglielmo Marconi"
    ],
    "answerIndex": 1,
    "explanation": "Alexander Graham Bell invented the telephone and conducted some of his key experiments at Brantford, Ontario. Bell is considered one of Canada's most famous inventors, though he is often primarily associated with the United States."
  },
  {
    "id": "q245",
    "topic": "Modern Canada",
    "subtopic": "Science and Technology",
    "question": "Who invented standard time zones?",
    "options": [
      "Alexander Graham Bell",
      "Joseph-Armand Bombardier",
      "Sir Sandford Fleming",
      "Reginald Fessenden"
    ],
    "answerIndex": 2,
    "explanation": "Sir Sandford Fleming, a Canadian engineer, proposed the system of worldwide standard time zones in 1878. His system — dividing the world into 24 time zones — was adopted internationally and is still used today."
  },
  {
    "id": "q246",
    "topic": "Modern Canada",
    "subtopic": "Science and Technology",
    "question": "Who invented the snowmobile?",
    "options": [
      "Alexander Graham Bell",
      "James Naismith",
      "Joseph-Armand Bombardier",
      "Matthew Evans"
    ],
    "answerIndex": 2,
    "explanation": "Joseph-Armand Bombardier, a Quebec inventor and entrepreneur, developed the snowmobile in the 1930s to travel across Quebec's snow-covered terrain. His company, Bombardier, grew into one of Canada's largest manufacturing companies."
  },
  {
    "id": "q247",
    "topic": "Modern Canada",
    "subtopic": "Science and Technology",
    "question": "Who invented basketball and where?",
    "options": [
      "Wayne Gretzky — in Edmonton, Alberta",
      "James Naismith — a Canadian, invented basketball in 1891 in Springfield, Massachusetts",
      "John A. Macdonald — in Kingston, Ontario",
      "Terry Fox — in Port Coquitlam, British Columbia"
    ],
    "answerIndex": 1,
    "explanation": "Basketball was invented in 1891 by James Naismith, a Canadian from Almonte, Ontario. He invented the game while working as a physical education instructor at the YMCA in Springfield, Massachusetts. Basketball has become one of the world's most popular sports."
  },
  {
    "id": "q248",
    "topic": "Modern Canada",
    "subtopic": "Social Programs",
    "question": "What is Old Age Security (OAS)?",
    "options": [
      "A savings plan for Canadians over 65",
      "A monthly government payment available to Canadians aged 65 and over who meet residency requirements",
      "A pension plan available only to federal government employees",
      "A private insurance program for the elderly"
    ],
    "answerIndex": 1,
    "explanation": "Old Age Security (OAS) is a monthly government payment available to Canadians and permanent residents aged 65 and over who have lived in Canada for a minimum of 10 years. It is funded by general tax revenues and does not require contributions."
  },
  {
    "id": "q249",
    "topic": "Modern Canada",
    "subtopic": "Demographics",
    "question": "What is Canada's land area rank in the world?",
    "options": [
      "Largest country in the world",
      "Second largest country in the world",
      "Third largest country in the world",
      "Fifth largest country in the world"
    ],
    "answerIndex": 1,
    "explanation": "Canada is the second largest country in the world by total area (after Russia), covering almost 10 million square kilometres. Despite its enormous size, Canada has a relatively small population of approximately 38 million people."
  },
  {
    "id": "q250",
    "topic": "Modern Canada",
    "subtopic": "Demographics",
    "question": "What is the most populous city in Canada?",
    "options": [
      "Montreal",
      "Vancouver",
      "Ottawa",
      "Toronto"
    ],
    "answerIndex": 3,
    "explanation": "Toronto, Ontario, is Canada's most populous city and the country's economic and cultural centre. The Greater Toronto Area (GTA) has a population of over 6 million people, making it one of the largest urban areas in North America."
  },
  {
    "id": "q251",
    "topic": "Modern Canada",
    "subtopic": "Society",
    "question": "What is Canada's approach to same-sex marriage?",
    "options": [
      "Same-sex marriage is not recognized anywhere in Canada",
      "Same-sex marriage is recognized only in Quebec",
      "Canada legalized same-sex marriage nationwide in 2005, making it one of the first countries to do so",
      "Same-sex marriage is left to each province to decide"
    ],
    "answerIndex": 2,
    "explanation": "Canada legalized same-sex marriage nationwide through the Civil Marriage Act in July 2005, making Canada one of the first countries in the world to legally recognize same-sex marriage at the national level. This reflected Canada's commitment to equality rights under the Charter."
  },
  {
    "id": "q252",
    "topic": "Modern Canada",
    "subtopic": "Society",
    "question": "What is Canada's Truth and Reconciliation Commission (TRC)?",
    "options": [
      "A commission investigating corruption in the federal government",
      "A national commission (2008–2015) that documented the history and impacts of the residential school system and called for reconciliation between Indigenous and non-Indigenous Canadians",
      "A provincial commission examining Quebec's relationship with Canada",
      "A UN commission overseeing Canadian peacekeeping activities"
    ],
    "answerIndex": 1,
    "explanation": "The Truth and Reconciliation Commission (TRC) of Canada was established in 2008 as part of the Indian Residential Schools Settlement Agreement. It gathered testimonies from survivors and documented the history of residential schools. The TRC released its final report in 2015, including 94 Calls to Action for reconciliation between Indigenous and non-Indigenous Canadians."
  },
  {
    "id": "q253",
    "topic": "Modern Canada",
    "subtopic": "International Organizations",
    "question": "What is the United Nations and what is Canada's relationship to it?",
    "options": [
      "The UN is a military alliance that Canada joined in 1949",
      "The UN is an international organization promoting peace, security, and development; Canada is a founding member and active contributor",
      "The UN is a trade organization similar to NAFTA",
      "Canada is not a member of the United Nations"
    ],
    "answerIndex": 1,
    "explanation": "The United Nations (UN) is an international organization founded in 1945 to promote peace, security, and cooperation between nations. Canada was a founding member and has been a consistent contributor to UN missions, programs, and values."
  },
  {
    "id": "q254",
    "topic": "Modern Canada",
    "subtopic": "Arts and Culture",
    "question": "What is the Canada Council for the Arts?",
    "options": [
      "A private arts funding organization in Toronto",
      "A federal agency that funds Canadian artists, arts organizations, and cultural activities",
      "A provincial agency promoting Quebec culture",
      "A school for performing arts in Ottawa"
    ],
    "answerIndex": 1,
    "explanation": "The Canada Council for the Arts is a federal Crown corporation that provides grants and funding to Canadian artists and arts organizations. It supports music, theatre, dance, visual arts, writing, and other cultural activities across Canada."
  },
  {
    "id": "q255",
    "topic": "Modern Canada",
    "subtopic": "Sports",
    "question": "Why is hockey considered central to Canadian identity?",
    "options": [
      "Canada invented hockey and it is the country's official national winter sport, deeply woven into Canadian culture and identity",
      "Hockey is the only sport Canadians play in winter",
      "Hockey is mandated by law as the national sport",
      "Most Canadians play hockey professionally"
    ],
    "answerIndex": 0,
    "explanation": "Ice hockey was developed in Canada (with roots in 19th-century Nova Scotia and Quebec) and is Canada's official national winter sport. It is deeply woven into Canadian culture — from frozen ponds to the NHL, it is a source of national pride and identity shared across generations."
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
    topic = "Modern Canada"
    count = len([q for q in existing if q['topic'] == topic])
    print(f"Added {added} questions. '{topic}' now has {count} questions. Total: {len(existing)}")

if __name__ == '__main__':
    main()
