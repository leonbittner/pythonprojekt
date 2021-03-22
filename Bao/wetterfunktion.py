
#!/usr/bin/env python
import requests
import json
import re
import pandas as pd

def wetteraufruf(): 
        
        abfrage=input("\nWähl Temperatur, Wetter oder die Vorhersage für die nächsten Tage aus und den Ort: ")
        abfrage=abfrage.lower()
        
        #mithilfe der Stadteingabe und der Art der Wetterabfrage, wird die genaue url bestimmt
        def urlfilter(abfrage, forecast):
            api_key = "c1748d6d84202a02706599d37ebc497b"
            vorhersage=forecast
            frage=abfrage.split()
            
            a=0
            while a<len(frage):
                stadt=frage[a].capitalize()
                url = f"https://api.openweathermap.org/data/2.5/{vorhersage}?q={stadt},DE&appid={api_key}&units=metric"
                response = requests.get(url)
                x= response.json()


                if x["cod"]!="404" and frage[a]!="wetter":
                    a=len(frage)+1
                    
                    

                else:
                    stadt="Hannover"
                    url = f"https://api.openweathermap.org/data/2.5/{vorhersage}?q={stadt},DE&appid={api_key}&units=metric"
                    response = requests.get(url)
                    x= response.json()
                a=a+1
            
            return x


        # weitere Abfrage ob die Wetterabfrage wiederholt werden soll
        def nachfrage():
            frage=input('\nWillst du weitere Wetterdaten:')
            frage.lower()

            if frage=="ja":
                wetteraufruf()
            elif frage=="nein":
                print ("Tschüss")
            else:
                print('\nAntworte bitte mit ja oder nein')
                nachfrage()

        #Auswahl der Ausführung, je nachdem ob 'Temperatur', 'Wetter', oder 'Vorhersage' eingegeben worden ist
        if (abfrage.find("temperatur")>-1):
            x=urlfilter(abfrage, "weather")
            y=x["main"]
            temperatur=y["temp"]
            wahrnehmung=y["feels_like"]

            print (f"\nEs ist gerade {temperatur} Grad, aber gefühlt nur {wahrnehmung} Grad.")

            
        
        elif (abfrage.find("wetter")>-1):
            x=urlfilter(abfrage, "weather")
            y=x["main"]

            #Aufbereitung der Winddaten mit der Anzeige der dazugehörigen Kategorie
            speed=x["wind"]["speed"]
            wind = pd.DataFrame({'speed': [speed]})
            binInterval=[0.2, 1.5, 3.3, 5.4,7.9, 10.7, 13.8,17.1, 20.7,24.4, 27.0]
            binLabels=["Windstille", "leiser Zug", "leichte Brise", "schwache Brise", "Mäßige Brise", "frische Brise", "starker Wind", "steifer Wind", "stürmischer Wind","Sturm"]
            wind['range'] = pd.cut(wind.speed, bins=binInterval, labels=binLabels, right=False)
            wind = wind.iloc[0]["range"]

            # Aufbereitung der Wetterbeschreibung
            wetter=x["weather"][0]["description"]
            wettermain=x["weather"][0]["main"]

            print (f"\nEs gibt hauptsächlich {wettermain}, genauer gesagt {wetter}.\nWind: {wind}")

        elif (abfrage.find("vorhersage")>-1):
            x=urlfilter(abfrage, "forecast")

            # Aufbereitung der Jsonmodule in der Tabellenform in pandas
            table_data = pd.json_normalize(x, record_path =['list'])[['dt_txt', 'main.temp_min', 'main.temp_max']]
            multiple_level_data = pd.json_normalize(x, record_path =['list',"weather"])[["main","description"]]
            data = pd.concat([table_data, multiple_level_data], axis=1)
            data = data.rename(columns={'dt_txt': 'Zeitraum', 'main.temp_min': 'Mindesttemperatur', 'main.temp_max':'Maximaltemperatur', 'main':'Überwiegend', 'description':'Beschreibung'})

            print (data)
            
        else:
            print ("\nGib bitte ein, ob du 'Temperatur', 'Wetter' oder die 'Vorhersage' der nächsten Tage angezeigt bekommen möchtest.")
            wetteraufruf()

        nachfrage()
    

