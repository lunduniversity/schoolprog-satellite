# Keelingkurvan A

I denna uppgift ska vi börja utforska Keelingkurvan som beskriver koldioxidhalten i atmosfären. Mätningarna påbörjades av forskaren Charles Keeling och har utförts sedan 1958 på vulkanen Mauna Loa på Hawaii. Observationerna på Mauna Loa var de första att tyda på att koldioxidhalten ökar i vår atmosfär.

I uppgiften kommer vi att lära oss följande om Python-programmering:

* göra om strängar till listor med `split`
* läsa in datafiler
* mer om plottning

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

Ser du förresten att det interpolerade värdet *inte* ligger precis mitt emellan värdena före och efter? Ett smartare sätt har använts för att räkna ut värdet, där man har tagit hänsyn till många värden runt det saknade värdet.

När vi programmerar kommer vi att använda de interpolerade koldioxidvärdena.

### 1.6 Kolumn 6 och 7

Kolumn 6 visar ett trendvärde som vi skall titta på i en senare uppgift. Kolumn 7 visar hur många dagar koldioxidhalten mättes under en månad (-1 betyder att uppgiften saknas).

## 2. Programmera med textsträngar

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

Några saker att notera:

* Strängar i Python kan skrivas antingen med dubbelfnuttar eller enkelfnuttar. Så `"hej"` och `'hej'` betyder samma sak.
* Strängen splittades upp efter blanktecken, och blanktecknen kom inte med i den resulterande listan.

### 2.2 Dela upp med annan separator

Hittills har vi delat upp strängar efter blanktecken. Men om vi anger ett argument till `split` kan vi separera (dela upp) strängen på andra sätt.

**Uppdrag:** Provkör följande kod. Hur delas strängen upp nu? Prova att ändra separatorn `"j"` till en annan sträng och kör programmet igen.

```python
str = "Hej svejs i lingonskogen!"
lst = str.split("j")
print(lst)
```

(Det kanske inte är så användbart att separera just på `"j"` i detta fall. Vi gör det bara för att se hur `split` fungerar.)

<details>
<summary markdown="span">
Svar
</summary>
<p>
Nu delas strängen upp till en lista med följande element: "He", " sve", "s i lingonskogen!".
</p>
</details>

Några saker att notera:

* Separatorn kommer inte själv med i listan.
* Separatorn kan bestå av flera tecken. Prova t.ex. med separatorn `"ej"`.
* Separatorn måste ha minst ett tecken. Prova gärna med en tom sträng, alltså `""`, så ser du att det blir det exekveringsfel.
* Om man anropar `split` *utan* separator-argument, alltså med `split()`, så är det samma sak som att anropa med en blank som separator, alltså `split(" ")`. Vi säger att *default*-separatorn är ett blanktecken.

### 2.3 Dela upp efter rader

En textfil består av flera rader text. Men vad är en "rad" egentligen? I filen skiljs rader åt med ett särskilt tecken *newline* som skrivs som `"\n"`. Vi kan skapa en sträng med flera rader genom att använda `"\n"`.

**Uppdrag:** Provkör följande kod. Vad skrivs ut?

```python
str = "Hej svejs!\nHur är läget?\nSjälv mår jag fint!"
print(str)
```
<details>
<summary markdown="span">
Svar
</summary>
<p>
Det skrivs ut tre rader. Varje "\n" ger en ny rad i utskriften.
</p>
</details>

**Uppdrag:** Dela upp strängen i en delsträng per rad genom att använda `split` med separatorn `"\n"`. Du kan fylla i nedanstående skelett för att lösa problemet:

```python
str = "Hej svejs!\nHur är läget?\nSjälv mår jag fint!"
lines = #FYLL I DIN KOD HÄR
print(lines)
```

Om du gjort rätt så skrivs följande ut:

```python
['Hej svejs!', 'Hur är läget?', 'Själv mår jag fint!']
```

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>lines = str.split("\n")
</code></pre>
</p>
</details>

### 2.4 Dela upp en sträng med tal

Nu vet vi det mesta vi behöver för att kunna läsa in en datafil och splitta upp resultatet till listor.

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
Resultatet blir en lista med elementen "1.2", "17.56", "0.33".
</p>
</details>

Vi kan notera att elementen är *strängar*, alltså sekvenser av tecken. För att vi skall kunna använda dem som decimaltal behöver de först omvandlas till decimaltal.

### 2.5 Omvandla en sträng till decimaltal med `float`

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

Saker att notera:

* För att `float` ska fungera krävs det att strängen verkligen motsvarar ett decimaltal. Om du anropar `float` med t.ex. `"hej"` som argument så blir det exekveringsfel. Prova gärna.

## 3. Läsa in datafilen

Nu kan vi äntligen läsa in datafilen. Vårt mål är att representera datan som två listor: en lista `years` som innehåller åren på decimalform (värdena i kolumn 3), och en lista `co2` som innehåller de interpolerade koldioxidvärdena (kolumn 5).

Vi skall göra detta i några steg.

Koden vi skrivit hittills har vi bara haft för att experimentera. Du kan ta bort den, eller kommentera bort den genom att skriva en "brädgård", `#`, först på varje kodrad.

### 3.1 Läs in hela filen i en sträng

Det finns flera olika sätt att läsa in en fil. I denna uppgift ska vi läsa in hela filen i en enda jättelång sträng, och sedan splitta upp den så vi får en lista av textrader.

**Uppdrag:** Skriv in och kör följande kod.

```python
f = open("data.txt")      # Öppna filen
data = f.read()           # Läs in hela innehållet
rows = data.split("\n")   # Dela upp i rader
```

För att veta att något faktiskt hände när vi körde koden ovan kan vi ta reda på hur många tecken som finns i datan och hur många rader det blev:

```python
print(len(data))
print(len(rows))
```

Vad fick du för resultat?

<details>
<summary markdown="span">
Svar
</summary>
<p>
Filen har 47039 tecken fördelade på 735 rader.
</p>
</details>

Saker att notera om filer:

* Funktionen `open` returnerar ett "filobjekt" som vi sparar i variabeln `f`. Argumentet `"data.txt"` är namnet på vilken fil vi vill öppna.
* Man kan göra `read` på ett filobjekt, och då får man hela innehållet i filen som en enda lång textsträng.

### 3.2 Skapa `years` och `co2`

Nu vill vi skapa en lista `years` och en lista `co2` som vi kan använda för att plotta en kurva över koldioxidhalterna.

Problemet är dock att vi fått in innehållet som rader, men det är kolumnerna vi vill åt.

Vi löser problemet med en `for`-loop som går igenom alla raderna. Inuti `for`loopen splittar vi upp raden efter blanktecken. Sedan plockar vi ut det 3:e och 5:e värdet, omvandlar dem till `floats`, och lägger till dem till `years` och `co2`.

**Uppdrag:** Lägg till koden nedan i ditt program för att skapa `years` och `co2`:

```python
years = [] # Skapa tom lista för years
co2 = []   # Skapa tom lista för co2
for row in rows:  # Gå igenom alla rader
  splitted = row.split()          # Splitta upp raden
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

Saker att notera:
* För att kunna lägga till element skapade vi först två tomma listor, innan for-loopen.
* Vi la till element till en lista med funktionen `append` ("append" betyder "lägg till sist").

## 4. Plotta

### 4.1 Plotta Keelingkurvan

Nu kan vi plotta Keelingkurvan! Vi vill ha `years` på x-axeln och `co2` på y-axeln.

**Uppdrag:** Lägg till följande kod för att plotta kurvan:

```python
import matplotlib.pyplot as plt
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

### Fråga 2
Vad skrivs ut av följande kod?
```python
str = "0.0 4.5 2.3"
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
<summary markdown="span">
Svar
</summary>
<p>
<code>4</code>
</p>
</details>

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

### Fråga 6
Vad mäts koldioxid i?

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
