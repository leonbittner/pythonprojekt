"""
Mika Selent
Matr.: 41326

Diese Funktion des Bots kann die tagesaktuellen News einer allgemeinen Kategorie oder eines individuellen Themas anzeigen.
Die Daten stammen aus einer Schnittstelle von 'newsapi.org', welche wiederum die Daten von weltweiten Nachrichtenverlagen beziehen.
Zunächst wird dafür die Benutzereingabe mit einem Dictionary der Kategorien abgeglichen.
Wenn die Benutzereingabe nicht mit einer Kategorie übereinstimmt, wird nach möglichen verfügbaren Artikeln für ein individuelles Thema gesucht.
Die Anfrage an die Schnittstelle erfolgt per HTTP und die Daten werden von der Schnittstelle im JSON-Format beantwortet.
Ausgegeben werden immer nur die ersten fünf Artikel, sortiert nach Popularität.
Nach erfolgreicher Ausgabe oder auch fehlerhafter Suche, kann eine neue Anfrage getätigt werden.
Vorraussetzung: pip install requests, colorama

"""
from datetime import date
import time
import json
import requests
from colorama import init, Fore

init(autoreset=True)

# Auswahl an verschiedenen Kategorien je nach User-Input
category = {"schlagzeilen": "", "wirtschaft": "category=business&",
                                    "unterhaltung": "category=entertainment&", "gesundheit": "category=health&",
                                    "wissenschaft": "category=science&", "sport": "category=sports&",
                                    "technologie": "category=technology&"}

def news_main():
    print("\nGerne teile ich mit Ihnen die aktuellsten News!\n")
    time.sleep(1)
    news_get_data(input("Bitte wählen Sie ein individuelles Thema oder eine Kategorie: Schlagzeilen, Wirtschaft, Unterhaltung, Gesundheit, Wissenschaft, Sport oder Technologie?\n"))

def news_get_data(category_request):
    # Input ist nicht case-sensitive
    category_request = category_request.lower()
    # API-Key wird aus einer Textdatei eingelesen
    api_key = open('Mika/api_key.txt', 'r')
    # Hier wird geprüft, ob die eingegebene Kategorie vorhanden ist
    if category_request in category:
        # Es wird eine HTTP-Anfrage zur Kategorie an die Schnittstelle gesendet
        url = "http://newsapi.org/v2/top-headlines?country=de&" + category[category_request] + "apiKey={}".format(api_key.read())
        response = requests.get(url)
        # News aus einer Kategorie werden über die Schnittstelle im JSON-Format geladen
        news_show(json.loads(response.text))
    else:
        # Es wird eine HTTP-Anfrage zum individuellen Thema an die Schnittstelle gesendet
        url = "https://newsapi.org/v2/everything?q=" + category_request + "&language=de&from=" + str(date.today()) + "&to=" + str(date.today()) + "&sortBy=popularity&apiKey={}".format(api_key.read())
        response = requests.get(url)
        # Hier wird geprüft, ob zu der individuellen Eingabe News vorhanden sind
        if json.loads(response.text)['totalResults'] != 0:
            # News aus individuellem Thema werden über die Schnittstelle im JSON-Format geladen
            news_show(json.loads(response.text))
        else:
            print("\nDas von Ihnen gewählte Thema oder die Kategorie ist mir nicht bekannt!")
    news_proceed()

def news_show(news):
    # Das Attribut 'count' bestimmt die Anzahl der maximal angezeigten Artikel
    count = 5
    # Die Artikel werden in der Kommandozeile angezeigt
    for i in news['articles']:
        if count > 0:
            print(Fore.RED + "\n-----------------------Titel------------------------")
            print(Fore.WHITE + i['title'])
            description = i['description']
            # Hier wird geprüft, ob eine Beschreibung des Artikels vorhanden ist
            if i['description'] != "":
                if i['description'] is not None:
                    print(Fore.RED + "--------------------Beschreibung--------------------")
                    # Vor einer Länge von 100 Zeichen erfolgt ein Zeilenumbruch
                    if len(description) > 100:
                        cursor = 100
                        while description[cursor] != " ":
                            cursor -= 1
                        description = description[:cursor] + description[cursor].replace(description[cursor],"\n") + description[cursor + 1:]
                        print(Fore.WHITE + description)
                    else:
                        print(Fore.WHITE + description)
            print(Fore.RED + "------------------------Link------------------------")
            print(Fore.BLUE + i['url'], "\n")
            count -= 1

def news_proceed():
    proceed_request = input("\nMöchten Sie über weitere News informiert werden? (Ja/Nein)\n")
    if proceed_request.lower() == "ja":
        news_get_data(input("\nBitte wählen Sie ein individuelles Thema oder eine Kategorie: Schlagzeilen, Wirtschaft, Unterhaltung, Gesundheit, Wissenschaft, Sport oder Technologie?\n"))
    else:
        print("\nBis zum nächsten Mal!")

#news_main()