# Växthusgasutsläpp per län 

I denna uppgfit kollar vi på koldioxid och metan utsläpp för valfritt län i Sverige. Vi studerar först hur koldioxidutsläppen utsläppen har förändrats under de senare åren, antingen för hela länet eller en specifik kommun. Därefter kollar vi även på metangas utsläpp och gör en omvandling till koldioxidekvivalenter för att lättare kunna jämföra de två gasernas påverkan. I slutet av uppgiften kollar vi på alla länets kommuner samtidigt och analyserar skillnader i deras utsläpp.

Programmeringsmässigt berörs följande koncept: 
  - Tabeller (listor av listor)
  - Hämta data från internet och ladda in i tabeller
  - Indexering i tabeller
  - Plocka ut antingen kolumner eller rader från tabeller. 
  - Slicing av listor.
  - Plotta grafer med hjälp av matplotlib

Följande miljödata berörs:
  - Hur olika kommuners koldioxidutsläpp skiljer sig åt och vad det kan bero på
  - Hur olika kommuners metangas-utsläpp skiljer sig åt och vad det kan bero på
  - Begreppet koldioxidekvivalent och att olika växthusgaser påverkar olika mycket

# Kör uppgiften i Colab 

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lunduniversity/schoolprog-satellite/blob/master/exercises/regional_greenhouse_emissions/UPPG_CO2_ekvivalenter.ipynb)

# Data
All data kommer från SMHI och kan hämtas från: [http://www.airviro.smhi.se/cgi-bin/RUS/apub.html_rusreport.cgi](http://www.airviro.smhi.se/cgi-bin/RUS/apub.html_rusreport.cgi)

# Inspirationsuppgift

Det finns även en inspirationsvariant av uppgiften. I denna kollar vi på växthusgasutsläpp per person i hela sveriges kommuner, och ritar upp på en interaktiv karta. Man kan själv välja färger, år att visa, samt sektor växthusgasutsläppen kommer från.

Programmeringsmässigt berörs följande koncept: 
  - Tilldela värden till variabler
  - Explicit skapa listor
  - Kodexekveringsföljd
  - Visualisera data med färgskalor

Följande miljödata berörs:
  - Hur olika kommuners växthusgas-utsläpp skiljer sig åt och vad det kan bero på
  - Hur växthusgas-utsläpp har förändrats över tid i Sverige
  - Vilka sektorer som står för olika utsläpp i olika kommuner

# Kör inspirationsuppgiften i Colab 

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lunduniversity/schoolprog-satellite/blob/master/exercises/regional_greenhouse_emissions/fargkarta-vaxthusgasutslapp.ipynb)

