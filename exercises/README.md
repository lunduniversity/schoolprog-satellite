---
layout: default
---
# Programmeringsuppdrag

Uppgifterna kan göras i den ordning de är listade, men det går också bra att ta dem i en annan ordning - se tabellen för vad man behöver kunna för olika uppgifter.

|Uppdrag|Miljödata och innehåll|Programmeringsbegrepp du behöver kunna|Programmeringsbegrepp du lär dig om|Bibliotek som används|
|-------|---------|----------------|-------------|---------------|
|[Väderdata A (repl.it)](weatherdata/Weatherdata_A_replit.md)|Vi plottar temperatur och regnmängder och beräknar medelvärden. |inga förkunskapskrav|listor, plot, loop|matplotlib|
|[Väderdata B (repl.it)](weatherdata/Weatherdata_B_replit.md)|Vi plottar temperaturdata för juli från SMHI (Lund och några andra orter), och jämför olika år. Vi läser in från enkla filer och plottar kurvor.|listor, plot|range, filer, loop, append|matplotlib|
|Kolcykeln[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lunduniversity/schoolprog-satellite/blob/master/exercises/kolcykeln/kolcykeln.ipynb)|Vi undersöker data från forskningsstationen ICOS Hyltemossa i Skåne. Vi lär oss om kolcykeln med källor och sänkor. Vi läser in data från csv-filer, organiserar data i tabeller med index, och plottar data i interaktiva diagram.|inga förkunskapskrav|tabeller, index|pandas, numpy, bokeh|
|[Keelingkurvan A (repl.it)](co2/Keeling_A_replit.md)|Vi undersöker koldioxid-data från Hawaii. Vi läser in från fil med många kolumner och plottar kurvor.|listor, plot, filer|split, float|matplotlib|
|[NumPy A (repl.it)](numpy_intro/numpy_A_replit.md)|Introduktion till paketet NumPy. Vi plottar data som 2D-bilder. |listor, plot| numpy, array, imshow|matplotlib, numpy|
|[Torkan A (repl.it)](drought/README.md)|Vi undersöker hur torkan sommaren 2018 kan ses från satellit (Sentinel). Vi läser in från numpy-filer, beräknar vegetationsindex och plottar 2D med olika färgskalor.|numpy, array, imshow|NpzFile, colormap|matplotlib, numpy|
|Avskogning[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lunduniversity/schoolprog-satellite/blob/master/exercises/avskogning/avskogning.ipynb)|Vi undersöker avskogning i Brasilien med hjälp av satellitbilder (Landsat). Vi plottar vegetationsindex och histogram.|inga förkunskapskrav|plottning, histogram|pandas, numpy, bokeh|
|[CO2 i Sverige A (repl.it)](co2_emission_sweden/co2_A_replit.md)|Vi undersöker statistik från SCB om koldioxidutsläpp i Sverige. Vi läser in från internet och plottar stapeldiagram. |listor, plot| nyckel-värdetabeller, slice, bar| matplotlib, requests|

<!--|Keelingkurvan B (repl.it)(TBA)|...|listor, plot|nyckel-värdetabeller|matplotlib|-->

## Snabbreferenser
Här finns snabbreferenser för Python-konstruktioner:
* [Snabbreferens för grundläggande konstruktioner](https://lunduniversity.github.io/schoolprog/cheatsheet/python/) (variabler, typer, listor, loopar, funktioner, etc.)
* [Snabbreferens för bibliotek vi använder i uppgifterna](snabbreferens.md) (filer, internet requests, numpy, matplotlib)


## Fler uppdrag

Vi utvecklar fler uppdrag efter hand, och vi har [ett antal prototyp-uppdrag](PROTOTYP.md) som ännu inte bearbetats pedagogiskt.
Under juni 2020 skapades även [fler uppdrag](JUNE2020.md), som inte heller är bearbetade än.
