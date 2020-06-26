import json

#Läser in filen
with open("quiz.txt", encoding="utf8") as f:
  data = f.read()

#Delar upp var fråga för sig
questions = data.split(';;')

#Skapar en lista som ska innehålle en dict för varje fråga
jsonfile = []

#Går igenom alla frågorna
for question in questions:
  #Skapar en dict som tillhör en fråga
  qdict = {}

  #Splittar på ; för att på frågan och alla alternativ för sig
  quest_parts = question.split(';')

  #Lägger in frågan i dicten och tar bort den från quest_parts
  qdict["question"] = quest_parts.pop((0)).strip()

  #Skapar options, feedback och answers för denna fråga
  options = []
  feedback = {}
  answers = []

  #Går igenom varje alternativ för frågan.
  for part in quest_parts:

    #Delar upp alternativet i option,feedback och answer
    part = part.split(':')

    #Lägger till svarsalternativet till listan option
    options.append(part[0].strip())

    #Lägger till feedbacken för svarsalternativet i nyckel-värde tabellen feedback
    feedback[part[0].strip()] = part[1].strip()

    #Om alternativet stämmer läggs det till i answer
    if part[2].strip().lower() == "true":
      answers.append(part[0].strip())

  #Lägger till listorna till vår dict
  qdict["options"] = options
  qdict["feedback"] = feedback
  qdict["answer"] = answers

  #Lägger till vårt fråga till listan av frågor
  jsonfile.append(qdict)


#Skriver hela listan till en .json fil
with open("quiz.json", "w") as outfile:
  json.dump(jsonfile, outfile, indent=2)
