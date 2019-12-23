# Keelingkurvan
I denna uppgift kommer vi utforska Keelingkurvan som beskriver koldioxidhalten i atmosfären. Mätningarna har utförts på Hawaii i ett laboratorium som befinner sig på vulkanen Mauna Loa sedan 1958. Observationerna på Mauna Loa var de första att tyda på att koldioxidhalten ökar i vår atmosfär.

För att enklast köra igång kan man gå till [repl.it](https://repl.it/@TeodorBucht1729/Keelingkurvan) där vi förberett datan. Uppgiften kan också köras på Colab på följande länk: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lunduniversity/schoolprog-satellite/blob/master/exercises/co2/Keelingkurvan.ipynb). Om man vill kan man också ladda ned den från [GitHub](https://github.com/lunduniversity/schoolprog-satellite/tree/master/exercises/co2).

## 1. Inläsning och plottning av data
Givet är en `.txt` fil som ni själva kan öppna och kolla på. Denna fil innehåller all data ni kommer behöva. Om ni kollar på filen ser ni att den består av 7 kolumner. De första två kolumnerna innehåller året och månaden för mätningen. Den tredje kolumnen innehåller året på decimalform, vilket är smidigt för att få rätt tidsskala på x-axeln. Den fjärde kolumnen innehåller det uppmätta medelvärdet för den månaden mätt i ppm CO2-molekyler i torkad luft. ppm står för points per million så värdena beskriver hur många CO2-molekyler per miljon luftmolekyler det finns i luften. Den observanta läsaren kanske här ser att vissa av dessa värden är -99.99. Detta beror på att mätvärdena för denna månaden inte blev tillräckligt bra. För att lösa detta problem har värden *interpolerats* med hjälp av resterande uppmätta värden. Detta innebär i princip att man räknar ut vad värdet borde ha varit om det förändras regelbundet. Vi kommer främst att använda de färdiginterpolerade värdena som finns i den femte kolumnen. I den sjätte kolumnen finns värden som beskriver en trend.

**Uppdrag:** Läs in åren på decimalform i en lista `years` och de interpolerade CO2-värdena i en lista `co2`.

<details>
<summary markdown="span">
Tips
</summary>
<p>
Använd <code>with open("data.txt", "r") as f:</code> och <code>data=f.read()</code> för att få hela filen som en sträng. Används sedan <code>data.split("\n")</code> för att dela upp filen vid varje rad.
</p>
</details>

<details><summary markdown="span">Lösning</summary>
<p>
<pre><code>with open("data.txt", "r") as f:
    data=f.read()
data = data.split("\n")
years=[]
co2=[]
for line in data:
    splitted = line.split()
    years.append(float(splitted[2]))
    co2.append(float(splitted[4]))
</code></pre></p>
</details>

Nu vill vi givetvis visualisera datan för att se hur keelingkurvan faktiskt ser ut.

**Uppdrag:** Kör följande kod och variera olika plotparametrar för att förstå vad de gör.
```python
import matplotlib.pyplot as plt
plt.plot(years, co2, color="red", linestyle="solid", marker="o", markersize=1.5, linewidth=0.5)
plt.savefig("keeling.png")
```
För ytterligare parametrar och information om de vi använder kan man läsa [här](https://matplotlib.org/2.1.1/api/_as_gen/matplotlib.pyplot.plot.html).

Vi vill gärna se trenden i samma plot.

**Uppdrag:** Läs in värdena från den sjätte kolumnen och spara dem i listan `trend` som du ska plotta i samma graf. Denna linje ska vara blå.

<details>
<summary markdown="span">
Tips
</summary>
<p>
Skriv ytterligare en <code>plt.plot()</code> direkt efter den första fast med trenden för att få dem i samma figur.
</p>
</details>

<details><summary markdown="span">Lösning</summary>
<p>
<pre><code>with open("data.txt", "r") as f:
    data=f.read()
data = data.split("\n")
years=[]
co2=[]
trend=[]
for line in data:
    splitted = line.split()
    years.append(float(splitted[2]))
    co2.append(float(splitted[4]))
    trend.append(float(splitted[5]))
import matplotlib.pyplot as plt
plt.plot(years, co2, color="red", linewidth=0.5)
plt.plot(years, trend, color="blue", linewidth=0.7)
plt.savefig("keeling.png")
</code></pre></p>
</details>

Nu har du förhoppningsvis en ganska fin graf men du tänker kanske att den inte särskilt förklarande, till exempel står det inte på axlarna vilka enheter det är och en utomstående person förstår nog inte vad de olika linjerna betyder. Det finns ännu fler saker som saknas för att det ska blir en riktigt bra graf. Detta problemet ska vi lösa nu! Ändra din förra plot-kod till följande:
```python
plt.plot(years, co2, color="red", linewidth=0.5)
plt.plot(years, trend, color="blue", linewidth=0.7)
plt.xlabel("År")
plt.ylabel("ppm CO2")
plt.title("Keelingkurvan")
plt.legend(["CO2", "Trend"])
plt.grid(True)
plt.savefig("keeling.png")
```
**Uppdrag:** Lek runt lite med de olika parametrarna och se hur grafen ändras för att förstå vad de har för innebörd.

De flesta metoderna är ganska självförklarande men vi listar ändå lite korta förklaringar här.
- `plt.xlabel()` tar en sträng och sätter texten på x-axeln till detta.
- `plt.ylabel()` funkar likadant fast för y-axeln.
- `plt.title()` sätter en titel för hela grafen.
- `plt.legend()` lägger till en liten ruta som beskriver de olika linjerna. Den tar en lista av strängar, en sträng för varje linje.
- `plt.grid()` avgör om grafen ska ha något rutnät eller inte.

Alla dessa metoderna går att variera ytterligare efter användarens önskan och det finns många fler valbara parametrar än vad vi skriver om här. För att lära sig mer kan man läsa på [här](https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot).


## 2. Förenkla datanvändningen med hjälp av dict
Om vi lättare vill kunna kolla på ett specifikt år eller månad skulle vi kunna lagra vår data i en `dict` istället. Vi skulle då kunna använda ett år och månad som nyckel för att lättare kunna plocka ut värden för ett motsvarande datum.

**Uppdrag:** Skapa en `dict` med tuplar `(year, month)` som nycklar för ett smotsvarande mätvärde. `year` och `month` kan båda var heltal där `month` representeras av talen 1 till 12.
<details>
<summary markdown="span">
Tips
</summary>
<p>
Du kan använda kod liknande den du använde för att bygga upp listorna innan, men istället lägga in det i en <code>dict</code>.
</p>
</details>


<details>
<summary markdown="span">
Lösning
</summary>
<p><pre>with open("data.txt", "r") as f:
    data=f.read()
data = data.split("\n")
co2_dict = {}
for line in data:
    splitted = line.split()
    co2_dict[(int(splitted[0]), int(splitted[1]))] = float(splitted[4])</pre>
</p>
</details>

## 3. Medelvärde för varje år

Vi vill nu använda vår `dict` för att räkna ut ett medelvärde för varje år. För att göra detta kan vi skapa en funktion `avg_year(year)` som tar in ett heltal `year` och returnerar ett genomsnittligt värde för hela året.

**Uppdrag:** Skriv funktionen `avg_year(year)`.


<details>
<summary markdown="span">
Lösning
</summary>
<p><pre>def avg_year(year):
    total = 0
    for i in range(1,13):
        total += co2_dict[(year,i)]
    return total/12</pre>
</p>
</details>

**Uppdrag:** Kommer lösningen till föregående uppgift fungera för alla år? Vad returnerar `avg_year(1958)`? Är din lösning bättre?

<details>
<summary markdown="span">
Svar
</summary>
<p>Åren 1958 och 2019 har inte data för alla månader. Vår funktion antar att alla månader finns med för alla år i <code>co2_dict</code>, vilket gör att programmet kraschar.  
</p>
</details>

En viktig detalj i programmering är att komma ihåg undantagsfallen som koden måste klara av. Det är lätt hänt att man bara testar <i>korrekt</i> indata och glömmer bort undantagsfall. I detta fall måste vi se till att vår metod klarar av de fallen då vi inte har mätdata för alla månader.

**Uppdrag:** Ändra funktionen `avg_year(year)` så att den inte kraschar då data fattas utan istället använder den data som finns för att räkna ut medelvärdet.

<details>
<summary markdown="span">
Tips
</summary>
<p>För att kolla om det finns ett värde kopplat till en viss nyckel kan du skriva: <code>(year, month) in co2_dict</code>, vilket kommer returnera <code>True</code> om det finns och annars <code>False</code>.
</p>
</details>

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre>def avg_year(year):
    total = 0
    values = 0
    for i in range(1,13):
        if((year,i) in co2_dict):
            total += co2_dict[(year,i)]
            values += 1
    return total/values</pre>
</p>
</details>

Vi kan nu ta fram en lista som inehåller medelvärde för åren 1958 till 2019 med hjälp av vår nya metod.

**Uppdrag:** Skapa listan `mean_year` med hjälp av funktionen `avg_year(year)`.

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre>mean_year = []
for i in range(1958,2020):
    mean_year.append(avg_year(i))
</pre>
</p>
</details>

**Uppdrag:** Plotta nu samma sak som i avsnitt 1 fast med `mean_year` istället för `trend`. Ser du någon skillnad när du använder `mean_year` istället för `trend`?
<details>
<summary markdown="span">
Lösning
</summary><p><pre>
plt.plot(years, co2, color="red", linewidth=0.5)
plt.plot(range(1958, 2020), mean_year, color="blue", linewidth=0.7)
plt.xlabel("År")
plt.ylabel("ppm CO2")
plt.title("Keelingkurvan")
plt.legend(["CO2", "Årsmedelvärde"])
plt.grid(True)
plt.savefig("year_mean.png")
</pre></p>
</details>

<details>
<summary markdown="span">
Svar
</summary>
<p>Om din kod är lik lösningsförslagen borde det se ut som <code>mean_year</code> hela tiden ligger lite högre än vad <code>trend</code> gör. Vad kan detta bero på?
</p>
</details>

<details>
<summary markdown="span">
Svar
</summary>
<p><code>mean_year</code> har bara ett värde per år medan <code>trend</code> har tolv. Detta gör att <code>mean_year</code> blir lite missvisande då hela årsgenomsnittet kommer hamna på motsvarande plats för januari i <code>trend</code>. Med andra ord blir hela grafen förskjuten ett halvår åt vänster.
</p>
</details>

**Uppdrag:** Förskjut `mean_year` ett halvår till höger för att bättre representera medelvärdet.

<details>
<summary markdown="span">
Lösning
</summary><p><pre>actual_years = [i+0.5 for i in range(1958, 2020)]
plt.plot(years, co2, color="red", linewidth=0.5)
plt.plot(actual_years, mean_year, color="blue", linewidth=0.7)
plt.xlabel("År")
plt.ylabel("ppm CO2")
plt.title("Keelingkurvan")
plt.legend(["CO2", "Årsmedelvärde"])
plt.grid(True)
plt.savefig("year_mean.png")
</pre></p>
</details>

## 4. Hur ser ökningen ut?

Genom att studera kurvorna kan vi ganska enkelt dra slutsatsen att koldioxidhalten i atmosfären har ökat sedan 1958. En intressant detalj kan vara att kolla på om själva ökningen ökar eller minskar för varje år (detta motsvarar andraderivatan som du kanske känner igen från matten). De senaste åren har man pratat väldigt mycket om att vi måste bromsa våra koldioxidutsläpp (växthuseffekten). Vad visar våra siffror? Kan vi se att ökningen har börjat bromsa in?

**Uppdrag:** Skapa en lista `mean_diff` med alla skillnaderna mellan två på varandra följande års medelvärde.

<details>
<summary markdown="span">
Tips
</summary>
<p>Du kan tillexempel bestämma ökningen mellan 2018 och 2019 med <code>avg_year(2019)-avg_year(2018)</code>.
</p>
</details>

<details>
<summary markdown="span">
Lösning
</summary><p><pre>mean_diff = []
for i in range(1958,2018):
    diff = avg_year(i+1)-avg_year(i)
    mean_diff.append(diff)</pre>(Då medelvärdet för 2019 inte är baserat på alla månader kommer ökningen inte motsvara den faktiskt ökningen och vi väljer därför att inte ta med den.)</p>
</details>

**Uppdrag:** Plotta `mean_diff`. Hur ser ökningen ut? Har vi börjat bromsa in ökningen?

<details>
<summary markdown="span">
Lösning
</summary><p><pre>plt.plot(range(1958,2018), mean_diff)
plt.savefig("mean_diff.png")</pre></p>
</details>

<details>
<summary markdown="span">
Svar
</summary><p>Ökningen varierar en del från år till år vilket gör att grafen blir ganska spretig. Det ser dock ut som att ökningen har ökat sedan 1958. Det ser inte ut som någon inbromsning har börjat.</p>
</details>

## 5. Koldioxidcykeln under ett år
Om man zoomar in och kollar närmre på keelingkurvan ser man att den svänger väldigt kraftigt och regelbundet. Detta fenomen ska vi undersöka närmre.

**Uppdrag:** Skriv en funktion `plot_co2_year()` som givet ett år plottar koldioxidnivån från varje månad tillsammans med trenden som finns i `trend`. Använd funktionen för att plotta koldioxidnivåerna under 2018. Hur ser den ut? Varför tror du den ser ut som den gör?


<details>
<summary markdown="span">
Tips
</summary>
<p>
Det blir lättare att plotta ett specifikt år om du använder en <code>dict</code> för trenden också.
</p>
</details>

<details>
<summary markdown="span">
Lösning
</summary><p><pre>trend_dict={}
for line in data:
    splitted = line.split()
    trend_dict[(int(splitted[0]), int(splitted[1]))] = float(splitted[5])
def plot_co2_year(year):
    co2_year = []
    trend_year = []
    for i in range(1, 13):
        co2_year.append(co2_dict[(year, i)])
        trend_year.append(trend_dict[(year, i)])
    plt.plot(range(1, 13), co2_year, color="red", linewidth=2, marker="o")
    plt.plot(range(1, 13), trend_year, color="blue", linewidth=2, marker="^")
    plt.xlabel("Månad")
    plt.ylabel("ppm CO2")
    plt.title("Keelingkurvan 2018")
    plt.legend(["CO2", "Trend"])
    plt.grid(True)
    plt.savefig("month_mean.png")
plot_co2_year(2018)
</pre></p>
</details>

<details>
<summary markdown="span">
Svar
</summary>
<p>
Vi ser att koldioxidnivåerna ökar mycket under vintern/våren och minskar mycket under sommar/höst. Detta kan förklaras med att växterna absorberar en hel del koldioxid under sommaren och hösten, medans växterna dör eller temporärt slutar ta upp koldioxid under vintern/våren.
</p>
</details>

## Fortsättningsuppgifter

- Som vi beskrivit i början var vissa mätpunkter för dåliga för att vara med i datan. Till exempel saknas ett månadsmedelvärde från april 1984. Använd datan i den fjärde kolumnen för att själva interpolera ett värde för april 1984. Kolla hur nära du kommer värdet i femte kolumnen.
- Försök att själv ta fram en egen trend likt den sjätte kolumnen i datan. Jämför sedan din trend med trenden som ges i sjätte kolumnen.
