import json
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.lines import Line2D


# Configuration
equal_size = True
use_background = True

# Load data
with open('../data/raw_fake_prototype.json', 'r') as file:
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
plt.figure(figsize=(8, 6))

# Background image with transparency
if use_background:
    img = mpimg.imread('../data/map.jpg')
    plt.imshow(img, extent=[0, 100, 0, 100], origin='lower', aspect='auto', alpha=0.5)

# Scatter plot
scatter = plt.scatter(
    x, y, c=signal_strength, s=sizes, cmap='viridis', alpha=0.8, edgecolor='gray'
)

# Add color bar
cbar = plt.colorbar(scatter, label="Signal Strength (dBm)")
cbar.ax.set_title("Weak (-110) to Strong (-60)", fontsize=8)


# Create custom legend entries
legend_elements = [
    Line2D([0], [0], label="Weak Signal (-110 to -90 dBm)", color='none'),
    Line2D([0], [0], label="Medium Signal (-89 to -70 dBm)", color='none'),
    Line2D([0], [0], label="Strong Signal (-69 to -60 dBm)", color='none')
]

# Add the custom legend
plt.legend(handles=legend_elements, loc="upper right", title="Signal Quality")



# Choose random points to display signal strength
for i in [24]:
    plt.text(
        x[i], y[i], f"{signal_strength[i]:.1f} dBm", fontsize=10, ha='center', va='center', color="black"
    )

# Labels and Title
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.title("2D Signal Strength Visualization (dBm)")

# Grid for better visualization
plt.grid(True, alpha=0.97)

# Show plot
plt.show()
