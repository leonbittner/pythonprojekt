#Endres Sander
#Matr.: 41324
'''
Dieser Abschnitt beschäftigt sich mit einigen kleinen Nebenfeatures wie ein paar Sport Informationen, einem Kalender
und einer Einkausliste. Um neben Spielen und Informationen auch ein paar andere nützliche Dinge zu haben, wurden hier
noch die Einkaufsliste und ein einfacher Kalender eingefügt. Um eine Einkaufsliste über eine Nutzung hinaus zu
behalten, wird diese in einer zusätzlichen Textdatei abgespeichert.
'''

#pip install gnewsclient

#Import für wichtige genutzte Bibliotheken
from gnewsclient import gnewsclient
import calendar


#Zusätzliche Sportnachrichtenfunktion, da zunächst eine Trennung von Nachrichten und Sport vorgesehen war
#Kann durch einfaches hinzufügen eines Schlüsselworts und eines Aufrufs in der Main hinzugefügt werden
def SportNachrichten():

    #Abfang Funktion für mögliche Verbindungsstörung
    try:
        #News Funktion funktioniert nur mit Englischer Sprach Eingabe
        print("(Input in Englischer Sprache verfassen)")

        #Input für Sprache kann wahlweise angestellt werden
        #Sprache = input("In welcher Sprache willst du Nachrichten sehen?:")
        Sprache = "German"

        #Input für Land
        Land = input("Von wo willst du Nachrichten sehen?:")

        #Themengebiet soll für diese Abfrage auf dem Bereich Sport liegen
        Themengebiet = "Sports"

        #Nachrichten Client importiert anhand Auswahl NAchrichten
        client = gnewsclient.NewsClient(Sprache, Land, Themengebiet, max_results=3)

        #Nachrichten werden als Matrix gespeichert
        news_list = client.get_news()

        #Nachrichten werden in Textform mit Zeilenumbruch gespeichert
        result = (news_list[0]["title"] + "\n" +
                         news_list[0]["link"] + "\n" +
                         news_list[1]["title"] + "\n" +
                         news_list[1]["link"] + "\n" +
                         news_list[2]["title"] + "\n" +
                         news_list[2]["link"])

        #Ausgabe Nachrichten mit Überschrift und Link
        print(result)

    except:

        print("Keine Verbindung möglich!")



#SportNachrichten()

#Kalendar Funktion für eine einfache Kalendar Darstellung
def Kalender():

    #Abfang für falsche Eingaben
    try:
        #Input für Jahr des Kalenders
        Jahr = input("Aus welchem Jahr willst du den Kalender sehen?(Beispiel: '2020')")

        #Input für Monat des Kalenders
        monatInput = input("Und aus welchem Monat willst du den Kalender sehen ?(Beispiel: 'Januar')")

        months = [
            (1, 'Januar'),
            (2, 'Februar'),
            (3, 'März'),
            (4, 'April'),
            (5, 'Mai'),
            (6, 'Juni'),
            (7, 'Juli'),
            (8, 'August'),
            (9, 'September'),
            (10, 'Oktober'),
            (11, 'November'),
            (12, 'Dezember'),
        ]

        monat = 1

        #Auswahl der Nummer des Monats zur Übergabe an die Kalenderfunktion
        for i in range(len(months)):
            if (months[i][1]) == monatInput:
                monat = months[i][0]

        #Ausgabe Kalender
        print(calendar.month(int(Jahr), monat))

    #Rückmeldung für falsche Eingaben
    except:
        print("Falsche Eingabe!")

#Kalender()


#Einkauslistenfunktion zum hinzufügen zur Liste und Anzeigen bereits eingetragener Dinge
def addEL():

    try:
        #Öffnen der Einkaufsliste
        einkaufsliste = open('Einkaufsliste.txt','a')
        print("Was soll auf der Einkaufslsite hinzugefügt werden?")
        print("Schreibe 'OK' wenn du fertig bist.")

        #while Schleife zum hinzufügen mehrerer Dinge
        while True:
            new_item = input("> ")

            #Abbruchfunktion zum Beenden des Hinzufügens
            if new_item == 'OK':
                einkaufsliste.close()
                break

            # Füge Dinge zur Liste hinzu
            einkaufsliste.write(new_item+"\n")

        # Anzeigen der Einkaufsliste
        print("Deine Einkaufsliste:\n")
        einkaufsliste = open('Einkaufsliste.txt', 'r')
        print(einkaufsliste.read())
        einkaufsliste.close()

    #Falls Datei fehlerhaft, wird eine neue Einkaufslsite angelegt
    except:
        print("Fehler mit Einkaufsliste!")
        einkaufsliste = open('Einkaufsliste.txt', 'w')
        print("Neue Einkaufsliste wurde erstellt!")
        einkaufsliste.close()
#addEL()

#Funktion zum Löschen der Liste
def delEL():

    #Zusätzliche Abfrage
    a = input("Einkaufsliste wirklich löschen? Ja/Nein\n> ")

    if a == "Ja":
        einkaufsliste = open('Einkaufsliste.txt', 'w')
        einkaufsliste.close()
        print("Liste wurde gelöscht.")

    elif a == "Nein":
        print("Liste wurde nicht gelöscht.")

    #Für falsche Eingaben
    else:
        print("Keine gültige Eingabe!")

#delEL()