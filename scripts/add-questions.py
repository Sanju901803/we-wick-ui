#!/usr/bin/env python3
"""
Script to append new citizenship exam questions to questions.json.
Covers all 12 topics from the Discover Canada guide.
"""
import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), '../src/assets/data/questions.json')

NEW_QUESTIONS = [
  # ─── APPLYING FOR CITIZENSHIP ───────────────────────────────────────────────
  {
    "id": "q041",
    "topic": "Applying for Citizenship",
    "subtopic": "Requirements",
    "question": "How many days out of 5 years must a permanent resident live in Canada before applying for citizenship?",
    "options": [
      "730 days (2 years)",
      "1,095 days (3 years)",
      "1,460 days (4 years)",
      "1,825 days (5 years)"
    ],
    "answerIndex": 1,
    "explanation": "An adult permanent resident must have lived in Canada for at least 1,095 days (3 years) within the 5 years before applying for citizenship."
  },
  {
    "id": "q042",
    "topic": "Applying for Citizenship",
    "subtopic": "Requirements",
    "question": "Which age group is required to take the citizenship knowledge test?",
    "options": [
      "Under 18 only",
      "18 to 54 years old",
      "18 to 64 years old",
      "All applicants regardless of age"
    ],
    "answerIndex": 1,
    "explanation": "Applicants between the ages of 18 and 54 must take the citizenship knowledge test. Those under 18 and those 55 and over are exempt from the test."
  },
  {
    "id": "q043",
    "topic": "Applying for Citizenship",
    "subtopic": "Requirements",
    "question": "What language requirement must adult citizenship applicants (18–54) meet?",
    "options": [
      "Must speak both English and French fluently",
      "Must demonstrate adequate knowledge of English or French",
      "No language requirement exists",
      "Must pass an advanced academic language exam"
    ],
    "answerIndex": 1,
    "explanation": "Adult applicants aged 18–54 must demonstrate adequate knowledge of English or French to become Canadian citizens."
  },
  {
    "id": "q044",
    "topic": "Applying for Citizenship",
    "subtopic": "Requirements",
    "question": "Which of the following is NOT a requirement to apply for Canadian citizenship as an adult?",
    "options": [
      "Being a permanent resident",
      "Having lived in Canada for 3 of the past 5 years",
      "Having been born in a Commonwealth country",
      "Demonstrating knowledge of English or French"
    ],
    "answerIndex": 2,
    "explanation": "Being born in a Commonwealth country is not a requirement. The main requirements are: permanent resident status, meeting the residency requirement (1,095 days in 5 years), language ability, and passing the citizenship knowledge test (for ages 18–54)."
  },
  {
    "id": "q045",
    "topic": "Applying for Citizenship",
    "subtopic": "Process",
    "question": "What is a citizenship ceremony?",
    "options": [
      "A test of English or French skills",
      "A formal event where permanent residents receive their PR cards",
      "A formal event where applicants take the Oath of Citizenship and become Canadian citizens",
      "A government interview to check residency history"
    ],
    "answerIndex": 2,
    "explanation": "A citizenship ceremony is the formal event where approved applicants take the Oath of Citizenship and officially become Canadian citizens."
  },
  {
    "id": "q046",
    "topic": "Applying for Citizenship",
    "subtopic": "Process",
    "question": "What document is given to a person who becomes a Canadian citizen?",
    "options": [
      "A permanent resident card",
      "A citizenship certificate",
      "A Canadian passport",
      "A landed immigrant certificate"
    ],
    "answerIndex": 1,
    "explanation": "After taking the Oath of Citizenship at a citizenship ceremony, a new citizen receives a citizenship certificate as proof of their Canadian citizenship."
  },
  {
    "id": "q047",
    "topic": "Applying for Citizenship",
    "subtopic": "Rights of Citizens",
    "question": "Which right is available to Canadian citizens but NOT to permanent residents?",
    "options": [
      "The right to live and work in Canada",
      "The right to publicly funded health care",
      "The right to vote in federal elections and run for elected office",
      "The right to send children to publicly funded schools"
    ],
    "answerIndex": 2,
    "explanation": "Only Canadian citizens have the right to vote in federal, provincial, and territorial elections and to run for elected office. Permanent residents have many rights but cannot vote or hold most elected offices."
  },
  {
    "id": "q048",
    "topic": "Applying for Citizenship",
    "subtopic": "Requirements",
    "question": "If a permanent resident is required to file income taxes, what must they have done to be eligible for citizenship?",
    "options": [
      "Filed taxes in all 5 years prior to applying",
      "Filed taxes in at least 3 of the 5 years before applying",
      "Never owed taxes",
      "Paid taxes in the year they apply only"
    ],
    "answerIndex": 1,
    "explanation": "To be eligible for citizenship, applicants must have filed income taxes, if required to do so under the Income Tax Act, in at least 3 of the 5 years before applying."
  },

  # ─── OATH OF CITIZENSHIP ────────────────────────────────────────────────────
  {
    "id": "q049",
    "topic": "Oath of Citizenship",
    "subtopic": "The Oath",
    "question": "To whom do new Canadians pledge allegiance in the Oath of Citizenship?",
    "options": [
      "The Prime Minister of Canada",
      "The people of Canada and the Constitution",
      "His/Her Majesty the King (or Queen), and his/her heirs and successors",
      "The Governor General of Canada"
    ],
    "answerIndex": 2,
    "explanation": "In the Oath of Citizenship, new Canadians pledge allegiance to His/Her Majesty the King (or Queen), and his/her heirs and successors, and swear to faithfully observe Canada's laws and fulfil the duties of a Canadian citizen."
  },
  {
    "id": "q050",
    "topic": "Oath of Citizenship",
    "subtopic": "The Oath",
    "question": "What do new citizens promise in the Oath of Citizenship?",
    "options": [
      "To renounce all other citizenships immediately",
      "To faithfully observe the laws of Canada and fulfil their duties as Canadian citizens",
      "To serve in the Canadian Armed Forces",
      "To learn both English and French within 5 years"
    ],
    "answerIndex": 1,
    "explanation": "In the Oath of Citizenship, new Canadians promise to faithfully observe the laws of Canada and fulfil their duties as Canadian citizens — a commitment to Canada's values and democratic principles."
  },
  {
    "id": "q051",
    "topic": "Oath of Citizenship",
    "subtopic": "Significance",
    "question": "Why is the Oath of Citizenship important?",
    "options": [
      "It is a legal requirement to receive a Canadian passport",
      "It marks the moment a person officially becomes a Canadian citizen and accepts the responsibilities of citizenship",
      "It is required to apply for a permanent resident card",
      "It exempts new citizens from income taxes for 5 years"
    ],
    "answerIndex": 1,
    "explanation": "The Oath of Citizenship is the final step in the citizenship process. By taking the Oath at a citizenship ceremony, a person officially becomes a Canadian citizen and commits to Canada's laws and values."
  },
  {
    "id": "q052",
    "topic": "Oath of Citizenship",
    "subtopic": "Ceremony",
    "question": "In how many languages is the Oath of Citizenship administered at a ceremony?",
    "options": [
      "One — in the applicant's preferred language",
      "Two — in English and French",
      "Three — in English, French, and the applicant's native language",
      "It is written, not spoken"
    ],
    "answerIndex": 1,
    "explanation": "The Oath of Citizenship is administered in both of Canada's official languages — English and French — at a citizenship ceremony."
  },
  {
    "id": "q053",
    "topic": "Oath of Citizenship",
    "subtopic": "Duties",
    "question": "Which of the following is a duty that new citizens commit to when they take the Oath?",
    "options": [
      "Serving in the military for at least 2 years",
      "Living in Canada permanently without ever leaving",
      "Obeying the laws of Canada",
      "Working for the federal government"
    ],
    "answerIndex": 2,
    "explanation": "By taking the Oath of Citizenship, new citizens commit to obeying Canada's laws. Military service is voluntary, not mandatory."
  },

  # ─── MODERN CANADA ──────────────────────────────────────────────────────────
  {
    "id": "q054",
    "topic": "Modern Canada",
    "subtopic": "Health Care",
    "question": "What is the name of Canada's publicly funded universal health care system?",
    "options": [
      "The National Health Service (NHS)",
      "Medicare",
      "HealthFirst Canada",
      "The Canada Care Act"
    ],
    "answerIndex": 1,
    "explanation": "Canada's publicly funded universal health care system is commonly called Medicare. It ensures that all Canadian residents have access to medically necessary hospital and physician services."
  },
  {
    "id": "q055",
    "topic": "Modern Canada",
    "subtopic": "International Organizations",
    "question": "Canada is a founding member of which military alliance formed in 1949?",
    "options": [
      "ASEAN",
      "The Warsaw Pact",
      "NATO (North Atlantic Treaty Organization)",
      "SEATO"
    ],
    "answerIndex": 2,
    "explanation": "Canada was a founding member of NATO (the North Atlantic Treaty Organization) in 1949. NATO is a military alliance committed to collective defence among member nations."
  },
  {
    "id": "q056",
    "topic": "Modern Canada",
    "subtopic": "International Organizations",
    "question": "Canada is a member of the G8. What is the G8?",
    "options": [
      "A group of 8 countries with nuclear weapons",
      "A group of 8 of the world's leading industrialized nations",
      "An 8-country military alliance",
      "A group of 8 countries in the Americas"
    ],
    "answerIndex": 1,
    "explanation": "The G8 (Group of Eight) is a forum of eight of the world's leading industrialized nations, including Canada. These nations meet to discuss major global economic and political issues."
  },
  {
    "id": "q057",
    "topic": "Modern Canada",
    "subtopic": "Demographics",
    "question": "Approximately how many people live in Canada?",
    "options": [
      "10 million",
      "20 million",
      "34 million",
      "50 million"
    ],
    "answerIndex": 2,
    "explanation": "Canada's population is approximately 34 million people (at the time of the Discover Canada study guide), making it one of the world's largest countries by area but relatively small by population."
  },
  {
    "id": "q058",
    "topic": "Modern Canada",
    "subtopic": "Society",
    "question": "What is Canada's policy toward newcomers and different cultures?",
    "options": [
      "Assimilation — newcomers must fully adopt Canadian culture",
      "Multiculturalism — Canada values and welcomes diversity",
      "Segregation — different cultures are kept separate",
      "Restriction — immigration is limited to specific countries"
    ],
    "answerIndex": 1,
    "explanation": "Canada has an official policy of multiculturalism, which means Canada values the diversity of its people and encourages citizens to keep their cultural heritage while adopting Canadian values and laws."
  },
  {
    "id": "q059",
    "topic": "Modern Canada",
    "subtopic": "Society",
    "question": "What percentage of Canadians live within 300 km (200 miles) of the US border?",
    "options": [
      "About 25%",
      "About 50%",
      "About 75%",
      "About 90%"
    ],
    "answerIndex": 3,
    "explanation": "About 90% of Canadians live within 300 km (200 miles) of the US border, largely because southern Canada has the most moderate climate, fertile land, and concentrated economic activity."
  },
  {
    "id": "q060",
    "topic": "Modern Canada",
    "subtopic": "Immigration",
    "question": "Why is immigration important to Canada today?",
    "options": [
      "It is not important — Canada restricts all immigration",
      "Immigration helps Canada's economy grow and addresses an aging population",
      "Immigrants are required to join the military",
      "Immigration only benefits Quebec"
    ],
    "answerIndex": 1,
    "explanation": "Immigration is vital to Canada's future as it supports economic growth, fills labour shortages, and helps address the challenges of an aging population. Canada welcomes people from all over the world."
  },
  {
    "id": "q061",
    "topic": "Modern Canada",
    "subtopic": "Broadcasting",
    "question": "What is the name of Canada's national public broadcaster?",
    "options": [
      "CTV",
      "Global TV",
      "The Canadian Broadcasting Corporation (CBC/Radio-Canada)",
      "TVA"
    ],
    "answerIndex": 2,
    "explanation": "The Canadian Broadcasting Corporation (CBC) in English and Radio-Canada in French is Canada's national public broadcaster, providing television and radio services across the country."
  },

  # ─── FEDERAL ELECTIONS ──────────────────────────────────────────────────────
  {
    "id": "q062",
    "topic": "Federal Elections",
    "subtopic": "Voting System",
    "question": "What voting system is used in Canadian federal elections?",
    "options": [
      "Proportional representation",
      "Ranked ballot voting",
      "First past the post — the candidate with the most votes in a riding wins",
      "Two-round runoff system"
    ],
    "answerIndex": 2,
    "explanation": "Canada uses a 'first past the post' voting system. In each riding, the candidate who receives the most votes wins the seat in the House of Commons, even if they receive less than 50% of votes."
  },
  {
    "id": "q063",
    "topic": "Federal Elections",
    "subtopic": "Electoral Districts",
    "question": "What is a federal electoral district in Canada called?",
    "options": [
      "A borough",
      "A county",
      "A ward",
      "A riding or constituency"
    ],
    "answerIndex": 3,
    "explanation": "A federal electoral district is called a riding or constituency. Each riding elects one Member of Parliament (MP) to represent it in the House of Commons."
  },
  {
    "id": "q064",
    "topic": "Federal Elections",
    "subtopic": "Elections Canada",
    "question": "What is Elections Canada?",
    "options": [
      "The party that wins the most seats in a federal election",
      "An independent, non-partisan agency responsible for administering federal elections",
      "A government ministry that manages political advertising",
      "The Prime Minister's campaign organization"
    ],
    "answerIndex": 1,
    "explanation": "Elections Canada is an independent, non-partisan agency of the Canadian Parliament that is responsible for administering federal elections and referendums, and maintaining the National Register of Electors."
  },
  {
    "id": "q065",
    "topic": "Federal Elections",
    "subtopic": "Voter Registration",
    "question": "What is the National Register of Electors?",
    "options": [
      "A list of all Canadian permanent residents",
      "A database of all political party members",
      "A permanent database of eligible Canadian voters maintained by Elections Canada",
      "A record of all federal election results"
    ],
    "answerIndex": 2,
    "explanation": "The National Register of Electors is a permanent database of Canadians who are eligible to vote, maintained by Elections Canada. It is used to produce voter lists for federal elections and referendums."
  },
  {
    "id": "q066",
    "topic": "Federal Elections",
    "subtopic": "Voting",
    "question": "What are the three ways eligible voters can cast their ballot in a federal election?",
    "options": [
      "In person, by mail, or online",
      "On Election Day, at advance polls, or by special ballot",
      "At a polling station, a government office, or a school",
      "Early voting, Election Day, and runoff voting"
    ],
    "answerIndex": 1,
    "explanation": "Eligible voters can vote on Election Day at their assigned polling station, at advance polls held before Election Day, or by special ballot (by mail or at an Elections Canada office)."
  },
  {
    "id": "q067",
    "topic": "Federal Elections",
    "subtopic": "Minority Government",
    "question": "What is a minority government in Canada?",
    "options": [
      "A government formed by parties representing visible minorities",
      "A government where the ruling party has fewer than half the seats in the House of Commons",
      "A government that has lost a confidence vote",
      "A government with fewer than 100 seats"
    ],
    "answerIndex": 1,
    "explanation": "A minority government is formed when the governing party holds fewer than half (less than 50%) of the seats in the House of Commons. The government must work with other parties to pass legislation."
  },
  {
    "id": "q068",
    "topic": "Federal Elections",
    "subtopic": "Official Opposition",
    "question": "What is the Official Opposition in the House of Commons?",
    "options": [
      "All parties that voted against the government on the last confidence vote",
      "The party with the fewest seats in the House of Commons",
      "The party with the second-largest number of seats, led by the Leader of the Opposition",
      "The Senate, which opposes bills from the House of Commons"
    ],
    "answerIndex": 2,
    "explanation": "The Official Opposition is the party with the second-largest number of seats in the House of Commons. Its leader is called the Leader of the Official Opposition, and the party's role is to hold the government accountable."
  },
  {
    "id": "q069",
    "topic": "Federal Elections",
    "subtopic": "By-Elections",
    "question": "What is a by-election?",
    "options": [
      "A provincial election held in the same year as a federal election",
      "An election held between general elections to fill a vacant seat in the House of Commons",
      "A special election for the Senate",
      "An election to choose the Governor General"
    ],
    "answerIndex": 1,
    "explanation": "A by-election is an election held in a single riding to fill a seat that has become vacant between general elections, due to the death, resignation, or disqualification of an MP."
  },
  {
    "id": "q070",
    "topic": "Federal Elections",
    "subtopic": "Campaign",
    "question": "On whose advice does the Governor General dissolve Parliament to call a federal election?",
    "options": [
      "The Speaker of the House of Commons",
      "The Chief Justice of Canada",
      "The Prime Minister",
      "The Leader of the Official Opposition"
    ],
    "answerIndex": 2,
    "explanation": "The Governor General dissolves Parliament and calls a general election on the advice of the Prime Minister. Under the fixed election date law, elections are normally held every four years."
  },
  {
    "id": "q071",
    "topic": "Federal Elections",
    "subtopic": "Political Parties",
    "question": "Which of the following is one of Canada's main federal political parties?",
    "options": [
      "The Canadian Alliance",
      "The Democratic Party",
      "The New Democratic Party (NDP)",
      "The Republican Party"
    ],
    "answerIndex": 2,
    "explanation": "The New Democratic Party (NDP) is one of Canada's main federal political parties. The other major parties are the Liberal Party and the Conservative Party of Canada."
  },

  # ─── THE JUSTICE SYSTEM ─────────────────────────────────────────────────────
  {
    "id": "q072",
    "topic": "The Justice System",
    "subtopic": "Courts",
    "question": "What is the highest court in Canada?",
    "options": [
      "The Federal Court of Canada",
      "The Ontario Court of Appeal",
      "The Supreme Court of Canada",
      "The Court of Queen's Bench"
    ],
    "answerIndex": 2,
    "explanation": "The Supreme Court of Canada is the highest court in the country. It is the final court of appeal for all legal matters and its decisions are binding on all other courts in Canada."
  },
  {
    "id": "q073",
    "topic": "The Justice System",
    "subtopic": "Rights of the Accused",
    "question": "What is the principle of 'presumption of innocence' in Canadian law?",
    "options": [
      "A person is considered guilty until proven innocent",
      "Police can detain anyone they consider suspicious",
      "A person is considered innocent until proven guilty in a court of law",
      "Judges determine guilt before a trial begins"
    ],
    "answerIndex": 2,
    "explanation": "The principle of presumption of innocence means that every person charged with a crime is considered innocent until the Crown (prosecution) proves guilt beyond a reasonable doubt in a court of law."
  },
  {
    "id": "q074",
    "topic": "The Justice System",
    "subtopic": "Rights of the Accused",
    "question": "What is habeas corpus?",
    "options": [
      "The right to remain silent when questioned by police",
      "The right to know the reasons for your arrest and to have a court hearing",
      "The right to a jury trial for all offences",
      "The right to appeal any court decision"
    ],
    "answerIndex": 1,
    "explanation": "Habeas corpus is the right to challenge unlawful detention — the right to know why you have been arrested and to have a court decide whether your detention is lawful. It comes from English common law."
  },
  {
    "id": "q075",
    "topic": "The Justice System",
    "subtopic": "Police",
    "question": "Which police force is responsible for national and federal policing across Canada?",
    "options": [
      "The Ontario Provincial Police (OPP)",
      "The Royal Canadian Mounted Police (RCMP)",
      "The Canadian Security Intelligence Service (CSIS)",
      "The Canadian Border Services Agency (CBSA)"
    ],
    "answerIndex": 1,
    "explanation": "The Royal Canadian Mounted Police (RCMP) is Canada's national police force. It enforces federal law across Canada and provides provincial policing services in all provinces and territories except Ontario and Quebec."
  },
  {
    "id": "q076",
    "topic": "The Justice System",
    "subtopic": "Police",
    "question": "Which two provinces have their own provincial police forces (in addition to the RCMP)?",
    "options": [
      "Alberta and British Columbia",
      "Manitoba and Saskatchewan",
      "Ontario and Quebec",
      "Nova Scotia and New Brunswick"
    ],
    "answerIndex": 2,
    "explanation": "Ontario has the Ontario Provincial Police (OPP) and Quebec has the Sûreté du Québec (SQ). All other provinces use the RCMP for provincial policing. Municipalities may also have their own city police forces."
  },
  {
    "id": "q077",
    "topic": "The Justice System",
    "subtopic": "Rights of the Accused",
    "question": "What does the right to legal counsel mean in Canada?",
    "options": [
      "The government must provide every citizen with a free lawyer",
      "Only wealthy Canadians can afford legal representation",
      "A person charged with a crime has the right to be represented by a lawyer",
      "Legal advice is only available for civil, not criminal cases"
    ],
    "answerIndex": 2,
    "explanation": "Under the Canadian Charter of Rights and Freedoms, everyone has the right to retain and instruct a lawyer without delay when arrested or detained. Legal aid programs exist to help those who cannot afford a lawyer."
  },
  {
    "id": "q078",
    "topic": "The Justice System",
    "subtopic": "Courts",
    "question": "Which court handles matters involving federal government laws and regulations?",
    "options": [
      "The Supreme Court of Canada",
      "The Federal Court of Canada",
      "Provincial Superior Courts",
      "Small Claims Court"
    ],
    "answerIndex": 1,
    "explanation": "The Federal Court of Canada deals with matters involving federal government laws, including immigration and refugee issues, intellectual property, federal administrative law, and national security matters."
  },
  {
    "id": "q079",
    "topic": "The Justice System",
    "subtopic": "Rights",
    "question": "What does the Canadian legal system protect citizens from?",
    "options": [
      "Having to pay taxes",
      "Living in poverty",
      "Arbitrary arrest, unlawful detention, and abuse of power by the government",
      "Being criticized in public"
    ],
    "answerIndex": 2,
    "explanation": "The Canadian legal system — including the Charter of Rights and Freedoms and the rule of law — protects individuals from arbitrary arrest, unlawful detention, and abuse of power by those in authority."
  },

  # ─── CANADIAN SYMBOLS ───────────────────────────────────────────────────────
  {
    "id": "q080",
    "topic": "Canadian Symbols",
    "subtopic": "Flag",
    "question": "When was the current Canadian flag (with the maple leaf) first raised?",
    "options": [
      "July 1, 1867",
      "November 11, 1918",
      "February 15, 1965",
      "April 17, 1982"
    ],
    "answerIndex": 2,
    "explanation": "The distinctive red and white Maple Leaf Flag was first raised on February 15, 1965, replacing the Canadian Red Ensign. Red and white have been Canada's national colours since 1921."
  },
  {
    "id": "q081",
    "topic": "Canadian Symbols",
    "subtopic": "Coat of Arms",
    "question": "What is the motto on Canada's Coat of Arms?",
    "options": [
      "In God We Trust",
      "Peace, Order and Good Government",
      "A Mari Usque Ad Mare",
      "Unity, Strength, Canada"
    ],
    "answerIndex": 2,
    "explanation": "'A Mari Usque Ad Mare' is Canada's motto, a Latin phrase meaning 'From Sea to Sea.' It reflects Canada's vast geography stretching from the Atlantic Ocean to the Pacific Ocean."
  },
  {
    "id": "q082",
    "topic": "Canadian Symbols",
    "subtopic": "Sports",
    "question": "What is Canada's official national winter sport?",
    "options": [
      "Curling",
      "Skiing",
      "Speed skating",
      "Ice hockey"
    ],
    "answerIndex": 3,
    "explanation": "Ice hockey is Canada's official national winter sport, deeply embedded in Canadian culture. The NHL plays for the Stanley Cup, which was donated in 1892 by Governor General Lord Stanley."
  },
  {
    "id": "q083",
    "topic": "Canadian Symbols",
    "subtopic": "Sports",
    "question": "What is Canada's official national summer sport?",
    "options": [
      "Soccer",
      "Baseball",
      "Lacrosse",
      "Tennis"
    ],
    "answerIndex": 2,
    "explanation": "Lacrosse is Canada's official national summer sport. It was originally played by Aboriginal peoples long before European contact and is one of the oldest team sports in North America."
  },
  {
    "id": "q084",
    "topic": "Canadian Symbols",
    "subtopic": "Symbols",
    "question": "What image is on the Canadian five-cent coin (nickel)?",
    "options": [
      "A maple leaf",
      "A loon",
      "A caribou",
      "A beaver"
    ],
    "answerIndex": 3,
    "explanation": "The beaver is depicted on the Canadian five-cent coin (nickel). The beaver is an official symbol of Canada — it was central to the early fur trade and appears on the badge of the Hudson's Bay Company."
  },
  {
    "id": "q085",
    "topic": "Canadian Symbols",
    "subtopic": "Anthem",
    "question": "When was 'O Canada' officially proclaimed as Canada's national anthem?",
    "options": [
      "July 1, 1867",
      "February 15, 1965",
      "July 1, 1980",
      "April 17, 1982"
    ],
    "answerIndex": 2,
    "explanation": "'O Canada' was officially proclaimed Canada's national anthem on July 1, 1980. The song was first performed in Quebec City on June 24, 1880, more than a century before it became the official anthem."
  },
  {
    "id": "q086",
    "topic": "Canadian Symbols",
    "subtopic": "Honours",
    "question": "What is the Order of Canada?",
    "options": [
      "Canada's highest military honour for bravery in battle",
      "A civilian honour recognizing outstanding achievement and service to Canada",
      "An award given to new immigrants",
      "A medal given to long-serving civil servants"
    ],
    "answerIndex": 1,
    "explanation": "The Order of Canada, established in 1967, is one of Canada's highest civilian honours. It recognizes outstanding achievement, dedication to the community, and service to Canada at all levels."
  },
  {
    "id": "q087",
    "topic": "Canadian Symbols",
    "subtopic": "Honours",
    "question": "What is the Victoria Cross?",
    "options": [
      "A monument in Victoria, British Columbia",
      "Canada's highest civilian honour",
      "Canada's highest military honour, awarded for extreme bravery in battle",
      "A religious symbol used in citizenship ceremonies"
    ],
    "answerIndex": 2,
    "explanation": "The Victoria Cross is the highest military honour awarded to Canadians for extreme bravery in battle. It was established in 1854, and 96 Canadians have been awarded the Victoria Cross since Confederation."
  },

  # ─── CANADA'S ECONOMY (additional) ─────────────────────────────────────────
  {
    "id": "q088",
    "topic": "Canada's Economy",
    "subtopic": "Economic Sectors",
    "question": "What are the three main sectors of the Canadian economy?",
    "options": [
      "Technology, agriculture, and mining",
      "Banking, real estate, and tourism",
      "Service industries, manufacturing, and natural resources",
      "Fishing, farming, and forestry only"
    ],
    "answerIndex": 2,
    "explanation": "The three main sectors of Canada's economy are service industries (the largest, accounting for more than 75% of jobs), manufacturing, and natural resources (including agriculture, fishing, mining, and energy)."
  },
  {
    "id": "q089",
    "topic": "Canada's Economy",
    "subtopic": "Economic Sectors",
    "question": "Approximately what percentage of Canadian jobs are in the service sector?",
    "options": [
      "About 25%",
      "About 50%",
      "More than 75%",
      "About 90%"
    ],
    "answerIndex": 2,
    "explanation": "The service sector employs more than 75% of Canadians and includes industries such as retail, health care, education, banking, finance, communications, and government."
  },
  {
    "id": "q090",
    "topic": "Canada's Economy",
    "subtopic": "Free Trade",
    "question": "When did Canada and the United States sign a free trade agreement?",
    "options": [
      "1982",
      "1988",
      "1994",
      "2001"
    ],
    "answerIndex": 1,
    "explanation": "Canada and the United States signed the Canada-US Free Trade Agreement in 1988, eliminating most trade barriers between the two countries. This was later expanded into NAFTA in 1994, which added Mexico."
  },
  {
    "id": "q091",
    "topic": "Canada's Economy",
    "subtopic": "Free Trade",
    "question": "What does NAFTA stand for, and when did it come into effect?",
    "options": [
      "North American Farming and Trade Act, 1988",
      "North American Free Trade Agreement, 1994, between Canada, the US, and Mexico",
      "Northern Alliance Free Trade Agreement, 2000",
      "National and Foreign Trade Act, 1996"
    ],
    "answerIndex": 1,
    "explanation": "NAFTA (North American Free Trade Agreement) came into effect in 1994. It created a free trade zone between Canada, the United States, and Mexico, and remains one of the world's largest free trade agreements."
  },
  {
    "id": "q092",
    "topic": "Canada's Economy",
    "subtopic": "Financial Institutions",
    "question": "When was the Bank of Canada established?",
    "options": [
      "1867",
      "1914",
      "1934",
      "1945"
    ],
    "answerIndex": 2,
    "explanation": "The Bank of Canada was established in 1934. It is the country's central bank, responsible for monetary policy, issuing bank notes, and promoting a safe and sound financial system."
  },

  # ─── CANADA'S REGIONS (additional) ─────────────────────────────────────────
  {
    "id": "q093",
    "topic": "Canada's Regions",
    "subtopic": "Provinces",
    "question": "What are the Prairie Provinces?",
    "options": [
      "Ontario, Quebec, and Manitoba",
      "Alberta, British Columbia, and Saskatchewan",
      "Manitoba, Saskatchewan, and Alberta",
      "Saskatchewan, Manitoba, and Ontario"
    ],
    "answerIndex": 2,
    "explanation": "Manitoba, Saskatchewan, and Alberta are called the Prairie Provinces. They are known for vast flat plains, fertile farmland, and major natural resources including oil and natural gas (especially in Alberta)."
  },
  {
    "id": "q094",
    "topic": "Canada's Regions",
    "subtopic": "Provinces",
    "question": "What are the Atlantic Provinces (Maritime Provinces + Newfoundland)?",
    "options": [
      "Ontario, Quebec, New Brunswick, and Nova Scotia",
      "Nova Scotia, New Brunswick, Prince Edward Island, and Newfoundland and Labrador",
      "Newfoundland, Nova Scotia, PEI, and Quebec",
      "New Brunswick, Quebec, and Newfoundland and Labrador"
    ],
    "answerIndex": 1,
    "explanation": "The Atlantic Provinces are Nova Scotia, New Brunswick, Prince Edward Island, and Newfoundland and Labrador. Nova Scotia, New Brunswick, and PEI are sometimes referred to as the Maritime Provinces."
  },
  {
    "id": "q095",
    "topic": "Canada's Regions",
    "subtopic": "Provinces",
    "question": "Which province joined Confederation last, in 1949?",
    "options": [
      "Prince Edward Island",
      "British Columbia",
      "Manitoba",
      "Newfoundland and Labrador"
    ],
    "answerIndex": 3,
    "explanation": "Newfoundland and Labrador was the last province to join Confederation, doing so on March 31, 1949, under Premier Joey Smallwood following a closely contested referendum."
  },
  {
    "id": "q096",
    "topic": "Canada's Regions",
    "subtopic": "Provinces",
    "question": "What is the only officially bilingual province in Canada?",
    "options": [
      "Ontario",
      "Quebec",
      "Nova Scotia",
      "New Brunswick"
    ],
    "answerIndex": 3,
    "explanation": "New Brunswick is Canada's only officially bilingual province, with both English and French as official languages. About one-third of New Brunswickers are Francophone Acadians."
  },
  {
    "id": "q097",
    "topic": "Canada's Regions",
    "subtopic": "Capitals",
    "question": "What is the capital city of British Columbia?",
    "options": [
      "Vancouver",
      "Victoria",
      "Kelowna",
      "Surrey"
    ],
    "answerIndex": 1,
    "explanation": "Victoria is the capital city of British Columbia, located on the southern tip of Vancouver Island. Vancouver is the largest city in BC but is not the provincial capital."
  },
  {
    "id": "q098",
    "topic": "Canada's Regions",
    "subtopic": "Capitals",
    "question": "What is the capital city of Alberta?",
    "options": [
      "Calgary",
      "Red Deer",
      "Edmonton",
      "Lethbridge"
    ],
    "answerIndex": 2,
    "explanation": "Edmonton is the capital city of Alberta. Calgary is the largest city in Alberta by population, but Edmonton is the provincial capital and home to the provincial legislature."
  },

  # ─── CANADA'S HISTORY (additional) ─────────────────────────────────────────
  {
    "id": "q099",
    "topic": "Canada's History",
    "subtopic": "Métis and Riel",
    "question": "Who led the Métis uprising in Manitoba (1869–70) and was later executed in 1885?",
    "options": [
      "Chief Sitting Bull",
      "Gabriel Dumont",
      "Louis Riel",
      "Joseph Brant"
    ],
    "answerIndex": 2,
    "explanation": "Louis Riel led the Red River Resistance (1869–70), which resulted in Manitoba joining Confederation. He also led a second resistance in Saskatchewan in 1885 and was subsequently tried for treason and executed."
  },
  {
    "id": "q100",
    "topic": "Canada's History",
    "subtopic": "World Wars",
    "question": "What is commemorated on April 9 (Vimy Day)?",
    "options": [
      "Canada's entry into World War II",
      "The signing of the Treaty of Paris",
      "The capture of Vimy Ridge by the Canadian Corps in 1917",
      "The end of World War I"
    ],
    "answerIndex": 2,
    "explanation": "April 9 is Vimy Day, commemorating the capture of Vimy Ridge in France on April 9, 1917, by the Canadian Corps. This victory is considered a defining moment in Canada's emergence as a nation."
  },
  {
    "id": "q101",
    "topic": "Canada's History",
    "subtopic": "Aboriginal Rights",
    "question": "What was the Royal Proclamation of 1763?",
    "options": [
      "A declaration of war against France after the Seven Years' War",
      "A founding document recognizing Aboriginal peoples' rights to their lands",
      "The agreement creating the Dominion of Canada",
      "An act abolishing slavery in British North America"
    ],
    "answerIndex": 1,
    "explanation": "The Royal Proclamation of 1763 was issued by King George III after Britain acquired New France. It recognized Aboriginal peoples' rights to their lands and established that treaties must be negotiated for land transfers."
  },
  {
    "id": "q102",
    "topic": "Canada's History",
    "subtopic": "Notable Canadians",
    "question": "Who was Agnes Macphail?",
    "options": [
      "The first female Prime Minister of Canada",
      "The first woman elected to the House of Commons (1921)",
      "The first female Governor General of Canada",
      "The first woman to vote in a Canadian federal election"
    ],
    "answerIndex": 1,
    "explanation": "Agnes Macphail was the first woman elected to the Canadian House of Commons, winning her seat in the 1921 federal election. She was a champion of social reform and pacifism."
  },
  {
    "id": "q103",
    "topic": "Canada's History",
    "subtopic": "Railways",
    "question": "What railway connected Canada from coast to coast, completing its last spike in 1885?",
    "options": [
      "The Grand Trunk Pacific Railway",
      "The Canadian National Railway",
      "The Trans-Canada Railway",
      "The Canadian Pacific Railway (CPR)"
    ],
    "answerIndex": 3,
    "explanation": "The Canadian Pacific Railway (CPR) was completed on November 7, 1885, when the last spike was driven at Craigellachie, British Columbia. The transcontinental railway was a condition of British Columbia joining Confederation."
  },
  {
    "id": "q104",
    "topic": "Canada's History",
    "subtopic": "Acadians",
    "question": "What was the 'Great Upheaval' (Le Grand Dérangement)?",
    "options": [
      "A major earthquake that struck Quebec City in the 18th century",
      "The forced deportation of Acadians from their homeland by the British (1755–1763)",
      "The forced relocation of First Nations peoples to residential schools",
      "The French Revolution's impact on New France"
    ],
    "answerIndex": 1,
    "explanation": "The Great Upheaval (Le Grand Dérangement) was the forced deportation of Acadians from their homeland in the Maritime provinces between 1755 and 1763 by British colonial authorities. Tens of thousands of Acadians were expelled."
  },
  {
    "id": "q105",
    "topic": "Canada's History",
    "subtopic": "French Canada",
    "question": "What did the Quebec Act of 1774 do for French Canadians?",
    "options": [
      "Made New France an independent country",
      "Banned the French language in government",
      "Granted religious freedom to Catholics and restored French civil law in Quebec",
      "United Upper and Lower Canada into one province"
    ],
    "answerIndex": 2,
    "explanation": "The Quebec Act of 1774 was significant for French Canadians: it restored French civil law, granted Catholics the freedom to practice their religion, and recognized French-Canadian culture — an important step in protecting French rights in British North America."
  },
  {
    "id": "q106",
    "topic": "Canada's History",
    "subtopic": "Exploration",
    "question": "Who sailed to Canada in 1497, exploring the Atlantic coast for England?",
    "options": [
      "Jacques Cartier",
      "Samuel de Champlain",
      "John Cabot",
      "Pierre de Monts"
    ],
    "answerIndex": 2,
    "explanation": "John Cabot sailed from England in 1497 and mapped much of Canada's Atlantic coast. His voyage was one of the first European explorations of Canada after the Vikings and formed the basis for England's claim to North America."
  },
  {
    "id": "q107",
    "topic": "Canada's History",
    "subtopic": "Exploration",
    "question": "Who founded Quebec City in 1608?",
    "options": [
      "Jacques Cartier",
      "Pierre de Monts",
      "John Cabot",
      "Samuel de Champlain"
    ],
    "answerIndex": 3,
    "explanation": "Samuel de Champlain built a fortress at Quebec City in 1608. Known as the 'Father of New France,' Champlain was a key figure in establishing French settlements in Canada."
  },
  {
    "id": "q108",
    "topic": "Canada's History",
    "subtopic": "Early Peoples",
    "question": "Who were the first Europeans to reach Canada (around 1000 AD)?",
    "options": [
      "Spanish explorers from the Azores",
      "Portuguese fishermen",
      "French merchants",
      "Norse (Viking) explorers from Iceland"
    ],
    "answerIndex": 3,
    "explanation": "Norse (Viking) explorers, led by Leif Eriksson, reached Labrador and Newfoundland around 1000 AD. The site of L'Anse aux Meadows in Newfoundland confirms their presence — it is Canada's only confirmed Norse settlement."
  },

  # ─── RIGHTS AND RESPONSIBILITIES (additional) ───────────────────────────────
  {
    "id": "q109",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Fundamental Freedoms",
    "question": "Which of the following is NOT one of the four fundamental freedoms protected by the Canadian Charter of Rights and Freedoms?",
    "options": [
      "Freedom of conscience and religion",
      "Freedom of thought, belief, opinion, and expression",
      "Freedom of peaceful assembly",
      "Freedom from taxation"
    ],
    "answerIndex": 3,
    "explanation": "The four fundamental freedoms in the Charter are: (1) freedom of conscience and religion; (2) freedom of thought, belief, opinion, and expression (including the press); (3) freedom of peaceful assembly; and (4) freedom of association. Freedom from taxation is not a fundamental freedom."
  },
  {
    "id": "q110",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Equality Rights",
    "question": "What do Canada's equality rights protect?",
    "options": [
      "Only the rights of Aboriginal peoples",
      "The right of all Canadians to be free from discrimination based on race, religion, sex, age, and other grounds",
      "Only the rights of French Canadians",
      "The right to equal pay in all private businesses"
    ],
    "answerIndex": 1,
    "explanation": "Canada's Charter of Rights and Freedoms guarantees equality rights — protection from discrimination based on race, national or ethnic origin, colour, religion, sex, age, or mental or physical disability."
  },
  {
    "id": "q111",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Responsibilities",
    "question": "What is jury duty in Canada?",
    "options": [
      "A voluntary service that any Canadian can choose to perform",
      "A service required only of lawyers and judges",
      "A civic responsibility of Canadian citizens to serve on a jury when called upon",
      "A requirement only for permanent residents"
    ],
    "answerIndex": 2,
    "explanation": "Serving on a jury is a civic responsibility of Canadian citizens. When summoned for jury duty, eligible citizens are required to consider the evidence fairly and reach a verdict according to the law."
  },
  {
    "id": "q112",
    "topic": "Rights and Responsibilities of Citizenship",
    "subtopic": "Equality Rights",
    "question": "What does Canada's commitment to gender equality mean?",
    "options": [
      "Men are given priority in employment decisions",
      "Women can only work in government jobs",
      "Men and women are equal under Canadian law, and gender-based violence is illegal",
      "Men and women have different legal rights depending on the province"
    ],
    "answerIndex": 2,
    "explanation": "Canada is committed to gender equality — men and women are equal under the law. Gender-based violence, including female genital mutilation, forced marriage, and so-called honour killings, are serious crimes in Canada."
  },

  # ─── WHO WE ARE (additional) ────────────────────────────────────────────────
  {
    "id": "q113",
    "topic": "Who We Are",
    "subtopic": "Aboriginal Peoples",
    "question": "What does the word 'Inuit' mean in Inuktitut?",
    "options": [
      "Northern people",
      "People of the ice",
      "The people",
      "Arctic dwellers"
    ],
    "answerIndex": 2,
    "explanation": "'Inuit' means 'the people' in Inuktitut, the Inuit language. Inuit people live in the Arctic regions of Canada, mainly in Nunavut, the Northwest Territories, northern Quebec, and Labrador."
  },
  {
    "id": "q114",
    "topic": "Who We Are",
    "subtopic": "Aboriginal Peoples",
    "question": "Who are the Métis people?",
    "options": [
      "Descendants of French settlers in Quebec",
      "Indigenous people of the Arctic who speak Inuktitut",
      "People of mixed Aboriginal and European heritage, with their own distinct culture",
      "A First Nations group from the Pacific coast"
    ],
    "answerIndex": 2,
    "explanation": "The Métis are a distinct group of people with mixed Aboriginal and European (mainly French) heritage. They developed their own unique culture and language (Michif). They primarily live in the Prairie provinces."
  },
  {
    "id": "q115",
    "topic": "Who We Are",
    "subtopic": "Francophones",
    "question": "What is the significance of the Québécois nation?",
    "options": [
      "Quebec is an independent country within Canada",
      "The Parliament of Canada recognized in 2006 that the Québécois form a nation within a united Canada",
      "Quebecers have a separate constitution",
      "Quebec has its own military force"
    ],
    "answerIndex": 1,
    "explanation": "In 2006, the Parliament of Canada recognized that the Québécois form a nation within a united Canada — acknowledging their unique language, culture, and civil law tradition while reaffirming Canada's unity."
  },
  {
    "id": "q116",
    "topic": "Who We Are",
    "subtopic": "Languages",
    "question": "Approximately how many Canadians speak French as their first language?",
    "options": [
      "About 1 million",
      "About 3 million",
      "About 7 million",
      "About 15 million"
    ],
    "answerIndex": 2,
    "explanation": "About 7 million Canadians (roughly one-quarter of the population) speak French as their first language. Most Francophones live in Quebec, but significant French-speaking communities also exist in Ontario, New Brunswick, and other provinces."
  },

  # ─── HOW CANADIANS GOVERN THEMSELVES (additional) ───────────────────────────
  {
    "id": "q117",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "Parliament",
    "question": "How many seats are currently in the Canadian House of Commons?",
    "options": [
      "265",
      "308",
      "338",
      "400"
    ],
    "answerIndex": 2,
    "explanation": "The Canadian House of Commons currently has 338 seats (electoral districts). Each seat represents one riding, and the MP elected in each riding represents the people of that district in Parliament."
  },
  {
    "id": "q118",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "Senate",
    "question": "What is the role of the Senate in Canada?",
    "options": [
      "To elect the Prime Minister",
      "To approve appointments made by the Prime Minister",
      "To review, refine, and amend legislation passed by the House of Commons",
      "To declare war on behalf of Canada"
    ],
    "answerIndex": 2,
    "explanation": "The Senate is the upper house of Parliament. Its role is to review and debate legislation passed by the House of Commons, and to give 'sober second thought' to proposed laws. The Senate can amend or reject bills."
  },
  {
    "id": "q119",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "Governor General",
    "question": "What is the role of the Governor General?",
    "options": [
      "To make federal laws",
      "To lead the governing party",
      "To represent the Sovereign (King/Queen) and carry out constitutional functions in Canada",
      "To command the Canadian Armed Forces in battle"
    ],
    "answerIndex": 2,
    "explanation": "The Governor General is the representative of the Sovereign (King/Queen) in Canada. The role includes opening and closing Parliament, granting Royal Assent to legislation, swearing in the Prime Minister, and performing ceremonial duties."
  },
  {
    "id": "q120",
    "topic": "How Canadians Govern Themselves",
    "subtopic": "Levels of Government",
    "question": "Which level of government is responsible for municipal services such as snow removal, transit, and local policing?",
    "options": [
      "Federal government",
      "Provincial government",
      "Municipal (city/town) government",
      "Territorial government"
    ],
    "answerIndex": 2,
    "explanation": "Municipal (city or town) governments are responsible for local services including snow removal, public transit, garbage collection, local police, firefighting, and community recreation. Municipal councils are led by a mayor or reeve."
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
        else:
            print(f"  Skipping duplicate: {q['id']}")

    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)

    print(f"\nDone. Added {added} new questions. Total: {len(existing)} questions.")

    # Summary by topic
    topics = {}
    for q in existing:
        topics[q['topic']] = topics.get(q['topic'], 0) + 1
    print("\nQuestions by topic:")
    for t, c in sorted(topics.items()):
        print(f"  {t}: {c}")

if __name__ == '__main__':
    main()
