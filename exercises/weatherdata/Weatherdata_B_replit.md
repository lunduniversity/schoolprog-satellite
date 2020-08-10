# Väderdata från SMHI. Del B.
I detta uppdrag fortsätter vi att undersöka temperaturdata från SMHI.

Nu när vi kan lite om listor och plottning kan vi snart plotta riktig data från SMHI.

I uppgiften kommer vi att lära oss hur man läser in data från filer.

## 1 Filer

### 1.1 Titta på filerna

Gå till följande exempel på repl.it där vi förberett datafiler från SMHI: [https://repl.it/@OscarWiklund96/Vaderdata-A](https://repl.it/@OscarWiklund96/Vaderdata-A)

Filerna syns till vänster i fönstret, under *Files*. Det finns tre filer: `lund_juli_2016.txt`, `lund_juli_2017.txt` och `lund_juli_2018.txt`.

Filerna visar medeltemperaturer i Lund under varje dag i juli för tre olika år. Värdena är *dygnsmedeltemperaturer*, alltså medeltemperaturen över hela dygnet, inklusive både natt och dag. Du kan klicka på filerna för att se hur de ser ut. Varje fil har 31 rader - en för varje dag i juli. På varje rad står medeltemperaturen för den dagen.

**Uppdrag 1.1 a** Titta på filerna. Vilken var medeltemperaturen den 14 juli 2016, 2017 respektive 2018?

<details>
<summary markdown="span">
Svar
</summary>
<p>
<ul>
  <li>14 juli 2016: 16.0 grader</li>
  <li>14 juli 2017: 15.2 grader</li>
  <li>14 juli 2018: 19.2 grader</li>
</ul>
</p>
</details>
<p></p>

### 1.2 Värm upp med lite listor

Först behöver vi lära oss lite mer om listor. Vi har tidigare sett hur man kan skapa en lista direkt, så här:

```python
lst = ["hej", "på", "dej"]
```

**Uppdrag 1.2 a** Nu ska vi i stället skapa listan genom att lägga till ett element i taget med hjälp av funktionen `append`. (*Append* betyder att man lägger till sist i listan.) Provkör följande kod:

```python
lst = []          # Skapa en tom lista
lst.append("hej") # Lägg till "hej" sist
lst.append("på")  # Lägg till "på" sist
lst.append("dej") # Lägg till "dej" sist
print(lst)        # Skriv ut listan
```

**Uppdrag 1.2 b** Skapa en egen lista `lst2` på liknande sätt med något annat innehåll som du själv hittar på.


### 1.3 Läs in från fil

Vi vill nu läsa in varje fil till en lista med temperaturvärden.

Vi börjar med att experimentera lite. En fil kan ses som en lista av rader, där varje rad består av en sekvens av tecken som avslutas med ett *newline*-tecken (skrivs `\n`).

**Uppdrag 1.3 a** Följande kod läser in filen `lund_juli_2016.txt` och lägger varje rad i en lista `data`. Testa att köra koden.

```python
f = open("lund_juli_2016.txt")
data = []
for line in f:
  data.append(line)
print(data)  
```

Observera att:
* Första raden öppnar filen med `open`. Det gör att vi kan läsa in data från filen.
* Vi kan loopa över raderna i filen med en for-sats.
* Vi skapar listan genom att börja med att göra en tom lista och sedan `append`:a varje rad till listan inuti loopen.

Vad blev resultatet? Vi fick en lista med textsträngar, inklusive *newline*-tecknet (`\n`).

### 1.4 Gör om textsträngar till float

Vi vill ju egentligen ha en lista av decimaltal (*floats*) och inte en lista av textsträngar.

**Uppdrag 1.4 a** Prova att göra om en textsträng till en float med följande kod:

```python
a = "1.2"       # Definiera en sträng
b = float(a)    # Gör om den till en float
c = b*2         # Multiplicera med 2
print(c)        # Skriv ut resultatet
```

**Uppdrag 1.4 b** Det går bra att strängen a innehåller blanka och newlines före och efter talet. Prova att ändra strängen t.ex. till `" 1.2 "`

**Uppdrag 1.4 c** Vad händer om man gör `float` på något som *inte* är ett decimaltal? Prova att ändra strängen t.ex. till `"hej"` eller `"1.2 hej"`. Vilket fel får du?

<details>
<summary markdown="span">
Lösning
</summary>
<p>
Man får ett fel <code>ValueError: could not convert string to float</code></p>
</details>
<p></p>

### 1.5 Läs in filen till en lista av floats

Nu vet du både hur man läser in filer och hur man omvandlar strängar till floats.

**Uppdrag 1.5 a** Skriv kod som läser in filen `lund_juli_2016.txt` till en lista `data2016` som innehåller temperaturerna för 2016 som floats.

*Tips!* Använd liknande kod som tidigare, men gör `float` på strängen innan du `append`-ar den till listan. Skriv ut `data2016` så att du ser att resultatet blir rätt.

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>f = open("lund_juli_2016.txt")
data2016 = []
for line in f:
  data2016.append(float(line))
print(data2016)</code></pre>
</p>
</details>
<p></p>

**Uppdrag 1.5 b** Lägg till liknande kod som skapar motsvarande listor `data2017` och `data2018`.

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>f = open("lund_juli_2017.txt")
data2017 = []
for line in f:
  data2017.append(float(line))
print(data2017)
</code></pre><pre><code>f = open("lund_juli_2018.txt")
data2018 = []
for line in f:
  data2018.append(float(line))
print(data2018)
</code></pre>
</p>
</details>
<p></p>


## 2 Refaktorisering

Vi har nu tre nästan likadana kodstycken för att skapa listorna `data2016`, `data2017` och `data2018`. Sådan repetitiv kod vill man gärna undvika, och i stället skriva på ett elegantare sätt.

Att förbättra sin kod utan att förändra resultatet kallas att man *refaktoriserar* koden.

### 2.1 Läs in med en funktion

I detta fall kan vi refaktorisera koden genom att skapa en egen *funktion* och därmed få både tydligare och kortare kod.

Först tittar vi på hur en enkel funktion fungerar.

**Uppgift 2.1 a** Nedan definieras en funktion `double` som dubblerar ett värde. Efter definitionen kan vi anropa vår nya funktion med olika argument. Provkör koden nedan:

```python
def double(x):     # Definiera funktionen double
  y = x + x
  return y

a = double(3)      # Anropa funktionen med några
b = double(4)      # olika argument
c = double(5)

print(a, b, c)     # och skriv sedan ut resultaten
```

Observera att:
* Funktionen har en parameter `x` som kan användas inuti funktionen
* Funktionen har en lokal variabel `y` som bara är giltig inuti funktionen
* Fuktionen returnerar ett värde (`y`).
* Koden inuti funktionen är *indenterad* med ett par blanka. Det är så Python vet vilken kod som hör till funktionen.
* Anropen av funktionen är *inte* indenterade. De hör ju inte till funktionens definition.

När vi ska införa en funktion är det bra att först tänka igenom hur vi skulle vilja anropa den. Det hade varit trevligt om vi hade haft en funktion `read_temps` som vi kunde anropa så här för att få listorna:

```python
data2016 = read_temps("lund_juli_2016.txt")
data2017 = read_temps("lund_juli_2017.txt")
data2018 = read_temps("lund_juli_2018.txt")
```

**Uppdrag 2.1 b** Skriv kod som definierar funktionen `read_temps`.

*Tips!* Här är ett kodskelett du kan använda:

```python
def read_temps(filename):
  f = ...
  data = []
  for ...
    ...
  return data
```

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>def read_temps(filename):
  f = open(filename)
  data = []
  for line in f:
    data.append(float(line))
  return data
</code></pre>
</p>
</details>
<p></p>

**Uppdrag 2.1 c** Lägg till anropen (nedanför funktionsdefinitionen) och skriv ut listorna så att du kan se att du får samma resultat som tidigare.

Om du får samma resultat som tidigare har du *refaktoriserat* koden - du har gjort koden tydligare och bättre, men utan att ändra vad som räknas ut.

### 2.2 Städa upp i koden

**Uppdrag 2.2 a** Städa upp din kod så att du tar bort eller kommenterar bort kod som inte behövs i fortsättningen. Det du behöver i fortsättningen är `data2016` `data2017` och `data2018`.

## 3 Skapa x-värden med `range`

För att kunna plotta våra värden behöver vi en lista med datumen för månaden juli, dvs `[1, 2, ..., 31]`. Vi kan skapa en sådan lista med hjälp av att funktionerna `range` och `list`.


**Uppdrag 3 a** Prova först att skapa en lista `[0, 1, 2, 3]` genom att köra följande kodsnutt:

```python
lst = list(range(4))
print(lst)
```
Observera:
* `range(n)` står för ett intervall från 0 till `n-1`
* Intervallet börjar alltså på 0 och `n` är det första värdet *efter* intervallet.
* anropet `list(...)` gör om range:en till en lista.

**Uppdrag 3 b** Om vi har två argument till `range` kan vi ange även start-punkten, så att vi kan börja på något annat än 0. Prova att köra följande kodsnutt. Vilken lista blir det?

```python
lst = list(range(1, 4))
print(lst)
```

<details>
<summary markdown="span">
Svar
</summary>
<p>Det blir <code>[1, 2, 3]</code>
</p>
</details>
<p></p>

Observera:
* Med `range(a, b)` får vi ett intervall som börjar på `a` och där `b` är det första värdet *efter* intervallet.

**Uppdrag 3 c** Nu vet du hur range fungerar och hur du skapar en lista från en range. Lägg nu till kod som skapar en lista `days` med datumen för juli, dvs `[1, 2, ..., 31]`.

<details>
<summary markdown="span">
Lösning
</summary>
<p>
<pre><code>days = list(range(1, 32))
</code></pre></p>
</details>
<p></p>

Nu har vi allt vi behöver för att kunna plotta våra temperaturer.

## 4 Plotta temperaturer

Nu har vi både x-värden (`days`) och y-värden (`data2016`, `data2017` och `data2018`) så att vi kan plotta temperaturkurvor.

**Uppdrag 4 a**: Plotta temperaturerna för juli 2016.

Här är lite tips om du glömt detaljer om plottning.
* Du behöver importera plot-biblioteket
* Du kan anropa `ion`-funktionen för att sätta på interaktiv mode, så att plotter visas automatiskt.
* Du behöver anropa `plot`-funktionen
* Du kan anropa `savefig`-funktionen för att spara diagrammet som fil.

<details>
<summary markdown="span">
Lösning
</summary>
<p>
Här är ett exempel på hur vi kan göra:
<pre><code>import matplotlib.pyplot as plt
plt.ion()
plt.plot(days, data2016)
plt.xlabel("dag i juli")
plt.ylabel("medeltemperatur")
plt.savefig("juli.png")
</code></pre></p>
</details>
<p></p>

**Uppdrag 4 b**: Lägg till lämpliga etiketter på x- och y-axeln, om du inte redan har gjort det. (Använd funktionerna `xlabel` och `ylabel`.)


**Uppdrag 4 c**: Ändra plotten så att du även plottar temperaturerna för juli 2017 och juli 2018.
Använd olika färger för kurvorna. Lägg till en etikett på varje kurva (med parametern `label`) så att man ser vilken kurva som är vilken.

*Tips!* Ett typiskt plot-anrop skulle kunna vara
\
 `plt.plot(days, data2020, "ro-", label="2020")`
\
Glöm inte att anropa funktionen `legend` för att få ut beskrivningen av vilken kurva som är vilken.


<details>
<summary markdown="span">
Lösning
</summary>
<p>
<pre><code>import matplotlib.pyplot as plt
plt.ion()
plt.plot(days, data2016, "bo-", label="2016")
plt.plot(days, data2017, "ro-", label="2017")
plt.plot(days, data2018, "go-", label="2018")
plt.xlabel("dag i juli")
plt.ylabel("medeltemperatur")
plt.legend()
plt.savefig("juli.png")
</code></pre></p>
</details>
<p></p>

**Uppdrag 4 d** Titta på kurvorna och fundera på hur de skiljer sig åt. Var det varmt eller kallt dessa somrar? Tänk på att värdet för varje dag motsvarar medeltemperaturen för *hela det dygnet* (både dag och natt). Vilket år var varmast? Vilket år var kallast? Kommer du ihåg vad du gjorde de olika somrarna och hur vädret var?

En tidningsrubrik i augusti 2018 var "Värmeböljan 2018 saknar motsvarighet i historien". Här kan du läsa om vad SMHI skriver om olika år och årstider, inklusive de tre somrarna: [https://www.smhi.se/klimat/klimatet-da-och-nu/arets-vader](https://www.smhi.se/klimat/klimatet-da-och-nu/arets-vader)

## 5 Titta på en annan ort i Sverige

Lund ligger långt söderut i Sverige. Hur ser det ut på andra orter?

**Uppdrag 5 a** Surfa till [https://github.com/lunduniversity/schoolprog-satellite-data/tree/master/smhi/julydir](https://github.com/lunduniversity/schoolprog-satellite-data/tree/master/smhi/julydir). Här finns filer med dygnsmedeltemperaturer under juli för många orter i Sverige, för åren 2016, 2017 och 2018. Känner du igen några ortnamn?

(Alla SMHIs stationer är inte med i denna lista. Endast de som har fullständig data för juli under alla tre åren är med.)

Om du vill se var en viss station är kan du titta på SMHI:s karta: [https://www.smhi.se/vadret/vadret-i-sverige/observationer](https://www.smhi.se/vadret/vadret-i-sverige/observationer). Kanske vill du titta på Tarfala som är en väderstation vid Kebnekajses fot?

**Uppdrag 5 b** Välj två olika orter och kopiera 2018 års värden till repl.it. Du kan kopiera en fil genom att:
* Skapa en ny fil till vänster i repl.it-fönstret (klicka på ikonen `Add file` vid *Files*).
* Namnge filen. Du behöver inte använda samma långa namn som originalfilerna, utan ta något kortare.
* Kopiera innehållet till den nya filen. Se till att första värdet hamnar på rad 1 och att det finns precis 31 rader i filen. (Koden vi har skrivit fungerar bara om det finns exakt ett värde på varje rad, och inga tomma rader.)

**Uppdrag 5 c** Ändra ditt program så att du plottar både  de nya orternas värden för 2018 och motsvarande värden för Lund 2018. Döp om variabler så att ditt program blir begripligt. Sätt lämpliga etiketter på axlar och kurvor så att man förstår diagrammet. Hur skiljer sig temperaturerna för de tre orterna?

## 6 Jämför kurvorna (extrauppgift)

Vilken kurva hade den högsta uppmätta medeltemperaturen för en dag? Skulle man kunna ta reda på de högsta respektive lägsta värdena för varje kurva med hjälp av programmering?

Du kan beräkna högsta värdet i en lista med funktionen `max`.

**Uppdrag 6 a** Prova hur `max` fungerar genom att provköra följande kod:

```python
data = [1, 17, 43, 8]
maxval = max(data)
print(maxval)
```

**Uppdrag 6 b** Använd funktionen `max` för att ta reda på högsta dygnsmedeltemperaturen i juli för de tre kurvorna. Stämmer värdena med vad du kan se i ditt diagram?

**Uppdrag 6 c** Gör motsvarande sak för att ta reda på lägsta dygnsmedeltemperaturen. Du kan använda funktionen `min` för detta.

**Uppdrag 6 d** Räkna ut medelvärdena för juli för de tre kurvorna (använd `sum` och `len` som i tidigare uppgifter). Hur mycket skiljer sig medelvärdena för de olika kurvorna?

**Uppdrag 6 e** Kan du refaktorisera din kod genom att införa en funktion `mean` för att räkna ut medelvärdet av en lista?

<details>
<summary markdown="span">
Lösning
</summary>
<p>
<pre><code>def medel(lst):
  return sum(lst)/len(lst)
</code></pre></p>
</details>
<p></p>

## 7 Quiz

### Fråga 1

Vilken rad kod skapar en tom lista?

* `lista = []`
* `lista = [0]`
* `lista = [" "]`

<details>
<summary markdown="span">
Svar
</summary>
<p>
<code>lista = []</code>
</p>
</details>
<p></p>

### Fråga 2

Vilken rad kod lägger till elementet `7` till listan `lista`?

* `lista = lista + 7`
* `lista.append(7)`
* `lista.add(7)`

<details>
<summary markdown="span">
Svar
</summary>
<p>
<code>lista.append(7)</code>
</p>
</details>
<p></p>

### Fråga 3

Vad skall man skriva för att omvandla strängen `"4.2"` till ett decimaltal?

* `round("4.2")`
* `string("4.2")`
* `float("4.2")`

<details>
<summary markdown="span">
Svar
</summary>
<p>
<code>float("4.2")</code>
</p>
</details>
<p></p>

### Fråga 4

Vilket fel får vi om vi anropar `float("Gott nytt år")`

* `ValueError: could not convert string to float`
* `ValueError: could not convert float to string`
* `ValueError: could not convert string to value`

<details>
<summary markdown="span">
Svar
</summary>
<p>
<code>ValueError: could not convert string to float</code>
</p>
</details>
<p></p>

### Fråga 5

Vad skriver följande program ut?

```python
def f(x):
  return x+1
print(f(0)+f(1))
```

* `1`
* `2`
* `3`

<details>
<summary markdown="span">
Svar
</summary>
<p>3
</p>
</details>
<p></p>

### Fråga 6

Vad betyder det att man refaktoriserar ett program?

* Man förbättrar koden, men utan att ändra vad den räknar ut.
* Man förbättrar koden genom att lägga till fler uträkningar.
* Man förbättrar koden genom att rätta alla fel.

<details>
<summary markdown="span">
Svar
</summary>
<p>Man förbättrar koden, men utan att ändra vad den räknar ut.
</p>
</details>
<p></p>

### Fråga 7

Vad skriver följande program ut?

```python
print(list(range(3, 6)))
```

* [3, 4, 5]
* [3, 4, 5, 6]
* [3, 4, 5, 6, 7, 8]

<details>
<summary markdown="span">
Svar
</summary>
<p><code>[3, 4, 5]</code>
</p>
</details>
<p></p>

### Fråga 8

Vilken av följande somrar var varmast i Sverige?


* 2016
* 2017
* 2018

<details>
<summary markdown="span">
Svar
</summary>
<p>2018
</p>
</details>
<p></p>

### Fråga 9

Vad skriver följande program ut?

```python
print(max([1, 15, 14, 33, 22]))
```

<details>
<summary markdown="span">
Svar
</summary>
<p><code>33</code>
</p>
</details>
<p></p>
