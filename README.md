# Python Projekt Chatbot

Das vorliegende Projekt wurde von Bao Nguyen, Endres Sander, Marius Meineke, Hendrik Schumann, Mika Selent und Leon Bittner erstellt. Es handelt sich um einen Chatbot, mit welchem größtenteils über die Kommandozeile interagiert wird. Er beeinhaltet die nachfolgenden Funktionen:

- Ausgabe von internationalen Covid-19-Fallzahlen (Leon Bittner)
- Anzeige von Nachrichten aus verschiedenen Kategorien und individuellen Themen (Mika Selent)
- Ausgabe des aktuellen Wetters sowie der Vorhersage für Orte in Deutschland (Bao Nguyen)
- Anzeige eines Monatskalenders sowie einer editierbaren Einkaufsliste (Endes Sander)
- Pong Game mit grafischen Elementen (Marius Meineke)
- Tic-Tac-Toe Game gegen den Computer (Hendrik Schumann)

## Funktionsweise

Die index.py ist für den Funktionsaufruf zuständig, stellt also das Hauptmenü dar. Dafür werden die Eingaben des Users mit simplen if-Bedingungen abgefragt und das entsprechende Pythonprogramm gestartet. Für eine größere Flexibilität wurden Listen mit Synonymen für verschiedene Worte angelegt (z.B. News, Nachrichten, Schlagzeilen).

## Nutzung

Bitte stellen Sie sicher, dass Sie Python Version 3 verwenden und vor der ersten Ausführung die Projektabhängigkeiten installiert haben:


```bash
pip3 install -r "requirements.txt"
```
Der Bot wird über die index.py gestartet. Wenn Sie das Programm mithilfe einer Entwicklungsumgebung starten, dann stellen Sie bitte sicher, dass die Shell auf das Projektverzeichnis zeigt. 
