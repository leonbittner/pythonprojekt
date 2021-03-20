
"""
Index.py erstellt von Mika Selent und Hendrik Schumann

Über die Index ist es mglich, die einzelnen Module zu öffnen.

"""

import re
from Leon import covidzahlen
from Hendrik import TIC_TAC_TOE
from Mika import news
from Bao import wetterfunktion
from Endres import Sport_Kalender_Einkaufen
from Marius import Marius_Pong
status = 1

print("Herzlichen Willkommen zum neuen Chatbot.")
nutzername = input("Wie heißt du denn?\n  ")
print("Cool " + nutzername + ", ich bin Bob,\n Ich habe bisher folgende Funktionalitäten:\n - Aktuelle Covid-19-Zahlen (Länder o. Bundesländer)​ \n - Aktuelle News/Schlagzeilen​ \n - Live Wetter / Wetteraussichten​ \n - Kalenderinformationen​ \n - Ihre Einkaufsliste")
print("Darüber hinaus können wir coole Spiele zusammen spielen, wie \n - Der Arcade-Klassiker Pong​ \n - Das Legendäre TicTacToe")


def funktionsaufruf(eingabe):
    if eingabe == "bye":
        print("Bis zum nächsten Mal, " + nutzername)
        status = 0
        exit()
        return 

    eingabe = eingabe.lower()
    input_filter = (" ".join(re.findall(r"[a-züäöß]*", eingabe))).replace("  ", " ")
    # Die Wörter der Eingabe werden in einer Liste aufgeteilt.
    words = input_filter.split()

    Covid = ["corona", "covid", "corona zahlen", "covid zahlen", "corona daten", "covidzahlen", "coronazahlen"]
    News = ["news", "nachrichten", "schlagzeilen", ]
    Spiel = ["spiel"]
    Spiel1 = ["tic", "tac", "toe", "legendäre", "drei", "tictactoe" ]
    Spiel2 = ["pong"]
    Wetter = ["wetter", "vorhersage"]
    Kalendar = ["kalender", "datum"]
    Einkaufsliste = ["liste", "einkaufsliste"]
    loescheEinkaufsliste = ["loesche"]

    for i in words:
        if i in Covid:
            #Starte CovidModul.
            covidzahlen.main()
        if i in News:
            #Starte NewsModul.
            news.news_main()
        if i in Spiel:
            if input("Tic Tac Toe (Ja/Nein)") == "Ja":
                TicTacToe = TIC_TAC_TOE.HendriksTicTacToe(nutzername)
                TicTacToe.starte_Spiel()
            else:
                TicTacToe.starte_Spiel()
    #------------------------Marius----------------------
        if i in Spiel1:
            #Starte TicTacToeModul. 
            TicTacToe = TIC_TAC_TOE.HendriksTicTacToe(nutzername)
            TicTacToe.starte_Spiel()
        if i in Spiel2:
           Marius_Pong.main
    #------------------------Marius----------------------
        if i in Wetter:
            #Starte NewsModul.
            wetterfunktion.wetteraufruf()
        if i in Kalendar:
            #Starte KalenderModul.
            Sport_Kalender_Einkaufen.Kalender()
        if i in Einkaufsliste:
            #Starte Einkaufslistenmodul hinzufügen/anzeigen
            Sport_Kalender_Einkaufen.addEL()
        if i in loescheEinkaufsliste:
            #Starte Einkaufslistenmodul löschen
            Sport_Kalender_Einkaufen.delEL()
        else:
            print("Das kenne ich leider noch nicht")



eingabe = input("Was möchtest du ausprobieren?\n ")
funktionsaufruf(eingabe)

if status == 1:
    eingabe = input("Kann ich dir noch anders helfen?\n Bitte wähle aus meinen Funktionalitäten:\n - Aktuelle Covid-19-Zahlen (Länder o. Bundesländer)​ \n - Aktuelle News/Schlagzeilen​ \n - Live Wetter / Wetteraussichten​ \n - Kalenderinformationen​ \n - Ihre Einkaufsliste \n - Der Arcade-Klassiker Pong​ \n - Das Legendäre TicTacToe \n - Wähle 'bye' zum Beenden. \n")
    funktionsaufruf(eingabe)