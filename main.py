import sys
import cv2
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QImage, QPixmap
from interface2 import Ui_MainWindow  
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidgetItem
import mysql.connector
import rospy
import numpy as np
import matplotlib.pyplot as plt
from nav_msgs.msg import OccupancyGrid
import os
from form_them import Ui_Form_nhaptenban
from form_save import Ui_Form_save_setting
from form_dichuyen import Ui_Form_dichuyen
from form_emergency import Ui_Form_emergency
from form_done_dichuyen import Ui_Form_done_dichuyen
from form_err_dh import Ui_Form_err_dh
from form_err_arduino import Ui_Form_err_arduino
from form_err_send_robot import Ui_Form_err_send_robot
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped
from Qthread import *
import subprocess
import re
from PIL import Image
import serial.tools.list_ports
import math
import signal
from scipy.optimize import fsolve






db = mysql.connector.connect(user="robot", password='123456', host='127.0.0.1', database='sys')
os.system('gnome-terminal -- roscore')
time.sleep(1)

class MainWindow(QtWidgets.QMainWindow):


    USB_MEGA_ROBOT = '/dev/ttyUSB1'
    BAUDRATE = '115200'
    def __init__(self):
        super(MainWindow, self).__init__()
        self.uic = Ui_MainWindow()  # Tạo instance của lớp giao diện
        self.uic.setupUi(self)  # Thiết lập giao diện trên MainWindow

        self.navigation_thread = NavigationThread()
        self.run_ros = run_roscore()
        # self.run_ErrOdemGoal = ErrOdemGoal()
        # self.navigation_thread.done_navigation.connect(self.update_vitri)
        self.navigation_thread.dichuyen_2diem.connect(self.update_2diem)
        self.navigation_thread.dichuyen_3diem.connect(self.update_3diem)
        self.navigation_thread.dichuyen_1diem.connect(self.update_1diem)
        self.navigation_thread.dichuyen_done.connect(self.done_dichuyen)
       

        # rospy.init_node('odometry_listener', anonymous=True)
        # rospy.init_node('goal_sender', anonymous=True)  
        
        self.uic.stackedWidget.setCurrentIndex(0)
        self.file_path = r"/home/robot/catkin_ws/src/navigation_bot/config/dwa_local_planner_params.yaml"
        self.file_path_1 = r"/home/robot/catkin_ws/src/navigation_bot/config/my_laser_config.yaml"
        self.map_folder_path = '/home/robot/catkin_ws/src/navigation_bot/map'

        self.l1 = 18
        self.l2 = 15
        self.l3 = 17


        # rospy.init_node('map_viewer', anonymous=True)
        # self.current_position = None
        # rospy.Subscriber("/slamware_ros_sdk_server_node/odom", Odometry, self.odometry_callback)

        
        
        # Đăng ký subscriber để lấy dữ liệu map từ topic 'map'
        # self.map_sub = rospy.Subscriber('/map', OccupancyGrid, self.map_callback)
        # self.map_data = None

        self.selected_goal_ids = []  # Khởi tạo danh sách điểm đến đã chọn
        self.current_goal_index = 0

        try:
            self.serial = serial.Serial(self.USB_MEGA_ROBOT, self.BAUDRATE)
        except serial.SerialException as e:
            print(f"Error opening serial port: {e}")
            self.show_popup_err_arduino()






        self.uic.Button_close_event.clicked.connect(self.dong_cua_so)
        self.uic.start.clicked.connect(self.trang_bat_dau)
        self.uic.Button_hide.clicked.connect(self.minisize_window)
        self.uic.Button_done_2.setEnabled(False)
        self.uic.Home.clicked.connect(self.trang_home)
        self.uic.Camera.clicked.connect(self.show_camera)
        self.uic.Button_Quaylai_3.clicked.connect(self.quay_lai_cam)
        self.uic.Setting.clicked.connect(self.trang_setting)
        self.uic.Manual.clicked.connect(self.trang_robot)
        self.uic.Button_done_2.clicked.connect(self.check_id)
        self.uic.Button_add.clicked.connect(self.nhap_ten)
        self.uic.Button_khuvuccho_2.clicked.connect(self.ve_home)
        self.uic.Button_capnhat.clicked.connect(self.load_data_to_listwidget)




        self.item_added = [False] * 10 
        self.current_item_index = None

        self.uic.Button_1_2.clicked.connect(lambda checked: self.toggle_data_on_list(0))
        self.uic.Button_2_2.clicked.connect(lambda checked: self.toggle_data_on_list(1))
        self.uic.Button_3_2.clicked.connect(lambda checked: self.toggle_data_on_list(2))
        self.uic.Button_4_2.clicked.connect(lambda checked: self.toggle_data_on_list(3))
        self.uic.Button_5_2.clicked.connect(lambda checked: self.toggle_data_on_list(4))
        self.uic.Button_6_2.clicked.connect(lambda checked: self.toggle_data_on_list(5))
        self.uic.Button_7_2.clicked.connect(lambda checked: self.toggle_data_on_list(6))
        self.uic.Button_8_2.clicked.connect(lambda checked: self.toggle_data_on_list(7))
        self.uic.Button_9_2.clicked.connect(lambda checked: self.toggle_data_on_list(8))
        self.uic.Button_10_2.clicked.connect(lambda checked: self.toggle_data_on_list(9))
    def  start_thread(self):
         self.run_ros.start()

    def trang_home(self):
        self.uic.stackedWidget.setCurrentIndex(0)
    def quay_lai_cam(self):
        self.quay_lai()
        self.close_camera()
    def trang_setting(self):
        self.uic.stackedWidget.setCurrentIndex(1)
        self.uic.Button_Quaylai_5.clicked.connect(self.quay_lai)
        self.uic.update_setting.clicked.connect(self.update_setting)
        self.uic.Button_done_4.clicked.connect(self.save_setting)
        self.read_dwa_config()
        self.read_lower_threshold()
        self.list_arduino_ports()
    def update_setting(self):
        self.read_dwa_config()
        self.read_lower_threshold()


    def trang_robot(self):
        self.uic.stackedWidget.setCurrentIndex(5)
        self.uic.Button_Quaylai_4.clicked.connect(self.quay_lai)
        self.uic.forward.clicked.connect(self.cals_fk)
        self.uic.Inverse.clicked.connect(self.cals_ik)
        self.uic.Delete.clicked.connect(self.delete_text)
        self.uic.home.clicked.connect(self.home_robot)
        self.uic.Run.clicked.connect(self.run_robot)
        self.uic.Return_box.clicked.connect(self.return_box)
    def save_setting(self):
        self.done_save_setting()
        min_vel_x = self.uic.min_vel_x.text()
        max_vel_x = self.uic.max_vel_x.text()
        min_vel_theta = self.uic.min_vel_theta.text()
        max_vel_theta = self.uic.max_vel_theta.text()
        acc_lim_x = self.uic.acc_lim_x.text()
        acc_lim_theta = self.uic.acc_lim_theta.text()
        lower_threshold = self.uic.lower_threshold.text()
        self.modify_dwa_config(max_vel_x, min_vel_x, max_vel_theta, min_vel_theta, acc_lim_x, acc_lim_theta)
        self.update_lower_threshold(lower_threshold)
        # self.done_save_setting()

    def modify_dwa_config(self, max_vel_x, min_vel_x, max_vel_theta, min_vel_theta, acc_lim_x, acc_lim_theta):
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
        params = {
            'max_vel_x': max_vel_x,
            'min_vel_x': min_vel_x,
            'max_vel_theta': max_vel_theta,
            'min_vel_theta': min_vel_theta,
            'acc_lim_x': acc_lim_x,
            'acc_lim_theta': acc_lim_theta
        }
        with open(self.file_path, 'w') as file:
            for line in lines:
                modified = False  # Cờ kiểm tra xem dòng đã được sửa đổi chưa
                indent_level = len(line) - len(line.lstrip())
                indent = " " * indent_level
                for param, value in params.items():
                    if line.strip().startswith(f"{param}:"):
                        line = f"{indent}{param}: {value}\n"  # Thay thế dòng cũ bằng dòng mới
                        modified = True
                        break  # Ngừng tìm kiếm trong các tham số khi tìm thấy khớp
                file.write(line)
    def update_lower_threshold(self, new_value):
        with open(self.file_path_1, 'r') as file:
            lines = [f"    lower_threshold: {new_value}\n" if line.strip().startswith('lower_threshold:') else line for line in file]
        with open(self.file_path_1, 'w') as file:
            file.writelines(lines)

    def read_dwa_config(self):
        # Initialize dictionary with default values
        params = {
            'max_vel_x': 'max_vel_x',
            'min_vel_x': 'min_vel_x',
            'max_vel_theta': 'max_vel_theta',
            'min_vel_theta': 'min_vel_theta',
            'acc_lim_x': 'acc_lim_x',
            'acc_lim_theta': 'acc_lim_theta'
        }
        
        # Read the configuration file and update dictionary
        with open(self.file_path, 'r') as file:
            for line in file:
                for key in params:
                    if line.strip().startswith(f"{key}:"):
                        params[key] = float(line.split(":")[1].strip())
        
        # Assign values to UI elements
        for param, value in params.items():
            getattr(self.uic, param).setText(str(value))
    def read_lower_threshold(self):
        with open(self.file_path_1, 'r') as file:
            for line in file:
                if line.strip().startswith('lower_threshold:'):
                    lower_threshold = float(line.split(':')[1].strip())
                    # print(f"lower_threshold: {lower_threshold}")
                    self.uic.lower_threshold.setText(str(lower_threshold))
                    return
        # print("Không tìm thấy thông số lower_threshold.")

    def list_arduino_ports(self):
        # Lấy danh sách các cổng serial
        ports = serial.tools.list_ports.comports()
        arduino_ports = []

        # Tìm các cổng có khả năng là Arduino
        for port in ports:
            if (#"Arduino" in port.description or 
                #"CH340" in port.description or 
                #"USB-SERIAL" in port.description or 
                "ttyUSB" in port.device or 
                "ttyACM" in port.device):
                arduino_ports.append(port.device)

        # In ra danh sách các cổng Arduino tìm được
        if arduino_ports:
            # print("Các cổng Arduino được tìm thấy:")
            for port in arduino_ports:
                # print(port)  # In ra tên cổng như '/dev/ttyUSB1'
                # Hiển thị cổng lên widget_9 nếu nó là QLabel hoặc QLineEdit
                self.uic.port_usb.setText(arduino_ports[1])  # Đặt giá trị cổng vào widget
        else:
            print("Không tìm thấy cổng Arduino nào.")
            self.uic.port_usb.setText("Không tìm thấy cổng Arduino")





        



        


    def dong_cua_so(self):
        self.close()
        self.exit()
    def minisize_window(self):
        self.showMinimized()
    def trang_bat_dau(self):
        # self.run_roscore()
        self.uic.stackedWidget.setCurrentIndex(7)
        self.uic.Button_Manu_2.clicked.connect(self.trang_manual)
        self.uic.Button_Auto_2.clicked.connect(self.trang_auto)
        self.uic.Button_Quaylai_2.clicked.connect(self.quay_lai)

    def quay_lai(self):
        self.uic.stackedWidget.setCurrentIndex(7)
    def ve_home(self):
        self.start_dichuyen(200)
        self.trang_xacnhan(text1= "HOME")


    def trang_auto(self):
        self.uic.stackedWidget.setCurrentIndex(2)
        # source_ros_command = "source /opt/ros/noetic/setup.bash && roslaunch navigation_bot openmap.launch"
        # subprocess.Popen(source_ros_command, shell=True, executable='/bin/bash', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        # os.system('gnome-terminal -- roslaunch navigation_bot openmap.launch')
        self.navigation_thread.start()
        self.uic.Button_Quaylai.clicked.connect(self.quay_lai)
        self.show_button()
        self.uic.Button_LoadMap.clicked.connect(self.load_map)
        


        self.item_added = [False] * 10  
        self.data = [f"Điểm đến {i+1}" for i in range(10)]  


    def load_map(self):
         # Lệnh ROS cần chạy
        command = "gnome-terminal -- bash -c 'source /opt/ros/noetic/setup.bash && source ~/catkin_ws/devel/setup.bash && roslaunch navigation_bot openmap.launch'"
        subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def show_button(self):
        # all_id = self.nhandulieu_mysql_id()  # Fetch IDs from the database
        buttons = [
            self.uic.Button_1_2, self.uic.Button_2_2, self.uic.Button_3_2,
            self.uic.Button_4_2, self.uic.Button_5_2, self.uic.Button_6_2,
            self.uic.Button_7_2, self.uic.Button_8_2, self.uic.Button_9_2,
            self.uic.Button_10_2
        ]

        # Initially hide all buttons
        for button in buttons:
            button.setVisible(False)

        idbans = self.nhandulieu_mysql_id() 
        # self.uic.listWidget_dsban.clear()  
        for idban in idbans:
            idban_int = int(idban)
            if 1 <= idban_int <= 10:  # Giới hạn từ 1 đến 10
                button_index = idban_int - 1  # Calculate the index for the button list
                button = buttons[button_index]
                button.setVisible(True)  # Show the button
                # item = QListWidgetItem(f"Điểm đến {idban_int}")////////////////////
                # item.setTextAlignment(Qt.AlignCenter)  # Căn giữa văn bản của mỗi mục
                # self.uic.listWidget_dsban.addItem(item)  # Thêm mục vào ListWidget
                # button.setVisible(True)



    def trang_manual(self):
        self.uic.stackedWidget.setCurrentIndex(6)
        self.uic.Button_Quaylai_2.clicked.connect(self.quay_lai)
        self.uic.Button_luuMap.clicked.connect(self.trang_save_map)
        self.load_data_to_listwidget()
        self.uic.Button_xoa.clicked.connect(self.xoa_du_lieu_da_chon)
    def trang_save_map(self):
        # self.save_map()
        self.uic.stackedWidget.setCurrentIndex(4)
        self.uic.Button_Quaylai_6.clicked.connect(self.trang_manual)
        
        # time.sleep(1)
        self.show_map()
        # self.uic.Button_huy.clicked.connect(self.save_map)

    def toggle_data_on_list(self, index):
            if self.item_added[index]:
                # Nếu mục đã được thêm, xóa mục khỏi QListWidget
                items = self.uic.listWidget_ds.findItems(self.data[index], QtCore.Qt.MatchExactly)
                if items:
                    for item in items:
                        self.uic.listWidget_ds.takeItem(self.uic.listWidget_ds.row(item))
                self.item_added[index] = False  
            else:
                self.uic.listWidget_ds.addItem(self.data[index])
                self.item_added[index] = True  
            self.update_ds()

    def update_ds(self):
        if 0 < self.uic.listWidget_ds.count()<=3:
            self.uic.Button_done_2.setEnabled(True)
        else:
            self.uic.Button_done_2.setEnabled(False)
    def show_camera(self):
        self.uic.stackedWidget.setCurrentIndex(8)  # Chuyển đến giao diện màn hình camera
        self.capture = cv2.VideoCapture(0)  # Mở camera

        # Khởi tạo timer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_frame)  # Kết nối với phương thức cập nhật khung hình
        self.timer.start(20)  # Bắt đầu timer với tần suất 20ms

    def update_frame(self):
        ret, frame = self.capture.read()  # Đọc khung hình từ camera
        if ret:
            # Chuyển đổi màu BGR sang RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Chuyển đổi numpy array thành QImage
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            q_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)

            # Hiển thị lên QLabel
            pixmap = QPixmap.fromImage(q_image)

            # Kéo dài pixmap để phù hợp với kích thước QLabel mà không giữ tỉ lệ khung hình
            self.uic.screen_cam_2.setPixmap(pixmap.scaled(self.uic.screen_cam_2.size(), QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation))
            self.uic.screen_cam.setPixmap(pixmap.scaled(self.uic.screen_cam.size(), QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation))
        else:
            pass
            # print("Không thể lấy khung hình từ camera")
    def close_camera(self):
        if hasattr(self, 'capture'):
            self.capture.release()  # Giải phóng camera
            self.capture = None  # Đặt lại biến capture
        if hasattr(self, 'timer'):
            self.timer.stop()  # Dừng timer
    def nhandulieu_mysql(self, idban):
        select_query = 'SELECT * FROM robot WHERE `Id` = %s LIMIT 0, 1'  
        mycursor = db.cursor()
        mycursor.execute(select_query, (idban,))
        result = mycursor.fetchone()  
        if result:
            return result[0:4]
        else:
            return None
    # def check_id(self):
    #     self.data_1 = {
    #     "Điểm đến 1": 1,
    #     "Điểm đến 2": 2,
    #     "Điểm đến 3": 3,
    #     "Điểm đến 4": 4,
    #     "Điểm đến 5": 5,
    #     "Điểm đến 6": 6,
    #     "Điểm đến 7": 7,
    #     "Điểm đến 8": 8,
    #     "Điểm đến 9": 9,
    #     "Điểm đến 10": 10,
    # }
    #     # Lấy tất cả các mục trong listWidget_ds
    #     all_items = [self.uic.listWidget_ds.item(i).text() for i in range(self.uic.listWidget_ds.count())]
    #     for item_text in all_items:
    #         idban = self.data_1.get(item_text)
    #         if idban is not None:
    #             stt1 = idban[0]
    #             stt2  = idban[1]
    #             stt3 = idban[0]
    #             # self.start_dichuyen(idban) 
    #             # self.selected_goal_ids.append(idban)
    #             self.start_dichuyen(idban)
    #         else:
    #             print(f"  {item_text} không có ID tương ứng")
    def check_id(self):
        self.data_1 = {
            "Điểm đến 1": 1,
            "Điểm đến 2": 2,
            "Điểm đến 3": 3,
            "Điểm đến 4": 4,
            "Điểm đến 5": 5,
            "Điểm đến 6": 6,
            "Điểm đến 7": 7,
            "Điểm đến 8": 8,
            "Điểm đến 9": 9,
            "Điểm đến 10": 10,
        }
        
        # Get all items from the listWidget_ds
        all_items = [self.uic.listWidget_ds.item(i).text() for i in range(self.uic.listWidget_ds.count())]
        
        selected_ids = []  # List to hold selected IDs


        for item_text in all_items:
            idban = self.data_1.get(item_text)
            if idban is not None:
                selected_ids.append(idban)  # Collecting valid IDs
                # self.start_dichuyen(idban)   # Perform your action
            else:
                print(f"{item_text} không có ID tương ứng")

        # Assigning to stt variables based on the count of selected_ids
        if len(selected_ids) >= 3:
            stt1, stt2, stt3 = selected_ids[0], selected_ids[1], selected_ids[2]
            print('3diem')
            text1 = all_items[0]
            text2 = all_items[1]
            text3 = all_items[2]
            self.trang_xacnhan(text1)
            self.start_dichuyen_3diem(stt1, stt2, stt3, text2, text3)
        elif len(selected_ids) == 2:
            # global stt1
            stt1, stt2 = selected_ids[0], selected_ids[1]
            stt3 = None  # or some default value
            print('2diem')
            text1 = all_items[0]
            text2 = all_items[1]
            self.trang_xacnhan(text1)
            self.start_dichuyen_2diem(stt1, stt2, text2)
            
        elif len(selected_ids) == 1:
            print('1diem')
            stt1 = selected_ids[0]
            stt2 = None  # or some default value
            stt3 = None  # or some default value
            text1 = all_items[0]
            self.trang_xacnhan(text1)
            self.start_dichuyen_1diem(stt1)
            
        
        else:
            stt1 = stt2 = stt3 = None  # or some default values if no IDs selected

        # Optionally do something with stt1, stt2, stt3 here

    def start_dichuyen(self,idban):
        x_goal, y_goal, z_goal, w_goal = self.get_goal(idban)
        self.navigation_thread.send_goal(x_goal=x_goal, y_goal=y_goal, z_goal=z_goal, w_goal=w_goal)
        # self.navigation_thread.quatrinh_move = True
        self.navigation_thread.send_data_goal(x_goal, y_goal, z_goal, w_goal)
        self.navigation_thread.quatrinh_dichuyen = True
        self.navigation_thread.quatrinh_dichuyen_2diem = False
        self.navigation_thread.quatrinh_dichuyen_3diem = False
    def start_dichuyen_1diem(self, stt1):
        self.stt1 = stt1
        x_goal, y_goal, z_goal, w_goal = self.get_goal(stt1)
        self.navigation_thread.send_goal(x_goal=x_goal, y_goal=y_goal, z_goal=z_goal, w_goal=w_goal)
        # self.navigation_thread.quatrinh_move = True
        self.navigation_thread.send_data_goal(x_goal, y_goal, z_goal, w_goal)
        self.navigation_thread.quatrinh_dichuyen_1diem = True

    def start_dichuyen_2diem(self, stt1, stt2, text2):
        self.stt1 = stt1
        self.stt2 = stt2
        self.text2 = text2
        x_goal, y_goal, z_goal, w_goal = self.get_goal(stt1)
        self.navigation_thread.send_goal(x_goal=x_goal, y_goal=y_goal, z_goal=z_goal, w_goal=w_goal)
        # self.navigation_thread.quatrinh_move = True
        self.navigation_thread.send_data_goal(x_goal, y_goal, z_goal, w_goal)
        self.navigation_thread.quatrinh_dichuyen =  False
        self.navigation_thread.quatrinh_dichuyen_2diem = True
        self.navigation_thread.quatrinh_dichuyen_3diem = False
        self.navigation_thread.quatrinh_dichuyen_2diem_1 = True
        self.navigation_thread.quatrinh_dichuyen_2diem_2 = False
    def update_2diem(self, flag):
        # global stt2
        # print("dao vao roi nha")
        # print(flag)
        # print(self.stt2)
        status=0
        if flag == 111 and self.stt2 is not None:
            # print("================OKE=================")
            # if status == 0:

            x_err, y_err, z_rr, w_err = self.get_goal(self.stt1)
            quaternion1 = (0, 0, z_rr, w_err)
            print(quaternion1)
            self.yaw_goal_controller(quaternion1, x_goal=x_err)
            print("........")
        #     status =1
        # elif status == 1:
            self.trang_xacnhan(self.text2)
            x_goal, y_goal, z_goal, w_goal = self.get_goal(self.stt2)
            self.navigation_thread.send_goal(x_goal=x_goal, y_goal=y_goal, z_goal=z_goal, w_goal=w_goal)
            self.navigation_thread.send_data_goal(x_goal, y_goal, z_goal, w_goal)
            # print('oke............')
            self.navigation_thread.quatrinh_dichuyen =  False
            self.navigation_thread.quatrinh_dichuyen_2diem = True
            self.navigation_thread.quatrinh_dichuyen_3diem = False
            self.navigation_thread.quatrinh_dichuyen_2diem_2 = True
            self.navigation_thread.quatrinh_dichuyen_2diem_1 = False
        elif flag == 222:
            # self.quaternion1 = self.stt2
            # self.yaw_goal_controller(quaternion1 = self.stt2)
            x_err, y_err, z_rr, w_err = self.get_goal(self.stt2)
            quaternion1 = (0, 0, z_rr, w_err)
            print(quaternion1)
            self.yaw_goal_controller(quaternion1, x_goal=x_err)
            print("........")
            self.start_dichuyen(200)
            self.trang_xacnhan(text1 = "HOME")
            # self.uic.stackedWidget.setCurrentIndex(2)
    def start_dichuyen_3diem(self, stt1, stt2, stt3, text2, text3):
        self.stt1 = stt1
        self.stt2 = stt2
        self.stt3 = stt3
        self.text2 = text2
        self.text3 = text3
        x_goal, y_goal, z_goal, w_goal = self.get_goal(stt1)
        self.navigation_thread.send_goal(x_goal=x_goal, y_goal=y_goal, z_goal=z_goal, w_goal=w_goal)
        # self.navigation_thread.quatrinh_move = True
        self.navigation_thread.send_data_goal(x_goal, y_goal, z_goal, w_goal)
        self.navigation_thread.quatrinh_dichuyen =  False
        self.navigation_thread.quatrinh_dichuyen_3diem = True
        self.navigation_thread.quatrinh_dichuyen_3diem_1 = True
        self.navigation_thread.quatrinh_dichuyen_3diem_2 = False
        self.navigation_thread.quatrinh_dichuyen_3diem_3 = False
    def update_3diem(self, flag1):
        if flag1 == 111 and  self.stt2 is not None:
            x_err, y_err, z_rr, w_err = self.get_goal(self.stt1)
            quaternion1 = (0, 0, z_rr, w_err)
            print(quaternion1)
            self.yaw_goal_controller(quaternion1, x_goal=x_err)
            print("........")
            self.trang_xacnhan(self.text2)
            x_goal, y_goal, z_goal, w_goal = self.get_goal(self.stt2)
            self.navigation_thread.send_goal(x_goal=x_goal, y_goal=y_goal, z_goal=z_goal, w_goal=w_goal)
            self.navigation_thread.send_data_goal(x_goal, y_goal, z_goal, w_goal)
            self.navigation_thread.quatrinh_dichuyen =  False
            self.navigation_thread.quatrinh_dichuyen_2diem = False
            self.navigation_thread.quatrinh_dichuyen_3diem = True
            self.navigation_thread.quatrinh_dichuyen_3diem_1 = False
            self.navigation_thread.quatrinh_dichuyen_3diem_2 = True
            self.navigation_thread.quatrinh_dichuyen_3diem_3 = False
        elif flag1 == 222 and self.stt3 is not None:
            x_err, y_err, z_rr, w_err = self.get_goal(self.stt2)
            quaternion1 = (0, 0, z_rr, w_err)
            print(quaternion1)
            self.yaw_goal_controller(quaternion1, x_goal=x_err)
            print("........")
            self.trang_xacnhan(self.text3)
            x_goal, y_goal, z_goal, w_goal = self.get_goal(self.stt3)
            self.navigation_thread.send_goal(x_goal=x_goal, y_goal=y_goal, z_goal=z_goal, w_goal=w_goal)
            self.navigation_thread.send_data_goal(x_goal, y_goal, z_goal, w_goal)
            self.navigation_thread.quatrinh_dichuyen =  False
            self.navigation_thread.quatrinh_dichuyen_2diem = False
            self.navigation_thread.quatrinh_dichuyen_3diem = True
            self.navigation_thread.quatrinh_dichuyen_3diem_1 = False
            self.navigation_thread.quatrinh_dichuyen_3diem_2 = False
            self.navigation_thread.quatrinh_dichuyen_3diem_3 = True
        elif flag1 == 333:
            x_err, y_err, z_rr, w_err = self.get_goal(self.stt3)
            quaternion1 = (0, 0, z_rr, w_err)
            print(quaternion1)
            self.yaw_goal_controller(quaternion1, x_goal=x_err)
            print("........")
            self.start_dichuyen(200)
            self.trang_xacnhan(text1 = "HOME")
            # self.uic.stackedWidget.setCurrentIndex(2)
    def get_goal(self, idban):
    # Fetch goal coordinates from the database
        data_vitri = self.nhandulieu_mysql(idban)
        return map(lambda x: float(x.strip("'")), data_vitri)
    def trang_xacnhan(self, text1):
        self.uic.stackedWidget.setCurrentIndex(3)
        self.uic.label_final.setText(text1)
    def update_1diem(self, flag2):
        if flag2 == 111:
            x_err, y_err, z_rr, w_err = self.get_goal(self.stt1)
            quaternion1 = (0, 0, z_rr, w_err)
            print(quaternion1)
            self.yaw_goal_controller(quaternion1, x_goal=x_err)
            print("........")
            self.start_dichuyen(200)
            self.trang_xacnhan(text1 = "HOME")
            # self.uic.stackedWidget.setCurrentIndex(2)
    def done_dichuyen(self, flag3):
        if flag3 == 111:
            # x_err, y_err, z_rr, w_err = self.get_goal(self.stt2)
            x_goal = 0
            quaternion1 = (0, 0, 0, 1)
            print(quaternion1)
            self.yaw_goal_controller(quaternion1,x_goal)
            print("........")
            self.show_popup_done_dichuyen()
            # self.uic.stackedWidget.setCurrentIndex(2)



        # self.start_dichuyen(stt2)
    # def start_dichuyen_3diem(self, stt1, stt2, stt3):
    #     pass
        # self.start_dichuyen(stt1)
    

    # def on_goal_reached(self):
    #     # print('da vaoooooooooooo')
    #     # Tăng chỉ số điểm đến và gửi điểm tiếp theo
    #     items = [self.uic.listWidget_ds.item(index).text() for index in
    #             range(self.uic.listWidget_ds.count())]
    #     if items and self.current_item_index < len(items):
    #         self.current_item_index += 1
    #         if self.current_item_index < len(items):
    #             next_item = items[self.current_item_index]
    #             if self.current_item_index == 1:
    #                 if next_item == 'Home':
    #                     data_vitri = self.nhandulieu_mysql(200)
    #                     x_goal, y_goal, z_goal, w_goal = map(lambda x: float(x.strip("'")), data_vitri)
    #                     self.navigation_thread.send_goal(x_goal=x_goal, y_goal=y_goal, z_goal=z_goal, w_goal=w_goal)
    #                     self.navigation_thread.quatrinh_dichuyen = True
    #                     self.navigation_thread.send_data_goal(x_goal, y_goal, z_goal, w_goal)
    #                 else:
    #                     self.data_send_sql = self.nhandulieu_mysql[self.stt2]
    #                     x_goal, y_goal, z_goal, w_goal = map(lambda x: float(x.strip("'")), self.data_send_sql)
        
        # if self.current_goal_index < len(self.selected_goal_ids):
        #     next_goal_id = self.selected_goal_ids[self.current_goal_index]
        #     print(f"Đã đến điểm thứ {self.current_goal_index}, tiếp tục gửi điểm tiếp theo.")
        #     self.start_dichuyen(next_goal_id)
        # else:
        #     print("Tất cả các điểm đến đã được hoàn thành.")
    # def update_vitri(self,flag):
    #     pass
        # print('da vao')
        # Được gọi liên tục để kiểm tra nếu robot đã đạt đến điểm đến hiện tại
        # if flag():
        # self.on_goal_reached()



    def nhandulieu_mysql_id(self):
        select_query = 'SELECT Id FROM robot'  # Lấy tất cả IDban
        mycursor = db.cursor()
        mycursor.execute(select_query)
        results = mycursor.fetchall()  # Lấy tất cả kết quả
        return [row[0] for row in results]  # Chỉ lấy IDban

    def load_data_to_listwidget(self):
        idbans = self.nhandulieu_mysql_id() 
        self.uic.listWidget_dsban.clear()  
        for idban in idbans:
            idban_int = int(idban)
            if 1 <= idban_int <= 10:  # Giới hạn từ 1 đến 10
                item = QListWidgetItem(f"Điểm đến {idban_int}")
                item.setTextAlignment(Qt.AlignCenter)  # Căn giữa văn bản của mỗi mục
                self.uic.listWidget_dsban.addItem(item)  # Thêm mục vào ListWidget
    # def xoa_du_lieu_da_chon(self):
    #     selected_items = self.uic.listWidget_dsban.selectedItems()  # Lấy các mục đã chọn 
    #     if not selected_items:
    #         # print("Không có mục nào được chọn để xóa.")
    #         return
    #     for item in selected_items:
    #         row = self.uic.listWidget_dsban.row(item)  # Lấy chỉ số của mục đã chọn
    #         self.uic.listWidget_dsban.takeItem(row)  # Xóa mục khỏi listWidget_dsban
    #         # print(f"Đã xóa: {item.text()}") 
    #     self.delete_values(id)

    def xoa_du_lieu_da_chon(self):
        selected_items = self.uic.listWidget_dsban.selectedItems()
        if not selected_items:
            return  # Không có mục nào được chọn

        for item in selected_items:
            id_text = item.text()
            match = re.search(r'\d+', id_text)

            if match:
                id = match.group()
                # print(id)
                self.delete_values(id)  # Xóa bản ghi trong cơ sở dữ liệu theo ID
                row = self.uic.listWidget_dsban.row(item)
                self.uic.listWidget_dsban.takeItem(row)  # Xóa mục khỏi listWidget_dsban
            else: pass



###############################################################
###############################################################

    def exit(self):
        os.system('gnome-terminal -- bash -c "pkill gnome-terminal"')
        print("kill terminal")
    def save_map(self):
        os.system(
            f'gnome-terminal -- bash -c "cd {self.map_folder_path} && rosrun map_server map_saver -f mymap2 map:=/slamware_ros_sdk_server_node/map"')


################################################################################
################################################################################
    # def map_callback(self, data):
    #     # Nhận dữ liệu bản đồ từ topic
    #     self.map_data = data
    #     self.display_map(data)

    # def display_map(self, map_data):
    #     # Lấy kích thước của bản đồ
    #     width = map_data.info.width
    #     height = map_data.info.height

    #     # Chuyển đổi dữ liệu bản đồ thành mảng numpy
    #     map_array = np.array(map_data.data).reshape((height, width))

    #     # Chuyển đổi giá trị map (-1, 0, 100) thành màu để hiển thị
    #     map_image = np.zeros((height, width, 3), dtype=np.uint8)
    #     map_image[map_array == -1] = [128, 128, 128]  # Ô chưa biết: màu xám
    #     map_image[map_array == 0] = [255, 255, 255]   # Ô trống: màu trắng
    #     map_image[map_array == 100] = [0, 0, 0]       # Ô chiếm dụng: màu đen

    #     # Chuyển đổi mảng numpy thành QImage
    #     h, w, ch = map_image.shape
    #     bytes_per_line = ch * w
    #     q_image = QImage(map_image.data, w, h, bytes_per_line, QImage.Format_RGB888)

    #     # Hiển thị hình ảnh lên QLabel (self.uic.screen_cam_3)
    #     pixmap = QPixmap.fromImage(q_image)

    #     # Đặt pixmap vào QLabel và điều chỉnh kích thước để đầy đủ màn hình
    #     self.uic.screen_cam_3.setPixmap(pixmap.scaled(self.uic.screen_cam_3.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
    #     self.uic.screen_cam_3.setAlignment(Qt.AlignCenter)
    #     self.uic.screen_cam_3.show()



    ##################################POPUP###################################33
    #===========================================================================
    def done_save_setting(self):
        self.form_save = QMainWindow()
        self.uic2 = Ui_Form_save_setting()
        self.uic2.setupUi(self.form_save)

        # self.form_them.setGeometry(160, 140, 750, 550)
        self.form_save.setGeometry(750, 350, 500, 201)
        self.form_save.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.form_save.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.form_save.show()
        # self.uic2.frame.setStyleSheet("""
        # QFrame {
        #     border-radius: 10px;           /* Bo tròn các góc */
        # }
        # """)
        QTimer.singleShot(1000, self.form_save.close)
    def show_popup_dichuyen(self):
        self.form_dichuyen = MainWindow()
        self.uic3 = Ui_Form_dichuyen()
        self.uic3.setupUi(self.form_save)
        self.form_dichuyen.setGeometry(750, 350, 540, 230)
        self.form_dichuyen.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.form_dichuyen.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.form_dichuyen.show()
    def show_popup_done_dichuyen(self):
        self.form_done_dichuyen = MainWindow()
        self.uic4 = Ui_Form_done_dichuyen()
        self.uic4.setupUi(self.form_done_dichuyen)
        self.form_done_dichuyen.setGeometry(750, 350, 540, 230)
        self.form_done_dichuyen.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.form_done_dichuyen.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.form_done_dichuyen.show()
        QTimer.singleShot(2000, self.form_done_dichuyen.close)
        self.uic.stackedWidget.setCurrentIndex(2)
    def show_popup_emergency(self):
        self.form_emergency = MainWindow()
        self.uic5 = Ui_Form_emergency()
        self.uic5.setupUi(self.form_done_dichuyen)
        self.form_emergency.setGeometry(750, 350, 521, 291)
        self.form_emergency.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.form_emergency.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.form_emergency.show()
        # QTimer.singleShot(2000, self.form_done_dichuyen.close)
    def show_popup_err_dh(self):
        self.form_err_dh = MainWindow()
        self.uic6 = Ui_Form_err_dh()
        self.uic6.setupUi(self.form_err_dh)
        self.form_err_dh.setGeometry(750, 350, 500, 201)
        self.form_err_dh.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.form_err_dh.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.form_err_dh.show()
        QTimer.singleShot(1500, self.form_err_dh.close)
    def show_popup_err_arduino(self):
        self.form_err_arduino = MainWindow()
        self.uic6 = Ui_Form_err_arduino()
        self.uic6.setupUi(self.form_err_arduino)
        self.form_err_arduino.setGeometry(750, 350, 500, 201)
        self.form_err_arduino.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.form_err_arduino.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.form_err_arduino.show()
        QTimer.singleShot(1500, self.form_err_arduino.close)
    def show_popup_err_send_robot(self):
        self.form_err_send_robot = MainWindow()
        self.uic6 = Ui_Form_err_send_robot()
        self.uic6.setupUi(self.form_err_send_robot)
        self.form_err_send_robot.setGeometry(750, 350, 500, 201)
        self.form_err_send_robot.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.form_err_send_robot.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.form_err_send_robot.show()
        QTimer.singleShot(1500, self.form_err_send_robot.close)


    ############################################################################################
    #==========================================================================================#
    def nhap_ten(self):
        self.form_them = QMainWindow()
        self.uic1 = Ui_Form_nhaptenban()
        self.uic1.setupUi(self.form_them)

        # self.form_them.setGeometry(160, 140, 750, 550)
        self.form_them.setGeometry(700, 350, 521, 291)
        self.form_them.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.form_them.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.form_them.show()
        self.uic1.Button_huy_capnhat.clicked.connect(self.close_capnhat)
        self.uic1.Button_xacnhan_capnhat.clicked.connect(self.done_capnhat)
    def close_capnhat(self):
        self.form_them.close()
    # def done_capnhat(self):
    #     self.get_odometry_once()
    #     self.form_them.close()
        
    #     # self.navigation_thread.send_odem()
    #     # x, y, z, w =  self.data_odem 
    #     # id = self.uic1.lineEdit_nhaptenban.text()
    #     # self.save_values(x, y, z, w, id)
        
    # def get_odometry_once(self):
    #     current_position = None
    #     def odometry_callback(msg):
    #         nonlocal current_position
    #         # id = self.uic1.lineEdit_nhaptenban.text()  # Lấy Id từ giao diện
    #         x = msg.pose.pose.position.x
    #         y = msg.pose.pose.position.y
    #         z = msg.pose.pose.orientation.z
    #         w = msg.pose.pose.orientation.w  # Hoặc các thành phần khác nếu cần

    #         current_position = (x, y, z, w)

    #         # self.save_values(x, y, z, w, id)
    #     rospy.Subscriber("/slamware_ros_sdk_server_node/odom", Odometry, odometry_callback)
    #     rospy.sleep(1)
    #     if current_position:
    #         id = self.uic1.lineEdit_nhaptenban.text()
    #         # print(f"Final Position -> x: {current_position[0]}, y: {current_position[1]}, z: {current_position[2]}, w: {current_position[3]}")
    #         self.save_values(current_position[0], current_position[1], current_position[2], current_position[3], id)
    #     else:
    #         # print("No odometry data received.")  
    #         pass

    #     rospy.signal_shutdown("Finished retrieving odometry data.")

    # def save_values(self, x, y, z, w, id):
    #     try:
    #         db.cursor().execute(
    #             "INSERT INTO robot (X, Y, Z, W, Id) VALUES (%s, %s, %s, %s, %s)", 
    #             (float(x), float(y), float(z), float(w), int(id))
    #         )
    #         db.commit()
    #     except mysql.connector.Error:
    #         db.rollback()
    def done_capnhat(self):
        self.get_odometry_once()
        self.form_them.close()

    def get_odometry_once(self):
        current_position = None

        # Callback để xử lý dữ liệu odometry
        def odometry_callback(msg):
            nonlocal current_position
            x = msg.pose.pose.position.x
            y = msg.pose.pose.position.y
            z = msg.pose.pose.orientation.z
            w = msg.pose.pose.orientation.w
            current_position = (x, y, z, w)

        # Đăng ký Subscriber để nhận dữ liệu từ topic odometry
        rospy.Subscriber("/slamware_ros_sdk_server_node/odom", Odometry, odometry_callback)
        rospy.sleep(1)

        # Nếu nhận được dữ liệu thì xử lý tiếp
        if current_position:
            id = self.uic1.lineEdit_nhaptenban.text()
            x, y, z, w = current_position
            # print(f"Position -> x: {x}, y: {y}, z: {z}, w: {w}")
            self.save_values(x, y, z, w, id)  # Gọi hàm lưu nếu cần
        else:
            print("Không nhận được dữ liệu odometry.")





    # def yaw_goal_controller(self, quaternion1):
    #     print(".......................ErrOdemGoal...............................")
    #     # rospy.init_node('yaw_goal_controller', anonymous=True)

    #     # Biến toàn cục
    #     daquayxong = False
    #     robot_yaw_goal_degree = 0  # Góc mục tiêu
    #     robot_yaw_degree = 0      # Góc hiện tại

    #     # Publisher cho /cmd_vel
    #     pub_twist = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    #     # rospy.Subscriber('/slamware_ros_sdk_server_node/odom', Odometry, odom_callback)

    #     # Callback xử lý dữ liệu từ /odom
    #     def odom_callback(data):
    #         nonlocal daquayxong, robot_yaw_goal_degree, robot_yaw_degree

            # # Lấy dữ liệu quaternion từ /odom
            # quaternion = (
            #     data.pose.pose.orientation.x,
            #     data.pose.pose.orientation.y,
            #     data.pose.pose.orientation.z,
            #     data.pose.pose.orientation.w
            # )
            # # print(quaternion)
            
            # # Chuyển đổi từ quaternion sang góc Euler
            # _, _, robot_yaw = euler_from_quaternion(quaternion)
            # robot_yaw_degree = np.degrees(robot_yaw)

            # # Góc mục tiêu (sửa quaternion1 nếu cần)
            # # quaternion1 = (0, 0, 0, 1)  # Thay đổi góc mục tiêu nếu cần
            # _, _, robot_yaw_goal = euler_from_quaternion(quaternion1)
            # robot_yaw_goal_degree = np.degrees(robot_yaw_goal)

            # # Tính toán sai số và chuẩn hóa về [-180, 180]
            # error = robot_yaw_goal_degree - robot_yaw_degree
            # error = (error + 180) % 360 - 180

            # # Điều khiển robot
            # twist_msg = Twist()
            # if not daquayxong:
            #     if abs(error) > 0.2:  # Nếu lỗi lớn hơn ngưỡng
            #         twist_msg.angular.z = 0.4 if error > 0 else -0.4
        #             pub_twist.publish(twist_msg)
        #             rospy.loginfo(f"Đang xoay: Lỗi {error:.2f}°")
        #         else:
        #             twist_msg.angular.z = 0
        #             pub_twist.publish(twist_msg)
        #             rospy.loginfo(f"Đã đạt góc mục tiêu! Góc hiện tại: {robot_yaw_degree:.2f}°")
        #             rospy.loginfo(f"ERROR hiện tại: {error:.2f}°")
        #             daquayxong = True
        #             # rospy.signal_shutdown("Hoàn thành nhiệm vụ")
        #             # Subscriber.unregister()
        #             # rospy.loginfo("Hoàn thành nhiệm vụ, đã dừng lắng nghe từ /odom.")

        # # Subscriber lắng nghe từ /odom
        # rospy.Subscriber('/slamware_ros_sdk_server_node/odom', Odometry, odom_callback)

        # # rospy.loginfo("Node đã khởi chạy!")

        # # rospy.spin()
        # while not daquayxong:
        #     rospy.sleep(0.1)  # Chờ một chút trước khi kiểm tra lại
        #     print("Đã hoàn thành việc quay, tiếp tục các tác vụ khác.")

        

    def yaw_goal_controller(self, quaternion1, x_goal):
        print(".......................ErrOdemGoal...............................")
        
        # Biến toàn cục
        daquayxong = False
        datientoi = True
        robot_yaw_goal_degree = 0  # Góc mục tiêu
        robot_yaw_degree = 0      # Góc hiện tại

        # Publisher cho /cmd_vel
        pub_twist = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        # Callback xử lý dữ liệu từ /odom
        def odom_callback(data):
            nonlocal daquayxong, robot_yaw_goal_degree, robot_yaw_degree, datientoi

            # Lấy dữ liệu quaternion từ /odom
            x_odem = data.pose.pose.position.x
            # y_odem = data.pose.pose.position.y
            
            
            quaternion = (
                data.pose.pose.orientation.x,
                data.pose.pose.orientation.y,
                data.pose.pose.orientation.z,
                data.pose.pose.orientation.w
            )
            
            # Chuyển đổi từ quaternion sang góc Euler
            _, _, robot_yaw = euler_from_quaternion(quaternion)
            robot_yaw_degree = np.degrees(robot_yaw)

            # Góc mục tiêu (sửa quaternion1 nếu cần)
            _, _, robot_yaw_goal = euler_from_quaternion(quaternion1)
            robot_yaw_goal_degree = np.degrees(robot_yaw_goal)

            # Tính toán sai số và chuẩn hóa về [-180, 180]
            error_yaw = robot_yaw_goal_degree - robot_yaw_degree
            error_yaw = (error_yaw + 180) % 360 - 180
            error_x = x_odem - x_goal
            # print(f'{x_odem}, {x_goal}, {error_x}')

            # Điều khiển robot
            twist_msg = Twist()
            
            # Xoay đến góc mục tiêu
            if not daquayxong:
                if abs(error_yaw) > 0.2:  # Nếu lỗi lớn hơn ngưỡng
                    twist_msg.angular.z = 0.4 if error_yaw > 0 else -0.4
                    pub_twist.publish(twist_msg)
                    # rospy.loginfo(f"Đang xoay: Lỗi {error_yaw:.2f}°")
                else:
                    twist_msg.angular.z = 0
                    pub_twist.publish(twist_msg)
                    rospy.loginfo(f"Đã đạt góc mục tiêu! Lỗi góc hiện tại: {error_yaw:.2f}°")
                    daquayxong = True  # Đã quay xong, chuyển sang di chuyển

            # Di chuyển tới vị trí mục tiêu
            if daquayxong and datientoi:
                if x_odem < x_goal:
                    if abs(error_x) > 0.03:  # Nếu lỗi lớn hơn ngưỡng
                        twist_msg.linear.x = +0.2 if error_x > 0 else -0.2
                        pub_twist.publish(twist_msg)
                        rospy.loginfo(f"Đang di chuyển: Lỗi X hiện tại {error_x:.2f}m")
                    else:
                        twist_msg.linear.x = 0
                        pub_twist.publish(twist_msg)
                        rospy.loginfo(f"Đã đạt vị trí mục tiêu: Lỗi X hiện tại {error_x:.2f}m")
                        datientoi = False  # Đã di chuyển đến vị trí mục tiêu
                else: 
                    if abs(error_x) > 0.05:  # Nếu lỗi lớn hơn ngưỡng
                        twist_msg.linear.x = -0.2 if error_x > 0 else 0.2
                        pub_twist.publish(twist_msg)
                        rospy.loginfo(f"Đang di chuyển: Lỗi X hiện tại {error_x:.2f}m")
                    else:
                        twist_msg.linear.x = 0
                        pub_twist.publish(twist_msg)
                        rospy.loginfo(f"Đã đạt vị trí mục tiêu: Lỗi X hiện tại {error_x:.2f}m")
                        datientoi = False  # Đã di chuyển đến vị trí mục tiêu

        # Subscriber lắng nghe từ /odom
        rospy.Subscriber('/slamware_ros_sdk_server_node/odom', Odometry, odom_callback)

        while not (daquayxong and not datientoi):
            rospy.sleep(0.1)  # Chờ một chút trước khi kiểm tra lại
            # print("Đang tiếp tục kiểm tra trạng thái di chuyển...")
        
        print("Hoàn thành nhiệm vụ.")






    def save_values(self, x, y, z, w, id):
        try:
            db.cursor().execute(
                "INSERT INTO robot (X, Y, Z, W, Id) VALUES (%s, %s, %s, %s, %s)", 
                (float(x), float(y), float(z), float(w), int(id))
            )
            db.commit()
            print("Dữ liệu đã được lưu thành công.")
        except mysql.connector.Error as e:
            db.rollback()
            print(f"Lỗi khi lưu dữ liệu: {e}")
    def delete_values(self, id):
        try:
            db.cursor().execute("DELETE FROM robot WHERE Id = %s", (int(id),))
            db.commit()
        except mysql.connector.Error:
            db.rollback()



    def show_map(self):
        file_path = '/home/robot/catkin_ws/src/navigation_bot/map/mymap2.pgm'

        # Mở file ảnh .pgm
        img = Image.open(file_path)
        img_array = np.array(img)  # Chuyển ảnh thành numpy array

        # Chuyển numpy array thành QImage để hiển thị lên QLabel
        height, width = img_array.shape
        bytes_per_line = width
        qimage = QImage(img_array.data, width, height, bytes_per_line, QImage.Format_Grayscale8)

        # Tạo QPixmap từ QImage và đặt lên QLabel
        pixmap = QPixmap.fromImage(qimage)
        self.uic.screen_cam_3.setPixmap(pixmap)
        self.uic.screen_cam_3.setScaledContents(True)  # Để ảnh tự động điều chỉnh theo kích thước QLabel





    ###########################################################################################################
    ############################## DONG HOC ROBOT MACIGIAN ####################################################



    def FK_3DOF(self, theta1, theta2, theta3):

        # Calculate the end-effector position
        Px = math.cos(math.radians(theta1)) * (self.l3 * math.cos(math.radians(theta2 + theta3)) + self.l2 * math.cos(math.radians(theta2)))
        Py = math.sin(math.radians(theta1)) * (self.l3 * math.cos(math.radians(theta2 + theta3)) + self.l2 * math.cos(math.radians(theta2)))
        Pz = self.l3 * math.sin(math.radians(theta2 + theta3)) + self.l2 * math.sin(math.radians(theta2))

        return Px, Py, Pz
    def IK_3DOF(self, Px, Py, Pz):

        # s1_1 = Py
        # c1_1 = Px
        # t1_1 = math.degrees(math.atan2(s1_1, c1_1))

        # # Calculate theta3
        # c3_1 = ((Px * math.cos(math.radians(t1_1)) + Py * math.sin(math.radians(t1_1)))**2 + Pz**2 - self.l3**2 - self.l2**2) / (2 * self.l2 * self.l3)
        # s3_1 = math.sqrt(1 - c3_1**2)
        # t3_1 = math.degrees(math.atan2(s3_1, c3_1))

        # d_1 = np.array([[self.l3 * math.cos(math.radians(t3_1)) + self.l2, - self.l3 * math.sin(math.radians(t3_1))],
        #                 [self.l3 * math.sin(math.radians(t3_1)), self.l3 * math.cos(math.radians(t3_1)) + self.l2]])
        
        # dc_1 = np.array([[Px * math.cos(math.radians(t1_1)) + Py * math.sin(math.radians(t1_1)), -self.l3 * math.sin(math.radians(t3_1))],
        #                 [Pz, self.l3 * math.cos(math.radians(t3_1)) + self.l2]])
        
        # ds_1 = np.array([[self.l3 * math.cos(math.radians(t3_1)) + self.l2, Px * math.cos(math.radians(t1_1)) + Py * math.sin(math.radians(t1_1))],
        #                 [self.l3 * math.sin(math.radians(t3_1)), Pz]])
        
        # c2_1 = np.linalg.det(dc_1) / np.linalg.det(d_1)
        # s2_1 = np.linalg.det(ds_1) / np.linalg.det(d_1)
        # t2_1 = math.degrees(math.atan2(s2_1, c2_1))

        # t2_1_1 = t2_1 + 90
        # t3_1_1 = t3_1 - 90

        # # Return the angles
        # return t1_1, t2_1_1, t3_1_1
    # Tính 2 giá trị của q1
        l1 = 180
        l2 = 150
        l3 = 170


        q1_solution1 = np.arctan2(Py, Px)
        q1_solution2 = np.arctan2(-Py, -Px)

        # Hàm để giải hệ phương trình cho q2 và q3
        def equations(vars):
            q2, q3 = vars
            eq1 = l1 + l3 * np.sin(q2 + q3) + l2 * np.cos(q2) - Pz   # Phương trình cho Pz
            eq2 = l3 * np.cos(q2 + q3) + l2 * np.sin(q2) - np.sqrt(Px**2 + Py**2)  # Tính r = sqrt(Px^2 + Py^2)
            return [eq1, eq2]

        # Sử dụng fsolve để giải hệ phương trình
        initial_guess = [0, 0]  # Giá trị ban đầu cho q2 và q3
        q2_solution1, q3_solution1 = fsolve(equations, initial_guess)

        # Chuyển đổi kết quả từ radian sang độ
        q1_solution1_deg = np.degrees(q1_solution1)
        q2_solution1_deg = np.degrees(q2_solution1)
        q3_solution1_deg = np.degrees(q3_solution1)

        # Tính giá trị tổng của q2 và q3 nếu cần thiết
        q3_sum_deg = q2_solution1_deg + q3_solution1_deg

        # Trả về kết quả
        return q1_solution1_deg, q2_solution1_deg, q3_sum_deg
    


    def cals_fk(self):
        try:
            theta1 = float(self.uic.theta1.text())
            theta2 = float(self.uic.theta2.text())
            theta3 = float(self.uic.theta3.text())
            # theta3 = 

            Px, Py, Pz = self.FK_3DOF(theta1=theta1, theta2=theta2, theta3=theta3)

            self.uic.Px.setText(f"{Px:.2f}")
            self.uic.Py.setText(f"{Py:.2f}")
            self.uic.Pz.setText(f"{Pz:.2f}")
        except ValueError:
            # print("Error: Please enter valid numbers for Px, Py, and Pz.")
            self.show_popup_err_dh()
            self.delete_text()
    def cals_ik(self):
        try:
            Px = float(self.uic.Px.text())
            Py = float(self.uic.Py.text())
            Pz = float(self.uic.Pz.text())

            theta1, theta2, theta3 = self.IK_3DOF(Px=Px, Py=Py, Pz=Pz)

            self.uic.theta1.setText(f"{theta1:.2f}")
            self.uic.theta2.setText(f"{theta2:.2f}")
            self.uic.theta3.setText(f"{theta3:.2f}")
        except ValueError:
            # print("Error: Please enter valid numbers for Px, Py, and Pz.")
            self.show_popup_err_dh()
            self.delete_text()
    def delete_text(self):
        self.uic.theta1.setText("")
        self.uic.theta2.setText("")
        self.uic.theta3.setText("")
        self.uic.Px.setText("")
        self.uic.Py.setText("")
        self.uic.Pz.setText("")
    def send_arduino(self, data1, data2, data3, data4):
        # try:
        #     time.sleep(1)  
        #     self.ser = serial.Serial(self.USB_MEGA_ROBOT, self.BAUDRATE)  
        #     message = f"{data1};{data2};{data3};{data4}"
        #     self.ser.write(message.encode())
        #     print("Sent:", message)
        #     self.ser.close()
        # except serial.SerialException as e:
        #     # print(f"Error opening serial port: {e}")
        #     self.show_popup_err_arduino()
        #     # self.delete_text()
        if self.serial.is_open:
            try:
                data = f"{data1};{data2};{data3};{data4}\n"
                self.serial.write(data.encode('utf-8'))
                # print(f"Dữ liệu đã gửi: {data.strip()}")
            except serial.SerialException as e:
                print(f"Error sending data: {e}")
                self.show_popup_err_arduino()
        
    def home_robot(self):
        self.send_arduino(data1=0, data2=0, data3=0, data4=0)
    def run_robot(self):
        try:
            theta1 = float(self.uic.theta1.text())
            theta2 = float(self.uic.theta2.text())
            theta3 = float(self.uic.theta3.text())
            self.send_arduino(data1 = theta1, data2 = theta2, data3 = theta3 , data4 = 1)
        except ValueError:
            # print("ERR")
            self.show_popup_err_send_robot()
    def return_box(self):
        pass

    def get_sai_so(self):
        pass










      










if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)  # Tạo ứng dụng Qt
    window = MainWindow()  # Tạo cửa sổ chính
    window.start_thread()
    time.sleep(2)
    window.showFullScreen()  # Hiển thị cửa sổ chính
    sys.exit(app.exec_())  # Chạy vòng lặp sự kiện Qt
