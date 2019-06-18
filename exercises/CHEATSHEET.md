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
