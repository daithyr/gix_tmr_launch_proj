import folium
import json
from matplotlib import cm, colors


with open('../data/raw_map.json', 'r') as file:
    data = json.load(file)

center_x = sum([point['latitude'] for point in data]) / len(data)
center_y = sum([point['longitude'] for point in data]) / len(data)

mymap = folium.Map(location=[center_y, center_x], zoom_start=15)


colormap = cm.get_cmap('RdYlGn')
norm = colors.Normalize(vmin=0, vmax=1)

for point in data:
    signal_strength = point['signal_strength']
    color = colors.rgb2hex(colormap(norm(signal_strength))) 
    folium.CircleMarker(
        location=[point['latitude'], point['longitude']],
        radius=signal_strength * 10,
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.6
    ).add_to(mymap)

mymap.save('../data/visualization_map_folium.html')
