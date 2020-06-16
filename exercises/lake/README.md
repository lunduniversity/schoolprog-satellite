# Räkna vattendrag i norra Sverige

I denna uppgift studerar vi en satellit bild tagen över norra Sverige. Genom att kolla på hur mycket ljus som reflekteras i de fyra banden blått, grönt, rött och nära infrarött avgör vi vad som är vatten och med hjälp av programmering räknar vi på hur många sjöar som finns i området. 

Programmerinsmässigt berörs följande koncept:
  - Tuplar
  - Listfunktionerna append och pop 
  - while-loopar och for-loopar
  - Funktioner
  - Djupet först sökning

Följande naturorienterandekoncept berörs:
  - Att ljus är uppdelat i olika våglängder och hur vi kan uttnyttja detta
  - NDVI och hur det kan användas för att identifiera vattenmassor

# Kör uppgiften i Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lunduniversity/schoolprog-satellite/blob/master/exercises/lake/Lake.ipynb)

# Data

Satellitbilderna är tagna av Sentinel-2 och är hämtade från [https://scihub.copernicus.eu](https://scihub.copernicus.eu). De har sedan bearbetats för att bli mer lättanvända. De bearbetade filerna finns på följande sido-repo [https://github.com/lunduniversity/schoolprog-satellite-data](https://github.com/lunduniversity/schoolprog-satellite-data/blob/master/lake/lake.npz).
