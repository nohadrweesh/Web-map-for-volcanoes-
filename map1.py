import folium
import pandas as pd

map1=folium.Map([38,-100],zoom_start=6,tiles="Mapbox Bright")

data=pd.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])

fg=folium.FeatureGroup(name="my_map")
for lt,ln,el in zip(lat,lon,elev):
    fg.add_child(folium.Marker(location=[lt,ln],popup=str(el)+" m",icon=folium.Icon("green")))
map1.add_child(fg)
map1.save("map1.html")