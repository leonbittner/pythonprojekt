# Wetterfunktion des Chatbots:

## Funktion

In dieser Funktion des Chatbots kann die Temperatur, das Wetter oder die Vorhersage der nächsten 5 Tage aus 
Hannover abgefragt werden. Es kann auch eine andere Stadt mit eingegeben werden und die dazugehörige Temperatur, Wetter, Vorhersage
wird wiedergegeben für die genannte Stadt
Beispieleingabe: Kann ich in berlin die temperatur haben. 
Die Daten stammen aus der Schnittstelle der openweathermap API und werden als Jsondatei wiedergegeben.
Die Temperaturabfrage gibt die momentane Temperatur der Stadt aus Deutschland und die gefühlte Temperatur wieder. Das Wetter gibt eine Beschreibung der 
momentanen Wetterlage und die Vorhersage für die nächsten 5 Tage wird in einer Tabelle (pandas) dargestellt in 3h-Schritten mit
dem Zeitraum, Mindesttemperatur, Maximaltemperatur und der Beschreibung des Wetters. Es muss vorerst eine Umwandlung von einer Json in Pandas vorgenommen werden.

## Aufbau

Das Programm erkennt beim Userinput, ob das keyword "wetter", "vorhersage", oder "temperatur" genommen wurde. Falls das nicht der Fall ist, wird
um eine wiederholte Eingabe gebeten. Zusätzlich erkennt das Programm, ob eine gültige Stadt gewählt worden ist. Falls keine zusätzliche Stadt eingegeben worden ist,
dann ist die Defaultstadt Hannover.

Nach der ersten Ausgabe wird im Anschluss gefragt, ob weitere Wetterabfragen vorgenommen werden sollen. Wenn die Frage mit ja beantwortet wird,
wird die Wetterfunktion wieder aufgerufen. Beim nein wird die wetterfunktion beendet.

In der Abfrage 'Willst du weitere Wetterdaten:' kann entweder mit ja oder nein beantwortet werden

## Installation

Voraussetzung für die Ausführung: pip install requests, pip install pandas

## Quellen:
https://openweathermap.org/api
https://www.w3schools.com/python/ref_requests_response.asp



