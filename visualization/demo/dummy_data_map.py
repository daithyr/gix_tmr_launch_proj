import json
import numpy as np

lat_min, lat_max = 47.6101, 47.6131
lon_min, lon_max = -122.2091, -122.2011

lat_resolution = 60
lon_resolution = 40

lat_values = np.linspace(lat_min, lat_max, lat_resolution)
lon_values = np.linspace(lon_min, lon_max, lon_resolution)

lat_grid, lon_grid = np.meshgrid(lat_values, lon_values)
points = np.c_[lat_grid.ravel(), lon_grid.ravel()]

def generate_signal_strength(lat, lon):
    pattern = (np.sin((lat - 47) * 100)* np.cos((lon + 130) * 10) + 1) / 2  
    noise = np.random.uniform(-0.1, 0.1)       
    return max(0, min(1, pattern + noise))         

data = [
    {"latitude": round(lat, 6), "longitude": round(lon, 6), "signal_strength": round(generate_signal_strength(lat, lon), 3)}
    for lat, lon in points
]

with open('../data/raw_map.json', 'w') as f:
    json.dump(data, f, indent=4)
