# För utvecklare

## Uppdatera notebooks
Från början låg originalfilerna för Colab Jupyter notebooks på Google Colab/Drive, i 2019-Rymden/Colabs/Uppdrag. Filerna kopierades manuellt till GitHub.

Sedan december 2019 ligger i stället originalen på GitHub. OAuth access har lagts till så att man kan spara direkt till GitHub via Colab-kommandot `File -> Save a copy to GitHub`.

Det är dock viktigt att man öppnar Jupyter-filen via rätt länk för att detta ska funka. Använd colab-länkarna som finns i `README.md`-dokumenten.

### Hur länkar till notebooks skall vara.

Jupyter-filerna har extension `ipynb`.

Om t.ex. en Jupyter-fil finns på följande url i github:
```
                      https://github.com/lunduniversity/schoolprog-satellite/blob/master/exercises/drought/Bokskogen.ipynb
```
så ska man surfa till följande länk för att automatiskt öppna en kopia i colab:
```
https://colab.research.google.com/github/lunduniversity/schoolprog-satellite/blob/master/exercises/drought/Bokskogen.ipynb
```
Dvs man byter helt enkelt prefixet från

```
https://github.com/
```
till
```
https://colab.research.google.com/github/
```

Alla colab-länkar i `exercises/README.md` är fixade på detta sätt. Det gör att användarna direkt får en editerbar kopia av filen, och slipper också göra "open in playground" som tidigare.

### Vad som sparas mellan sessioner
Vad som sparas mellan sessioner på google colab: Koden i rutorna, outputten från rutorna och allt i textrutorna. Men filer, pythonvariabler, installerade bibliotek etc. sparas inte och måste laddas in igen. Då eleverna ska göra uppgiften vill vi inte ha tidigare outputs sparade. Ta därför bort alla outputs i orginalfilen. Man kan lägga till en keyboard shortcut för att ta bort alla outputs under Tools.

### Hämta data i notebooks
- Antingen görs detta genom `wget` som tar ganska lång tid, men går bra för filer som bara är några MB. Vi brukar använda det för att hämta datafiler från GitHub

- Kör man på colab kan man också hämta data från drive. Detta beskrivs i `guide_to_loading_data_from_drive.ipynb` [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lunduniversity/schoolprog-satellite/blob/master/for_developers/guide_to_loading_data_from_drive.ipynb).
- I binder kan datafiler placeras i repot och då behöver man inte hämta dem.

## Uppgifter på repl.it

Vissa uppgifter har hela uppgiftsbeskrivningar i Markdown format i motsvarande README och kan köras på repl.it. De senare uppgifterna har bara gjorts för Google Colab men skulle relativt lätt kunna översättas för att passa repl.it. För att sköta datahantering med repl.it har vi skapat repls där vi laddat upp datafilerna och sen kopierat en delningslänk.

## Binder

Guide till binder finns [ħär](https://mybinder.readthedocs.io/en/latest/introduction.html).

### Hämta länk
Binderlänker hämtas från [deras hemsida](https://gke.mybinder.org/). Där kopierar man in länken till repot. Man kan också ange om man direkt vill öppna en fil med länken, detta har vi gjort för uppgiften som använder binder, så när man klickar på binderlänken öppnar man direkt uppgiften.

### Configfiler

För att använda binder (och för att kunna köra uppgiften man vill) måste man ha vissa configfiler. Dessa finns i home i repot. Just nu finns `postBuild` och `requirements.txt`.

`requirements.txt` öppnar bestämmer vilka pythonbibliotek som ska installeras, för att uppgiften ska gå att köra är det viktigt att versionerna som nu är angivna används. Vi har haft problem med att nyare versioner av `ipywidgets` inte fungerar.

I `postBuild` finns kommandon som körs av binder innan man kommer in. Här finns några jupyterinställningar som är viktiga för att uppgiften ska gå att köra. Det finns också en funktion att man måste trusta notebooks för att kunna köra den. I `postBuild` finns ett kommando som gör att uppgiftsnotebooken automatiskt trustas.  

## Hur elever skulle köra uppgifter

### Google colab

När en elev klickar på en Google Colab länk kommer en kopia av notebooken öppnas i editerbart och körbart läge. Man kan dock inte spara något om man inte gör "Save a copy to Drive".

Om en elev vill fortsätta på en sparad uppgift finns den i en map med namnet "Colab Notebooks" på sin Drive om man inte själv angett något annat. All kod är sparad men "Runtime" är återställd så man blir eventuellt tvungen att köra de kodblock man skapat sedan tidigare om uppgiften bygger vidare på tidigare kodrutor.

*Obs!* Det hände för någon på vattenhallen att de fick felmeddelande 400 när de klickade på en gammal colab-länk (som gick direkt till google drive). Problemet verkade vara att de inte var inloggade på Google. Med de nya länkarna så verkar man inte få det problemet. Men man måste logga in för att kunna köra koden.


### Repl.it

För att öppna uppgifter i repl.it behöver man bara klicka på länken som finns i README, då kommer man till en repl där data är förberedd. Om man vill spara sin kod för att forsätta senare krävs det att man har ett eget konto. Detta kan göras snabbt och gratis. Om du är inloggad sparas allt du gör automatiskt och du kan hitta din repl igen under "my repls".

### Binder
För att öppna uppgiften i binder klickar man på en förberedd binderlänk och väntar tills binder har byggt miljön. För att spara på binder är det lättaste att välja file och sedan download as `.ipynb`. Detta sparar filen lokalt på datorn (oklart om detta funkar för chromebooks). För att sedan ladda upp den väljer man file och sedan open. Då kommer man ut till mappen notebooken ligger i. Då kan man välja upload och välja filen på sin dator. Sedan öppnar man den genom att trycka på den, notera att här sparas likt colab bara text, kod och output från kod.


## Beskrivning av notebookexperiment

- `test_of_bokeh_events_and_js.ipynb` [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lunduniversity/schoolprog-satellite/blob/master/for_developers/test_of_bokeh_events_and_js.ipynb) är ett test av att plotta bilder med bokeh och registrera var användaren klickar i bilden. Det var tänkt att detta skulle vara början på en speluppgift där man skulle gissa sjöstorlek. Man läser in en satellitbild av bokskogen från drive. Bilderna som laddas in finns i 2019-Rymden/Colabs. Med hjälp av javascript skivs det i consolen när man klickar nånstans, och koordinaterna för där man klickar.
- `example_of_interactive_bokeh_in_colab.ipynb` [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lunduniversity/schoolprog-satellite/blob/master/for_developers/example_of_interactive_bokeh_in_colab.ipynb) är ungefär som Väderdata 2 fast den använder javascript för att uppdatera grafen.
- `guide_to_loading_data_from_drive.ipynb` [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lunduniversity/schoolprog-satellite/blob/master/for_developers/guide_to_loading_data_from_drive.ipynb) är en guide som visar hur man lätt laddat in data från drive. Den ska vara ganska förklarande.

## Uppgiftsstruktur

### Uppgiftsbeskrivning
I vissa uppgifter står en beskrivning i `README`, det är för uppgifterna som kan köras i repl.it. Alla uppgifter finns också på notebookbformat. Väderdata 2 har två olika beskrivningar, en för binder som använder bokeh och en för colab som använder matplotlib.


### Data
Den data som används i uppgifterna finns antingen i samma mapp som uppgiften eller motsvarande map i schoolprog-satellite-data repot (för större filer). Ifall filerna är större än några MB har vi lagt dem på Drive för att snabbare kunna hämta in dem till Colab (ca 70MB/s från Drive till Colab). Den enda uppgiften vi gör detta för är Torkan 2. Där ligger datan i 2019-Rymden/Torkan 2018/sentinel2_sw_scania.tar.gz.

För Väderdata har data hämtats från SMHI. Scripten för detta finns i katalogen `smhidata`.
