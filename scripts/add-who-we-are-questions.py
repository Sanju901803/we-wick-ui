#!/usr/bin/env python3
"""
Add new 'Who We Are' questions (q163–q205).
"""
import json, os

DATA_FILE = os.path.join(os.path.dirname(__file__), '../src/assets/data/questions.json')

NEW_QUESTIONS = [
  {
    "id": "q163",
    "topic": "Who We Are",
    "subtopic": "Founding Peoples",
    "question": "What are the three founding peoples of Canada?",
    "options": [
      "British, Americans, and French",
      "Aboriginal peoples, French, and British",
      "English, Scottish, and Irish",
      "French, German, and Aboriginal peoples"
    ],
    "answerIndex": 1,
    "explanation": "Canada's three founding peoples are the Aboriginal peoples (First Nations, Métis, and Inuit), the French, and the British. Their languages, laws, and cultures form the foundation of Canadian society."
  },
  {
    "id": "q164",
    "topic": "Who We Are",
    "subtopic": "Aboriginal Peoples",
    "question": "What are the three groups of Aboriginal peoples in Canada?",
    "options": [
      "Inuit, Mohawk, and Métis",
      "Cree, Ojibwe, and Iroquois",
      "First Nations, Métis, and Inuit",
      "Northern, Eastern, and Western Indigenous peoples"
    ],
    "answerIndex": 2,
    "explanation": "Canada's Aboriginal peoples consist of three distinct groups: First Nations (approximately 65%), Métis (approximately 30%), and Inuit (approximately 4%). Each has its own unique cultures, languages, and histories."
  },
  {
    "id": "q165",
    "topic": "Who We Are",
    "subtopic": "Aboriginal Peoples",
    "question": "Where do most Inuit people in Canada live?",
    "options": [
      "In British Columbia and Alberta",
      "In the Prairie provinces",
      "In the Arctic regions — Nunavut, the Northwest Territories, northern Quebec (Nunavik), and Labrador",
      "In Nova Scotia and New Brunswick"
    ],
    "answerIndex": 2,
    "explanation": "Inuit people primarily live in the Arctic and sub-Arctic regions of Canada: Nunavut, the Northwest Territories, northern Quebec (Nunavik), and northern Labrador (Nunatsiavut). The Inuit homeland is called Inuit Nunangat."
  },
  {
    "id": "q166",
    "topic": "Who We Are",
    "subtopic": "Aboriginal Peoples",
    "question": "What is the Michif language?",
    "options": [
      "The language spoken by the Inuit of the Arctic",
      "The mixed language of the Métis, blending French and Cree (and other Aboriginal languages)",
      "An Indigenous language of British Columbia",
      "The official language of the Northwest Territories"
    ],
    "answerIndex": 1,
    "explanation": "Michif is the traditional language of the Métis people. It is a unique blend of French and Cree (and other Aboriginal languages) that reflects the Métis people's mixed Aboriginal and European heritage."
  },
  {
    "id": "q167",
    "topic": "Who We Are",
    "subtopic": "Aboriginal Peoples",
    "question": "What percentage of Canada's Aboriginal peoples are First Nations?",
    "options": [
      "About 30%",
      "About 50%",
      "About 65%",
      "About 80%"
    ],
    "answerIndex": 2,
    "explanation": "First Nations people represent approximately 65% of Canada's Aboriginal population. There are more than 630 First Nations communities across Canada, with diverse languages and cultural traditions."
  },
  {
    "id": "q168",
    "topic": "Who We Are",
    "subtopic": "Francophones",
    "question": "Where do most French-speaking Canadians (Francophones) live?",
    "options": [
      "Ontario and New Brunswick",
      "Manitoba and Saskatchewan",
      "Quebec, with significant communities in Ontario, New Brunswick, and other provinces",
      "Nova Scotia and PEI"
    ],
    "answerIndex": 2,
    "explanation": "The majority of Canada's Francophones (approximately 7 million) live in Quebec. Significant French-speaking communities also exist in Ontario (Ottawa region), New Brunswick (Acadians), and in smaller numbers across other provinces."
  },
  {
    "id": "q169",
    "topic": "Who We Are",
    "subtopic": "Acadians",
    "question": "Who are the Acadians?",
    "options": [
      "French Canadians who live in Quebec",
      "Descendants of French colonists who settled in the Maritime provinces beginning in 1604",
      "Indigenous people of New Brunswick",
      "British settlers who came to PEI in the 1700s"
    ],
    "answerIndex": 1,
    "explanation": "Acadians are descendants of French colonists who settled in the Maritime provinces (now New Brunswick, Nova Scotia, and PEI) beginning in 1604. They have a distinct culture, dialect, and history — including the tragic Great Upheaval deportation of 1755–1763."
  },
  {
    "id": "q170",
    "topic": "Who We Are",
    "subtopic": "English Canadians",
    "question": "Approximately how many Canadians speak English as their first language?",
    "options": [
      "About 5 million",
      "About 12 million",
      "About 18 million",
      "About 25 million"
    ],
    "answerIndex": 2,
    "explanation": "Approximately 18 million Canadians (about 57% of the population) speak English as their first language. Most Anglophones live outside Quebec, though there is an English-speaking minority within Quebec."
  },
  {
    "id": "q171",
    "topic": "Who We Are",
    "subtopic": "Religion",
    "question": "What is the largest religious group in Canada?",
    "options": [
      "Protestant Christians",
      "Roman Catholics",
      "Muslims",
      "Those with no religious affiliation"
    ],
    "answerIndex": 1,
    "explanation": "Roman Catholics form the largest religious group in Canada. The second-largest Christian group is Protestant. Canada also has growing communities of Muslims, Jews, Hindus, Sikhs, and people of other faiths, reflecting its multicultural character."
  },
  {
    "id": "q172",
    "topic": "Who We Are",
    "subtopic": "Immigration History",
    "question": "Who were the Loyalists and why did they come to Canada?",
    "options": [
      "French settlers who came to New France in the 1600s",
      "Around 40,000 people who remained loyal to the British Crown and fled to Canada after the American Revolution (1776)",
      "Scottish settlers who came to Nova Scotia in the 1700s",
      "Chinese labourers who built the Canadian Pacific Railway"
    ],
    "answerIndex": 1,
    "explanation": "The Loyalists were approximately 40,000 people who remained loyal to the British Crown and fled to Canada (mainly Nova Scotia and what is now Ontario) after the American Revolution. They played a major role in shaping English Canada."
  },
  {
    "id": "q173",
    "topic": "Who We Are",
    "subtopic": "Immigration History",
    "question": "What is the 'Last Best West' associated with in Canadian history?",
    "options": [
      "The settlement of British Columbia by gold seekers",
      "The advertising campaign that brought hundreds of thousands of immigrants to the Prairie provinces to farm",
      "The final push of the Canadian Pacific Railway to the Pacific Ocean",
      "The settlement of Newfoundland by British fishermen"
    ],
    "answerIndex": 1,
    "explanation": "The 'Last Best West' was a famous advertising campaign by the Canadian government (especially under PM Wilfrid Laurier) that promoted the Prairie provinces as ideal farmland to attract hundreds of thousands of immigrants from Britain, the US, and Europe in the late 1800s–early 1900s."
  },
  {
    "id": "q174",
    "topic": "Who We Are",
    "subtopic": "Diversity",
    "question": "What does Canada's 'social contract' mean?",
    "options": [
      "A legal contract all immigrants must sign",
      "The unwritten agreement that Canadians respect each other's rights and differences while sharing common values and responsibilities",
      "The agreement between provinces to share tax revenues equally",
      "The treaty between Canada and Indigenous peoples"
    ],
    "answerIndex": 1,
    "explanation": "Canada's social contract is the understanding that Canadians respect one another's differences — of culture, language, religion, and background — while sharing common values such as democracy, equality, and the rule of law, and accepting common responsibilities."
  },
  {
    "id": "q175",
    "topic": "Who We Are",
    "subtopic": "Language",
    "question": "What are Canada's two official languages?",
    "options": [
      "English and French",
      "English and Indigenous languages",
      "French and Inuktitut",
      "English and Spanish"
    ],
    "answerIndex": 0,
    "explanation": "English and French are Canada's two official languages at the federal level. This reflects the founding of the country by British and French colonists. The Official Languages Act of 1969 made both languages equal in federal institutions."
  },
  {
    "id": "q176",
    "topic": "Who We Are",
    "subtopic": "Immigration History",
    "question": "The Chinese Head Tax was a discriminatory tax imposed on which group?",
    "options": [
      "Japanese Canadians during World War II",
      "Chinese immigrants entering Canada, enacted in 1885",
      "South Asian immigrants in the early 1900s",
      "Ukrainian Canadians interned during World War I"
    ],
    "answerIndex": 1,
    "explanation": "The Chinese Head Tax was a discriminatory fee imposed on Chinese immigrants entering Canada, enacted in 1885. It was designed to discourage Chinese immigration after the CPR was built. The Canadian government officially apologized for it in 2006."
  },
  {
    "id": "q177",
    "topic": "Who We Are",
    "subtopic": "Immigration History",
    "question": "When did the Canadian government apologize for the Chinese Head Tax?",
    "options": [
      "1988",
      "1999",
      "2006",
      "2008"
    ],
    "answerIndex": 2,
    "explanation": "The Government of Canada officially apologized for the Chinese Head Tax in 2006. The apology acknowledged the discriminatory impact the tax had on Chinese Canadians and their families."
  },
  {
    "id": "q178",
    "topic": "Who We Are",
    "subtopic": "Immigration History",
    "question": "What happened to Japanese Canadians during World War II?",
    "options": [
      "They were recruited into the Canadian military as a special unit",
      "They were forced into internment camps and had their property confiscated",
      "They were given special protection as neutral civilians",
      "They were deported to Japan during the war"
    ],
    "answerIndex": 1,
    "explanation": "During World War II, approximately 22,000 Japanese Canadians — most of them Canadian-born — were forcibly removed from the BC coast and interned in camps. Their properties were confiscated and sold. Canada apologized and provided compensation in 1988."
  },
  {
    "id": "q179",
    "topic": "Who We Are",
    "subtopic": "Indigenous History",
    "question": "What were residential schools?",
    "options": [
      "Schools that taught Indigenous children their traditional languages",
      "Government-funded, church-run schools where Indigenous children were forcibly removed from their families and forbidden from practicing their culture or language",
      "Free boarding schools for rural children in remote areas",
      "Schools established by Indigenous communities in the 19th century"
    ],
    "answerIndex": 1,
    "explanation": "Residential schools were government-funded, church-administered schools where Indigenous children were forcibly removed from their families and communities. Children were forbidden to speak their language or practice their culture. The system caused immense harm. The Canadian government apologized in 2008."
  },
  {
    "id": "q180",
    "topic": "Who We Are",
    "subtopic": "Indigenous History",
    "question": "When did the Canadian government apologize for the residential school system?",
    "options": [
      "1982",
      "1999",
      "2006",
      "2008"
    ],
    "answerIndex": 3,
    "explanation": "On June 11, 2008, Prime Minister Stephen Harper delivered a formal apology in the House of Commons for the residential school system, acknowledging the lasting harm it caused to Indigenous children, families, and communities."
  },
  {
    "id": "q181",
    "topic": "Who We Are",
    "subtopic": "Symbols",
    "question": "What is the 'fleur-de-lys' and what is its significance in Canada?",
    "options": [
      "A type of maple tree found in Quebec",
      "A French royal heraldic symbol that appears on the flag of Quebec and is associated with French-Canadian heritage",
      "The symbol of the Hudson's Bay Company",
      "Canada's first official coat of arms"
    ],
    "answerIndex": 1,
    "explanation": "The fleur-de-lys is a stylized lily from French royal heraldry. In Canada, it appears prominently on the Quebec flag (adopted in 1948) and is a symbol of French-Canadian heritage and identity."
  },
  {
    "id": "q182",
    "topic": "Who We Are",
    "subtopic": "Diversity",
    "question": "Canada is sometimes described as a 'cultural mosaic.' What does this mean?",
    "options": [
      "Canada is a country with only a few distinct ethnic groups",
      "Canada encourages immigrants to fully abandon their cultural heritage",
      "Canada values and preserves the diverse cultural identities of its people rather than requiring full assimilation",
      "Canada only accepts immigrants from specific countries to maintain cultural balance"
    ],
    "answerIndex": 2,
    "explanation": "Canada is often described as a cultural mosaic because it values the diverse cultural backgrounds of its people. Unlike the 'melting pot' concept, the mosaic idea means cultures can maintain their distinct identities while contributing to Canadian society."
  },
  {
    "id": "q183",
    "topic": "Who We Are",
    "subtopic": "Notable Canadians",
    "question": "Who is Terry Fox and why is he celebrated in Canada?",
    "options": [
      "A Canadian politician who introduced universal health care",
      "A cancer survivor who ran the Marathon of Hope across Canada to raise money for cancer research before his death in 1981",
      "A hockey player who won Canada's first Olympic gold medal",
      "An Indigenous leader who signed historic land treaties"
    ],
    "answerIndex": 1,
    "explanation": "Terry Fox was a Canadian athlete who, after losing his leg to cancer, ran the Marathon of Hope — a cross-Canada run — in 1980 to raise money for cancer research. He ran 5,373 km before cancer spread to his lungs. He died in 1981 and remains one of Canada's greatest heroes."
  },
  {
    "id": "q184",
    "topic": "Who We Are",
    "subtopic": "Notable Canadians",
    "question": "Who is Rick Hansen and what is he famous for?",
    "options": [
      "A Prime Minister who introduced multiculturalism policy",
      "An athlete who wheeled his wheelchair around the world (the Man in Motion World Tour) to raise awareness of people with physical disabilities",
      "An Indigenous chief who led resistance against the CPR",
      "A scientist who discovered insulin"
    ],
    "answerIndex": 1,
    "explanation": "Rick Hansen is a Canadian athlete who, after being paralyzed from the waist down, wheeled his wheelchair around the world in the Man in Motion World Tour (1985–1987) to raise awareness and funds for spinal cord injury research. He became one of Canada's great inspirational figures."
  },
  {
    "id": "q185",
    "topic": "Who We Are",
    "subtopic": "Notable Canadians",
    "question": "What is Roberta Bondar known for?",
    "options": [
      "She was the first Indigenous woman elected to Parliament",
      "She was Canada's first female astronaut in space (1992)",
      "She was the first woman to climb Mount Logan",
      "She was the first female Chief Justice of Canada"
    ],
    "answerIndex": 1,
    "explanation": "Dr. Roberta Bondar became Canada's first female astronaut in space in 1992 when she flew aboard the Space Shuttle Discovery. She was also a neurologist and is celebrated as a pioneering figure for Canadian women in science."
  },
  {
    "id": "q186",
    "topic": "Who We Are",
    "subtopic": "Geography & Identity",
    "question": "What is Canada's national capital?",
    "options": [
      "Toronto",
      "Montreal",
      "Vancouver",
      "Ottawa"
    ],
    "answerIndex": 3,
    "explanation": "Ottawa, in Ontario, is Canada's national capital. It was chosen as the capital of the Province of Canada by Queen Victoria in 1857 because of its location on the border of English and French Canada."
  },
  {
    "id": "q187",
    "topic": "Who We Are",
    "subtopic": "Geography & Identity",
    "question": "Why was Ottawa chosen as Canada's capital?",
    "options": [
      "It was the largest city in Canada at the time",
      "It was far from the American border and on the border between English and French Canada",
      "It was the home city of Sir John A. Macdonald",
      "It was the site of the first British settlement in Canada"
    ],
    "answerIndex": 1,
    "explanation": "Ottawa was chosen as Canada's capital in 1857 by Queen Victoria partly because of its location: it was far enough from the US border to make it defensible and sat on the boundary between English Upper Canada (Ontario) and French Lower Canada (Quebec)."
  },
  {
    "id": "q188",
    "topic": "Who We Are",
    "subtopic": "Founding Peoples",
    "question": "What is the significance of the Battle of the Plains of Abraham (1759)?",
    "options": [
      "It established French dominance in North America",
      "British forces defeated the French, leading to the end of France's empire in North America",
      "It was the battle that led to Canadian Confederation",
      "It ended the War of 1812 between Canada and the United States"
    ],
    "answerIndex": 1,
    "explanation": "The Battle of the Plains of Abraham took place in 1759 near Quebec City. British forces defeated French forces, leading to the fall of New France and the eventual end of France's North American empire. It is one of the most significant battles in Canadian history."
  },
  {
    "id": "q189",
    "topic": "Who We Are",
    "subtopic": "Immigration History",
    "question": "Why did many immigrants come to Canada in the late 1800s and early 1900s?",
    "options": [
      "To escape the cold climate of Europe",
      "To seek land, economic opportunities, and freedom — including fleeing poverty, famine, and persecution",
      "Because Canada was the only country accepting immigrants at the time",
      "Because the Canadian government required immigrants to replace departing citizens"
    ],
    "answerIndex": 1,
    "explanation": "Many immigrants came to Canada in the late 1800s and early 1900s seeking better lives — land to farm in the Prairies, economic opportunity, and freedom from poverty, religious persecution, or political oppression in their home countries."
  },
  {
    "id": "q190",
    "topic": "Who We Are",
    "subtopic": "Language",
    "question": "What is the Official Languages Act (1969)?",
    "options": [
      "A law requiring all Canadians to speak both English and French",
      "A federal law declaring English and French equal official languages of Canada, used in Parliament and federal government services",
      "A law banning the use of any language other than English and French in schools",
      "A law protecting Indigenous languages"
    ],
    "answerIndex": 1,
    "explanation": "The Official Languages Act of 1969, passed under Prime Minister Pierre Trudeau, declared English and French the equal official languages of Canada. It requires that federal government services be available in both official languages."
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
    topic = "Who We Are"
    count = len([q for q in existing if q['topic'] == topic])
    print(f"Added {added} questions. '{topic}' now has {count} questions. Total: {len(existing)}")

if __name__ == '__main__':
    main()
