import requests
import pandas as pd
import os
from datetime import datetime
from calendar import monthrange
import json

key = "X4lrW9Ng981W9NslRxwP4NuJa4mIDVu6ydb7jv69"

url_stations = 'https://api.meteo.cat/xema/v1/estacions/metadades'

# Function 1: get_stations_metadata
 
response = requests.get(url_stations, headers={"Content-Type": "application/json", "X-Api-Key": key})

print(f'The response code is: {response.status_code}')
print(f'Content of the response: {response.text}')

if response.status_code == 200:

    stations = response.json()

    print(f"Number of stations: {len(stations)}")
    print(f"First station: {stations[0]}")

    all_dates = []

    for info_station in stations:
        for info_estat in info_station['estats']:
            all_dates.append({
                'station_code': info_station['codi'],
                'station_name': info_station['nom'],
                'start_date': info_estat['dataInici'],
                'end_date': info_estat['dataFi']
            })

    print(f'Status: {all_dates}')

else: 
    print(f"Error: {response.status_code}")

df = pd.DataFrame(all_dates)
df.head()
df.info()

# UTC
df['start_date'] = pd.to_datetime(df['start_date'])
df['end_date'] = pd.to_datetime(df['end_date'])

df.info()

df.loc[(df['start_date'].dt.year == 1999) & (df['end_date'].isna())]

# Function 2: get_weather_metadata
url_variables = 'https://api.meteo.cat/xema/v1/variables/mesurades/metadades'

response = requests.get(url_variables, headers={"Content-Type": "application/json", "X-Api-Key": key})

print(f'The response code is: {response.status_code}')
print(f'Content of the response: {response.text}')

if response.status_code == 200:

    variables = response.json()

    print(f"Number of stations: {len(variables)}")
    print(f"First station: {variables[0]}")

    all_variables = []

    for info_variables in variables:
        all_variables.append({"code":info_variables['codi'], 
                             "name":info_variables['nom'],
                             "unit":info_variables['unitat']})

else: 
    print(f"Error: {response.status_code}")

print(all_variables)

# Function 3: get_weather_info

first_station = df['station_code'].iloc[0]
year = 2000

all_weather_data = []

month = 1  # Enero
days_in_month = monthrange(year, month)[1]

# Iterar por cada día de enero
for day in range(1, days_in_month + 1):
    
    # Construir URL usando el endpoint que quieres
    url = f"https://api.meteo.cat/xema/v1/estacions/mesurades/{first_station}/{year}/{month:02d}/{day:02d}"
    
    print(f"📡 Día {day:02d} - URL: {url}")
    
    # Headers
    headers = {
        "Content-Type": "application/json",
        "X-Api-Key": key
    }
    
    # Hacer petición
    response = requests.get(url, headers=headers)
    print(f"Status: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        
        # Ver estructura de la respuesta
        print(f"Keys en respuesta: {list(data)}")