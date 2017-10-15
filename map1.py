import folium
map1=folium.Map([38,-100],zoom_start=6,tiles="Mapbox Bright")
fg=folium.FeatureGroup(name="my_map")
fg.add_child(folium.Marker(location=[38,-100],popup="My car is here",icon=folium.Icon("green")))
map1.add_child(fg)
map1.save("map1.html")