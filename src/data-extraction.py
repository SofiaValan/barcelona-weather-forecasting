import requests
import pandas as pd
import os
from datetime import datetime
import json

key = "X4lrW9Ng981W9NslRxwP4NuJa4mIDVu6ydb7jv69"

url_stations = 'https://api.meteo.cat/xema/v1/estacions/metadades'

# Extraction cities 
# url_cities = 'https://api.meteo.cat/referencia/v1/municipis'
# response = requests.get(url_cities, headers={"Content-Type": "application/json", "X-Api-Key": key})
 
# Extraction stations
response = requests.get(url_stations, headers={"Content-Type": "application/json", "X-Api-Key": key})

print(f'The response code is: {response.status_code}')
print(f'Content of the response: {response.text}')

if response.status_code == 200:

    # Convert response to JSON
    stations = response.json()

    print(f"Number of stations: {len(stations)}")
    print(f"First station: {stations[0]}")

    all_dates = []

    for info_station in stations:
        for info_estat in info_station['estats']:
            all_dates.append({
                'station_code': info_station['codi'],
                'station_name': info_station['nom'],
                'dataInici': info_estat['dataInici'],
                'dataFi': info_estat['dataFi']
            })

    print(f'Status: {all_dates}')

else: 
    print(f"❌ Error: {response.status_code}")

df = pd.DataFrame(all_dates)
df.head()