import json
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.lines import Line2D

equal_size = True
use_background = True

with open('../data/raw_real_for_poster.json', 'r') as file:
    data = json.load(file)

# Preprocess data: set signal_strength to -60 for points where x < 0 and y > 0
for point in data:
    if point['x'] < 3 and point['y'] > 3:
        point['signal_strength'] = -91
    if point['x'] < 0 and point['y'] > 3:
        point['signal_strength'] = -100


x = [point['x'] for point in data]
y = [point['y'] for point in data]
signal_strength = [point['signal_strength'] for point in data]

if equal_size:
    sizes = [80] * len(signal_strength)
else:
    sizes = [abs(s + 110) for s in signal_strength]  # Scale sizes based on signal strength

plt.figure(figsize=(8, 6))

if use_background:
    img = mpimg.imread('../data/map_145.jpg')
    plt.imshow(img, extent=[-1.5, 9, -2.5, 5], origin='lower', aspect='auto', alpha=0.45)

# Scatter plot with RdYlGn colormap (Red->Yellow->Green)
scatter = plt.scatter(
    x, y, c=signal_strength, s=sizes, cmap='RdYlGn', alpha=1, edgecolor='gray', linewidths=0.2,
    vmin=-110, vmax=-60  # Red(-110) -> Yellow(-85) -> Green(-60)
)

# Add color bar with clear labels
cbar = plt.colorbar(scatter, label="Signal Strength (dBm)", extend='both')
cbar.ax.set_title("Signal Strength", fontsize=10)

# Create custom legend entries with colors
legend_elements = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label="Weak Signal (-110 to -90 dBm)"),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='yellow', markersize=10, label="Medium Signal (-89 to -70 dBm)"),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='green', markersize=10, label="Strong Signal (-69 to -60 dBm)")
]

# Add the custom legend
plt.legend(handles=legend_elements, loc="lower left", title="Signal Quality Guide")

# Choose random points to display signal strength
# Evenly select three points from the data
indices = [int(len(signal_strength) * i / 2) for i in [0, 1]]
for i in indices:
    if i < len(signal_strength):
        plt.text(
            x[i], y[i], f"{signal_strength[i]:.1f} dBm", fontsize=9, ha='left', va='bottom', color="black"
        )

plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.title("2D Signal Strength Visualization (dBm)")
plt.grid(True, alpha=0.5)
plt.show()
