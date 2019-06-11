---
layout: page
title: Väderdata
permalink: /exercises/weatherdata/
toc: true
type: exercise
tags:
 - medel
 - plottning
 - list comprehension
 - input/output
 - inläsning från fil
---

Använd riktig väderdata för att analysera hur temperaturen förändrats i Sverige de senaste 50 åren
==========================================================================================================

I den här uppgiften kommer vi använda python för att analysera data som är jobbig att räkna på för hand. Vi kommer att kolla på hur man kan använda data från filer i sitt program.

För att komma igång behöver du gå till [Repl.it](https://repl.it/@TeodorBucht1729/WeatherData) där vi har förberett datafiler och några förskrivna funktioner. Om du inte vill använda Repl.it kan du ladda ner filerna från [GitHub](https://github.com/lunduniversity/schoolprog-satellite/tree/master/exercises/weatherdata) istället.

Vi börjar med att kolla på ett mindre exempel för att se hur inläsning från fil fungerar.

## 1. Inläsning från fil

Tidigare har vi testat att mata in data till programmet genom consolen. När man vill skicka in mycket information till ett program kan det vara lättare att låta programmet läsa från en fil.
Vi har förberett en fil med medeltemperaturer i Lund från april 2017. Testa att läsa in filen genom att skriva:

```python
with open("april_2017.txt", "r") as f:
  data = f.read()
print(data)  
```
**Uppdrag:** Vad hände? Förstår du vad programmet gör?

Programmet läste först in all information från filen för att sedan skriva ut det igen i console-vyn. Man kan säga att vi öppnar vår fil `april_2017.txt` och kallar filen `f`. Vi öppnar den i <i>read</i>-läge, där av `"r"` i koden. Därefter läser vi från filen med metoden `read()` och sparar detta i vår variabel `data`.

Kan vi kombinera inläsning från fil med plottning av grafer med hjälp av `matplotlib`? Vi kan inte plotta direkt eftersom formatet på vår data inte matchar det `plt.plot()` vill ha, en lista av tal. Vi måste därför utföra lite typomvandling på vår data först. Funktionen `read()` som vi använder för att läsa in datan från filen sparar allt innehåll som en enda lång sträng. Vi kan dela upp en sträng till flera genom att anropa ```split()```. Vi kan till exempel välja ett dela upp vår sträng vid varje radbrytning med ```data.split("\n")```. Vår data kommer då vara lagrad som en lista av mindre strängar istället.


**Uppdrag:** Testa nu skriva stycket nedan. Vad blir typen? Varför?

```python
data = data.split("\n")
```


<details>
<summary markdown="span">
Svar
</summary>
<p>Typen blir en <code>'list'</code> som innehåller strängar.</p>
</details>

För att vårt program ska kunna plotta värdena behöver vi göra om våra strängar till tal, eller mer specifikt flyttal (decimaltal). Detta kan vi göra genom att använda listcomprehension som vi tidigare kollat på. Stycket nedan gör om alla strängar till floats
```python
data = [float(x) for x in data]
```

**Uppdrag:** Vad blir typen av data nu? Varför? Vad är skillnaden jämfört med innan? Testa skriva ut data både innan och efter omvandlingen till floats.

<details>
<summary markdown="span">
Svar
</summary>

<p>Typen blir fortfarande <code>'list'</code> men innehåller nu floats istället. Om vi printar ut listorna kan vi se en liten skillnad eftersom strängar representeras med apostrofer före och efter.</p>
</details>



**Uppdrag:** Vår data är nu redo att plottas! Vad visar diagrammet?


<details>
<summary markdown="span">
Har du glömt hur man plottar med <code>matplotlib</code>?
</summary>
<p>
<pre><code>plt.plot(data)
plt.savefig(data.png)</code>
</pre>
</p>
</details>


## 2. Inläsning av mer data
Nu har vi testat hur man kan läsa in en fil själv från grunden. Det kanske verkade krångligt och det skulle inte varit så jobbigt att manuellt skriva in 30 värden. Men när mängden data växer är det en klar fördel att använda inläsning av filer.

Innan kollade vi på medeltemperaturen från varje dag under en månad i Lund, men nu ska vi istället studera medeltemperaturen från varje dag från 1961 till och med 2017. Här blir det ganska jobbigt att läsa in datan själv jämfört med förut, så det har vi hjälpt till med här.

I filen ```api.py``` finns det några funktioner som är användbara för att lösa den här uppgiften. För att kunna använda funktionerna från denna fil kan man importera dessa genom att skriva ```import api```.

Det finns en funktion i `api` som heter ```get_station_data```, denna funktion öppnar och läser en komprimerad fil med väderdata. ```get_station_data``` läser in data från flera olika stationer, så för att organisera detta används en ```dict``` som är kort för dictionary. En ```dict``` funkar likt en lista, men istället för index använder man nycklar för att komma åt elementen. I vårt fall används väderstationsnamn som nycklar.

För att skriva ut vilka väderstationer som finns kan ni skriva följande:

```python
import api
data = api.get_station_data()
print(list(data.keys()))
```
Programmet skriver ut olika städer.

**Uppdrag:** Varför skrivs dessa städer ut? Vad gör ```list(data.keys())```?


<details>
<summary markdown="span">
Svar
</summary>
<p>Dessa är städerna där temperaturen är mätt. <code>list(data.keys())</code> returnerar en lista med alla nycklar som används. </p>
</details>

För att undersöka hur datan ser ut kan det vara bra att printa ut en del av den. Kör följande kod:
```python
lund = data["Lund"]
print(lund[:10])
```
Då hamnar Lunds data i listan `lund` och de `10` första datapunkterna skrivs ut för Lund. Här används något som kallas <i>list slicing</i>. Skriver man `lund[:10]` betyder det att man tar med allt till och med det tionde elementet. Skulle man däremot skrivit `lund[10:]` tar man det elfte elementet och alla som kommer efteråt. För mer information om <i>list slicing</i> kan man läsa en tutorial [här](https://www.programiz.com/python-programming/methods/built-in/slice).

**Uppdrag:** Vad betyder betyder datan som skrivs ut?

<details>
<summary markdown="span">
Svar
</summary>
<p>De tre första talen i varje element anger datumet på formatet <code>yyyy, mm, dd</code>. Det sista talet är medeltemperaturen för den dagen. </p>
</details>

Nu ska vi äntligen börja plotta datan vi har läst in. För detta behöver vi en lista som innehåller alla temperaturer från listan `lund`.

**Uppdrag:** Skapa en lista `temps` som innehåller alla temperaturer från `lund`.

<details>
<summary markdown="span">
Tips
</summary>
<p>Loopa igenom <code>lund</code> med en <code>for</code>-loop. Till exempel ger <code>lund[0][3]</code> medeltemperaturen den första januari 1961.</p>
</details>

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>temps = []
for day in lund:
  temps.append(day[3])</code>
</pre>
</p>
</details>

Nu vill vi dock visualisera datan vi har i `temps`. Istället för att använda `matplotlib` direkt kan du använda funktionen `plot` som finns i `api`. Kör följande kod och se vad som händer:

```python
api.plot(y=temps)
```

**Uppdrag:** Vad betyder plotten? Var betyder värdena på x-axeln respektive y-axeln?

<details>
<summary markdown="span">
Svar
</summary>
<p>Plottat är medeltemperaturen för varje dag från 1961 till 2017. Temperaturerna finns på y-axeln och på x-axeln finns indexet för temperaturen i listan.</p>
</details>

*Kommentar:* Du kanske har märkt att det i koden ovan används `api.plot(y=temps)` och inte bara `api.plot(temps)`. Detta är för att `plot` är en funktion som har <i>valbara parametrar</i>, detta betyder att funktionen inte behöver alla parametrar som kan matas in och om inget värde anges finns det ett standardvärde som den parametern får. `plot` har totalt tre parametrar, `x`, `y` och `fname`. `x` är en lista med mätpunkternas x-värden, `y` är en lista med mätpunkternas y-värden och `fname` är en sträng där man kan välja vilket namn figuren ska sparas som. Till exempel kan man skriva `api.plot(x=times, y=temps, fname="weather.png")` för att plotta temperaturer i `temps` som är uppmätte vid tiderna i `times` och sedan spara grafen som `weather.png`.




Om vi istället vill ha årtal med x-axeln behöver vi även en lista som innehåller motsvarande datum för temperaturerna, representerat i år. Till exempel vill vi att första juli 2000 ska representeras som ungefär 2000,5.

**Uppdrag:** Skapa en lista `times` som innehåller alla datum, representerat i år, för de uppmätta temperaturerna i Lund. Om du vill kan du anta att varje månad har 30 dagar för att göra koden lite lättare att skriva.

<details>
<summary markdown="span">
Tips
</summary>
<p>
Vi måste omvandla våra månader och dagar till år. Om vi omvandlar månader till dagar kan vi dela antalet dagar på 365 för att få ett decimaltal som representerar en del av ett år.  
</p>
</details>


<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>times = []
for datum in lund:
    (y, m, d, t) = datum
    times.append(y+((m-1)*30+d)/365)</code>
</pre>
</p>
</details>

*Kommentar:* Om du tänker efter ser du att uträkningen i lösningen ovan inte blir helt exakt. Till exempel blir sista decemeber dag 361. Kan vi göra detta mer exakt? Bör vi ta hänsyn till skottår? Kommer vi se någon skillnad på grafen?

**Uppdrag:** Testa nu att plotta grafen igen men denna gång använder vi vår nya lista `times` för att representera x-axeln. Vad blev skillnaden?

<details>
<summary markdown="span">
Lösning
</summary>
<p>
<code>api.plot(x=times, y=temps)</code>
</p>
</details>

<details>
<summary markdown="span">
Svar
</summary>
<p>
Vår graf har nu fått år från 1960 till 2020 på x-axeln.
</p>
</details>



## 3. Temperaturförändring under ett år

I våra tidigare grafer har vi sett hur temperaturer skiljer sig från dag till dag. I dessa grafer kan det dock vara svårt att se hur temperaturen skiljer sig under bara ett år eftersom ett år representeras av en väldigt liten del av x-axeln. För att kunna besvara frågor som: "Vilka månader var varmast?" och "Vilka var kallast?" Vi vill nu försöka plotta ut medeltemperaturer för endast ett år istället. För att kunna göra detta måste vi på något sätt filtrera vår data så vi endast har data från ett specifikt år.

**Uppdrag:** Skriv en funktion `data_by_year(year, city_data)` som plockar ut alla temperaturer för ett specifikt år och stad. Parametern `year` är ett heltal som representerar ett år och `city_data` är vår data för en specifik stad, till exempel kan vi mata in listan `lund`.

<details>
<summary markdown="span">
Tips
</summary>
<p>
Vi kan till exempel använda en <code>if</code>-sats inuti en <code>for</code>-loop för att sålla ut all data som inte har med det specifika året att göra.
</p>
</details>

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>def data_by_year(year, city_data):
    result = []
    for datum in city_data:
        if datum[0] == year:
            result.append(datum[3])
    return result</code>
</pre>
</p>
</details>

Vi kan nu använda vår funktion för att skapa en graf som visar temperaturen från varje dag under ett år.

**Uppdrag:** Använd din funktion och plotta temperaturen under 2016 i Lund.

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>lund2016 = data_by_year(2016, lund)
api.plot(y=lund2016)</code>
</pre>
</p>
</details>

## 4. Medeltemperaturen för varje år
Efter att ha sett plotten från varje år kan man fråga sig om vi kan se någon trend. Blir det varmare, kallare eller håller det sig ungefär konstant? Eftersom vi plottar medeltemperaturen från varje dag kan det vara ganska svårt att se någon trend eftersom grafen hoppar mycket upp och ner. För att lösa detta kan man plotta medeltemperaturen från varje år istället. För att göra detta behöver vi kunna räkna ut medeltemperaturen för ett år.

**Uppdrag:** Skriv en funktion `avg(data)` som tar en lista `data` med flyttal som returnerar medelvärdet av talen i `data`.

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>def avg(data):
    summa = 0
    for tal in data:
        summa += tal
    medel = summa / len(data)
    return medel</code>
</pre>
</p>
</details>

Nu behöver vi få ut datan från varje år och mata in den i `avg()`. Till detta ska vi ta hjälp av funktionen `data_by_year()` du precis skrivit.

**Uppdrag:** Skapa en lista `avg_temps` som innehåller medeltemperaturen från varje år. Skapa också en lista `years` som innehåller åren för de olika medeltemperaturerna.

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>years = []
avg_temps = []
for year in range(1961, 2018):
    years.append(year)
    avg_temps.append(avg(data_by_year(1961, lund)))</code>
</pre>
</p>
</details>

Nu vill vi givetvis se resultatet och vill därför plotta medeltemperaturerna.

**Uppdrag:** Plotta medeltemperaturerna varje år. Kan du se några trender?

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>api.plot(x=years, y=avg_temps)</code>
</pre>
</p>
</details>

## 5. Medeltemperaturen för hela Sverige
Vill vi se tydligare trender vill vi kolla på så mycket data som möjligt. Totalt har vi ungefär 500 000 datapunkter men vi har bara utnyttjat ungefär 20 000 eftersom vi bara kollar på Lund. För att utnyttja all data ska vi skriva hjälpfunktioner.

*Kommentar:* En hjälpfunktion är en funktion som egentligen inte hade behövt vara en funktion för sig själv, men som gör koden betydligt smidigare och mer lättförståelig. Generellt sett vill man dela upp en stor uppgift i mindre deluppgifter, där deluppgifterna kan lösas med hjälpfunktioner. I föregående uppgift finns ett bra exempel på en hjälpfunktion, nämligen `avg(data)`. För att beräkna medeltemperaturen för varje år behöver vi kunna beräkna medeltemperaturen för ett år i taget, och denna deluppgiften löser `avg(data)`.

**Uppdrag:** Skriv en funktion `mean_by_year(city, year)` som tar in en sträng `city` som namnet på staden samt heltalet `year` som är vilket år vi vill beräkna medelvärdet för. Returnera medeltemperaturen från det året i den staden.

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>def mean_by_year(city, year):
    city_data = data[city]
    year_temps = data_by_year(year, city_data)
    return avg(year_temps)</code>
</pre>
</p>
</details>

Nu när vi kan få fram medelvärdet från varje stad vill vi ta medelvärdet av alla dessa olika värden.

**Uppdrag:** Skapa en lista `total_mean` och en lista `years` på liknande sätt som vi gjorde med Lund. `total_mean` ska innehålla medelvärdet från varje stad av värdena vi får från `mean_by_year` och `years` ska innehålla varje år för medeltemperaturerna. Slutligen ska du plotta värdena. Ser du fortfarande en trend? Är den tydligare eller otydligare? Varför?

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>total_mean = []
years = []
for year in range(1961, 2018):
    cities = list(data.get_keys())
    city_means = []
    for city in cities:
        city_means.append(mean_by_year(city, year))
    total_mean.append(avg(city_means))
    years.append(year)
api.plot(x=years, y=total_mean)</code>
</pre>
</p>
</details>


## 6. Frivilligt: Refaktorisering med hjälp av nya funktioner

Många av upppdragen som vi här löst med `for`-loopar går även att lösa med funktionen `filter()`. Tillexempel kan man skriva `list(filter(lambda x: x[0] == 2016, lund))` för att plocka ut all data där året motsvarar 2016 för `lund`. `filter()` tar emot en funktion och en lista. Den kör funktionen på varje element i listan och om resultatet är `True` så behåller filter värdet, annars slängs det.`filter()` returnerar dock inte en lista direkt, så vi använder `list()` för att få det som en lista igen.

Det finns även en funktion `map()` som kan vara användbar för vissa av de tidigare uppdragen. `map()` tar emot en funktion och en lista för att sedan köra funktionen på varje element i listan. `map()`, likt `filter()`, returnerar inte en lista direkt så du behöver använda `list(map())` för att lägga tillbaka ditt resultat i en lista.

**Uppdrag:** Försök lösa något av de tidigare uppdragen med `filter()` eller `map()` istället!

<details>
<summary markdown="span">
Tips för <code>map()</code>
</summary>
<p>Du kan till exempel använda <code>map()</code> för att ta fram listan <code>temps</code>.
</p>
</details>

<details>
<summary markdown="span">
Tips för <code>filter()</code>
</summary>
<p> Funktionen <code>data_by_year()</code> kan skrivas med <code>filter()</code>, kan du komma på hur?
</p>
</details>

<details>
<summary markdown="span">
Exempellösning för <code>map()</code>
</summary>
<p><code>temps = list(map(lambda x: x[3], lund))</code>
</p>
</details>

<details>
<summary markdown="span">
Exempellösning för <code>filter()</code>
</summary>
<p><pre>def data_by_year(year, city_data):
    return list(filter(lambda x: x[0] == year, city_data))</pre>
</p>
</details>    

# Fortsättningsuppgifter
- Utforska mer med hjälp av datan. Hur ser det ut om du till exempel tar medelvärdet över var femte år istället för varje år?
- Vilken dag har varit kallast respektive varmast?
- Vilka år har det (troligtvis) varit snö på julafton? Hur avgör du detta?
