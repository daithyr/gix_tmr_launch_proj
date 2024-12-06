import pandas as pd
import json
from datetime import datetime

# File paths
odom_file = "../../data/odom_data.csv"
signal_file = "../../data/5G_Signal_Data_20241205_1536.csv"
output_file = "../data/raw_real.json"

# Read the odom data
odom_data = pd.read_csv(odom_file)
odom_data['timestamp'] = pd.to_datetime(odom_data['timestamp'], unit='ms')

# Read the 5G signal data
signal_data = pd.read_csv(signal_file)
signal_data['Milliseconds'] = pd.to_datetime(signal_data['Milliseconds'], unit='ms')

# Merge the data with allowable timestamp error
tolerance = pd.Timedelta(milliseconds=100)
merged_data = pd.merge_asof(
    odom_data.sort_values('timestamp'),
    signal_data.sort_values('Milliseconds'),
    left_on='timestamp',
    right_on='Milliseconds',
    tolerance=tolerance,
    direction='nearest'
)

# Select relevant columns and format into the desired JSON structure
result_data = merged_data[['x', 'y', 'Signal Strength (dBm)']].dropna()
result_data.rename(columns={'Signal Strength (dBm)': 'signal_strength'}, inplace=True)



# Convert to list of dictionaries
formatted_data = result_data.apply(lambda row: {
    "x": row['x'],
    "y": row['y'],
    "signal_strength": row['signal_strength']
}, axis=1).tolist()

# Save to JSON
with open(output_file, 'w') as f:
    json.dump(formatted_data, f, indent=4)
