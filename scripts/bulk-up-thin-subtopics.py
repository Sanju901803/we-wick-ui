#!/usr/bin/env python3
"""Add 4+ questions to every thin (1-2 question) subtopic, sourced from Discover Canada."""
import json, os

script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_dir, '..', 'src', 'assets', 'data', 'questions.json')

with open(data_path) as f:
    questions = json.load(f)

existing_texts = {q['question'].strip().lower() for q in questions}
max_id = max(int(q['id'][1:]) for q in questions)
next_id = max_id + 1

new_questions = [

    # ===== Canada's History - Aboriginal Peoples (existing: 1) =====
    {
        "topic": "Canada's History",
        "subtopic": "Aboriginal Peoples",
        "question": "Which Aboriginal group in Canada were nomadic hunters who traditionally followed the bison (buffalo) herds?",
        "options": ["Inuit", "Cree", "Sioux", "Huron-Wendat"],
        "answerIndex": 2,
        "explanation": "The Sioux were nomadic, following the bison (buffalo) herds across the plains. The Huron-Wendat were farmers and hunters near the Great Lakes, the Cree and Dene were hunter-gatherers of the Northwest, and the Inuit lived off Arctic wildlife."
    },
    {
        "topic": "Canada's History",
        "subtopic": "Aboriginal Peoples",
        "question": "Which Aboriginal people of Canada lived off Arctic wildlife and adapted to one of the harshest environments on earth?",
        "options": ["Cree", "Sioux", "Huron-Wendat", "Inuit"],
        "answerIndex": 3,
        "explanation": "The Inuit lived off Arctic wildlife. Their knowledge of the land, sea and wildlife enabled them to adapt to the harsh Arctic environment."
    },
    {
        "topic": "Canada's History",
        "subtopic": "Aboriginal Peoples",
        "question": "What was the federal government's policy regarding Aboriginal children from the 1800s until the 1980s?",
        "options": [
            "Granting them full voting rights in all elections",
            "Placing them in residential schools to educate and assimilate them into mainstream Canadian culture",
            "Giving them special tax exemptions",
            "Providing free university education"
        ],
        "answerIndex": 1,
        "explanation": "From the 1800s until the 1980s, the federal government placed many Aboriginal children in residential schools to educate and assimilate them into mainstream Canadian culture. The schools were poorly funded and inflicted hardship on the students."
    },
    {
        "topic": "Canada's History",
        "subtopic": "Aboriginal Peoples",
        "question": "In what year did the Government of Canada formally apologize to former residential school students?",
        "options": ["1998", "2003", "2008", "2015"],
        "answerIndex": 2,
        "explanation": "In 2008, the Government of Canada formally apologized to the former students of residential schools for the hardship they experienced."
    },

    # ===== Canada's History - Aboriginal Rights (existing: 1) =====
    {
        "topic": "Canada's History",
        "subtopic": "Aboriginal Rights",
        "question": "Which British monarch issued the Royal Proclamation of 1763 that guaranteed Aboriginal territorial rights?",
        "options": ["King George II", "King George III", "King Charles II", "King William IV"],
        "answerIndex": 1,
        "explanation": "The Royal Proclamation of 1763 was issued by King George III. It first guaranteed Aboriginal territorial rights and established the basis for negotiating treaties with newcomers."
    },
    {
        "topic": "Canada's History",
        "subtopic": "Aboriginal Rights",
        "question": "Where are Aboriginal and treaty rights officially enshrined in Canada?",
        "options": ["The Indian Act", "The Canadian Constitution", "The Quebec Act", "The British North America Act"],
        "answerIndex": 1,
        "explanation": "Aboriginal and treaty rights are in the Canadian Constitution. Territorial rights were first guaranteed through the Royal Proclamation of 1763 by King George III."
    },
    {
        "topic": "Canada's History",
        "subtopic": "Aboriginal Rights",
        "question": "What was a major reason why large numbers of Aboriginal people died after European contact?",
        "options": [
            "Warfare with settlers",
            "Forced relocations to northern territories",
            "European diseases to which they lacked immunity",
            "Starvation due to overhunting by Europeans"
        ],
        "answerIndex": 2,
        "explanation": "Large numbers of Aboriginal people died of European diseases to which they lacked immunity. This was one of the most devastating consequences of European contact."
    },
    {
        "topic": "Canada's History",
        "subtopic": "Aboriginal Rights",
        "question": "What characterized the relationship between Aboriginals and Europeans in the first 200 years of coexistence?",
        "options": [
            "Constant warfare and conflict",
            "Complete separation with no interaction",
            "Strong economic, religious and military bonds",
            "Aboriginal dominance over European settlers"
        ],
        "answerIndex": 2,
        "explanation": "Aboriginals and Europeans formed strong economic, religious and military bonds in the first 200 years of coexistence, which laid the foundations of Canada."
    },

    # ===== Canada's History - Acadians (existing: 1) =====
    {
        "topic": "Canada's History",
        "subtopic": "Acadians",
        "question": "When did French colonists (ancestors of the Acadians) begin settling in what are now the Maritime provinces?",
        "options": ["1534", "1604", "1670", "1713"],
        "answerIndex": 1,
        "explanation": "The Acadians are the descendants of French colonists who began settling in what are now the Maritime provinces in 1604. Pierre de Monts and Samuel de Champlain established the first European settlement north of Florida at Port-Royal."
    },
    {
        "topic": "Canada's History",
        "subtopic": "Acadians",
        "question": "During which years did the Great Upheaval — the deportation of Acadians — occur?",
        "options": ["1713 to 1730", "1755 to 1763", "1776 to 1783", "1812 to 1815"],
        "answerIndex": 1,
        "explanation": "Between 1755 and 1763, during the war between Britain and France, more than two-thirds of the Acadians were deported from their homeland. This ordeal is known as the Great Upheaval."
    },
    {
        "topic": "Canada's History",
        "subtopic": "Acadians",
        "question": "What portion of Acadians were deported during the Great Upheaval?",
        "options": ["About one-quarter", "About one-third", "More than two-thirds", "Almost all"],
        "answerIndex": 2,
        "explanation": "Between 1755 and 1763, more than two-thirds of the Acadians were deported from their homeland during the Great Upheaval."
    },
    {
        "topic": "Canada's History",
        "subtopic": "Acadians",
        "question": "Despite the Great Upheaval, what has happened to Acadian culture today?",
        "options": [
            "It has been completely assimilated into English-Canadian culture",
            "It has survived and is flourishing as a lively part of French-speaking Canada",
            "It exists only in museums and historical archives",
            "It merged with Québécois culture"
        ],
        "answerIndex": 1,
        "explanation": "Despite the Great Upheaval, the Acadians survived and maintained their unique identity. Today, Acadian culture is flourishing and is a lively part of French-speaking Canada."
    },

    # ===== Canada's History - Early Peoples (existing: 1) =====
    {
        "topic": "Canada's History",
        "subtopic": "Early Peoples",
        "question": "What is the name of the Viking settlement in Newfoundland that is a UNESCO World Heritage site?",
        "options": ["Fort Garry", "L'Anse aux Meadows", "Port-Royal", "Fort Henry"],
        "answerIndex": 1,
        "explanation": "The Vikings from Iceland colonized Greenland 1,000 years ago and also reached Labrador and the island of Newfoundland. The remains of their settlement, L'Anse aux Meadows, are a World Heritage site."
    },
    {
        "topic": "Canada's History",
        "subtopic": "Early Peoples",
        "question": "For which country did John Cabot claim the 'New Founde Land' when he arrived in 1497?",
        "options": ["France", "Spain", "Portugal", "England"],
        "answerIndex": 3,
        "explanation": "John Cabot, an Italian immigrant to England, claimed the 'New Founde Land' for England when he set foot on Newfoundland or Cape Breton Island in 1497."
    },
    {
        "topic": "Canada's History",
        "subtopic": "Early Peoples",
        "question": "When did English settlement in Canada begin?",
        "options": ["1497", "1534", "1610", "1670"],
        "answerIndex": 2,
        "explanation": "Although John Cabot arrived in 1497, English settlement did not begin until 1610. France had already established its first permanent settlement at Port-Royal in Acadia in 1604."
    },
    {
        "topic": "Canada's History",
        "subtopic": "Early Peoples",
        "question": "Who were the Huron-Wendat people, and where did they live?",
        "options": [
            "Nomadic hunters of the Arctic",
            "Farmers and hunters of the Great Lakes region",
            "Hunter-gatherers of the Northwest",
            "Coastal fishermen of the West Coast"
        ],
        "answerIndex": 1,
        "explanation": "The Huron-Wendat of the Great Lakes region, like the Iroquois, were farmers and hunters. Different Aboriginal groups across Canada had very different ways of life."
    },

    # ===== Canada's History - French Canada (existing: 1) =====
    {
        "topic": "Canada's History",
        "subtopic": "French Canada",
        "question": "What were French-speaking Catholic inhabitants of colonial Quebec known as?",
        "options": ["Loyalists", "Habitants or Canadiens", "Voyageurs", "Coureurs des bois"],
        "answerIndex": 1,
        "explanation": "The French-speaking Catholic people of colonial Quebec were known as 'habitants' or 'Canadiens.' They strove to preserve their way of life under British rule after the British conquest of 1759."
    },
    {
        "topic": "Canada's History",
        "subtopic": "French Canada",
        "question": "Which legal system did the Quebec Act of 1774 restore for French Canadians?",
        "options": ["British civil law", "Scottish common law", "French civil law", "Roman law"],
        "answerIndex": 2,
        "explanation": "The Quebec Act of 1774 restored French civil law while maintaining British criminal law. This was an important accommodation for the French-speaking Catholic population of Quebec."
    },
    {
        "topic": "Canada's History",
        "subtopic": "French Canada",
        "question": "Which historical governor famously refused to surrender Quebec to the English in 1690, saying his reply would come 'from the mouths of my cannons'?",
        "options": ["Samuel de Champlain", "Sir Guy Carleton", "Count Frontenac", "Jean Talon"],
        "answerIndex": 2,
        "explanation": "Count Frontenac refused to surrender Quebec to the English in 1690, saying: 'My only reply will be from the mouths of my cannons!' He was one of the great leaders who built New France."
    },
    {
        "topic": "Canada's History",
        "subtopic": "French Canada",
        "question": "What did the Quebec Act of 1774 allow for Catholics in Quebec that was not then allowed in Britain?",
        "options": [
            "The right to own property",
            "Religious freedom and the right to hold public office",
            "The right to vote in elections",
            "Freedom of speech"
        ],
        "answerIndex": 1,
        "explanation": "The Quebec Act of 1774 allowed religious freedom for Catholics and permitted them to hold public office, a practice not then allowed in Britain. It was one of the constitutional foundations of Canada."
    },

    # ===== Canada's History - French-English Relations (existing: 1) =====
    {
        "topic": "Canada's History",
        "subtopic": "French-English Relations",
        "question": "In what year did the British defeat the French in the Battle of the Plains of Abraham?",
        "options": ["1713", "1745", "1759", "1775"],
        "answerIndex": 2,
        "explanation": "In 1759, the British defeated the French in the Battle of the Plains of Abraham at Québec City, marking the end of France's empire in America."
    },
    {
        "topic": "Canada's History",
        "subtopic": "French-English Relations",
        "question": "Who were the two commanders killed leading their troops at the Battle of the Plains of Abraham?",
        "options": [
            "Sir Isaac Brock and Chief Tecumseh",
            "Brigadier James Wolfe and the Marquis de Montcalm",
            "General Currie and General Ross",
            "Samuel de Champlain and Lord Dorchester"
        ],
        "answerIndex": 1,
        "explanation": "The commanders of both armies, Brigadier James Wolfe (British) and the Marquis de Montcalm (French), were both killed leading their troops in the Battle of the Plains of Abraham."
    },
    {
        "topic": "Canada's History",
        "subtopic": "French-English Relations",
        "question": "What did the Official Languages Act of 1969 establish?",
        "options": [
            "French as Canada's sole official language",
            "English as Canada's sole official language",
            "Equality between French and English in Parliament and the Government of Canada",
            "Mandatory French education in all provinces"
        ],
        "answerIndex": 2,
        "explanation": "Parliament passed the Official Languages Act in 1969. It established equality between French and English in Parliament, the Government of Canada and institutions subject to the Act."
    },
    {
        "topic": "Canada's History",
        "subtopic": "French-English Relations",
        "question": "What did the Battle of the Plains of Abraham (1759) mark in North American history?",
        "options": [
            "The founding of New France",
            "The end of France's empire in North America",
            "The beginning of Confederation",
            "The defeat of Napoleon Bonaparte"
        ],
        "answerIndex": 1,
        "explanation": "The British defeated the French in the Battle of the Plains of Abraham at Québec City in 1759, marking the end of France's empire in America."
    },

    # ===== Canada's History - Great Depression (existing: 1) =====
    {
        "topic": "Canada's History",
        "subtopic": "Great Depression",
        "question": "What event triggered the Great Depression in Canada?",
        "options": ["World War I ending in 1918", "The stock market crash of 1929", "A severe drought in 1925", "The collapse of the fur trade"],
        "answerIndex": 1,
        "explanation": "The stock market crash of 1929 led to the Great Depression, also called the 'Dirty Thirties.' It caused widespread unemployment and economic hardship across Canada."
    },
    {
        "topic": "Canada's History",
        "subtopic": "Great Depression",
        "question": "What was Canada's peak unemployment rate during the Great Depression?",
        "options": ["10%", "17%", "27%", "40%"],
        "answerIndex": 2,
        "explanation": "Unemployment reached 27% in 1933 during the Great Depression. Many businesses were wiped out and farmers in Western Canada were hit hardest by low grain prices and a terrible drought."
    },
    {
        "topic": "Canada's History",
        "subtopic": "Great Depression",
        "question": "Which financial institution was created in 1934 to manage the money supply and bring stability to Canada's financial system?",
        "options": ["The Toronto Stock Exchange", "The Royal Bank of Canada", "The Bank of Canada", "The Montreal Stock Exchange"],
        "answerIndex": 2,
        "explanation": "The Bank of Canada, a central bank to manage the money supply and bring stability to the financial system, was created in 1934 during the Great Depression."
    },
    {
        "topic": "Canada's History",
        "subtopic": "Great Depression",
        "question": "Who was hardest hit by the Great Depression in Canada?",
        "options": [
            "Fishermen in Atlantic Canada",
            "Farmers in Western Canada",
            "Factory workers in Central Canada",
            "Fur traders in the North"
        ],
        "answerIndex": 1,
        "explanation": "Farmers in Western Canada were hit hardest by the Great Depression due to low grain prices and a terrible drought. There was growing demand for a social safety net including minimum wages and unemployment insurance."
    },

    # ===== Canada's History - Indigenous Peoples (existing: 1) =====
    {
        "topic": "Canada's History",
        "subtopic": "Indigenous Peoples",
        "question": "What are Canada's three founding peoples?",
        "options": [
            "English, French, and German",
            "Aboriginal, French, and British",
            "Inuit, Métis, and First Nations",
            "Indigenous, European, and Asian"
        ],
        "answerIndex": 1,
        "explanation": "To understand what it means to be Canadian, it is important to know about our three founding peoples — Aboriginal, French and British."
    },
    {
        "topic": "Canada's History",
        "subtopic": "Indigenous Peoples",
        "question": "From where are the ancestors of Aboriginal peoples believed to have migrated to Canada?",
        "options": ["Europe", "Africa", "Asia", "South America"],
        "answerIndex": 2,
        "explanation": "The ancestors of Aboriginal peoples are believed to have migrated from Asia many thousands of years ago. They were well established here long before explorers from Europe first came to North America."
    },
    {
        "topic": "Canada's History",
        "subtopic": "Indigenous Peoples",
        "question": "What are the three distinct groups that make up Canada's Aboriginal peoples today?",
        "options": [
            "Inuit, Huron, and Cree",
            "First Nations, Métis, and Inuit",
            "Mohawk, Sioux, and Algonquin",
            "Plains, Woodland, and Arctic peoples"
        ],
        "answerIndex": 1,
        "explanation": "Today, the term Aboriginal peoples refers to three distinct groups: First Nations (formerly called Indian), Inuit, and Métis. About 65% are First Nations, 30% are Métis, and 4% are Inuit."
    },
    {
        "topic": "Canada's History",
        "subtopic": "Indigenous Peoples",
        "question": "What language do the Métis people speak as their own dialect?",
        "options": ["Cree", "Inuktitut", "Michif", "Algonquin"],
        "answerIndex": 2,
        "explanation": "The Métis are a distinct people of mixed Aboriginal and European ancestry who come from both French- and English-speaking backgrounds and speak their own dialect called Michif."
    },

    # ===== Canada's History - Loyalists (existing: 1) =====
    {
        "topic": "Canada's History",
        "subtopic": "Loyalists",
        "question": "Approximately how many Loyalists fled to Canada after the American Revolution?",
        "options": ["More than 5,000", "More than 15,000", "More than 40,000", "More than 100,000"],
        "answerIndex": 2,
        "explanation": "More than 40,000 people loyal to the Crown, called 'Loyalists,' fled the oppression of the American Revolution to settle in Nova Scotia and Quebec."
    },
    {
        "topic": "Canada's History",
        "subtopic": "Loyalists",
        "question": "Who led thousands of Loyalist Mohawk Indians into Canada after the American Revolution?",
        "options": ["Chief Tecumseh", "Joseph Brant", "Sir Guy Carleton", "Chief Pontiac"],
        "answerIndex": 1,
        "explanation": "Joseph Brant led thousands of Loyalist Mohawk Indians into Canada when Loyalists fled the American Revolution."
    },
    {
        "topic": "Canada's History",
        "subtopic": "Loyalists",
        "question": "What did the Constitutional Act of 1791 do to the Province of Quebec?",
        "options": [
            "Made it a fully independent colony",
            "Divided it into Upper Canada and Lower Canada",
            "Merged it with Nova Scotia",
            "Gave it responsible government"
        ],
        "answerIndex": 1,
        "explanation": "The Constitutional Act of 1791 divided the Province of Quebec into Upper Canada (mainly Loyalist, Protestant and English-speaking) and Lower Canada (heavily Catholic and French-speaking). It also granted legislative assemblies elected by the people."
    },
    {
        "topic": "Canada's History",
        "subtopic": "Loyalists",
        "question": "What diverse backgrounds did the Loyalists come from?",
        "options": [
            "Only British Protestant settlers",
            "Mainly wealthy landowners from Virginia",
            "Dutch, German, British, Scandinavian, Aboriginal and other origins with various religious backgrounds",
            "Mostly French Catholic settlers"
        ],
        "answerIndex": 2,
        "explanation": "The Loyalists came from Dutch, German, British, Scandinavian, Aboriginal and other origins and from Presbyterian, Anglican, Baptist, Methodist, Jewish, Quaker, and Catholic religious backgrounds. About 3,000 were black Loyalists."
    },

    # ===== Canada's History - Railways (existing: 1) =====
    {
        "topic": "Canada's History",
        "subtopic": "Railways",
        "question": "Why did British Columbia agree to join Confederation in 1871?",
        "options": [
            "Ottawa promised to give BC special fishing rights",
            "Ottawa promised to build a railway to the West Coast",
            "Ottawa promised to pay off BC's debts",
            "BC was given control of the fur trade"
        ],
        "answerIndex": 1,
        "explanation": "British Columbia joined Canada in 1871 after Ottawa promised to build a railway to the West Coast. The Canadian Pacific Railway was completed in 1885."
    },
    {
        "topic": "Canada's History",
        "subtopic": "Railways",
        "question": "Who drove the last spike of the Canadian Pacific Railway on November 7, 1885?",
        "options": ["Sir John A. Macdonald", "Sir Wilfrid Laurier", "Donald Smith (Lord Strathcona)", "Sir George-Étienne Cartier"],
        "answerIndex": 2,
        "explanation": "On November 7, 1885, Donald Smith (Lord Strathcona), the Scottish-born director of the Canadian Pacific Railway (CPR), drove the last spike, completing a powerful symbol of national unity."
    },
    {
        "topic": "Canada's History",
        "subtopic": "Railways",
        "question": "What discriminatory policy did Canada impose on Chinese immigrants who helped build the CPR?",
        "options": [
            "Deportation after the railway was completed",
            "A race-based entry fee called the Head Tax",
            "Forced labour without any wages",
            "Denial of Canadian citizenship permanently"
        ],
        "answerIndex": 1,
        "explanation": "After the railway was built with Chinese labour, the Chinese were subject to discrimination, including the Head Tax, a race-based entry fee. The Government of Canada apologized for this discriminatory policy in 2006."
    },
    {
        "topic": "Canada's History",
        "subtopic": "Railways",
        "question": "In what year did the Government of Canada apologize for the Chinese Head Tax?",
        "options": ["1988", "1998", "2006", "2012"],
        "answerIndex": 2,
        "explanation": "The Government of Canada apologized in 2006 for the discriminatory Head Tax policy imposed on Chinese immigrants who helped build the Canadian Pacific Railway."
    },

    # ===== Canada's History - Métis and Riel (existing: 1) =====
    {
        "topic": "Canada's History",
        "subtopic": "Métis and Riel",
        "question": "What did Louis Riel do in 1869 when Canada took over the northwest from the Hudson's Bay Company without consulting the Métis?",
        "options": [
            "Peacefully negotiated land rights",
            "Led an armed uprising and seized Fort Garry",
            "Fled to the United States immediately",
            "Petitioned the British Parliament for protection"
        ],
        "answerIndex": 1,
        "explanation": "When Canada took over the vast northwest region from the Hudson's Bay Company in 1869, the 12,000 Métis were not consulted. In response, Louis Riel led an armed uprising and seized Fort Garry, the territorial capital."
    },
    {
        "topic": "Canada's History",
        "subtopic": "Métis and Riel",
        "question": "What new province was established as a result of the first Métis uprising of 1869–70?",
        "options": ["Saskatchewan", "Alberta", "Manitoba", "British Columbia"],
        "answerIndex": 2,
        "explanation": "After Louis Riel's first uprising, Ottawa sent soldiers to retake Fort Garry and established a new province: Manitoba (1870). Riel fled to the United States."
    },
    {
        "topic": "Canada's History",
        "subtopic": "Métis and Riel",
        "question": "Who was the Métis' greatest military leader during the 1885 rebellion in Saskatchewan?",
        "options": ["Louis Riel", "Gabriel Dumont", "Chief Poundmaker", "Big Bear"],
        "answerIndex": 1,
        "explanation": "Gabriel Dumont was the Métis' greatest military leader during the 1885 rebellion in present-day Saskatchewan. Louis Riel was the political leader who was later executed for high treason."
    },
    {
        "topic": "Canada's History",
        "subtopic": "Métis and Riel",
        "question": "What police force did Prime Minister Macdonald establish in 1873 in response to unrest in the West?",
        "options": [
            "Royal Canadian Mounted Police",
            "North West Mounted Police",
            "Canadian Border Services",
            "Dominion Police"
        ],
        "answerIndex": 1,
        "explanation": "After the first Métis uprising, Prime Minister Macdonald established the North West Mounted Police (NWMP) in 1873 to pacify the West and assist in negotiations with Indigenous peoples. It later became the Royal Canadian Mounted Police (RCMP)."
    },

    # ===== Canada's Regions - Provinces and Territories (existing: 1) =====
    {
        "topic": "Canada's Regions",
        "subtopic": "Provinces and Territories",
        "question": "In which year did Newfoundland and Labrador join Confederation, making it the last province to do so?",
        "options": ["1905", "1931", "1949", "1967"],
        "answerIndex": 2,
        "explanation": "Newfoundland and Labrador joined Confederation in 1949, making it the last province to join. It was previously a separate British entity."
    },
    {
        "topic": "Canada's Regions",
        "subtopic": "Provinces and Territories",
        "question": "Which Canadian province is the birthplace of Confederation and is connected to the mainland by the Confederation Bridge?",
        "options": ["Nova Scotia", "New Brunswick", "Prince Edward Island", "Newfoundland"],
        "answerIndex": 2,
        "explanation": "Prince Edward Island (P.E.I.) is the birthplace of Confederation, connected to mainland Canada by the Confederation Bridge, one of the longest continuous multispan bridges in the world."
    },
    {
        "topic": "Canada's Regions",
        "subtopic": "Provinces and Territories",
        "question": "Which is the only officially bilingual province in Canada, where about one-third of the population lives and works in French?",
        "options": ["Quebec", "Ontario", "New Brunswick", "Manitoba"],
        "answerIndex": 2,
        "explanation": "New Brunswick is the only officially bilingual province. About one-third of the population lives and works in French, and it has a proud Loyalist and Acadian cultural heritage."
    },
    {
        "topic": "Canada's Regions",
        "subtopic": "Provinces and Territories",
        "question": "Which Canadian province has the largest French-speaking population outside of Quebec?",
        "options": ["New Brunswick", "Manitoba", "Ontario", "British Columbia"],
        "answerIndex": 2,
        "explanation": "Ontario has the largest French-speaking population outside of Quebec, with a proud history of preserving the French language and culture. Founded by United Empire Loyalists, Ontario is home to over 12 million people."
    },

    # ===== Canada's Regions - Quebec (existing: 1) =====
    {
        "topic": "Canada's Regions",
        "subtopic": "Quebec",
        "question": "What is Canada's main producer of pulp and paper?",
        "options": ["Ontario", "British Columbia", "Quebec", "New Brunswick"],
        "answerIndex": 2,
        "explanation": "Quebec is Canada's main producer of pulp and paper. The resources of the Canadian Shield, including vast forests, have helped Quebec develop important forestry industries."
    },
    {
        "topic": "Canada's Regions",
        "subtopic": "Quebec",
        "question": "What is Canada's largest producer of hydro-electricity?",
        "options": ["British Columbia", "Manitoba", "Ontario", "Quebec"],
        "answerIndex": 3,
        "explanation": "Quebec's huge supply of fresh water has made it Canada's largest producer of hydro-electricity."
    },
    {
        "topic": "Canada's Regions",
        "subtopic": "Quebec",
        "question": "What is Montreal's distinction in the French-speaking world?",
        "options": [
            "It is the largest French-speaking city in the world",
            "It is the second largest mainly French-speaking city in the world after Paris",
            "It is the oldest French-speaking city in the Americas",
            "It is the capital of Quebec"
        ],
        "answerIndex": 1,
        "explanation": "Montreal is Canada's second largest city and the second largest mainly French-speaking city in the world after Paris. It is famous for its cultural diversity."
    },
    {
        "topic": "Canada's Regions",
        "subtopic": "Quebec",
        "question": "What fraction of Quebec's nearly 8 million people speak French as their first language?",
        "options": ["About half", "About two-thirds", "More than three-quarters", "Virtually all"],
        "answerIndex": 2,
        "explanation": "Nearly eight million people live in Quebec, and more than three-quarters speak French as their first language. Most live along or near the St. Lawrence River."
    },

    # ===== Canada's Regions - Territories (existing: 1) =====
    {
        "topic": "Canada's Regions",
        "subtopic": "Territories",
        "question": "What is Yellowknife, the capital of the Northwest Territories, known as?",
        "options": [
            "The gold rush capital of Canada",
            "The diamond capital of North America",
            "The oil sands capital of the world",
            "The gateway to the Arctic"
        ],
        "answerIndex": 1,
        "explanation": "Yellowknife (population 20,000) is called the 'diamond capital of North America.' More than half the population of the NWT is Aboriginal (Dene, Inuit and Métis)."
    },
    {
        "topic": "Canada's Regions",
        "subtopic": "Territories",
        "question": "What is the coldest temperature ever recorded in Canada, set in the Yukon?",
        "options": ["-45°C", "-53°C", "-63°C", "-73°C"],
        "answerIndex": 2,
        "explanation": "Yukon holds the record for the coldest temperature ever recorded in Canada: -63°C."
    },
    {
        "topic": "Canada's Regions",
        "subtopic": "Territories",
        "question": "After whom is Iqaluit, the capital of Nunavut (formerly Frobisher Bay), named?",
        "options": [
            "Sir William Logan",
            "Martin Frobisher",
            "Robert Service",
            "Samuel Hearne"
        ],
        "answerIndex": 1,
        "explanation": "Iqaluit, formerly Frobisher Bay, is named after the English explorer Martin Frobisher, who penetrated the uncharted Arctic for Queen Elizabeth I in 1576."
    },
    {
        "topic": "Canada's Regions",
        "subtopic": "Territories",
        "question": "What is the Mackenzie River's distinction among North American river systems?",
        "options": [
            "It is the longest river in North America",
            "It is the second-longest river system in North America after the Mississippi",
            "It is the widest river in Canada",
            "It is the only river system that drains into three oceans"
        ],
        "answerIndex": 1,
        "explanation": "The Mackenzie River, at 4,200 kilometres, is the second-longest river system in North America after the Mississippi and drains an area of 1.8 million square kilometres in the Northwest Territories."
    },

    # ===== Canadian Symbols - Flag (existing: 1) =====
    {
        "topic": "Canadian Symbols",
        "subtopic": "Flag",
        "question": "What inspired the red-white-red pattern of the current Canadian flag?",
        "options": [
            "The British Union Jack",
            "The flag of the Royal Military College, Kingston",
            "The French tricolour",
            "The Hudson's Bay Company flag"
        ],
        "answerIndex": 1,
        "explanation": "The red-white-red pattern of the current Canadian flag comes from the flag of the Royal Military College, Kingston, founded in 1876."
    },
    {
        "topic": "Canadian Symbols",
        "subtopic": "Flag",
        "question": "What flag served as Canada's national flag for about 100 years before 1965?",
        "options": ["The Union Jack", "The Royal Standard", "The Canadian Red Ensign", "The French Tricolour"],
        "answerIndex": 2,
        "explanation": "The Canadian Red Ensign served as the Canadian flag for about 100 years before the current maple leaf flag was raised for the first time in 1965."
    },
    {
        "topic": "Canadian Symbols",
        "subtopic": "Flag",
        "question": "Since when have red and white been Canada's official national colours?",
        "options": ["1867", "1900", "1921", "1965"],
        "answerIndex": 2,
        "explanation": "Red and white had been colours of France and England since the Middle Ages and became the national colours of Canada since 1921, when King George V assigned them."
    },
    {
        "topic": "Canadian Symbols",
        "subtopic": "Flag",
        "question": "What is Canada's official Royal Flag?",
        "options": ["The Canadian Red Ensign", "The Union Jack", "The Royal Standard of Canada", "The Fleur-de-lys flag"],
        "answerIndex": 1,
        "explanation": "The Union Jack is Canada's official Royal Flag. The provinces and territories also have flags that embody their distinct traditions."
    },

    # ===== Canadian Symbols - Coat of Arms (existing: 2) =====
    {
        "topic": "Canadian Symbols",
        "subtopic": "Coat of Arms",
        "question": "After which event did Canada adopt its official coat of arms and national motto?",
        "options": ["Confederation in 1867", "The First World War", "The Second World War", "The signing of the Statute of Westminster"],
        "answerIndex": 1,
        "explanation": "As an expression of national pride after the First World War, Canada adopted an official coat of arms and a national motto, A Mari Usque Ad Mare ('from sea to sea')."
    },
    {
        "topic": "Canadian Symbols",
        "subtopic": "Coat of Arms",
        "question": "What symbols are contained in Canada's coat of arms?",
        "options": [
            "A maple leaf, a beaver, and a moose",
            "Symbols of England, France, Scotland and Ireland, plus red maple leaves",
            "The Crown, the fleur-de-lys, and the Union Jack",
            "A bear, an eagle, and a salmon"
        ],
        "answerIndex": 1,
        "explanation": "The coat of arms contains symbols of England, France, Scotland and Ireland as well as red maple leaves. Today the arms can be seen on dollar bills, government documents and public buildings."
    },
    {
        "topic": "Canadian Symbols",
        "subtopic": "Coat of Arms",
        "question": "Where can Canada's coat of arms be seen today?",
        "options": [
            "Only on Parliament Buildings",
            "Only on Canadian passports",
            "On dollar bills, government documents and public buildings",
            "On military uniforms only"
        ],
        "answerIndex": 2,
        "explanation": "Canada's coat of arms can be seen on dollar bills, government documents and public buildings across the country."
    },

    # ===== Canadian Symbols - Symbols (existing: 2) =====
    {
        "topic": "Canadian Symbols",
        "subtopic": "Symbols",
        "question": "When did French-Canadians first adopt the maple leaf as a symbol?",
        "options": ["In the 1600s", "In the 1700s", "In the 1800s", "In the 1900s"],
        "answerIndex": 1,
        "explanation": "The maple leaf is Canada's best-known symbol. Maple leaves were adopted as a symbol by French-Canadians in the 1700s and have appeared on Canadian uniforms and insignia since the 1850s."
    },
    {
        "topic": "Canadian Symbols",
        "subtopic": "Symbols",
        "question": "What does the Crown symbolize in Canada?",
        "options": [
            "Only the monarchy",
            "The state, including Parliament, the legislatures, courts, police services and the Canadian Forces",
            "The Prime Minister's authority",
            "Canada's ties to Great Britain only"
        ],
        "answerIndex": 1,
        "explanation": "The Crown is a symbol of government in Canada, representing the state including Parliament, the legislatures, the courts, police services and the Canadian Forces."
    },
    {
        "topic": "Canadian Symbols",
        "subtopic": "Symbols",
        "question": "Since when have maple leaves appeared on Canadian uniforms and insignia?",
        "options": ["Since the 1700s", "Since the 1850s", "Since Confederation in 1867", "Since the First World War"],
        "answerIndex": 1,
        "explanation": "Maple leaves have appeared on Canadian uniforms and insignia since the 1850s, and are also carved into the headstones of Canadian fallen soldiers buried overseas and in Canada."
    },

    # ===== Who We Are - English Canadians (existing: 1) =====
    {
        "topic": "Who We Are",
        "subtopic": "English Canadians",
        "question": "Which groups of settlers established the basic way of life in English-speaking Canada?",
        "options": [
            "Only English settlers from Britain",
            "English, Welsh, Scottish and Irish settlers from the 1600s to the 20th century",
            "American Loyalists and British soldiers only",
            "German, Dutch, and Scandinavian immigrants"
        ],
        "answerIndex": 1,
        "explanation": "The basic way of life in English-speaking areas was established by hundreds of thousands of English, Welsh, Scottish and Irish settlers, soldiers and migrants from the 1600s to the 20th century."
    },
    {
        "topic": "Who We Are",
        "subtopic": "English Canadians",
        "question": "What key phrase from the British North America Act of 1867 defines Canada's commitment to governance?",
        "options": [
            "'Life, Liberty and the Pursuit of Happiness'",
            "'Liberty, Equality, Fraternity'",
            "'Peace, Order, and Good Government'",
            "'Truth, Justice and Democracy'"
        ],
        "answerIndex": 2,
        "explanation": "Canada's institutions uphold a commitment to 'Peace, Order, and Good Government,' a key phrase in Canada's original constitutional document in 1867, the British North America Act."
    },
    {
        "topic": "Who We Are",
        "subtopic": "English Canadians",
        "question": "What type of constitutional tradition has Canada inherited, considered the oldest continuous one in the world?",
        "options": [
            "A republican tradition",
            "A constitutional monarchy",
            "A parliamentary democracy without a monarchy",
            "A federal republic"
        ],
        "answerIndex": 1,
        "explanation": "Canadians have inherited the oldest continuous constitutional tradition in the world. Canada is the only constitutional monarchy in North America."
    },

    # ===== Who We Are - Multiculturalism (existing: 1) =====
    {
        "topic": "Who We Are",
        "subtopic": "Multiculturalism",
        "question": "Since what decade have most immigrants to Canada come from Asian countries?",
        "options": ["Since the 1950s", "Since the 1960s", "Since the 1970s", "Since the 1990s"],
        "answerIndex": 2,
        "explanation": "Since the 1970s, most immigrants have come from Asian countries. Canada is often referred to as a land of immigrants, as millions of newcomers have helped build and defend Canadian society."
    },
    {
        "topic": "Who We Are",
        "subtopic": "Multiculturalism",
        "question": "What is the second most-spoken language at home in Vancouver and Toronto after English?",
        "options": ["French", "Punjabi", "Chinese languages", "Spanish"],
        "answerIndex": 2,
        "explanation": "Chinese languages are the second most-spoken at home, after English, in two of Canada's biggest cities. In Vancouver, 13% of the population speak Chinese languages at home; in Toronto, the number is 7%."
    },
    {
        "topic": "Who We Are",
        "subtopic": "Multiculturalism",
        "question": "What are the largest ethnic groups in Canada?",
        "options": [
            "English, French, German, Italian and Chinese",
            "British, French, Indigenous, and East Asian",
            "English, French, Scottish, Irish, German, Italian, Chinese, Aboriginal, Ukrainian, Dutch, South Asian and Scandinavian",
            "English, French, and Indigenous peoples only"
        ],
        "answerIndex": 2,
        "explanation": "The largest groups in Canada are the English, French, Scottish, Irish, German, Italian, Chinese, Aboriginal, Ukrainian, Dutch, South Asian and Scandinavian. Many ethnic and religious groups live and work in peace as proud Canadians."
    },

    # ===== Who We Are - Population (existing: 1) =====
    {
        "topic": "Who We Are",
        "subtopic": "Population",
        "question": "Although Canada has about 34 million people spread across a vast area, where do most Canadians live?",
        "options": ["In rural farming communities", "In the far North", "In cities", "Along the Pacific coast"],
        "answerIndex": 2,
        "explanation": "Canada has a population of about 34 million people. While the majority live in cities, Canadians also live in small towns, rural areas and everywhere in between."
    },
    {
        "topic": "Who We Are",
        "subtopic": "Population",
        "question": "Since when has the majority of Canadians been born in Canada rather than abroad?",
        "options": ["Since Confederation in 1867", "Since the 1800s", "Since the 1920s", "Since World War II"],
        "answerIndex": 1,
        "explanation": "The majority of Canadians were born in this country and this has been true since the 1800s. However, Canada is often referred to as a land of immigrants because millions of newcomers have helped build Canadian society."
    },
    {
        "topic": "Who We Are",
        "subtopic": "Population",
        "question": "Why is Canada often referred to as 'a land of immigrants'?",
        "options": [
            "Because Canada has no Indigenous population",
            "Because all Canadians must be born abroad to become citizens",
            "Because over the past 200 years, millions of newcomers have helped build and defend the Canadian way of life",
            "Because immigration is the only path to Canadian citizenship"
        ],
        "answerIndex": 2,
        "explanation": "Canada is often referred to as a land of immigrants because, over the past 200 years, millions of newcomers have helped to build and defend the Canadian way of life."
    },

    # ===== Who We Are - Regions (existing: 1) =====
    {
        "topic": "Who We Are",
        "subtopic": "Regions",
        "question": "What is Central Canada (southern Ontario and Quebec) known as?",
        "options": [
            "The breadbasket of Canada",
            "The industrial and manufacturing heartland of Canada",
            "Canada's Pacific gateway",
            "The agricultural heartland of Canada"
        ],
        "answerIndex": 1,
        "explanation": "More than half the people in Canada live in cities and towns near the Great Lakes and the St. Lawrence River in southern Quebec and Ontario, known as Central Canada and the industrial and manufacturing heartland."
    },
    {
        "topic": "Who We Are",
        "subtopic": "Regions",
        "question": "Together, Ontario and Quebec produce more than what fraction of all Canadian manufactured goods?",
        "options": ["One-quarter", "One-half", "Two-thirds", "Three-quarters"],
        "answerIndex": 3,
        "explanation": "Together, Ontario and Quebec produce more than three-quarters of all Canadian manufactured goods, making Central Canada the industrial heartland of the country."
    },
    {
        "topic": "Who We Are",
        "subtopic": "Regions",
        "question": "Where do more than half of all Canadians live?",
        "options": [
            "In the Prairie Provinces",
            "In the Northern Territories",
            "In cities and towns near the Great Lakes and the St. Lawrence River in Central Canada",
            "Along the Pacific coast in British Columbia"
        ],
        "answerIndex": 2,
        "explanation": "More than half the people in Canada live in cities and towns near the Great Lakes and the St. Lawrence River in southern Quebec and Ontario, known as Central Canada."
    },

    # ===== Who We Are - Religion (existing: 1) =====
    {
        "topic": "Who We Are",
        "subtopic": "Religion",
        "question": "After Catholics, what is the next largest religious group in Canada?",
        "options": ["Muslims", "Various Protestant churches", "Jews", "Sikhs"],
        "answerIndex": 1,
        "explanation": "The great majority of Canadians identify as Christians. The largest religious affiliation is Catholic, followed by various Protestant churches."
    },
    {
        "topic": "Who We Are",
        "subtopic": "Religion",
        "question": "Which religious groups are growing in numbers in Canada alongside traditional Christian communities?",
        "options": [
            "Only Muslims",
            "Muslims, Jews, Hindus, Sikhs and members of other religions, as well as people with no religion",
            "Only Hindus and Buddhists",
            "Only those with no religion"
        ],
        "answerIndex": 1,
        "explanation": "The numbers of Muslims, Jews, Hindus, Sikhs and members of other religions, as well as people who state 'no religion,' are growing in Canada alongside the Christian majority."
    },
    {
        "topic": "Who We Are",
        "subtopic": "Religion",
        "question": "What has been Canada's traditional role in partnering with faith communities?",
        "options": [
            "To establish a state religion",
            "To tax religious organizations",
            "To promote social welfare, provide schools and health care, resettle refugees, and uphold religious freedom",
            "To ensure all immigrants adopt Canadian religious practices"
        ],
        "answerIndex": 2,
        "explanation": "In Canada the state has traditionally partnered with faith communities to promote social welfare, harmony and mutual respect; to provide schools and health care; to resettle refugees; and to uphold religious freedom, religious expression and freedom of conscience."
    },
]

added = 0
skipped = 0
for q in new_questions:
    if q['question'].strip().lower() in existing_texts:
        print(f'SKIP (duplicate): {q["question"][:70]}')
        skipped += 1
        continue
    q['id'] = f'q{next_id}'
    questions.append(q)
    existing_texts.add(q['question'].strip().lower())
    next_id += 1
    added += 1

with open(data_path, 'w') as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)

print(f'\nDone! Added {added} questions, skipped {skipped}.')
print(f'Total questions: {len(questions)}')
