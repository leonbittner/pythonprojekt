"""
Leon Bittner

Diese Funktion des Bots kann die tagesaktuellen Covid-19 Fallzahlen verschiedener Regionen anzeigen. Die Daten stammen aus einer frei zugänglichen Schnisttselle der Johns Hopkins University. 

Der Bot kann Daten eines spezifischen deutschen Bundeslandes anzeigen. Dafür wird die Usereingabe mit einer Liste der deutschen Bundesländer abgeglichen. Wenn es einen Treffer gibt, wird eine HTTP Anfrage mit dem Namen des Bundeslandes an die API übermittelt.

Es können auch Nationalstaaten abgefragt werden (hier jedoch nur Gesamtzahlen, keine Regionen bzw. Bundesländer). Dafür wird anstelle des Bundeslandes eine Anfrage mit dem ISO Code des Landes an die Schnittstelle geschickt (z.B. DEU für Deutschland). Um den ISO Code zu ermitteln, wird die Usereingabe mit einer CSV Datei abgeglichen, in welcher der deutsche Name jedes Staates mit dem entsprechenden ISO Code hinterlegt wird.

Die Daten werden von der Schnittstelle im JSON Format beantwortet. Für jeden Tag muss eine einzelne Anfrage gestellt werden, dies ist zwar performance-technisch nicht optimal, allerdings der Architektur der Schnittstelle geschuldet. Um die Daten der letzten 30 Tage anzuzeigen, wird das aktuelle Datum um 30 Tage rückdatiert und mit einer for-Schleife wird in jedem Durchgang ein Tag addiert und eine neue Anfrage erstellt.

Es werden durch die for-Schleife zwei Listen befüllt: "dates" und "fallzahlen". Mithilfe der Bibliothek "termplotlib" werden die Listen in der Kommandozeile geplottet. Außerdem wird die tagesaktuelle Zahl der aktiv Infizierten, genesenen Menschen und der Todesfälle ausgegeben. 

Wichtig: Bitte Python Version 3 zur Ausführung benutzen. Vor dem ersten Ausführen mit pip [bzw. pip3] die Packages "tqdm" sowie "termplotlib" installieren.
"""

import http.client
import json
import datetime
import time
#import termplotlib as tpl
from tqdm import tqdm
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np


dates = []
fallzahlen = []
bundeslaender = [
    "bayern", "niedersachsen", "baden-württemberg", "nordrhein-westfalen",
    "brandenburg", "mecklenburg-vorpommern", "hessen", "sachsen-anhalt",
    "rheinland-pfalz", "sachsen", "thüringen", "schleswig-holstein",
    "saarland", "berlin", "hamburg", "bremen"
]

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
    #Das aktuelle Datum wird um 31 Tage zurückdatiert.
    first_day = datetime.date.today() - datetime.timedelta(days=31)
    #In diesem CSV File werden die ISO-Kennungen der Länder gespeichert. 
    csv_file = csv.reader(open('isocodes.csv', "r"), delimiter=";")
    for i in tqdm(range(31)):
        #Hier wird geprüft, ob die Usereingabe ein Bundesland in Deutschland oder ein Nationalstaat ist.
        if land.lower() in bundeslaender:
            conn.request("GET","/reports?region_province=" + land +"%20&iso=DEU&date=" + str(first_day),headers=headers)
        else:
            for row in csv_file:
              if land.lower() == row[0].lower():
                iso = row[1]         
            try:  
              conn.request("GET","/reports?iso=" + iso + "&date=" + str(first_day),headers=headers)
            except UnboundLocalError:
              print("\nEntschuldigung! Dieses Land kenne ich leider nicht. Bitte verändern Sie die Formulierung oder wählen Sie ein anderes Land. \n")
              proceed()
        res = conn.getresponse()
        data = res.read()
        covdata = json.loads(data)
        #Die Fallzahl für den jeweiligen Tag werden aus der JSON Antwort ausgelesen und in der "fallzahlen" liste gespeichert. Die Zahlen der aktiv Infizierten, Gensenen und Verstorbenen werden in keiner Liste gespeichert. Da diese nur als Text unter dem Graphen für den jeweiligen Tag gespeichert werden. Somit wird hier immer der Wert der letzten Iteration gezeigt. 
        i = 0
        fallzahl = 0
        aktiv_infiziert = 0
        verstorben = 0
        genesen = 0
        while i < len(covdata['data']):
            fallzahl += covdata["data"][i]["confirmed_diff"]
            aktiv_infiziert += covdata["data"][i]["active"]
            genesen += covdata["data"][i]["recovered"]
            verstorben += covdata["data"][i]["deaths"]
            i = i + 1
        fallzahlen.append(fallzahl)
        dates.append(str(first_day))
        #Die Variable "first_day" wird um einen Tag erhöht, damit der nächste Tag in der nächsten Interation abgefragt wird.
        first_day = first_day + one_day 
    #Die Zahl der Neuinfektionen wird geplottet und die restlichen Werte in der Kommandozeile ausgegeben.
    print("\nIn " + land + " gibt es zur Zeit " +
          str(fallzahl) + " Neuinfektionen, " +
          str(aktiv_infiziert) + " aktiv Infizierte, " +
          str(genesen) + " Genesene und " +
          str(verstorben) + " Todesfälle. ")
    print("Quelle: Johns Hopkins University\n\nBitte Grafik schließen, um fortzufahren.")
    showFigures(land)
    #Die Listen werden für die nächste Abfrage zurückgesetzt.
    dates = []
    fallzahlen = []
    proceed()


def proceed():
    weiter = input("Möchten Sie eine weitere Abfrage tätigen?\n")
    if weiter.lower() == "ja":
        getdata(input("Bitte geben Sie das Land für die neue Anfrage ein:\n"))
    else:
        print("Ich wünsche Ihnen einen schönen Tag.")
        exit()


def showFigures(land):
    #Die Listen "dates" und "fallzahlen" werden mithilfe von numpy und matplotlib geplottet.
    x = np.array(dates)
    y = np.array(fallzahlen)
    
    fig, ax = plt.subplots() 
    fig.canvas.set_window_title("Covidzahlen " + land)      
    #Fenstertitel einstellen
    ax.set_title('Neuinfektionen der letzten 30 Tage in ' + land) 
      
    #X- und Y-Achse beschriften
    ax.set_ylabel('Neuinfektionen') 
    ax.set_xlabel('Datum') 
    #Beschriftung der X-Achse einstellen
    fig.autofmt_xdate()
    ax.bar(x, y) 
    ax.xaxis.set_major_locator(plt.MaxNLocator(10))
    plt.show() 

def main():
    print("Guten Tag! Gerne informiere ich Sie über die Covid-19-Lage in Ihrem Land.")
    time.sleep(2)
    getdata(input("Für welches Land soll ich Ihnen die aktuellen Zahlen mitteilen? \nGeben Sie entweder ein Bundesland in Deutschland (z.B. Niedersachsen) oder einen Nationalstaat (z.B. Japan) ein.\n"))


main()

