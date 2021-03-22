'''
In dieser Funktion des Chatbots kann die Temperatur, das Wetter oder die Vorhersage der nächsten 5 Tage aus 
Hannover abgefragt werden. Es kann auch eine andere Stadt mit eingegeben werden und die dazugehörige Temperatur, Wetter, Vorhersage
wird wiedergegeben für die genannte Stadt
Beispieleingabe: Kann ich in berlin die temperatur haben. 
Die Temperaturabfrage gibt die momentane Temperatur der Stadt und die gefühlte Temperatur wieder. Das Wetter gibt eine Beschreibung der 
momentanen Wetterlage und die Vorhersage für die nächsten 5 Tage wird in einer Tabelle (pandas) dargestellt in 3h-Schritten mit
dem Zeitraum, Mindesttemperatur, Maximaltemperatur und der Beschreibung des Wetters.
Die Daten stammen aus der Schnittstelle der openweathermap.
In der Abfrage 'Willst du weitere Wetterdaten:' kann entweder mit ja oder nein beantwortet werden
Voraussetzung für die Ausführung: pip install requests, pip install pandas
'''
