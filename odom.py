import rospy
from nav_msgs.msg import Odometry
import csv

# init
rospy.init_node('odom_listener', anonymous=True)

# csv
csv_file = open('odom_data.csv', mode='w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['timestamp', 'x', 'y', 'z'])

def odom_callback(data):
    # timestamp & pose
    timestamp = int(data.header.stamp.to_sec()*1000)
    x = data.pose.pose.position.x
    y = data.pose.pose.position.y
    z = data.pose.pose.position.z
	
    # output
    rospy.loginfo(f"Time: {timestamp}, X: {x}, Y: {y}, Z: {z}")
    
    # CSV
    csv_writer.writerow([timestamp, x, y, z])
    csv_file.flush()


rospy.Subscriber('/jetauto_1/odom', Odometry, odom_callback)


rospy.spin()


csv_file.close()
