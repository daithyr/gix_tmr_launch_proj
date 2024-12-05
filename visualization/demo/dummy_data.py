import json
import numpy as np

X = 60
Y = 40

x_values = np.arange(0, X, 1)
y_values = np.arange(0, Y, 1)

xx, yy = np.meshgrid(x_values, y_values)
points = np.c_[xx.ravel(), yy.ravel()]

def generate_signal_strength(x, y):
    pattern = (np.sin(x / 10) * np.cos(y / 10) + 1) / 2  
    noise = np.random.uniform(-0.05, 0.05)       
    return max(0, min(1, pattern + noise))         


data = [
    {"x": int(x), "y": int(y), "signal_strength": round(generate_signal_strength(x, y), 3)}
    for x, y in points
]

with open('../data/raw.json', 'w') as f:
    json.dump(data, f, indent=4)
