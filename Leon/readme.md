# Covid-Bot

Diese Funktion des Bots kann die tagesaktuellen Covid-19 Fallzahlen verschiedener Regionen anzeigen. Die Daten stammen aus einer frei zugänglichen Schnisttselle der Johns Hopkins University. 

## Funktionsweise

Der Bot kann Daten eines spezifischen deutschen Bundeslandes anzeigen. Dafür wird die Usereingabe mit einer Liste der deutschen Bundesländer abgeglichen. Wenn es einen Treffer gibt, wird eine HTTP Anfrage mit dem Namen des Bundeslandes an die API übermittelt.

Es können auch Nationalstaaten abgefragt werden (hier jedoch nur Gesamtzahlen, keine Regionen bzw. Bundesländer). Dafür wird anstelle des Bundeslandes eine Anfrage mit dem ISO Code des Landes an die Schnittstelle geschickt (z.B. DEU für Deutschland). Um den ISO Code zu ermitteln, wird die Usereingabe mit einer CSV Datei abgeglichen, in welcher der deutsche Name jedes Staates mit dem entsprechenden ISO Code hinterlegt wird.

Die Daten werden von der Schnittstelle im JSON Format beantwortet. Für jeden Tag muss eine einzelne Anfrage gestellt werden, dies ist zwar performance-technisch nicht optimal, allerdings der Architektur der Schnittstelle geschuldet. Um die Daten der letzten 30 Tage anzuzeigen, wird das aktuelle Datum um 30 Tage rückdatiert und mit einer for-Schleife wird in jedem Durchgang ein Tag addiert und eine neue Anfrage erstellt.

Es werden durch die for-Schleife zwei Listen befüllt: "dates" und "fallzahlen". Mithilfe der Bibliothek "termplotlib" werden die Listen in der Kommandozeile geplottet. Außerdem wird die tagesaktuelle Zahl der aktiv Infizierten, genesenen Menschen und der Todesfälle ausgegeben. 

## Daten

Die Rohdaten können [hier](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports) eingesehen werden.
## Nutzung

Bitte stellen Sie sicher, dass Sie Python Version 3 verwenden und vor der ersten Ausführung aus dem Projektverzeichnis die Projektabhängigkeiten installiert haben:


```bash
pip3 install -r "requirements.txt"
```
