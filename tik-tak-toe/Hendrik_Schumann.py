import time
import random
import csv

class HendriksTicTacToe():
    def __init__(self, name):
        self.feld = ["0","1","2","3","4","5","6","7","8"]
        self.spielername = name
        self.status = 1
        self.Startzeit = time.time()
        pass

    def spielfeld_ausgeben(self):
        feld = self.feld
        print (feld[0] + "|" + feld[1] + "|" + feld[2] )
        print (feld[3] + "|" + feld[4] + "|" + feld[5] )
        print (feld[6] + "|" + feld[7] + "|" + feld[8] )
        pass

    def starte_Spiel(self):
        if self.status == 0:
            return
        if self.status == 1:
            print("Herzlich Willkommen bei TIC TAC TOE, " + self.spielername)
            print("Du bist X. Bei jeder Eingabe kannst du das Spiel mit 'e' beenden")
            time.sleep(2)
            self.status = 2
        self.spielfeld_ausgeben()
        spielzug = input("Bitte Feld eingeben: ")
            #Durch drücken von e kann der Spieler das SPiel verlassen
        if spielzug == "e":
            return
        try:
            spielzug = int(spielzug)
        except ValueError:
            print("Es muss eine Zahl zwischen 1 und 9 eingegeben werden, um ein Spielzug zu machen.")
            self.starte_Spiel()
        else:
            if spielzug >= 0 and spielzug < 10:
                if self.feld[spielzug] == 'X' or self.feld[spielzug] == 'O':
                    print("Das Feld ist bereits belegt, " + self.spielername + " du musst ein anderes Feld auswählen!")     
                    self.starte_Spiel()       
                else:
                    self.feld[spielzug] = 'X'
                    self.kontrolle_gewonnen()
                    self.KI_spielzug()      
            else:
                print("Die Zahl muss zwischen 1 und 9 liegen!")
                self.starte_Spiel()

    def KI_spielzug(self):
        if self.status == 0:
            return
        print("Jetzt bin ich dran")
        time.sleep(2)
        freiefelder = []
        for freiesfeld in self.feld:
            if freiesfeld != 'X' and freiesfeld != 'O':
                freiefelder += freiesfeld
        spielzug = int(random.choice(freiefelder))
        self.feld[spielzug] = 'O'
        self.kontrolle_gewonnen()
        self.starte_Spiel()  

    def kontrolle_gewonnen(self):
        # wenn alle 3 Felder gleich sind, hat der entsprechende Spieler gewonnen
        # Kontrolle auf Reihen
        if self.feld[0] == self.feld[1] == self.feld[2]:
            self.gewinner_ausgabe(self.feld[1])
        if self.feld[3] == self.feld[4] == self.feld[5]:
            self.gewinner_ausgabe(self.feld[3])
        if self.feld[6] == self.feld[7] == self.feld[8]:
            self.gewinner_ausgabe(self.feld[7])
        # Kontrolle auf Spalten
        if self.feld[0] == self.feld[3] == self.feld[6]:
            self.gewinner_ausgabe(self.feld[0])
        if self.feld[1] == self.feld[4] == self.feld[7]:
            self.gewinner_ausgabe(self.feld[1])
        if self.feld[2] == self.feld[5] == self.feld[8]:
            self.gewinner_ausgabe(self.feld[2])
        # Kontrolle auf Diagonalen
        if self.feld[0] == self.feld[4] == self.feld[8]:
            self.gewinner_ausgabe(self.feld[0])
        if self.feld[6] == self.feld[4] == self.feld[2]:
            self.gewinner_ausgabe(self.feld[6])

    def gewinner_ausgabe(self, Spieler):
        print("Ergebnis:")
        self.spielfeld_ausgeben()
        if Spieler == 'X':
            print("Herzlichen Glückwunssch " + self.spielername + " ,diese Runde hast du gewonnen")
        else:
            print("Diese Runde habe ich gewonnen")
        endzeit = time.time()
        Spielzeit = endzeit - self.Startzeit
        print("Das Spiel dauerte: ")
        print(Spielzeit)
        self.csv_hnadling(Spielzeit)
        self.status = 0
        return

    def csv_hnadling(self, spielzeit):
        with open('C:/tmp/test.csv', 'a') as f:
            #f.write(self.spielername)
            f.writelines(self.spielername + ";" + str(spielzeit)  + '\n')
            print("Speichere Ergebnisse")
            f.close()

        with open('C:/tmp/test.csv', 'r') as f:
            print("Lade Highscoreboard")
            read = f.readlines()
            #print(read)
            self.ShowHighscore(read)

    def ShowHighscore(self, Values):
        import matplotlib.pyplot as plt
        ywerte = []
        xwerte = []
        for element in Values:
            print(element)
            datensatz =(element.split(';', 1))
            print(datensatz[0])
            #zeitscore =datensatz[1].split('/', 1)
            zeitscore =datensatz[1]
            zeitscore =zeitscore[:-14]
            """
            test = zeitscore[0]
            print(test)
            """
            xwerte.append(datensatz[0])
            #ywerte.append(zeitscore[0])
            ywerte.append(zeitscore)
        plt.bar(xwerte, ywerte)
        plt.xlabel("Name")
        plt.ylabel("Benötigte Zeit")
        plt.show()
        
EinSpiel = HendriksTicTacToe("Hendrik")
EinSpiel.starte_Spiel()




