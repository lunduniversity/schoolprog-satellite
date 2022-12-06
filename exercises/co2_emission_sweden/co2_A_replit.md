# CO<sub>2</sub>-utsläpp i Sverige
I denna uppgift ska vi börja titta på statistik från statistiska centralbyrån ([SCB](https://www.scb.se/)) om CO<sub>2</sub>-utsläpp i Sverige.

För att programmera, gå till [https://replit.com/languages/python3](https://replit.com/languages/python3) och klicka på *create repl*.

## 1. Titta på datafilen

Vi skall använda oss av en modifierad datafil från SCB som vi lagt här:
[https://raw.githubusercontent.com/lunduniversity/schoolprog-satellite/master/exercises/co2_emission_sweden/data.txt](https://raw.githubusercontent.com/lunduniversity/schoolprog-satellite/master/exercises/co2_emission_sweden/data.txt)

### 1.1 Surfa till datafilen

**Uppdrag 1.1:** Börja med att surfa till adressen ovan för att se hur datan ser ut. Notera att:
* Filen har fyra kolumner. Detta kan vara lite svårt att se, för kolumnerna skiljs åt med *tabb*-tecken, som ser likadana ut som blanka. Men när vi programmerar kommer vi att se att det är skillnad.
* I första kolumnen står det `Totala Växthusgaser (kt CO2-ekv.)` på varje rad.
* I andra kolumnen står namnet på en *sektor*, dvs en kategori av utsläpp. T.ex. `NATIONELL TOTAL (exklusive LULUCF, inklusive internationella transporter)` eller `ARBETSMASKINER, TOTALT`.
* I tredje kolumnen står ett årtal.
* I fjärde kolumnen står ett mätvärde (mängden utsläpp).
* Första raden har rubriker för de fyra kolumnerna.

### 1.2 Vad visar raderna i filen?

Varje rad visar utsläpp av växthusgaser inom en viss sektor för ett visst år. Siffrorna gäller utsläpp i Sverige.

Olika växthusgaser, t.ex. metan och koldioxid, har olika mycket växthuseffekt. För att kunna lägga ihop utsläpp från olika gaser har de därför räknats om till motsvarande mängd koldioxid ("koldioxid-ekvivalenter").

Mätvärdet längst till höger på varje rad räknas i "kt CO2-ekv", alltså kiloton koldioxid-ekvivalenter. (Ett kiloton är 1000 ton.)

**Uppdrag 1.2:** Kan du lista ut från filen hur många kiloton koldioxid-ekvivalenter som släpptes ut från sektorn `ARBETSMASKINER, TOTALT` under år 2002?

<details>
<summary markdown="span">
Svar
</summary>
<p>
3511.3 kiloton
</p>
</details>
<p></p>

### 1.3 Vad betyder de olika sektorerna?

Sektorn som heter `NATIONELL TOTAL ...` är summan av alla de andra sektorerna. De andra sektorerna är utsläpp från specifika kategorier:
* arbetsmaskiner
* avfall
* el och fjärrvärme
* industri
* inrikes transporter
* utrikes transporter
* jordbruk
* lösningsmedel och övrig produktanvändning
* uppvärmning av bostäder och lokaler

**Uppdrag 1.3:** Vad kan man tänka sig för exempel på utsläpp från de olika sektorerna? Försök hitta ett exempel för varje sektor.

*Tips* Läs om sektorerna här: [http://www.naturvardsverket.se/Sa-mar-miljon/Statistik-A-O/Vaxthusgaser-territoriella-utslapp-och-upptag/](http://www.naturvardsverket.se/Sa-mar-miljon/Statistik-A-O/Vaxthusgaser-territoriella-utslapp-och-upptag/)

<details>
<summary markdown="span">
Svar
</summary>
<p>
Några exempel:
<ul>
<li> arbetsmaskiner: utsläpp från diesel-driven grävmaskin</li>
<li> avfall: metan från soptipp</li>
<li> el och fjärrvärme: utsläpp från kolkraftverk</li>
<li> industri: utsläpp vid tillverkning av stål</li>
<li> inrikes transporter: utsläpp från personbil</li>
<li> utrikes transporter: båt som avgår från Sverige och där bränslet köpts i Sverige</li>
<li> jordbruk: metan från kor som rapar och fiser</li>
<li> lösningsmedel och övrig produktanvändning: läckage från kylsystem</li>
<li> uppvärmning av bostäder och lokaler: hus med oljepanna</li>
</ul>
</p>
</details>
<p></p>

En sektor som *inte* är med i vår statistik-fil är "LULUCF". Det är en engelsk förkortning för "markanvändning, förändrad markanvändning och skogsbruk". Här har Sverige *negativa* utsläpp, dvs mer och mer koldioxid binds på olika sätt, till exempel på grund av att skogen växer.

## 2. Python Dictionaries (nyckel-värdetabeller)

För att programmera denna uppgift behöver vi veta lite om en datastruktur som kallas *dictionaries*, eller *nyckel-värdetabell* på svenska. (Kallas ibland också *map* eller *lexikon*.)

Iden är enkel: Vi har sett att vi kan accessa enskilda element i en lista med hjälp av index inom hakparenteser. T.ex.
```python
lista = ["hej", "på", "dej"]
print(lista[0]) # Skriver ut "hej"
```

När vi accessar ett element i en lista kan vi tänka på detta som att värdena i listan är numrerade (från 0), och vi slår upp vad värdet är på en viss plats.

Vi kan tänka på en lista som en sekvens av värden, antingen så här:

<table><tr><td>"hej"</td><td>"på"</td><td>"dej"</td></tr></table>

eller så här:

<table>
<tr><td>"hej"</td></tr>
<tr><td>"på"</td></tr>
<tr><td>"dej"</td></tr>
</table>

Vi kan också tänka oss listan som en tabell från index till värden:

|index|värde |
|:---:|:----:|
| 0   | "hej"|
| 1   | "på" |
| 2   | "dej"|

Vore det inte bra om vi kunde indexera med något annat än tal? Det kan vi göra med nyckel-värdetabeller.

### 2.1 Skapa en nyckel-värdetabell

En nyckel-värdetabell är helt enkelt en speciell slags lista där varje element består av en *nyckel* och ett *värde*.

Visuellt kan vi tänka oss en nyckel-värdetabell så här:

|nyckel|värde |
|:---:|:----:|
| "apelsin" | "gul"|
| "banan"   | "gul" |
| "päron"   | "grön"|
| "lingon"  | "röd"|


**Uppdrag 2.1:** Kör följande kod som skapar en nyckel-värdetabell `color` där vi kan slå upp färgen på olika saker.

```python
color = {
  "apelsin": "gul",
  "banan": "gul",
  "päron": "grön",
  "lingon": "röd"
}
print(color["päron"])
```
Vi kan tänka på uttrycket `color["päron"]` som att vi slår vi upp i tabellen `color` för att se vilken färg `"päron"` har.

Vad skrivs ut av programmet?

(Hittar du inte krullparenteserna `{}`? På Mac håller du nere Shift och Alt samtidigt, och trycker på de vanliga parenteserna. På Windows använder du Alt-Gr.)

<details>
<summary markdown="span">
Svar
</summary>
<p>
grön
</p>
</details>
<p></p>

Att notera:
* Varje element i tabellen har en *nyckel*, t.ex. `"päron"` och ett *värde*, t.ex. `"grön"`. Man skriver kolon mellan nyckeln och värdet.
* Tabellen skrivs med *krullparenteser* , `{` och `}`, runt om, i stället för hakparenteser som vi använde för vanliga listor. Krullparenteser används när ordningen mellan elementen inte spelar någon roll.
* När man slår upp något i tabellen används hakparenteser, precis som för vanliga listor.
* Alla nycklarna i tabellen är *olika*. Om vi skulle försöka lägga till ytterligare ett elementet för `"päron"` i tabellen, så kommer bara det senast tillagda att finnas kvar.
* Vi har skrivit elementen på varsin rad för att det skall bli lätt att läsa koden. Vi hade kunnat skriva hela tabellen på en rad om vi hade velat.


<!--
### 2.2 Skriv ut hela listan
- med print
- med en loop

en apelsin är orange
en druva är blå
ett äpple är grönt
ett päron är grönt
en jordgubbe är röd
en köttbulle är brun
en falafel är brun
en gurka är grön
en tomat är röd
en hammare är hård
en lampa är ljus
en squash är grön

-->

### 2.2 Skapa en egen nyckel-värdetabell

**Uppdrag 2.2:** Skapa en nyckel-värdetabell `capital` (huvudstad) som mappar länder till huvudstäder. Om vi till exempel accessar `capital["Sverige"]` så skall resultatet bli `"Stockholm"`.

Som hjälp får du detta kodskelett (byt ut `...` mot rätt sak).

```python
capital = {
  "Sverige": ...,
  "Norge": ...,
  "Danmark": ...,
  "Finland": ...
}
print(capital["Sverige"])
```

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>capital = {
  "Sverige": "Stockholm",
  "Norge": "Oslo",
  "Danmark": "Köpenhamn",
  "Finland": "Helsingfors"
}
print(capital["Sverige"])
</code></pre>
</p>
</details>
<p></p>

### 2.3 Felaktig nyckel

Vad händer om vi försöker slå upp värdet för en nyckel som inte finns med i tabellen?

**Uppdrag 2.3:** Slå upp ett land som inte finns med i tabellen. T.ex. `capital["Island"]`. Vilket fel får du?

<details>
<summary markdown="span">
Svar
</summary>
<p>Man får felet <code>KeyError</code>. Alltså att man använt en nyckel som inte finns med i tabellen.
</p>
</details>
<p></p>

### 2.4 Skapa en nyckel-värdetabell successivt

I stället för att skapa en nyckel-värdetabell på en gång, så kan vi skapa den successivt. Vi börjar med att skapa en tom nyckel-värdetabell, och sedan kan vi lägga in värden efter hand.

Här är ett exempel:
```python
color = {}    # Skapa en tom nyckel-värdetabell
color["apelsin"] = "gul"
color["banan"] = "gul"
color["päron"] = "grön"
color["lingon"] = "röd"
```

Vid ett senare tillfälle kan vi nu lägga till exempelvis
```python
color["blåbär"] = "blå"
```

**Uppdrag 2.4:** Skriv kod för att lägga till fler länder, som t.ex. Island i din tabell `capital`. Prova att din kod fungerar genom att skriva ut några av de städer du lagt till. Till exempel:
```python
print(capital["Island"])
```

### 2.5 Typen `dict`

En nyckel-värdetabell i Python kallas ofta helt enkelt `dict` som förkortning för *dictionary*. Vi kan också se att typen för en nyckel-värdetabell är `dict` genom att skriva ut den på följande sätt:

```python
print(type(capital))
```



## 3. List slices

Hittills har vi bara programmerat med hela listor. Men ibland vill man kunna kopiera ut en *del* av en lista, en så kallad *slice*. Det kan man göra med notationen `lista[start:stop]`.

### 3.1 Enkla slices

**Uppdrag 3.1 a:** Kör följande kod som skapar en lista och kopierar ut några av elementen till en ny lista:

```python
lista = ["hej", "på", "dej", "du", "glade"]
s = lista[1:3]
print(s)
```

Att observera:
* Här gör vi en slice som startar på index `1` (alltså det andra elementen eftersom listor numreras från `0`).
* Slicens sista element är `2`. Argumentet `3` är alltså elementet *efter* det sista elementet i slicen.
* Vi får en ny lista som motsvarar slicen, och den ursprungliga listan ändras inte.

**Uppdrag 3.1 b:** Använd slice-notationen för att skriva ut följande listor:
* `["hej", "på", "dej"]`
* `["du", "glade"]`

*Tips!* Utgå från följande kodskelett `print(lista[ ... : ... ])`, och byt ut `...` mot något lämpligt tal.

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>print(lista[0:3])
print(lista[3:5])
</code></pre>
</p>
</details>
<p></p>

### 3.2 Slices från början eller slutet

Om vi vill skapa en slice från listans början, så kan vi utelämna `start`-argumentet.

**Uppdrag 3.2 a:** Prova att skriva ut `["hej", "på", "dej"]` genom att köra följande kod:

```python
print(lista[:3])  # Samma sak som lista[0:3]
```

**Uppdrag 3.2 b:** Skriv liknande kod som skriver ut `["hej", "på", "dej", "du"]`.

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>print(lista[:4])
</code></pre>
</p>
</details>
<p></p>

På liknande sätt kan du utelämna `stop`-argumentet och därmed ta ut slutet av en lista.

**Uppdrag 3.2 c:** Prova att skriva ut `["du", "glade"]` genom att köra följande kod:

```python
print(lista[3:])  # Samma sak som lista[3:5]
```

**Uppdrag 3.2 d:** Skriv liknande kod som skriver ut `["på", "dej", "du", "glade"]`. Dvs, alla element ska med utom det första.

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>print(lista[1:])
</code></pre>
</p>
</details>  
<p></p>

**Uppdrag 3.2 e:** Vilken lista får du med uttrycket `lista[:]`? Alltså där både start och stopp-index har utelämnats?

<details>
<summary markdown="span">
Svar
</summary>
<p>Du får en slice med alla elementen. Alltså en kopia av listan.
</p>
</details>  
<p></p>


### 3.3 Listor/Slices med negativa index
Man kan ange ett negativt index för en lista. Då räknas positionen bakifrån i stället för framifrån. T.ex. betyder `lista[-1]` det sista elementet i listan, `lista[-2]` det näst sista, osv.

**Uppdrag 3.3 a:** Skriv kod som skriver ut det tredje sista elementet i `lista`.

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>print(lista[-3])
</code></pre>
</p>
</details>  
<p></p>

Negativa index kan användas också för start och stopp-index i en slice. T.ex. betyder `lista[1:-1]` att man får en ny lista utan både första och sista elementet i `lista`.

**Uppdrag 3.3 b:** Skriv kod som skriver ut `["dej", "du"]` med hjälp av ett positivt start-index och ett negativt stopp-index.

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>print(lista[2:-1])
</code></pre>
</p>
</details>  
<p></p>

### 3.4 Slices med steg

Genom att skriva `lista[start:stop:steg]` kan vi ta en slice som tar med t.ex. vartannat eller vart tredje element i listan. Till exempel kommer `lista[::2]` att ge en ny lista med bara vartannat element.

**Uppdrag 3.4:** Skriv kod som skriver ut vart tredje element av `lista`

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>print(lista[::3])
</code></pre>
</p>
</details>
<p></p>

### 3.5 Vänd på en lista med negativt steg

Om man anger ett negativt steg så får man elementen i baklänges ordning. Till exempel kan vi få vartannat element i baklänges ordning med `lista[::-2]`

**Uppdrag 3.5:** Vilken lista får du om du skriver `lista[::-1]`?

<details>
<summary markdown="span">
Lösning
</summary>
<p>Du får samma lista men i baklänges ordning.
</p>
</details>
<p></p>


## 4. Hämta data över internet

Hittills har vi bara skrivit experimentkod. Du kan nu ta bort (eller kommentera bort) denna kod. Nu ska vi läsa in filen vi tittade på tidigare.

### 4.1 Hämta filen över internet

**Uppdrag 4.1:** Vi ska börja med att hämta filen från internet med hjälp av biblioteket `requests` som kan göra anrop över "http-protokollet" (det kommunikationsprotokoll som används för att hämta webbsidor). Kör följande kod:

```python
import requests
response = requests.get("...")
data = response.text
print(data)
```

Den URL du skall använda i stället för `...` ovan är
[https://raw.githubusercontent.com/lunduniversity/schoolprog-satellite/master/exercises/co2_emission_sweden/data.txt](https://raw.githubusercontent.com/lunduniversity/schoolprog-satellite/master/exercises/co2_emission_sweden/data.txt)

Om du gjort rätt fick du nu in all datan i variabeln `data` och printade ut samma sak igen.

Att notera:
* Biblioteket `requests` används för att läsa filer över internet.
* Anropet `get` hämtar en fil över internet, och svaret lagras i variabeln `response`.
* Själva fil-innehållet finns i `text`-variabeln i svaret.

Du kan nu kommentera bort anropet `print(data)`.

### 4.2 Splitta upp raderna

Nästa steg är att splitta upp datan i en lista med rader. Det kan vi göra med funktionen `splitlines()`:

<!--Kom ihåg att rader är separerade med "newline" som skrivs som `\n`. Vi kan alltså skapa listan med rader genom följande kod:
-->

```python
lines = data.splitlines()
```


**Uppdrag 4.2:** Splitta nu upp datan i rader med koden ovan. Hur många rader blev det?

*Tips!* Använd `print` och `len` för att ta reda på antalet rader.

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>lines = data.splitlines()
print(len(lines))
</code></pre>
Det blir 281 rader.
</p>
</details>
<p></p>

Vi har nu en lista `lines` som motsvarar filen. Hur ska vi kunna plotta datan? Vi behöver göra flera steg:
* Vi behöver skala bort rubrikraden.
* Vi behöver dela in varje återstående rad i kolumner.
* Vi skulle vilja skapa en nyckelvärde-tabell från sektor till lista av mätvärden
* Sedan skulle vi vilja göra ett fint diagram så att vi kan se hur utsläppen ökar eller minskar från år till år.

Vi ska nu göra varje sak i tur och ordning.

### 4.3 Ta bort rubrikraden

Första raden i filen är ju en rubrikrad. Den vill vi inte ha med när vi ska göra beräkningar på datan.

**Uppdrag 4.3:** Skapa en ny lista `data_lines` som är likadan som `lines`, men som inte har med första raden.

*Tips!* Använd en slice som tar med alla rader utom den första.

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>data_lines = lines[1:]
</code></pre>
</p>
</details>
<p></p>

Om du vill försäkra dig om att du programmerat rätt så kan du skriva ut t.ex. `data_lines[0]` så att du ser att första raden inte är rubrikraden.


### 4.4 Dela upp varje rad i kolumner

Nu har vi de intressanta raderna i listan `data_lines`. Varje rad i listan är en textsträng. Visuellt kan vi tänka oss `data_lines` så här:

data_lines:
<table>
<tr><td>"Totala ... NATIONELL ... 1990 ... 74921.1"</td></tr>
<tr><td>"Totala ... NATIONELL ... 1991 ... 75267.7"</td></tr>
<tr><td>"..."</td></tr>
</table>

Nästa steg är att skapa en ny lista där varje rad i stället är uppdelad i kolumnvärden. Vi kan kalla denna lista `raw_data` (rådata). Visuellt kan vi tänka oss den nya listan så här:

raw_data:
<table>
<tr>
  <td>
  <table>
  <tr align=center>
    <td width=150>"Totala ..."</td>
    <td width=150>"NATIONELL ..."</td>
    <td width=150>"1990"</td>
    <td width=150>"74921.1"</td>
  </tr>
  </table>
  </td>
</tr>
<tr>
  <td>
  <table>
  <tr align=center>
    <td width=150>"Totala ..."</td>
    <td width=150>"NATIONELL ..."</td>
    <td width=150>"1991"</td>
    <td width=150>"75267.7"</td>
  </tr>
  </table>
  </td>
</tr>
<tr>
<td>
<table>
<tr align=center>
  <td width=150>"..."</td>
  <td width=150>"..."</td>
  <td width=150>"..."</td>
  <td width=150>"..."</td>
</tr>
</table>
</td>
</tr>
</table>

Detta blir alltså en lista av rader där varje rad är en lista av kolumnvärden.

Vi kan skapa den nya listan `raw_data` genom att gå igenom `data_lines` med en `for`-loop och lägga till ett element för varje rad. Elementet skall vara en lista av kolumnvärden som vi kan få genom att splitta raden efter tabb-tecken. Tabb-tecken skrivs som `\t` när man programmerar. Vi kan få listan genom att göra `split("\t")` på raden.

Här är koden för att skapa `raw_data`:

```python
# Skapa lista av rådata, med en lista per rad
# Splitta på tabbar för att få de 4 elementen per rad
raw_data = []
for line in data_lines:
  raw_data.append(line.split("\t"))
```

**Uppdrag 4.4 a:** Kör koden ovan för att skapa listan `raw_data`.

Vad vi fått nu är en lista av listor enligt figuren ovan: varje element i `raw_data` är i sig en lista med fyra element, ett för varje kolumn.

**Uppdrag 4.4 b:** För att förstå strukturen på `raw_data`, prova att skriva ut första raden med `print(raw_data[0])`. Du ser att raden består av en lista med fyra värden.

Hur kan vi skriva ut ett av de fyra värdena? Vi kan till exempel skriva ut det fjärde värdet så här:

```python
r = raw_data[0]
c = r[3]
print(c)
```

Eller helt enkelt:
```python
print(raw_data[0][3])
```

Här beräknas först `raw_data[0]`, och resultatet är en lista. Sedan indexeras denna lista med `[3]` och resultatet är det fjärde värdet i listan. Sist skrivs detta värde ut.

**Uppdrag 4.4 c:** Skriv ut det tredje värdet på den första raden i `raw_data` (alltså året).

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>print(raw_data[0][2])
</code></pre>
</p>
</details>
<p></p>

### 4.5 Skapa en nyckel-värdetabell

Nu har vi rådata med rader och kolumner i `raw_data`. Nästa steg är att skapa en nyckel-värdetabell, så att vi för varje sektor kan slå upp en lista av mätvärden. Vi kan kalla denna tabell `data_by_sector`. Visuellt kan vi tänka oss den så här:

data_by_sector:
<table>
<tr>
  <th>nyckel</th>
  <th>värde</th>
</tr>
<tr>
  <td> "NATIONELL ..."</td>
  <td>
  <table>
  <tr align=center>
    <td width=135>74921.1</td>
    <td width=135>75267.7</td>
    <td width=135>...</td>
  </tr>
  </table>
  </td>
</tr>
<tr>
  <td> "ARBETSMASKINER ..."</td>
  <td>
  <table>
  <tr align=center>
  <td width=135>3166.2</td>
  <td width=135>2973.3</td>
  <td width=135>...</td>
  </tr>
  </table>
  </td>
</tr>
<tr>
  <td> "..."</td>
  <td>
  <table>
  <tr align=center>
  <td width=135>...</td>
  <td width=135>...</td>
  <td width=135>...</td>
  </tr>
  </table>
  </td>
</tr>
</table>

Vi kan skapa `data_by_sector` på följande sätt:
* Gå igenom alla raderna i `raw_data`.
* För varje rad tar vi ut sektorn (kolumn 2) och mätvärdet (kolumn 4).
* Om sektorn inte redan finns i tabellen, så lägger vi till den, med en tom lista som värde.
* Sedan lägger vi till mätvärdet till sektorns lista.

Här är koden för att skapa `data_by_sector`:

```python
# Skapa en nyckel-värdetabell från sektor (kolumn 2) till lista med mätvärden (kolumn 4)
data_by_sector = {}
for line in raw_data:
  # extrahera sektorn (kolumn 2)
  sector = line[1]
  # om sektorn inte redan finns i nyckel-värdetabellen, så skapa en tom lista för sektorn
  if (sector not in data_by_sector):
    data_by_sector[sector] = []
  # Lägg till mätvärdet till rätt sektor
  data_by_sector[sector].append(float(line[3]))
```

**Uppdrag 4.5:** Lägg till koden för att skapa `data_by_sector`, och prova att slå upp en sektor, t.ex. `"ARBETSMASKINER, TOTALT"`. Du bör få ut en lista av mätvärden.

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>print(data_by_sector["ARBETSMASKINER, TOTALT"])
</code></pre>
</p>
</details>
<p></p>

## 5. Plotta

Nu ska vi plotta värdena för de olika sektorerna.

### 5.1 Plotta totala utsläppen

Vi börjar med att plotta de totala utsläppen, alltså sektorn `NATIONELL TOTAL (exklusive LULUCF, inklusive internationella transporter)`.

På x-axeln vill vi ha åren (1990-2017), och på y-axeln de totala utsläppen för respektive år.

**Uppdrag 5.1 a:** Skapa en lista `years` för värdena på x-axeln. *Tips!* Skapa en `range` och gör om den till en lista med `list`.

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>years = list(range(1990, 2018))
</code></pre>
</p>
</details>
<p></p>

**Uppdrag 5.1 b:** Plotta de totala utsläppen till en fil `totalco2.png`.

*Tips!* Du behöver:
* importera plot-biblioteket och slå på interactive mode
* slå upp y-värdena i `data_by_sector`
* anropa `plot`-funktionen
* anropa `savefig`-funktionen för att visa och spara diagrammet

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>import matplotlib.pyplot as plt
plt.ion()
y = data_by_sector["NATIONELL TOTAL (exklusive LULUCF, inklusive internationella transporter)"]
plt.plot(years, y)
plt.savefig("totalco2.png")
</code></pre>
</p>
</details>
<p></p>

**Uppdrag 5.1 c:** För att du ska kunna tolka kurvan bättre kan du lägga till följande anrop:

```python
plt.grid()
plt.ylim(0, 100000)
```
Observera att
* `grid` slår på ett rutnät i diagrammet, så att vi lättare kan läsa av värdena
* `ylim` anger gränserna för y-axeln. Genom att låta y-axeln börja på 0 ser vi lättare hur mycket utsläppen har minskat eller ökat.

**Uppdrag 5.1 d:** Läs av i diagrammet: Hur mycket har vi släppt ut som mest? Vilket år var det? Hur mycket släppte vi ut 2017?

<details>
<summary markdown="span">
Svar
</summary>
<p>År 1996 släppte vi ut som mest, strax över 80000 kiloton. År 2017 hade utsläppen sjunkit till strax över 60000 kiloton.
</p>
</details>
<p></p>

**Uppdrag 5.1 e:** Kurvan visar ju bara utsläpp inom Sverige. Vilka andra utsläpp kan man tänka sig att Sveriges befolkning orsakar?

<details>
<summary markdown="span">
Svar
</summary>
<p>Sverige importerar stora mängder varor som odlas eller tillverkas i andra länder, och motsvarande utsläpp är inte med. Dessutom reser vi mycket, och flyger man från andra länder är de utsläppen inte heller med i datan vi har tittat på. Ett par länkar:
<ul>
<li><a href="https://www.svt.se/nyheter/vetenskap/svenskars-klimatpaverkan-utomlands-allt-storre">https://www.svt.se/nyheter/vetenskap/svenskars-klimatpaverkan-utomlands-allt-storre</a></li>
<li><a href="https://www.naturvardsverket.se/Nyheter-och-pressmeddelanden/Nyhetsarkiv/Nyheter-och-pressmeddelanden-2019/Svensk-konsumtion-orsakar-stora-utslapp-i-utlandet-/">https://www.naturvardsverket.se/Nyheter-och-pressmeddelanden/Nyhetsarkiv/Nyheter-och-pressmeddelanden-2019/Svensk-konsumtion-orsakar-stora-utslapp-i-utlandet-/</a></li>
</ul>
</p>
</details>
<p></p>


### 5.2 Plotta ett stapeldiagram

I stället för att plotta en kurva kan vi plotta ett stapeldiagram. Vi använder då anropet `bar` (stapel) i stället för `plot`.

**Uppdrag 5.2:** Prova att plotta totala utsläppen som ett stapeldiagram i stället för en kurva.


### 5.3 Plotta sektor för sektor

**Uppdrag 5.3 a:** Vi ska nu göra en ny plot. Lägg till anropet `plt.close()` efter förra plottens `savefig`, så att nästa diagram inte störs av den tidigare plotten.

Vi skulle nu vilja plotta alla sektorerna i samma diagram.

Vi börjar med att skapa en lista `sectors` av alla sektorer *utom* den med totala utsläppen:

**Uppdrag 5.3 b:** Kör följande kod:

```python
sectors = list(data_by_sector.keys())
sectors.remove("NATIONELL TOTAL (exklusive LULUCF, inklusive internationella transporter)")
```

Att observera:
* anropet `keys` ger oss en lista av alla nycklarna till tabellen `data_by_sector`
* anropet `remove` tar bort sektorn med de totala utsläppen från listan.

Nästa steg är att plotta ett stapeldiagram med en stapel per år (som tidigare), men där varje stapel är uppdelad efter sektor.

Vi gör detta genom att loopa över sektorerna och plotta varje sektor ovanför den förra. Vi håller reda på var i höjdled nästa sektor ska plottas genom en lista `bottoms`.

**Uppdrag 5.3 c:** Kör följande kod för att plotta ett initialt stapeldiagram över alla sektorerna:

```python
import numpy as np

bottoms = np.zeros(len(years)) # Sätt bottenvärdena till 0
for sector in sectors:
    plt.bar(years, data_by_sector[sector], bottom=bottoms, label=sector)
    # Öka bottenvärdena till nästa sektor
    bottoms = np.array(data_by_sector[sector]) + bottoms
plt.legend()
plt.savefig("sektorco2.png")
```

Vi har använt numpy-listor för `bottoms`-värdena i stället för vanliga listor, för det gör att vi kan använda en enkel addition för att öka alla bottenvärdena på en gång.

Plotten vi får ut ser ju tjusig ut - anropen till `bar` ger automatiskt olika färg på alla delstaplarna! Men legenden kommer rakt ovanpå plotten, och dessutom med sektorerna i baklänges ordning jämfört med plotten.

**Uppdrag 5.3 d:** Gör en snyggare plot genom att ändra koden till följande:

```python
import numpy as np

bars = [] # Spara resultaten av anropen till bar
bottoms = np.zeros(len(years))
plt.figure(figsize=(15,10)) # Större figur
for sector in sectors:
    bar = plt.bar(years, data_by_sector[sector], bottom=bottoms, label=sector)
    bars.append(bar) # Spara resultatet
    bottoms = np.array(data_by_sector[sector]) + bottoms
plt.legend(handles=bars[::-1]) # Baklänges ordning
plt.ylim(0, 110000)  # Gör mer plats för legenden
plt.grid()           # Lägg till ett rutnär
plt.savefig("sektorco2.png")
```

Det vi gjort här är att:
* Vi anropar `figure` med en större storlek på plotten (15 x 10 tum). Då blir legenden relativt sett mindre, och får bättre plats.
* Vi sparar resultatet av varje anrop till `bar` i en variabel. Dessa samlas upp i en lista `bars`. Listan kan vi vända baklänges och använda i anropet till `legend`. Då får vi ut legenden i rätt ordning.
* Vi anropar `ylim` med ett lite större värde, så blir hela plotten relativt sett lite lägre, och det blir mer plats till legenden.
* Vi har lagt till en `grid` för att lättare kunna läsa av diagrammet.

**Uppdrag 5.3 e:** Titta på det genererade diagrammet. Hur har de olika sektorerna förändrats sedan 1990? Vilken har minskat mest? Finns det någon sektor som har ökat de senaste åren? Varför tror du sektorerna har ökat eller minskat? Finns det någon sektor som är stor och som borde kunna minska?

*Tips!* Du hittar mer information här: [http://www.naturvardsverket.se/Sa-mar-miljon/Statistik-A-O/Vaxthusgaser-territoriella-utslapp-och-upptag/](http://www.naturvardsverket.se/Sa-mar-miljon/Statistik-A-O/Vaxthusgaser-territoriella-utslapp-och-upptag/)

<details>
<summary markdown="span">
Svar
</summary>
<p>Exempelvis kan vi se att uppvärmning av bostäder och lokaler har minskat mycket sedan 1990 och är idag i princip fossilfri. Tidigare var det vanligt med oljeeldning i enskilda hus. Idag är det vanligt med el kombinerat med värmepumpar, och där elen kommer från vindkraft, vattenkraft, eller kärnkraft. Det är också vanligt med fjärrvärme där värmen kommer från mer effektiv olje- eller koleldning, eller från eldning med biobränsle eller avfall.</p>
<p>Vi kan se att utsläppen från utrikes transporter har ökat. Det är dock svårt att bedöma hur mycket av detta som beror på att mängden transporter har ökat. En del av ökningen kan bero på att det har blivit billigare att tanka i Sverige och att fartyg hellre tankar här än i andra närliggande länder som Danmark.</p>
<p>Utsläpp från industrin är fortfarande stora. Forskning pågår för att hitta industriella processer som ger lägre utsläpp, men det tar tid att ta fram nya processer. Se, t.ex. <a href="https://www.naturvardsverket.se/Miljoarbete-i-samhallet/Miljoarbete-i-Sverige/Uppdelat-efter-omrade/Klimat/Klimatneutralt-Sverige/Industri/">https://www.naturvardsverket.se/Miljoarbete-i-samhallet/Miljoarbete-i-Sverige/Uppdelat-efter-omrade/Klimat/Klimatneutralt-Sverige/Industri/</a>
</p>
</details>
<p></p>
