import urllib.request
import json 

URL = "https://data.geo.admin.ch/ch.meteoschweiz.messwerte-wind-boeenspitze-kmh-10min/ch.meteoschweiz.messwerte-wind-boeenspitze-kmh-10min_en.json"

f = urllib.request.urlopen(URL)
data = json.load(f)

# Gesucht 1: Grösste gemessene Windböe
print(max([ point['properties']['value'] for point in data['features'] ]))

# Gesucht 2: Durchschnitt aller gemessen Windböen
print(sum([ point['properties']['value'] for point in data['features'] ]) / len(data['features']), 'km/h')

# Gesucht 3: Anzahl Messwerte
print(len(data['features']))
