# Skolprogrammering: miljödata-uppdrag

Välkommen till programmeringens värld!

Här hittar du uppdrag i Python där vi använder öppen "miljö"-data, t.ex. från satelliter och väderstationer för att med programmering undersöka intressanta frågor relaterade till [FNs globala mål](https://www.globalgoals.org). Målet med uppdragen är att du
* lär dig mer programmering och hur man kan göra beräkningar på stora datamängder
* lär dig om olika typer av data, t.ex. mätvärden från satelliter och väderstationer och hur man kan använda dem för att förstå vad som händer i vår miljö

Vi hoppas du tycker uppdragen är roliga och intressanta, och får en insikt i hur programmering kan användas för att utforska olika frågor.

## Vad behöver du kunna?

Om du ska göra uppdragen på egen hand (utan handledning av en lärare), så behöver du kunna enkel programmering i Python med variabler, tilldelningssatser, for-loopar, if-satser, funktioner, och listor. Titta [här](prerequisites.md) för att se om du har lagom förkunskaper.

## Våra uppdrag

Följande uppdrag är tänkta att användas för skolelever i högstadiet och på gymnasiet. De använder repl.it som Python-plattform.

|Uppdrag|Miljödata|Programmering|
|-------|-----------|--------------|
|[Väderdata A](weatherdata/Weatherdata_A_replit.md)|Vi undersöker temperaturdata från SMHI|grundläggande om listor, grundläggande om plottning, filer|
|Väderdata B (TBA)|...|...|
|[Keelingkurvan A](co2/Keeling_A_replit.md)|Vi undersöker koldioxid-data från Hawaii|splitta sträng, läsa in textrader från fil, göra om till kolumnlistor av decimaltal, plotta kurvor|
|Keelingkurvan B (TBA)|...|grundläggande om dictionaries|

## Inspirationsuppdrag

Följande uppdrag kan användas som inspiration. En del av dem täcker samma områden som ovan, men de går betydligt snabbare fram, och programmeringen kan vara lite svår att hänga med på för nybörjare. Men det finns lösningar i uppgifterna, så du kan försöka dig på dem också. En del av dem kan köras i vanlig Python-miljö, som repl.it. En del körs som s.k. Jupyter notebooks, med antingen Google Colab eller Binder.

|Uppdrag|Beskrivning|Python-begrepp|Google Colab/Binder|
|-------|-----------|--------------|------------|
|[Väderdata](weatherdata/README.md)|Hur har temperaturen förändrats de senaste 50 åren? Vi undersöker data från SMHI|filer, matplotlib|[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/open?id=1aMR-_LyHoG2C3DWY_y6_u_1CXlq7_MR8)|
|[Väderdata 2](weatherdata2/README.md)|Fortsättning på Väderdata. Vi plottar interaktiva grafer med hjälp av biblioteket Bokeh|filer, bokeh, binder|[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/open?id=1Go3iOSQWsPa2RcHdr_Kz35rcoRVwoMKN) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/lunduniversity/schoolprog-satellite/master?filepath=exercises%2Fweatherdata2%2FWeatherdata_2.ipynb)|
|[Keelingkurvan](co2/README.md)|Undersök hur koldioxidnivån har förändrats sedan 50-talet|filer, matplotlib|[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/open?id=1HDGOcSsCcui3sHJ0NxtcqbiEZdxV7qHZ)|
|[Introduktion NumPy](numpy_intro/README.md)|Introduktion till paketet NumPy. Testar på att skapa och använda arrayer|numpy arrayer|[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/open?id=1ZVFKnbELw_2D8vc1VpC2-ZX9aYNGV6gV)|
|[Torkan](drought/README.md)|Undersök hur torkan sommaren 2018 kan ses från satellit|numpy arrayer, matplotlib|[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/open?id=1sJLN6_QD1VdIORMaONaQpjT7OzYqgdWS)|
|[Torkan 2](drought2/README.md)|Forsättning av Torkan. Vi undersöker fler mått på torka| numpy arrayer, matplotlib|[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/open?id=1zgCiM7sZ9Adu0AhzkXPXNv-iOSp3XsHJ)|
|[CO2-utsläpp i Sverige](co2-utsl%C3%A4pp_sverige/README.md)|Undersök hur utsläppen för olika sektorer i Sverige ser ut med hjälp av ett stapeldiagram|filer, matplotlib, numpy|[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/open?id=1O0jo_UZKRtsbmUEFk1eIho8L99KKCbPe)|
|[CO2-utsläpp per capita](co2_per_capita/README.md)|Undersök hur utsläppen per capita har förändrats i Sverige sen 1990.|filer, matplotlib, numpy|[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/open?id=1BmQIeymoANIO5zaSS9nVCJiVcwhTSLN1)|

## Programmeringsplattform

Vi använder online-plattformar för Python som repl.it och google colab, så du behöver inte installera något på din dator.
