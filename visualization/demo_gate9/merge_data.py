import pandas as pd
import json
from datetime import datetime
import matplotlib.pyplot as plt

# File paths
odom_file = "./data/odom_data.csv"
signal_file = "./data/5g_signal_data_new.csv" 
output_file = "./data/raw_real.json"

# Read the odom data
odom_data = pd.read_csv(odom_file)
odom_data['timestamp'] = pd.to_datetime(odom_data['timestamp'], unit='ms')

# Read the 5G signal data
signal_data = pd.read_csv(signal_file)
signal_data['Milliseconds'] = pd.to_datetime(signal_data['Milliseconds'], unit='ms')

# Print data info for debugging
print("Odom data shape:", odom_data.shape)
print("Signal data shape:", signal_data.shape)
# Print first and last few rows of each dataset
print("\nFirst few rows of odom data:")
print(odom_data.head())
print("\nLast few rows of odom data:")
print(odom_data.tail())

print("\nFirst few rows of signal data:") 
print(signal_data.head())
print("\nLast few rows of signal data:")
print(signal_data.tail())

# Plot timestamps for comparison
# plt.figure(figsize=(12, 6))
# plt.plot(odom_data['timestamp'], [1]*len(odom_data), 'b.', label='Odom Data', markersize=2)
# plt.plot(signal_data['Milliseconds'], [0]*len(signal_data), 'r.', label='Signal Data', markersize=4)
# plt.yticks([0, 1], ['Signal Data', 'Odom Data'])
# plt.xlabel('Timestamp')
# plt.title('Timestamp Comparison between Odom and Signal Data')
# plt.legend()
# plt.grid(True)
# plt.show()

# Merge the data with allowable timestamp error
tolerance = pd.Timedelta(milliseconds=1000)
merged_data = pd.merge_asof(
    signal_data.sort_values('Milliseconds'),
    odom_data.sort_values('timestamp'),
    left_on='Milliseconds',
    right_on='timestamp',
    tolerance=tolerance,
    direction='nearest'
)

# Select relevant columns and format into the desired JSON structure
result_data = merged_data[['x', 'y', 'Signal Strength (dBm)']].dropna()
result_data.rename(columns={'Signal Strength (dBm)': 'signal_strength'}, inplace=True)

# Convert to list of dictionaries
formatted_data = result_data.to_dict('records')

# Save to JSON
with open(output_file, 'w') as f:
    json.dump(formatted_data, f, indent=4)

print(f"\nData has been successfully saved to {output_file}")
