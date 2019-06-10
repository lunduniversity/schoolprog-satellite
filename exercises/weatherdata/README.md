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

I den här uppgiften kommer vi använda python för att analysera data som är jobbig att räkna på för hand. Vi kommer att kolla på hur man kan använda data från filer i sitt program. Vi har förberett en fil med medeltemperaturer i Lund från april 2017. Testa läs in denna filen genom att skriva

```python
with open("apirl_2017.txt", "r") as f:
  data = f.read()

print(data)  
```
**Uppdrag:** Vad hände? Förstår du vad programmet gör? Försök ändra texten som skrivs ut. Var ska du ändra?

Programmet läste först in all information från filen för att sedan skriva ut det igen i console-vyn.

Kan vi kombinera inläsning från fil med plottning av grafer?

**Uppdrag:** Testa plotta en graf med värdena från filen. Vår data är sparad som en enda lång sträng. Använd ```split("\n")``` på något sätt för att dela upp datan. Glöm ej att importera matplotlib genom att skriva ```import matplotlib.pyplot as plt```


<details>
<summary markdown="span">
Svar
</summary>
<p><code>f(x) = 2*x</code>
</p>
</details>

<details>
<summary markdown="span">
Tips 1:
</summary>
<p>
Vi kan t.ex. använda ```data = data.split("\n")``` för att dela upp datan.
</p>
</details>

<details>
<summary markdown="span">
Minns du hur man plottar en graf?
</summary>
<p><code>plt.plot(data)<code/></p>
</details>

Vi börjar med att kolla på ett mindre exempel för att se hur inläsning från fil fungerar.

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

Om ni lägger till följnade
```python
lund = data['Lund']
print(lund[:10])
```
Hamnar Lunds data i variabeln `lund` och ni printar de `10` första datapunkterna för Lund.

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
