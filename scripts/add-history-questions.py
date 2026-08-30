#!/usr/bin/env python3
"""
Add new Canada's History questions (q191–q255).
"""
import json, os

DATA_FILE = os.path.join(os.path.dirname(__file__), '../src/assets/data/questions.json')

NEW_QUESTIONS = [
  # ── PRE-CONFEDERATION & EXPLORATION ─────────────────────────────────────────
  {
    "id": "q191",
    "topic": "Canada's History",
    "subtopic": "Exploration",
    "question": "What is the significance of L'Anse aux Meadows?",
    "options": [
      "The site of the first British fort in Canada",
      "The site of Canada's first parliament building",
      "The only confirmed Norse (Viking) settlement in North America, in Newfoundland",
      "The place where Jacques Cartier first landed in 1534"
    ],
    "answerIndex": 2,
    "explanation": "L'Anse aux Meadows in Newfoundland is the only confirmed Norse (Viking) settlement in North America, dating to around 1000 AD. It was designated a UNESCO World Heritage Site and proves Europeans reached Canada centuries before Columbus."
  },
  {
    "id": "q192",
    "topic": "Canada's History",
    "subtopic": "Exploration",
    "question": "Who was Jacques Cartier and what did he do?",
    "options": [
      "A British explorer who mapped the Pacific coast of Canada in 1778",
      "A French explorer who made three voyages to Canada (1534–1542) and named the country 'Canada' from the Iroquoian word 'kanata'",
      "A Scottish explorer who founded Halifax in 1749",
      "A Portuguese navigator who first reached Newfoundland"
    ],
    "answerIndex": 1,
    "explanation": "Jacques Cartier was a French explorer who made three voyages to Canada between 1534 and 1542. He explored the Gulf of St. Lawrence and the St. Lawrence River and named the region 'Canada' from the Iroquoian word 'kanata,' meaning village or settlement."
  },
  {
    "id": "q193",
    "topic": "Canada's History",
    "subtopic": "New France",
    "question": "When was the first permanent European settlement in Canada established, and by whom?",
    "options": [
      "1497 by John Cabot",
      "1534 by Jacques Cartier",
      "1604 by Pierre de Monts and Samuel de Champlain, in present-day Nova Scotia",
      "1670 by the Hudson's Bay Company"
    ],
    "answerIndex": 2,
    "explanation": "The first permanent European settlement in Canada was established in 1604 by Pierre de Monts and Samuel de Champlain at Port Royal, in present-day Nova Scotia. This was the beginning of Acadia, the first permanent French colony in North America."
  },
  {
    "id": "q194",
    "topic": "Canada's History",
    "subtopic": "New France",
    "question": "What was the Hudson's Bay Company and when was it founded?",
    "options": [
      "A fur-trading company established in 1670 by a royal charter, given exclusive trading rights over all lands draining into Hudson Bay",
      "A railway company that built the transcontinental rail line in 1885",
      "A British military company that managed forts across Canada in the 1800s",
      "A bank established in New France in 1720"
    ],
    "answerIndex": 0,
    "explanation": "The Hudson's Bay Company (HBC) was established in 1670 by a royal charter from King Charles II. It was granted exclusive trading rights over all lands draining into Hudson Bay — a vast territory called Rupert's Land. The HBC played a central role in Canada's fur trade and early settlement."
  },
  {
    "id": "q195",
    "topic": "Canada's History",
    "subtopic": "New France",
    "question": "What was New France?",
    "options": [
      "A French colony in the Caribbean",
      "The French colonial territory in North America, including Quebec, Acadia, and territories around the Great Lakes and Mississippi River",
      "A part of France set aside for Canadian trade",
      "The name for Montreal before 1642"
    ],
    "answerIndex": 1,
    "explanation": "New France was the French colonial empire in North America, stretching from Newfoundland to the Rocky Mountains and from the Gulf of Mexico to Hudson Bay at its height. Quebec City (founded 1608) was its capital. New France came under British control after 1763."
  },
  {
    "id": "q196",
    "topic": "Canada's History",
    "subtopic": "British Rule",
    "question": "What was the Treaty of Paris (1763)?",
    "options": [
      "The treaty ending World War I",
      "The treaty that ended the Seven Years' War, through which France ceded most of New France to Britain",
      "A trade agreement between Canada and France signed in 1763",
      "The peace treaty ending the War of 1812"
    ],
    "answerIndex": 1,
    "explanation": "The Treaty of Paris (1763) ended the Seven Years' War between Britain and France. Through this treaty, France ceded most of New France (including what is now Quebec and eastern Canada) to Britain, transforming Canada into a British colony."
  },
  {
    "id": "q197",
    "topic": "Canada's History",
    "subtopic": "British Rule",
    "question": "What did the Constitutional Act of 1791 do?",
    "options": [
      "Created the Dominion of Canada",
      "Divided Quebec into Upper Canada (mainly English-speaking) and Lower Canada (mainly French-speaking)",
      "Gave women the right to vote in elections",
      "Abolished the British Parliament's right to legislate for Canada"
    ],
    "answerIndex": 1,
    "explanation": "The Constitutional Act of 1791 divided the former Province of Quebec into Upper Canada (present-day Ontario, mostly English-speaking, using British law) and Lower Canada (present-day Quebec, mostly French-speaking, using French civil law). Each had its own elected assembly."
  },
  {
    "id": "q198",
    "topic": "Canada's History",
    "subtopic": "Responsible Government",
    "question": "What does 'responsible government' mean in Canadian history?",
    "options": [
      "A government that balances its budget",
      "A system where the executive government must have the confidence and support of the elected legislature",
      "A government that responds quickly to emergencies",
      "A form of government where judges make all major decisions"
    ],
    "answerIndex": 1,
    "explanation": "Responsible government means the Cabinet (executive) must have the support (confidence) of the elected legislature to govern. If it loses a confidence vote, the government must resign or call an election. Nova Scotia was the first British colony to achieve responsible government in 1847–48."
  },
  {
    "id": "q199",
    "topic": "Canada's History",
    "subtopic": "Rebellions",
    "question": "What were the Rebellions of 1837–38?",
    "options": [
      "Indigenous uprisings against European settlement",
      "Armed rebellions in Upper and Lower Canada against British colonial rule, demanding democratic reform",
      "Rebellions by American settlers trying to join the United States",
      "Military revolts by the French army in Quebec"
    ],
    "answerIndex": 1,
    "explanation": "The Rebellions of 1837–38 were armed uprisings in Upper Canada (led by William Lyon Mackenzie) and Lower Canada (led by Louis-Joseph Papineau) against British colonial rule. They failed militarily but led to important political reforms, including responsible government."
  },
  {
    "id": "q200",
    "topic": "Canada's History",
    "subtopic": "Confederation",
    "question": "Which four provinces originally formed the Dominion of Canada at Confederation in 1867?",
    "options": [
      "Ontario, Quebec, Nova Scotia, and British Columbia",
      "Ontario, Quebec, New Brunswick, and Nova Scotia",
      "Quebec, Ontario, PEI, and New Brunswick",
      "Nova Scotia, New Brunswick, Quebec, and Manitoba"
    ],
    "answerIndex": 1,
    "explanation": "On July 1, 1867, the Dominion of Canada was formed by four provinces: Ontario (formerly Upper Canada), Quebec (formerly Lower Canada), Nova Scotia, and New Brunswick. Other provinces joined later."
  },
  {
    "id": "q201",
    "topic": "Canada's History",
    "subtopic": "Confederation",
    "question": "What was the British North America Act (1867)?",
    "options": [
      "A law drafted by the British Parliament creating the Dominion of Canada and setting out its federal structure",
      "A treaty between Britain and the United States about the US–Canada border",
      "A declaration of Canadian independence from Britain",
      "A law establishing the Canadian Charter of Rights and Freedoms"
    ],
    "answerIndex": 0,
    "explanation": "The British North America Act (BNA Act) of 1867, passed by the British Parliament, created the Dominion of Canada and established Canada's federal structure — outlining the division of powers between the federal and provincial governments. It is now called the Constitution Act, 1867."
  },
  {
    "id": "q202",
    "topic": "Canada's History",
    "subtopic": "Confederation",
    "question": "What is 'Dominion Day' and what is it called today?",
    "options": [
      "The day Confederation was declared — July 1, 1867 — now called Canada Day",
      "The day the first Prime Minister was elected",
      "The day the Charter of Rights was adopted",
      "The day the last province joined Canada"
    ],
    "answerIndex": 0,
    "explanation": "Dominion Day was the original name for July 1, the anniversary of Confederation in 1867. In 1982, the name was officially changed to Canada Day. It is celebrated as a national holiday across Canada."
  },
  {
    "id": "q203",
    "topic": "Canada's History",
    "subtopic": "Post-Confederation",
    "question": "When did British Columbia join Confederation, and why?",
    "options": [
      "1867 — as a founding province",
      "1871 — on the condition that Canada build a transcontinental railway linking BC to the rest of Canada",
      "1873 — after a referendum on joining Canada",
      "1885 — after the Canadian Pacific Railway was completed"
    ],
    "answerIndex": 1,
    "explanation": "British Columbia joined Confederation on July 20, 1871, on the condition that the Canadian government build a transcontinental railway connecting BC to eastern Canada within 10 years. This led to the construction of the Canadian Pacific Railway."
  },
  {
    "id": "q204",
    "topic": "Canada's History",
    "subtopic": "Post-Confederation",
    "question": "What is the significance of the North West Mounted Police (NWMP), established in 1873?",
    "options": [
      "Canada's first permanent army, created to fight the United States",
      "A police force created to bring Canadian law and order to the Northwest territories and protect settlers, eventually becoming the RCMP",
      "A private security company hired by the Hudson's Bay Company",
      "A military force established to suppress Indigenous uprisings"
    ],
    "answerIndex": 1,
    "explanation": "The North West Mounted Police (NWMP) was established in 1873 to bring law and order to the vast Northwest Territories after Canada acquired Rupert's Land. They negotiated peace with Indigenous peoples and protected settlers. The NWMP became the Royal Canadian Mounted Police (RCMP) in 1920."
  },
  {
    "id": "q205",
    "topic": "Canada's History",
    "subtopic": "Post-Confederation",
    "question": "Who was Sir Wilfrid Laurier and why is he significant?",
    "options": [
      "Canada's first Prime Minister and Father of Confederation",
      "Canada's first French-Canadian Prime Minister (1896–1911), famous for encouraging immigration to the Prairies",
      "The Governor General who signed the Constitution Act, 1982",
      "The Prime Minister who introduced universal health care"
    ],
    "answerIndex": 1,
    "explanation": "Sir Wilfrid Laurier (1841–1919) was Canada's first French-Canadian Prime Minister, serving from 1896 to 1911. He presided over a period of great immigration and economic growth. His portrait appears on the $5 bill. Laurier Day is November 20."
  },
  # ── WORLD WARS ────────────────────────────────────────────────────────────────
  {
    "id": "q206",
    "topic": "Canada's History",
    "subtopic": "World Wars",
    "question": "How many Canadians served in World War I, and how many were killed?",
    "options": [
      "About 100,000 served; 10,000 killed",
      "About 600,000 served; 60,000 killed",
      "About 1 million served; 100,000 killed",
      "About 200,000 served; 30,000 killed"
    ],
    "answerIndex": 1,
    "explanation": "More than 600,000 Canadians served in World War I (1914–1918). Of those, about 60,000 were killed and more than 170,000 were wounded. Canada's contribution to WWI — including the victory at Vimy Ridge — helped forge a sense of national identity."
  },
  {
    "id": "q207",
    "topic": "Canada's History",
    "subtopic": "World Wars",
    "question": "What was the Conscription Crisis of 1917?",
    "options": [
      "A crisis caused by too many Canadians volunteering for the military",
      "A political crisis when the government introduced mandatory military service (conscription), dividing Canadians — especially between English and French Canada",
      "A labour dispute at munitions factories in Ontario",
      "A dispute over who would command Canadian troops in Europe"
    ],
    "answerIndex": 1,
    "explanation": "The Conscription Crisis of 1917 arose when Prime Minister Robert Borden introduced mandatory military service. Most English Canadians supported it; most French Canadians (who felt little connection to Britain or France) strongly opposed it. The crisis caused deep divisions between French and English Canada."
  },
  {
    "id": "q208",
    "topic": "Canada's History",
    "subtopic": "World Wars",
    "question": "What happened at Dieppe in August 1942?",
    "options": [
      "A major Canadian naval victory in the English Channel",
      "A disastrous Allied raid on the French coast in which most of the nearly 5,000 Canadian soldiers were killed, wounded, or captured",
      "The first Canadian air force mission of WWII",
      "The liberation of a major French city by Canadian forces"
    ],
    "answerIndex": 1,
    "explanation": "The Dieppe Raid (August 19, 1942) was a disastrous Allied assault on the French port of Dieppe. Of nearly 5,000 Canadian soldiers who participated, about 900 were killed and nearly 2,000 were captured. The lessons learned at Dieppe helped plan the more successful D-Day landings."
  },
  {
    "id": "q209",
    "topic": "Canada's History",
    "subtopic": "World Wars",
    "question": "What was the role of Canadian women during World War II?",
    "options": [
      "They were not allowed to participate in the war effort",
      "They served in the armed forces in non-combat roles and worked in factories, farms, and industry to support the war effort",
      "They served as combat soldiers on the front lines",
      "They only volunteered as nurses in Canadian hospitals"
    ],
    "answerIndex": 1,
    "explanation": "Canadian women played a vital role in WWII. More than 45,000 women served in the armed forces in non-combat roles (communications, medical, administration). Many more worked in factories, farms, and businesses to replace men who had gone to war."
  },
  {
    "id": "q210",
    "topic": "Canada's History",
    "subtopic": "World Wars",
    "question": "How many Canadians served in World War II?",
    "options": [
      "About 200,000",
      "About 500,000",
      "About 1 million",
      "About 2 million"
    ],
    "answerIndex": 2,
    "explanation": "More than 1 million Canadians served in World War II (1939–1945), out of a population of about 11 million. About 44,000 were killed. Canada made massive contributions on land, at sea, and in the air."
  },
  {
    "id": "q211",
    "topic": "Canada's History",
    "subtopic": "World Wars",
    "question": "What was Canada's contribution to the liberation of the Netherlands in WWII?",
    "options": [
      "Canada played no role in liberating the Netherlands",
      "Canadian forces liberated much of the Netherlands in 1944–1945; the Dutch consider Canadians national heroes",
      "Canadian airmen exclusively conducted the liberation by bombing",
      "Canada sent only medical teams to the Netherlands"
    ],
    "answerIndex": 1,
    "explanation": "Canadian forces played a leading role in the liberation of the Netherlands in 1944–1945. The Dutch, who had suffered greatly under Nazi occupation, have an enduring bond of gratitude with Canada — Holland sends Canada 10,000 tulip bulbs annually as a thank-you."
  },
  {
    "id": "q212",
    "topic": "Canada's History",
    "subtopic": "World Wars",
    "question": "What was General Sir Arthur Currie's role in World War I?",
    "options": [
      "He was the British commander who ordered the Vimy Ridge assault",
      "He was Canada's most distinguished general in WWI, who led the Canadian Corps in the Hundred Days Offensive that helped end the war",
      "He was the first Canadian to receive the Victoria Cross in WWI",
      "He was the Prime Minister who declared war on Germany in 1914"
    ],
    "answerIndex": 1,
    "explanation": "General Sir Arthur Currie was Canada's greatest general in WWI. He commanded the Canadian Corps and led the Hundred Days Offensive (August–November 1918), a series of successful Allied attacks that helped bring WWI to an end. He was the first Canadian-born general to command the Canadian Corps."
  },
  # ── MODERN ERA ────────────────────────────────────────────────────────────────
  {
    "id": "q213",
    "topic": "Canada's History",
    "subtopic": "Modern Era",
    "question": "When was the first Canadian flag (the current Maple Leaf flag) raised?",
    "options": [
      "July 1, 1867",
      "November 11, 1918",
      "February 15, 1965",
      "April 17, 1982"
    ],
    "answerIndex": 2,
    "explanation": "The current Canadian flag — the red-and-white maple leaf flag — was first raised on February 15, 1965, replacing the Canadian Red Ensign. The design was inspired by the flag of the Royal Military College (RMC) of Canada, founded in Kingston in 1876."
  },
  {
    "id": "q214",
    "topic": "Canada's History",
    "subtopic": "Modern Era",
    "question": "Who was Pierre Elliott Trudeau and what is he known for?",
    "options": [
      "Canada's first Prime Minister",
      "A Prime Minister (1968–1979, 1980–1984) who introduced the Charter of Rights and Freedoms and the Official Languages Act",
      "The Governor General who signed the BNA Act",
      "Canada's first French-Canadian Prime Minister"
    ],
    "answerIndex": 1,
    "explanation": "Pierre Elliott Trudeau served as Prime Minister of Canada in 1968–1979 and 1980–1984. He is known for introducing the Official Languages Act (1969), the War Measures Act during the 1970 October Crisis, and most importantly, the Constitution Act and Canadian Charter of Rights and Freedoms in 1982."
  },
  {
    "id": "q215",
    "topic": "Canada's History",
    "subtopic": "Modern Era",
    "question": "What was the October Crisis of 1970?",
    "options": [
      "A stock market crash that caused the Great Depression in Canada",
      "A political crisis in Quebec when the FLQ kidnapped British trade commissioner James Cross and Quebec minister Pierre Laporte, leading PM Trudeau to invoke the War Measures Act",
      "A flood that devastated Manitoba in October 1970",
      "A crisis caused by Quebec's vote to separate from Canada"
    ],
    "answerIndex": 1,
    "explanation": "The October Crisis of 1970 was triggered by the Quebec separatist group FLQ, which kidnapped British trade commissioner James Cross and Quebec labour minister Pierre Laporte (who was later murdered). PM Trudeau invoked the War Measures Act, suspending civil liberties and mobilizing the army. Cross was eventually freed; the FLQ members were flown to Cuba."
  },
  {
    "id": "q216",
    "topic": "Canada's History",
    "subtopic": "Modern Era",
    "question": "What happened in the Quebec Referendum of 1980?",
    "options": [
      "Quebec voted to separate from Canada",
      "Quebec voted to allow the federal government to use the notwithstanding clause",
      "The 'Yes' side (sovereignty-association) was defeated — Quebecers voted to remain in Canada",
      "Quebec voted to adopt English as a co-official language"
    ],
    "answerIndex": 2,
    "explanation": "In the 1980 Quebec Referendum, Quebecers voted on whether to give the provincial government a mandate to negotiate sovereignty-association (political independence with economic ties) with the rest of Canada. The 'Yes' (sovereignty) side lost, with about 60% voting 'No' to separation."
  },
  {
    "id": "q217",
    "topic": "Canada's History",
    "subtopic": "Modern Era",
    "question": "What happened in the Quebec Referendum of 1995?",
    "options": [
      "Quebec voted overwhelmingly to remain in Canada",
      "Quebec voted 50.6% to separate from Canada",
      "The sovereignty side was narrowly defeated, with about 50.6% voting 'No' to separation",
      "The referendum was cancelled by the federal government"
    ],
    "answerIndex": 2,
    "explanation": "In the 1995 Quebec Referendum, the sovereignty (separation) side was narrowly defeated. The 'No' side (staying in Canada) won by a very slim margin — approximately 50.6% to 49.4%. It was the closest Canada has ever come to breaking apart."
  },
  {
    "id": "q218",
    "topic": "Canada's History",
    "subtopic": "Modern Era",
    "question": "When was Nunavut created, and what is its significance?",
    "options": [
      "1982 — as part of the Constitution Act",
      "1999 — as Canada's newest territory, carved out of the Northwest Territories, with an Inuit majority population",
      "2006 — as a province recognizing Indigenous self-government",
      "1949 — at the same time Newfoundland joined Confederation"
    ],
    "answerIndex": 1,
    "explanation": "Nunavut ('Our Land' in Inuktitut) was created on April 1, 1999, when it was carved out of the Northwest Territories. It is Canada's largest and newest territory and has a majority Inuit population. It represented a major milestone in Indigenous land rights and self-government."
  },
  {
    "id": "q219",
    "topic": "Canada's History",
    "subtopic": "Modern Era",
    "question": "What was 'Expo 67'?",
    "options": [
      "An international trade fair focused on oil and gas",
      "A world's fair held in Montreal in 1967 to celebrate Canada's 100th anniversary (centennial) of Confederation",
      "A national science and technology exhibition held in Ottawa",
      "A military parade to mark the end of World War II"
    ],
    "answerIndex": 1,
    "explanation": "Expo 67 was the World's Fair held in Montreal in 1967 to celebrate Canada's 100th birthday (centennial). It was one of the most successful world's fairs of the 20th century, attracting 50 million visitors, and is seen as a high point of Canadian national pride."
  },
  {
    "id": "q220",
    "topic": "Canada's History",
    "subtopic": "Abolition of Slavery",
    "question": "What was Upper Canada's historic role regarding slavery?",
    "options": [
      "Upper Canada was the last province to abolish slavery",
      "Upper Canada, in 1793, became the first province to move toward abolishing slavery — passing legislation to limit the practice",
      "Upper Canada introduced slavery to Canada",
      "Upper Canada never had any enslaved people"
    ],
    "answerIndex": 1,
    "explanation": "In 1793, Upper Canada (now Ontario) under Governor John Graves Simcoe passed legislation making it the first province to move toward abolishing slavery. The Act limited slavery — those already enslaved remained so, but no new enslaved people could be brought in, and children of enslaved people would be freed at age 25."
  },
  {
    "id": "q221",
    "topic": "Canada's History",
    "subtopic": "Abolition of Slavery",
    "question": "What was the Underground Railroad?",
    "options": [
      "An actual railway built underground in Toronto in the 1800s",
      "A secret network of safe houses and escape routes that helped enslaved African Americans escape to Canada",
      "A code name for the Canadian Pacific Railway construction",
      "A French-Canadian smuggling network during the War of 1812"
    ],
    "answerIndex": 1,
    "explanation": "The Underground Railroad was a secret network of safe houses and routes used by enslaved African Americans to escape to freedom in the northern United States and Canada. Canada was seen as a safe destination because slavery was abolished in the British Empire in 1834."
  },
  {
    "id": "q222",
    "topic": "Canada's History",
    "subtopic": "Notable Canadians",
    "question": "Who was Nellie McClung?",
    "options": [
      "Canada's first female Senator",
      "A prominent Canadian woman who campaigned for women's right to vote and is one of the 'Famous Five' who won the 'Persons Case'",
      "The first woman elected to the House of Commons",
      "A French-Canadian novelist who campaigned for Quebec independence"
    ],
    "answerIndex": 1,
    "explanation": "Nellie McClung (1873–1951) was a famous Canadian activist, author, and politician who fought for women's rights, including the right to vote. She was one of the Famous Five who successfully argued in the 'Persons Case' (1929) that women were legally 'persons' under Canadian law."
  },
  {
    "id": "q223",
    "topic": "Canada's History",
    "subtopic": "Notable Canadians",
    "question": "What was the 'Persons Case' of 1929?",
    "options": [
      "A Supreme Court case determining whether corporations were legal persons",
      "A landmark court ruling that confirmed women were 'persons' under Canadian law and therefore eligible to be appointed to the Senate",
      "A case determining the rights of new immigrants",
      "A case about Indigenous treaty rights"
    ],
    "answerIndex": 1,
    "explanation": "The Persons Case (1929) was a landmark ruling by the British Privy Council (then Canada's highest court of appeal) that confirmed women were 'persons' under Canadian law and could be appointed to the Senate. The case was brought by the Famous Five: Emily Murphy, Nellie McClung, Irene Parlby, Louise McKinney, and Henrietta Muir Edwards."
  },
  {
    "id": "q224",
    "topic": "Canada's History",
    "subtopic": "World Wars",
    "question": "What was the Battle of the Atlantic?",
    "options": [
      "A naval battle between Canada and the United States off Newfoundland",
      "The longest continuous military campaign of WWII, in which Canada played a major role protecting supply convoys crossing the Atlantic from German U-boats",
      "A WWI naval battle in which Canada's navy was destroyed",
      "An air battle over the Atlantic between German and British forces"
    ],
    "answerIndex": 1,
    "explanation": "The Battle of the Atlantic (1939–1945) was the longest continuous military campaign of WWII. Canada's Royal Canadian Navy (RCN) played a crucial role, escorting supply convoys across the Atlantic and protecting vital supply lines from German U-boat attacks. By war's end, the RCN was one of the world's largest navies."
  },
  {
    "id": "q225",
    "topic": "Canada's History",
    "subtopic": "Aboriginal Peoples",
    "question": "When were Aboriginal peoples in Canada granted the right to vote in federal elections?",
    "options": [
      "1867, at Confederation",
      "1918, after WWI",
      "1948, after WWII",
      "1960, under PM Diefenbaker"
    ],
    "answerIndex": 3,
    "explanation": "Aboriginal peoples in Canada were not granted the right to vote in federal elections until 1960, under Prime Minister John Diefenbaker. Before this, many Indigenous peoples had been excluded from voting for decades."
  },
  {
    "id": "q226",
    "topic": "Canada's History",
    "subtopic": "Post-Confederation",
    "question": "What was 'Klondike Gold Rush' (1896–98) and how did it affect Canada?",
    "options": [
      "A gold rush in Ontario that funded Canada's railway expansion",
      "A major gold discovery in the Klondike region of Yukon that brought over 100,000 prospectors and led to the creation of the Yukon Territory in 1898",
      "A gold rush in British Columbia that led to BC joining Confederation",
      "A gold rush in Nova Scotia that established Halifax as a major port"
    ],
    "answerIndex": 1,
    "explanation": "The Klondike Gold Rush (1896–1899) brought more than 100,000 prospectors to the Yukon. The Klondike River area yielded millions of dollars of gold. The influx of people and attention to the region contributed to the creation of the Yukon Territory in 1898."
  },
  {
    "id": "q227",
    "topic": "Canada's History",
    "subtopic": "Great Depression",
    "question": "What was the Great Depression in Canada?",
    "options": [
      "A national mental health crisis in the 1960s",
      "A severe global economic downturn from 1929 that devastated Canada, with unemployment reaching 27% by 1933",
      "A recession during World War I caused by war spending",
      "An economic slowdown following Confederation in 1867"
    ],
    "answerIndex": 1,
    "explanation": "The Great Depression was a severe worldwide economic crisis triggered by the 1929 stock market crash. In Canada, it was particularly devastating — unemployment reached 27% in 1933 and drought destroyed Prairie farms during the 'Dirty Thirties.' It transformed Canadian economic policy and led to new social programs."
  },
  {
    "id": "q228",
    "topic": "Canada's History",
    "subtopic": "Post-Confederation",
    "question": "Who was Tommy Douglas and what is he famous for?",
    "options": [
      "A Conservative Prime Minister who signed NAFTA",
      "Premier of Saskatchewan who introduced Canada's first publicly funded universal health care system — the model for Medicare",
      "Canada's first Aboriginal Member of Parliament",
      "A general who led Canada's forces in World War II"
    ],
    "answerIndex": 1,
    "explanation": "Tommy Douglas (1904–1986) was the Premier of Saskatchewan (1944–1961) and leader of the CCF (predecessor to the NDP). He introduced North America's first universal publicly funded hospital insurance plan in Saskatchewan in 1947 — the model for Canada's national Medicare system. He was voted the Greatest Canadian in a national poll."
  },
  {
    "id": "q229",
    "topic": "Canada's History",
    "subtopic": "Notable Canadians",
    "question": "Whose portrait appears on the Canadian $10 bill?",
    "options": [
      "Sir Wilfrid Laurier",
      "Sir Robert Borden",
      "Sir John A. Macdonald",
      "Pierre Elliott Trudeau"
    ],
    "answerIndex": 2,
    "explanation": "Sir John A. Macdonald, Canada's first Prime Minister and a Father of Confederation, is depicted on the Canadian $10 bill. His portrait has appeared on the $10 bill for many years as recognition of his central role in creating the country."
  },
  {
    "id": "q230",
    "topic": "Canada's History",
    "subtopic": "Notable Canadians",
    "question": "Whose portrait appears on the Canadian $5 bill?",
    "options": [
      "Sir John A. Macdonald",
      "Sir Wilfrid Laurier",
      "John Diefenbaker",
      "Lester Pearson"
    ],
    "answerIndex": 1,
    "explanation": "Sir Wilfrid Laurier, Canada's first French-Canadian Prime Minister, appears on the Canadian $5 bill. He served from 1896 to 1911 and is celebrated as one of Canada's greatest Prime Ministers."
  },
  {
    "id": "q231",
    "topic": "Canada's History",
    "subtopic": "Modern Era",
    "question": "What did Lester B. Pearson win the Nobel Peace Prize for in 1957?",
    "options": [
      "Negotiating Canada's free trade agreement with the United States",
      "His role in resolving the Suez Crisis through the creation of the first United Nations peacekeeping force",
      "Introducing the Canadian Charter of Rights and Freedoms",
      "Ending the Korean War through diplomatic negotiations"
    ],
    "answerIndex": 1,
    "explanation": "Lester B. Pearson (later Prime Minister, 1963–1968) won the Nobel Peace Prize in 1957 for his creative resolution of the Suez Crisis, during which he proposed the creation of a United Nations Emergency Force — the world's first modern UN peacekeeping force."
  },
  {
    "id": "q232",
    "topic": "Canada's History",
    "subtopic": "Modern Era",
    "question": "What was the 'Quiet Revolution' (Révolution tranquille) in Quebec?",
    "options": [
      "Quebec's peaceful separation from Canada in the 1960s",
      "A period of rapid social, political, and economic change in Quebec during the 1960s, involving secularization and the rise of Quebec nationalism",
      "A period of quiet diplomacy between Quebec and Ottawa in the 1980s",
      "The introduction of French-language laws in Quebec schools"
    ],
    "answerIndex": 1,
    "explanation": "The Quiet Revolution was a major period of rapid change in Quebec during the 1960s. The Quebec government took control of education and health care from the Catholic Church, expanded the role of the state, promoted French-Canadian culture, and gave rise to a modern Quebec identity and separatist movement."
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
    topic = "Canada's History"
    count = len([q for q in existing if q['topic'] == topic])
    print(f"Added {added} questions. '{topic}' now has {count} questions. Total: {len(existing)}")

if __name__ == '__main__':
    main()
