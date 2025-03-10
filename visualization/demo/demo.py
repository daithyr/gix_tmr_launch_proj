import json
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

equal_size = True
use_background = True

with open('../data/raw_real.json', 'r') as file:
    data = json.load(file)

x = [point['x'] for point in data]
y = [point['y'] for point in data]
signal_strength = [point['signal_strength'] for point in data]

if equal_size:
    sizes = [50] * len(signal_strength)
else:
    sizes = [s * 200 for s in signal_strength]

plt.figure(figsize=(8, 6))

if use_background:
    img = mpimg.imread('../data/map.jpg')
    plt.imshow(img, extent=[-1, 8, -2, 5], origin='lower', aspect='auto', alpha=0.8)

# if use_background:
#     img = mpimg.imread('../data/map_145.jpg')
#     plt.imshow(img, extent=[-1, 8, -2, 5], origin='lower', aspect='auto', alpha=0.5)

# scatter = plt.scatter(x, y, c=signal_strength, s=sizes, cmap='viridis', alpha=0.8)
scatter = plt.scatter(x, y, c=signal_strength, s=sizes, cmap='viridis', vmin=0, vmax=1)
plt.colorbar(scatter, label="Signal Strength")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.title("2D Signal Strength Visualization")
plt.grid(True, alpha=0.5)
plt.show()
