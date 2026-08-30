#!/usr/bin/env python3
"""
Add new 'The Justice System' questions (q301–q335).
"""
import json, os

DATA_FILE = os.path.join(os.path.dirname(__file__), '../src/assets/data/questions.json')

NEW_QUESTIONS = [
  {
    "id": "q301",
    "topic": "The Justice System",
    "subtopic": "Courts",
    "question": "What is the highest court in Canada?",
    "options": [
      "The Federal Court of Canada",
      "The Superior Court of each province",
      "The Supreme Court of Canada",
      "The Court of Appeal for Ontario"
    ],
    "answerIndex": 2,
    "explanation": "The Supreme Court of Canada is the highest court in the country. It is the final court of appeal for all legal matters, including criminal, civil, and constitutional cases. It consists of nine judges, including a Chief Justice."
  },
  {
    "id": "q302",
    "topic": "The Justice System",
    "subtopic": "Law",
    "question": "What is the difference between criminal law and civil law?",
    "options": [
      "Criminal law deals with disputes between individuals; civil law deals with crimes against the state",
      "Criminal law deals with crimes against society and the state; civil law deals with disputes between individuals or organizations",
      "Criminal law only applies to adults; civil law applies to everyone",
      "Criminal law is federal; civil law is municipal"
    ],
    "answerIndex": 1,
    "explanation": "Criminal law deals with crimes that harm society — such as theft, assault, or murder — and is prosecuted by the state. Civil law deals with disputes between private parties — such as contract disputes or property damage — and usually results in compensation rather than imprisonment."
  },
  {
    "id": "q303",
    "topic": "The Justice System",
    "subtopic": "Rights Upon Arrest",
    "question": "What right do Canadians have when arrested?",
    "options": [
      "The right to be released without charge within 24 hours",
      "The right to know the reason for arrest and to speak to a lawyer immediately",
      "The right to refuse to answer any police questions without penalty",
      "The right to have a family member present during questioning"
    ],
    "answerIndex": 1,
    "explanation": "Under the Canadian Charter of Rights and Freedoms, anyone who is arrested has the right to be informed promptly of the reason for their arrest, and the right to retain and instruct a lawyer without delay. Police must also inform the person of this right."
  },
  {
    "id": "q304",
    "topic": "The Justice System",
    "subtopic": "Jury",
    "question": "What is the role of a jury in a criminal trial?",
    "options": [
      "To determine the sentence if the accused is found guilty",
      "To listen to the evidence presented and decide whether the accused is guilty or not guilty",
      "To advise the judge on points of law",
      "To investigate the crime and gather evidence"
    ],
    "answerIndex": 1,
    "explanation": "In a criminal trial, the jury is a group of citizens (usually 12) chosen to hear the evidence and decide whether the accused is guilty or not guilty. The judge then determines the sentence if the accused is found guilty. Jury duty is a civic responsibility."
  },
  {
    "id": "q305",
    "topic": "The Justice System",
    "subtopic": "Jury",
    "question": "Who is eligible for jury duty in Canada?",
    "options": [
      "Any resident of Canada over 18",
      "Only citizens who have lived in Canada for 10 years",
      "Adult Canadian citizens who meet provincial eligibility requirements",
      "Only citizens over 25 with post-secondary education"
    ],
    "answerIndex": 2,
    "explanation": "Jury duty is a civic responsibility for adult Canadian citizens. Exact eligibility rules vary by province but generally require being a Canadian citizen and being on the voters' list. Some people, such as lawyers and judges, may be exempted."
  },
  {
    "id": "q306",
    "topic": "The Justice System",
    "subtopic": "Law",
    "question": "What does 'innocent until proven guilty' mean in the Canadian justice system?",
    "options": [
      "Police must release a suspect unless they have video evidence",
      "Every person charged with a crime is presumed to be innocent, and the state must prove guilt beyond a reasonable doubt",
      "A person found innocent can never be charged again for the same crime",
      "An accused person is innocent until a jury is selected"
    ],
    "answerIndex": 1,
    "explanation": "'Innocent until proven guilty' is a fundamental principle of Canadian law. The Crown (state) bears the burden of proving, beyond a reasonable doubt, that the accused committed the crime. The accused does not have to prove their innocence."
  },
  {
    "id": "q307",
    "topic": "The Justice System",
    "subtopic": "Law",
    "question": "What does 'rule of law' mean in Canada?",
    "options": [
      "The government can make any rule it chooses without judicial review",
      "Everyone — including the government — is subject to the law, and no one is above it",
      "All laws must be approved by a public referendum",
      "Laws are enforced by the military, not the police"
    ],
    "answerIndex": 1,
    "explanation": "The rule of law means that everyone — including governments, police, and politicians — must obey the law. No one is above the law. The rule of law is a cornerstone of Canadian democracy and protects citizens from arbitrary use of power."
  },
  {
    "id": "q308",
    "topic": "The Justice System",
    "subtopic": "Courts",
    "question": "Who appoints federally appointed judges in Canada?",
    "options": [
      "The Prime Minister alone",
      "The Governor General on the advice of the Minister of Justice",
      "The Supreme Court of Canada",
      "Parliament by a majority vote"
    ],
    "answerIndex": 1,
    "explanation": "Federally appointed judges (including Supreme Court justices and judges of the Federal Court) are appointed by the Governor General on the advice of the Minister of Justice (and for the Supreme Court, the Prime Minister). Provincial court judges are appointed by provincial governments."
  },
  {
    "id": "q309",
    "topic": "The Justice System",
    "subtopic": "Law",
    "question": "What body is responsible for criminal law in Canada?",
    "options": [
      "Each province creates its own criminal laws",
      "Municipalities set criminal law based on local community standards",
      "The federal government — criminal law is an exclusive federal responsibility",
      "Criminal law is set jointly by federal and provincial governments"
    ],
    "answerIndex": 2,
    "explanation": "Criminal law is an exclusive federal responsibility under the Constitution Act, 1867. The Criminal Code of Canada (a federal law) applies uniformly across all provinces and territories. However, the provinces administer the courts that try criminal cases."
  },
  {
    "id": "q310",
    "topic": "The Justice System",
    "subtopic": "Courts",
    "question": "What is the Federal Court of Canada?",
    "options": [
      "The court that handles criminal cases involving federal employees",
      "A court that deals with federal matters including immigration, intellectual property, maritime law, and judicial review of federal decisions",
      "A court that hears appeals from all provincial courts",
      "The court where the Prime Minister and Cabinet are tried for misconduct"
    ],
    "answerIndex": 1,
    "explanation": "The Federal Court of Canada has jurisdiction over matters involving federal law — such as immigration and refugee decisions, intellectual property, maritime law, and judicial review of federal government decisions. It is not a general criminal court."
  },
  {
    "id": "q311",
    "topic": "The Justice System",
    "subtopic": "Rights Upon Arrest",
    "question": "What is habeas corpus?",
    "options": [
      "A legal requirement that all accused persons testify at trial",
      "The right of a person who is detained to challenge the lawfulness of their detention before a court",
      "The right to a fair and speedy trial",
      "A court order preventing police from searching your home"
    ],
    "answerIndex": 1,
    "explanation": "Habeas corpus is a fundamental legal right that allows a detained person to challenge the lawfulness of their detention before a court. If the court finds the detention unlawful, it must order the person's release. It is a key protection against arbitrary imprisonment."
  },
  {
    "id": "q312",
    "topic": "The Justice System",
    "subtopic": "Law",
    "question": "What is the purpose of bail in the Canadian justice system?",
    "options": [
      "Bail is a fine paid to the Crown when found guilty",
      "Bail allows a charged person to be released from custody while awaiting trial, usually with conditions",
      "Bail is a payment to the victim as compensation",
      "Bail is only available after conviction, as an alternative to prison"
    ],
    "answerIndex": 1,
    "explanation": "Bail allows a person who has been charged with a crime to be released from custody while awaiting trial. The accused may have to pay an amount of money or agree to conditions (such as curfew, no contact with victims). Bail reflects the principle of innocent until proven guilty."
  },
  {
    "id": "q313",
    "topic": "The Justice System",
    "subtopic": "Rights Upon Arrest",
    "question": "What does the right to 'remain silent' mean in Canada?",
    "options": [
      "A suspect must answer all police questions truthfully",
      "A person who is arrested is not required to answer police questions (except to provide their name in some circumstances)",
      "A convicted person does not have to give evidence at their sentencing hearing",
      "A witness in a civil case may refuse to testify"
    ],
    "answerIndex": 1,
    "explanation": "The right to remain silent (the right against self-incrimination) means that an arrested person is not required to answer police questions or incriminate themselves. The police must caution an arrested person of this right. Anything a person says voluntarily can be used in court."
  },
  {
    "id": "q314",
    "topic": "The Justice System",
    "subtopic": "Law",
    "question": "What is the difference between a summary conviction offence and an indictable offence?",
    "options": [
      "Summary offences are dealt with in federal courts; indictable offences are tried provincially",
      "Summary conviction offences are less serious crimes with lower penalties; indictable offences are more serious crimes with higher penalties",
      "Summary offences require a jury; indictable offences are decided by a judge alone",
      "There is no meaningful distinction — both are tried identically"
    ],
    "answerIndex": 1,
    "explanation": "The Criminal Code divides offences into summary conviction offences (less serious, tried quickly without a jury, lower penalties) and indictable offences (more serious crimes, longer process, higher penalties, may involve a jury). Some offences are 'hybrid' — the Crown chooses how to proceed."
  },
  {
    "id": "q315",
    "topic": "The Justice System",
    "subtopic": "Law",
    "question": "What is the role of a Crown Attorney (Crown Prosecutor)?",
    "options": [
      "To defend the accused against criminal charges",
      "To act as the judge's assistant in criminal matters",
      "To represent the state (Crown) and prosecute people accused of crimes on behalf of the public",
      "To manage the prison system"
    ],
    "answerIndex": 2,
    "explanation": "A Crown Attorney (Crown Prosecutor) is a lawyer employed by the government to present the prosecution's case against a person accused of a crime. They represent the Crown (the state) and the public interest, not any individual victim. They must act fairly and disclose evidence to the defence."
  },
  {
    "id": "q316",
    "topic": "The Justice System",
    "subtopic": "Law",
    "question": "What is legal aid in Canada?",
    "options": [
      "Free legal advice available only to immigrants applying for citizenship",
      "Government-funded legal assistance for people who cannot afford a lawyer",
      "A police service that provides information about legal rights upon request",
      "A community service where law students give free advice"
    ],
    "answerIndex": 1,
    "explanation": "Legal aid provides government-funded legal representation and advice for people who cannot afford a lawyer. It is especially important in criminal cases where a person's liberty is at stake. Legal aid is administered provincially and funded by provincial and federal governments."
  },
  {
    "id": "q317",
    "topic": "The Justice System",
    "subtopic": "Courts",
    "question": "What is the process for appealing a court decision in Canada?",
    "options": [
      "Appeals can only be made to the Governor General",
      "A party who disagrees with a court's decision can apply to a higher court to review and potentially overturn it",
      "All court decisions are automatically reviewed by the federal government",
      "Appeals are only available in civil cases, not criminal cases"
    ],
    "answerIndex": 1,
    "explanation": "In Canada's court system, a party who believes a lower court made an error of law or fact can appeal to a higher court. The court hierarchy runs from provincial trial courts to provincial courts of appeal, and finally to the Supreme Court of Canada (which grants leave to appeal in most cases)."
  },
  {
    "id": "q318",
    "topic": "The Justice System",
    "subtopic": "Law",
    "question": "Under Canadian law, at what age are young people tried under the Youth Criminal Justice Act rather than the adult Criminal Code?",
    "options": [
      "Under 14 years old",
      "Under 16 years old",
      "Under 18 years old",
      "Under 21 years old"
    ],
    "answerIndex": 2,
    "explanation": "In Canada, young people who are 12 to 17 years old at the time of an offence are dealt with under the Youth Criminal Justice Act (YCJA), which emphasizes rehabilitation over punishment. Those who are 18 or older are tried as adults under the Criminal Code."
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
    topic = "The Justice System"
    count = len([q for q in existing if q['topic'] == topic])
    print(f"Added {added} questions. '{topic}' now has {count} questions. Total: {len(existing)}")

if __name__ == '__main__':
    main()
