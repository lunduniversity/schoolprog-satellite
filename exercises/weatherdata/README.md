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

Använd riktig väderdata för att analysera hur temperaturen förändrats i Sverige de senaste 50 åren.
==========================================================================================================

I den här uppgiften kommer vi använda python för att analysera data som är jobbig att räkna på för hand. Vi kommer att kolla på hur man kan använda data från filer i sitt program.

Vi börjar med att kolla på ett mindre exempel för att se hur inläsning från fil fungerar.

## 1. Inläsning från fil

Tidigare har vi testat på att mata in data till programmet genom consolen. När man vill skicka in mycket information till ett program kan det vara lättare att låta programmet läsa från en fil.
Vi har förberett en fil med medeltemperaturer i Lund från april 2017. Testa att läsa in filen genom att skriva

```python
with open("apirl_2017.txt", "r") as f:
  data = f.read()

print(data)  
```
**Uppdrag:** Vad hände? Förstår du vad programmet gör?

Programmet läste först in all information från filen för att sedan skriva ut det igen i console-vyn.

Kan vi kombinera inläsning från fil med plottning av grafer? Vi kan inte plotta direkt eftersin formatet på vår data in matchar det plot funktionen vill ha. Vi måste därför utföra lite typomvandling på vår data först. Vår data blir sparad som en enda lång sträng när vi läser in den. Vi kan dela upp en sträng till flera genom att anropa ```split()```. Vi kan t.ex. välja ett dela upp vår sträng vid varje radbrytning med ```data.split("\n")```. Vår data kommer då vara lagrad som en lista av mindre strängar istället.

**Uppdrag:** Vad har vår data för typ? Varför? (Om du behöver hjälp kan du använda ```print(type(data))```).

<details>
<summary markdown="span">
Svar
</summary>
<p>```'str'```</p>
</details>

**Uppdrag:** Testa nu skriva stycket nedan. Vad blir typen nu? Varför?

```python
data = data.split("\n")
```


<details>
<summary markdown="span">
Svar
</summary>
<p>Typen blir ```'list'``` men innehåller strängar.</p>
</details>

För att vårt program ska kunna plotta värdena behöver vi göra om vår text till tal, eller mer specifikt floats (decimaltal). Detta kan vi göra genom att använda listcomprehension som vi tidigare kollat på. Stycket nedan gör om alla strängar till floats
```python
data = [float(x) for x in data2]
```

**Uppdrag:** Vad blir typen av data nu? Varför? Vad är skillnaden från innan? Testa skriva ut data både innan och efter omvandlingen till floats.

<details>
<summary markdown="span">
Svar
</summary>

<p>Typen blir fortfarande ```'list'``` men innehåller nu floats istället. Om vi printar ut listerna kan vi se en liten skillnad då strängar representeras med apostrofer före och efter.</p>
</details>



**Uppdrag:** Vår data är nu redo att plottas! Vad visar diagrammet?


<details>
<summary markdown="span">
Har du glömt hur man plottar en graf?
</summary>
<p>
<pre><code>
plt.plot(data)
plt.savefig(data.png)</code>
</pre>
</p>
</details>


## 2. Inläsning av mer data
Nu har vi testat hur man kan läsa in en fil själv från grunden. Det kanske verkade krånligt och det skulle inte varit så jobbigt att manuellt skriva in 30 värden. Men när mängden data växer är det en klar fördel att använda inläsning av filer.

Innan kollade vi på medeltemperaturen från varje dag under en månad i Lund, men nu ska vi istället studera medeltemperaturen från varje dag under 56 år. Här blir det ganska jobbigt att läsa in datan själv jämfört med föut, så det har vi hjälpt till med här.

I filen ```api.py``` finns det några funktioner som är användbara för att lösa den här uppgiften. För att kunna använda funktionerna från denna fil kan man importera dessa genom att skriva ```import api```.

Det finns en funktion som heter ```get_station_data```, denna funktion öppnar och läser en komprimerad fil med väderdata. ```get_station_data``` läser in data från flera olika stationer, så för att organisera detta används en ```dict``` som är kort för dictionary. En ```dict``` funkar likt en lista, men istället för index använder man nycklar för att komma åt elementen. I vårt fall används väderstationsnamn som nycklar.

För att skriva ut vilka väderstationer som finns kan ni skriva följande:

```python
import api
data = api.get_station_data()
print(data.keys())
```
Programmet skriver ut olika städer.

**Uppdrag:** Varför skrivs dessa städer ut? Vad gör ```data.keys()```?


<details>
<summary markdown="span">
Svar
</summary>
<p>Dessa är städerna där temperaturen är mätt. ```data.keys()``` returnerar en lista med alla nycklar som används. </p>
</details>

För att undersöka hur datan ser ut kan det vara bra att printa ut en del av den. Om man kör följande kod:
```python
lund = data['Lund']
print(lund[:10])
```
Hamnar Lunds data i listan `lund` och de `10` första datapunkterna printas för Lund. Här används något som kallas <i>list slicing</i>. Skriver man `lund[:10]` betyder det att man tar med allt till och med det tionde elementet. Skulle man däremot skrivit `lund[10:]` tar man det elfte elementet och alla som kommer efteråt. För mer information om <i>list slicing</i> kan man läsa en tutorial [här](https://www.programiz.com/python-programming/methods/built-in/slice).

**Uppdrag:** Vad betyder betyder datan som skrivs ut?

<details>
<summary markdown="span">
Svar
</summary>
<p>De tre första talen i varje element anger datumet på formatet `yyyy mm dd`. Det sista talet är medeltemperaturen för den dagen. </p>
</details>

Nu ska vi äntligen börja plotta datan vi har läst in. För detta behöver vi en lista som innehåller alla temperaturer från listan `lund`.

**Uppdrag:** Skapa en lista `temps` som innehåller alla temperaturer från `lund`.

<details>
<summary markdown="span">
Tips
</summary>
<p>Loopa igenom `lund` med en `for`-loop. `lund[0][3]` ger medeltemperaturen den första januari 1961.</p>
</details>

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>temps = []
for day in lund:
  temps.append(day[3])
</code>
</pre>
</p>
</details>

# Uppgifter
- Skapa två listor `time` och `temp` som innehåller tiden repsektive temperatur för varje datapunkt.
- Plotta temperaturerna genom `api.plot(y=temp)`. Vill ni själva välja filnamnet kan detta göras genom `api.plot(temp, fname='myplot.png')`.
- Filtrera ut alla temperaturer uppmätta under 2016 och plotta dessa, för att se hur temperaturen varierar under ett år.
- Skapa en funktion `avg(temp)` som beräknar medelvärdet av en lista med temperaturer.
- Använd funktionen `avg` för att beräkna medeltemperaturen i lund för varje år och platta alla dessa.
- Använd funktionen `avg` för att beräkna medeltemperaturen i varje stad som finns i datasetet för varje år. Beräkna sedan medelvärdet av dessa medelvärden och plotta det gemensamma medelvärdet för varje år.



# Fortsättningsuppgifter
- Instructions for calculating yearly average (standard deviation) for a station.
- Download more data from SMHI by exploring their API
- Download more data from other sources?
