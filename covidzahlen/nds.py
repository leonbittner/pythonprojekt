"""
Leon Bittner

Diese Funktion des Bots kann die tagesaktuellen Covid-19 Fallzahlen verschiedener Regionen anzeigen. Die Daten stammen aus einer frei zugänglichen Schnisttselle der Johns Hopkins University. 
Der Bot kann Daten eines spezifischen deutschen Bundeslandes anzeigen. Dafür wird die Usereingabe mit einer Liste der deutschen Bundesländer abgeglichen. Wenn es einen Treffer gibt, wird eine HTTP Anfrage mit dem Namen des Bundeslandes an die API übermittelt.

Es können auch Nationalstaaten abgefragt werden (hier jedoch nur Gesamtzahlen, keine Bundesländer). Dafür wird anstelle des Bundeslandes eine Anfrage mit dem ISO Code des Landes an die Schnittstelle geschickt (z.B. DEU für Deutschland). Um den ISO Code zu ermitteln, wird die Usereingabe mit einer CSV Datei abgeglichen, in welcher der deutsche Name jedes Staates mit dem entsprechenden ISO Code hinterlegt wird.

Die Daten werden von der Schnittstelle im JSON Format beantwortet. Für jeden Tag muss eine einzelne Anfrage gestellt werden. Um die Daten der letzten 30 Tage anzuzeigen, wird das aktuelle Datum um 30 Tage rückdatiert und mit einer for-Schleif wird in jedem Durchgang ein Tag addiert und eine neue Anfrage erstellt.

Es werden durch die for-Schleife zwei Listen befüllt: "dates" und "fallzahlen". Mithilfe der Bibliothek "termplotlib" werden die Listen in der Kommandozeile geplottet. Außerdem wird die tagesaktuelle Zahl der aktiv Infizierten, Genesenen Menschen und der Todesfälle ausgegeben. 

"""

import http.client
import json
import datetime
import time
import termplotlib as tpl
import numpy
from tqdm import tqdm
import csv
import sys

dates = []
fallzahlen = []
bundeslaender =["bayern","niedersachsen","baden-württemberg","nordrhein-westfalen","brandenburg","mecklenburg-vorpommern","hessen","sachsen-anhalt","rheinland-pfalz","sachsen","thüringen","schleswig-holstein","saarland","berlin","hamburg","bremen"]

headers = {
    'x-rapidapi-key': "6bf9bf4f6emshfd176586f689aa9p1055e6jsn0d347582fced",
    'x-rapidapi-host': "covid-19-statistics.p.rapidapi.com"
    }

def getdata(land):
    print(land + "! Eine gute Wahl! Bitte haben Sie einen Moment geduld...\n")
    global dates
    global fallzahlen
    conn = http.client.HTTPSConnection("covid-19-statistics.p.rapidapi.com")
    one_day = datetime.timedelta(days=1)
    first_day = datetime.date.today() - datetime.timedelta(days=31)
    csv_file = csv.reader(open('isocodes.csv', "r"), delimiter=";")
    for row in csv_file:
        if land.lower() == row[0].lower():
            iso = row[1]
        
    for i in tqdm(range(30)):
        #Hier wird geprüft, ub die Usereingabe ein Bundesland in Deutschland oder ein Nationalstaat ist. 
        if land.lower() in bundeslaender:
            conn.request("GET", "/reports?region_province=" + land + "%20&iso=DEU&date=" + str(first_day), headers=headers)
        else:
            conn.request("GET", "/reports?iso="+ iso +"&date=" + str(first_day), headers=headers)
        res = conn.getresponse()
        data = res.read()
        covdata = json.loads(data)
        #Die Fallzahl für den jeweiligen Tag werden aus der JSON Antwort ausgelesen und in der "fallzahlen" liste gespeichert.
        fallzahl = covdata["data"][0]["active"]
        fallzahlen.append(fallzahl)
        dates.append(str(first_day))
        first_day = first_day + one_day
    showFigures()
    print("\nIn " + land + " gibt es zur Zeit " + str(covdata["data"][0]["active"]) + " aktiv Infizierte, " + str(covdata["data"][0]["recovered"]) + " Genesene und "+ str(covdata["data"][0]["deaths"]) + " Todesfälle. ")
    print("Quelle: Johns Hopkins University")
    proceed()
    
def proceed():
    weiter = input("Möchten Sie eine weitere Abfrage tätigen?\n")
    if weiter.lower() == "ja":
        getdata(input("Bitte geben Sie das Land für die neue Anfrage ein:\n"))
    else:
        print("Ich wünsche Ihnen einen schönen Tag.")
        exit()

def showFigures():
    #Die Daten werden in der Kommandozeile geplottet.
    fig = tpl.figure()
    fig.barh(fallzahlen, dates, force_ascii=True)
    print("\nDatum    Gemeldete Fälle")
    fig.show()
    
def main():
    print("Guten Tag! Gerne informiere ich Sie über die Covid-19-Lage in Ihrem land.")
    time.sleep(2)
    getdata(input("Für welches land soll ich Ihnen die aktuellen Zahlen mitteilen? \nGeben Sie Deutschland ein, um einen Bericht für ganz Deutschland zu erhalten.\n"))
    
main()
