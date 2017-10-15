import folium
import pandas as pd
def color_producer(elevation):
    if elevation<1000:
        return "green"
    elif elevation<3000:
        return "orange"
    else:
        return 'red'

map1=folium.Map([38,-100],zoom_start=6,tiles="Mapbox Bright")

data=pd.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])

fg=folium.FeatureGroup(name="Volcanoes")
for lt,ln,el in zip(lat,lon,elev):
    fg.add_child(folium.Marker(location=[lt,ln],popup=str(el)+" m",icon=folium.Icon(color_producer(el))))
    #fg.add_child(folium.CircleMarker(location[lt,ln],popup=str(el)+"m",fill=True,radius=6,color='grey',fill_opacity=0.7,fill_color=(color_producer(el))))
                 
#fg.add_child(folium.GeoJson(data=open('world.json', 'r' ,encoding='utf-8-sig')))           
map1.add_child(fg)
map1.add_child(folium.LayerControl())
map1.save("map1.html")