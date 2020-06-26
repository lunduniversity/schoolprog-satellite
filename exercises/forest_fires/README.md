# Skogsbränder

I denna uppgift studerar vi satellitbilder tagna över områden som har drabbats hårt av skogsbränder. Vi kollar på skogsbranden i Kårböle som var en av många bränder i Sverige under 2018 och skogsbranden på Kangaroo island som var en av flera bränder som härjade i Australien i årskiftet 2019/2020. Genom att kolla på bilder innan och efter bränderna försöker vi uppskatta hur stor yta som blev drabbad genom att ringa in området med polygoner.

Programmeringsmässigt berörs följande koncept:
  - Plotta bilder utifrån matriser av pixelvärden.
  - Polygoner
  - Små funktioner

Följande naturorienterandekoncept berörs:
  - Att ljus är uppdelat i olika våglängder och hur vi kan uttnyttja detta
  - NDVI och hur det kan användas för att identifiera växtlighet
  - Genom att jämföra NDVI bilder från före och efter kan vi se vilket område som har drabbats av bränderna

# Kör uppgiften i Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lunduniversity/schoolprog-satellite/blob/master/exercises/forest_fires/skogsbrander.ipynb)

# Data

Satellitbilderna är tagna av Sentinel-2 och är hämtade från [https://scihub.copernicus.eu](https://scihub.copernicus.eu). De har sedan bearbetats för att bli mer lättanvända. De bearbetade filerna finns på följande sido-repo [https://github.com/lunduniversity/schoolprog-satellite-data](https://github.com/lunduniversity/schoolprog-satellite-data/blob/master/forest_fires).
