#!/usr/bin/env python3
"""
Add new questions across all topics based on official Discover Canada guide gaps.
Starts from id q381.
"""

import json

NEW_QUESTIONS = [
  # ─────────────────────────────────────────────────────────────────────────────
  # OATH OF CITIZENSHIP  (20 → +10 = 30)
  # ─────────────────────────────────────────────────────────────────────────────
  {
    "id": "q381",
    "topic": "Oath of Citizenship",
    "subtopic": "The Oath",
    "question": "According to the Oath of Citizenship, to whom do new citizens pledge their allegiance?",
    "options": [
      "The Constitution of Canada",
      "The Prime Minister of Canada",
      "His Majesty King Charles the Third, King of Canada, His Heirs and Successors",
      "The flag and national anthem of Canada"
    ],
    "answerIndex": 2,
    "explanation": "The Oath of Citizenship pledges allegiance to 'His Majesty King Charles the Third, King of Canada, His Heirs and Successors.' In Canada's constitutional monarchy, loyalty is pledged to a person (the Sovereign) who represents all Canadians, not to a document or banner."
  },
  {
    "id": "q382",
    "topic": "Oath of Citizenship",
    "subtopic": "The Oath",
    "question": "What does the Oath of Citizenship say about Aboriginal and treaty rights?",
    "options": [
      "It says citizens will negotiate new treaties with Aboriginal peoples",
      "It acknowledges the Constitution, which recognizes and affirms the Aboriginal and treaty rights of First Nations, Inuit and Métis peoples",
      "It requires citizens to learn about Aboriginal cultures",
      "It promises to protect Aboriginal lands"
    ],
    "answerIndex": 1,
    "explanation": "The Oath of Citizenship includes a reference to faithfully observing the laws of Canada 'including the Constitution, which recognizes and affirms the Aboriginal and treaty rights of First Nations, Inuit and Métis peoples.' This was added to highlight the importance of Indigenous rights."
  },
  {
    "id": "q383",
    "topic": "Oath of Citizenship",
    "subtopic": "Significance",
    "question": "Why do Canadians profess loyalty to the Sovereign rather than to a document like the Constitution?",
    "options": [
      "Because the Constitution is too complex to understand",
      "Because it is a tradition inherited from France",
      "Because Canada is personified by the Sovereign, who represents all Canadians and encompasses the country, its flag and values",
      "Because the Sovereign writes the laws of Canada"
    ],
    "answerIndex": 2,
    "explanation": "Canada's constitutional monarchy is based on the principle that 'Canada is personified by the Sovereign just as the Sovereign is personified by Canada.' The Sovereign represents all Canadians and is a symbol of the nation itself, making it a remarkably simple yet powerful principle."
  },
  {
    "id": "q384",
    "topic": "Oath of Citizenship",
    "subtopic": "The Oath",
    "question": "What phrase in the Oath of Citizenship expresses a new citizen's commitment to Canadian law?",
    "options": [
      "\"I promise to pay taxes and obey traffic laws\"",
      "\"I will faithfully observe the laws of Canada\"",
      "\"I will defend Canada from all enemies\"",
      "\"I will learn English or French within one year\""
    ],
    "answerIndex": 1,
    "explanation": "The Oath states 'I will faithfully observe the laws of Canada including the Constitution.' This phrase commits the new citizen to upholding all of Canada's laws, including the Constitution with its protection of Aboriginal and treaty rights."
  },
  {
    "id": "q385",
    "topic": "Oath of Citizenship",
    "subtopic": "Significance",
    "question": "What is the French name of the Oath of Citizenship?",
    "options": [
      "Le serment de citoyenneté",
      "La promesse de fidélité",
      "Le vœu du citoyen",
      "L'engagement national"
    ],
    "answerIndex": 0,
    "explanation": "The French name of the Oath of Citizenship is 'Le serment de citoyenneté.' The Oath is available in both English and French, Canada's two official languages, and new citizens may choose to swear or affirm the oath in either language."
  },
  {
    "id": "q386",
    "topic": "Oath of Citizenship",
    "subtopic": "The Oath",
    "question": "What does 'bear true allegiance' mean in the context of the Oath of Citizenship?",
    "options": [
      "To carry the Canadian flag at all times",
      "To serve in the Canadian military",
      "To be faithful and loyal to the Sovereign and Canada",
      "To pay allegiance fees to the Crown"
    ],
    "answerIndex": 2,
    "explanation": "'Bear true allegiance' means to be faithful and loyal to the Sovereign—King Charles III—and through the Sovereign to Canada. The opening line 'I swear (or affirm) that I will be faithful and bear true allegiance' is the foundational promise of the Oath."
  },
  {
    "id": "q387",
    "topic": "Oath of Citizenship",
    "subtopic": "Ceremony",
    "question": "What does a person say at the citizenship ceremony to complete the naturalization process?",
    "options": [
      "The National Anthem in both English and French",
      "The Oath of Citizenship",
      "A pledge to the Canadian Constitution",
      "A declaration of renouncing previous citizenship"
    ],
    "answerIndex": 1,
    "explanation": "At the citizenship ceremony, the applicant repeats the Oath of Citizenship. This is the defining moment of becoming a Canadian citizen. Citizens may 'swear' (a religious affirmation) or 'affirm' (a secular affirmation) the Oath."
  },
  {
    "id": "q388",
    "topic": "Oath of Citizenship",
    "subtopic": "The Oath",
    "question": "Which phrase in the Oath commits the new citizen to the responsibilities that come with Canadian citizenship?",
    "options": [
      "\"And bear true allegiance\"",
      "\"Long live the King\"",
      "\"And fulfil my duties as a Canadian citizen\"",
      "\"With glowing hearts\""
    ],
    "answerIndex": 2,
    "explanation": "The closing phrase 'and fulfil my duties as a Canadian citizen' commits the new citizen to the responsibilities of citizenship — obeying the law, voting, helping others, protecting the environment, and if necessary, defending Canada."
  },
  {
    "id": "q389",
    "topic": "Oath of Citizenship",
    "subtopic": "The Oath",
    "question": "The Oath of Citizenship mentions 'His Heirs and Successors.' What does this mean?",
    "options": [
      "Allegiance is to the current King only and must be renewed with each new monarch",
      "Allegiance extends to future monarchs who succeed to the throne, ensuring continuity of the Crown",
      "Citizens must pledge again when a new monarch is crowned",
      "Only direct heirs of King Charles III are included, not future successors"
    ],
    "answerIndex": 1,
    "explanation": "By pledging allegiance to 'His Heirs and Successors,' new citizens are committing to loyalty to the institution of the Canadian Crown — not just to King Charles III personally, but to all future monarchs who inherit the throne, ensuring continuity of allegiance."
  },
  {
    "id": "q390",
    "topic": "Oath of Citizenship",
    "subtopic": "History",
    "question": "What is significant about the Oath mentioning the Constitution specifically?",
    "options": [
      "It means citizens must memorize the entire Constitution",
      "It signals that Canada is a constitutional monarchy where even the Sovereign must follow the Constitution",
      "It means the Constitution overrides the authority of the King",
      "It requires citizens to study constitutional law before becoming citizens"
    ],
    "answerIndex": 1,
    "explanation": "Referencing the Constitution in the Oath reflects Canada's constitutional monarchy: the Sovereign reigns in accordance with the Constitution — the rule of law. The Constitution limits the Sovereign's power and protects citizens' rights, including those of First Nations, Inuit and Métis peoples."
  },

  # ─────────────────────────────────────────────────────────────────────────────
  # RIGHTS AND RESPONSIBILITIES  (38 → +10 = 48)
  # ─────────────────────────────────────────────────────────────────────────────
  {
    "id": "q391",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "History of Rights",
    "question": "The Magna Carta, signed in 1215 in England, is also known as what?",
    "options": [
      "The Great Charter of Freedoms",
      "The Declaration of Rights",
      "The Bill of Rights",
      "The Constitutional Charter"
    ],
    "answerIndex": 0,
    "explanation": "The Magna Carta (1215) is also known as the 'Great Charter of Freedoms.' It established an 800-year tradition of ordered liberty that Canada inherited from Great Britain, including freedom of conscience and religion, freedom of thought and expression, freedom of peaceful assembly, and freedom of association."
  },
  {
    "id": "q392",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Legal Rights",
    "question": "What is habeas corpus?",
    "options": [
      "The right to a trial by jury",
      "The right to remain silent when arrested",
      "The right to challenge unlawful detention by the state",
      "The right to legal representation at no cost"
    ],
    "answerIndex": 2,
    "explanation": "Habeas corpus is the right to challenge unlawful detention by the state. It comes from English common law and is a foundational protection ensuring that no person can be imprisoned without a legal justification that can be reviewed by a court."
  },
  {
    "id": "q393",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Charter",
    "question": "With what phrase does the Canadian Charter of Rights and Freedoms begin?",
    "options": [
      "\"We the people of Canada\"",
      "\"Whereas Canada is founded upon principles that recognize the supremacy of God and the rule of law\"",
      "\"All Canadians are created equal under the law\"",
      "\"Canada is a free and democratic nation\""
    ],
    "answerIndex": 1,
    "explanation": "The Canadian Charter of Rights and Freedoms begins with 'Whereas Canada is founded upon principles that recognize the supremacy of God and the rule of law.' This phrase underlines the importance of religious traditions to Canadian society and the dignity and worth of the human person."
  },
  {
    "id": "q394",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Mobility Rights",
    "question": "What do Mobility Rights in the Canadian Charter of Rights and Freedoms guarantee?",
    "options": [
      "The right to own a car and drive anywhere in Canada",
      "The right to move freely within a city or province",
      "Canadians can live and work anywhere in Canada, enter and leave freely, and apply for a passport",
      "The right to travel between Canada and the United States without a passport"
    ],
    "answerIndex": 2,
    "explanation": "Mobility Rights in the Charter guarantee that Canadians can live and work anywhere they choose in Canada, enter and leave the country freely, and apply for a passport. These rights ensure freedom of movement throughout Canada."
  },
  {
    "id": "q395",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Equality Rights",
    "question": "What does the Charter say about practices such as spousal abuse, forced marriage, or female genital mutilation?",
    "options": [
      "They are protected as cultural practices under the multiculturalism provision",
      "They are permitted under religious freedom provisions",
      "Canada's openness and generosity do not extend to these barbaric cultural practices; those guilty are severely punished under criminal laws",
      "They are addressed separately through provincial human rights codes"
    ],
    "answerIndex": 2,
    "explanation": "Canada is clear that its openness and generosity 'do not extend to barbaric cultural practices that tolerate spousal abuse, honour killings, female genital mutilation, forced marriage or other gender-based violence.' Men and women are equal under the law, and those guilty of such crimes are severely punished."
  },
  {
    "id": "q396",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Responsibilities",
    "question": "Which of the following is listed as a citizenship responsibility in Canada?",
    "options": [
      "Learning to speak both English and French fluently",
      "Serving on a jury when called to do so",
      "Owning property in Canada",
      "Belonging to a political party"
    ],
    "answerIndex": 1,
    "explanation": "Serving on a jury is a legal requirement when called upon and is listed as a citizenship responsibility. Other responsibilities include obeying the law, voting in elections, helping others in the community, and protecting our heritage and environment."
  },
  {
    "id": "q397",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Responsibilities",
    "question": "What does 'Defending Canada' mean for citizens who choose not to join the military?",
    "options": [
      "Citizens are required to complete at least one year of military service",
      "Citizens can serve in the Coast Guard, emergency services, police, or fire departments in their community",
      "Citizens must pay a national defence tax",
      "Only male citizens aged 18-45 are expected to serve"
    ],
    "answerIndex": 1,
    "explanation": "There is no compulsory military service in Canada. However, citizens can contribute to defence by serving in the regular Canadian Forces, Coast Guard, or emergency services such as police or fire departments. Young people can also join the cadets to learn discipline, responsibility and skills."
  },
  {
    "id": "q398",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Language Rights",
    "question": "What does the Charter say about Official Language Rights?",
    "options": [
      "English is the official language of Canada; French is only official in Quebec",
      "French and English have equal status in Parliament and throughout the federal government",
      "The federal government may use either language but not both simultaneously",
      "Language rights only apply to citizens, not permanent residents"
    ],
    "answerIndex": 1,
    "explanation": "The Charter guarantees that 'French and English have equal status in Parliament and throughout the government.' The federal government is required by law to provide services in both official languages, reflecting Canada's bilingual identity."
  },
  {
    "id": "q399",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Responsibilities",
    "question": "Why is volunteering considered an important citizenship responsibility in Canada?",
    "options": [
      "It is legally required for citizenship applicants",
      "It reduces government spending on social services",
      "It helps people in need, builds skills and friendships, and contributes to community well-being",
      "It allows immigrants to gain work experience"
    ],
    "answerIndex": 2,
    "explanation": "Millions of Canadians volunteer by helping people in need, assisting at schools, supporting food banks, and encouraging newcomers to integrate. Volunteering is described as 'an excellent way to gain useful skills and develop friends and contacts' and is an important part of Canadian community life."
  },
  {
    "id": "q400",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Rule of Law",
    "question": "What does Canada's founding principle of the 'rule of law' mean?",
    "options": [
      "The majority always wins in a democracy",
      "Parliament can override any law",
      "Individuals and governments are regulated by laws, and no person or group is above the law",
      "The law applies only to those who are not citizens"
    ],
    "answerIndex": 2,
    "explanation": "One of Canada's founding principles is the rule of law: 'Individuals and governments are regulated by laws and not by arbitrary actions. No person or group is above the law.' This includes the government itself, meaning even those in power must follow the law."
  },

  # ─────────────────────────────────────────────────────────────────────────────
  # WHO WE ARE  (38 → +10 = 48)
  # ─────────────────────────────────────────────────────────────────────────────
  {
    "id": "q401",
    "topic": "Who We Are",
    "subtopic": "Languages",
    "question": "How many Anglophones and Francophones are there in Canada?",
    "options": [
      "12 million Anglophones and 3 million Francophones",
      "18 million Anglophones and 7 million Francophones",
      "25 million Anglophones and 9 million Francophones",
      "10 million Anglophones and 5 million Francophones"
    ],
    "answerIndex": 1,
    "explanation": "Canada has 18 million Anglophones (people who speak English as a first language) and 7 million Francophones (people who speak French as a first language). While the majority of Francophones live in Quebec, one million live in Ontario, New Brunswick and Manitoba."
  },
  {
    "id": "q402",
    "topic": "Who We Are",
    "subtopic": "Languages",
    "question": "Which is the only officially bilingual province in Canada?",
    "options": [
      "Quebec",
      "Ontario",
      "New Brunswick",
      "Manitoba"
    ],
    "answerIndex": 2,
    "explanation": "New Brunswick is the only officially bilingual province in Canada. About one-third of New Brunswick's population lives and works in French. The province has a proud Acadian heritage and the Francophone Acadian centre of Moncton."
  },
  {
    "id": "q403",
    "topic": "Who We Are",
    "subtopic": "Acadians",
    "question": "What was the 'Great Upheaval' in Canadian history?",
    "options": [
      "The forced relocation of Aboriginal peoples to reserves in the 1870s",
      "The deportation of more than two-thirds of the Acadians from their homeland between 1755 and 1763",
      "The migration of Loyalists from the United States after the American Revolution",
      "The displacement of Métis people during western settlement in the 1880s"
    ],
    "answerIndex": 1,
    "explanation": "The 'Great Upheaval' refers to the deportation of more than two-thirds of the Acadians from their homeland (present-day Maritime provinces) between 1755 and 1763, during the war between Britain and France. Despite this ordeal, the Acadians survived and maintained their unique identity."
  },
  {
    "id": "q404",
    "topic": "Who We Are",
    "subtopic": "Francophones",
    "question": "What did the House of Commons recognize in 2006 about Quebecers?",
    "options": [
      "That Quebec should become an independent nation",
      "That the Quebecois form a nation within a united Canada",
      "That Quebec has special veto power over constitutional amendments",
      "That French should be the sole official language of Quebec"
    ],
    "answerIndex": 1,
    "explanation": "In 2006, the House of Commons recognized that 'the Quebecois form a nation within a united Canada.' This recognition acknowledges the distinct identity, culture and language of Quebecers — the vast majority of whom are descendants of 8,500 French settlers from the 1600s and 1700s."
  },
  {
    "id": "q405",
    "topic": "Who We Are",
    "subtopic": "Indigenous History",
    "question": "When did the Canadian government formally apologize to former students of residential schools?",
    "options": [
      "1982",
      "1995",
      "2008",
      "2015"
    ],
    "answerIndex": 2,
    "explanation": "In 2008, Ottawa formally apologized to the former students of residential schools. From the 1800s until the 1980s, the federal government placed many Aboriginal children in residential schools to educate and assimilate them. The schools were poorly funded and many students experienced hardship or abuse."
  },
  {
    "id": "q406",
    "topic": "Who We Are",
    "subtopic": "Aboriginal Peoples",
    "question": "What language do the Métis people speak as their own distinct dialect?",
    "options": [
      "Cree",
      "Michif",
      "Inuktitut",
      "Dene"
    ],
    "answerIndex": 1,
    "explanation": "The Métis are a distinct people of mixed Aboriginal and European ancestry who speak their own dialect called Michif. The majority of Métis live in the Prairie provinces and come from both French- and English-speaking backgrounds."
  },
  {
    "id": "q407",
    "topic": "Who We Are",
    "subtopic": "Aboriginal Peoples",
    "question": "What percentage of Aboriginal people in Canada are First Nations, Métis, and Inuit respectively?",
    "options": [
      "First Nations 80%, Métis 15%, Inuit 5%",
      "First Nations 65%, Métis 30%, Inuit 4%",
      "First Nations 50%, Métis 40%, Inuit 10%",
      "First Nations 75%, Métis 20%, Inuit 5%"
    ],
    "answerIndex": 1,
    "explanation": "About 65% of the Aboriginal people in Canada are First Nations, while 30% are Métis and 4% are Inuit. Today about half of First Nations people live on reserve land in about 600 communities, while the other half live off-reserve, mainly in urban centres."
  },
  {
    "id": "q408",
    "topic": "Who We Are",
    "subtopic": "Immigration History",
    "question": "What does 'Inuit' mean in the Inuktitut language?",
    "options": [
      "The hunters",
      "The people of the north",
      "The people",
      "Children of the Arctic"
    ],
    "answerIndex": 2,
    "explanation": "Inuit means 'the people' in the Inuktitut language. The Inuit live in small, scattered communities across the Arctic. Their knowledge of the land, sea and wildlife enabled them to adapt to one of the harshest environments on earth."
  },
  {
    "id": "q409",
    "topic": "Who We Are",
    "subtopic": "Diversity",
    "question": "Since the 1970s, most immigrants to Canada have come from which region?",
    "options": [
      "Europe",
      "Africa",
      "Latin America",
      "Asian countries"
    ],
    "answerIndex": 3,
    "explanation": "Since the 1970s, most immigrants have come from Asian countries. This shift has greatly diversified Canada's population. The largest ethnic groups in Canada include English, French, Scottish, Irish, German, Italian, Chinese, Aboriginal, Ukrainian, Dutch, South Asian and Scandinavian."
  },
  {
    "id": "q410",
    "topic": "Who We Are",
    "subtopic": "Founding Peoples",
    "question": "What does Canada's constitutional tradition include that makes it unique in North America?",
    "options": [
      "A written constitution that can be changed by simple majority vote",
      "The oldest continuous constitutional tradition in the world and the only constitutional monarchy in North America",
      "A system where the President has veto power over Parliament",
      "A right to bear arms guaranteed since Confederation"
    ],
    "answerIndex": 1,
    "explanation": "Canada has inherited the oldest continuous constitutional tradition in the world and is the only constitutional monarchy in North America. Our institutions uphold a commitment to 'Peace, Order, and Good Government' — a key phrase in Canada's original constitutional document, the British North America Act of 1867."
  },

  # ─────────────────────────────────────────────────────────────────────────────
  # CANADA'S HISTORY  (62 → +10 = 72)
  # ─────────────────────────────────────────────────────────────────────────────
  {
    "id": "q411",
    "topic": "Canada's History",
    "subtopic": "Exploration",
    "question": "Who was the first European to map Canada's Atlantic coastline, and in what year?",
    "options": [
      "Jacques Cartier in 1534",
      "Samuel de Champlain in 1604",
      "John Cabot in 1497",
      "Martin Frobisher in 1576"
    ],
    "answerIndex": 2,
    "explanation": "John Cabot, an Italian immigrant to England, was the first to map Canada's Atlantic shore, setting foot on Newfoundland or Cape Breton Island in 1497 and claiming the 'New Founde Land' for England. European settlement in Newfoundland did not begin until 1610."
  },
  {
    "id": "q412",
    "topic": "Canada's History",
    "subtopic": "Exploration",
    "question": "What is the Iroquoian meaning of the word 'kanata' that gave Canada its name?",
    "options": [
      "Great river",
      "Land of the north",
      "Village",
      "Hunting ground"
    ],
    "answerIndex": 2,
    "explanation": "Between 1534 and 1542, Jacques Cartier heard two captured guides speak the Iroquoian word 'kanata,' meaning 'village.' By the 1550s, the name Canada began appearing on maps. Cartier made three voyages across the Atlantic, claiming the land for King Francis I of France."
  },
  {
    "id": "q413",
    "topic": "Canada's History",
    "subtopic": "War of 1812",
    "question": "Who was Laura Secord and why is she celebrated in Canadian history?",
    "options": [
      "A nurse who served in the First World War",
      "A pioneer wife who made a dangerous 30 km journey on foot to warn British troops of a planned American attack during the War of 1812",
      "A politician who fought for women's right to vote in Ontario",
      "An Aboriginal leader who helped negotiate peace treaties in the 1800s"
    ],
    "answerIndex": 1,
    "explanation": "In 1813 during the War of 1812, Laura Secord made a dangerous 19-mile (30 km) journey on foot to warn Lieutenant James FitzGibbon of a planned American attack. Her bravery contributed to the British victory at the Battle of Beaver Dams, and she is recognized as a heroine to this day."
  },
  {
    "id": "q414",
    "topic": "Canada's History",
    "subtopic": "War of 1812",
    "question": "What role did Lieutenant-Colonel Charles de Salaberry play in the War of 1812?",
    "options": [
      "He commanded the British fleet at the Battle of the Atlantic",
      "He burned the White House in Washington, D.C.",
      "He and 460 soldiers, mostly French Canadiens, turned back 4,000 American invaders at Châteauguay",
      "He captured Fort Detroit from the Americans"
    ],
    "answerIndex": 2,
    "explanation": "In 1813, Lieutenant-Colonel Charles de Salaberry and 460 soldiers, mostly French Canadiens, turned back 4,000 American invaders at Châteauguay, south of Montreal. This was a remarkable Canadian victory in the War of 1812 that demonstrated the bravery of French-Canadian forces."
  },
  {
    "id": "q415",
    "topic": "Canada's History",
    "subtopic": "Rebellions",
    "question": "What did Lord Durham recommend after the Rebellions of 1837–38?",
    "options": [
      "That Canada should seek independence from Britain immediately",
      "That Upper and Lower Canada be merged and given responsible government",
      "That French Canadians should be expelled from the country",
      "That Canada should form a military alliance with the United States"
    ],
    "answerIndex": 1,
    "explanation": "Lord Durham, an English reformer sent to report on the rebellions, recommended that Upper and Lower Canada be merged and given responsible government — meaning that ministers of the Crown must have the support of a majority of elected representatives. He controversially also said Canadiens should assimilate into English culture."
  },
  {
    "id": "q416",
    "topic": "Canada's History",
    "subtopic": "World Wars",
    "question": "What was Canada's role in the Battle of Amiens on August 8, 1918?",
    "options": [
      "Canada defended Amiens against a German counterattack",
      "The Canadian Corps led a victorious assault that Germans called 'the black day of the German Army'",
      "Canadian troops liberated Amiens from French Vichy forces",
      "Canada negotiated the Armistice at Amiens"
    ],
    "answerIndex": 1,
    "explanation": "Under General Sir Arthur Currie, Canada's greatest soldier, the Canadian Corps participated in the victorious Battle of Amiens on August 8, 1918 — which the Germans called 'the black day of the German Army.' This was part of Canada's famous Hundred Days campaign that helped end WWI."
  },
  {
    "id": "q417",
    "topic": "Canada's History",
    "subtopic": "World Wars",
    "question": "On D-Day (June 6, 1944), which beach did Canadian troops storm?",
    "options": [
      "Omaha Beach",
      "Gold Beach",
      "Juno Beach",
      "Sword Beach"
    ],
    "answerIndex": 2,
    "explanation": "In the epic invasion of Normandy on June 6, 1944 (D-Day), 15,000 Canadian troops stormed and captured Juno Beach from the German Army. Approximately one in ten Allied soldiers on D-Day was Canadian — a great national achievement."
  },
  {
    "id": "q418",
    "topic": "Canada's History",
    "subtopic": "Responsible Government",
    "question": "Who was the first leader of a responsible government in the Canadas and championed French language rights?",
    "options": [
      "Sir John A. Macdonald",
      "Sir Étienne-Paschal Taché",
      "Sir Louis-Hippolyte La Fontaine",
      "Lord Elgin"
    ],
    "answerIndex": 2,
    "explanation": "Sir Louis-Hippolyte La Fontaine, a champion of democracy and French language rights, became the first leader of a responsible government (similar to a Prime Minister) in Canada in 1849. He worked alongside Robert Baldwin to achieve responsible government in the Province of Canada."
  },
  {
    "id": "q419",
    "topic": "Canada's History",
    "subtopic": "World Wars",
    "question": "How many Canadians served and how many were killed in the Second World War?",
    "options": [
      "250,000 served, 10,000 killed",
      "500,000 served, 25,000 killed",
      "Over one million served, 44,000 killed",
      "750,000 served, 60,000 killed"
    ],
    "answerIndex": 2,
    "explanation": "More than one million Canadians and Newfoundlanders served in the Second World War (Newfoundland was a separate British entity at the time), out of a population of 11.5 million. Of these, 44,000 were killed. Canada had the third-largest navy in the world by the end of the war."
  },
  {
    "id": "q420",
    "topic": "Canada's History",
    "subtopic": "Notable Canadians",
    "question": "Who wrote the famous war poem 'In Flanders Fields' and when was it composed?",
    "options": [
      "Sir Arthur Currie, composed in 1918",
      "Lieutenant-Colonel John McCrae, a Canadian medical officer, composed it in 1915",
      "Agnes Macphail, composed in 1921",
      "Terry Fox, composed in 1980"
    ],
    "answerIndex": 1,
    "explanation": "Canadian medical officer Lieutenant-Colonel John McCrae composed the poem 'In Flanders Fields' in 1915. It begins 'In Flanders fields the poppies blow / Between the crosses, row on row.' It is often recited on Remembrance Day (November 11) and inspired the tradition of wearing red poppies."
  },

  # ─────────────────────────────────────────────────────────────────────────────
  # MODERN CANADA  (31 → +15 = 46)
  # ─────────────────────────────────────────────────────────────────────────────
  {
    "id": "q421",
    "topic": "Modern Canada",
    "subtopic": "Social Programs",
    "question": "When was unemployment insurance (now called employment insurance) introduced in Canada?",
    "options": [
      "1927",
      "1934",
      "1940",
      "1965"
    ],
    "answerIndex": 2,
    "explanation": "Unemployment insurance was introduced by the federal government in 1940. Canada built a social safety net over time: Old Age Security was introduced as early as 1927, and the Canada and Quebec Pension Plans in 1965. Today it is called employment insurance."
  },
  {
    "id": "q422",
    "topic": "Modern Canada",
    "subtopic": "International Organizations",
    "question": "What is NORAD and who are its members?",
    "options": [
      "A Nordic trade organization for Norway, Denmark and Canada",
      "The North American Aerospace Defence Command, a military alliance between Canada and the United States",
      "A NATO peacekeeping force based in Ottawa",
      "Canada's national defence department"
    ],
    "answerIndex": 1,
    "explanation": "NORAD stands for the North American Aerospace Defence Command, a military alliance between Canada and the United States. Canada joined NORAD along with NATO (the North Atlantic Treaty Organization) during the Cold War to protect against Soviet threats."
  },
  {
    "id": "q423",
    "topic": "Modern Canada",
    "subtopic": "International Role",
    "question": "How many Canadians were killed and wounded in the Korean War (1950–53)?",
    "options": [
      "100 dead, 300 wounded",
      "500 dead, 1,000 wounded",
      "2,000 dead, 5,000 wounded",
      "44 dead, 200 wounded"
    ],
    "answerIndex": 1,
    "explanation": "Canada participated in the UN operation defending South Korea in the Korean War (1950–53), with 500 dead and 1,000 wounded. Canada has taken part in numerous UN peacekeeping missions around the world, in places as varied as Egypt, Cyprus, Haiti, Yugoslavia, and Afghanistan."
  },
  {
    "id": "q424",
    "topic": "Modern Canada",
    "subtopic": "Society",
    "question": "What was the Quiet Revolution in Quebec?",
    "options": [
      "A peaceful protest movement against conscription in the Second World War",
      "A period of rapid social and political change in Quebec in the 1960s",
      "The quiet introduction of bilingualism laws across Canada in the 1950s",
      "The transition from the British Empire to the Commonwealth in the 1930s"
    ],
    "answerIndex": 1,
    "explanation": "Quebec experienced an era of rapid change in the 1960s known as the Quiet Revolution (Révolution tranquille). French-Canadian society modernized rapidly, the Catholic Church's influence declined, and many Quebecers began seeking greater autonomy or independence for Quebec."
  },
  {
    "id": "q425",
    "topic": "Modern Canada",
    "subtopic": "Immigration",
    "question": "When did Aboriginal people in Canada gain the right to vote in federal elections?",
    "options": [
      "1918",
      "1948",
      "1960",
      "1982"
    ],
    "answerIndex": 2,
    "explanation": "Aboriginal people were granted the right to vote in federal elections in 1960. Previously, most Canadians of Asian descent had also been denied voting rights; Japanese-Canadians were the last group to gain the right to vote, in 1948. Today every citizen over the age of 18 may vote."
  },
  {
    "id": "q426",
    "topic": "Modern Canada",
    "subtopic": "Sports",
    "question": "Who invented basketball and where was the invention connected to Canada?",
    "options": [
      "Wayne Gretzky invented it in Edmonton",
      "James Naismith, a Canadian, invented basketball in 1891",
      "Terry Fox invented it during his Marathon of Hope",
      "Paul Henderson invented it in 1972"
    ],
    "answerIndex": 1,
    "explanation": "Basketball was invented by Canadian James Naismith in 1891. Naismith was born in Ontario and invented the sport while working in Massachusetts, USA. Canada is proud of this invention as one of the world's most popular sports."
  },
  {
    "id": "q427",
    "topic": "Modern Canada",
    "subtopic": "Science and Technology",
    "question": "Who discovered insulin and how many lives has it saved?",
    "options": [
      "Dr. Wilder Penfield; saved millions from brain disease",
      "Sir Frederick Banting of Toronto and Charles Best; discovered a hormone to treat diabetes that has saved 16 million lives",
      "Dr. John Hopps; invented a cardiac pacemaker saving heart patients",
      "Reginald Fessenden; first wireless voice transmission"
    ],
    "answerIndex": 1,
    "explanation": "Sir Frederick Banting of Toronto and Charles Best discovered insulin, a hormone to treat diabetes that has saved 16 million lives worldwide. This is one of Canada's greatest contributions to medicine and human health."
  },
  {
    "id": "q428",
    "topic": "Modern Canada",
    "subtopic": "Arts and Culture",
    "question": "Who were the Group of Seven and what are they known for?",
    "options": [
      "Seven Canadian Prime Ministers who shaped modern Canada",
      "A group of seven Nobel Prize-winning Canadian scientists",
      "Artists founded in 1920 who developed a distinctive style capturing Canada's rugged wilderness landscapes",
      "Seven hockey players on Canada's first Olympic gold medal team"
    ],
    "answerIndex": 2,
    "explanation": "The Group of Seven, founded in 1920, were Canadian artists who developed a distinctive style of painting to capture Canada's rugged wilderness landscapes. They are historically perhaps the best-known Canadian visual artists and had a defining influence on Canadian art and national identity."
  },
  {
    "id": "q429",
    "topic": "Modern Canada",
    "subtopic": "Sports",
    "question": "Why is Terry Fox a hero to Canadians?",
    "options": [
      "He won multiple Olympic gold medals in track and field",
      "He was the first Canadian astronaut to walk in space",
      "He lost his leg to cancer and in 1980 began a cross-country 'Marathon of Hope' to raise money for cancer research",
      "He invented the game of basketball in 1891"
    ],
    "answerIndex": 2,
    "explanation": "In 1980, Terry Fox, a British Columbian who lost his right leg to cancer at age 18, began a cross-country run — the 'Marathon of Hope' — to raise money for cancer research. Though he did not finish the run and ultimately lost his battle with cancer, his legacy continues through annual Terry Fox runs worldwide."
  },
  {
    "id": "q430",
    "topic": "Modern Canada",
    "subtopic": "Science and Technology",
    "question": "What is the Canadarm and who built it?",
    "options": [
      "A Canadian-designed robotic arm used in outer space, invented by SPAR Aerospace and the National Research Council",
      "A mechanical harvesting machine for the wheat fields of the prairies",
      "A long-range Canadian missile defence system",
      "A specialized crane used in Canadian oil sands operations"
    ],
    "answerIndex": 0,
    "explanation": "The Canadarm is a robotic arm used in outer space, invented by SPAR Aerospace / National Research Council. Since 1989, the Canadian Space Agency and Canadian astronauts have participated in space exploration, often using the Canadarm aboard space shuttles and the International Space Station."
  },
  {
    "id": "q431",
    "topic": "Modern Canada",
    "subtopic": "International Organizations",
    "question": "What is La Francophonie and when did Canada help found it?",
    "options": [
      "A Quebec provincial festival of French culture, founded in 1967",
      "An international association of French-speaking countries that Canada helped found in 1970",
      "A Canadian government department promoting French language rights, founded in 1969",
      "A bilateral cultural agreement between France and Canada, founded in 1982"
    ],
    "answerIndex": 1,
    "explanation": "In 1970, Canada helped found La Francophonie, an international association of French-speaking countries. Quebec films, music, literary works and food have international stature, especially within La Francophonie. This reflects Canada's commitment to preserving French language and culture globally."
  },
  {
    "id": "q432",
    "topic": "Modern Canada",
    "subtopic": "Health Care",
    "question": "What does the Canada Health Act ensure?",
    "options": [
      "All Canadians receive free private health insurance",
      "Common elements and a basic standard of health care coverage across the country",
      "That hospitals must treat patients within 24 hours",
      "That provinces must spend at least 30% of their budget on health care"
    ],
    "answerIndex": 1,
    "explanation": "The Canada Health Act ensures common elements and a basic standard of coverage for health care across Canada. Health care is provided by the provinces and territories, and the federal government provides funding through transfers to help maintain the system."
  },
  {
    "id": "q433",
    "topic": "Modern Canada",
    "subtopic": "International Role",
    "question": "What happened to Japanese Canadians during the Second World War?",
    "options": [
      "They were celebrated for their loyalty to Canada",
      "They were forcibly relocated and their property sold without compensation; Canada apologized in 1988",
      "They were conscripted into the military",
      "They were permitted to serve in the Royal Canadian Navy"
    ],
    "answerIndex": 1,
    "explanation": "During WWII, Canadians of Japanese origin were forcibly relocated by the federal government and their property was sold without compensation — even though the military and RCMP advised Ottawa that they posed little danger. The Government of Canada apologized in 1988 for these wartime wrongs and compensated the victims."
  },
  {
    "id": "q434",
    "topic": "Modern Canada",
    "subtopic": "Broadcasting",
    "question": "Who were Marshall McLuhan and Harold Innis?",
    "options": [
      "Canadian prime ministers who served consecutively in the 1960s",
      "Pioneer thinkers in communications whose ideas changed how the world understands media",
      "Canadian artists who founded the Group of Seven",
      "Scientists who won Nobel Prizes for discoveries in chemistry"
    ],
    "answerIndex": 1,
    "explanation": "Marshall McLuhan and Harold Innis were pioneer thinkers in communications. McLuhan coined the phrase 'the medium is the message' and predicted the global village. Their ideas about media and communications have had a lasting impact on how the world understands the role of technology and information."
  },
  {
    "id": "q435",
    "topic": "Modern Canada",
    "subtopic": "International Organizations",
    "question": "What replaced the General Agreement on Tariffs and Trade (GATT) that helped open Canada's postwar economy?",
    "options": [
      "NAFTA (North American Free Trade Agreement)",
      "The World Trade Organization (WTO)",
      "The G8 summit framework",
      "The Trans-Pacific Partnership (TPP)"
    ],
    "answerIndex": 1,
    "explanation": "The General Agreement on Tariffs and Trade (GATT) was replaced by the World Trade Organization (WTO). After WWII, the world's restrictive trading policies were opened up by such treaties as GATT, now the WTO. These trade liberalization efforts contributed to Canada's postwar prosperity."
  },

  # ─────────────────────────────────────────────────────────────────────────────
  # HOW CANADIANS GOVERN THEMSELVES  (40 → +10 = 50)
  # ─────────────────────────────────────────────────────────────────────────────
  {
    "id": "q436",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "System of Government",
    "question": "What are the three key characteristics of Canada's system of government?",
    "options": [
      "A republic, a democracy, and a constitutional monarchy",
      "A federal state, a parliamentary democracy, and a constitutional monarchy",
      "A unitary state, a direct democracy, and a republic",
      "A federal state, a presidential democracy, and a constitutional monarchy"
    ],
    "answerIndex": 1,
    "explanation": "There are three key facts about Canada's system of government: our country is a federal state (power shared between federal and provincial governments), a parliamentary democracy (the people elect representatives to Parliament), and a constitutional monarchy (the Sovereign is Head of State)."
  },
  {
    "id": "q437",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "The Crown",
    "question": "Who appoints the Governor General of Canada and for how long do they typically serve?",
    "options": [
      "Elected by Parliament for a four-year term",
      "Appointed by the Prime Minister directly for three years",
      "Appointed by the Sovereign on the advice of the Prime Minister, usually for five years",
      "Appointed by the Senate for a seven-year term"
    ],
    "answerIndex": 2,
    "explanation": "The Governor General is appointed by the Sovereign on the advice of the Prime Minister, usually for five years. The Governor General represents the Sovereign in Canada. In each province, the Lieutenant Governor is appointed by the Governor General on the advice of the Prime Minister, also normally for five years."
  },
  {
    "id": "q438",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "Legislation",
    "question": "How many steps must a bill go through before it receives Royal Assent and becomes law in Canada?",
    "options": [
      "3 steps (Introduction, Debate, Vote)",
      "5 steps (three readings, committee, and royal assent)",
      "7 steps (First Reading, Second Reading, Committee, Report Stage, Third Reading, Senate process, Royal Assent)",
      "2 steps (House of Commons vote, and Senate vote)"
    ],
    "answerIndex": 2,
    "explanation": "A bill must pass through 7 steps: (1) First Reading — printed; (2) Second Reading — principles debated; (3) Committee Stage — studied clause by clause; (4) Report Stage — other amendments; (5) Third Reading — debate and vote; (6) Senate — similar process; and (7) Royal Assent — granted by the Governor General."
  },
  {
    "id": "q439",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "Separation of Powers",
    "question": "What are the three branches of government in Canada, and how do they relate to each other?",
    "options": [
      "The Crown, Parliament, and Police — they work independently",
      "The Executive, Legislative and Judicial branches — they work together and sometimes in creative tension to secure rights and freedoms",
      "Federal, Provincial, and Municipal — they share all responsibilities equally",
      "The Senate, Cabinet, and Supreme Court — they each have veto power over the others"
    ],
    "answerIndex": 1,
    "explanation": "The interplay between the three branches of government — the Executive, Legislative and Judicial — helps secure the rights and freedoms of Canadians. They work together but also sometimes in creative tension, providing checks and balances on each other."
  },
  {
    "id": "q440",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "Provincial Government",
    "question": "What are elected members of provincial and territorial legislatures called in different provinces?",
    "options": [
      "All provinces call them Members of Parliament (MPs)",
      "MLAs (most provinces), MNAs (Quebec), MPPs (Ontario), or MHAs (Newfoundland and Labrador)",
      "Senators in all provinces and territories",
      "Councillors in all provinces except Quebec"
    ],
    "answerIndex": 1,
    "explanation": "Members of provincial/territorial legislatures are called: Members of the Legislative Assembly (MLAs) in most provinces, Members of the National Assembly (MNAs) in Quebec, Members of the Provincial Parliament (MPPs) in Ontario, or Members of the House of Assembly (MHAs) in Newfoundland and Labrador."
  },
  {
    "id": "q441",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "Levels of Government",
    "question": "What responsibilities are shared between the federal and provincial governments?",
    "options": [
      "Defence and criminal law",
      "Navigation and currency",
      "Agriculture and immigration",
      "Foreign policy and citizenship"
    ],
    "answerIndex": 2,
    "explanation": "Agriculture and immigration are responsibilities shared between the federal and provincial governments. The federal government handles defence, foreign policy, criminal law, currency, and citizenship, while provinces handle education, health, natural resources, and civil rights."
  },
  {
    "id": "q442",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "Levels of Government",
    "question": "What role does the Commissioner play in Canada's three territories?",
    "options": [
      "Commissioners are elected by territorial residents to lead the government",
      "Commissioners represent the federal government and play a ceremonial role in the territories",
      "Commissioners are equivalent to provincial premiers",
      "Commissioners are appointed by the territorial assemblies"
    ],
    "answerIndex": 1,
    "explanation": "In the three territories (Yukon, Northwest Territories, Nunavut), the Commissioner represents the federal government and plays a ceremonial role — similar to a Lieutenant Governor in a province. Unlike provinces, the territories do not have the same level of self-governance."
  },
  {
    "id": "q443",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "Constitutional Monarchy",
    "question": "What is the distinction between Canada's Head of State and Head of Government?",
    "options": [
      "There is no distinction; the Prime Minister is both Head of State and Government",
      "The Head of State is the Sovereign (represented by the Governor General); the Head of Government is the Prime Minister who directs the governing of the country",
      "The Head of State is the Governor General; the Head of Government is the Senate Speaker",
      "The Head of State is the Chief Justice; the Head of Government is the Prime Minister"
    ],
    "answerIndex": 1,
    "explanation": "There is a clear distinction: Canada's Head of State is the Sovereign (represented in Canada by the Governor General), who has a non-partisan ceremonial role. The Head of Government is the Prime Minister, who actually directs the governing of the country and advises the Governor General."
  },
  {
    "id": "q444",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "Senate",
    "question": "Until what age do Senators appointed in Canada serve?",
    "options": [
      "65 years old",
      "70 years old",
      "75 years old",
      "They serve for life"
    ],
    "answerIndex": 2,
    "explanation": "Senators are appointed by the Governor General on the advice of the Prime Minister and serve until age 75. Both the House of Commons and the Senate consider and review bills. No bill can become law until it has been passed by both chambers and received Royal Assent."
  },
  {
    "id": "q445",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "Federal vs Provincial",
    "question": "Under Canada's federal system, what allows different provinces to adopt different policies?",
    "options": [
      "Provincial autonomy guaranteed by the Royal Proclamation of 1763",
      "Federalism, which allows different provinces to adopt policies tailored to their populations and experiment with new ideas",
      "The Senate's power to veto federal laws",
      "The Supreme Court's ability to issue provincial laws"
    ],
    "answerIndex": 1,
    "explanation": "Federalism allows different provinces to adopt policies tailored to their own populations and gives provinces the flexibility to experiment with new ideas and policies. This is why health care and education systems can differ between provinces, while national standards are maintained."
  },

  # ─────────────────────────────────────────────────────────────────────────────
  # FEDERAL ELECTIONS  (29 → +12 = 41)
  # ─────────────────────────────────────────────────────────────────────────────
  {
    "id": "q446",
    "topic": "Federal Elections",
    "subtopic": "Electoral System",
    "question": "How many electoral districts (ridings) is Canada divided into for federal elections?",
    "options": [
      "150 electoral districts",
      "250 electoral districts",
      "308 electoral districts",
      "400 electoral districts"
    ],
    "answerIndex": 2,
    "explanation": "Canada is divided into 308 electoral districts (also known as ridings or constituencies). An electoral district is a geographical area represented by one Member of Parliament (MP). Citizens in each district vote for one MP to represent them in the House of Commons."
  },
  {
    "id": "q447",
    "topic": "Federal Elections",
    "subtopic": "Voting",
    "question": "When must federal elections be held by law in Canada?",
    "options": [
      "The first Monday in May every five years",
      "The third Monday in October every four years following the most recent general election",
      "Any time the Prime Minister chooses, with no fixed schedule",
      "Every three years on the second Monday in September"
    ],
    "answerIndex": 1,
    "explanation": "Under legislation passed by Parliament, federal elections must be held on the third Monday in October every four years following the most recent general election. However, the Prime Minister may still ask the Governor General to call an earlier election."
  },
  {
    "id": "q448",
    "topic": "Federal Elections",
    "subtopic": "Voter Registration",
    "question": "What is the National Register of Electors?",
    "options": [
      "A list of all political party candidates in Canada",
      "A permanent database of Canadian citizens 18 years of age or older who are qualified to vote",
      "A record of everyone who voted in the last federal election",
      "A list of all MPs and senators in the federal government"
    ],
    "answerIndex": 1,
    "explanation": "The National Register of Electors is a permanent database of Canadian citizens 18 years of age or older who are qualified to vote in federal elections and referendums. Elections Canada, a neutral agency of Parliament, uses this register to produce voters' lists and mail voter information cards."
  },
  {
    "id": "q449",
    "topic": "Federal Elections",
    "subtopic": "Voting",
    "question": "What can you do if you did not receive a voter information card before an election?",
    "options": [
      "You cannot vote without a voter information card",
      "You must apply for citizenship again",
      "You can be added to the voters' list at any time, including on election day",
      "You must vote by mail only"
    ],
    "answerIndex": 2,
    "explanation": "Even if you choose not to be listed in the National Register of Electors or do not receive a voter information card, you can still be added to the voters' list at any time, including on election day. You can call Elections Canada at 1-800-463-6868 to ensure you are on the voters' list."
  },
  {
    "id": "q450",
    "topic": "Federal Elections",
    "subtopic": "Voting",
    "question": "What is an advance poll and why might you use one?",
    "options": [
      "A pre-election survey to gauge public opinion",
      "A ballot you mail to Elections Canada",
      "An opportunity to vote before election day if you cannot or prefer not to vote on the scheduled election day",
      "A special poll for voters living outside Canada"
    ],
    "answerIndex": 2,
    "explanation": "If you cannot or do not wish to vote on election day, you can vote at the advance polls or by special ballot. The dates and locations are listed on your voter information card. Advance polls ensure all eligible voters can participate regardless of their schedule."
  },
  {
    "id": "q451",
    "topic": "Federal Elections",
    "subtopic": "Voting System",
    "question": "How does a candidate win a seat in the House of Commons?",
    "options": [
      "By winning more than 50% of the votes in their electoral district",
      "By receiving the most votes of any candidate in their electoral district (first-past-the-post)",
      "By being appointed by their political party leader",
      "By winning a runoff election between the top two candidates"
    ],
    "answerIndex": 1,
    "explanation": "The candidate who receives the most votes in an electoral district becomes the MP for that district — this is called the 'first-past-the-post' system. A candidate does not need a majority (50%+), just more votes than any other candidate in the riding."
  },
  {
    "id": "q452",
    "topic": "Federal Elections",
    "subtopic": "Municipal Government",
    "question": "What types of laws do municipal (local) governments pass, and what are they called?",
    "options": [
      "Municipal governments pass federal laws on behalf of the national government",
      "Municipal governments pass provincial regulations called 'sub-laws'",
      "Municipal governments pass laws called 'by-laws' that affect only the local community",
      "Municipal governments do not pass laws; they only administer federal decisions"
    ],
    "answerIndex": 2,
    "explanation": "Local or municipal governments usually have a council that passes laws called 'by-laws' that affect only the local community. A council usually includes a mayor (or reeve) and councillors or aldermen. Municipalities handle local planning, roads, garbage, snow removal, firefighting, and recreation."
  },
  {
    "id": "q453",
    "topic": "Federal Elections",
    "subtopic": "Official Opposition",
    "question": "What is the role of opposition parties in Canada's Parliament?",
    "options": [
      "To delay all government legislation as long as possible",
      "To form a parallel shadow government",
      "To peacefully oppose or try to improve government proposals; the Official Opposition has the most seats among opposition parties",
      "To advise the Governor General on appointments"
    ],
    "answerIndex": 2,
    "explanation": "The role of opposition parties is to peacefully oppose or try to improve government proposals. The opposition party with the most members of the House of Commons is the Official Opposition or 'Her Majesty's Loyal Opposition.' Opposition parties keep the government accountable by questioning its decisions."
  },
  {
    "id": "q454",
    "topic": "Federal Elections",
    "subtopic": "Electoral Districts",
    "question": "What is a by-election and when does it occur?",
    "options": [
      "An election held simultaneously in all ridings on a fixed date",
      "An election held in a specific electoral district when a seat becomes vacant between general elections",
      "An election held only in provinces, not at the federal level",
      "A special election for the Senate"
    ],
    "answerIndex": 1,
    "explanation": "A by-election is held in a specific electoral district when a seat in the House of Commons becomes vacant between general elections — for example, when an MP resigns, dies, or is expelled. By-elections allow the riding's constituents to choose a new representative."
  },
  {
    "id": "q455",
    "topic": "Federal Elections",
    "subtopic": "Political Parties",
    "question": "What are the three major political parties historically represented in the House of Commons?",
    "options": [
      "The Liberal Party, the Reform Party, and the Green Party",
      "The Conservative Party, the Liberal Party, and the New Democratic Party",
      "The Conservative Party, the Bloc Québécois, and the New Democratic Party",
      "The Liberal Party, the Green Party, and the New Democratic Party"
    ],
    "answerIndex": 1,
    "explanation": "The three major political parties historically represented in the House of Commons are: the Conservative Party, the Liberal Party, and the New Democratic Party. Canada's multi-party system means several parties compete for seats, and voters choose based on their preferred candidate and party platform."
  },
  {
    "id": "q456",
    "topic": "Federal Elections",
    "subtopic": "Campaign",
    "question": "Who is eligible to run as a candidate in a Canadian federal election?",
    "options": [
      "Only members of registered political parties",
      "Any Canadian citizen who is 18 years old or older",
      "Any permanent resident aged 18 or older",
      "Only Canadian citizens who have lived in Canada for at least 10 years"
    ],
    "answerIndex": 1,
    "explanation": "Canadian citizens who are 18 years old or older may run in a federal election. Candidates can run as members of a registered political party or as independents. There can be many candidates in an electoral district, and the one with the most votes becomes the MP."
  },
  {
    "id": "q457",
    "topic": "Federal Elections",
    "subtopic": "Minority Government",
    "question": "What is a confidence vote, and what happens if the government loses one?",
    "options": [
      "A vote where MPs rate the Prime Minister's performance; losing it results in a salary cut",
      "A vote on major issues such as the budget; if the majority of MPs vote against the government, it usually results in the Prime Minister asking the Governor General to call an election",
      "A vote held annually to confirm the government stays in power",
      "A Senate vote on whether to approve the Prime Minister's cabinet picks"
    ],
    "answerIndex": 1,
    "explanation": "When the House of Commons votes on a major issue such as the budget, this is considered a matter of confidence. If a majority of MPs vote against a major government decision, the party in power is defeated, which usually results in the Prime Minister asking the Governor General to call an election."
  },

  # ─────────────────────────────────────────────────────────────────────────────
  # THE JUSTICE SYSTEM  (26 → +12 = 38)
  # ─────────────────────────────────────────────────────────────────────────────
  {
    "id": "q458",
    "topic": "The Justice System",
    "subtopic": "Law",
    "question": "What is 'due process' in the Canadian justice system?",
    "options": [
      "The time it takes to process a court case from start to finish",
      "The principle that the government must respect all legal rights a person is entitled to under the law",
      "A specific court procedure for handling criminal cases",
      "The process of appealing a decision to a higher court"
    ],
    "answerIndex": 1,
    "explanation": "Due process is the principle that the government must respect all of the legal rights a person is entitled to under the law. The Canadian justice system guarantees everyone due process under the law, ensuring that legal proceedings are fair and that rights are protected."
  },
  {
    "id": "q459",
    "topic": "The Justice System",
    "subtopic": "Rights",
    "question": "What does the foundational principle of 'presumption of innocence' mean in Canada?",
    "options": [
      "Police must assume everyone is innocent until an officer witnesses the crime",
      "Everyone is considered innocent until proven guilty in a court of law",
      "A person charged with a crime cannot be arrested before trial",
      "Only first-time offenders are presumed innocent"
    ],
    "answerIndex": 1,
    "explanation": "The presumption of innocence is a foundational principle: everyone is innocent until proven guilty. Canada's judicial system is founded on this principle, meaning the burden of proof lies with the prosecution, not with the accused to prove their innocence."
  },
  {
    "id": "q460",
    "topic": "The Justice System",
    "subtopic": "Courts",
    "question": "What does the Federal Court of Canada deal with?",
    "options": [
      "All criminal cases across Canada",
      "Matters concerning the federal government",
      "Appeals from provincial courts",
      "Cases involving Indigenous land rights only"
    ],
    "answerIndex": 1,
    "explanation": "The Federal Court of Canada deals with matters concerning the federal government, such as immigration cases, federal tax disputes, intellectual property, and judicial review of federal administrative decisions. The Supreme Court of Canada is the country's highest court."
  },
  {
    "id": "q461",
    "topic": "The Justice System",
    "subtopic": "Courts",
    "question": "What are small claims courts used for?",
    "options": [
      "Cases involving minor criminal offences like jaywalking",
      "Civil cases involving small sums of money",
      "Family disputes about child custody",
      "Cases involving government employees"
    ],
    "answerIndex": 1,
    "explanation": "Small claims courts handle civil cases involving small sums of money. They provide an accessible and affordable way for individuals to resolve minor financial disputes without needing a lawyer, making the justice system more accessible to ordinary Canadians."
  },
  {
    "id": "q462",
    "topic": "The Justice System",
    "subtopic": "Police",
    "question": "In which provinces does the RCMP not serve as the provincial police force?",
    "options": [
      "Alberta and British Columbia",
      "Ontario and Quebec",
      "Manitoba and Saskatchewan",
      "Nova Scotia and New Brunswick"
    ],
    "answerIndex": 1,
    "explanation": "The Royal Canadian Mounted Police (RCMP) enforces federal laws throughout Canada and serves as the provincial police in all provinces and territories EXCEPT Ontario and Quebec, which have their own provincial police forces (Ontario Provincial Police and Sûreté du Québec)."
  },
  {
    "id": "q463",
    "topic": "The Justice System",
    "subtopic": "Rights",
    "question": "What should you do if you are not satisfied with how police have handled a matter or their conduct?",
    "options": [
      "There is no process to challenge police conduct in Canada",
      "You can bring your concerns to an internal police process, as almost all police forces in Canada have a process for handling complaints",
      "You must hire a lawyer to file a complaint with the Supreme Court",
      "You can only complain to your local MP"
    ],
    "answerIndex": 1,
    "explanation": "Almost all police forces in Canada have a process by which you can bring your concerns to the police and seek action. This accountability mechanism ensures police are held to high standards and Canadians can question police service or conduct when needed."
  },
  {
    "id": "q464",
    "topic": "The Justice System",
    "subtopic": "Rights of the Accused",
    "question": "What does it mean that 'the law in Canada applies to everyone, including judges, politicians and the police'?",
    "options": [
      "All public officials must pass the same bar exam as lawyers",
      "It is the rule of law — no one is above the law, regardless of their position or authority",
      "Police officers can be arrested for minor offences just like ordinary citizens",
      "Judges must follow the same traffic laws as everyone else"
    ],
    "answerIndex": 1,
    "explanation": "This is the principle of the rule of law: no person or group is above the law, not even those in positions of authority. The law applies to judges, politicians, police, and citizens alike. Our laws provide order in society, a peaceful way to settle disputes, and express the values and beliefs of Canadians."
  },
  {
    "id": "q465",
    "topic": "The Justice System",
    "subtopic": "Rights",
    "question": "What is legal aid and who can access it?",
    "options": [
      "A government website providing legal information to citizens",
      "Free legal services provided by law schools",
      "Legal services available free of charge or at low cost to people who cannot afford a lawyer",
      "A government program that reimburses people for legal fees after a court case"
    ],
    "answerIndex": 2,
    "explanation": "If you cannot pay for a lawyer, in most communities there are legal aid services available free of charge or at a low cost. This ensures that access to the justice system is not limited only to those who can afford it, reflecting the principle of equal justice under the law."
  },
  {
    "id": "q466",
    "topic": "The Justice System",
    "subtopic": "Law",
    "question": "What does the blindfolded Lady Justice symbolize?",
    "options": [
      "That justice is blind to the suffering of victims",
      "That judges cannot watch court proceedings",
      "The impartial manner in which laws are administered — blind to all considerations but the facts",
      "That the law is too complex for ordinary citizens to understand"
    ],
    "answerIndex": 2,
    "explanation": "The blindfolded Lady Justice holding scales symbolizes the impartial manner in which laws are administered: blind to all considerations but the facts. This symbol, seen at the Vancouver Law Courts and many Canadian courthouses, represents that justice applies equally regardless of a person's status."
  },
  {
    "id": "q467",
    "topic": "The Justice System",
    "subtopic": "Rights of the Accused",
    "question": "What is Canada's legal system based on in terms of heritage?",
    "options": [
      "The Napoleonic Code of France only",
      "The United States Constitution",
      "The rule of law, freedom under the law, democratic principles, and due process, inherited from Britain",
      "Indigenous customary law traditions"
    ],
    "answerIndex": 2,
    "explanation": "Canada's legal system is based on a heritage that includes the rule of law, freedom under the law, democratic principles and due process. It also draws on English common law, the civil code of France (in Quebec), and the unwritten constitution inherited from Great Britain."
  },
  {
    "id": "q468",
    "topic": "The Justice System",
    "subtopic": "Courts",
    "question": "What types of courts exist at the provincial level for lesser offences?",
    "options": [
      "Only one type of court exists in each province",
      "Provincial courts for lesser offences, family courts, traffic courts, and small claims courts",
      "Provincial courts handle all matters from minor traffic offences to murder cases",
      "Provincial courts only handle civil, not criminal, matters"
    ],
    "answerIndex": 1,
    "explanation": "In most provinces there is an appeal court and a trial court (sometimes called the Court of Queen's Bench or Supreme Court). There are also provincial courts for lesser offences, family courts, traffic courts, and small claims courts for civil cases involving small sums. This structure ensures that cases are heard in the most appropriate court."
  },
  {
    "id": "q469",
    "topic": "The Justice System",
    "subtopic": "Jury",
    "question": "In what types of situations can Canadians ask the police for help?",
    "options": [
      "Only in emergency situations involving physical danger",
      "Only in criminal matters; civil disputes must go to court directly",
      "In all kinds of situations — accidents, theft, assault, missing persons, witnessing crimes, or any time you need help",
      "Only when filing an official complaint about another person"
    ],
    "answerIndex": 2,
    "explanation": "You can ask the police for help in all kinds of situations — if there's been an accident, if something has been stolen from you, if you are a victim of assault, if you witness a crime, or if someone you know has gone missing. The police are there to keep people safe and enforce the law."
  },

  # ─────────────────────────────────────────────────────────────────────────────
  # CANADIAN SYMBOLS  (26 → +15 = 41)
  # ─────────────────────────────────────────────────────────────────────────────
  {
    "id": "q470",
    "topic": "Canadian Symbols",
    "subtopic": "Flags and Emblems",
    "question": "What is the origin of Canada's red-white-red flag pattern?",
    "options": [
      "It was taken from the Union Jack of Great Britain",
      "It comes from the flag of the Royal Military College, Kingston, founded in 1876",
      "It represents the three founding peoples — Aboriginal, French, and British",
      "It was designed by a committee of Parliament in 1965"
    ],
    "answerIndex": 1,
    "explanation": "The red-white-red pattern of the Canadian flag comes from the flag of the Royal Military College, Kingston, founded in 1876. Red and white had been colours of France and England since the Middle Ages and became Canada's national colours in 1921. The new Canadian flag was first raised in 1965."
  },
  {
    "id": "q471",
    "topic": "Canadian Symbols",
    "subtopic": "Royal Symbols",
    "question": "What is the history of the fleur-de-lys as a Canadian symbol?",
    "options": [
      "It was introduced to Canada by British colonists in the 1700s",
      "It was adopted by the French king in 496 AD, symbolized French royalty for over 1,000 years, and was included in the Canadian Red Ensign before Quebec adopted its own flag in 1948",
      "It was designed by French-Canadian artists in the 1960s as a symbol of Quebec identity",
      "It represents the three rivers of Quebec — the St. Lawrence, Ottawa, and Richelieu"
    ],
    "answerIndex": 1,
    "explanation": "The fleur-de-lys ('lily flower') was adopted by the French king in the year 496 and became the symbol of French royalty for over a thousand years, including in New France. Revived at Confederation, it was in the Canadian Red Ensign. In 1948, Quebec adopted its own flag based on the Cross and fleur-de-lys."
  },
  {
    "id": "q472",
    "topic": "Canadian Symbols",
    "subtopic": "Buildings and Landmarks",
    "question": "What happened to the Centre Block of the Parliament Buildings in 1916 and when was it rebuilt?",
    "options": [
      "It was damaged in a German air raid in 1916 and rebuilt in 1925",
      "It was destroyed by an accidental fire in 1916 and rebuilt in 1922",
      "It was demolished for renovations in 1916 and rebuilt in 1930",
      "It was flooded by the Ottawa River in 1916 and rebuilt in 1920"
    ],
    "answerIndex": 1,
    "explanation": "The Centre Block of the Parliament Buildings was destroyed by an accidental fire in 1916 and rebuilt in 1922. The Library of Parliament is the only part of the original building that survived the fire. The Peace Tower, completed in 1927, was built as a memorial to the First World War."
  },
  {
    "id": "q473",
    "topic": "Canadian Symbols",
    "subtopic": "Buildings and Landmarks",
    "question": "What is the Memorial Chamber inside the Peace Tower?",
    "options": [
      "A gallery of paintings depicting Canadian battles",
      "A room containing the Books of Remembrance with the names of soldiers who died serving Canada",
      "A memorial to all prime ministers of Canada",
      "A chamber where senators are sworn in"
    ],
    "answerIndex": 1,
    "explanation": "The Memorial Chamber within the Peace Tower contains the Books of Remembrance in which are written the names of soldiers, sailors and airmen who died serving Canada in wars or while on duty. The Peace Tower was completed in 1927 in memory of the First World War."
  },
  {
    "id": "q474",
    "topic": "Canadian Symbols",
    "subtopic": "National Symbols",
    "question": "On which Canadian coin does the beaver appear?",
    "options": [
      "The one-dollar coin (loonie)",
      "The two-dollar coin (toonie)",
      "The five-cent coin (nickel)",
      "The twenty-five cent coin (quarter)"
    ],
    "answerIndex": 2,
    "explanation": "The industrious beaver can be seen on the five-cent coin (nickel). The beaver was adopted as a symbol of the Hudson's Bay Company centuries ago and became an emblem of the St. Jean Baptiste Society in 1834. It also appears on the coats of arms of Saskatchewan, Alberta, and cities such as Montreal and Toronto."
  },
  {
    "id": "q475",
    "topic": "Canadian Symbols",
    "subtopic": "Coat of Arms",
    "question": "What is Canada's national motto and what does it mean?",
    "options": [
      "\"Peace, Order, and Good Government\" — meaning stable democratic governance",
      "\"A Mari Usque Ad Mare\" — meaning 'from sea to sea' in Latin",
      "\"True North Strong and Free\" — meaning national independence",
      "\"Glorious and Free\" — taken from the national anthem"
    ],
    "answerIndex": 1,
    "explanation": "Canada's national motto is 'A Mari Usque Ad Mare,' which in Latin means 'from sea to sea.' It comes from Psalm 72 and was suggested by Sir Leonard Tilley. Canada adopted its official coat of arms and national motto after the First World War as an expression of national pride."
  },
  {
    "id": "q476",
    "topic": "Canadian Symbols",
    "subtopic": "Anthem",
    "question": "When was 'O Canada' first sung and when did it become the official National Anthem?",
    "options": [
      "First sung in 1867; became the anthem in 1900",
      "First sung in 1880 in Quebec City; became the National Anthem in 1980",
      "First sung in 1927; became the National Anthem in 1967",
      "First sung in 1900; became the National Anthem in 1967"
    ],
    "answerIndex": 1,
    "explanation": "O Canada was first sung in Quebec City in 1880. It was proclaimed as the National Anthem in 1980. French and English Canadians sing different words to the National Anthem — both versions honour Canada's identity and traditions."
  },
  {
    "id": "q477",
    "topic": "Canadian Symbols",
    "subtopic": "Royal Symbols",
    "question": "What is the Royal Anthem of Canada and when is it played?",
    "options": [
      "O Canada — played at all official government events",
      "'God Save the King (or Queen)' — played or sung when Canadians wish to honour the Sovereign",
      "The Ode to Newfoundland — played at the opening of Parliament",
      "The Maple Leaf Forever — played at military ceremonies"
    ],
    "answerIndex": 1,
    "explanation": "The Royal Anthem of Canada is 'God Save the King (or Queen).' It can be played or sung on any occasion when Canadians wish to honour the Sovereign. This is distinct from the National Anthem, 'O Canada,' which is used to celebrate the nation."
  },
  {
    "id": "q478",
    "topic": "Canadian Symbols",
    "subtopic": "Honours",
    "question": "When was the Order of Canada established and what anniversary did it mark?",
    "options": [
      "1867, at Confederation",
      "1927, for Canada's 60th anniversary",
      "1967, Canada's centennial of Confederation",
      "1982, when the Constitution was patriated"
    ],
    "answerIndex": 2,
    "explanation": "Canada started its own honours system with the Order of Canada in 1967 — the centennial (100th anniversary) of Confederation. Before this, Canada used British honours. The Order of Canada recognizes outstanding citizens who have made significant contributions to Canadian society."
  },
  {
    "id": "q479",
    "topic": "Canadian Symbols",
    "subtopic": "Sports Trophies",
    "question": "Who donated the Stanley Cup and the Clarkson Cup, and what are they awarded for?",
    "options": [
      "Lord Grey donated the Stanley Cup for hockey; Prime Minister Trudeau donated the Clarkson Cup for women's hockey",
      "Lord Stanley (Governor General) donated the Stanley Cup in 1892 for hockey; Adrienne Clarkson (Governor General) established the Clarkson Cup in 2005 for women's hockey",
      "The NHL donated the Stanley Cup in 1917; the CFL donated the Clarkson Cup in 1909",
      "Lord Grey donated both cups — the Stanley Cup for men's hockey and the Clarkson Cup for women's hockey"
    ],
    "answerIndex": 1,
    "explanation": "Lord Stanley, the Governor General, donated the Stanley Cup in 1892 for the NHL championship. The Clarkson Cup was established in 2005 by Adrienne Clarkson, the 26th Governor General (and the first of Asian origin), for women's hockey. Both cups celebrate Canada's beloved sport of ice hockey."
  },
  {
    "id": "q480",
    "topic": "Canadian Symbols",
    "subtopic": "Sports",
    "question": "Which sport is Canada's official summer sport and what is its origin?",
    "options": [
      "Soccer, introduced by British settlers in the 1800s",
      "Curling, introduced by Scottish pioneers",
      "Lacrosse, an ancient sport first played by Aboriginal peoples",
      "Baseball, introduced by American settlers"
    ],
    "answerIndex": 2,
    "explanation": "Lacrosse is Canada's official summer sport. It is an ancient sport first played by Aboriginal peoples and remains an important part of Canadian sporting culture. Ice hockey is the national winter sport, while soccer has the most registered players of any game in Canada."
  },
  {
    "id": "q481",
    "topic": "Canadian Symbols",
    "subtopic": "Anthem and Holidays",
    "question": "What is Victoria Day in Canada and when is it celebrated?",
    "options": [
      "The birthday of the current Sovereign's representative, celebrated July 1",
      "The first Monday after May 25 — also known as the Sovereign's Birthday",
      "The anniversary of Queen Victoria's coronation, celebrated May 24",
      "A holiday celebrating the building of the Parliament Buildings, celebrated September 1"
    ],
    "answerIndex": 1,
    "explanation": "Victoria Day is celebrated on the Monday preceding May 25 and is also known as the Sovereign's Birthday. It honours the legacy of Queen Victoria, under whose reign Canada became a Dominion in 1867. Other national holidays include Canada Day (July 1), Remembrance Day (November 11), and Thanksgiving (second Monday of October)."
  },
  {
    "id": "q482",
    "topic": "Canadian Symbols",
    "subtopic": "Honours",
    "question": "What is the Victoria Cross (V.C.) and who was the first Canadian to receive it?",
    "options": [
      "Canada's highest civilian honour for community service; first received by John McCrae",
      "The highest military honour for conspicuous bravery in the presence of the enemy; first received by Lieutenant Alexander Roberts Dunn in the Crimean War (1854)",
      "An honour awarded to all veterans who served in the World Wars",
      "A medal given to all soldiers completing 10 years of service"
    ],
    "answerIndex": 1,
    "explanation": "The Victoria Cross (V.C.) is the highest honour available to Canadians, awarded for the most conspicuous bravery in the presence of the enemy. The V.C. has been awarded to 96 Canadians. The first Canadian was Lieutenant Alexander Roberts Dunn, who served in the British Army's Charge of the Light Brigade at Balaclava (1854)."
  },
  {
    "id": "q483",
    "topic": "Canadian Symbols",
    "subtopic": "Anthem and Holidays",
    "question": "What are Canada's three language-related requirements for citizenship, according to the Official Languages Act?",
    "options": [
      "Citizens must be fluent in both French and English",
      "Citizens must speak at least one language, plus take a civics test in English or French",
      "The Act establishes equality of French and English in Parliament, maintains official language minority communities, and promotes equality of both languages in Canadian society",
      "Citizens must pass language tests in both English and French"
    ],
    "answerIndex": 2,
    "explanation": "The Official Languages Act (1969) has three main objectives: (1) Establish equality between French and English in Parliament and government; (2) Maintain and develop official language minority communities; and (3) Promote equality of French and English in Canadian society. Citizens aged 18-54 must demonstrate adequate knowledge of English or French."
  },
  {
    "id": "q484",
    "topic": "Canadian Symbols",
    "subtopic": "Symbols",
    "question": "What inspired the term 'Dominion of Canada' and who suggested it?",
    "options": [
      "It was suggested by John A. Macdonald, inspired by Britain's dominion over the seas",
      "It was suggested by Sir Leonard Tilley, inspired by Psalm 72's reference to 'dominion from sea to sea'",
      "It was suggested by Queen Victoria, reflecting Britain's imperial dominion",
      "It was agreed upon by all Fathers of Confederation without a specific individual suggesting it"
    ],
    "answerIndex": 1,
    "explanation": "Sir Leonard Tilley, an elected official and Father of Confederation from New Brunswick, suggested the term 'Dominion of Canada' in 1864. He was inspired by Psalm 72 in the Bible, which refers to 'dominion from sea to sea and from the river to the ends of the earth.' This embodied the vision of a united nation spanning a continent."
  },

  # ─────────────────────────────────────────────────────────────────────────────
  # CANADA'S ECONOMY  (24 → +14 = 38)
  # ─────────────────────────────────────────────────────────────────────────────
  {
    "id": "q485",
    "topic": "Canada's Economy",
    "subtopic": "Free Trade",
    "question": "When did Canada enact free trade with the United States?",
    "options": [
      "1984",
      "1988",
      "1994",
      "2001"
    ],
    "answerIndex": 1,
    "explanation": "In 1988, Canada enacted free trade with the United States. Mexico became a partner in 1994 in the broader North American Free Trade Agreement (NAFTA), creating a trading block of over 444 million people and over $1 trillion in merchandise trade. These agreements helped Canada maintain its prosperity."
  },
  {
    "id": "q486",
    "topic": "Canada's Economy",
    "subtopic": "International Organizations",
    "question": "Which countries are part of the G8 group of leading industrialized countries with Canada?",
    "options": [
      "United States, Germany, United Kingdom, Italy, France, Japan, Russia",
      "United States, China, India, Brazil, Australia, South Korea, Mexico",
      "United States, United Kingdom, France, Australia, New Zealand, Japan, Spain",
      "United States, Germany, France, Netherlands, Belgium, Sweden, Switzerland"
    ],
    "answerIndex": 0,
    "explanation": "Canada is part of the G8 group of leading industrialized countries, along with the United States, Germany, the United Kingdom, Italy, France, Japan and Russia. Canada has one of the ten largest economies in the world. The G8 meets regularly to coordinate economic and political policies."
  },
  {
    "id": "q487",
    "topic": "Canada's Economy",
    "subtopic": "Economic Sectors",
    "question": "Approximately what percentage of working Canadians have jobs in service industries?",
    "options": [
      "More than 25%",
      "About 50%",
      "More than 75%",
      "More than 90%"
    ],
    "answerIndex": 2,
    "explanation": "More than 75% of working Canadians now have jobs in service industries. Service industries provide thousands of different jobs in transportation, education, health care, construction, banking, communications, retail services, tourism and government — making the service sector the dominant part of Canada's economy."
  },
  {
    "id": "q488",
    "topic": "Canada's Economy",
    "subtopic": "Manufacturing",
    "question": "What types of products does Canada's manufacturing sector produce?",
    "options": [
      "Only automotive products and raw materials",
      "Paper, high-technology equipment, aerospace technology, automobiles, machinery, food, clothing and many other goods",
      "Primarily agricultural products and timber",
      "Electronics and consumer goods only"
    ],
    "answerIndex": 1,
    "explanation": "Canada's manufacturing industries make products to sell in Canada and around the world, including paper, high-technology equipment, aerospace technology, automobiles, machinery, food, clothing and many other goods. The United States is Canada's largest international trading partner for manufactured goods."
  },
  {
    "id": "q489",
    "topic": "Canada's Economy",
    "subtopic": "Natural Resources",
    "question": "What are the main natural resource industries in Canada?",
    "options": [
      "Electronics, pharmaceuticals, and telecommunications",
      "Forestry, fishing, agriculture, mining and energy",
      "Tourism, entertainment, and hospitality",
      "Banking, insurance, and financial services"
    ],
    "answerIndex": 1,
    "explanation": "Canada's natural resources industries include forestry, fishing, agriculture, mining and energy. These industries have played an important part in Canada's history and development. Today, a large percentage of Canada's exports are natural resource commodities, particularly to the United States."
  },
  {
    "id": "q490",
    "topic": "Canada's Economy",
    "subtopic": "Trade",
    "question": "What fraction of Canadian exports are destined for the United States?",
    "options": [
      "About one-quarter",
      "About one-half",
      "Over three-quarters",
      "Almost all (95%+)"
    ],
    "answerIndex": 2,
    "explanation": "Over three-quarters (75%+) of Canadian exports are destined for the U.S.A. Canada and the United States have the biggest bilateral trading relationship in the world. Integrated Canada-U.S.A. supply chains compete with the rest of the world across many sectors."
  },
  {
    "id": "q491",
    "topic": "Canada's Economy",
    "subtopic": "Trade",
    "question": "What is the Peace Arch at Blaine, Washington, and what is its significance?",
    "options": [
      "A monument marking the end of the War of 1812",
      "A symbol of Canada-US friendship inscribed with 'children of a common mother' and 'brethren dwelling together in unity'",
      "A border checkpoint celebrating NAFTA",
      "A memorial to Canadian soldiers who died on American soil"
    ],
    "answerIndex": 1,
    "explanation": "At Blaine in the State of Washington, the Peace Arch is inscribed with the words 'children of a common mother' and 'brethren dwelling together in unity.' It symbolizes the close ties and common interests between Canada and the United States, who share what is traditionally known as 'the world's longest undefended border.'"
  },
  {
    "id": "q492",
    "topic": "Canada's Economy",
    "subtopic": "Economic Overview",
    "question": "What does Canada export to the United States each year?",
    "options": [
      "Primarily manufactured goods and automobiles only",
      "Energy products, industrial goods, machinery, equipment, automotive, agricultural, fishing and forestry products, and consumer goods",
      "Mainly raw commodities such as wheat, fish, and timber",
      "Only high-technology products and services"
    ],
    "answerIndex": 1,
    "explanation": "Canada exports billions of dollars worth of energy products, industrial goods, machinery, equipment, automotive, agricultural, fishing and forestry products, and consumer goods to the United States every year. This reflects the enormous diversity and depth of the Canada-US economic relationship."
  },
  {
    "id": "q493",
    "topic": "Canada's Economy",
    "subtopic": "Free Trade",
    "question": "What is NAFTA and when did Mexico join Canada and the US in this agreement?",
    "options": [
      "The Northern Atlantic Free Trade Association; formed in 1988 with Mexico",
      "The North American Free Trade Agreement; Mexico became a partner in 1994",
      "The National Association for Trade Agreements; Mexico joined in 1990",
      "The North American Financial Treaty Agreement; formed in 2000"
    ],
    "answerIndex": 1,
    "explanation": "NAFTA stands for the North American Free Trade Agreement. Mexico became a partner in 1994 in this agreement, expanding the original 1988 Canada-US free trade deal into a three-country trading block. NAFTA created a market of over 444 million people with over $1 trillion in merchandise trade."
  },
  {
    "id": "q494",
    "topic": "Canada's Economy",
    "subtopic": "Agriculture",
    "question": "What role do natural resources play in Canada's economic history?",
    "options": [
      "They have always been unimportant compared to manufacturing",
      "They formed the basis of Canada's economy for centuries, including fur, fish and timber, and continue to be a large part of Canada's exports",
      "They only became important after Confederation in 1867",
      "They are important only in Western Canada"
    ],
    "answerIndex": 1,
    "explanation": "For centuries, Canada's economy was based mainly on farming and on exporting natural resources such as fur, fish and timber. Today, natural resource industries (forestry, fishing, agriculture, mining and energy) remain crucial to many regions of Canada, and a large percentage of Canada's exports are natural resource commodities."
  },
  {
    "id": "q495",
    "topic": "Canada's Economy",
    "subtopic": "Financial Institutions",
    "question": "When did the Montreal Stock Exchange open, marking an early step in Canada's financial development?",
    "options": [
      "1792",
      "1812",
      "1832",
      "1867"
    ],
    "answerIndex": 2,
    "explanation": "The Montreal Stock Exchange opened in 1832, making it one of Canada's earliest financial institutions. The first financial institutions opened in the late 18th and early 19th centuries, reflecting Canada's growing commercial economy that would eventually support Confederation and westward expansion."
  },
  {
    "id": "q496",
    "topic": "Canada's Economy",
    "subtopic": "Economic Overview",
    "question": "What is the traditional description of the Canada-US border?",
    "options": [
      "The world's most secure border",
      "The world's longest international border",
      "The world's longest undefended border",
      "The world's busiest border crossing"
    ],
    "answerIndex": 2,
    "explanation": "The Canada-US border is traditionally known as 'the world's longest undefended border.' Millions of Canadians and Americans cross it every year safely. Both countries are committed to a safe, secure and efficient frontier, reflecting their long partnership and shared values."
  },
  {
    "id": "q497",
    "topic": "Canada's Economy",
    "subtopic": "Economic Sectors",
    "question": "What is an example of a service industry in Canada?",
    "options": [
      "Oil extraction in Alberta",
      "Car manufacturing in Ontario",
      "Banking, health care, education, or retail",
      "Wheat farming in Saskatchewan"
    ],
    "answerIndex": 2,
    "explanation": "Service industries include transportation, education, health care, construction, banking, communications, retail services, tourism and government — sectors where workers provide services rather than physical products. More than 75% of working Canadians now work in service industries, making it Canada's dominant economic sector."
  },
  {
    "id": "q498",
    "topic": "Canada's Economy",
    "subtopic": "Economic Overview",
    "question": "Where does Canada rank among the world's economies and which international body does it belong to?",
    "options": [
      "One of the 25 largest economies; member of the G20 only",
      "One of the 5 largest economies; founding member of the UN Security Council",
      "One of the 10 largest economies in the world; part of the G8 group of leading industrialized nations",
      "One of the 15 largest economies; member of the G20 only"
    ],
    "answerIndex": 2,
    "explanation": "Today, Canada has one of the ten largest economies in the world and is part of the G8 group of leading industrialized countries (with the United States, Germany, the United Kingdom, Italy, France, Japan and Russia). Canadians enjoy one of the world's highest standards of living."
  },

  # ─────────────────────────────────────────────────────────────────────────────
  # CANADA'S REGIONS  (38 → +12 = 50)
  # ─────────────────────────────────────────────────────────────────────────────
  {
    "id": "q499",
    "topic": "Canada's Regions",
    "subtopic": "Geography",
    "question": "What are the five distinct geographical regions of Canada?",
    "options": [
      "Eastern Canada, Central Canada, Western Canada, Northern Canada, and the Pacific",
      "The Atlantic Provinces, Central Canada, the Prairie Provinces, the West Coast, and the Northern Territories",
      "Quebec, Ontario, the Prairies, BC, and the North",
      "The Maritimes, the St. Lawrence, the Great Plains, the Rocky Mountains, and the Arctic"
    ],
    "answerIndex": 1,
    "explanation": "Canada includes five distinct geographical regions: The Atlantic Provinces, Central Canada, the Prairie Provinces, the West Coast, and the Northern Territories. Each region has its own distinctive geography, climate, culture, and economic activities."
  },
  {
    "id": "q500",
    "topic": "Canada's Regions",
    "subtopic": "Capital",
    "question": "When was Ottawa chosen as Canada's capital and by whom?",
    "options": [
      "1867, by the Fathers of Confederation",
      "1857, by Queen Victoria",
      "1840, by Lord Durham",
      "1867, by Parliament's first vote"
    ],
    "answerIndex": 1,
    "explanation": "Ottawa, located on the Ottawa River, was chosen as the capital in 1857 by Queen Victoria. Today Ottawa is Canada's fourth largest metropolitan area. The National Capital Region of 4,700 square kilometres preserves and enhances the area's built heritage and natural environment."
  },
  {
    "id": "q501",
    "topic": "Canada's Regions",
    "subtopic": "Atlantic Canada",
    "question": "What connects Prince Edward Island to mainland Canada?",
    "options": [
      "The Trans-Canada Highway tunnel",
      "A ferry service that has run since 1873",
      "The Confederation Bridge, one of the longest continuous multispan bridges in the world",
      "The Northumberland Strait railway bridge"
    ],
    "answerIndex": 2,
    "explanation": "Prince Edward Island is connected to mainland Canada by the Confederation Bridge, one of the longest continuous multispan bridges in the world. P.E.I. is the smallest province, known for its beaches, red soil and agriculture, especially potatoes, and is the birthplace of Confederation."
  },
  {
    "id": "q502",
    "topic": "Canada's Regions",
    "subtopic": "Atlantic Canada",
    "question": "What classic Canadian children's novel is set in Prince Edward Island?",
    "options": [
      "The Stone Angel, set in Manitoba",
      "Who Has Seen the Wind, set in Saskatchewan",
      "Anne of Green Gables by Lucy Maud Montgomery, about a red-headed orphan girl",
      "The Apprenticeship of Duddy Kravitz, set in Quebec"
    ],
    "answerIndex": 2,
    "explanation": "Anne of Green Gables, written by Lucy Maud Montgomery, is set in Prince Edward Island. It is a much-loved story about the adventures of a little red-headed orphan girl named Anne. The novel has made PEI famous around the world and attracts many tourists to the province."
  },
  {
    "id": "q503",
    "topic": "Canada's Regions",
    "subtopic": "Prairie Provinces",
    "question": "What is the most famous street intersection in Canada and where is it located?",
    "options": [
      "Yonge and Bloor, in Toronto, Ontario",
      "Granville and Georgia, in Vancouver, British Columbia",
      "Portage and Main, in Winnipeg, Manitoba",
      "St. Catherine and Peel, in Montreal, Quebec"
    ],
    "answerIndex": 2,
    "explanation": "Portage and Main in Winnipeg's Exchange District is the most famous street intersection in Canada. Winnipeg is Manitoba's most populous city. Manitoba's French Quarter, St. Boniface, has Western Canada's largest Francophone community at 45,000 residents."
  },
  {
    "id": "q504",
    "topic": "Canada's Regions",
    "subtopic": "Ontario and Quebec",
    "question": "Which body of water is the largest freshwater lake in the world?",
    "options": [
      "Lake Ontario",
      "Lake Huron",
      "Lake Erie",
      "Lake Superior"
    ],
    "answerIndex": 3,
    "explanation": "Lake Superior is the largest freshwater lake in the world. There are five Great Lakes located between Ontario and the United States: Lake Ontario, Lake Erie, Lake Huron, Lake Michigan (entirely in the U.S.A.) and Lake Superior. More than half of Canadians live in the Great Lakes and St. Lawrence River region."
  },
  {
    "id": "q505",
    "topic": "Canada's Regions",
    "subtopic": "North",
    "question": "What does 'Nunavut' mean in Inuktitut, and when was it established as a territory?",
    "options": [
      "'Our land' — established in 1999",
      "'The people' — established in 1982",
      "'Land of snow' — established in 1993",
      "'Northern home' — established in 2005"
    ],
    "answerIndex": 0,
    "explanation": "Nunavut means 'our land' in Inuktitut and was established in 1999 from the eastern part of the Northwest Territories. The capital is Iqaluit (formerly Frobisher Bay). The population is about 85% Inuit, and Inuktitut is an official language and the first language in schools."
  },
  {
    "id": "q506",
    "topic": "Canada's Regions",
    "subtopic": "North",
    "question": "What is Mount Logan and why is it significant?",
    "options": [
      "The second-highest mountain in North America, located in BC",
      "The highest mountain in Canada, located in the Yukon, named after geologist Sir William Logan",
      "A famous ski resort in the Rocky Mountains of Alberta",
      "A historical landmark near the site of the Yukon Gold Rush"
    ],
    "answerIndex": 1,
    "explanation": "Mount Logan, located in the Yukon, is the highest mountain in Canada. It is named in honour of Sir William Logan, a world-famous geologist born in Montreal in 1798. Logan founded and directed the Geological Survey of Canada from 1842 to 1869 and is considered one of Canada's greatest scientists."
  },
  {
    "id": "q507",
    "topic": "Canada's Regions",
    "subtopic": "North",
    "question": "What is the 'Land of the Midnight Sun' and which part of Canada does it describe?",
    "options": [
      "The prairies in summer, where the sun sets very late",
      "The Northern Territories, where at the height of summer daylight can last up to 24 hours",
      "Newfoundland, which has the earliest sunrises in Canada",
      "British Columbia, which has the longest summer days on the Pacific coast"
    ],
    "answerIndex": 1,
    "explanation": "The North is often referred to as the 'Land of the Midnight Sun' because at the height of summer, daylight can last up to 24 hours. In winter, the sun disappears and darkness sets in for three months. The Northern Territories contain one-third of Canada's land mass but only about 100,000 people."
  },
  {
    "id": "q508",
    "topic": "Canada's Regions",
    "subtopic": "Pacific Region",
    "question": "What is the most valuable industry in British Columbia?",
    "options": [
      "Mining",
      "Fishing",
      "Forestry — about one-half of all goods produced in BC are forestry products",
      "Tourism"
    ],
    "answerIndex": 2,
    "explanation": "About one-half of all the goods produced in British Columbia are forestry products, including lumber, newsprint, and pulp and paper products — making it the most valuable forestry industry in Canada. BC is also known for mining, fishing, and the fruit orchards and wine industry of the Okanagan Valley."
  },
  {
    "id": "q509",
    "topic": "Canada's Regions",
    "subtopic": "Prairie Provinces",
    "question": "What is Saskatchewan known as and why?",
    "options": [
      "'The Wild Rose Country' because of its vast wildflower meadows",
      "'The Breadbasket of the World' — it has 40% of the arable land in Canada and is the largest producer of grains and oilseeds",
      "'The Petroleum Province' because of its vast oil reserves",
      "'The Land of Living Skies' solely because of its wide flat prairies"
    ],
    "answerIndex": 1,
    "explanation": "Saskatchewan was once known as the 'breadbasket of the world' and the 'wheat province.' It has 40% of the arable land in Canada and is the country's largest producer of grains and oilseeds. Saskatchewan also has the world's richest deposits of uranium and potash and produces oil and natural gas."
  },
  {
    "id": "q510",
    "topic": "Canada's Regions",
    "subtopic": "Ontario and Quebec",
    "question": "What fraction of all Canadian manufactured goods do Ontario and Quebec together produce?",
    "options": [
      "About one-quarter",
      "About one-half",
      "More than three-quarters",
      "About two-thirds"
    ],
    "answerIndex": 2,
    "explanation": "Together, Ontario and Quebec produce more than three-quarters of all Canadian manufactured goods. Central Canada is described as 'the industrial and manufacturing heartland' of Canada. More than half of all Canadians live in cities and towns near the Great Lakes and the St. Lawrence River in this region."
  }
]

def main():
    with open('src/assets/data/questions.json', 'r') as f:
        questions = json.load(f)

    existing_ids = {q['id'] for q in questions}
    added = 0
    skipped = 0

    for q in NEW_QUESTIONS:
        if q['id'] in existing_ids:
            print(f"  SKIP (already exists): {q['id']}")
            skipped += 1
        else:
            questions.append(q)
            existing_ids.add(q['id'])
            added += 1

    with open('src/assets/data/questions.json', 'w') as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)

    print(f"\nDone! Added {added} questions, skipped {skipped}.")
    print(f"Total questions: {len(questions)}")

    # Print topic breakdown
    from collections import Counter
    counts = Counter(q['topic'] for q in questions)
    print("\nTopic breakdown:")
    for topic, count in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"  {count:3d}  {topic}")

if __name__ == '__main__':
    main()
