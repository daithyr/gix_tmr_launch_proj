from gmplot import gmplot
import json


with open('../data/raw_map.json', 'r') as file:
    data = json.load(file)


latitude_list = [point['y'] for point in data]
longitude_list = [point['x'] for point in data]


gmap = gmplot.GoogleMapPlotter(latitude_list[0], longitude_list[0], 15, apikey="YOUR_GOOGLE_MAPS_API_KEY")


for lat, lon, strength in zip(latitude_list, longitude_list, [point['signal_strength'] for point in data]):
    gmap.circle(lat, lon, radius=strength * 10, color="blue", face_alpha=0.6)


gmap.draw("../data/visualization_map_google.html")
