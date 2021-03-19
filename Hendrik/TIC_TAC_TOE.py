'''
Hendrik Schumann

Diese Klasse bietet die Möglichkeit, dass Spiel TicTacToe zu spielen. Nachdem das Objekt erzeugt wurde(Übergabeparameter: Nutzername), kann das Spiel mit der Funktion  starteSpiel begeonnen werden. 
Es wurde darauf geachtet, alles in einzelene Funktionen  abzubilden.

Tic-Tac-Toe oder Drei gewinnt (auch Kreis und Kreuz, Dodelschach) ist ein klassisches, 
einfaches Zweipersonen-Strategiespiel, dessen Geschichte sich bis ins 12. Jahrhundert v. Chr. zurückverfolgen lässt.
Auf einem quadratischen, 3×3 Felder großen Spielfeld setzen die beiden Spieler abwechselnd ihr Zeichen (ein Spieler Kreuze, der andere Kreise) 
in ein freies Feld. Der Spieler, der als Erster drei Zeichen in eine Zeile, 
Spalte oder Diagonale setzen kann, gewinnt. Wenn allerdings beide Spieler optimal spielen, kann keiner gewinnen, 
und es kommt zu einem Unentschieden. Das heißt, alle neun Felder sind gefüllt, ohne dass ein Spieler die erforderlichen Zeichen in einer Reihe, 
Spalte oder Diagonalen setzen konnte.

Requirements: pip install mathplotlib

'''

import time
import random
import csv
import matplotlib.pyplot as plt

#Klasse, über welche das Spiel initialisiert wurde.
class HendriksTicTacToe():
    def __init__(self, name):
        #Initialisierung des Spielfeldes.
        self.feld = ["0","1","2","3","4","5","6","7","8"]
        self.spielername = name
        self.status = 1
        self.Startzeit = time.time()
        pass

    #Mit dieser Methode wird das Tic Tac Toe Feld ausgegeben.
    def spielfeld_ausgeben(self):
        feld = self.feld
        print (feld[0] + "|" + feld[1] + "|" + feld[2] )
        print (feld[3] + "|" + feld[4] + "|" + feld[5] )
        print (feld[6] + "|" + feld[7] + "|" + feld[8] )
        pass

    #Diese Methode Startet den nächsten Spielzyklus.
    def starte_Spiel(self):
        #Überprüfung, ob das Spiel noch läuft.
        if self.status == 0:
            return
        #Überprüfung ob es sich um die erste Spielrunde handelt, wenn ja, wird dier User begrüßt.
        if self.status == 1:
            print("Herzlich Willkommen bei TIC TAC TOE, " + self.spielername)
            print("Du bist X. Bei jeder Eingabe kannst du das Spiel mit 'e' beenden")
            time.sleep(1)
            #Status wird auf 2 gesetzt, dies bedeutet, dass das Spiel nun läuft und es sich um eine Folgerunte handelt.
            self.status = 2
        self.spielfeld_ausgeben()
        #Abfrage nach dem nächsten Spielzug.
        spielzug = input("Bitte Feld eingeben: ")
        #Durch drücken von e kann der Spieler das SPiel verlassen.
        if spielzug == "e":
            return
        #Überprüfung, ob es sich um einen Integer handelt.
        try:
            spielzug = int(spielzug)
        except ValueError:
            print("Es muss eine Zahl zwischen 1 und 9 eingegeben werden, um ein Spielzug zu machen.")
            self.starte_Spiel()
        else:
            #Überprüfung, ob der Wert im Bereich des Spielfeldes liegt.
            if spielzug >= 0 and spielzug < 10:
                #Überprüfung, ob das Spielfeld bereits belegt ist.
                if self.feld[spielzug] == 'X' or self.feld[spielzug] == 'O':
                    print("Das Feld ist bereits belegt, " + self.spielername + " du musst ein anderes Feld auswählen!")     
                    self.starte_Spiel() 
                #Wenn alle Bedingungen erfüllt sind, wird der Spielzug durchgeführt.      
                else:
                    self.feld[spielzug] = 'X'
                    #Es wird überprüft, ob der Nutzer gewonnen hat, wenn nicht, darf die "KI" einen Spielzug durchführen.
                    self.kontrolle_gewonnen()
                    self.KI_spielzug()      
            else:
                print("Die Zahl muss zwischen 1 und 9 liegen!")
                self.starte_Spiel()
    #Mit dieser Funktion führt der Computer seinen Spielzug durch.
    def KI_spielzug(self):
        if self.status == 0:
            return
        print("Jetzt bin ich dran")
        time.sleep(1)
        freiefelder = []
        for freiesfeld in self.feld:
            #Nicht belegte Felder werden in ein extra Array gespeichert, aus welchen die KI eins zufällig wählt.
            if freiesfeld != 'X' and freiesfeld != 'O':
                freiefelder += freiesfeld
        spielzug = int(random.choice(freiefelder))
        self.feld[spielzug] = 'O'
        self.kontrolle_gewonnen()
        #Der nächste Spielzug des Spielers wird gestartet.
        self.starte_Spiel()  

    def kontrolle_gewonnen(self):
        # wenn alle 3 Felder gleich sind, hat der Computer oder der Spieler gewonnen.
        # Kontrolle der Reihen.
        if self.feld[0] == self.feld[1] == self.feld[2]:
            self.gewinner_ausgabe(self.feld[1])
        if self.feld[3] == self.feld[4] == self.feld[5]:
            self.gewinner_ausgabe(self.feld[3])
        if self.feld[6] == self.feld[7] == self.feld[8]:
            self.gewinner_ausgabe(self.feld[7])
        # Kontrolle der Spalten.
        if self.feld[0] == self.feld[3] == self.feld[6]:
            self.gewinner_ausgabe(self.feld[0])
        if self.feld[1] == self.feld[4] == self.feld[7]:
            self.gewinner_ausgabe(self.feld[1])
        if self.feld[2] == self.feld[5] == self.feld[8]:
            self.gewinner_ausgabe(self.feld[2])
        # Kontrolle der Diagonalen.
        if self.feld[0] == self.feld[4] == self.feld[8]:
            self.gewinner_ausgabe(self.feld[0])
        if self.feld[6] == self.feld[4] == self.feld[2]:
            self.gewinner_ausgabe(self.feld[6])
    #Mit dieser Funktion wird der Gewinner ausgegeben.
    def gewinner_ausgabe(self, Spieler):
        print("Ergebnis:")
        self.spielfeld_ausgeben()
        if Spieler == 'X':
            print("Herzlichen Glückwunssch " + self.spielername + " ,diese Runde hast du gewonnen")
        else:
            print("Diese Runde habe ich gewonnen")
        #Zeit des Spiels wird ermittelt.
        endzeit = time.time()
        Spielzeit = endzeit - self.Startzeit
        print("Das Spiel dauerte: ")
        print(Spielzeit)
        #Die Spielzeit wird der CSV Methode übergeben. 
        self.csv_hnadling(Spielzeit)
        #Das Spiel wird als beendet deklariert.
        self.status = 0
        return
    #Diese Funktion schreibt das Ergebniss in eine CSV Datei und liest danach alle Spielergebnisse ein.
    def csv_hnadling(self, spielzeit):
        #Es wird überprüft, ob der tmp Ordner existiert.
        try:
            with open('C:/tmp/test.csv', 'a') as f:
                #f.write(self.spielername)
                f.writelines(self.spielername + ";" + str(spielzeit)  + '\n')
                print("Speichere Ergebnisse")
                f.close()

            with open('C:/tmp/test.csv', 'r') as f:
                print("Lade Highscoreboard")
                read = f.readlines()
                #print(read)
                #Diese Funktion zeigt das Highscoreboard an.
                self.ShowHighscore(read)
        except:
            print("Highscore kann nicht geladen werden")
    #Diese Highscorefunktion zeigt alle vergangenen Spiele in einem extra Highscoreboard an.
    def ShowHighscore(self, values):
        ywerte = []
        xwerte = []
        for element in values:
            print(element)
            datensatz =(element.split(';', 1))
            print(datensatz[0])
            #zeitscore =datensatz[1].split('/', 1)
            zeitscore =datensatz[1]
            zeitscore =zeitscore[:-14]
            xwerte.append(datensatz[0])
            #ywerte.append(zeitscore[0])
            ywerte.append(zeitscore)
        plt.bar(xwerte, ywerte)
        plt.xlabel("Name")
        plt.ylabel("Benötigte Zeit")
        plt.show()
        





