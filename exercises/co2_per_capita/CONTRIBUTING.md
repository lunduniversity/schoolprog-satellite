# CO2-utsläpp per capita för utvecklare
De två datafilerna som används är `folkmangd.zip` som finns i uppgiftsmappen och `data.zip` som laddas ned i uppgiften från en annan mapp i repot. För en beskrivning av hur `data.zip` tas fram, se [här](https://github.com/lunduniversity/schoolprog-satellite/blob/master/exercises/co2-utsl%C3%A4pp_sverige/CONTRIBUTING.md).

`folkmangd.zip` är en zippad textfil, där textfilen är direkt nedladdad från SCB:s statistikdatabas under Befolkning/Befolkningsstatistik/Folkmängd/Befolkning efter ålder och kön. År 1860-2018. En länk till sidan finns [här](http://www.statistikdatabasen.scb.se/pxweb/sv/ssd/START__BE__BE0101__BE0101A/BefolkningR1860/). Variablerna som valdes är:

- ålder: total ålder
- kön: inget valdes för att få med allt
- år: 1990-2017

Formatet valdes till Relationstabell som textfil (txt)

