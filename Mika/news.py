# Methode TextLower + Textbereinigung
# Methode proceed() ja-Alternativen
from datetime import date
import time
#import re
import json
import requests
from colorama import init, Fore#, Back

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
    #category_request = (" ".join(re.findall(r"[a-züäöß]*", category_request ))).replace("  ", " ")
    # API-Key wird aus einer Textdatei eingelesen
    api_key = open('api_key.txt', 'r')
    # Hier wird geprüft, ob die eingegebene Kategorie vorhanden ist
    if category_request in category:
        # News aus einer Kategorie werden über die Schnittstelle im JSON-Format geladen
        url = "http://newsapi.org/v2/top-headlines?country=de&" + category[category_request] + "apiKey={}".format(api_key.read())
        response = requests.get(url)
        news_show(json.loads(response.text))
    # Hier wird geprüft, ob zu der individuellen Eingabe News vorhanden sind
    else:
        # News aus individuellem Thema werden über die Schnittstelle im JSON-Format geladen
        url = "https://newsapi.org/v2/everything?q=" + category_request + "&language=de&from=" + str(date.today()) + "&to=" + str(date.today()) + "&sortBy=popularity&apiKey={}".format(api_key.read())
        response = requests.get(url)
        if json.loads(response.text)['totalResults'] != 0:
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
    proceed_request = input("\nMöchten Sie über weitere News informiert werden?\n")
    if proceed_request.lower() == "ja":
        news_get_data(input("\nBitte wählen Sie ein individuelles Thema oder eine Kategorie: Schlagzeilen, Wirtschaft, Unterhaltung, Gesundheit, Wissenschaft, Sport oder Technologie?\n"))
    else:
        print("\nBis zum nächsten Mal!")
        exit()

#news_main()