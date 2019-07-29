# Att hämta data från SMHI

SMHI har öppen data som t.ex. temperaturdata som används i WeatherData-uppgiften. Dokumentationen på SMHI är tyvärr rätt svårbegriplig. Här är därför lite tips.

## Hämta data direkt via en browser
Man kan hämta data direkt med en browser. Först hämtar man alla stationer som har data av ett visst slag (t.ex. temperatur). Detta finns som json-filer. Sedan hämtar man data från en station i taget. Detta finns som csv-filer. Filerna innehåller både meta-data och data.

Exempel:

* Hämta alla stationer som har data av typ "2" (dygnsmedeltemperatur). Browsa till: https://opendata-download-metobs.smhi.se/api/version/latest/parameter/2.json
* Hämta alla dygnsmedeltemperaturer från stationen Lund (). Browsa till: https://opendata-download-metobs.smhi.se/api/version/latest/parameter/2/station/53430/period/corrected-archive/data.csv

`parameter`:

* 2:an i url:erna betyder dygnsmedeltemperatur. Jag har inte hittat någon bra förteckning över vilka parametrar som finns. Men på sidan https://www.smhi.se/data/meteorologi/ladda-ner-meteorologiska-observationer finns en meny där man ser parametrar, och antagligen kommer de i ordning, för dygnsmedeltemperaturen kommer som alternativ 2 där.
* För att verifiera vilken parameter man fick ner kan man titta i csv-filerna på metadatan där.
* Om man vill förstå hur en parameter mäts kan man se i SMHI:s kunskapsbank. T.ex. står det hur dygnsmedeltemperaturen mäts här: https://www.smhi.se/kunskapsbanken/meteorologi/hur-beraknas-medeltemperatur-1.3923

`period`:

* I url:en anges också `period`. Här har vi angett `corrected-archive` vilket såvitt jag förstår betyder att man utfört viss kvalitetskontroll på datan.

## Hämta data via Python:

Det finns lite python-kod som wrappar SMHIs api och som dels filtrerar ut informationen på enklare format och dels cachar nerladdade filer så att man inte behöver hämta samma filer om och om igen när man experimenterar. (Det ingår i SMHIs användarvillkor att man skall undvika att hämta filer i onödan.)

### Wrapper-funktioner i `wrap_smhi_api.py`

* Interna funktionen `__get_raw(url)` hämtar en rådata-fil från SMHI via en URL. Det kan vara en json-fil, csv-fil, eller annan fil.
* Alla rådata-filer cachas i en katalog `cache`. Försöker man hämta samma data igen används cachen i stället.
* `cache`-katalogen är undantagen från git. Se filen `.gitignore`.
* funktionen `get_stations()` hämtar en fil med alla stationer (id och namn) som mäter dygnsmedeltemperatur, och omvandlar till en Python-lista.
* funktionen `get_data(id)` hämtar temperaturdata för en viss station, och returnerar som en sorterad Python-lista med år, månad, dag och temp.

### Test-program `test_smhi_api.py`

Test-programmet använder wrapper-api:et och skriver ut exempel.

* Test-programmet `test_smhi_api.py` laddar ner stations-info och skriver ut stations-id och namn, samt laddar sedan ner temperaturerna för en av stationerna (Lund), och printar ut.
* Observera att vissa datum kan fattas i serierna. T.ex. om mätutrustningen varit ur funktion.
* Provkör med kommandot `python test_smhi_api.py`

Man kan jämföra med rådata-filerna i `cache`-katalogen, t.ex. om man vill titta på meta-informationen för datan.

### Hämta all data med `fetchdata.py`

Det finns ett program `fetchdata.py` som hämtar alla stationsdata. I programmet finns konstanter som anger:
* Vilket startår och slutår som skall användas
* Hur många datapunkter som får saknas i detta intervall.

Data filtreras sedan ut för de stationer som uppfyller dessa villkor. Resultatet blir en utskrift med all data för alla sådana stationer, och är tänkt att pipas till en fil. Formatet är för varje station: en rad med id och namn på stationen, följt av en rad per datapunkt med y, m, d, t. En blankrad mellan stationerna.

* Kör med `python fetchdata.py > result.txt`
* Obs! Det tar en liten stund att köra detta första gången, för det innebär att över 800 stationer laddas ner (och cachas i `cache`-katalogen). Ett mindre antal av stationerna kommer med i output, baserat på villkoren ovan.

### Läs in data som sparats i textfil
Antag att du kört `fetchdata` ovan och sparat resultatet i textfilen result.txt. Du kan då läsa in datan till ett Python dictionary med biblioteket `readdata.py`. Se filen `testread.py` för ett exempel.
