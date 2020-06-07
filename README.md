# Våra övningar
[Programmeringsövningar med satellitdata och annan miljödata](https://lunduniversity.github.io/schoolprog-satellite/) för högstadium och gymnasium.

# För utvecklare

* **Webb-siten** är gjord med github pages och ligger på https://lunduniversity.github.io/schoolprog-satellite/. Den uppdateras vid varje commit och styrs av filerna `_config.yml` och `index.md`.

* **Övningarna** ligger i katalogen `exercises` med en underkatalog per övning. Filstruktur för varje övning:
    * en `README.md` eller annan md-fil som riktar sig till skoleleven
    * en `CONTRIBUTING.md` med information man kan behöva känna till som utvecklare. T.ex. om hur data extraherats från externa källor, och förberetts för användning i uppgiften.
    * små datafiler, t.ex. upp till några kilobyte,
    * script för att extrahera data
    * lösningar

* **Huvudsidor** med länkar till övningarna:
    * [exercises/README.md](exercises/README.md) länkar till de övningar som syns på webben.
    * [exercises/PROTOTYP.md](exercises/PROTOTYP.md) länkar till prototypövningar utvecklade under 2019 som ännu inte är bearbetade för att synas på webben.
    * [exercises/JUNE2020.md](exercises/JUNE2020.md) länkar till nya övningar som utvecklas under juni 2020.

* **Övrig info**
    * Projektbeskrivning, uppdragsideer, etc. finns på [Google Drive](https://drive.google.com/drive/folders/1svwmHStMxmkm5pGE-U4PO6GWMpGCyXYH)
    * Lägg alla (stora) datafiler i följande sido-repo: https://github.com/lunduniversity/schoolprog-satellite-data
    * Skapa issues för att dokumentera utvecklingen och ange aktuell issue för varje commit
    * Filerna `requirements.txt` och `postBuild` är config-filer för [binder](https://gke.mybinder.org/) som används i Väderdata 2.

# License
* Copyright &copy; 2019-2020. Dept. of Computer Science at Lund University, Lund, Sweden.
* Copyright © 2019-2020 ICOS ERIC
* This work is licensed under a
Creative Commons Attribution 4.0 International License ([CC BY 4.0](http://creativecommons.org/licenses/by/4.0/)).
