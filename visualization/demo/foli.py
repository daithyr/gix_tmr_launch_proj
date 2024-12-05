import folium
import json


with open('../data/raw_map.json', 'r') as file:
    data = json.load(file)


center_x = sum([point['latitude'] for point in data]) / len(data)
center_y = sum([point['longitude'] for point in data]) / len(data)


mymap = folium.Map(location=[center_y, center_x], zoom_start=15)


for point in data:
    folium.CircleMarker(
        location=[point['latitude'], point['longitude']],  
        radius=point['signal_strength'] * 10, 
        color='blue',
        fill=True,
        fill_color='blue',
        fill_opacity=0.6
    ).add_to(mymap)


mymap.save('../data/visualization_map_folium.html')
