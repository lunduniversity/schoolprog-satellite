# Väderdata från SMHI. Del B.
I detta uppdrag ska vi undersöka temperaturdata från SMHI.

## 1 Filer

Nu när vi kan lite om listor och plottning kan vi snart plotta riktig data från SMHI.

Den här uppgiften är tänkt att köras på följande repl.it-projekt: [https://repl.it/@OscarWiklund96/Vaderdata-A](https://repl.it/@OscarWiklund96/Vaderdata-A). Gå till denna länk så skapas en kopia av projektet för dig. I detta projekt finns filer som uppgiften använder sig av.



Vi behöver först lära oss hur man läser in data från filer.

Filerna vi ska använda finns tillgängliga om du använde länken till repl.it i början av uppgiften. (Ska synas under "Files" på vänster sida i form av `lund_juli_2016.txt`, `lund_juli_2017.txt` och `lund_juli_2018.txt`) Du kan klicka på filerna för att se hur de ser ut. De består en medeltemperatur per rad, totalt 31 rader som motsvarar datumen för månaden juli.

### 1.1 Läs in från fil

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

**Uppdrag 1.1 a**: Skapa en lista med hjälp av `range()` som innehåller värdena 1 till 31.
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

**Uppdrag 1.1 b**: Plotta temperaturerna med tillhörande datum på samma sätt som i tidigare avsnitt.

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

**Uppdrag 1.1 c**: Testa kopiera koden från tidigare uppgifter för att på samma sätt skapa `data2017` och `data2018`.

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

**Uppdrag 1.1 d**: Plotta nu graferna i samma fönster. Du kan använda parametern label för att göra det tydiligare vilken linje som tillhör vilket år. Exempel: `plt.plot(datum,data,label="2016")`.

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

## 2 Quiz

### Fråga 1

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

### Fråga 2
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
