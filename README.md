# gix_tmr_launch_proj

**GIX Launch Project:** T-Mobile Autonomous Robot for 5G Signal Testing in Indoor Environments

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

### RTAB-Map Creation
To create a map using RTAB-Map, run the following commands:

```bash
sudo systemctl stop start_app_node.service
roslaunch jetauto_slam slam.launch slam_methods:=rtabmap
roslaunch jetauto_slam rviz_slam.launch slam_methods:=rtabmap
roslaunch jetauto_peripherals teleop_key_control.launch
```

---

### Suggestions:
1. Use this README in conjunction with project-specific instructions for easier reference.
2. Add a table of contents for larger projects if necessary.
3. Include a "Contributing" or "Issues" section if other collaborators will use this repository. 

