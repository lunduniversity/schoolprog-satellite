# Introduktion till NumPy A
I denna uppgift ska vi titta lite grann på biblioteket NumPy.

NumPy stödjer *array*-er som liknar listor men som är bättre lämpade för numeriska beräkningar. Numeriska beräkningar på arrayer är både smidigare och snabbare än på listor. En array tar dessutom mycket mindre plats i datorns minne än motsvarande lista.

När vi skall hantera stora datamängder, som t.ex. satellitbilder, så behöver vi NumPys arrayer. Listor skulle bli alldeles för långsamt. Många Python-bibliotek använder NumPy, inklusive `matplotlib` som du redan känner till.

Listor är däremot bra när antalet element ändrar sig medan programmet kör. T.ex. om vi läser in data och inte vet hur stor listan kommer att bli. Att lägga till ett element i en lista är en snabb operation. När vi använder arrayer måste vi veta från början hur stor arrayen skall vara.

Denna uppgift är tänkt att köras på [https://replit.com/languages/python3](https://replit.com/languages/python3). Klicka på *create repl* för att skapa ditt egna repl.

## 1. Din första NumPy array
I sin enklaste form är arrayer väldigt lika vanliga listor. För att använda arrayer måste vi importera NumPy-biblioteket:

```python
import numpy as np
```
Vi kan nu skapa en array och printa den genom att skriva:

```python
a = np.array([1,2,3])
print(a)
```
Som du ser så kan vi använda en vanlig lista som argument till `array()`. Det gör att vi enkelt kan omvandla en färdig lista till en array.

**Uppdrag 1 a:** Skapa på liknande sätt en array `x` som innehåller värdena 1, 2, 3, 4, 5. Skriv ut `x` så du ser att den har rätt innehåll.

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>import numpy as np
x = np.array([1,2,3,4,5])
print(x)</code></pre>
</p>
</details>
<p></p>

Observera att en array skrivs ut på liknande sätt som en lista, men utan komma-tecken mellan värdena.

Vi kan indexera arrayer på samma sätt som listor. Till exempel betyder `a[0]` det första elementet i `a`.

**Uppdrag 1 b:** Skriv ut det sista elementet i `x`.

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>print(x[4])</code></pre>
</p>
<p>
Alternativt kan vi skriva
<pre><code>print(x[-1])</code></pre></p>
</details>
<p></p>

## 2. Plotta kurva med NumPy

När vi plottar med MatPlotLib går det lika bra att använda NumPy-arrayer som listor.

**Uppdrag 2:** Skapa en numpy-array `y` som innehåller värdena 1, 4, 9, 16, 25. Plotta en kurva med matplotlib där du använder `x` som x-värden och `y` som y-värden.

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>import matplotlib.pyplot as plt
import numpy as np
plt.ion()
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 9, 16, 25])
plt.plot(x,y)
plt.savefig("test.png")</code></pre></p>
</details>
<p></p>


## 3. Fler-dimensionell array

Du kan nu ta bort eller kommentera bort koden du skrivit hittills, eller starta ett nytt fönster för [https://replit.com/languages/python3](https://replit.com/languages/python3).

En trevlig sak med arrayer är att de kan ha flera *dimensioner*. En 1-dimensionell array motsvarar en lista av värden. En 2-dimensionell array motsvarar ett rutnät av värden, eller en lista av listor. En 3-dimensionell array motsvarar en lista av listor av listor, osv.

En 2-dimensionell array kallas ofta *matris*, och passar bra för att representera en 2D-bild av pixlar.

Vi kan t.ex. skapa en matris `m` genom att skapa en lista av listor, och omvandla till en numpy `array` så här:

```python
m = np.array(
  [[0, 1, 0, 1, 0],
   [1, 0, 1, 0, 1],
   [0, 1, 0, 1, 0],
   [1, 0, 1, 0, 1],
   [0, 1, 0, 1, 0]])
```

**Uppdrag 3 a:** Skapa matrisen `m` ovan, och gör sedan en bildplot av den på följande sätt: (Glöm inte att du behöver importera `numpy` och `matplotlb` som vanligt.)

```python
plt.imshow(m)
plt.savefig("matrix.png")
```

Att observera:
* Varje värde i matrisen motsvarar en färg. Matplotlib hittar själv på färger för de olika värdena.
* `imshow` står för *image show*, alltså "visa bild".
* Plotten har en given storlek, och eftersom matrisen är så liten (bara 5x5 värden) så blir pixlarna motsvarande stora.

**Uppdrag 3 b:** Ändra matrisen `m` så att du byter ut några av ettorna eller nollorna mot andra värden, t.ex. 2 eller 5. Hur blir bilden?


**Uppdrag 3 c:** Ändra matrisen `m` så att du bara använder två färger och försöker få en bild som ser ut ungefär som bokstaven "A" eller någon annan bokstav. Lyckas du?

<details>
<summary markdown="span">
Lösningsförslag
</summary>
<p><pre><code>import matplotlib.pyplot as plt
import numpy as np
plt.ion()
m = np.array(
  [[0, 1, 1, 1, 0],
   [1, 0, 0, 0, 1],
   [1, 1, 1, 1, 1],
   [1, 0, 0, 0, 1],
   [1, 0, 0, 0, 1]])
plt.imshow(m)
plt.savefig("matrix.png")</code></pre></p>
</details>
<p></p>

## 4. Fler sätt att skapa arrayer

Du kan nu rensa bort tidigare kod.

Det finns många sätt att skapa nya arrayer. Om man till exempel vill ha en array med tio nollor kan man skriva:
```python
a = np.zeros(10)
```

På liknande sätt kan man skapa en array med åtta ettor på följande sätt:
```python
a = np.ones(8)
```


**Uppdrag 4:** Skapa en array med 6 nollor och en annan med 6 ettor, och skriv ut dem med `print` för att se hur de ser ut.

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>a = np.zeros(6)
b = np.ones(6)
print(a)
print(b)</code></pre>
</p>
</details>
<p></p>

Observera att elementen blir decimaltal. Det går att skapa heltal i stället genom att ange ett extra argument `dtype=int` till `zeros` eller `ones`.

<!--

Behöver förklara tupler för att kunna visa detta exempel.

Vi kan även skapa arrayer av olika rank. En arrays rank motsvarar hur många dimensioner arrayen utgör. En vanliga lista motsvarar rank 1 medan en tvådimensionell lista, eller rutnät motsvarar rank 2. På samma sätt som en bild kan vara 2D eller 3D kan en array ha olika många dimensioner. Om vi vill skapa vår tidigare array fast nu i rank 2 istället kan vi skriva:

```python
a = np.zeros((10,10))
```
Om du printar denna på samma sätt som tidigare kommer du se att vi nu har fått en array av rank 2. Vi kan även skapa en liknande array med ettor genom att skriva:



```python
a = np.ones((10,5))
```

-->

## 5. Matematiska operationer på arrayer

Du kan nu rensa bort tidigare kod.

Det är enkelt att göra addition och andra matematiska operationer på elementen i en array. Vi ska se på några exempel.

**Uppdrag 5 a:** Om vi har två arrayer, så kan vi addera dem elementvis. Prova följande kod. Vad skrivs ut?

```python
npa = np.array([1, 2, 3])
npb = np.array([4, 5, 6])
print(npa + npb)
```

<details>
<summary markdown="span">
Svar
</summary>
<p>Vi får en array <code>[5 7 9]</code> som resultat. Varje element i resultatet är summan av motsvarande element i de två adderade arrayerna.
</p>
</details>
<p></p>

**Uppdrag 5 b:** Prova andra operationer än `+`. Vilket resultat får du om du gör `*`, `\` eller `-` i stället?

Observera att även här görs operationerna elementvis.

**Uppdrag 5 c:** Man kan också addera en konstant till varje element i en array. Prova följande kod. Vad skrivs ut?

```python
print(npa + 5)
```

<details>
<summary markdown="span">
Svar
</summary>
<p>Vi får en array <code>[6 7 8]</code> som resultat. Varje element i <code>npa</code> har ökats med 5.
</p>
</details>
<p></p>

**Uppdrag 5 d:** Prova att multiplicera `npa`med en konstant i stället. Vilket resultat får du?


**Uppdrag 5 e:** För att kunna addera två arrayer måste de ha samma "form" (lika många dimensioner och samma storlek i varje dimension). Prova följande kod. Vilket fel får du?

```python
npa = np.array([1, 2, 3, 7])
npb = np.array([4, 5, 6])
print(npa + npb)
```

<details>
<summary markdown="span">
Svar
</summary>
<p>Det blir ett <code>ValueError</code>. I felmeddelandet står det att formen ("shape") på de två operanderna inte passar.
</p>
</details>
<p></p>

## 6. Jämförelse mellan listor och arrayer

Du kan nu rensa bort tidigare kod.

Som vi nämnt är listor inte lika smidiga som arrayer för matematiska operationer.

**Uppdrag 6 a:** Vad skulle hänt om du hade försökt addera två listor i stället för två arrayer? Prova följande kod:

```python
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
```

<details>
<summary markdown="span">
Svar
</summary>
<p>Resultatet blir en ny lista med 6 element (a-elementen följt av b-elementen).
</p>
</details>
<p></p>

Observera att addition för listor inte är matematisk addition, utan i stället *konkatenering* ("hopkedjning"). Det samma gäller strängar. T.ex. blir `"abc" + "def"` en ny sträng `"abcdef"`.

Om vi skulle vilja addera elementen i listorna `a` och `b` så skulle vi i stället behöva skriva någon typ av loop, t.ex.:

```python
c = [0, 0, 0]
for i in range(len(a)):
  c[i] = a[i] + b[i]
print(c)
```

**Uppdrag 6 b:** Skapa en lista [1, 3, 5] och en annan lista [10, 11, 12] och addera dem genom att skriva en loop, som i exemplet ovan. Resultatet borde bli en lista [11, 14, 17].


<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>a = [1, 3, 5]
b = [10, 11, 12]
c = [0, 0, 0]
for i in range(len(a)):
  c[i] = a[i] + b[i]
print(c)</code></pre>
</p>
</details>
<p></p>

Vi kan inte multiplicera två listor - då får vi ett fel. Men vi kan faktiskt multiplicera en lista med en konstant! Vad kan det betyda?

**Uppdrag 6 c:** Provkör koden nedan. Vad blir resultatet?

```python
print(a*3)
```

Vi ser att det blir en ny lista som repeteras 3 gånger i följd. `a*3` blir alltså samma sak som `a+a+a`, vilket ju är logiskt!

Men man kan ju undra vilken nytta man kan ha av detta? En sak vi kan göra är att skapa en lista av samma värde på ett enkelt sätt.

**Uppdrag 6 d:** Provkör koden nedan. Vad blir resultatet?

```python
print([1]*10)
```

Vi ser att vi får en lista med 10 ettor. Detta hade vi kunnat utnyttja i uppdrag 6b genom att skriva

```python
c = [0]*3
```
i stället för

```python
c = [0, 0, 0]
```

## 7. Effektivitet hos numpy (extrauppgift)

Vi har nämnt tidigare att numpy arrayer är mycket mer effektiva än listor.

Nedan ser du ett exempelprogram där vi har en funktion `time_for_adding_lists` som tar tiden för att skapa två stora listor och addera dem, och en motsvarande funktion `time_for_adding_arrays` som skapar två arrayer och adderar dem.

```python
import time
import numpy as np

size = 10000

def time_for_adding_lists():
    t = time.time()
    a = range(size)
    b = range(size)
    c = [0]*size
    for i in range(len(a)):
      c = a[i] + b[i]
    return time.time() - t

def time_for_adding_arrays():
    t = time.time()
    a = np.arange(size)
    b = np.arange(size)
    c = a + b
    return time.time() - t

t_lists = time_for_adding_lists()
t_arrays = time_for_adding_arrays()
print("Addition av listor med", size, "element tog",round(t_lists*1000,2), "ms")
print("Addition av arrayer med", size, "element tog", round(t_arrays*1000,2), "ms")
print("Addition av arrayer gick", round(t_lists/t_arrays, 1), "gånger så snabbt")
```

Några saker att observera om koden:
* Tiden mäts genom att läsa av tiden före och efter operationerna, och subtrahera.
* Uttrycket `[0]*size` ger en lista av nollor som är `size` lång.
* Funktionen `range(size)` ger en lista [0, 1, 2, ... size-1]. Funktionen `np.arange(size)` fungerar på motsvarande sätt, men för arrayer.

**Uppdrag 7:** Provkör koden ovan. Hur mycket snabbare är arrayer än listor? Kör gärna några gånger, för resultaten kan variera väldigt mycket. Du bör dock kunna se att arrayer oftast är mycket snabbare än listor.

En anledning till att resultaten varierar mycket är att datorn gör många andra saker samtidigt som den kör ditt program. Din laptop kör t.ex. typiskt mail, webbrowser och kalender samtidigt, och dessutom många program som har med datorns operativ-system att göra. Om du kör på repl.it så kör du egentligen på en server där många olika användare kör sina repl.it-program samtidigt.

<!-- Egentligen är förklaringen mycket mer komplicerad med cache-misses, etc., etc., men det blir för mycket att gå in på här... --->

## 8. Quiz

### Fråga 1

Vilka anledningar kan finnas att använda NumPy arrayer i stället för listor?

* a) De tar mindre plats i datorns minne.
* b) Numeriska beräkningar som addition och multiplikation är både smidigare och snabbare.
* c) Arrayen kan göras större eller mindre genom att lägga till eller ta bort element.

<details>
<summary markdown="span">
Svar
</summary>
<p>a) och b) är korrekta, men c) är fel. Man kan inte ändra storleken på en array. Det kan man däremot med en lista. Man kan t.ex. lägga till ett element i en lista med funktionen <code>append</code>, vilket är en snabb operation. Om man gör <code>append</code> på en array så ändras inte arrayen, utan man får en ny array som är större och där elementen i den gamla har kopierats till den nya. Detta kan ta lång tid om arrayen är stor.
</p>
</details>
<p></p>

### Fråga 2

Vilket av dessa uttryck skapar en NumPy array med elementen 1, 4, 7?

* `np.array([1 4 7])`
* `np.array([1, 4, 7])`
* `np.array(1, 4, 7)`

<details>
<summary markdown="span">
Svar
</summary>
<p><pre><code>np.array([1, 4, 7])</code></pre>
Först skapas listan [1, 4, 7]. Sedan skapas en array från denna lista.
</p>
</details>
<p></p>

### Fråga 3

Vilket anrop plottar en bild?

* `plt.implot(...)`
* `plt.imshow(...)`
* `plt.figplot(...)`

<details>
<summary markdown="span">
Svar
</summary>
<p><pre><code>plt.imshow(...)</code></pre>
</p>
</details>
<p></p>

### Fråga 4

Vad blir resultatet av uttrycket `np.ones(3) + np.ones(3)`?

* En array `[2 2 2]`
* En array `[2. 2. 2.]`
* En array `[1 1 1 1 1 1]`

<details>
<summary markdown="span">
Svar
</summary>
<p>En array <code>[2. 2. 2.]</code>
</p>
</details>
<p></p>

### Fråga 5

Vad blir resultatet av uttrycket `[1]*3 + [1]*3`

* En lista `[2, 2, 2]`
* En lista `[2., 2., 2.]`
* En lista `[1, 1, 1, 1, 1, 1]`

<details>
<summary markdown="span">
Svar
</summary>
<p>En lista <code>[1, 1, 1, 1, 1, 1]</code>
</p>
</details>
<p></p>
