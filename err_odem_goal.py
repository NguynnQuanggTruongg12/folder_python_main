#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist, PoseStamped
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
import numpy as np

# Biến toàn cục
robot_x = 0
robot_y = 0
robot_yaw_degree = 0
robot_yaw_goal_degree = 0  # Giá trị mặc định (cập nhật từ /move_base_simple/goal)
daquayxong = 0

# Callback xử lý dữ liệu từ /move_base_simple/goal
def goal_callback(data):
    global robot_yaw_goal_degree

    # Lấy giá trị quaternion từ message
    quaternion = (
        data.pose.orientation.x,
        data.pose.orientation.y,
        data.pose.orientation.z,
        data.pose.orientation.w
    )

    # Chuyển đổi quaternion sang góc Euler
    _, _, yaw_goal = euler_from_quaternion(quaternion)

    # Chuyển góc yaw từ radian sang độ
    robot_yaw_goal_degree = np.degrees(yaw_goal)

    rospy.loginfo(f"Goal received: yaw_goal_degree={robot_yaw_goal_degree:.2f}°")

# Callback xử lý dữ liệu từ /odom
def odom_callback(data):
    global daquayxong, robot_yaw_degree, robot_x, robot_y

    robot_x = data.pose.pose.position.x
    robot_y = data.pose.pose.position.y

    # Lấy quaternion từ dữ liệu odom
    quaternion = (
        data.pose.pose.orientation.x,
        data.pose.pose.orientation.y,
        data.pose.pose.orientation.z,
        data.pose.pose.orientation.w
    )
    _, _, robot_yaw = euler_from_quaternion(quaternion)
    robot_yaw_degree = np.degrees(robot_yaw)

    # Chuẩn hóa góc lỗi [-180, 180]
    error = robot_yaw_goal_degree - robot_yaw_degree #+ 180) % 360 - 180

    twist_msg = Twist()
    if daquayxong == 0:
        if abs(error) > 0.3:  # Nếu lỗi lớn hơn ngưỡng 0.3 độ
            # Điều chỉnh tốc độ góc dựa trên hướng lỗi
            if error > 0:
                twist_msg.angular.z = -0.4  # Xoay trái (góc âm)
            else:
                twist_msg.angular.z = 0.4  # Xoay phải (góc dương)
            pub_twist.publish(twist_msg)
        else:
            twist_msg.angular.z = 0  # Dừng quay khi đạt mục tiêu
            pub_twist.publish(twist_msg)
            rospy.loginfo(f"Góc mục tiêu: {robot_yaw_goal_degree:.2f}° | Góc hiện tại: {robot_yaw_degree:.2f}° | Lỗi: {error:.2f}°")
            daquayxong = 1
            rospy.signal_shutdown("Hoàn thành nhiệm vụ")

# Hàm chính
def main():
    global pub_twist

    # Khởi tạo node ROS
    rospy.init_node('yaw_goal_controller', anonymous=True)

    # Publisher gửi lệnh vận tốc đến /cmd_vel
    pub_twist = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    # Subscriber lắng nghe dữ liệu từ /odom
    rospy.Subscriber('/odom', Odometry, odom_callback)

    # Subscriber lắng nghe dữ liệu từ /move_base_simple/goal
    rospy.Subscriber('/move_base_simple/goal', PoseStamped, goal_callback)

    rospy.loginfo("Node yaw_goal_controller đã sẵn sàng...")

    # Vòng lặp ROS
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
