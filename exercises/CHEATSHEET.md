Cheatsheet
===

## Filer

### Läsa från fil
Exempel läsa från fil. Skapar varaiabeln data och lägger allt innehåll från filen i data i form av en sträng:

```python
with open("file_name.txt", "r") as f:    # "r" anger read-mode
    data = f.read()                      
```

Eller

```python
f = open("file_name.txt", "r")
...
...
data = f.read()                
```
### Skriva till fil
Exempel skriva till fil:

```python
with open("file_name.txt", "w") as f:    # "w" anger write-mode
    f.write("Hej")                       # Skriver "Hej" till filen.
```
Om filen inte finns skapas filen. Om filen redan finns kommer innehållet skrivas över. Om du istället vill appenda till en fil kan du använda

```python
with open("file_name.txt", "a") as f:    # "a" anger append-mode
    f.write("Hej")                      # Skiver "Hej" efter det som redan finns.

```
## NumPy

Importera NumPy:

```python
import numpy as np
```
### Skapa arrayer
Skapa en array av rank 1:
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

Skapa en array av rank 2:
```python
a = np.array([[1,2],[3,4]]) # skapar en 2x2 matris
```

Skapa en zeros/ones med högre rank:
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

### Operationer

Utföra operationer så som +, -, * och / elementvis:

```python
a = np.array([1,2,3])
b = np.array([4,5,6])
c = a+b # == array([5,7,9])
```
Kan även till exempel plusa med konstant eller ta kvadraten av arrayen elementvis:

```python
a = np.array([1,2,3])
c = a**2 # == array([1,4,9])
```

### Funktioner

Köra sinus funktionen elementvis på arrayen:

```python
a = np.array([30,60,90])
np.sin(a) # == array([0.5, 0.8660254, 1.0])
```
Finns väldigt många matematiska funktioner som används på liknande sätt, [se här.](https://docs.scipy.org/doc/numpy-1.15.1/reference/routines.math.html)

## Matplotlib.pyplot
Det finns otroligt många funktioner i `matplotlib` och vi kommer inte kunna täcka allt här. För ytterligare information: se dessa [tutorials](https://matplotlib.org/3.1.0/tutorials/index.html).

### Allämnt om figurer
Du kan modifiera din figur på många sätt.
```python
plt.figure(figsize(10, 10)) # Skapar ny figure av storlek 10*10 inches
plt.ylim(0, 10) # Gör så att plotfönstret är mellan 0 och 10 på yaxeln
plt.xlim(0, 10) # Gör motsvarande för x-axeln
plt.xlabel("x-axel (s)") # Sätter text på x-axeln
plt.ylabel("y-axeln (m)") # Sätter text på y-axeln
plt.title("Min fina graf") # Sätter en titel   
plt.grid(True) # Gör så att man får ett rutnär i plotten
plt.show() # Visar plotten
plt.savefig("min_graf.png") # Sparar plotten till min_graf.png
```

### Plotta linjer
Oftast vill vi bara plotta linjer genom punkter vi anger. 
```python
plt.plot(x1, y1, color="red", linewidth=0.5) # Plottar en röd linje med bredd 0.5. x1 och y1 kan vara listor eller np-arrayer av rank 1.
plt.plot(x2, y2, color="blue", linewidth=0.7) # Gör samma som ovan fast en tjockare blå linje
plt.legend(["linje 1", "linje 2"]) #Sätter en legend 
```
### Plotta stapeldiagram
Om man vill plotta ett stapeldiagram kan man använda `plt.bar()`.

```python
bar = plt.bar(x=x, height=heights, width=width, bottom=bottoms) # Lägger till ett antal staplar. Informationen sparas i bar
plt.legend(bar[0], "mina staplar") # Lägger till en legend
```

### Plotta bilder
Om du har en array av rank 2 du vill plotta kan du använda `plt.imshow()`.

```python
plt.imshow(picture, cmap='PiYG') # Plottar arrayen picture som en bild med colormap 'PiYG'
plt.clim(-1.0, 1.0) # Sätter ändpunkterna för colormappen
plt.colorbar(label='min färgskala') # Skapar en colorbar med en label
```

