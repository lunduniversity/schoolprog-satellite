# Skolprogrammering: miljödata-uppdrag

Välkommen till programmeringens värld!

Här hittar du uppdrag i Python där vi använder öppen "miljö"-data, t.ex. från satelliter och väderstationer för att med programmering undersöka intressanta frågor relaterade till [FNs globala mål](https://www.globalgoals.org). Målet med uppdragen är att du
* lär dig mer programmering och hur man kan göra beräkningar på stora datamängder
* lär dig om olika typer av data, t.ex. mätvärden från satelliter och väderstationer och hur man kan använda dem för att förstå vad som händer i vår miljö

Vi hoppas du tycker att uppdragen är roliga och intressanta, och får en insikt i hur programmering kan användas för att utforska olika frågor.

## Vad behöver du kunna?

Om du ska göra uppdragen på egen hand (utan handledning av en lärare), så är det bra om du kan enkel programmering i Python med variabler, tilldelningssatser, for-loopar, if-satser, funktioner, och listor. [Titta här för att se om du har lagom förkunskaper](prerequisites.md). Du kan också prova uppdragen direkt. Lösningsförslag ingår i alla uppgifterna.

Har du handledning så kan du göra uppdragen utan förkunskaper i programmering.

Om du är lärare, eller pedagog på ett Science Center, [se vår lärarhandledning](handledning.md).

## Våra uppdrag

Följande uppdrag är tänkta att användas för skolelever i högstadiet och på gymnasiet. Vi använder online-plattformarna *repl.it* (https://repl.it/languages/python3) och *Google Colab* för programmeringen, så du behöver inte installera något på din dator. För Google Colab behöver du dock ett Google-konto för att kunna köra uppgifterna.

|Uppdrag|Miljödata och innehåll|Du behöver kunna|Du lär dig om|
|-------|---------|----------------|-------------|
|[Väderdata A (repl.it)](weatherdata/Weatherdata_A_replit.md)|Vi plottar temperatur och regn och beräknar medelvärden. |variabler, print|listor, plot, loop|
|[Väderdata B (repl.it)](weatherdata/Weatherdata_B_replit.md)|Vi plottar temperaturdata för juli från SMHI (Lund och några andra orter), och jämför olika år. Vi läser in från enkla filer och plottar kurvor.|listor, plot|range, filer, loop, append|
|Kolcykeln[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lunduniversity/schoolprog-satellite/blob/master/exercises/kolcykeln/kolcykeln.ipynb)|Vi undersöker data från forskningsstationen ICOS Hyltemossa i Skåne. Vi lär oss om kolcykeln med källor och sänkor. Vi läser in data från csv-filer, organiserar data i tabeller med index, och plottar data i interaktiva diagram.|inga förkunskapskrav|tabeller, index|
|[Keelingkurvan A (repl.it)](co2/Keeling_A_replit.md)|Vi undersöker koldioxid-data från Hawaii. Vi läser in från fil med många kolumner och plottar kurvor.|listor, plot, filer|split, float|
|Keelingkurvan B (repl.it)(TBA)|...|listor, plot|nyckel-värdetabeller|
|[CO2 i Sverige A (repl.it)](co2_emission_sweden/co2_A_replit.md)|Vi undersöker statistik från SCB om koldioxidutsläpp i Sverige. Vi läser in från internet och plottar stapeldiagram. |listor, plot| nyckel-värdetabeller, slice, requests, bar|
|[NumPy A (repl.it)](numpy_intro/numpy_A_replit.md)|Introduktion till paketet NumPy. Vi plottar data som 2D-bilder. |listor, plot| numpy, array, imshow|
|[Torkan A (repl.it)](drought/README.md)|Vi undersöker hur torkan sommaren 2018 kan ses från satellit. Vi läser in från numpy-filer och plottar 2D med olika färgskalor.|numpy, array, imshow|NpzFile, colormap|

## Snabbreferenser
Här finns snabbreferenser för Python-konstruktioner:
* [Snabbreferens för grundläggande konstruktioner](https://lunduniversity.github.io/schoolprog/cheatsheet/python/) (variabler, typer, listor, loopar, funktioner, etc.)
* [Snabbreferens för bibliotek vi använder i uppgifterna](snabbreferens.md) (filer, internet requests, numpy, matplotlib)


## Fler uppdrag

Vi utvecklar fler uppdrag efter hand, och vi har [ett antal prototyp-uppdrag](PROTOTYP.md) som ännu inte bearbetats pedagogiskt.
