#Index.py erstellt von Mika Selent, Leon Bittner und Hendrik Schumann


import re
from Leon import covidzahlen
from Hendrik import TIC_TAC_TOE
from Mika import news
from Bao import wetterfunktion
from Endres import Sport_Kalender_Einkaufen
from Marius import Marius_Pong
global status 
status = 1

print("\nHerzlich Willkommen zu unserem Chatbot.")
nutzername = input("Wie heißt du denn?\n  ")
print("Cool " + nutzername + ", ich bin Bob,\n Ich habe bisher folgende Funktionalitäten:\n - Aktuelle Covid-19-Zahlen (Länder o. Bundesländer)​ \n - Aktuelle News/Schlagzeilen​ \n - Live Wetter / Wetteraussichten​ \n - Kalenderinformationen​ \n - Ihre Einkaufsliste (Anzeigen/ Loeschen)")
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
    loescheEinkaufsliste = ["loesche", "loeschen", "lösche", "löschen"]

    for i in words:
        if i in Covid:
            #Starte CovidModul.
            covidzahlen.main(nutzername)
            return
        if i in News:
            #Starte NewsModul.
            news.news_main()
            return
        if i in Spiel:
            if input("Tic Tac Toe (Ja/Nein)").lower() == "ja":
                TicTacToe = TIC_TAC_TOE.HendriksTicTacToe(nutzername)
                TicTacToe.starte_Spiel()
                return
            else:
                TicTacToe.starte_Spiel()
                return
    #------------------------Marius----------------------
        if i in Spiel1:
            #Starte TicTacToeModul. 
            TicTacToe = TIC_TAC_TOE.HendriksTicTacToe(nutzername)
            TicTacToe.starte_Spiel()
            return
        if i in Spiel2:
           Marius_Pong.spielAblauf()
           return
    #------------------------Marius----------------------
        if i in Wetter:
            #Starte NewsModul.
            wetterfunktion.wetteraufruf()
            return
        if i in Kalendar:
            #Starte KalenderModul.
            Sport_Kalender_Einkaufen.Kalender()
            return
        if i in Einkaufsliste:
            #Starte Einkaufslistenmodul hinzufügen/anzeigen
            Sport_Kalender_Einkaufen.addEL()
            return
        if i in loescheEinkaufsliste:
            #Starte Einkaufslistenmodul löschen
            Sport_Kalender_Einkaufen.delEL()
            return
        else:
            print("Das kenne ich leider noch nicht")



eingabe = input("Was möchtest du ausprobieren?\n ")
funktionsaufruf(eingabe)


def main():
    while status == 1:
        eingabe = input("Kann ich dir noch anders helfen?\n Bitte wähle aus meinen Funktionalitäten:\n - Aktuelle Covid-19-Zahlen (Länder o. Bundesländer)​ \n - Aktuelle News/Schlagzeilen​ \n - Live Wetter / Wetteraussichten​ \n - Kalenderinformationen​ \n - Ihre Einkaufsliste (Anzeigen/ Loeschen) \n - Der Arcade-Klassiker Pong​ \n - Das Legendäre TicTacToe \n - Wähle 'bye' zum Beenden. \n")
        funktionsaufruf(eingabe)
        
main()