import folium
import json
from matplotlib import cm, colors

with open('../data/raw_map.json', 'r') as file:
    data = json.load(file)

default_lat = 47.6131
default_lon = -122.2121
zoom_level = 17 

mymap = folium.Map(location=[default_lat, default_lon], zoom_start=zoom_level)


colormap = cm.get_cmap('RdYlGn')
norm = colors.Normalize(vmin=0, vmax=1)

for point in data:
    signal_strength = point['signal_strength']
    color = colors.rgb2hex(colormap(norm(signal_strength))) 
    folium.CircleMarker(
        location=[point['latitude'], point['longitude']],
        radius=5 + signal_strength * 2,
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.6
    ).add_to(mymap)

mymap.save('../data/visualization_map_folium.html')
