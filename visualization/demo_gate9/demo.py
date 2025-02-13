import json
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.lines import Line2D


# Configuration
equal_size = True
use_background = True

# Load data
with open('./data/raw_real_1.json', 'r') as file:
    data = json.load(file)

x = [point['x'] for point in data]
y = [point['y'] for point in data]
signal_strength = [point['signal_strength'] for point in data]

# Point sizes (based on configuration)
if equal_size:
    sizes = [100] * len(signal_strength)
else:
    sizes = [abs(s + 110) for s in signal_strength]  # Scale sizes based on signal strength

# Plot configuration
plt.figure(figsize=(8, 8))

# Background image with transparency
if use_background:
    from scipy.ndimage import rotate  # Add rotation function import
    img = mpimg.imread('./data/map.jpg')
    img = rotate(img, 10, reshape=True, mode='constant', cval=255) 
    plt.imshow(img, extent=[-4, 11, -2, 13], origin='upper', aspect='auto')

# Save rotated image
# plt.imsave('./data/map_rotate.jpg', img)


# Scatter plot with RdYlGn colormap (Red->Yellow->Green)
scatter = plt.scatter(
    x, y, c=signal_strength, s=sizes, cmap='RdYlGn', alpha=1, edgecolor='gray',
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
plt.legend(handles=legend_elements, loc="lower right", title="Signal Quality Guide")

# Choose random points to display signal strength
for i in [24, 120, 150, 180, 200, 220, 250]:
    plt.text(
        x[i], y[i], f"{signal_strength[i]:.1f} dBm", fontsize=9, ha='center', va='center', color="black"
    )

# Labels and Title
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.title("2D Signal Strength Visualization (dBm)")

# Show plot
plt.show()
