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

## Quizzar
Quizzar kan genereras till uppgifterna i colab med hjälp av `quiz.py`. Tanken är att man laddar ner `quiz.py` och en json-fil med uppgifter till colaben. Sen kan man generera ett quiz inne i colab. Exempel på hur detta görs finns i uppgiften `regional_greenhouse_emissions`.

### Quiz format
Antingen kan quizzet skrivas direkt som en json-fil. Se någon av de andra quizzen för exakt format. Det finns även en fil `jsonparser.py` som tar en txt-fil och gör om den till en json-fil med rätt format. txt-filen ska då vara på samma format som `example_quiz.txt`. Frågor är separerade från varandra med dubbla semikolon. Varje fråge-objekt inleds med frågan följt av ett semikolon. Svarsalternativen kommer sedan på formatet alternativ:feedback:True/False. Svarsalternativen skiljs även dem åt med ett semikolon. Litet exempel:

Question1?;
alternativ:feedback:True;
alternativ2:feedback:False;
alternativ3:feedback:False
;;
Question2?;
alternativ:feedback:False;
alternativ2:feedback:True;
alternativ3:feedback:True

Fråga 2 kommer här bli en multiple choice fråga då det finns mer än ett rätt alternativ.
För större exempel se `example_quiz.txt`.
`jsonparser.py` tar en fil som heter `quiz.txt` och genererar `quiz.json`. (Eller editera `jsonparser.py` så den använder andra filnamn.)


### Buggar och problem
Vi har hittat ett par buggar och problem som inte lyckats lösas.

Om ett alternativ i en flervalsfråga innehåller ett `<` slängs texten efter det här tecknet, såvida `<` inte ligger precis i slutet av alternativtexten. Vi tror att det tolkas som början av en html-tag någonstans, men är inte säkra på var/varför. Som en workaround kan man byta ut `<` mot `>`.

Ett problem som dykt upp ibland på vissa datorer är att när man laddar ett quiz så kommer inte frågetexten till alla frågor med. Det saknas text till olika frågor varje gång man laddar quizzet, vi har inte lyckats ta reda på var i koden eller exakt under vilka omständigheter detta uppstår.

## GitHub pages

### Webbläsare
Hemsidan har testats och fungerar bra i följande webbläsare 2020-06-25: Google Chrome, Microsoft Edge, Safari, Firefox, Opera.

### Filstruktur
/\_data innehåller för tillfället endast navigation.yml som styr navigationsmenyn. Om di vill ha fler flikar i menyn så är det navigation.yml som ska ändras.

/\_includes innehåller bilder som används på hemsidan och html moduler för exempelvis navigationbar och footer. Alla moduler bör ligga här.

/\_layouts innehåller alla layouts. För tillfället finns endast default layouten som används på alla sidor.

assets/css/style.css innehåller all css för hemsidan. Filen importar all css från det valda jekyll temat som grund och kan sedan ändras genom att lägga till nya css regler som skriver över temats.

Gemfile används för lokal utveckling av hemsidan (vilket i princip är ett måste då du annars behöver pusha kod för att se dina ändringar).
