# Endres Sander - Matr.: 41324

## Beschreibung
Mein Programmabschnitt beschäftigt sich im Allgemeinen mit einigen Zusatzfunktionen, welch bei vielen 
Standard Chatbots integriert sind. Als einfache Inspiration kann hier die Alexa von Amazon genannt werden.

Der erste Abschnitt beschäftigt sich mit einer Idee zur Anzeigen zur Sportnachrichten, welche nachträglich
mit in die Nachrichten Funktion integriert wurde. Bei Bedarf kann diese jedoch noch mit integriert werden.
Grundlegend funktioniert die Anzeige über die Integration der Google API und der Hauptauswahl auf den
Themenbereich Sport. Die gesammelten Daten werden als Liste übergeben und dann jeweils als einzelne
Zeile augegeben.

Der zweite Abschnitt beschäftig sich mit der Anzeige eines einfachen Kalenders, welchen man flexibel
auswählen kann. Der Nutzer übergibt eine Jahreszahl und einen ausgeschriebenen Monat welcher über eine
Indextabelle mit dem Jahr an die calendar Funktion übergeben wird. HIer erfolgt dann die Ausgabe und 
Darstellung des Kalenders.

Der letzte Abschnitt beschäftigt sich mit der Idee einer persistenten Einkaufsliste, welche auch nach
dem Beenden des Programms erhalten bleibt. Hierfür werden Funktionen zum schreiben und speichern von
.txt-Datein verwendet. Dadurch kann die Liste angezeigt erweitert und auch gelöscht werden. Durch eine
Schleife können bis das Beenden vom User gefordert wird Dinge hinzugefügt werden. Eine weitere Funktion
überschreibt die Einkaufsliste und erstellt so eine Neue.

## Quellen
Vorlesungsinhalte
Alexa von Amazon
Sportnachrichten: https://www.geeksforgeeks.org/build-an-application-to-extract-news-from-google-news-feed-using-python/
Einkaufsliste: https://www.python-lernen.de/dateien-auslesen.htm
