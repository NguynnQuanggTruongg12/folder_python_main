import cv2
import numpy as np
import math
import rospy
from geometry_msgs.msg import Twist, PoseStamped
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion

# Khởi tạo biến toàn cục
daquayxong = 0
robot_yaw_goal_degree = 0  # Góc mục tiêu
robot_yaw_degree = 0  # Góc hiện tại

# Publisher cho /cmd_vel
pub_twist = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

def odom_callback(data):
    global daquayxong, robot_yaw_goal_degree, robot_yaw_degree

    # Lấy dữ liệu từ /odom
    quaternion = (
        data.pose.pose.orientation.x,
        data.pose.pose.orientation.y,
        data.pose.pose.orientation.z,
        data.pose.pose.orientation.w
    )

    # Chuyển từ quaternion sang góc Euler
    _, _, robot_yaw = euler_from_quaternion(quaternion)
    robot_yaw_degree = np.degrees(robot_yaw)

    # Góc mục tiêu (sửa quaternion1 hoặc cập nhật qua topic khác)
    quaternion1 = (
        0,
        0,
        0,
        1
    )
    _, _, robot_yaw_goal = euler_from_quaternion(quaternion1)
    robot_yaw_goal_degree = np.degrees(robot_yaw_goal)
    # print(robot_yaw_goal_degree)

    # Tính toán sai số và chuẩn hóa về [-180, 180]
    error = robot_yaw_goal_degree - robot_yaw_degree
    error = (error + 180) % 360 - 180  # Chuẩn hóa góc

    # Điều khiển robot quay
    twist_msg = Twist()
    if daquayxong == 0:
        if abs(error) > 0.3:  # Nếu lỗi góc lớn hơn ngưỡng
            twist_msg.angular.z = 0.4 if error > 0 else -0.4
            pub_twist.publish(twist_msg)
            rospy.loginfo(f"Đang xoay: Lỗi {error:.2f}°")
        else:
            twist_msg.angular.z = 0
            pub_twist.publish(twist_msg)
            rospy.loginfo(f"Đã đạt góc mục tiêu! Góc hiện tại: {robot_yaw_degree:.2f}°")
            daquayxong = 1
            rospy.signal_shutdown("Hoàn thành nhiệm vụ")

# Node chính
def main():
    rospy.init_node('yaw_goal_controller', anonymous=True)

    # Lắng nghe dữ liệu từ /odom
    rospy.Subscriber('/slamware_ros_sdk_server_node/odom', Odometry, odom_callback)

    rospy.loginfo("Node đã khởi chạy!")
    rospy.spin()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
