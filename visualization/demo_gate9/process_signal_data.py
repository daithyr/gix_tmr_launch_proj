import pandas as pd
import numpy as np

# Read the 5G signal data file
signal_data = pd.read_csv('./data/5G_Signal_Data.csv')

# Delete Timestamp column
signal_data = signal_data.drop('Timestamp', axis=1)

# Get min and max milliseconds
min_ms = signal_data['Milliseconds'].min()
max_ms = signal_data['Milliseconds'].max()

# Generate new timestamps with random intervals between 50-150ms
new_timestamps = []
current_ms = min_ms
while current_ms <= max_ms:
    new_timestamps.append(current_ms)
    current_ms += np.random.randint(50, 151)

# Create new dataframe with generated timestamps
new_data = pd.DataFrame({
    'Milliseconds': new_timestamps,
    'Signal Strength (dBm)': [-74] * len(new_timestamps)
})

# Combine original and new data
combined_data = pd.concat([signal_data, new_data], ignore_index=True)

# Sort by Milliseconds
combined_data = combined_data.sort_values('Milliseconds')

# Save to new CSV file
combined_data.to_csv('./data/5g_signal_data_new.csv', index=False)
