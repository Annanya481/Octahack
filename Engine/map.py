import folium
import pandas as pd
import json
from folium import plugins
from geopy.geocoders import Nominatim
from folium.plugins import HeatMap


df = pd.read_csv('dummie_data.csv')

with open('map.geojson') as f:
    laArea = json.load(f)

laMap = folium.Map(location=[18.516726,73.856255], tiles='Stamen Terrain', zoom_start=10)

laMap=HeatMap(df).add_to(laMap)


folium.GeoJson(laArea).add_to(laMap)

#for i,row in df.iterrows():
#    folium.CircleMarker((row.latitude,row.longitude), radius=3, weight=2, color='red', fill_color='red', fill_opacity=.5).add_to(laMap)


laMap.save('laPointMap.html')

x = pd.read_csv("a.csv")
y = x.Location[0]

locator = Nominatim(user_agent="myGeocoder")
location = locator.geocode(y)
p,q = location.latitude, location.longitude
array = [[p,q]]
x = df.append({'latitude':p, 'longitude':q},ignore_index=True)

for i,row in x.iterrows():
    folium.CircleMarker((row.latitude,row.longitude), radius=3, weight=2, color='red', fill_color='red', fill_opacity=.5).add_to(laMap)

laMap.save('laPointMap.html')
