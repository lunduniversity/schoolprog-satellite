# CO<sub>2</sub>-utsläpp i Sverige
I denna uppgift ska vi börja titta på statistik från statistiska centralbyrån ([SCB](https://www.scb.se/)) om CO<sub>2</sub>-utsläpp i Sverige.

I uppgiften kommer vi att lära oss följande om Python-programmering:
* Läsa in textfiler från internet
* ...

För att programmera, gå till [(https://repl.it/languages/python3](https://repl.it/languages/python3)

## 1. Titta på datafilen

Vi skall använda oss av en modifierad datafil från SCB som vi lagt här:
[https://raw.githubusercontent.com/lunduniversity/schoolprog-satellite/master/exercises/co2_emission_sweden/data.txt](https://raw.githubusercontent.com/lunduniversity/schoolprog-satellite/master/exercises/co2_emission_sweden/data.txt)

### 1.1 Surfa till datafilen

**Uppdrag:** Börja med att surfa till denna adress för att se hur datan ser ut. Notera att:
* Första raden har rubriker för de olika kolumnerna (fyra stycken)
* Kolumnerna är separerade med *tabb*-tecken. Det är svårt att se skillnad på tabbar och blanktecken med blotta ögat, men om vi använder programmering kommer vi att se att det är skillnad.

### 1.2 Vad visar raderna i filen?

Varje rad visar utsläpp av växthusgaser för ett visst år. Olika växthusgaser har olika mycket växthuseffekt. För att kunna lägga ihop utsläpp från olika gaser räknas de därför om till motsvarande (ekvivalent) mängd koldioxid.

Mätvärdet längst till höger på varje rad visar antalet "kt CO2-ekv", alltså kiloton koldioxid-ekvivalenter. (Ett kiloton är 1000 ton.)

Kategorin som heter `NATIONELL TOTAL (exklusive LULUCF, inklusive internationella transporter)` är det totala koldioxidutsläppet från Sverige mätt i tusen ton CO2-ekvivalenter.

**Uppdrag:** Kan du lista ut från filen hur många kiloton koldioxid-ekvivalenter som släpptes ut från ARBETSMASKINER i Sverige under år 2002?

<details>
<summary markdown="span">
Svar
</summary>
<p>
3511.3 kiloton
</p>
</details>

## 2 Python Dictionaries (nyckel-värde-tabeller)

För att programmera denna uppgift behöver vi veta lite om en datastruktur som kallas *dictionaries*, eller *nyckel-värdetabell* på svenska. (Kallas ibland också *map* eller *lexikon*)

Iden är enkel: Vi har sett att vi kan accessa enskilda element i en lista med hjälp av index inom hakparenteser. T.ex.
```python
lista = ["hej", "på", "dej"]
print(lista[0])
```

När vi accessar ett element i en lista kan vi tänka på detta som att värdena i listan är numrerade (från 0), och vi slår upp vad värdet är på en viss plats.

Vore det inte bra om vi kunde indexera med något annat än tal? Det kan vi göra med nyckel-värdetabeller.

### 2.1 Skapa en nyckel-värdetabell

En nyckel-värdetabell är helt enkelt en speciell slags lista där varje element består av en *nyckel* och ett *värde*.

**Uppdrag:** Kör följande kod som skapar en nyckel-värdetabell från frukter till färg.

```python
fruitcolor = {
  "apelsin": "gul",
  "banan": "gul",
  "päron": "grön",
  "lingon": "röd"
}
print(fruitcolor["päron"])
```
Vad skrivs ut?

(Hittar du inte krullparenteserna? På Mac håller du nere Shift och Alt samtidigt, och trycker på de vanliga parenteserna. På Windows använder du Alt-Gr.)

<details>
<summary markdown="span">
Svar
</summary>
<p>
grön
</p>
</details>

Vi kan tänka på uttrycket `fruitcolor["päron"]` som att vi slår vi upp i tabellen `fruitcolor` för att se vilken färg `"päron"` har.

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

### 2.3 Lägg till något till en nyckel-värdetabell

-->

### 2.2 Skapa en egen nyckel-värdetabell

**Uppdrag:** Skapa en nyckel-värdetabell `co2` somvi kan använda för att slå upp koldioxidutsläppen för arbetsmaskiner för åren 2002-2004. Slå sedan upp värdet för 2003 och skriv ut det.

Som hjälp får du detta kodskelett (byt ut `...` mot rätt sak).

```python
co2 = {
  2002: ...,
  2003: ...,
  2004: ...
}
print(co2[...])
```
<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>
co2 = {2002: 3511.3, 2003: 3548.9, 2004: 3575.9}
print(co2[2003])
</pre></code>
</p>
</details>

## 3. Hämta data över internet

Du kan ta bort (eller kommentera bort) din tidigare kod. Nu ska vi läsa in filen vi tittade på tidigare.

### 3.1 Hämta filen över internet

**Uppdrag:** Kör följande kod:

```python
import requests
response = requests.get("https://raw.githubusercontent.com/lunduniversity/schoolprog-satellite/master/exercises/co2_emission_sweden/data.txt")
data = response.text
print(data)
```

Om du gjort rätt fick du nu in all datan i variabeln `data` och printade ut samma sak igen.

Att notera:
* Biblioteket `requests` används för att läsa filer över internet.
* När man gör `get` hämtas en fil över internet
* Resultatet från `get` är "svaret" från hämtningen, och vi lägger det i variabeln `response`
* Själva fil-innehållet finns i `text`-variabeln i svaret.

Du kan nu kommentera bort `print(data)`.

### 3.2 Splitta upp raderna

**Uppdrag:** Splitta nu upp datan i rader, som vi gjorde i tidigare uppgift genom att köra nedanstående kod. (Kom ihåg att rader är separerade med "newline" som skrivs som `\n`.) Hur många rader blev det? (Använd `print` och `len` för att ta reda på det.)

```python
rows = data.split("\n")
```
<details>
<summary markdown="span">
Lösning
</summary>
Gör:
<p><pre><code>
print(len(rows))
</pre></code>
Det blir 281 rader.
</p>
</details>

### 3.3 Stoppa in datan i en nyckel-värdetabell

**Uppdrag:** Kör följande kod för att skapa en nyckel-värdetabell från kategori till lista av mätvärden.

(Detta behöver göras steg för steg så man förstår vad som händer. Får fixa senare.)

```python
# Ta ut dataraderna (alla utom rubrikraden)
data_rows = rows[1:]

# Skapa lista av rådata, med en lista per rad
# Splitta på tabbar för att få de 4 elementen per rad
raw_data = []
for row in data_rows:
  raw_data.append(row.split("\t"))

# Skapa en nyckel-värdetabell från kategori (kolumn 2) till lista med mätvärden (kolumn 4)
data_by_category = {}
for measure in raw_data:
  # extrahera kategorin (kolumn 2)
  category = measure[1]
  # om kategorin inte redan finns i nyckel-värdetabellen, så skapa en tom lista för kategorin
  if (category not in data_by_category):
    data_by_category[category] = []
  # Lägg till mätvärdet till rätt kategori
  data_by_category[category].append(float(measure[3]))
```

Nu har vi skapat en nyckel-värdetabell där vi kan slå upp varje kategori (t.ex. ARBETSMASKINER), och få en lista av mätvärden.

## 4. Plotta

Behöver förklaras mer.

### 4.1 Plotta totala utsläppen

Kör följande kod:

```python
import matplotlib.pyplot as plt
years = [i for i in range(1990, 2018)]
y = data_by_category['NATIONELL TOTAL (exklusive LULUCF, inklusive internationella transporter)']
plt.grid(True)
plt.plot(years, y)
plt.ylim(0, 100000)
plt.savefig("totalco2.png")
```
Hur mycket har vi släppt ut som mest, hur mycket släppte vi ut 2017?

### 4.2 Plotta sektor för sektor

Kör följande kod:

```python
import numpy as np

bars = []
categories = list(data_by_category.keys())
categories = categories[1:]
bottoms = np.zeros(28)

for category in categories:
    bar = plt.bar(years, data_by_category[category], 0.5, bottom=bottoms)
    bars.append(bar)
    bottoms = np.array(data_by_category[category]) + bottoms

bars = []
bottoms = np.zeros(28)
plt.figure(figsize=(15,10))
for category in categories:
    bar = plt.bar(years, data_by_category[category], 0.5, bottom=bottoms)
    bars.append(bar)
    bottoms = np.array(data_by_category[category]) + bottoms
plt.grid(True)
plt.ylim(0, 110000)
plt.legend(tuple(map(lambda x:x[0], bars))[::-1], tuple(categories[::-1]))
plt.savefig("sektorco2.png")
```

Hur har de olika kategorierna förändrats sedan 1990? Vilken har minskat mest?

<details>
<summary markdown="span">
Svar
</summary>
Uppvärmning av bostäder och lokaler har minksat mycket sedan 1990 och är idag i princip fossilfri.
</details>


# LICENSE
Källa: Statistiska Centralbyrån. Datan som används i uppgiften är hämtad under Creative Commons Erkännande 4.0 Internationell [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.sv). Orginalfilerna har modifierats.

# Datafiler
- `data.txt` innehåller utsläppt för olika sektorer i Sverige.
- `data.zip` är den zippade versionen av `data.txt`.
