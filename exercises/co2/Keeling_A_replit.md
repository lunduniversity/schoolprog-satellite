# Keelingkurvan A

I denna uppgift ska vi börja utforska Keelingkurvan som beskriver koldioxidhalten i atmosfären. Mätningarna påbörjades av forskaren Charles Keeling och har utförts sedan 1958 på vulkanen Mauna Loa på Hawaii. Observationerna på Mauna Loa var de första att tyda på att koldioxidhalten ökar i vår atmosfär.

Gå till följande exempel på repl.it där vi förberett datafilen: [https://repl.it/@TeodorBucht1729/Keelingkurvan](https://repl.it/@TeodorBucht1729/Keelingkurvan)

## 1. Titta på datafilen

Börja med att titta på datafilen (`data.txt`).

### 1.1 Kolumner

Ser du att filen har 7 kolumner? Gör fönstret lite bredare om du inte kan se det. (Till vänster om filen visar repl.it radnummer, men de är inte med i själva filen.)

### 1.2 År och månad

Varje rad visar en mätning. De två första kolumnerna visar år och månad för mätningen.

**Läs av i filen:** När gjordes den första mätningen?

<details>
<summary markdown="span">
Svar
</summary>
<p>
Mars 1958
</p>
</details>
<p></p>

### 1.3 Året på decimalform

Den tredje kolumnen innehåller tidpunkten på decimalform, räknat i år. Varje mätpunkt motsvarar mitten av en månad. Till exempel kommer mitten av januari 1959 att representeras som `1959 + 15.5/365`. (Eftersom januari har 31 dagar så blir mitten av januari 15.5 dagar efter årssskiftet).

**Uppdrag:** Kör `print(1959 + 15.5/365)` i repl.it för att se tidpunkten i decimalform för mitten av januari 1959. Stämmer det med värdet i tredje kolumnen i filen?

<details>
<summary markdown="span">
Svar
</summary>
<p>
Vi får ut 1959.0424657534247. Detta stämmer bra med raden som börjar med värdena 1959 och 1. Det tredje värdet på raden är 1959.042.
</p>
</details>
<p></p>
När vi programmerar kommer vi att använda dessa decimalformvärden.

### 1.4 Koldioxidhalten

Den fjärde kolumnen innehåller själva mätvärdet, alltså koldioxidhalten. Varje mätvärde är ett medelvärde för månaden.

Koldioxid har den kemiska formeln CO<sub>2</sub>. En molekyl består alltså av en kolatom (C) och två syreatomer (O<sub>2</sub>).

Koldioxidhalten mäts i "ppm" vilket betyder "parts per million". Man mäter hur många CO<sub>2</sub>-molekyler det finns, och jämför med totala antalet molekyler i torkad luft. Värdena beskriver alltså hur många CO<sub>2</sub>-molekyler det finns per miljon molekyler i luften (vatten borträknat).

**Läs av i filen:** Vad var CO<sub>2</sub>-halten för januari 1959?

<details>
<summary markdown="span">
Svar
</summary>
<p>
315.62
</p>
</details>
<p></p>

### 1.5 Interpolerade koldioxidvärden

Det kan saknas värden för vissa månader. Kanske var mätutrustningen sönder, eller stördes av ett lokalt vulkanutbrott.

Ett saknat värde i kolumn 4 representeras som talet `-99.99`. Titta på juni 1958. Kan du se det saknade värdet?

För att lösa problemet med saknade värden kan man räkna ut vad värdet *borde* ha varit. Det gör man genom att använda de riktiga uppmätta värdena på båda sidor om det saknade värdet. Detta kallas att man *interpolerar*.

Kolumn 5 visar interpolerade värden. Titta på maj, juni och juli 1958. För maj och juli visas de riktiga uppmätta värdena i kolumn 5, alltså samma som i kolumn 4. För juni har ett interpolerat värde räknats ut.

**Läs av i filen:** Vad är det interpolerade värdet för juni 1958?

<details>
<summary markdown="span">
Svar
</summary>
<p>
317.10
</p>
</details>
<p></p>

Ser du förresten att det interpolerade värdet *inte* ligger precis mitt emellan värdena före och efter? Ett smartare sätt har använts för att räkna ut värdet, där man har tagit hänsyn till många värden runt det saknade värdet.

När vi programmerar kommer vi att använda de interpolerade koldioxidvärdena.

### 1.6 Kolumn 6 och 7

Kolumn 6 visar ett trendvärde som vi skall titta på i en senare uppgift. Kolumn 7 visar hur många dagar koldioxidhalten mättes under en månad (-1 betyder att uppgiften saknas).

## 2. Dela upp textsträngar

Datafilen består egentligen bara av rader med text. Vi behöver nu lära oss lite mer programmering så att vi kan plocka ut värdena i filen och använda dem i en plott.


### 2.1 Dela upp en sträng med `split`

För textsträngar, som t.ex. `"Hej svejs i lingonskogen!"`, finns flera användbara funktioner. Funktionen `split` splittar upp strängen i delar och returnerar en lista med delarna.

Här är ett exempel där vi använder `split` för att splitta upp strängen `str` till en lista.

```python
str = "Hej svejs i lingonskogen!"
lst = str.split()
print(lst)
```

**Uppdrag:** Provkör koden ovan. Vilka är elementen i den utskrivna listan? Prova att ändra till en annan sträng och kör programmet igen. Vad händer om du lägger in flera blanktecken i rad?

<details>
<summary markdown="span">
Svar
</summary>
<p>
Elementen i listan är "Hej", "svejs", "i", "lingonskogen!".
</p>
</details>
<p></p>

Några saker att notera:

* Strängar i Python kan skrivas antingen med dubbelfnuttar eller enkelfnuttar. Så `"hej"` och `'hej'` betyder samma sak.
* Strängen splittades upp efter blanktecken, och blanktecknen kom inte med i den resulterande listan.
* Om strängen innehåller tabb-tecken eller andra "whitespace-tecken" (t.ex. ny rad), så behandlas de likadant som blanktecken.


### 2.2 Splitta upp en sträng med tal

Nu vet vi hur man delar upp en sträng med hjälp av split, och får en lista av de ingående orden.

Men datafilen har ju tal i sig. Vad händer om vi delar upp en sträng med tal?

**Uppdrag:** Provkör följande kod. Vad blir det för element i listan?

```python
str = "1.2   17.56    0.33"
lst = str.split()
print(lst)
```

<details>
<summary markdown="span">
Svar
</summary>
<p>
Resultatet blir en lista med strängarna "1.2", "17.56", "0.33".
</p>
</details>
<p></p>

Vi kan notera att elementen är *strängar*, alltså sekvenser av tecken. För att vi skall kunna använda dem som decimaltal behöver de först omvandlas.

### 2.3 Omvandla en sträng till decimaltal med `float`

Om vi har en sträng, t.ex. `"1.2"`, så kan vi omvandla den till ett decimaltal (en float) genom att skriva `float("1.2")`

**Uppdrag:** Följande kod är felaktig eftersom den försöker räkna med ett tal som egentligen är en sträng och inte ett tal. Vad händer när du kör programmet? Kan du rätta programmet genom att anropa `float`?

```python
tal = "1.2"
print(tal+2)
```

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>tal = float("1.2")
print(tal+2)
</code></pre>
</p>
</details>
<p></p>

Saker att notera:

* För att `float` ska fungera krävs det att strängen verkligen motsvarar ett decimaltal. Om du anropar `float` med t.ex. `"hej"` som argument så blir det exekveringsfel. Prova gärna.

## 3. Läsa in datafilen

Nu kan vi läsa in datafilen. Vårt mål är att representera datan som två listor: en lista `years` som innehåller åren på decimalform (värdena i kolumn 3), och en lista `co2` som innehåller de interpolerade koldioxidvärdena (kolumn 5).

Vi skall göra detta i några steg.

Koden vi skrivit hittills har vi bara haft för att experimentera. Du kan ta bort den, eller kommentera bort den genom att skriva en "brädgård", `#`, först på varje kodrad.

### 3.1 Läs in filen

Läs in filen till en lista `lines` genom att först öppna filen och sedan loopa över dess rader. I varje varv i loopen lägger vi till den aktuella raden till `lines`.

**Uppdrag:** Skriv in och kör följande kod.

```python
f = open("data.txt")      # Öppna filen
lines = []                # Skapa en tom lista "lines"
for line in f:            # För varje rad i filen,
  lines.append(line)          # lägg till raden till lines
```

För att veta att något faktiskt hände när vi körde koden ovan kan vi ta reda på hur många rader det blev:

```python
print(len(lines))
```

Vad fick du för resultat?

<details>
<summary markdown="span">
Svar
</summary>
<p>
Filen har 735 rader.
</p>
</details>
<p></p>

### 3.2 Skapa `years` och `co2`

Nu vill vi skapa en lista `years` och en lista `co2` som vi kan använda för att plotta en kurva över koldioxidhalterna.

Problemet är dock att vi fått in innehållet som rader, men det är kolumnerna vi vill åt.

Vi löser problemet med en `for`-loop som går igenom alla raderna. Inuti `for`loopen splittar vi upp raden efter blanktecken. Sedan plockar vi ut det 3:e och 5:e värdet, omvandlar dem till `floats`, och lägger till dem till `years` och `co2`.

**Uppdrag:** Lägg till koden nedan i ditt program för att skapa `years` och `co2`:

```python
years = [] # Skapa tom lista för years
co2 = []   # Skapa tom lista för co2
for line in lines:  # Gå igenom alla rader
  splitted = line.split()          # Splitta upp raden
  years.append(float(splitted[2]))# Lägg till 3:e talet till years
  co2.append(float(splitted[4]))  # Lägg till 5:e talet till co2
```
För att se att något hänt när du kör koden ovan så kan du skriva ut hur långa listorna `years` och `co2` är. Hur långa är de?

<details>
<summary markdown="span">
Svar
</summary>
Lägg till nedanstående kod, så ser du att båda listorna har längden 735.
<p><pre><code>print(len(years))
print(len(co2))
</code></pre>
</p>
</details>
<p></p>

<!--
### 3.3 Förenkla koden (frivilligt)

Egentligen var det onödigt att skapa listan `lines`. Vi kan förenkla koden genom att ta bort `lines`-variabeln och i stället skapa `years` och `co2` direkt när vi läser in raderna från filen.

**Uppdrag:** Förenkla din kod enligt ovan. Skriv ut längden på `years` och `co2` för att kontrollera att din kod verkar göra samma sak som tidigare.

<details>
<summary markdown="span">
Svar
</summary>
<p><pre><code>f = open("data.txt") # Öppna filen
years = []                         # Skapa tom lista "years"
co2 = []                           # Skapa tom lista "co2"
for line in f:                     # För varje rad i filen,
  splitted = line.split()            # Splitta upp raden
  years.append(float(splitted[2]))   # Lägg till 3:e talet till years
  co2.append(float(splitted[4]))     # Lägg till 5:e talet till co2
print(len(years))
print(len(co2))
</code></pre>
</p>
</details>

*Observera!* Det är inte givet att koden utan `lines` är bättre än den med `lines`. På sätt och vis kan koden med `lines` uppfattas som lite enklare eftersom man hanterar ett problem i taget.
-->

## 4. Plotta

### 4.1 Plotta Keelingkurvan

Nu kan vi plotta Keelingkurvan! Vi vill ha `years` på x-axeln och `co2` på y-axeln.

**Uppdrag:** Lägg till följande kod för att plotta kurvan:

```python
import matplotlib.pyplot as plt
plt.ion()
plt.plot(years, co2)
plt.savefig("keeling.png")
```

Hur hög var koldioxidhalten när man började mäta? Vilket år blev c02-halten för första gången högre än 400 ppm? Vilket år passerades 400 ppm helt?

*Tips!* Lägg till anropet `plt.grid()` för att få ett rutnät i plotten så att man lättare kan läsa av värdena.

<details>
<summary markdown="span">
Svar
</summary>
Koldioxidhalten var lite mindre än 320 ppm när man började mäta, 1958. Från kurvan ser det ut som att den första gången gick över 400 ppm cirka år 2014. Vi ser också att kurvan är helt över 400 ppm cirka år 2016.
</p>
</details>
<p></p>

## 5. Quiz

### Fråga 1
Är det någon skillnad på `"x"` och `'x'` i Python?

<details>
<summary markdown="span">
Svar
</summary>
<p>
Nej det är ingen skillnad. Det betyder samma sak.
</p>
</details>
<p></p>

### Fråga 2
Vad skrivs ut av följande kod?
```python
str = "0.0  4.5  2.3"
print(str.split())
```

*   `'0.0 4.5 2.3'`
*   `[0.0, 4.5, 2.3]`
*   `['0.0', '4.5', '2.3']`

<details>
<summary markdown="span">
Svar
</summary>
<p>
<code>['0.0', '4.5', '2.3']</code>
</p>
</details>
<p></p>

### Fråga 3
Vad skrivs ut av följande kod?
```python
lst = [0.0, 4.3, 2.7, 4.5]
print(len(lst))
```

*   `3`
*   `4`
*   `11.5`

<details>
<p></p>

<summary markdown="span">
Svar
</summary>
<p>
<code>4</code>
</p>
</details>
<p></p>

### Fråga 4
Vad skall man anropa för att få ut ett rutnät i en plot?

*  `grid()`
*  `square()`
*  `net()`

<details>
<summary markdown="span">
Svar
</summary>
<p>
<code>grid()</code>
</p>
</details>
<p></p>

### Fråga 5
Vad är formeln för koldioxid?

*  C<sub>2</sub>O<sub>2</sub>
*  C<sub>2</sub>O
*  CO<sub>2</sub>

<details>
<summary markdown="span">
Svar
</summary>
<p>
CO<sub>2</sub>
</p>
</details>
<p></p>

### Fråga 6
Vad brukar man mäta koldioxid i?

*  procent (hundradelar)
*  promille (tusendelar)
*  ppm (parts per million)

<details>
<summary markdown="span">
Svar
</summary>
<p>
ppm
</p>
</details>
<p></p>


### Fråga 7
Var görs mätningarna som ligger till grund för Keelingkurvan?

*  På en ö väster om Australien
*  På vulkanen Mauna Lua, på Hawaii
*  På Antarktis

<details>
<summary markdown="span">
Svar
</summary>
<p>
På vulkanen Mauna Lua, på Hawaii. Mätningarna påbörjades av Charles Keeling.
</p>
</details>
<p></p>
