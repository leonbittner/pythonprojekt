# Python Projekt Chatbot

Das vorliegende Projekt wurde von Bao Nguyen, Endres Sander, Marius Meineke, Hendrik Schumann, Mika Selent und Leon Bittner erstellt. Es handelt sich um einen Chatbot, mit welchem größtenteils über die Kommandozeile interagiert wird. Er beeinhaltet die nachfolgenden Funktionen:

- Ausgabe von internationalen Covid-19-Fallzahlen (Leon Bittner)
- Anzeige von Nachrichten verschiedener Kategorien (Mika Selent)
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
Der Bot wird über die index.py gestartet. 
=======
/********** Marius Meineke (41311) - Pong - Der Arcade Klassiker **********/

/********** Grundidee ***********/

Anfangs hatten wir in der Projektgruppe eine Brainstorming-Session, wo wir sämtliche Ideen für den ChatBot aufgeschrieben haben. 
Dabei habe ich für mich den Arcade Klassiker "Pong" entschieden, weil es mit eins der aller ersten Arcade-Spiele war. 
In der Grundidee habe ich das Spiel ein wenig abgeändert, da der Bot nur alleine genutzt wird und somit eine Mehrspieler-Umsetzung nicht möglich war. 
Aus diesem Grund habe ich es als Einzelspieler-Game programmiert, wo der User versuchen muss den Ball oberhalb seines Schlägers zu halten. 
Generell hat der Spieler drei Leben und seine erzielten Treffer mit dem Schläger werden unten Rechts ausgebenen.

/********** Funktionsweise des Spiels ***********/

Diese aufzurufende Funktion des ChatBots beinhaltet das Spiel Pong, welches aus vielen alten Spielhallen bekannt ist. Es wurde 1972 von Atari als Arcade-Spiel produziert und zum ersten weltweit beliebten Videospiel.
Es entspricht in etwa einem Solo-Pong, bei dem man mit dem Schläger den Ball so lenken soll, dass der Ball nicht am Schläger vorbei geht. 
Wenn der Schläger den Ball verliert, bekommt man einen neuen Ball, verliert man aber insgesamt drei Bälle, so gilt das Spiel als Verloren.
Die Leben werden dabei oben Links in der Ausgabe angezeigt. 
Außerdem kann der Spieler während des Spiel seine Treffer mit dem Schläger einsehen. Diese Treffer werden auf der Score-Anzeige unten Rechts ausgegeben. 
Der Score bezieht sich auf die erzielten Treffer während der ganzen drei Leben.

/********** Inspirationsquellen ***********/

https://www.python-lernen.de/chatbot-programmieren.htm

https://www.python-forum.de/viewtopic.php?t=33094

ww3.school

YouTube

Brainstorming in der Gruppe

/********** Bilder ***********/

Google Bilder

/********** Nutzung ***********/

Bitte stellen Sie sicher, dass Sie Python Version 3 verwenden und vor der ersten Ausführung aus dem Projektverzeichnis die Projektabhängigkeiten installiert haben:
pip3 install -r "requirements.txt"
