# Keelingkurvan - för utvecklare

Filen `data.txt` är nerladdad från NOOA på ftp://aftp.cmdl.noaa.gov/products/trends/co2/co2_mm_mlo.txt i juni 2019, och har sparats utan de inledande raderna med metadata och kolumnrubriker. Filen innehåller bara mätvärden för att vara enklare att programmera mot.

Dock har originalet på NOOA strukturerats om under 2020, och har nu andra kolumner och innehåll. Vi har därför tyvärr inte kvar metadata för filen `data.txt`.

Den nya filen på NOOA verkar dessutom använda sig av fler mätstationer än den på Mauna Loa.

I stället är det bättre att använda information från SCRIPPS för att rita Keelingkurvan. Se https://scrippsco2.ucsd.edu. Där finns en fil som motsvarar data.txt, men med lite andra kolumner. Filen finns på https://scrippsco2.ucsd.edu/assets/data/atmospheric/stations/in_situ_co2/monthly/monthly_in_situ_co2_mlo.csv

Filen `monthly_in_situ_co2_mlo.csv` är en cachad version av denna fil, som är nerladdad december 2020. Filen på SCRIPPS uppdateras kontinuerligt. Den cachade filen sparas här så att vi har möjlighet att köra våra uppgifter även om remote-filen i framtiden ändrar struktur.
