# Chatbot News Mika Selent

Diese Funktion des Bots kann die tagesaktuellen News einer allgemeinen Kategorie oder eines individuellen Themas anzeigen.

## Funktionsweise
Die Daten stammen aus einer Schnittstelle von 'newsapi.org', welche wiederum die Daten von weltweiten Nachrichtenverlagen beziehen.
Zunächst wird dafür die Benutzereingabe mit einem Dictionary der Kategorien abgeglichen. Bei den Kategorien stehen zur Auswahl: Schlagzeilen, Wirtschaft, Unterhaltung, Gesundheit, Wissenschaft, Sport oder Technologie.
Wenn die Benutzereingabe nicht mit einer Kategorie übereinstimmt, wird nach möglichen verfügbaren Artikeln für ein individuelles Thema gesucht.
Die Anfrage an die Schnittstelle erfolgt per HTTP und die Daten werden von der Schnittstelle im JSON-Format beantwortet. Der Key für die Anfrage wird hierbei aus einer externen Text-Datei bezogen.

Ausgegeben werden immer nur die ersten fünf Artikel, sortiert nach Popularität.
Nach erfolgreicher Ausgabe oder auch fehlerhafter Suche, kann eine neue Anfrage getätigt werden.

## Vorraussetzung:
pip install requests, colorama

## Inspiration
https://www.python-lernen.de/chatbot-programmieren.htm

https://newsapi.org/s/germany-news-api

YouTube
