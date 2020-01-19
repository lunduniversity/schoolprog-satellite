# Extra Snabbreferens för prototypuppgifter
Snabbreferens för prototypuppgifterna för programmering med miljödata


## Bokeh
Bokeh är ett alternativ till `matplotlib` som är bättre till att göra interaktiva uppgifter. Åter igen kommer vi inte kunna ta med allt här. För mer information om bokeh, se [här](https://bokeh.pydata.org/en/latest/docs/user_guide.html).

### Skapa en figur

Centralt i `bokeh` är `figure()`, den skapar en figur/plot som du sedan lägger till saker i och till sist visar.
```python
from bokeh.plotting import figure
from bokeh.io import output_notebook, show
plot = figure(title="Min titel", plot_height=300, plot_width=600, y_range=(-10, 15)) # Skapar en figur
output_notebook() # Säger att man ska outputta figuren i notebooken
show(plot) # Visar plotten
```

### Plotta linjer
Att plotta linjer är ganska likt i bokeh som i matplotlib.

```python
my_line = plot.line(x, y) # Skapar en linje med listorna x och y
```

### Plotta stapeldiagram
Även stapeldiagram är ganska likt matplotlib.

```python
my_vbar = plot.vbar(x, top=y, width = 0.5) # Skapar staplar av listorna x och y
```

## Ipywidgets
Ipywidgets kan användas för att skapa sliders och dropdowns vilket gör grafer interaktiva.

### Ipywidgets och bokeh
Det som funkar bäst med ipywidgets är bokeh med det kan inte köras i google colab.
```python
#importera bibliotek:
from ipywidgets import interact
from bokeh.io import push_notebook, show, output_notebook
from bokeh.plotting import figure
output_notebook()

def update(city): # update-funktion som anropas när man väljer något nytt
    my_line.data_source.data['y'] = get_data(city) # ändrar datan för en bokeh-linje med en lista av data från get_data(city)
    push_notebook(handle=my_handle) # uppdaterar en bokeh-plot med ett visst handle

my_handle=show(plot, notebook_handle=True) # visar plotten och ger den ett speciellt handle
interact(update, city=["Lund", "Malmö"]) # visar en dropdown som anropar update
```

### Ipywidgets och matplotlib
Man kan också använda ipywidgets och matplotlib, men man får laggig interaktion. Detta kan dock köras i google colab.

```python
# importera bibliotek:
from ipywidgets import interact
import matplotlib.pyplot as plt
import numpy as np

def update(slope): # update-funktion för ipywidgets
    plt.figure(figsize=(12, 7)) # Skapa en ny figur
    x = np.linspace(-10, 10, 1000) # Skapa x-värden
    y = x * slope # Beräkna y-värden för en linje med lutning slope
    plt.ylim(-10, 10) # Sätt y-gränser
    plt.xlim(-10, 10) # Sätt x-gränser
    plt.plot(x, y) # Plotta värdena

interact(update, slope=(-10, 10, 0.01)) # Skapa en slider från -10 till 10 som hoppar 0.01 i varje steg.
```
