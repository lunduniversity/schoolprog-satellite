# Introduktion till NumPy
I denna uppgift kommer vi kolla på biblioteket NumPy. Centralt i NumPy är arrayer. Dessa kan man oftast tänka sig som en- eller tvådimensionella listor fast med andra egenskaper. Varför då använda arrayer och inte bara vanliga listor? Anledningen är delvis att NumPy kan utföra operationer på arrayer mycket snabbare än vad man kan göra på vanliga listor och framför allt är det mycket smidigare att utföra operationer på arrayer jämfört med vanliga listor. Dessutom finns det en massa andra bibliotek som använder NumPy-arrayer, bland annat `matplotlib` som du känner till.

Om man har kommit väldigt långt i matten och läst lite linjär algebra kan man säga att NumPy behandlar matriser och vektorer effektivt.

Denna uppgift kan köras på [repl.it](https://repl.it/languages/python3) eller colab: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lunduniversity/schoolprog-satellite/blob/master/exercises/numpy_intro/Introduktion_NumPy.ipynb)


## 1. Din första NumPy array
I sin lättaste form kan arrayer vara väldigt lika vanliga listor. För att använda arrayer måste vi importera NumPy biblioteket. Skriv följande kod:

```python
import numpy as np
```
Vi kan nu skapa en array och printa den genom att skriva:

```python
a = np.array([1,2,3])
print(a)
```
Som du ser så kan vi använda en vanlig python lista som argument till `array()`. Detta gör att vi till exempel kan ta färdiga listor och på ett enkelt sätt omvandla till en array. Det finns såklart även många andra sätt att skapa nya arrayer. Om man till exempel vill ha en array med nollor kan man skriva:
```python
a = np.zeros(10)
```
**Uppdrag:** Använd `print()` för att se hur arrayen `a` ser ut.

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre>a = np.zeros(10)
print(a)</pre>
</p>
</details>

Vi kan även skapa arrayer av olika rank. En arrays rank motsvarar hur många dimensioner arrayen utgör. En vanliga lista motsvarar rank 1 medan en tvådimensionell lista, eller rutnät motsvarar rank 2. På samma sätt som en bild kan vara 2D eller 3D kan en array ha olika många dimensioner. Om vi vill skapa vår tidigare array fast nu i rank 2 istället kan vi skriva:

```python
a = np.zeros((10,10))
```
Om du printar denna på samma sätt som tidigare kommer du se att vi nu har fått en array av rank 2. Vi kan även skapa en liknande array med ettor genom att skriva:



```python
a = np.ones((10,5))
```

**Uppdrag:** Skapa en array `b` av rank 1 med 5 valfria tal. Skriv sedan `print(b*a)`. Vad hände?

Som du såg så multiplicerades din array elementvis med varje rad av arrayen med ettor. Vi kommer kolla mer på hur detta och liknanande funktioner kan användas i nästa del.

Vill du skapa en array av rank 2 kan du också använda `array()`-metoden fast på en tvådimensionell lista.

**Uppdrag:** Kör följande kod och variera parametrarna för att se vad som händer:

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
```


## 2. Operationer på arrayer
När det kommer till operationer skiljer sig arrayer en hel del från listor. Om vi tidigare har velat lägga ihop två listor elementvis har vi varit tvugna att själva loopa igenom listorna och lägga ihop elementen. Skriv följande kod:

```python
a = [1,2,3]
b = [4,5,6]
print(a+b)

npa = np.array([1,2,3])
npb = np.array([4,5,6])
print(npa+npb)
```

**Uppdrag:** Vad blev skillnaden i ovanstående kod?

<details>
<summary markdown="span">
Svar
</summary>
<p>När vi använder <code>+</code> mellan vanliga listor läggs de ihop till en lista medan <code>+</code> mellan arrayer adderas arrayerna elementvis.
</p>
</details>

Denna egenskap gör att det blir väldigt smidigt att använda arrayer för just matematiska beräkningar. De flesta operationer som går att köra på ett tal, går att köra på en array och körs då elementvis. Det går även att skriva tillexemepel `array +2 ` där vi kommer då lägga till två på varje plats i arrayen `array`.

**Uppdrag:** Skapa en valfri array och testa operationer så som `*`,`**`, `-` och `/`.










## 3. Använd NumPy för att plotta funktioner
Ett vanligt användningsområde för NumPy är när man vill skapa grafer till funktioner. I uppgiften "Plotta funktioner" som du kanske redan har gjort har du plottat funktioner med hjälp av listor. Men vi ska visa hur vi enklare kan göra det med arrayer.

För att börja måste vi skapa x-värdena för punkterna vi vill plotta. Detta kan göras med `np.linspace(start, stop, nbr_points)` som skapar en array av rank 1 vars första värde är `start`, sista värdet är `stop` och den inntehåller `nbr_points` stycken värden.

**Uppdrag:** Kör följande kod och variera de olika parametrarna för att se vad som händer.

```python
a = np.linspace(0, 10, 5)
print(a)
```

Det finns också en annan funktion lik `linspace()` för att skapa liknande arrayer av rank 1. Denna funktion är `arange(start, stop, step)` som ger en array av rank 1 som börjar på `start` och ökar med `step` i varje steg, och dess sista värde är precis mindre än `stop`, det vill säga, om man hade gått ett steg till hade värdet blivit större än eller lika med `stop`.

**Uppdrag:** Kör följande kod och variera de olika parametrarna för att se vad som händer.

```python
a = np.arange(0, 10, 2)
print(a)
```

Fördelen med `linspace()` är att man får precis de start- och slutpunkter man vill och kan lätt bestämma hur många punkter man vill ha, medans detta är inte är fallet för `arange()`, den är istället bra när man vill ange specifikt hur långa steg man ska ta.

För att få punkter vi kan ge till `matplotlib` vill vi nu använda funkioner på värdena vi får från exempelvis `linspace()`. Och här kommer en av de stora fördelarna med NumPy: Vi kan väldigt lätt applicera funktioner elementvis på arrayer. Till exempel finns det `np.cos(x)` som applicerar cosinusfunktionen elementvis på arrayen och det finns många andra som till exempel `np.exp(x)` som är exponentialfunktionen elementvis. De flesta funktioner man kan tänkas behöva finns. För en utförligare lista över funktionerna kan man se [denna sida](https://www.geeksforgeeks.org/numpy-mathematical-function/).

**Uppdrag:** Kör följande kod och se vad som händer. Vad betyder de olika delarna? Vad händer när du varierar antalet punkter i `linspace()`?

```python
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.savefig("myplot.png")
```

<details>
<summary markdown="span">
Svar
</summary>
<p>
<code>x = np.linspace(0, 10, 100)</code> skapar en array av x-värden. <code>y = np.sin(x)</code> applicerar sinusfunktionen elementvis på var av dessa värden. Detta gör att vi får massa punkter på grafen till sinusfunktionen. Sist plottar vi den som vanligt. Ju fler punkter man har i linspace, desto "mjukare" blir kurvan.
</p>
</details>


**Uppdrag:** Plotta exponentialfunktionen mellan -1 och 1.

<details><summary markdown="span">Lösning</summary>
<p>
<pre><code>x = np.linspace(-1, 1, 100)
y = np.exp(x)
plt.plot(x, y)
plt.savefig("myplot.png")
</code></pre></p>
</details>

## Fortsättningsuppgifter

- Plotta tangensfunktionen. Går det fläckfritt eller stöter du på några problem? Hur löser du dem?
