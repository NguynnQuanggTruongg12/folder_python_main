from PyQt5.QtCore import QThread,pyqtSignal
import rospy
import math
from tf.transformations import euler_from_quaternion

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped

import os
import time
import subprocess
from move_base_msgs.msg import MoveBaseActionGoal
import serial
from geometry_msgs.msg import Twist, PoseStamped, Pose
from actionlib_msgs.msg import GoalStatusArray
import mysql.connector
from PyQt5.QtCore import QThread, pyqtSignal
import sys

from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
from actionlib_msgs.msg import GoalStatus
from datetime import datetime
import time
import os
import numpy as np

done_goal = False
hieu = 0


class run_roscore(QThread):
    USB_MEGA_XE = '/dev/ttyUSB0'
    def __init__(self) :
        super().__init__()
        self.is_running = False
        
    
    def run(self):
        self.run_login()

    def run_login(self):

        # rospy.Subscriber('/slamware_ros_sdk_server_node/odom', Odometry, send_odom)
        # rospy.Subscriber('/cmd_vel', Twist, send_cmd_vel)
        
        

        # time.sleep(1)
        os.system('gnome-terminal -- roslaunch navigation_bot move_base_qd.launch')
        # # os.system('gnome-terminal -- rosrun map_server map_server /home/dong/catkin_ws/src/navigation_bot/map/{map_file}.yaml')
        # time.sleep(2)
        os.system('gnome-terminal -- roslaunch slamware_ros_sdk slamware_ros_sdk_server_node.launch ip_address:=192.168.11.1')
        # time.sleep(2)
        # os.system('gnome-terminal -- rosrun rosserial_python serial_node.py /dev/ttyUSB0')
        subprocess.Popen(['gnome-terminal', '--', 'rosrun', 'rosserial_python', 'serial_node.py', self.USB_MEGA_XE])

        # ------------------- chay file final cam ------------------
        process3 = subprocess.Popen("python3 /home/robot/Documents/ROBOT_INTERFACE/GUI_ROBOT_07_1_18h/reset_lidar.py", shell=True)
        process3.wait()

        self.spin_ros()
        # print('roscore done')
    def spin_ros(self):
        rospy.spin()
# class err_odem_goal(QThread):
class ErrOdemGoal(QThread):
    def __init__(self, quaternion1):
        super().__init__()
        self.quaternion1 = quaternion1

    def run(self):
        self.yaw_goal_controller(self.quaternion1)

    def yaw_goal_controller(self, quaternion1):
        print(".......................ok..................................")
        
        # Biến toàn cục
        daquayxong = False
        robot_yaw_goal_degree = 0  # Góc mục tiêu
        robot_yaw_degree = 0      # Góc hiện tại

        # Publisher cho /cmd_vel
        pub_twist = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        # Callback xử lý dữ liệu từ /odom
        def odom_callback(data):
            nonlocal daquayxong, robot_yaw_goal_degree, robot_yaw_degree

            # Lấy dữ liệu quaternion từ /odom
            quaternion = (
                data.pose.pose.orientation.x,
                data.pose.pose.orientation.y,
                data.pose.pose.orientation.z,
                data.pose.pose.orientation.w
            )
            print(quaternion)
            
            # Chuyển đổi từ quaternion sang góc Euler
            _, _, robot_yaw = euler_from_quaternion(quaternion)
            robot_yaw_degree = np.degrees(robot_yaw)

            # Góc mục tiêu
            _, _, robot_yaw_goal = euler_from_quaternion(quaternion1)
            robot_yaw_goal_degree = np.degrees(robot_yaw_goal)

            # Tính toán sai số và chuẩn hóa về [-180, 180]
            error = robot_yaw_goal_degree - robot_yaw_degree
            error = (error + 180) % 360 - 180

            # Điều khiển robot
            twist_msg = Twist()
            if not daquayxong:
                if abs(error) > 0.3:  # Nếu lỗi lớn hơn ngưỡng
                    twist_msg.angular.z = 0.4 if error > 0 else -0.4
                    pub_twist.publish(twist_msg)
                    rospy.loginfo(f"Đang xoay: Lỗi {error:.2f}°")
                else:
                    twist_msg.angular.z = 0
                    pub_twist.publish(twist_msg)
                    rospy.loginfo(f"Đã đạt góc mục tiêu! Góc hiện tại: {robot_yaw_degree:.2f}°")
                    daquayxong = True
                    # rospy.signal_shutdown("Hoàn thành nhiệm vụ")

        # Subscriber lắng nghe từ /odom
        rospy.Subscriber('/slamware_ros_sdk_server_node/odom', Odometry, odom_callback)

        # Chạy vòng lặp để kiểm tra trạng thái
        while not daquayxong:
            rospy.sleep(0.1)  # Chờ một chút trước khi kiểm tra lại
        print("Đã hoàn thành việc quay, tiếp tục các tác vụ khác.")


        
# class module_camera(QThread):
#     def __init__(self):
#         super().__init__()



class NavigationThread(QThread):
    send_bool = pyqtSignal(bool)
    text_finish = pyqtSignal(bool)
    enable_btn = pyqtSignal(bool)
    clear_auto = pyqtSignal(bool)
    arduino_charing = pyqtSignal(bool)
    done_navigation = pyqtSignal(bool)
    dichuyen_2diem = pyqtSignal(int)
    dichuyen_3diem = pyqtSignal(int)
    dichuyen_1diem = pyqtSignal(int)
    dichuyen_done = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.is_running = True
        self.data_odom = []
        self.ve_home = False
        self.quatrinh_move = False
        self.dung = 0
        self.robot_dang_di_chuyen = False
        self.ve_home = False
        self.quatrinh_dichuyen = False
        self.quatrinh_dichuyen_2diem = False
        self.quatrinh_dichuyen_3diem = False
        self.quatrinh_dichuyen_2diem_2 = False
        self.quatrinh_dichuyen_2diem_1 = False
        self.quatrinh_dichuyen_3diem = False
        self.quatrinh_dichuyen_3diem_1 = False
        self.quatrinh_dichuyen_3diem_2 = False
        self.quatrinh_dichuyen_3diem_3 = False
        self.quatrinh_dichuyen_1diem = False

        # Variables for tracking goal position
        self.x_goal = 0
        self.y_goal = 0
        self.z_goal = 0
        self.w_goal = 0

        # Initialize ROS node (done once)
        rospy.init_node('navigation_thread', anonymous=True)

    def run(self):
        if self.is_running:
            print("done start")

            # Subscriber for odometry
            rospy.Subscriber('/slamware_ros_sdk_server_node/odom', Odometry, self.send_odom)

            # SimpleActionClient for move_base
            self.client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
            self.client.wait_for_server()

            # Subscriber for goal status
            rospy.Subscriber('/move_base/status', GoalStatus)

            # Publisher for sending goals
            self.goal_publisher = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=10)
            self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
            # self.kiemtra_hoanthanh_nv()

    def send_goal(self, x_goal, y_goal, z_goal, w_goal):
        # Clear costmaps (optional)
        os.system('rosservice call /move_base/clear_costmaps')

        # Publish the navigation goal
        goal = PoseStamped()
        goal.header.frame_id = "map"  # Set this to your map frame
        goal.header.stamp = rospy.Time.now()

        goal.pose.position.x = x_goal
        goal.pose.position.y = y_goal
        goal.pose.orientation.z = z_goal
        goal.pose.orientation.w = w_goal

        # Publish the goal to the move_base_simple/goal topic
        self.goal_publisher.publish(goal)
        # print(f"Sent Goal -> x: {x_goal}, y: {y_goal}, z: {z_goal}, w: {w_goal}")

        # Optionally, update internal status
        # self.ve_home = False
        # print('Goal published successfully')



    def yaw_from_quaternion(self, quaternion):
        # Chuyển đổi quaternion sang góc Euler (roll, pitch, yaw)
        (roll, pitch, yaw) = euler_from_quaternion([quaternion.x, quaternion.y, quaternion.z, quaternion.w])
        return yaw

    def tinhgoc_yaw(self, z, w):
        esp1 = 0
        esp2 = 0
        esp3 = z
        esp4 = w
        r11 = 1 - 2 * esp2 * esp2 - 2 * esp3 * esp3
        r21 = 2 * (esp1 * esp2 + esp3 * esp4)
        yaw = math.atan2(r21, r11)
        yaw = yaw * 180 / math.pi

        return yaw


    def kiemtra_hoanthanh_nv(self, x, x_goal, y, y_goal, z, z_goal, w, w_goal):
        x , y, z,  w = self.data_odom
        x_goal, y_goal, z_goal, w_goal = self.data_goal
        yaw_des = self.tinhgoc_yaw(z=z_goal, w=w_goal)
        yaw = self.tinhgoc_yaw(z=z, w=w)
        yaw_diff = (yaw - yaw_des + 180) % 360 - 180

        # Check if the robot is close enough to the goal (both position and orientation)
        if (abs(x - x_goal) < 0.2) and (abs(y - y_goal) < 0.2) and (abs(yaw_diff) < 20):
            # print(f"Robot is near the goal: x={x}, y={y}, yaw={yaw}")
            # print('Doneeeeeeee roi nha')
            return True
        else:
            # print(f"Robot still moving: x={x}, y={y}, yaw={yaw}")
            return False
    def send_data_goal(self, x_goal, y_goal, z_goal, w_goal):
        # x_goal =  self.x_goal
        # y_goal = self.y_goal
        # z_goal = self.z_goal
        # w_goal = self.w_goal
        self.data_goal = [x_goal, y_goal, z_goal, w_goal]
        # print(self.data_goal)


    def send_odom(self, data):
        # global done_goal, hieu

        # Extract robot's current position and orientation from odometry data
        x = data.pose.pose.position.x
        y = data.pose.pose.position.y
        z = data.pose.pose.orientation.z
        w = data.pose.pose.orientation.w
        orientation = data.pose.pose.orientation
        yaw = math.degrees(self.yaw_from_quaternion(orientation))
        self.data_odom = [x, y, z, w]

        # If the robot is currently moving towards the goal
        # if self.quatrinh_move:
        #     self.robot_dang_di_chuyen = True
        #     # print(f"Robot is moving: x={x}, y={y}, yaw={yaw}")

        #     # Check if the robot has reached the goal

        if self.quatrinh_dichuyen == True:
            # self.done_navigation.emit(True)
            if self.kiemtra_hoanthanh_nv(x, self.x_goal, y, self.y_goal, z, self.z_goal, w, self.w_goal):
                self.dung += 1
                # print(f"Robot is near the goal, stationary count: {self.dung}")

            #         # After 150 consecutive checks where the robot is at the goal, consider it arrived
                if self.dung > 150:
                    print("Goal reached")
            #             self.robot_dang_di_chuyen = False
                    self.dichuyen_done.emit(111)
                    self.quatrinh_dichuyen= False
                    self.dung = 0  # Reset the counter

            #             self.done_navigation.emit(True)  # Emit signal that navigation is complete
            else:
                self.dung = 0  # Reset counter if the robot moves away from the goal
        # self.navigation_dadiem(x, y, z, w)


        ################################=======================================
        if self.quatrinh_dichuyen_1diem == True:
            if self.kiemtra_hoanthanh_nv(x, self.x_goal, y, self.y_goal, z, self.z_goal, w, self.w_goal):
                self.dung += 1
                # print(f"Robot is near the goal, stationary count: {self.dung}")

            #         # After 150 consecutive checks where the robot is at the goal, consider it arrived
                if self.dung > 150:
                    print("Goal reached")
            #             self.robot_dang_di_chuyen = False
                    self.dichuyen_1diem.emit(111)
                    self.quatrinh_dichuyen_1diem= False
                    self.dung = 0  # Reset the counter

            #             self.done_navigation.emit(True)  # Emit signal that navigation is complete
            else:
                self.dung = 0  # Reset counter if the robot moves away from the goal

        if self.quatrinh_dichuyen_2diem == True:
            # print('davao')
            if self.quatrinh_dichuyen_2diem_1 == True:
                if self.kiemtra_hoanthanh_nv(x, self.x_goal, y, self.y_goal, z, self.z_goal, w, self.w_goal):
                    self.dung += 1
                    if self.dung > 150:
                        self.dichuyen_2diem.emit(111)
                        print("Goal reached1")
                        self.quatrinh_dichuyen_2diem_1 = False
                        self.dung = 0  # Reset the counter 
                else: self.dung = 0 
            if self.quatrinh_dichuyen_2diem_2 == True:
                if self.kiemtra_hoanthanh_nv(x, self.x_goal, y, self.y_goal, z, self.z_goal, w, self.w_goal):
                    self.dung += 1
                    if self.dung > 150:
                        print("Goal reached2")
                        self.dichuyen_2diem.emit(222)
                        self.quatrinh_dichuyen_2diem_2 = False
                        self.dung = 0  # Reset the counter
                else: self.dung = 0


        ##############################======================
        if self.quatrinh_dichuyen_3diem == True:
            # print('davao')
            if self.quatrinh_dichuyen_3diem_1 == True:
                if self.kiemtra_hoanthanh_nv(x, self.x_goal, y, self.y_goal, z, self.z_goal, w, self.w_goal):
                    self.dung += 1
                    if self.dung > 150:
                        self.dichuyen_3diem.emit(111)
                        print("Goal reached1111111111111111")
                        self.quatrinh_dichuyen_3diem_1 = False
                        self.dung = 0  # Reset the counter 
                else: self.dung = 0 
            if self.quatrinh_dichuyen_3diem_2 == True:
                if self.kiemtra_hoanthanh_nv(x, self.x_goal, y, self.y_goal, z, self.z_goal, w, self.w_goal):
                    self.dung += 1
                    if self.dung > 150:
                        self.dichuyen_3diem.emit(222)
                        print("Goal reached2222222222222222")
                        self.quatrinh_dichuyen_3diem_2 = False
                        self.dung = 0  # Reset the counter
                else: self.dung = 0
            if self.quatrinh_dichuyen_3diem_3 == True:
                if self.kiemtra_hoanthanh_nv(x, self.x_goal, y, self.y_goal, z, self.z_goal, w, self.w_goal):
                    self.dung += 1
                    if self.dung > 150:
                        self.dichuyen_3diem.emit(333)
                        print("Goal reached33333333333333333")
                        self.quatrinh_dichuyen_3diem_3 = False
                        self.dung = 0  # Reset the counter
                else: self.dung = 0
        
    # def navigation_dadiem(self, x, y, z, w):
    #     # """Handle navigation between multiple points (2 or 3 points)."""
    #     if self.quatrinh_dichuyen_2diem:
    #         # Navigating between two points
    #         if self.quatrinh_dichuyen_2diem_1:
    #             if self.check_and_update_goal(x, y, z, w, "1"):
    #                 self.dichuyen_2diem.emit(222)
    #                 print("First goal reached")
    #                 self.quatrinh_dichuyen_2diem_1 = False
    #                 self.quatrinh_dichuyen_2diem_2 = True  # Ensure transition to second goal
    #         elif self.quatrinh_dichuyen_2diem_2:
    #             if self.check_and_update_goal(x, y, z, w, "2"):
    #                 print("Second goal reached")
    #                 self.quatrinh_dichuyen_2diem_2 = False

    #     elif self.quatrinh_dichuyen_3diem:
    #         # Navigating between three points
    #         if self.quatrinh_dichuyen_3diem_1:
    #             if self.check_and_update_goal(x, y, z, w, "1"):
    #                 self.dichuyen_3diem.emit(111)
    #                 print("First goal reached")
    #                 self.quatrinh_dichuyen_3diem_1 = False
    #                 self.quatrinh_dichuyen_3diem_2 = True  # Ensure transition to second goal
    #         elif self.quatrinh_dichuyen_3diem_2:
    #             if self.check_and_update_goal(x, y, z, w, "2"):
    #                 self.dichuyen_3diem.emit(222)
    #                 print("Second goal reached")
    #                 self.quatrinh_dichuyen_3diem_2 = False
    #                 self.quatrinh_dichuyen_3diem_3 = True  # Ensure transition to third goal
    #         elif self.quatrinh_dichuyen_3diem_3:
    #             if self.check_and_update_goal(x, y, z, w, "3"):
    #                 print("Third goal reached")
    #                 self.quatrinh_dichuyen_3diem_3 = False

    # def check_and_update_goal(self, x, y, z, w, goal_number):
    #     # """ Helper function to check if the robot has reached a goal """
    #     if self.kiemtra_hoanthanh_nv(x, self.x_goal, y, self.y_goal, z, self.z_goal, w, self.w_goal):
    #         print("okk")
    #         self.dung += 1
    #         if self.dung > 150:
    #             # print(f"Goal {goal_number} reached")
    #             print('done navigation')
    #             self.dung = 0  # Reset counter after goal reached
    #             return True
    #     else:
    #         self.dung = 0  # Reset counter if robot moves away from the goal
    #     return False

        



  



