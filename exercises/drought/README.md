
# Hur påverkades Bokskogen av torkan 2018?
I denna uppgift ska vi se hur växtlighet kan undersökas med hjälp av satellitbilder. Vi ska titta på bilder över [Bokskogen](https://sv.wikipedia.org/wiki/Torups_rekreationsomr%C3%A5de), ett naturområde i Skåne. Bilderna är alla tagna under första halvan av augusti, men från tre olika år. Frågan är, kommer vi att kunna se någon skillnad efter en sommar med torka? Här är en färgbild från 2017 på området vi kommer undersöka senare:

![En färgbild över bokskogen.](tci_hd.png)

Det kan vara svårt att se om en gran mår bra eller dåligt med blotta ögat. Men vi kommer att använda oss av fler färger än de ögat kan se för att undersöka hur växtligheten mår.

## 1. Om satellitbilder

### 1.1 Pixlar och band

En satellitbild består av *pixlar* i ett rutmönster, som vi kan illustrera så här:

    o o o
    o o o
    o o o
    o o o

Varje pixel motsvarar en yta på t.ex. 10 x 10 meter på jorden. Så ovanstående pixlar skulle motsvara ett område som är 30 m brett och 40 m långt. En riktig satellitbild är förstås mycket större, med många fler pixlar.

Varje pixel har information om ljusintensiteten för flera olika färger, som rött, grönt eller blått. Men det kan också finnas information om färger utanför det synliga spektret, som till exempel *infrarött*.

För satellitbilder kallar vi färgerna för *band*. Det står egentligen för *frekvensband*, alltså ett frekvensområde. Färgen röd motsvarar till exempel frekvensområdet 405-480 THz (1 TeraHertz är tusen miljarder svängningar per sekund). Infrarött ljus har en lägre frekvens än rött.

Infrarött ljus består av ett ganska stort frekvensområde. Den del som ligger närmast rött ljus kallas *nära infrarött* ("near infrared" på engelska).

Satellitbilden innehåller information om de olika banden för varje pixel. Till exempel kan vi representera det röda bandet med en två-dimensionell numpy-array. Varje värde i arrayen motsvarar intensiteten av rött ljus på motsvarande punkt i bilden. Här är exempel på det röda bandet för en liten bit av en satellitbild:

    [[1186 1178 1126]
     [1318 1210 1322]
     [1342 1309 1400]
     [1376 1333 1405]]

**Uppdrag 1.1:** Provkör python-koden nedan som skapar numpy-arrayen för detta röda band:

```python
import numpy as np

red = np.array([
  [1186, 1178, 1126],
  [1318, 1210, 1322],
  [1342, 1309, 1400],
  [1376, 1333, 1405]])

print(red)
```

### 1.2 NDVI - Normalized Difference Vegetation Index

Växtlighet innehåller *klorofyll*, som spelar en avgörande roll i fotosyntesen, och också ger växterna deras gröna färg. Att växterna ser gröna ut beror på att de reflekterar grönt ljus. Rött ljus tas i stället upp av växten (det *absorberas*). Det visar sig att frisk vegetation också reflekterar *NIR* (nära-infrarött ljus). Om en pixel har högt värde i NIR-bandet, men lågt värde i röda bandet är det stor sannolikhet att pixeln motsvarar frisk vegetation.

För pixlarna ovan ser NIR ut så här:

    [[2953 3105 3239]
     [2109 2298 2062]
     [2260 1911 1546]
     [2348 1875 1222]]


För att bedöma vilka pixlar som innehåller frisk vegetation används *NDVI* - Normalized Difference Vegetation Index, som beräknas enligt formeln nedan:


           NIR - Red
    NDVI = ---------
           NIR + Red

Formeln ger alltid ett värde mellan -1 och 1.  Ju högre värde, desto friskare och tätare vegetation. Här är exempel på typiska värden från olika typer av terräng (enligt [https://custom-scripts.sentinel-hub.com/landsat-8/ndvi/](https://custom-scripts.sentinel-hub.com/landsat-8/ndvi/)):

|Terräng|Typiskt ndvi|
|:------|:-----------|
|vatten                                        | mellan -1.0 och -0.1|
|sand, sten, snö                               | mellan -0.1 och 0.1|
|friska gräs- och buskmarker (gles vegetation) | mellan 0.2 och 0.4|
|frisk skog och regnskog                       | mellan 0.4 och 1.0|


Så länge vi har NDVI-värden över 0.1 rör det sig troligen om någon form av (levande) vegetation. För jordbruksmark beror NDVI-värdet på vad man odlar.

Om vegetationen torkar ut blir NDVI-värdena lägre. Vi ser kanske ingen skillnad med blotta ögat - skogen eller odlingen är kanske lika grön - men med NDVI kan vi se om den håller på att torka ut.

**Uppdrag 1.2 a:** Skriv Pythonkod för att beräkna NDVI för övre vänstra pixeln. Vilken typ av terräng kan vi gissa att pixeln motsvarar?

*Tips* Här är ett kodskelett du kan använda:

```python
ndvi = (2953 - ...)/(... + ...)
print(ndvi)
```

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>ndvi = (2953 - 1186)/(2953+1186)
print(ndvi)
</code></pre>
</p>
</details>
<p></p>

<details>
<summary markdown="span">
Svar
</summary>
<p>
Resultatet är cirka 0.43 och vi kan gissa att det rör sig om skog eller annan tät vegetation.
</p>
</details>
<p></p>

**Uppdrag 1.2 b:** Skriv Pythonkod för att i stället beräkna NDVI för hela matrisen av pixlar i exemplet ovan. Vilka olika typer av terräng verkar finnas i området?

*Tips* Din kod behöver göra följande:
* Importera numpy-biblioteket
* Skapa matrisen `red` (på samma sätt som ovan)
* Skapa matrisen `nir` (på liknande sätt)
* Räkna ut en matris `ndvi` (genom att använda formeln)
* Skriv ut `ndvi`

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>import numpy as np
red = np.array([
  [1186, 1178, 1126],
  [1318, 1210, 1322],
  [1342, 1309, 1400],
  [1376, 1333, 1405]])
nir = np.array([
  [2953, 3105, 3239],
  [2109, 2298, 2062],
  [2260, 1911, 1546],
  [2348, 1875, 1222]])
ndvi = (nir - red)/(nir+red)
print(ndvi)
</code></pre>
</p>
</details>
<p></p>

<details>
<summary markdown="span">
Svar
</summary>
<p>
Vi ser att det finns värden inom flera olika intervall, och att det mesta är vegetation. Några områden har värden över 0.4 och är kanske skog. Andra områden har lite lägre värden och är kanske gräs eller någon form av odling.
</p>
</details>
<p></p>


För att läsa mer om NDVI se
* [https://sv.wikipedia.org/wiki/NDVI](https://sv.wikipedia.org/wiki/NDVI)
* [https://en.wikipedia.org/wiki/Normalized_difference_vegetation_index#Rationale](https://en.wikipedia.org/wiki/Normalized_difference_vegetation_index#Rationale)
* [https://earthobservatory.nasa.gov/features/MeasuringVegetation/measuring_vegetation_2.php](https://earthobservatory.nasa.gov/features/MeasuringVegetation/measuring_vegetation_2.php)

### 1.3 Enkel plottning av NDVI

Vi ska nu gå vidare och plotta NDVI-värdena.

**Uppdrag 1.3:** Plotta matrisen `ndvi` med hjälp av `imshow`. Vilka färger blir det? Hjälper färgerna dig att förstå bilden?

*Tips!* Du behöver
* Räkna ut `ndvi` enligt ovan.
* Importera `matplotlib` som vanligt
* Anropa `imshow` med `ndvi` som argument.
* Spara plotten i en fil som vanligt.

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>import matplotlib.pyplot as plt
plt.ion()
plt.imshow(ndvi)
plt.savefig(ndvi.png)
</code></pre>
</p>
</details>
<p></p>

Troligen tycker du inte att färgerna passar så bra. De pixlar med mest och friskast vegetation blir alldeles gula. Vi skulle vilja använda färger som passar bättre för NDVI.


### 1.4 Undersök hur färgskalan fungerar.

Matplotlib använder en *colormap* (färgskala) för att plotta varje pixel i en färg som motsvarar värdet. Den färgskala som används som standard heter `viridis`, och använder gröna, blåa och gula färger.

`viridis`-skalan är speciellt utformad för att vara lätt att läsa av, även för färgblinda (som har svårt att se skillnad mellan rött och grönt). För många fall när man ska visa data är det en mycket bra färgskala, men den passar inte riktigt för att visa NDVI.

Innan vi ger oss på att byta färgskala, låt oss först undersöka hur färgskalan fungerar.

**Uppdrag 1.4 a:** Lägg till ett anrop `plt.colorbar(label='NDVI')` till din plot. Du får färgskalan utritad. Vilket värde motsvarar den mörkaste blå? Vilket värde motsvarar den gulaste gul?

<details>
<summary markdown="span">
Svar
</summary>
<p>Den mörkaste blå används för det lägsta värdet i ndvi-matrisen, dvs ungefär -0.07. Den gulaste gula används för det högsta värdet i ndvi-matrisen, dvs ungefär 0.48.
</p>
</details>
<p></p>

Ser du att färgskalan matchas mot de värden vi råkar ha i ndvi-matrisen? Dvs det högsta värdet i matrisen matchas mot gulaste gul, och det lägsta mot mörkaste blå.

Detta är inte bra, för det gör ju att färgerna kommer att betyda andra värden om vi tittar på en annan ndvi-matris. Om vi t.ex. skulle titta på ett område där alla värdena ligger mellan 0.8 och 1.0, så kommer 0.8 att matchas mot mörkblått och 1.0 mot gult.

Vi skulle vilja att färgerna alltid betyder samma NDVI-värde, oavsett vilken NDVI-matris vi plottar. Detta kan vi åstadkomma genom att lägga till följande anrop:

```python
plt.clim(-1.0, 1.0)
```

`clim` står för "color limit" och talar om vilket område av värden som skall matchas mot färgskalan. Detta gör att om vi gör två olika plottar, så kommer samma färg att motsvara samma värde.

**Uppdrag 1.4 b:** Lägg till anropet till `clim`. Hur ändrades plotten?

<details>
<summary markdown="span">
Svar
</summary>
<p>Plotten använder inte längre hela färgskalan. Detta är bra eftersom vi då skulle kunna jämföra den med andra plottar, som visar andra ndvi-matriser.
</p>
</details>
<p></p>

Vi har löst en del problem nu, men inte alla. Vi skulle vilja ha en bättre färgskala.


### 1.5 Välj en bättre färgskala för NDVI

Det finns många olika färgskalor att välja mellan i Python, och man kan till och med skapa egna. Hur ögat uppfattar olika färger är komplext, och att konstruera bra färgskalor för att visa data är en vetenskap för sig.  

Vi ska prova en färgskala som heter `PiYG`. Den är rosa för låga värden, vit i mitten och grön för höga värden.

Vi kan ändra färgskalan genom att anropa `imshow` med ett extra argument `cmap` som talar om vilken `colormap` som skall användas. T.ex. så här:

```python
plt.imshow(ndvi, cmap="PiYG")
```

**Uppdrag 1.4 c:** Ändra anropet till `imshow` så att du använder `PiYG` som färgskala. Vilken färg mappas mot vilken sorts terräng? Är det lättare att förstå figuren nu?

<details>
<summary markdown="span">
Svar
</summary>
<p>Förhoppningsvis tycker du att figuren är lättare att förstå nu. Ju mörkare grön, desto högre ndvi-värde, och alltså friskare och tätare växtlighet. Barmark blir nära vit. Vatten blir rosa.
</p>
</details>
<p></p>

Det finns information om matplotlibs färgskalor här: [https://matplotlib.org/examples/color/colormaps_reference.html](https://matplotlib.org/examples/color/colormaps_reference.html)

Om du vill kan du experimentera med fler färgskalor, eller vänta tills lite senare när du tittar på hela satellitbilder.


## 2. Växtligheten 2015

Nu ska vi titta på data för hela naturområdet som nämndes i början (Bokskogen i Skåne).

Klicka på följande länk [https://repl.it/@OscarWiklund96/Bokskogen](https://repl.it/@OscarWiklund96/Bokskogen) för att få tillgång till satellit-datan som används i denna uppgift. Man kan även ladda ner datan från GitHub på [https://github.com/lunduniversity/schoolprog-satellite-data/tree/master/drought/bokskogen](https://github.com/lunduniversity/schoolprog-satellite-data/tree/master/drought/bokskogen).

I mappen Bokskogen ligger det tre filer som heter `data_15.npz`, `data_17.npz` och `data_18.npz`. Varje fil innehåller satellit-data från en dag i första halvan i augusti, men från olika år (2015, 2017 och 2018). Filerna är lagrade på numpy-format (`.npz`) som lätt kan läsas in till datastrukturer i Python.

(Filtypen `npz` står för att flera np-arrayer har lagts ihop ("zippats") till en fil.)

Vi ska börja med att läsa in filen `data_15.npz` som alltså innehåller data för en sensommardag 2015.


<!--Detta är numpy-arrays som innehåller ett heltal för varje pixel, som tillsammans kan skapa en bild. Vi ska börja med att kolla på `data_15.npz`. Skriv följande kod för att ladda in alla nödvändiga paket och npz-filen:-->

**Uppdrag 2 a:** Skriv följande kod för att ladda in filen:

```python
import numpy as np
import matplotlib.pyplot as plt
plt.ion()

bands15 = np.load('bokskogen/data_15.npz')
```

Variabeln `bands15` är en `NpzFile` och ger oss tillgång till innehållet i filen. Den fungerar ungefär som en nyckel-värdetabell, där vi kan slå upp numpy-arrayen för en viss nyckel.

**Uppdrag 2 b:** Ta reda på vilka nycklar som `bands15` har genom att anropa `list(bands15.keys())`. (`keys` ger en sekvens av nycklar som kan göras om till en lista med `list`.)

<details>
<summary markdown="span">
Svar
</summary>
<p>Om du gör <pre><code>print(list(bands15.keys()))</code></pre>
ser du att nycklarna är <code>"red"</code> och <code>"nir"</code> (nir = near-infrared)</p>
</details>
<p></p>

Vi ser att nycklarna är frekvensband, som `"red"` och `"nir"`. För varje nyckel finns en numpy-array som innehåller en matris med ljusintensiteter. Matrisen ser ut ungefär som i exemplet vi såg i 1.1, men är mycket större.

För att lättare kunna använda datan vill vi nu skapa en variabel för varje band.

**Uppdrag 2 c:** Skapa variablerna `red15` och `nir15` med hjälp av `bands15`.

*Tips!* Du kan slå upp ett värde genom att skriva `bands15["..."]`.

<details>
<summary markdown="span">
Svar
</summary>
<p><pre><code>red15 = bands15["red"]
nir15 = bands15["nir"]</code></pre>
</p>
</details>
<p></p>

Vi har nu delat upp datan för de båda banden var för sig. För att få en känsla av vad det faktiskt är för data vi har att göra med skulle vi kunna testa plotta dem.

**Uppdrag:** Plotta en eller båda variablerna vi precis skapade. Vad visar plotten?

*Tips!* Använd `imshow` för att plotta. Du kan använda standardfärgskalan och se vad du får.

<details>
<summary markdown="span">
Lösning
</summary>
<p><pre><code>plt.imshow(red15)
plt.savefig("red15.png")</code></pre>
</p>
</details>
<p></p>

Plotten visar en bild över Bokskogen med närliggande åkrar och sjöar. Bilderna består endast av ljus från röda respektive nära-infraröda bandet, vilket gör att det blir svårt att se vad de föreställer.



<!--
Behövs ej. Det blir exakt samma resultat. Kanske rest från Python2 ??

För att uträkningar ska bli mer exakta vill vi egentligen ha våra värden i form av flyttal. Gör om `red15` och `nir15` till flyttal med hjälp av följande kod:

```python
red15 = red15.astype(float)
nir15 = nir15.astype(float)
```
-->

För att lättare kunna tolka bilden vill vi räkna ut NDVI. Detta kommer göra att partier med mycket växtligher skiljer sig i färg gentemot partier utan växtlighet när vi plottar bilden.

**Uppdrag 2 d:** Skapa en variabel `ndvi15` och räkna ut den med hjälp av `red15` och `nir15`.

*Tips!* Använd formeln för att räkna ut ndvi, som du gjort tidigare.

<details>
<summary markdown="span">
Lösning
</summary>
<p>
<pre><code>ndvi15 = (nir15-red15)/(nir15+red15)</code></pre>
</p>
</details>
<p></p>

**Uppdrag 2 e:** Plotta `ndvi15` på liknande sätt som du gjorde i 1.4 och 1.5. Glöm inte att
* använda en bra färgskala, som `"PiYG"`
* sätta `clim` för att mappa färgskalan till tal mellan -1.0 och 1.0.
* lägga till en färgskala med hjälp av `colorbar`

<details>
<summary markdown="span">
Lösning
</summary>
<p>
<pre><code>plt.imshow(ndvi15, cmap="PiYG")
plt.colorbar(label='NDVI')
plt.clim(-1.0, 1.0)
plt.savefig("ndvi15.png")
</code></pre>
</p>
</details>
<p></p>

**Uppdrag 2 f:** Vad visar bilden? Kan du urskilja olika sorters terräng? Kan du se vilka bönder som inte har skördat sina åkrar än?

<details>
<summary markdown="span">
Svar
</summary>
<p>Ett fyrkantigt grönt område tyder på att det är en åkerlapp. En vitare åker tyder på att det finns låg växtlighet och att åkern troligtvis är skördad. Vita områden tyder på bebyggelse som hus och vägar. Till höger i bilden ser vi en flygplats (Sturup) med sina landningsbanor. Ett antal sjöar kan ses som rosa områden. Runtomkring sjöarna finns mörkgröna områden som inte ser ut att vara åkerlappar, så vi kan gissa att det är skog.
</p>
</details>
<p></p>

Vi kan notera att bilden är lite pixlig. Det beror på att vi dragit ner upplösningen så att filerna inte ska bli alltför stora.

<!--ATT KOLLA UPP: ÄR FILERNA KOMPRIMERADE EGENTLIGEN?--->

## 3. Jämför växtlighet
För att kunna jämföra åren måste vi nu egentligen göra samma sak för 2017 och 2018. Vi skulle kunna skriva ungefär samma kod som vi precis skrivit ytterligare två gånger, men detta är inte särskilt effektivt eftersom vi i princip skriver samma sak tre gånger med ett fåtal utbytta ord. För ändamål som dessa är därför funktioner väldigt användbara.

**Uppdrag 3 a:** Skriv en funktion `plot_ndvi(file_name, save_name)` som tar in en sträng `file_name`, som är namnet på `.npz`-filen du vill läsa in datan från, och en sträng `save_name`, som blir namnet på den bild som plottas. Bilden som plottas ska vara baserad på NDVI med liknande inställningar som innan.

*Tips!* Du kan återanvända väldigt stor del av den kod du redan skrivit. Du behöver dock lägga till ett anrop till `close` efter `savefig` eftersom du skapar flera bilder.

<details><summary markdown="span">Lösning</summary>
<p>
<pre><code>def plot_ndvi(file_name, save_name):
  bands = np.load(file_name)
  red = bands["red"]
  nir = bands["nir"]
  ndvi = (nir-red) / (nir+red)
  plt.imshow(ndvi, cmap="PiYG")
  plt.clim(-1.0, 1.0)
  plt.colorbar(label="NDVI")
  plt.savefig(save_name)
  plt.close()</code></pre></p>
</details>
<p></p>


Nu när du har en smidig funktion för att plotta NDVI kan du enkelt göra detta för alla tre år.

**Uppdrag 3 b:** Plotta NDVI för 2015, 2017 och 2018. Jämför bilderna. Kan du se någon skillnad? Om du ser skillnad, vilken och varför?

<details><summary markdown="span">Lösning</summary>
<p>
<pre><code>plot_ndvi("bokskogen/data_15.npz", "bok15.png")
plot_ndvi("bokskogen/data_17.npz", "bok17.png")
plot_ndvi("bokskogen/data_18.npz", "bok18.png")
</code></pre></p>
</details>
<p></p>

<details><summary markdown="span">Svar</summary>
<p>
Torkan 2018 hade sin påverkan på växtligheten. Om du tittar på åkrarna ser du att växtligheten inte är i närheten av de tidigare åren. Det ser ut som att många bönder blev tvungna att skörda de grödor som klarade sig mycket tidigare på grund av torkan. Man kan även se på själva skogen att växtligheten har sjunkit då den inte framstår som lika grön.</p>
</details>
<p></p>

**Uppdrag 3 c: (extra-uppgift)**  Modifiera funktionen `plot_ndvi()` så att du kan ange en titel för figuren och plotta figurerna igen fast med beskrivande titlar.

## 4 Quiz

### Fråga 1
En bild består av ett rutnät av smådelar som kallas
*   pixlar
*   band
*   färger

<details>
<summary markdown="span">
Svar
</summary>
<p>
pixlar
</p>
</details>
<p></p>

### Fråga 2
Ett frekvensband motsvarar ett
*   en färg
*   en rad pixlar
*   en intensitet

<details>
<summary markdown="span">
Svar
</summary>
<p>
en färg
</p>
</details>
<p></p>

### Fråga 3
Infrarött ljus har
*   frekvenser inom det synliga spektret
*   lägre frekvenser än det synliga spektret
*   högre frekvenser än det synliga spektret

<details>
<summary markdown="span">
Svar
</summary>
<p>
lägre frekvenser än det synliga spektret
</p>
</details>
<p></p>

### Fråga 4
Vad gäller om frisk växtlighet?
*   den reflekterar grönt och nära-infrarött ljus, men absorberar rött ljus
*   den reflekterar grönt och rött ljus, men absorberar nära-infrarött ljus
*   den reflekterar rött och nära-infrarött ljus, men absorberar grönt ljus

<details>
<summary markdown="span">
Svar
</summary>
<p>
den reflekterar grönt och nära-infrarött ljus, men absorberar rött ljus
</p>
</details>
<p></p>

### Fråga 5
Vilka värden används för att räkna ut NDVI (Normalized Difference Vegetation Index)?
*   rött och grönt ljus
*   rött och nära-infrarött ljus
*   grönt och nära-infrarött ljus

<details>
<summary markdown="span">
Svar
</summary>
<p>
rött och nära-infrarött ljus
</p>
</details>
<p></p>
