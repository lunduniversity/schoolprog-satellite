# Förkunskaper för uppdragen

Förstår du vad detta program skriver ut? I så fall har du lagom förkunskaper.

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
