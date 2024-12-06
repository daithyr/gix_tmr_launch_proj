import pandas as pd
import json
from datetime import datetime

# File paths
odom_file = "../../data/odom_data.csv"
signal_file = "../../data/5G_Signal_Data_20241205_1536.csv"
output_file = "../data/raw_real.json"

def map_signal_strength(signal_strength):
    """
    将 5G 信号强度从 dBm 映射到 0-1 的范围，根据以下偏好：
    Excellent: ≥-89 dBm
    Good: -90 to -104 dBm
    Fair: -105 to -114 dBm
    Poor: -115 to -124 dBm
    No signal: ≤-125 dBm
    """
    if signal_strength >= -89:
        return 1.0  # Excellent
    elif -104 <= signal_strength <= -90:
        return 0.75  # Good
    elif -114 <= signal_strength <= -105:
        return 0.5  # Fair
    elif -124 <= signal_strength <= -115:
        return 0.25  # Poor
    elif signal_strength <= -125:
        return 0.0  # No signal
    else:
        return None  # For unexpected cases

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

# Process and map signal strength
merged_data['signal_strength_mapped'] = merged_data['Signal Strength (dBm)'].apply(map_signal_strength)

# Select relevant columns and format into the desired JSON structure
result_data = merged_data[['x', 'y', 'signal_strength_mapped']].dropna()
result_data.rename(columns={'signal_strength_mapped': 'signal_strength'}, inplace=True)

# Convert to list of dictionaries
formatted_data = result_data.apply(lambda row: {
    "x": row['x'],
    "y": row['y'],
    "signal_strength": row['signal_strength']
}, axis=1).tolist()

# Save to JSON
with open(output_file, 'w') as f:
    json.dump(formatted_data, f, indent=4)

print(f"Data has been successfully saved to {output_file}")
