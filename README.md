# TMR: T-Mobile Autonomous Robot for 5G Signal Testing in Indoor Environments

## TurtleBot 4 Documentation

### Key References
- **Button Indication:** [Create 3 Button Indicators](https://iroboteducation.github.io/create3_docs/hw/face/)
- **Setup Instructions:** [TurtleBot 4 Basic Setup Guide](https://turtlebot.github.io/turtlebot4-user-manual/setup/basic.html)
- **Mounting Reference:**
  - [Mechanical Overview](https://iroboteducation.github.io/create3_docs/hw/mechanical/)
  - [Payload Mounting Guide](https://turtlebot.github.io/turtlebot4-user-manual/mechanical/payloads.html)

### Networks
1. **Access Point Mode** (Preferred Mode):  
   - On your PC, connect to the TurtleBot4 Wi-Fi network.  
   - The Wi-Fi password is `Turtlebot4`.

---

## HiWonder Setup

Noname Settings
```bash
Host: 10.19.141.37
Port: 4000
```

Hiwonder Login
```bash
Username: jetauto
Password: hiwonder
```

### RTAB-Map
To create a map using RTAB-Map, run the following commands:

```bash
sudo systemctl stop start_app_node.service
roslaunch jetauto_slam slam.launch slam_methods:=rtabmap
roslaunch jetauto_slam rviz_slam.launch slam_methods:=rtabmap
roslaunch jetauto_peripherals teleop_key_control.launch
```

if encountering permission issues, run the following commands:

```bash
sudo chmod 666 /dev/ttyTHS1
```

To navigate using the created map, run the following commands:

```bash
sudo systemctl stop start_app_node.service
roslaunch jetauto_navigation rtabmap_navigation.launch
roslaunch jetauto_navigation rviz_rtabmap_navigation.launch
roslaunch jetauto_navigation publish_point.launch
```
打开 Rtabmap_cloud 选项卡,将 Download namespace 内容修改为 robot_1/rtabmap
---

## Visualization Demo

This section explains how to visualize the 5G signal data collected by the autonomous robot on a 2D map.

### Features
- Displays 5G signal strength on a 2D map of the indoor environment.
- Interactive visualization with color-coded signal strength.
- Background map integration for enhanced spatial understanding.

### Prerequisites
1. Ensure Python 3.x is installed on your system.
2. Install required libraries:
   ```bash
   pip install matplotlib numpy
   ```
3. Place the 2D room map image (`map.jpg`) in the `data/` directory.

### Running the Visualization
To run the visualization demo:

1. Ensure `data.json` (signal data) and `map.jpg` (background image) are in the `data/` directory.
2. Run the Python script:
   ```bash
   cd visualization/demo
   # python dummy_data.py
   python demo.py
   ```
3. The script will display a scatter plot of 5G signal strength:
   - **Point Size**: Signal strength representation (optional: toggle uniform size).
   - **Point Color**: Intensity of 5G signal strength.
   - **Background**: Room map overlaid with signal data.

### Example Output
- A scatter plot with the indoor map as a background.
- Signal strength visualized in gradient colors (e.g., blue for low and yellow for high).

### Files
- `data/data.json`: JSON file containing signal strength data with `x`, `y` coordinates.
- `data/map.jpg`: Background image of the indoor environment.
- `visualization_demo.py`: Script to generate the visualization.

