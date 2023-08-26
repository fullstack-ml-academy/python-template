''' Aufgabe
Geodaten Heßstraße 49 - Lat: 48.1525736 Long: 11.5632592
WOEID laut Yahoo: 676757, laut flickr 20071093
API Key: 997098cc1bee22e9a0dc3be54cf0b2d7

Aufgabe 1.1:
Finden Sie die “woeid”, sowie den Längen- und Breitengrad “latt_long” Ihres Wohnortes.

Aufgabe 1.2:
Finden Sie die Wettervorhersage der nächsten 5 Tage  für Ihren Wohnort.

Aufgabe 1.3:
Finden Sie die Wettervorhersage für Ihren Wohnort am 08. März 2019.


'''
import datetime
import json
import requests
import pandas as pd
from pathlib import Path

print("Aufgabe 1.2")
api_key = "58151a9aa5fc88d5f418535e2a1523ce"
city = "Muenchen"
lat = 48.1525736
lon = 11.5632592
#weather_url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric&&appid="+ api_key
weather_api = "https://api.openweathermap.org/data/2.5/forecast?lat="+ str(lat) +"&lon=" + str(lon) +"&units=metric&appid=" + api_key
desired_hour = 14

wetter = requests.get(weather_api)
#print("wetter", wetter.content)
data = wetter.json()
#print("Wetter Json = data", data)


#Temperatur aus Daten herauslesen
datum = []
temperatur = []

for entry in data['list']:
    dt_timestamp = entry['dt']
    timestamp_datetime = datetime.datetime.fromtimestamp(dt_timestamp)
    european_datetime = timestamp_datetime.strftime('%d-%m-%Y %H:%M:%S')
    if timestamp_datetime.hour == desired_hour:
        datum.append(european_datetime)
        temperatur.append(entry['main']['temp'])

#Werte zusammensetzen
wetterdaten_df = pd.DataFrame({
    'datum': datum,
    'temperatur': temperatur
})

#print(wetterdaten_df.shape)
#print(wetterdaten_df.columns)
print(wetterdaten_df)



'''forecast for a certain day'''
print("Aufgabe 1.3")
# Define the desired date for filtering
desired_date = '2023-08-26'  # Replace with your desired date

# Convert the desired date to a datetime object
desired_datetime = datetime.datetime.strptime(desired_date, '%Y-%m-%d')
forecast = []



datum_A=[]
temperatur_A=[]

# Filter and print data for the desired date
for entry in data['list']:
    dt_timestamp = entry['dt']
    timestamp_datetime = datetime.datetime.fromtimestamp(dt_timestamp)

    if timestamp_datetime.date() == desired_datetime.date():
        datum_A.append(timestamp_datetime)
        temperatur_A.append(entry['main']['temp'])
        wetter_bestimmter_Tag = pd.DataFrame({
           'datum_A': datum_A,
           'temperatur_A': temperatur_A
           })
print(wetter_bestimmter_Tag)
#print(datum_A)
#print(temperatur_A)
