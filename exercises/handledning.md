---
layout: default
---
# För lärare
Denna handledning riktar sig till lärare på högstadiet och gymnasiet, samt till pedagoger vid Science Centers.

## Plattformar

**Repl.it** är en online-programmeringsmiljö för flera olika språk. Vi använder [repl.it Python3](https://repl.it/languages/python3). Man kan köra anonymt på repl.it, men det är bättre att registrera ett konto. repl.it-övningarna använder ren python, och vill man använda en annan python-miljö så går det fint.

**Colab** är en online-programmeringsmiljö för Python där man använder "Jupyter notebooks". En Jupyter notebook innehåller både text, bilder och körbara kodrutor. Det gör det enkelt att kombinera uppgifter och förklaringar med koden. För att använda Colab behöver man ett google-konto.

## Pedagogiska ideer
* Repl.it-övningarna är avsedda att lära ut programmering, och använda miljödata-exempel för att göra uppgifterna intressanta. Målet är att eleverna ska förstå allt programmen gör.
* Colab-övningarna använder oftast en del färdiga funktioner och huvudmålet där är primärt att ge aha-upplevelser inom miljödata, och förståelse för *vad* man kan åstadkomma med programmering. Man lär sig också lite programmering, men de färdiga funktionerna förklaras inte.

## Hur mycket Python behöver du kunna?

Uppdragen kan göras utan förkunskaper om man har handledning. Som handledare är det bra om du kan enkel programmering i Python med variabler, tilldelningssatser, for-loopar, if-satser, funktioner, och listor. [Titta här för att se om du har lagom förkunskaper](prerequisites.md). Du kan också prova uppdragen direkt. Lösningsförslag ingår i de flesta av uppgifterna.

## Förberedelser inför en övning med elever

### Övningar med repl.it

* **Skriv helst ut övningen på papper till eleverna.**
  * Med övningen på en utskrift kan eleverna använda hela skärmen för programmering. Annars behöver de ett fönster för uppgiften och ett för programmeringen.
  * Det rekommenderas att eleverna arbetar i par - det räcker med en utskrift och en dator per par.
  * Med övningen på papper lockas eleverna inte att tjuvtitta på lösningarna som finns i utfällbara flikar.
  * Med övningen på papper måste eleverna skriva in all kod själv i programmeringsfönstret (i stället för att göra copy-paste), och de lär sig då mer.

* **På Science Center, starta datorerna i förväg** och skapa ett fönster med repl.it på varje dator, enligt instruktioner i övningen. Det går att köra anonymt på repl.it, så det behövs ingen inloggning.
* **I skolan har nog varje elev sin egen dator**, och det är enklast att de själva browsar till rätt plats på repl.it, enligt instruktioner i övningen. Om eleverna skaffar eget konto så sparas deras program automatiskt.

### Övningar med Jupyter notebooks i Colab

* För att köra Colab behöver man vara inloggad med personligt konto. Detta brukar fungera bra i skolor eftersom många skolor använder Google Gmail och alla elever/lärare har då konto.

## Själva övningen

* Låt eleverna arbeta två och två. Det är roligare, och de kan hjälpa varandra så att de inte fastnar så lätt.
* Introduktion om det är första gången ni kör en av uppgifterna:
    * Att det finns mkt data om miljön som finns tillgänglig på webben
    * Med programmering kan man analysera datan och förstå vad som händer i miljön.
    * Nu skall vi lära oss lite om programmering och se hur detta kan gå till.

### Övningar med repl.it

* Innan de sätter igång, använd projektor och visa dem hur de skriver ett enkelt program i repl.it och kör det. Det kan till exempel vara följande program:
```python
	x = 14 + 7
	print(x)
```
* Förklara vad som händer (ungefär så här mycket behöver de förstå om programmering för att kunna göra Väderdata A):
    * 14 och 7 läggs ihop och värdet (21) sparas i variabeln x.
    * Sedan skrivs värdet på x ut.
    * Förklara att en variabel är som en låda som kan innehålla ett värde. Vi kan kalla den vad vi vill.
* Förklara och visa att programmet körs när man trycker på Run.
* Om du vill kan ni göra första uppgifterna gemensamt. Diskutera vad man ska göra. Låt alla skriva in kod och prova. Efter en stund kan eleverna arbeta vidare mer självständigt och i sin egen takt.

### Övningar med Jupyter notebooks i Colab

För Kolcykeln och Avskogning, ta gärna upp ditt eget fönster på en projektor, och gå igenom de inledande mer teoretiska avsnitten tillsammans. När själva programmeringen börjar kan du låta dem börja arbeta själva (två och två).

## Några typiska problem och frågor som eleverna kan ha

### Relaterat till tangentbord
* Hittar inte hakparenteser `[]` på tangentbordet.
    * På Windows: håll nere Alt-Gr och tryck på tangent märkt med hakparentes.
    * På Mac: Håll nere Alt och tryck på vanlig parentes.
* Krullparenteser `{}`
    * På Windows: håll nere Alt-Gr och tryck på tangent märkt med krullparentes.
    * På Mac: Håll nere Shift-Alt och tryck på vanlig parentes.

### Relaterat till repl.it

* Första gången man försöker skriva i ett preparerat repl.it-fönster “tar” det inte. Det beror på att man först ser en Read-Only-version. När man börjar skriva kod så skapas en ny kopia som man kan editera. Sedan funkar det.
* Irriterande popup-fönster i repl.it. Dvs s.k. “Code completion”, eller “Code intelligence”. Man kan stänga av det under Settings (kugghjulet). Tryck på kugghjulet en gång till för att stänga Settings.
* Ibland försvinner plot-fönstret. Det brukar dyka upp igen om man klickar på filen (t.ex. keeling.png till vänster i fönstret.) Klicka sedan på main.py igen.
* Ibland tappar man kontakten med repl.it-servern. Man kan då behöva ladda om webbsidan. Om man kör utan inloggning tappar man dock då all kod man skrivit in.
* Vill kunna kommentera bort flera rader på en gång. Det finns en shortcut i repl.it för det. Med högerklick får man fram en meny med editeringskommandon och deras shortcuts. Där kan man se vad shortcut för “add line comment” och “remove line comment” är.

### Relaterat till Google Colab
* Om meny-alternativen för att köra kod är grå så måste man först trycka på `Connect`-knappen uppe till höger.
* Om något har gått fel och man tycker att allt ser rätt ut, och man inte förstår vad problemet är, så kan man prova att starta om genom att använda menyn `Runtime -> Restart and run all...`. Detta kan hjälpa speciellt när man kört kodrutorna i oordning, eller när man har experimenterat och råkat förstöra någon variabel som räknats ut tidigare. Genom att köra om från början kommer man ifrån sådana fel.
* Numren till vänster på kodrutorna visar i vilken ordning de har körts.

### Relaterat till själva Python-programmeringen

* Försöker göra variabelnamn med svenska tecken och blanktecken. Det fungerar inte. T.ex funkar inte:
```python
	vår fina sång = ["hej", "tomtegubbar", "slå", "i", "glasen"]
```
(Variabeln kan inte heta "vår fina sång": det går bra med svenska tecken och blanktecken i strängar, men inte i variabelnamn. Variabeln kan t.ex. heta "song" i stället.)

* Använder vanliga parenteser i stället för hakparenteser för listor. Rätt mycket av Väderdata A kan fungera ändå (det blir s.k. “tupler” i stället för listor). Men tupler kan inte ändras, så i uppgift Väderdata B, när man gör “append” på en lista, så fungerar det inte med tupler.

* Indentering av loopar. Speciellt för elever/personer som sett annan programmering med krullparenteser så kan det vara lite ovant och därför förvirrande att det räcker att indentera satserna inne i loopen.

## Andra frågor och svar

### Vilken typ av dator kan man använda?
Det bör fungera med Mac, Windows, Linux eller Chromebook.

### Kan man använda iPad?
Nej, tyvärr inget vidare (februari 2020). Du kan köra program, men det är mycket svårt att redigera dem, beroende på att det inte fungerar att göra välj/klippa/klistra i kodfönstren, vare sig i repl.it eller colab.

## Data till uppgifterna
För de flesta av uppdragen har vi preparerat datan så att den ska vara lättare att använda i programmeringen.

Ofta krävs det en hel del programmering för att hämta och förbehandla data.

Är du intresserad av hur vi har hämtat data och vill göra liknande egna uppgifter, se [vårt grundmaterial på github](https://github.com/lunduniversity/schoolprog-satellite) (webb-sidorna är genererade från detta grundmaterial). Då behöver du dock en hel del programmeringsvana.

Information om hur vi gjort för de olika uppgifterna finns i samma katalog som uppgiften, i en fil `CONTRIBUTING.md`. T.ex. finns information om hur SMHI-datan preparerats i [weatherdata/CONTRIBUTING.md](https://github.com/lunduniversity/schoolprog-satellite/blob/master/exercises/weatherdata/CONTRIBUTING.md).

## Workshops för lärare
Om du jobbar på science center och har workshops för lärare (eller om du är lärare och vill introducera andra lärare), så finns det lite presentationsmaterial på [denna google-drive-mapp](https://docs.google.com/document/d/1LGNCGpyUpq5lSGsrgoX9y2ufhaO8mYUnSVOUfgjyBBs/edit?usp=sharing). Börja med att titta på dokumentet [SSC handledning](https://docs.google.com/document/d/1LGNCGpyUpq5lSGsrgoX9y2ufhaO8mYUnSVOUfgjyBBs/edit?usp=sharing).
