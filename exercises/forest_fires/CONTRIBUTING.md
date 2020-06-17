Filen extract_ndvi.py kan användas för att skapa en .npz fil som innehåller det blåa, gröna , röda och nir banden i form av np-arrayer. 

# Användning

För att köra filen behöver du ha gdal installerat.
Se exempelvis: https://mothergeo-py.readthedocs.io/en/latest/development/how-to/gdal-ubuntu-pkg.htmli

Filen är anpassad för satellitbilder hämtade från https://scihub.copernicus.eu/dhus/#/home med följande inställningar. 


Mission: Sentinel-2
Satellite Platform: blank
Product Type: S2MSI1C

Ladda ner en fil och packa upp den. Du bör då ha en fil med ett filnamn likt följande exempel: S2B_MSIL1C_20200422T103619_N0209_R008_T33VUE_20200422T133128.SAFE

Modifiera extract_ndvi.py och ange pathen till din .SAFE map som dir_name. save_name väljer du själv och filen kommer sparas med detta namn i samma .SAFE map.

red_num kan anges för att "försämra" upplösningen av bilden. Stora bilder kan ta lång tid att jobba med i Google Colab vilket innebär att de bör antingen beskäras eller reduceras till en storlek på maximalt 2000x2000 pixlar (rekommendation baserad på egna experiment, i de flesta fall är en upplösning på 1000x1000 tillräckligt bra för ändamålet vilket kommer göra arbetet i Colab lättare. Större bilder fungerar om de endast ska behandlas enstaka gånger men du kommer då behöva vänta på att Colab jobbar.)

Beskärning av bilder har gjorts i funktionen getband() då vi vill beskära alla band likadant.  
