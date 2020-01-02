# Handledning
Handledning angående uppgifterna för miljödata.
Denna handledning riktar sig till lärare på högstadiet och gymnasiet, samt till pedagoger vid Science Centers.

## Pedagogiska ideer
* Repl.it-övningarna är avsedda att lära ut programmering, och använda miljödata-exempel för att göra uppgifterna intressanta.
* Jupyter/Colab-övningarna använder oftast lite mer avancerad programmering än repl.it-övningarna, och huvudmålet där är primärt att ge aha-upplevelser inom miljödata, och förståelse för vad man kan åstadkomma med programmering.

## Allmänna förberedelser

* Se till att du har lite egen programmeringsbakgrund i Python, se råd [här](prerequisites.md).

* Kör själv igenom den uppgift du vill att eleverna ska lösa. Lösningarna finns som utvikbara flikar i uppgiften.

## Förberedelser inför en övning med elever

* Skriv helst ut övningen på papper till eleverna. Då kan de använda hela skärmen för programmeringen, och de slipper krångla med att bläddra inom/mellan fönster.
* Eleverna ska arbeta i par - det räcker med en utskrift och en dator per par.

### Övningar med repl.it

* En fördel med att ha övningen på papper är att eleverna inte kan fälla ut lösningarna då.
* Om man har övningen online i ett fönster kan man kopiera kodsnuttar till repl.it. Det kan i och för sig kännas praktiskt, men är man nybörjare på programmering så kan det vara bättre att skriva in all kod själv. Det kanske tar lite längre tid, men då lär man sig Python bättre.
* Om du vill, skriv ut ett eget exemplar där du fällt ut alla lösningarna som du kan tjuvkika på vid behov.
* På Science Center, starta datorerna och skapa ett fönster med repl.it på varje dator, enligt instruktioner i övningen. Det går att köra anonymt på repl.it, så det behövs ingen inloggning.
* I skolan har nog varje elev sin egen dator, och det är enklast att de själva browsar till rätt plats på repl.it, enligt instruktioner i övningen. Om eleverna skaffar eget konto så sparas deras program automatiskt.

### Övningar med Jupyter/Colab

* För att köra Jupyter/Colab behöver man vara inloggad med personligt konto. Detta brukar fungera bra i skolor eftersom många skolor använder Google Gmail och alla elever/lärare har då konto.
* Om man försöker browsa till en Jupyter/Colab-övning utan att vara inloggad kan man få felmeddelande 400.

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

### Övningar med Jupyter/Colab

TBA

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
* Vill kunna kommentera bort flera rader på en gång. Det finns en shortcut i repl.it för det. Med högerklick får man fram en meny med editeringskommandon och deras shortcuts. Där kan man se vad shortcut för “add line comment” och “remove line comment” är.

### Relaterat till själva Python-programmeringen

* Försöker göra variabelnamn med svenska tecken och blanktecken. Det fungerar inte. T.ex funkar inte:
```python
	vår fina sång = [“hej”, “tomtegubbar”, “slå”, “i”, “glasen”]
```
(Det går bra med svenska tecken och blanktecken i strängar, men inte i variabelnamn.)

* Använder vanliga parenteser i stället för hakparenteser för listor. Rätt mycket av Väderdata A kan fungera ändå (det blir s.k. “tupler” i stället för listor). Men tupler kan inte ändras, så i uppgift Väderdata B, när man gör “append” på en lista, så fungerar det inte med tupler.

* Indentering av loopar. Speciellt för elever/personer som sett annan programmering med krullparenteser så kan det vara lite förvirrande att det räcker att indentera satserna inne i loopen.

## Data till uppgifterna
För de flesta av uppdragen har vi preparerat datan så att den ska vara lättare att använda i programmeringen.

Ofta krävs det en hel del programmering för att hämta och förbehandla data.

Information om hur vi gjort för de olika uppgifterna finns i samma katalog som uppgiften, i en fil `CONTRIBUTING.md`. T.ex. finns information om hur SMHI-datan preparerats i [weatherdata/CONTRIBUTING.md](weatherdata/CONTRIBUTING.md).
