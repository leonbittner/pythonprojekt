# Hendrik Schumann (41325) - Tic-Tac-Toe 

## Grundidee:

Tic-Tac-Toe oder Drei gewinnt (auch Kreis und Kreuz, Dodelschach) ist ein klassisches, 
einfaches Zweipersonen-Strategiespiel, dessen Geschichte sich bis ins 12. Jahrhundert v. Chr. zurückverfolgen lässt.
Auf einem quadratischen, 3×3 Felder großen Spielfeld setzen die beiden Spieler abwechselnd ihr Zeichen (ein Spieler Kreuze, der andere Kreise) 
in ein freies Feld. Der Spieler, der als Erster drei Zeichen in eine Zeile, 
Spalte oder Diagonale setzen kann, gewinnt. Wenn allerdings beide Spieler optimal spielen, kann keiner gewinnen, 
und es kommt zu einem Unentschieden. Das heißt, alle neun Felder sind gefüllt, ohne dass ein Spieler die erforderlichen Zeichen in einer Reihe, 
Spalte oder Diagonalen setzen konnte. (Quelle: Wikipedia)

## Konzeption des Spiels 

Diese Klasse bietet die Möglichkeit, dass Spiel TicTacToe zu gegen den Chatbot zuspielen. Nachdem das Objekt erzeugt wurde(Übergabeparameter: Nutzername), kann das Spiel mit der Funktion  starteSpiel() begonnen werden. 
Es wurde darauf geachtet, alles in einzelene Funktionen  abzubilden, um die modularität zu gewährleisten und ggf. Weitere Entwicklungen einfach vorzunehmen.
Nachdem der Spieler einen validen Spielzug gespielt hat, wird überprüft, ob ein Spieler gewonnen hat, danach wird die Funktion für den Zug der KI aufgerufen. Zwischen den Spielzügen wird immer das Spielfeld ausgegeben.
Wenn ein Spieler gewonnen hat, wird seine benötigte Zeit ausgegeben und das Ergebniss in eine CSV Datei gespeichert. Danach werden alle Spielergebnisse in einem Balkemdiagram ausgegeben.

## Weitere Informationen zu Verwendung

Bitte stellen Sie sicher, dass Sie Python Version 3 verwenden und vor der ersten Ausführung aus dem Projektverzeichnis die Projektabhängigkeiten installiert haben:

pip3 install -r "requirements.txt"



