# Förkunskaper för uppdragen

## Innan du börjar med uppdragen
Förstår du hur detta program fungerar och vad det skriver ut? I så fall har du lagom förkunskaper.

```python
import matplotlib.pyplot as plt

def power(x, n):
    return x**n

def get_x_list(start, stop, step):
    ret = []
    curr = start
    while(curr < stop):
        ret.append(curr)
        curr += step
    return ret

def plot():
    x = get_x_list(-37, 37, 0.01)
    y = []
    for value in x:
        y.append(power(value, 3))
    plt.plot(x, y)
    plt.show()

plot()
```

Om du aldrig har programmerat tidigare, eller vill repetera lite, så kan du köra igenom följande uppdrag från [LU skolprogrammering](https://lunduniversity.github.io/schoolprog/):

*  [Månghörningar](https://lunduniversity.github.io/schoolprog/exercises/back-to-start). Bra första-uppgift. Du lär dig om sekvenser och loopar.
*  [Slumpvandring](https://lunduniversity.github.io/schoolprog/exercises/random-walk). Du lär dig om villkorssatser och blockstruktur.
*  [Kvadrera talet](https://lunduniversity.github.io/schoolprog/exercises/square-the-number). Du lär dig lite om input, output, strängar och andra typer av värden.
*  [Avlusning](https://lunduniversity.github.io/schoolprog/exercises/debugging). Lite grunder om felsökning vilket är mycket viktigt när man programmerar.
*  [Plotta funktioner](https://lunduniversity.github.io/schoolprog/exercises/plot/). Du lär dig grunder om plottning.

<!--
## Svårighetsordning för uppdragen
Många av uppdragen bygger på varandra och vissa uppdrag förutsätter att ni har lärt er begrepp från tidigare uppdrag. Ordningen vi rekommenderar är därför:

1. Väderdata
2. Keelingkurvan
3. Introduktion NumPy
4. Torkan
5. Torkan 2
6. Väderdata 2
7. CO2-utsläpp i Sverige
8. CO2-utsläpp per capita

Notera att detta bara är en rekommendation och att ni kan göra dem i en annorlunda ordning.
-->
