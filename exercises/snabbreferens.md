# Snabbreferens
Snabbreferens för programmering med miljödata

## 1. Mer om listor och nyckel-värdetabeller, etc.
### 1.1 Några funktioner på listor
```python
lst = [1, 7, 4]
s = sum(lst)  # Ger summan av elementen i listan (12)
n = len(lst)  # Ger antalet element i listan (3)
m = max(lst)  # Ger största elementet i listan (7)
lst.append(7) # Lägg till elementet 7 sist i listan.
              # Nu är lst = [1, 7, 4, 7]
lst.remove(7) # Ta bort första förekomsten av 7
              # Nu är lst = [1, 4, 7]
```

### 1.2 Ranges
* `range(n)` ger en sekvens av heltal som börjar på 0 och slutar på n-1
* `range(m, n)` ger en sekvens som börjar på m och slutar på n-1.
* Vi kan göra om en `range` till en lista med funktionen `list`
```python
lst1 = list(range(5))    # Ger [0, 1, 2, 3, 4]
lst2 = list(range(2, 5)) # Ger [2, 3, 4]
```

### 1.3 Splittra upp sträng till lista
Splittra upp efter whitespace (blanka, tabbar, etc.)
```python
s = "några ord i en sträng"
words = s.split() # Ger listan ["några", "ord", "i", "en", "sträng"]
```

Splittra upp efter rader (newline etc.)
```python
s = "några\nrader\nmed\nnewline\nmellan\nsig"
rows = s.splitlines() # Ger listan ["några", "rader", "med", "newline", "mellan", "sig"]
```

Splittra upp sträng efter specifikt tecken
```python
s = "sträng med tabb-separerade kolumner\t 13\t 14.2"
cols = s.split("\t") # Ger listan ["sträng med tabb-separerade kolumner", " 13", " 14.2"]
```

### 1.4 List slices
`lst[start:stop]` ger en bit av listan, där första elementet är `start` och sista är `stop-1`. Negativa index räknar från slutet (`-1` är sista elementet). Utelämnas `start` motsvarar det `start=0`. Utelämnast `stop` motsvarar det `stop=-1`.
```python
lst = [0, 10, 20, 30, 40, 50, 60, 70]
lst[2:5] # Ger [20, 30, 40]
lst[:5]  # Ger [0, 10, 20, 30, 40]
lst[2:]  # Ger [20, 30, 40, 50, 60, 70]
lst[:]   # Ger en kopia på listan
lst[1:]  # Ger [10, 20, 30, 40, 50, 60, 70]
lst[:-1] # Ger [0, 10, 20, 30, 40, 50, 60]
```

lst[start:stop:steg] ger en bit av listan från `start` till `stop-1`, med steglängd `steg`. Om `steg` utelämnas mostvarar det `steg=1`. Om `steg` är negativ skapas en lista från höger till vänster.

```python
lst = [0, 10, 20, 30, 40, 50, 60, 70]
lst[::2]   # Ger [0, 20, 40, 60]
lst[1::2]  # Ger [10, 30, 50, 70]
lst[::-1]  # Ger [70, 60, 50, 40, 30, 20, 10, 0]
```

### 1.5 Mer om nyckel-värdetabeller

En nyckel-värdetabell är en tabell av nyckel-värdepar (`key:value`). Man kan slå upp värdet för en nyckel. Man kan ta ut alla nycklarna till en lista.
```python
t = {1:3, 5:4, 8:3}
t[5] # Slår upp värdet för nyckel 5 (ger 4)
lst = list(t.keys()) # Tar ut alla nycklarna och gör om till lista
     # Nu är lst=[1, 5, 8]
```

### 1.6 Avrundning
```python
x = 10/3
xr = round(x, 2) # Ger x avrundat till två decimaler
```

## 2. Filer

### 2.1 Läsa från fil
<!--
Exempel läsa från fil. Skapar varaiabeln `data` och lägger allt innehåll från filen i data i form av en sträng. Därefter splittas innehållet upp till en lista.

```python
f = open("file_name.txt") # Öppna filen
data = f.read()  # Lägg hela filinnehållet i en sträng "data"
lines = data.split("\n")  # Omvandla till lista av rader
```            

En annan variant är att loopa över den öppnade filen. Man får en rad per varv:
-->

```python
f = open("file_name.txt") # Öppna filen
lines = []
for line in f:
  lines.append(line)
```            

En annan variant använder en `with`-sats för att öppna filen. Läsning sker inuti `with`-satsen. `with`-satsen gör att filen automatiskt stängs efteråt.

```python
with open("file_name.txt") as f:
  lines = []
  for line in f:
    lines.append(line)                     
```

### 2.2 Skriva till fil
Exempel skriva till fil:

```python
with open("file_name.txt", "w") as f:    # "w" anger write-mode
    f.write("Hej")                       # Skriver "Hej" till filen.
```
Om filen inte finns skapas filen. Om filen redan finns kommer innehållet skrivas över. Om du istället vill lägga till saker på slutet av en existerande fil, kan du använda

```python
with open("file_name.txt", "a") as f:    # "a" anger append-mode
    f.write("Hej")                      # Skiver "Hej" efter det som redan finns.

```
"Append" betyder att man lägger till i slutet.

## 3. Hämta data över internet

Biblioteket `requests` kan användas för att hämta en fil över internet.

Importera requests:

```python
import requests
```
Hämta fil över internet
```python
response = requests.get("https://...")
data = response.text      # Hämta data som en lång sträng
lines = data.splitlines() # Gör om till lista av rader
```

* `get` ger ett svar med info om filen
* Filens innehåll finns i svarets `text` som en lång textsträng.


## 4. NumPy

Importera NumPy:

```python
import numpy as np
```
### 4.1 Skapa numpy arrayer
Skapa en 1-dimensionell array:
```python
a = np.array([1,2,3]) # [1,2,3] kan ersättas med variabelnamn för en lista.
```

Skapa en array fylld med nollor:

```python
zeros = np.zeros(n) # Skapar en array med n st nollor (floats).
```

Skapa en array fylld av ettor:
```python
ones = np.ones(n) # Skapar en array med n st ettor.
```

Skapa en 2-dimensionell array:
```python
a = np.array([[1,2,3],[4,5,6],[7,8,9]]) # skapar en 3x3 matris
```

Skapa en zeros/ones med högre dimension. Obs! De dubbla parenteserna behövs för att det är en tupel `(2,3)` som är argumentet till funktionen `zeros`.
```python
zeros2 = np.zeros((2,3)) # Skapar en matris med 2 rader och 3 kolumner, fylld med nollor.
```

Skapa array med angivet steg mellan element. Börjar på start och lägger till alla element till stop (men inte stop) med skillnaden step:
```python
a = np.arange(start, stop, step)
```

Skapa array med ett visst antal punkter mellan start och stop. Start och stop kommer själva vara med i arrayen.

```python
a = np.linspace(start, stop, antal) #  antal = antal inklusive start och stop
```

### 4.2 Numpy-operationer

Utföra operationer så som +, -, * och / elementvis:

```python
a = np.array([1,2,3])
b = np.array([4,5,6])
c = a+b # == array([5,7,9])
```
Kan även till exempel addera konstant eller ta kvadraten av arrayen elementvis:

```python
a = np.array([1,2,3])
c = a**2 # == array([1,4,9])
```

### 4.3 Numpy-funktioner

Köra sinus-funktionen elementvis på arrayen:

```python
a = np.array([30,60,90])
np.sin(a) # == array([0.5, 0.8660254, 1.0])
```
Finns väldigt många matematiska funktioner som används på liknande sätt, [se här.](https://docs.scipy.org/doc/numpy-1.15.1/reference/routines.math.html)

## 5. Matplotlib.pyplot
Det finns otroligt många funktioner i `matplotlib` och vi kommer inte kunna täcka allt här. För ytterligare information: se dessa [tutorials](https://matplotlib.org/3.1.0/tutorials/index.html).

Importera Matplotlib:

```python
import matplotlib.pyplot as plt
```

### 5.1 Allmänt om figurer
Du kan modifiera din figur på många sätt.
```python
plt.figure(figsize(10, 10)) # Skapar ny figure av storlek 10*10 inches
plt.ylim(0, 10) # Gör så att plotfönstret är mellan 0 och 10 på y-axeln
plt.xlim(0, 10) # Gör motsvarande för x-axeln
plt.xlabel("x-axel (s)")    # Sätter text på x-axeln
plt.ylabel("y-axeln (m)")   # Sätter text på y-axeln
plt.title("Min fina graf")  # Sätter en titel   
plt.grid(True) # Gör så att man får ett rutnär i plotten
plt.show()                  # Visar plotten
plt.savefig("min_graf.png") # Sparar plotten till min_graf.png
plt.close() # Stänger figuren så att en ny figur kan skapas
```

### 5.2 Plotta linjer
Plotta en linje genom punkter vi anger med `x` och `y`:

```python
plt.plot(x, y) # x och y kan vara listor eller np-arrayer av rank 1.
```

Vi kan sätta extra argument i plot-anropet

```python
plt.plot(x, y, marker="o")     # En liten rund markering för varje datapunkt
plt.plot(x, y, color="r")      # Röd linje ("b" för blå)
plt.plot(x, y, linestyle="--") # Streckad linje ("-" för heldragen)
plt.plot(x, y, "or--")         # Kortform för ovanstående
plt.plot(x, y, linewidth=0.5)  # Linjebredd 0.5
plt.plot(x, y, label="min linje") # Sätt etikett
plt.legend()            # Lägg till "legend" med etiketter
```

Plott av två kurvor. Typiska anrop:

```python
plt.plot(x1, y1, "ro-", label="linje 1")
plt.plot(x2, y2, "bo-", label="linje 2")
plt.legend()
```

För mer information om vilka möjligheter som finns för format-argumentet (i stil med `"ro-"`), se https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.plot.html, sektionen *Notes*.

### 5.3 Plotta stapeldiagram
Om man vill plotta ett stapeldiagram i stället för en kurva kan man använda `plt.bar`.

```python
bar = plt.bar(x, heights, width=width, bottom=bottoms, label="mina staplar") # Lägger till ett antal staplar. Informationen sparas i bar
plt.legend() # Lägger till en legend
```

### 5.4 Plotta bilder
Om du har en 2D array du vill plotta kan du använda `plt.imshow()`.

```python
plt.imshow(picture, cmap="PiYG") # Plottar arrayen picture som en bild med colormap "PiYG"
plt.clim(-1.0, 1.0) # Sätter ändpunkterna för colormappen
plt.colorbar(label="min etikett") # Skapar en colorbar med en label
```
