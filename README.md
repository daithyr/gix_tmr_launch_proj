# gix_tmr_launch_proj
gix launch project -- T-mobile autonomous robot 5g signal testing for indoor enviornment

## turtlebot 4 docs
button indication: https://iroboteducation.github.io/create3_docs/hw/face/

setup instruction: https://turtlebot.github.io/turtlebot4-user-manual/setup/basic.html

mounting reference: https://iroboteducation.github.io/create3_docs/hw/mechanical/

https://turtlebot.github.io/turtlebot4-user-manual/mechanical/payloads.html

### Neworks
1. Access point mode (always use this mode): On your PC, connect to the Turtlebot4 Wi-Fi network. The password is also Turtlebot4.

## HiWonder
Rtab create map:
```
sudo systemctl stop start_app_node.service
roslaunch jetauto_slam slam.launch slam_methods:=rtabmap
roslaunch jetauto_slam rviz_slam.launch slam_methods:=rtabmap
roslaunch jetauto_peripherals teleop_key_control.launch
```