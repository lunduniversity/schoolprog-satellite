# Våra övningar
[Programmeringsövningar med satellitdata och annan miljödata](https://lunduniversity.github.io/schoolprog-satellite/) för högstadium och gymnasium.

## För utvecklare

* Övningarna kan ses direkt på github på [exercises/README.md](exercises/README.md).

* Webb-siten är gjord med github pages och ligger på https://lunduniversity.github.io/schoolprog-satellite/

* Projektbeskrivning, uppdragsideer, etc. finns på [Google Drive](https://drive.google.com/drive/folders/1svwmHStMxmkm5pGE-U4PO6GWMpGCyXYH)
* Lägg alla (stora) datafiler i följande sido-repo: https://github.com/lunduniversity/schoolprog-satellite-data
* Skapa issues för att dokumentera utvecklingen och ange aktuell issue för varje commit
* Filstruktur för varje uppdrag:
    * en `README.md` som riktar sig till skoleleven
    * en `CONTRIBUTING.md` med information man kan behöva känna till som utvecklare. T.ex. om hur data extraherats från externa källor, och förberetts för användning i uppgiften.
    * små datafiler, t.ex. upp till några kilobyte,
    * script för att extrahera data
    * lösningar
* Filerna `requirements.txt` och `postBuild` är config-filer för [binder](https://gke.mybinder.org/) som används i Väderdata 2.

## License
* Copyright &copy; 2019-2020. Dept. of Computer Science at Lund University, Lund, Sweden.
* Copyright © 2019-2020 ICOS ERIC
* This work is licensed under a
Creative Commons Attribution 4.0 International License ([CC BY 4.0](http://creativecommons.org/licenses/by/4.0/)).
