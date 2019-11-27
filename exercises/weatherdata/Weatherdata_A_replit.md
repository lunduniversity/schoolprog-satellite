# Väderdata från SMHI. Del A.
SMHI har temperaturer och annan data från olika mätstationer i Sverige.

I detta uppdrag ska vi lära oss om listor, plottning och filer i Python och använda detta för att undersöka temperaturdata från SMHI.

Den uppgift är tänkt att köras på [repl.it](https://repl.it/@OscarWiklund96/Vaderdata-A). Använd någon av länkarna till [repl.it](https://repl.it/@OscarWiklund96/Vaderdata-A) i detta dokument för att få tillgång till de filer som uppgfiten använder sig av.

## 1 Listor
Vi börjar med några uppdrag för att se hur listor fungerar i Python.
### 1.1 Skapa en lista och skriv ut den
En lista är en sekvens av värden. I koden nedan skapas en lista som sedan skrivs ut.

**Uppdrag:** Kopiera koden nedan och provkör den på [repl.it](https://repl.it/@OscarWiklund96/Vaderdata-A).

```python
ts = [14.1, 13.5, 17.5, 16.2, 18.9, 11.3]
print("Temperaturerna är:")
print(ts)
```
Några saker att observera:
*   Man har hakparenteser runt listan
*   Decimaltal skrivs med punkt (inte med komma)
*   Listan har sparats i variabeln `ts`

Värdena ovan är temperaturer som mätts upp under ett antal dagar i juni. Tabellen nedan visar temperaturerna, regnmängderna och vilka dagar det gäller.

|dag|3|7|10|11|14|17|
|:--:|--:|-:|--:|-:|-:|-:|
|**temp**|14.1|13.5|17.5|16.2|18.9|11.3|
|**regn**|0|0.2|0.1|0.3|0|3.2|


**Uppdrag:** Skriv kod som skapar en lista `days` med värdena för dagarna i tabellen (3, 7, 10, ...) och som sedan skriver ut listan, på liknande sätt som i förra exemplet. Provkör koden för att se att den fungerar.

Om du inte vet hur du skall göra så finns lösningen här.
<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>days = [3, 7, 10, 11, 14, 17]
print("Dagarna är:")
print(days)
</code></pre></p>
</details>

\
**Uppdrag:** Skriv kod som på liknande sätt skapar en lista `rain` med värdena för regnmängderna i tabellen. Anropa också `print` som tidigare så att du kan se att den nya listan har rätt värden.

<details>
<summary markdown="span">
Tips
</summary>
<p>
Försök först lösa uppdraget själv. Titta på förra exemplet för att förstå hur du ska göra. Titta inte på lösningen nedan förrän du verkligen har försökt själv.
<details>
<summary markdown="span">
Lösning
</summary>
<p>
<pre><code>rain = [0, 0.2, 0.1, 0.3, 0, 3.2]
print("Regnmängderna är:")
print(rain)
</code></pre>
</p>
</details>
</p>
</details>

### 1.2 Beräkna medeltemperatur med `sum` och `len`
Det finns en inbyggd funktion `sum(list)` som kan summera elementen i en lista. Det finns också en inbyggd funktion `len(list)` som ger längden på listan.

Följande kod skriver ut summan av temperaturerna och längden på listan. Kopiera och provkör den.
```python
print(sum(ts))
print(len(ts))
```
Undrar du varför summan inte blir 91.5, utan visas med många decimaler? Hur kan det vara så?

<details>
<summary markdown="span">
Svar
</summary>
<p>Det beror på att tal representeras binärt i datorn, dvs med nollor och ettor. Många decimaltal kan inte representeras exakt med binära tal, så omvandlingen ger avrundningsfel.
  </p>
  </details>
<details>
<summary markdown="span">
Tips om att skriva ut med färre decimaler:
</summary>
<p> Om man vill skriva ut ett decimaltal avrundat till färre decimaler kan man göra det genom att sätta det i en formatsträng på följande sätt:
<pre><code>print(f"{sum(temperatures):.3f}")</code>
</pre>
Det första f:et står för formatsträng. Det andra f:et står för float (decimaltal heter så med datorterminologi). 3:an står för att vi vill se 3 decimaler. Prova gärna att lägga till en sådan printsats i kodrutan ovan. Kan du få ut värdet med 4 decimaler i stället?
</details>

\
**Uppdrag:** Skriv kod som räknar ut medeltemperaturen och skriver ut den.

<details>
<summary markdown="span">
Tips
</summary>
<p>
 För att få medeltemperaturen dividerar du summan med antalet temperaturer (alltså längden på listan).
</p>
</details>

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>s = sum(ts)
n = len(ts)
avg = s/n
print("medeltemperaturen är:")
print(avg)
# Eller för att skriva ut med bara en decimal:
print("medeltemperaturen med en decimal:")
print(f"{avg:.1f}")
</code></pre></p>
</details>

### 1.3 Accessa list-element

Du kan accessa (komma åt) enskilda element i en lista `lst` med notationen `lst[i]` där `i`  är positionen för elementet i listan. Första elementet har position 0, nästa position 1, osv.

Här är ett exempel på en lista med strängar där elementen är strängar. Kopiera och provkör koden.
```python
song = ["glad", "såsom", "fågeln", "i", "morgonstunden"]
print(song[0])
print(song[1])
print(song[2])
print(song[3])
print(song[4])
```
**Uppdrag:** Skriv kod som skriver ut första och sista elementet i listan `rain`.
<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>print(rain[0])
print(rain[5])
</code></pre></p>
</details>

### 1.4 Loopa över listor

En `for` sats kan loopa över elementen i en lista. Till exempel kan vi skriva ut alla orden i listan `song` med följande kod:

```python
for word in song:
  print(word)
```
For-loopen körs lika många varv som det finns element i listan. För varje varv får loopvariabeln <code>word</code> nästa värde i listan. Satsen <code>print(word)</code> skriver ut värdet.

**Uppdrag:** Skriv kod som skriver ut alla regnmängderna i listan `rain`.
<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>for v in rain:
  print(v)
</code></pre></p>
<p>Kommentar: Här har vi döpt loopvariabeln till <code>v</code>. Loopvariabeln kan ha vilket namn som helst, men man bör välja ett namn som passar för elementen i listan. Prova att ändra din loopvariabel till exempel till <code>r</code>.</p>
</details>

\
För att loopa ett visst antal gånger används ofta  en `for` loop med en `range`, som i följande exempel:
```python
for i in range(4):
  print("värdet är", i)
```
Kopiera och provkör!

Loopen gör 4 varv där loopvariabeln `i` får värdena 0, 1, 2, 3 i tur och ordning.

Observera också att vi kan skriva ut flera saker på en rad genom att ha flera argument till `print`.

**Uppdrag** Skriv en liknande loop (med en loopvariabel och range), och som gör lika många varv som det finns element i listan `days`.
<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>for i in range(len(days)):
  print("värdet är", i)
</code></pre></p>
</details>

\
**Uppdrag:** Skriv en loop som skriver ut en rad för varje dag, temperatur och regnmängd. Till exempel skall de tre första raderna vara:

    3 14.1 0
    7 13.5 0.2
    10 17.5 0.1

Tips:
* Använd loopvariabeln för att accessa värden i listorna

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>for i in range(len(days)):
  print(days[i], ts[i], rain[i])
</code></pre></p>
</details>

## 2 Plottning
Nu skall vi titta på hur plottning fungerar i Python.
### 2.1 Plotta en kurva

Vi börjar med att plotta en temperaturkurva med dagar på x-axeln och temperaturer på y-axeln.

Vi använder biblioteket `matplotlib` för detta. Provkör följande kod:
```python
import matplotlib.pyplot as plt

plt.plot(days, ts)
plt.savefig("temperaturkurva.png")
```
Några saker att observera:
*   `import`-satsen ger oss access till biblioteket `matplotlib.pyplot` och låter oss använda det lite kortare namnet `plt` för det.
*   anropet till `plot`-funktionen anger att vi vill ha  `days` på x-axeln och `ts` på y-axeln.

<details>
<summary markdown="span">
Fler detaljer
</summary>
<p>
<ul>
   <li> plt.savefig() sparar plotten som en bild som du kan hitta under Files på vänster sida av repl.it. Repl.it visar även bilden automatiskt när den sparas. I andra miljöer kan man vara tvungen att använda plt.show() för att bilden ska synas
  
</ul>
</p>
</details>

### 2.2 Experimentera med fel vid plottning
En viktig sak när man plottar är att listorna för x och y-värdena måste vara lika långa. Annars får man ett felmeddelande.

Till exempel är följande anrop felaktigt

    plt.plot([3, 7, 10], ts)

eftersom listan av x-värden är kortare än temperaturlistan `ts`.

**Uppdrag:** 
*  Provkör det felaktiga anropet ovan för att se att du får ett felmeddelande.
*  Felmeddelandet innehåller mycket information, men längst ner hittar du en förklaring av felet (`ValueError: ...`). Kan du förstå förklaringen?
*  Kan du ändra koden så att du blir av med felmeddelandet?

<details>
<summary markdown="span">
Lösning
</summary>
<p>
I felmeddelandet kan man se att första listan har längden 3, medan den andra har längden 6. För att bli av med felmeddelandet kan man ändra första listan så att den också får 6 element. Till exempel:
<pre><code>plt.plot([3, 7, 10, 11, 14, 17], ts)
</pre></code></p>
</details>

### 2.3 Gör en mer informativ plott
Det finns många olika möjligheter att göra plotten finare och mer informativ. Vi borde till exempel skriva ut
*  vad x och y-axlarna visar (dag och grader Celsius)
*  en teckenförklaring som säger vad kurvan visar (temperaturer i juni)

Det vore också bra att sätta en prick för varje mätvärde, eftersom många dagar saknar mätvärde. (T.ex. inleds mätvärden med värden från den 3:e och 7:e juni i exemplet.)

**Uppdrag:** Provkör koden nedan för att se hur man får med denna information.

```python
plt.plot(days, ts, "o-", label="temperaturer i juni")
plt.xlabel("dag")
plt.ylabel("grader Celsius")
plt.legend()
plt.savefig("test.png")
```

Förklaring:
* anropet "xlabel" skriver ut etikett (label) på x-axeln
* anropet "ylabel" skriver ut etikett på y-axeln
* anropet "legend" skriver ut en teckenförklaring ("legend" på engelska).
*  parametern "label=..." i plot-anropet sätter en etikett på kurvan som skrivs ut om man anropar "legend"
*  parametern "`o-`" i plot-anropet ger ett "format" för kurvan, och säger att det skall vara en prick för varje mätvärde och linjer emellan. Det finns många andra "format" att välja på. T.ex. kommer "<code>r+--</code>" att rita en röd kurva med ett plus-tecken för varje mätvärde och streckade linjer emellan.

<details>
<summary markdown="span">
Detaljer om format
</summary>
<p>
Om du är intresserad av fler exempel på vilka format som kan användas i plot-anrop kan du titta i den officiella <a href="https://matplotlib.org/tutorials/introductory/pyplot.html">pyplot handledningen</a>. Om du vill se alla möjligheter för format så hittar du det i <a href="https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.plot.html">dokumentationen för plot-funktionen</a>, se sektionen <i>Notes</i>.)</p>
</details>

<details>
<summary markdown="span">
Detaljer om valfria och namngivna parametrar
</summary>
<p>
  Format-parametern är ett exempel på en <i>valfri</i> parameter. Den har ett standardvärde som används om man inte anger parametern. Standardvärdet för format-parametern är "b-" (blå linje).
  
  Parametern "label=..." är ett exempel på en <i>namngiven</i> parameter. Namngivna parametrar måste komma i slutet på anropet (efter icke-namngivna) och ordningen mellan dem spelar ingen roll. De är praktiska att använda när en funktion har väldigt många valfria parametrar (vilket plot har). 
</p>
</details>

\
**Uppdrag:** Kopiera koden för plottningen i föregående uppdrag och experimentera med andra värden för format, label, xlabel och ylabel. Kan du få en grön kurva med streckade linjer?

### 2.4 Skapa en egen plott

**Uppdrag:** Skriv kod för att plotta regnmängderna (använd listan `rain` som vi skapade tidigare). Kan du göra plotten fin och informativ med etiketter på axlarna och en legend?

<details>
<summary markdown="span">
Tips
</summary>
<p>
Arbeta i små steg: gör en sak i taget och provkör koden efter varje steg så du ser att det blir rätt. 
  <ul>
    <li> Anropa <code>plt.plot(...)</code> så att dagarna hamnar på x-axeln och regnmängderna på y-axeln.
    <li> Lägg till "o-" som parameter till "plot" för att få prickar för värdena.
    <li> Anropa <code>plt.xlabel(...)</code> och <code>plt.ylabel(...)</code> för att sätta etiketter på axlarna.
    <li> Lägg till parametern "label=..." i plot-anropet och anrop till <code>plt.legend()</code> för att få ut "legenden" för kurvan.
    <li> Glöm inte att avsluta med <code>plt.savefig("namn")</code> för att din plot ska visas.
  </ul>
</p>
</details>

Om du gjort rätt så bör ditt diagram se ut något i följande stil

<details>
<summary markdown="span">
Diagram
</summary>
<p>
<img src="https://drive.google.com/uc?id=1rfC3NUK9Sp16J-Pe-PFYL7J9Z_vfMhhr"
height="300">
</p>
</details>

<details>
<summary markdown="span">
Mer tips
</summary>
<p>
Försök först lösa uppdraget själv. Titta på tidigare exempel för att förstå hur du ska göra. Titta inte på lösningen förrän du verkligen har försökt själv.
<details>
<summary markdown="span">
Lösning
</summary>
<p>
<pre><code>rain = [0, 0.2, 0.1, 0.3, 0, 3.2]
plt.plot(days, rain, "o-", label="regnmängder i juni")
plt.xlabel("dag")
plt.ylabel("mm")
plt.legend()
plt.savefig("regn.png")
</code></pre>
</p>
</details>
</p>
</details>

### 2.5 Plotta två kurvor

Vi kan lägga två kurvor i samma plot.

**Uppdrag:** Skapa en plot där du visar både regnmängden och temperaturen. (Tips: gör ett plot-anrop för regnmängden och ett för temperaturen.) Kan du göra en fin informativ plot med olika färg på kurvorna? Vad skall du skriva för etikett på y-axeln?

<details>
<summary markdown="span">
Lösning
</summary>
<p>
Här är ett exempel på hur vi kan göra:
<pre><code>plt.plot(days, rain, "bo-", label="regnmängder i juni")
plt.plot(days, ts, "ro-", label="temperaturer i juni")
plt.xlabel("dag")
plt.ylabel("mm eller grader")
plt.legend()
plt.savefig("regnochtemp.png")
</pre></code></p>
</details>

## 3 Filer

Nu när vi kan lite om listor och plottning kan vi snart plotta riktig data från SMHI.

Vi behöver först lära oss hur man läser in data från filer.

Filerna vi ska använda finns tillgängliga om du använde länken till repl.it i början av uppgiften. (Ska synas under "Files" på vänster sida i form av `lund_juli_2016.txt`, `lund_juli_2017.txt` och `lund_juli_2018.txt`) Du kan klicka på filerna för att se hur de ser ut. De består en medeltemperatur per rad, totalt 31 rader som motsvarar datumen för månaden juli.

### 2.1 Läs in från fil

Vi börjar med att läsa in innehållet från filen `lund_juli_2016.txt` till en variabel `data`. Testa köra följande kod.

```python
with open("lund_juli_2016.txt", "r") as f:
  data = f.read()
print(data)  
```

Programmet läste först in all information från filen för att sedan skriva ut det igen. Man kan säga att vi öppnar vår fil `lund_juli_2016.txt` och kallar filen `f`. Vi öppnar den i <i>read</i>-läge, där av `"r"` i koden. Därefter läser vi från filen med metoden `read()` och sparar detta i vår variabel `data`.

Kan vi kombinera inläsning från fil med plottning av grafer med hjälp av `matplotlib`? Vi kan inte plotta direkt eftersom formatet på vår data inte matchar det `plt.plot()` vill ha, en lista av tal. Vi måste därför utföra lite typomvandling på vår data först. Funktionen `read()` som vi använder för att läsa in datan från filen sparar allt innehåll som en enda lång sträng. Vi kan dela upp en sträng till flera genom att anropa ```split()```. Vi kan till exempel välja ett dela upp vår sträng vid varje radbrytning med ```data.split("\n")```. Vår data kommer då vara lagrad som en lista av mindre strängar istället.

För att göra det enklare kan du kopiera och köra kodstycket nedan.
```python
data = data.split("\n")
print("Lista i form av många strängar:")
print(data)
data = [float(i) for i in data]
print("Lista i form av floats:")
print(data)
```

Som du ser i utskriften så får vi en lista av många små strängar efter att vi har gjort `data.split("\n")`. Därefter omvandlar vi strängarna till tal i form av floats. Om du kollar noggrant så ser du att formatet skiljer sig åt på de två utskrifterna.

För att kunna plotta våra värden behöver vi även en lista med datumen för månaden juli. 

**Uppdrag**: Skapa en lista med hjälp av `range()` som innehåller värdena 1 till 31. 
<details>
<summary markdown="span">
Lösning
</summary>
<p>
Här är ett exempel på hur vi kan göra:
<pre><code>datum = list(range(1, 32))
</pre></code></p>
</details>

Nu har vi allt vi behöver för att kunna plotta våra temperaturer. 

**Uppdrag**: Plotta temperaturerna med tillhörande datum på samma sätt som i tidigare avsnitt.

<details>
<summary markdown="span">
Lösning
</summary>
<p>
Här är ett exempel på hur vi kan göra:
<pre><code>plt.plot(datum,data)
plt.xlabel("datum")
plt.ylabel("medeltemperatur")
plt.savefig("2016.png")
</pre></code></p>
</details>

\
På samma sätt skulle vi nu kunna ta fram motsvarande värde för 2017 och 2018 och jämföra alla 3. 

**Uppdrag**: Testa kopiera koden från tidigare uppgifter för att på samma sätt skapa `data2017` och `data2018`.

<details>
<summary markdown="span">
Lösning
</summary>
<p>
Här är ett exempel på hur vi kan göra:
<pre><code>with open("lund_juli_2017.txt", "r") as f:
  data2017 = f.read()
data2017 = data2017.split("\n")
data2017 = [float(i) for i in data2017]
with open("lund_juli_2018.txt", "r") as f:
  data2018 = f.read()
data2018 = data2018.split("\n")
data2018 = [float(i) for i in data2018]
</pre></code></p>
</details>

**Uppdrag**: Plotta nu graferna i samma fönster. Du kan använda parametern label för att göra det tydiligare vilken linje som tillhör vilket år. Exempel: `plt.plot(datum,data,label="2016")`.

<details>
<summary markdown="span">
Lösning
</summary>
<p>
Här är ett exempel på hur vi kan göra:
<pre><code>plt.plot(datum,data, label="2016")
plt.plot(datum,data2017, label="2017")
plt.plot(datum,data2018, label="2018")
plt.legend()
plt.savefig("allajuli.png")
</pre></code></p>
</details>

Vilket år hade den högsta uppmätta medeltemperaturen för en dag? Skulle man kunna ta reda på de högsta repspektive minsta värden för varje år med hjälp av programmering? 

***Extra Uppdrag:*** Använd funktionerna `max()` och `min()` för att bestämma störtsa respektive minsta värde för samtliga år.

## 4 Quiz

### Fråga 1
Vilka av dessa är en lista i python? 
*   `[0, 1, 7]`
*   `(0, 1, 7)`
*   `{0, 1, 7}`

<details>
<summary markdown="span">
Svar
</summary>
<p>
<code>[0, 1, 7]</code>
</p>
</details>

### Fråga 2
Vad skriver man för att få längden på en lista som kallas `data`?
* `len(data)`
* `size(data)`
* `range(data)`

<details>
<summary markdown="span">
Svar
</summary>
<p>
<code>len(data)</code>
</p>
</details>

### Fråga 3

Vad skriver följande kodstycke ut?

```python
list = ["hej", "på", "dig"]
print(list[1])
```

<details>
<summary markdown="span">
Svar
</summary>
<p>
<code>på</code>
</p>
</details>

### Fråga 4

Vad skriver följande kodstycke ut?

```python
list = ["hej", "på", "dig"]
for word in list:
    print(word)
```

<details>
<summary markdown="span">
Svar
</summary>
<p>
<pre><code>hej
på
dig</code>
</pre>
</p>
</details>

### Fråga 5

Vad skriver följande kodstycke ut?

```python
list = ["hej", "på", "dig"]
for i in range(2):
    print(list[i])
```

<details>
<summary markdown="span">
Svar
</summary>
<p>
<pre><code>hej
på</code>
</pre>
</p>
</details>

### Fråga 6

Vad kommer stå på x-axeln i plotten som genereras av följande kod?

```python
x = [1, 2 3]
y = [1, 4, 9]
plt.plot(x, y)
plt.xlabel("mina fina x-värden")
plt.ylabel("mina vackra y-värden")
```

<details>
<summary markdown="span">
Svar
</summary>
<p>
<code>mina fina x-värden</code>
</p>
</details>

### Fråga 7

Vilken rad kod öppnar filen `text.txt` i läsläge?

* `with open("text.txt", "r") as f:`
* `with open("text.txt", "w") as f:`
* `read("text.txt") as f:`

<details>
<summary markdown="span">
Svar
</summary>
<p>
<code>with open("text.txt", "r") as f:</code>
</p>
</details>

### Fråga 8
Följande kod:
```python
with open("text.txt", "r") as f:
    data = f.read()
print(data)
```

skriver ut:
```python
hej
på
dig
```
Vad skrivs nu ut av följande stycke?
```python
print(data.split("\n"))
```

<details>
<summary markdown="span">
Svar
</summary>
<p>
<code>["hej", "på", "dig"]</code>
</p>
</details>

