#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Pose
import time
def publish_pose(x,y,z,w):
    rospy.init_node('pose_publisher', anonymous=True)
    pub = rospy.Publisher('/slamware_ros_sdk_server_node/set_pose', Pose, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz
    count = 0
    while not rospy.is_shutdown():
        # Tạo đối tượng Pose với giá trị cụ thể
        pose_msg = Pose()
        pose_msg.position.x = x
        pose_msg.position.y = y
        pose_msg.orientation.z = z
        pose_msg.orientation.w = w
        # Publish dữ liệu lên topic
        pub.publish(pose_msg)
        rate.sleep()
        count +=1
        if count == 2:
            print('reset done')
            break

publish_pose(0,0,0,1)