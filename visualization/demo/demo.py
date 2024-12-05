import json
import matplotlib.pyplot as plt


with open('../data/raw.json', 'r') as file:
    data = json.load(file)


x = [point['x'] for point in data]
y = [point['y'] for point in data]
signal_strength = [point['signal_strength'] for point in data]


plt.figure(figsize=(8, 6))
scatter = plt.scatter(x, y, c=signal_strength, s=[s * 200 for s in signal_strength], cmap='viridis', alpha=0.8)
plt.colorbar(scatter, label="Signal Strength")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.title("2D Signal Strength Visualization")
plt.grid(True)
plt.show()
