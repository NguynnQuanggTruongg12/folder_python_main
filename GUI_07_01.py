# GUI
from PyQt5.QtGui import QPixmap
from form_login import LOGIN
from Second_win import Ui_MainWindow
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QTableWidget
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import QImage
# FigureCanvas and plot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
# from matplotlib import pyplot as plt

# FK_IK
from math import cos, sin, pi, atan2, sqrt, degrees, radians
import numpy as np
import sys

# Pyserial
import serial
import serial.tools.list_ports  # Check Port
#  Voice
import speech_recognition as sr
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import time
# import nltk
# Camera
import cv2

# nltk.download('punkt')
# Khởi tạo vector  và classifier Naive Bayes
vector = CountVectorizer()
classifier = MultinomialNB()
train_data = []
train_labels = []

# khai báo giá trị
alpha = pi / 4  # khai báo góc lệch dof 1
the_x = pi / 6  # khai báo góc lệch dof 3
d1 = 8.5
L1 = d1 * sin(alpha)
L2 = 12.9
L3 = 21.9
L4 = 0  # độ dài lệch trong dof 3 robot
Lx = L3 + L4 * sin(the_x)
Ly = -L4 * cos(the_x)


def basic_00(a, b, d):
    try:
        anp = atan2(b, a)
        mau_so = sqrt(a ** 2 + b ** 2)
        temp = 1 - d ** 2 / (a ** 2 + b ** 2)
        x1 = atan2(sqrt(temp), d / mau_so) + anp
        x2 = atan2(-sqrt(temp), d / mau_so) + anp
        x_all = np.array([x1, x2])
        return x_all
    except ValueError as e:
        print(f"Bị lỗi: {e}")


def inv_kinematics(x_inv, y_inv, z_inv, l1=L1, l2=L2, lx=Lx, ly=Ly):
    if (x_inv >= 35) or (x_inv < 21) or (y_inv >= 16) or (y_inv <= -16):
        print("loi gia tri")
    else:
        try:
            # print(x_inv, y_inv, z_inv)
            x_inv, y_inv, z_inv = get_sai_so(x_inv, y_inv, z_inv)
            # Calc Theta_1
            theta_1 = basic_00(y_inv, -x_inv, 0)
            the_11 = theta_1[0]
            the_12 = theta_1[1]
        except (ValueError, TypeError, IndexError) as e:
            print(f'Theta1: Error with == {e}')
            the_11, the_12 = None, None
            ##
        try:
            # Calculate Theta_2
            a21 = 2 * l2 * (x_inv * cos(the_11) + y_inv * sin(the_11) - l1)
            b21 = 2 * l2 * z_inv
            d21 = -((lx ** 2) + (ly ** 2)) + (z_inv * z_inv) + (l2 * l2) + (
                    (x_inv * cos(the_11) + y_inv * sin(the_11) - l1) *
                    (x_inv * cos(the_11) + y_inv * sin(the_11) - l1))
            theta_21 = basic_00(a21, b21, d21)
            ##
            the_21 = theta_21[0]
            the_22 = theta_21[1]
        except (TypeError, IndexError) as e:
            print(f"Theta2: Error with == {e}")
            # the_21, the_22, the_23, the_24 = None, None, None, None
            the_21, the_22 = None, None

            # Calc Theta_3
        try:
            the_31 = atan2(z_inv - l2 * sin(the_21),
                           x_inv * cos(the_11) + y_inv * sin(the_11) - l2 * cos(the_21) - l1) - the_21
            the_32 = atan2(z_inv - l2 * sin(the_22),
                           x_inv * cos(the_11) + y_inv * sin(the_11) - l2 * cos(the_22) - l1) - the_22

        except TypeError as e:
            print(f"Theta3: Error with == {e}")
            the_31, the_32 = None, None
            ##
        value_all = the_11, the_12, the_21, the_22, the_31, the_32  # Lấy 2 bộ
        if None in value_all:
            print("Value Theta 1, 2, 3 = None -- Error")
            return None
        else:
            the1, the2, the3 = round(degrees(the_11), 4), round(degrees(the_21), 4), round(degrees(the_31), 4)
            return the1, the2, the3


def fw_kinematics(the_1, the_2, the_3, l1=L1, l2=L2, lx=Lx, ly=Ly):
    try:
        # Đổi góc độ sang radian
        the_1 = radians(the_1)
        the_2 = radians(the_2)
        the_3 = radians(the_3)

        x_fw = cos(float(the_1)) * (l1 + lx * cos(float(the_2) + float(the_3)) - ly * sin(float(the_2) + float(the_3))
                                    + L2 * cos(float(the_2)))
        y_fw = sin(float(the_1)) * (l1 + lx * cos(float(the_2) + float(the_3)) - ly * sin(float(the_2) + float(the_3))
                                    + l2 * cos(float(the_2)))
        z_fw = ly * cos(float(the_2) + float(the_3)) + lx * sin(float(the_2) + float(the_3)) + l2 * sin(
            float(the_2)) + 17.7
        # print(f"{round(x_fw, 3)}, {round(y_fw, 3)}, {round(z_fw, 3)}")
        return round(x_fw, 2), round(y_fw, 2), round(z_fw, 2)
    except (ValueError, TypeError) as e:
        print(f"FW -- Error: {e}")


def get_value(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


# Sai số động học
def get_sai_so(x, y, z):
    if 33 <= x < 35:
        if -10 < y <= 0:
            x = x - 1.5
            y = y
            z = z - (12.7 + 5.2)
        elif -10 >= y >= -16:
            x = x - 1.5
            y = y + 0.5
            z = z - (12.8 + 5.2)
        elif 0 < y <= 10:
            x = x - 1.6
            y = y + 0.5
            z = z - (12.6 + 5.2)
        elif 10 < y <= 14:
            x = x - 1.6
            y = y
            z = z - (13 + 5.2)
    ########################################
    elif 31 <= x < 33:
        if 0 <= y <= 10:  # ok
            x = x - 1.7
            y = y
            z = z - (12.5 + 5.2)
        elif 10 < y < 16:
            x = x - 1.7
            y = y + 0.2
            z = z - (12.7 + 5.2)

        elif -10 <= y < 0:
            x = x - 1.5
            y = y + 0.3
            z = z - (12.5 + 5.2)
        elif -16 < y < -10:
            x = x - 1.5
            y = y + 0.5
            z = z - (12.7 + 5.2)
    ########################################
    elif 29 <= x < 31:
        if -10 <= y <= 0:  # ok
            x = x - 1.7
            y = y + 0.4
            z = z - (12.3 + 5.2)
        elif -12 >= y > -16:
            x = x - 1.7
            y = y + 0.9
            z = z - (12.5 + 5.2)
        elif 0 < y <= 10:
            x = x - 1.7
            y = y + 0.5
            z = z - (12.2 + 5.2)
        elif 10 < y < 16:
            x = x - 1.7
            y = y + 0.7
            z = z - (12.3 + 5.2)
    ########################################
    elif 27 <= x < 29:
        if -6 <= y < 0:  # ok
            x = x - 1.5
            y = y + 0.6
            z = z - (12 + 5.2)
        elif y == 0:
            x = x - 1.5
            y = y
            z = z - (11.8 + 5.2)
        elif -6 > y >= -14:
            x = x - 1.4
            y = y + 1
            z = z - (12.1 + 5.2)
        elif 0 < y <= 8:
            x = x - 1.7
            y = y + 0.5
            z = z - (12.1 + 5.2)
        elif 8 < y < 16:
            x = x - 1.7
            y = y + 0.3
            z = z - (12.2 + 5.2)
    ########################################
    elif 25 <= x < 27:
        if -4 <= y <= 4:  # ok
            x = x - 1.5
            y = y
            z = z - (11.9 + 5.2)

        elif y < -4:  # ok
            x = x - 1.5
            y = y + 0.6
            z = z - (12 + 5.2)

        elif y > 4:  # ok
            x = x - 1.5
            y = y
            z = z - (12 + 5.2)
    ########################################
    elif 23 <= x < 25:
        if -4 <= y < 0:  # ok
            x = x - 1.4
            y = y + 0.5
            z = z - (11.7 + 5.2)
        elif y < -4:  # ok
            x = x - 1.4
            y = y + 0.8
            z = z - (11.7 + 5.2)
        elif 0 < y < 6:  # ok
            x = x - 1.8
            y = y + 0.2
            z = z - (11.8 + 5.2)
        elif 6 <= y < 15:
            x = x - 1.7
            y = y
            z = z - (11.9 + 5.2)
        elif y == 0:
            x = x - 1.7
            y = y
            z = z - (11.5 + 5.2)
    #######################################
    elif 21 <= x < 23:
        if -6 <= y < 0:
            x = x - 1.7
            y = y + 0.3
            z = z - (11.6 + 5.2)
        elif -6 > y > -16:
            x = x - 1.7
            y = y + 0.6
            z = z - (11.8 + 5.2)
        elif 0 < y <= 4:
            x = x - 1.7
            y = y + 0.2
            z = z - (11.4 + 5.2)
        elif 4 < y <= 8:
            x = x - 1.7
            y = y
            z = z - (11.6 + 5.2)
        elif 8 < y < 16:
            x = x - 1.7
            y = y
            z = z - (11.7 + 5.2)
        elif y == 0:
            x = x - 1.7
            y = y
            z = z - (11.5 + 5.2)
    if (x > 35) or (x < 20) or (y > 16) or (y < -16):
        print("loi gia tri")
    # print(x, y, z)
    return round(x, 2), round(y, 2), round(z, 2)


# Check port khả dụng
def list_com_ports():
    try:
        list_device = []
        port_arduino = ''
        ports = serial.tools.list_ports.comports()
        for port in ports:
            list_device.append(port.description)
        for device in list_device:  # Kiếm port của arduino
            if 'Arduino' in device or 'SERIAL' in device:
                device = device.replace('(', '').replace(')', '')
                port_arduino = device.split()[-1]
                print(f"Port hiện tại của Arduino: {port_arduino}")
        return port_arduino

    except (Exception, serial.SerialException) as e:
        print(f"Login_Check_Port -- Error {e}")


# Chạy Auto Tính nghiệm cho DHN
def run_calc_inv(x_auto, y_auto, z_auto):
    the1, the2, the3 = None, None, None
    x, y, z = x_auto, y_auto, z_auto
    if x is not None and y is not None and z is not None:
        calc_inv = inv_kinematics(float(x), float(y), float(z))
        if calc_inv is not None:
            the1, the2, the3 = calc_inv
    else:
        print("Không thể tính toán với giá trị không hợp lệ.")
    return the1, the2, the3


def pixel_to_cm(x_pixel, y_pixel, calibration_factor_x, calibration_factor_y):
    y_cm = x_pixel * calibration_factor_x
    x_cm = y_pixel * calibration_factor_y
    return x_cm, y_cm


def detect_circle_object(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(
        gray,
        cv2.HOUGH_GRADIENT,
        dp=1,
        minDist=15,
        param1=30,
        param2=30,
        minRadius=1,
        maxRadius=15
    )
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            cv2.circle(image, center, i[2], (0, 255, 0), 2)
            return center
    else:
        return None


def detect_red_object(image):
    # lower_red = np.array([0, 0, 100])
    # upper_red = np.array([50, 50, 255])
    lower_red = np.array([100, 0, 0])
    upper_red = np.array([255, 50, 50])
    mask_red = cv2.inRange(image, lower_red, upper_red)
    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours_red:
        largest_contour_red = max(contours_red, key=cv2.contourArea)
        m_red = cv2.moments(largest_contour_red)
        if m_red["m00"] != 0:
            cx_red = int(m_red["m10"] / m_red["m00"])
            cy_red = int(m_red["m01"] / m_red["m00"])
            # cv2.drawContours(image, [largest_contour_red], -1, (0, 0, 255), 2)
            # cv2.circle(image, (cx_red, cy_red), 7, (255, 255, 255), -1)
            # cv2.putText(image, "Red Object", (cx_red - 20, cy_red - 20), cv2.FONT_HERSHEY_SIMPLEX,0.5,
            #             (255, 255, 255),2)
            return cx_red, cy_red
    else:
        return None


class KalmanFilter:
    def __init__(self, state_dim, measurement_dim):
        self.kalman_filter = cv2.KalmanFilter(state_dim, measurement_dim, 0)
        self.state = np.zeros(state_dim, dtype=np.float32)
        self.kalman_filter.statePre = self.state
        self.kalman_filter.statePost = self.state
        self.kalman_filter.transitionMatrix = np.eye(state_dim, dtype=np.float32)
        cv2.setIdentity(self.kalman_filter.measurementMatrix)
        cv2.setIdentity(self.kalman_filter.processNoiseCov, 1e-4)
        cv2.setIdentity(self.kalman_filter.measurementNoiseCov, 1e-1)
        cv2.setIdentity(self.kalman_filter.errorCovPost, 1)

    def update(self, measurement):
        # prediction = self.kalman_filter.predict()
        estimated = self.kalman_filter.correct(measurement)
        return estimated


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.second_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.second_win)
        self.second_win.show()
        # Các biến
        self.animation1, self.animation2, self.animation3,self.animation4 = None, None, None,None
        self.animation5, self.animation6, self.animation7 = None, None, None
        self.Side_Menu_num = 0
        # Các biến trong arduino
        self.ser = None
        self.mode_ser = False
        self.port_check = None, None
        self.movie = QMovie("icon/giphy.gif")       # Set Gif connect
        self.uic.Arrow_vinh.setMovie(self.movie)    # Set cho label để hiển thị
        self.data_box = f'{0} {0} {-30} {0}'
        # Các biến set cho FK_IK
        self.forward_mode = True
        self.mode_send = False
        # Biến cho chế độ chạy auto_manual
        self.the_1_list = []
        self.the_2_list = []
        self.the_3_list = []
        self.mode_auto = False
        self.mode_manual = False
        # biến camera
        self.frame_img = None
        self.mode_cam = False
        self.x_values = []
        self.y_values = []
        # Tương tác các nút trong GUI
        self.uic.stackedWidget.setCurrentWidget(self.uic.page_login)
        self.uic.Home.clicked.connect(self.show_login)
        self.uic.start.clicked.connect(self.show_setting)
        self.uic.Menu.clicked.connect(self.animate_button)
        self.uic.Setting.clicked.connect(self.show_setting)
        self.uic.Camera.clicked.connect(self.show_camera)
        self.uic.Manual.clicked.connect(self.show_manual)
        self.uic.mode_manual.clicked.connect(self.set_manual_mode)
        self.uic.mode_auto.clicked.connect(self.set_auto_mode)
        self.uic.forward.clicked.connect(self.set_forward_mode)
        self.uic.Inverse.clicked.connect(self.set_inverse_mode)
        self.uic.Run.clicked.connect(self.send_value_manual_auto)
        self.uic.CONNECT.clicked.connect(self.connect_to_arduino)
        self.uic.DISCONNECT.clicked.connect(self.disconnect_to_arduino)
        self.uic.Mic.clicked.connect(self.voice_recognition)
        self.uic.graph.clicked.connect(self.show_graph)
        self.uic.Calc.clicked.connect(self.calc_theta)
        self.uic.Return_box.clicked.connect(self.set_box_robot)
        self.uic.clear_row.clicked.connect(self.clear_row_the)
        # Biến cho chạy thread
        self.thread = {}
        self.uic.reset.setEnabled(False)
        self.uic.reset.clicked.connect(self.worker_1)
        self.uic.start_cam.clicked.connect(self.worker_2)
        self.uic.send_cam.clicked.connect(self.send_value_cam)
        self.uic.stop.clicked.connect(self.stop_camera)
        self.uic.set_robot.clicked.connect(self.set_robot_cam)
        # Biến cho Plot 3dof and
        self.canvas = FigureCanvas(Figure())
        self.ax = self.canvas.figure.add_subplot(111, projection='3d')
        self.uic.Screen_diagram.addWidget(self.canvas)
        # Plot grap theta
        self.figure_2d = Figure()
        self.canvas_2d = FigureCanvas(self.figure_2d)
        self.uic.Screen_graph.addWidget(self.canvas_2d)
        self.ax_1 = self.figure_2d.add_subplot(311)
        self.ax_2 = self.figure_2d.add_subplot(312)
        self.ax_3 = self.figure_2d.add_subplot(313)
        self.the1_grap, self.the2_grap, self.the3_grap = [], [], []

    def connect_to_arduino(self):
        port = self.uic.Port_2.currentText()
        print(f'Đã chọn: {port}')
        baud_rate = int(self.uic.Baudrate_2.currentText())
        print(f'Đã chọn: {baud_rate}')
        # Mở kết nối với Arduino
        if not self.mode_ser:
            if port == self.port_check and baud_rate == 115200:
                try:
                    self.ser = serial.Serial(port.strip(), baud_rate)
                    time.sleep(1.5)
                    if self.ser.isOpen():
                        self.uic.reset.setEnabled(True)
                        self.mode_ser = True
                        QMessageBox.about(self.second_win, "Connect to Arduino", "Kết nối thành công!")
                        self.uic.Arrow_vinh.show()
                        self.movie.start()
                    else:
                        print("Chưa kết nối được arduino")
                except serial.SerialException as e:
                    print(f"Error -- {e}")
            else:
                QMessageBox.critical(self.second_win, "Connect to Arduino", "Kết nối không thành công!")
        else:
            QMessageBox.critical(self.second_win, "Robot", "Đã có kết nối rồi!")

    def worker_1(self):
        if self.mode_ser:
            self.thread[1] = ThreadClass(index=1, ser_1=self.ser)
            self.thread[1].start()
            self.thread[1].signal.connect(self.reset_arduino)
            self.uic.Mode.setText("Reset")
            self.uic.reset.setEnabled(False)
            self.uic.Run.setEnabled(False)
            self.uic.Return_box.setEnabled(False)
        else:
            QMessageBox.critical(self.second_win, "Robot", "Chưa kết nối Arduino")

    def worker_2(self):
        if self.mode_ser:
            self.thread[2] = ThreadClass(index=2, ser_1=self.ser)
            self.thread[2].start()
            self.thread[2].frame_update.connect(self.show_wed_cam)
            self.thread[2].frame_update.connect(self.scan_cam)
        else:
            QMessageBox.critical(self.second_win, "Robot", "Chưa kết nối Arduino")

    def reset_arduino(self, result):
        try:
            a = result
            data_home = f'{0} {-151.5} {150} {0}'
            self.ser.write(data_home.encode())
            if a == 'the1: 0.00 the2: -151.50 the3: 150.00':
                self.disconnect_to_arduino()
                self.connect_to_arduino()
                self.uic.Mode.setText("")
                self.uic.Run.setEnabled(True)
                self.uic.Return_box.setEnabled(True)
                print("Arduino reset thành công.")
        except (Exception, serial.SerialException) as e:
            print(f"Lỗi khi reset Arduino: {e}")

    def disconnect_to_arduino(self):
        try:
            try:
                self.thread[1].stop()
                # self.thread[1].wait()
            except Exception as e:
                print(f"Error stop thread_1:..... {e}")
            if self.ser is not None:
                self.ser.close()
            if self.movie is not None:
                self.uic.Arrow_vinh.hide()
                self.movie.stop()
            self.mode_ser = False
            self.uic.Run.setEnabled(True)
            self.uic.Return_box.setEnabled(True)
        except Exception as e:
            print(f"Disconnection -- Error ==  {e}")

    def voice_recognition(self):
        try:
            if self.mode_ser:
                key = "None - voice"
                # Khởi tạo recognizer
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Lắng nghe...")
                    audio = r.listen(source, timeout=30)
                    print("Đã nghe xong.")
                try:
                    # Đổi voice thành text
                    text = r.recognize_google(audio, language='vi-VN')
                    print("Giọng nói đã nhận dạng:", text)
                    text = text.lower()
                    keywords_all = {
                        "vat_1": ["vật 1", "vật một","vật thứ nhất","thứ nhất","một","đầu tiên","điểm thứ nhất",
                                  "điểm đầu tiên"],
                        "vat_2": ["vật 2", "vật hai","vật thứ hai","thứ hai","hai","điểm hai","điểm thứ hai"],
                        "vat_3": ["vật 3", "vật ba","vật thứ ba","thứ ba","ba","điểm thứ ba"],
                        "vat_4": ["vật 4", "vật bốn","vật thứ bốn","vật thứ tư","thứ tư","một","cuối","vật cuối",
                                  "điểm cuối","điểm thứ 4"]}
                    # Check xem có đủ từ để tạo biến x, y, z
                    for action, keywords in keywords_all.items():
                        for keyword in keywords:
                            if keyword in text:
                                key = action
                    print(key)
                    if key == "vat_1":
                        self.uic.theta1.setText("-14.63")
                        self.uic.theta2.setText("3.87")
                        self.uic.theta3.setText("-61.86")
                        x, y, z = fw_kinematics(-14.63,3.87,-61.86)
                        self.uic.Px.setText(str(x))
                        self.uic.Py.setText(str(y))
                        self.uic.Pz.setText(str(z))
                        data_vat_1 = f"{-14.63} {3.87} {-61.86} {1}"
                        self.ser.write(data_vat_1.encode())
                        self.update_plot(-14.63,3.87,-61.86)
                        # self.set_box_robot()
                    elif key == "vat_2":
                        self.uic.theta1.setText("-7.15")
                        self.uic.theta2.setText("5.79")
                        self.uic.theta3.setText("-65.99")
                        x, y, z = fw_kinematics(-7.15, 5.79, -65.99)
                        self.uic.Px.setText(str(x))
                        self.uic.Py.setText(str(y))
                        self.uic.Pz.setText(str(z))
                        data_vat_2 = f"{-7.15} {5.79} {-65.99} {1}"
                        self.ser.write(data_vat_2.encode())
                        self.update_plot(-7.15, 5.79, -65.99)
                        # self.set_box_robot()
                    elif key == "vat_3":
                        self.uic.theta1.setText("7.77")
                        self.uic.theta2.setText("6.18")
                        self.uic.theta3.setText("-66.82")
                        x, y, z = fw_kinematics(7.77, 6.18, -66.82)
                        self.uic.Px.setText(str(x))
                        self.uic.Py.setText(str(y))
                        self.uic.Pz.setText(str(z))
                        data_vat_3 = f"{7.77} {6.18} {-66.82} {1}"
                        self.ser.write(data_vat_3.encode())
                        self.update_plot(7.77, 6.18, -66.82)
                        # self.set_box_robot()
                    elif key == "vat_4":
                        self.uic.theta1.setText("15.27")
                        self.uic.theta2.setText("4.18")
                        self.uic.theta3.setText("-62.51")
                        x, y, z = fw_kinematics(15.27, 4.18, -62.51)
                        self.uic.Px.setText(str(x))
                        self.uic.Py.setText(str(y))
                        self.uic.Pz.setText(str(z))
                        data_vat_3 = f"{15.27} {4.18} {-62.51} {1}"
                        self.ser.write(data_vat_3.encode())
                        self.update_plot(15.27, 4.18, -62.51)
                        # self.set_box_robot()
                    else:
                        print("không nhận dạng được")

                except sr.UnknownValueError:
                    print("Không nhận dạng được giọng nói.")
                except sr.RequestError as e:
                    print("Lỗi trong quá trình kết nối với nhận dạng giọng nói; {0}".format(e))
            else:
                QMessageBox.critical(self.second_win, "Robot", "Chưa kết nối Arduino")
        except Exception as e:
            print(f"Error -- Def_voice: {e}")

    def set_auto_mode(self):
        try:
            if self.mode_ser:
                self.uic.led_auto.setStyleSheet('background-color: blue;border-radius: 5px; border: 1px solid black;')
                self.uic.led_manual.setStyleSheet('background-color: gray;border-radius: 5px; border: 1px solid black;')
                self.mode_manual = False
                self.mode_auto = True
                self.forward_mode = False
                self.mode_send = True
                self.uic.clear_row.setText("Clear row")
                self.uic.forward.hide()
                self.uic.Inverse.hide()
                self.uic.Mic.hide()
                self.canvas.hide()
                self.uic.table_the.show()
                self.forward_mode = False
                self.mode_send = True
                # Enable các QLineEdit liên quan đến Forward và Disable các QLineEdit liên quan đến Inverse
                self.set_inverse_mode()
            else:
                QMessageBox.critical(self.second_win, "Robot", "Chưa kết nối Arduino")
        except (Exception, ValueError, TypeError) as e:
            print(f"Set_Auto-- Error: {e}")

    def set_manual_mode(self):
        try:
            if self.mode_ser:
                self.uic.led_manual.setStyleSheet('background-color:yellow;border-radius:5px; border:1px solid black;')
                self.uic.led_auto.setStyleSheet('background-color: gray;border-radius: 5px; border: 1px solid black;')
                self.mode_manual = True
                self.mode_auto = False
                self.uic.clear_row.setText("Home")
                self.uic.forward.show()
                self.uic.Inverse.show()
                self.uic.Mic.show()
                self.canvas.show()
                self.uic.table_the.hide()
                self.uic.Mode.setText("")
                self.forward_mode = False
                self.mode_send = False
                self.uic.theta1.setEnabled(True)
                self.uic.theta2.setEnabled(True)
                self.uic.theta3.setEnabled(True)
                self.uic.Px.setEnabled(True)
                self.uic.Py.setEnabled(True)
                self.uic.Pz.setEnabled(True)
            else:
                QMessageBox.critical(self.second_win, "Robot", "Chưa kết nối Arduino")
        except (Exception, ValueError, TypeError) as e:
            print(f"Set_Manual-- Error: {e}")

    def set_forward_mode(self):
        if self.mode_ser:
            if self.mode_manual:
                self.forward_mode = True
                self.mode_send = True
                # Enable các QLineEdit liên quan đến Forward và Disable các QLineEdit liên quan đến Inverse
                self.uic.theta1.setEnabled(True)
                self.uic.theta2.setEnabled(True)
                self.uic.theta3.setEnabled(True)
                self.uic.Px.setEnabled(False)
                self.uic.Py.setEnabled(False)
                self.uic.Pz.setEnabled(False)
                self.uic.Mode.setText("Forward")
            else:
                QMessageBox.critical(self.second_win, "Robot", "VUI LÒNG CHỌN AUTO OR MANUAL")

        else:
            QMessageBox.critical(self.second_win, "Robot", "Chưa kết nối Arduino")

    def set_inverse_mode(self):
        if self.mode_ser:
            if self.mode_manual or self.mode_auto:
                self.forward_mode = False
                self.mode_send = True
                self.uic.theta1.setEnabled(False)
                self.uic.theta2.setEnabled(False)
                self.uic.theta3.setEnabled(False)
                self.uic.Px.setEnabled(True)
                self.uic.Py.setEnabled(True)
                self.uic.Pz.setEnabled(True)
                self.uic.Mode.setText("Inverse")
            else:
                QMessageBox.critical(self.second_win, "Robot", "VUI LÒNG CHỌN MANUAL")
        else:
            QMessageBox.critical(self.second_win, "Robot", "Chưa kết nối Arduino")

    def set_table_the(self):
        try:
            # Lấy độ dài ngắn nhất của mảng để chạy for
            num_rows = min(len(self.the_1_list), len(self.the_2_list), len(self.the_3_list))
            for row in range(num_rows):
                for col in range(3):
                    item = QTableWidgetItem(str(self.the_1_list[row])) if col == 0 else QTableWidgetItem(
                        str(self.the_2_list[row])) if col == 1 else QTableWidgetItem(str(self.the_3_list[row]))
                    item.setTextAlignment(Qt.AlignCenter)  # Thiết lập căn giữa cho ô
                    self.uic.table_the.setItem(row, col, item)

        except Exception as e:
            print(f"Set_table_the --- Error: {e}")

    def clear_row_the(self):
        try:
            if self.mode_auto:
                table = self.uic.table_the
                table.clearContents()
                self.the_1_list, self.the_2_list, self.the_3_list = [], [], []
            if self.mode_manual:
                self.uic.theta1.setText("0")
                self.uic.theta2.setText("0")
                self.uic.theta3.setText("0")
                x, y, z = fw_kinematics(0,0,0)
                self.uic.Px.setText(str(x))
                self.uic.Py.setText(str(y))
                self.uic.Pz.setText(str(z))
                data_home = f"{0} {0} {0} {0}"
                self.ser.write(data_home.encode())
                self.plot_3dof(str(0), str(0), str(0))
                self.update_plot(0, 0, 0)
        except Exception as e:
            print(f"Error -- def_clear_row_the: {e}")

    def calc_theta(self):
        try:
            if self.mode_auto:
                if not self.forward_mode:
                    x = self.uic.Px.text()
                    y = self.uic.Py.text()
                    z = self.uic.Pz.text()
                    if not get_value(x) or not get_value(y) or not get_value(z):
                        QMessageBox.critical(self.second_win, "Robot", "Vui lòng nhập giá trị hợp lệ!")
                        self.uic.Px.setText("")
                        self.uic.Py.setText("")
                        self.uic.Pz.setText("")
                        return
                    else:
                        run_5 = run_calc_inv(x, y, z)
                        if None in run_5:
                            QMessageBox.critical(self.second_win, "Robot", "Lỗi tính toán")
                        else:
                            the1, the2, the3 = run_5
                            if self.mode_auto:
                                self.the_1_list.append(the1)
                                self.the_2_list.append(the2)
                                self.the_3_list.append(the3)
                                self.set_table_the()
                else:
                    QMessageBox.critical(self.second_win, "Robot", "VUI LÒNG CHỌN ĐHN")
            else:
                QMessageBox.critical(self.second_win, "Robot", "Chưa chọn chế độ manual_auto")
        except (Exception,ValueError, TypeError) as e:
            print("Calc_Auto -- Error:", e)

    def run_auto(self):
        try:
            count_auto = 0
            if self.mode_auto:
                # send value Auto
                len_array_1 = len(self.the_1_list)
                len_array_2 = len(self.the_2_list)
                len_array_3 = len(self.the_3_list)
                if len_array_1 == 5 and len_array_2 == 5 and len_array_3 == 5:
                    the1_1, the1_2, the1_3, the1_4, the1_5 = None, None, None, None, None
                    the2_1, the2_2, the2_3, the2_4, the2_5 = None, None, None, None, None
                    the3_1, the3_2, the3_3, the3_4, the3_5 = None, None, None, None, None
                    for i in range(5):
                        if i == 0:
                            the1_1 = self.the_1_list[i]
                            the2_1 = self.the_2_list[i]
                            the3_1 = self.the_3_list[i]
                        elif i == 1:
                            the1_2 = self.the_1_list[i]
                            the2_2 = self.the_2_list[i]
                            the3_2 = self.the_3_list[i]
                        elif i == 2:
                            the1_3 = self.the_1_list[i]
                            the2_3 = self.the_2_list[i]
                            the3_3 = self.the_3_list[i]
                        elif i == 3:
                            the1_4 = self.the_1_list[i]
                            the2_4 = self.the_2_list[i]
                            the3_4 = self.the_3_list[i]
                        elif i == 4:
                            the1_5 = self.the_1_list[i]
                            the2_5 = self.the_2_list[i]
                            the3_5 = self.the_3_list[i]
                    # Point_1
                    if count_auto == 0:
                        data1 = f'{the1_1} {the2_1} {the3_1} {1}'
                        self.ser.write(data1.encode())
                        ##
                        # print(the1_1)
                        dk_p1 = format(round(the1_1, 2), '.2f')
                        dk_p2 = format(round(the2_1, 2), '.2f')
                        dk_p3 = format(round(the3_1, 2), '.2f')
                        print(dk_p1, dk_p2, dk_p3)
                        for k in range(5):
                            read_serial = self.ser.readline().decode('utf-8').strip('\r\n')
                            print(read_serial)
                            if read_serial == f"the1: {dk_p1} the2: {dk_p2} the3: {dk_p3}":
                                break
                        time.sleep(1)
                        data1_up = f"{the1_1} {the2_1 + 15} {the3_1} {1}"
                        self.ser.write(data1_up.encode())
                        time.sleep(2)
                        print(data1_up)
                        dk_p11 = dk_p1
                        dk_p33 = dk_p3
                        dk_p22 = format(round(the2_1 + 15, 2), '.2f')
                        for k in range(5):
                            read_serial = self.ser.readline().decode('utf-8').strip('\r\n')
                            print(read_serial)
                            if read_serial == f"the1: {dk_p11} the2: {dk_p22} the3: {dk_p33}":
                                break
                        time.sleep(2)
                        self.ser.write(self.data_box.encode())
                        for k in range(5):
                            read_serial = self.ser.readline().decode('utf-8').strip('\r\n')
                            print(read_serial)
                            if read_serial == 'the1: 0.00 the2: 0.00 the3: -30.00':
                                break
                        count_auto = 1
                        self.update_plot(the1_1, the2_1, the3_1)
                        self.update_plot(the1_1, (the2_1 + 15), the3_1)
                        self.update_plot(0, 0, -30)
                        print("Done_point_1")
                        time.sleep(2)
                    # Point_2
                    if count_auto == 1:
                        data2 = f'{the1_2} {the2_2} {the3_2} {1}'
                        self.ser.write(data2.encode())
                        dk_p2_1 = format(round(the1_2, 2), '.2f')
                        dk_p2_2 = format(round(the2_2, 2), '.2f')
                        dk_p2_3 = format(round(the3_2, 2), '.2f')
                        for k in range(5):
                            read_serial = self.ser.readline().decode('utf-8').strip('\r\n')
                            print(read_serial)
                            if read_serial == f"the1: {dk_p2_1} the2: {dk_p2_2} the3: {dk_p2_3}":
                                break
                        time.sleep(2)
                        data2_up = f"{the1_2} {the2_2 + 15} {the3_2} {1}"
                        self.ser.write(data2_up.encode())
                        dk_p2_11 = dk_p2_1
                        dk_p2_33 = dk_p2_3
                        dk_p2_22 = format(round(the2_2 + 15, 2), '.2f')
                        for k in range(5):
                            read_serial = self.ser.readline().decode('utf-8').strip('\r\n')
                            print(read_serial)
                            if read_serial == f"the1: {dk_p2_11} the2: {dk_p2_22} the3: {dk_p2_33}":
                                break
                        time.sleep(2)
                        self.ser.write(self.data_box.encode())
                        for k in range(5):
                            read_serial = self.ser.readline().decode('utf-8').strip('\r\n')
                            print(read_serial)
                            if read_serial == 'the1: 0.00 the2: 0.00 the3: -30.00':
                                break
                        count_auto = 2
                        self.update_plot(the1_2, the2_2, the3_2)
                        self.update_plot(the1_2, (the2_2 + 15), the3_2)
                        self.update_plot(0, 0, -30)
                        print("Done_point_2")
                        time.sleep(2)
                    # Point_3
                    if count_auto == 2:
                        data3 = f'{the1_3} {the2_3} {the3_3} {1}'
                        self.ser.write(data3.encode())
                        ##
                        # print(the1_1)
                        dk_p3_1 = format(round(the1_3, 2), '.2f')
                        dk_p3_2 = format(round(the2_3, 2), '.2f')
                        dk_p3_3 = format(round(the3_3, 2), '.2f')
                        for k in range(5):
                            read_serial = self.ser.readline().decode('utf-8').strip('\r\n')
                            print(read_serial)
                            if read_serial == f"the1: {dk_p3_1} the2: {dk_p3_2} the3: {dk_p3_3}":
                                break
                        time.sleep(2)
                        data3_up = f"{the1_3} {the2_3 + 15} {the3_3} {1}"
                        self.ser.write(data3_up.encode())
                        dk_p3_11 = dk_p3_1
                        dk_p3_33 = dk_p3_3
                        dk_p3_22 = format(round(the2_3 + 15, 2), '.2f')
                        for k in range(5):
                            read_serial = self.ser.readline().decode('utf-8').strip('\r\n')
                            print(read_serial)
                            if read_serial == f"the1: {dk_p3_11} the2: {dk_p3_22} the3: {dk_p3_33}":
                                break
                        time.sleep(2)
                        self.ser.write(self.data_box.encode())
                        for k in range(5):
                            read_serial = self.ser.readline().decode('utf-8').strip('\r\n')
                            print(read_serial)
                            if read_serial == 'the1: 0.00 the2: 0.00 the3: -30.00':
                                break
                        count_auto = 3
                        self.update_plot(the1_3, the2_3, the3_3)
                        self.update_plot(the1_3, (the2_3 + 15), the3_3)
                        self.update_plot(0, 0, -30)
                        print("Done_point_3")
                        time.sleep(2)
                    # Point_4
                    if count_auto == 3:
                        data4 = f'{the1_4} {the2_4} {the3_4} {1}'
                        self.ser.write(data4.encode())
                        ##
                        # print(the1_1)
                        dk_p4_1 = format(round(the1_4, 2), '.2f')
                        dk_p4_2 = format(round(the2_4, 2), '.2f')
                        dk_p4_3 = format(round(the3_4, 2), '.2f')
                        for k in range(5):
                            read_serial = self.ser.readline().decode('utf-8').strip('\r\n')
                            print(read_serial)
                            if read_serial == f"the1: {dk_p4_1} the2: {dk_p4_2} the3: {dk_p4_3}":
                                break
                        time.sleep(2)
                        data4_up = f"{the1_4} {the2_4 + 15} {the3_4} {1}"
                        self.ser.write(data4_up.encode())
                        dk_22 = format(round(the2_4 + 15, 2), '.2f')
                        for k in range(5):
                            read_serial = self.ser.readline().decode('utf-8').strip('\r\n')
                            print(read_serial)
                            if read_serial == f"the1: {dk_p4_1} the2: {dk_22} the3: {dk_p4_3}":
                                break
                        time.sleep(2)
                        self.ser.write(self.data_box.encode())
                        for k in range(5):
                            read_serial = self.ser.readline().decode('utf-8').strip('\r\n')
                            print(read_serial)
                            if read_serial == 'the1: 0.00 the2: 0.00 the3: -30.00':
                                break
                        count_auto = 4
                        self.update_plot(the1_4, the2_4, the3_4)
                        self.update_plot(the1_4, (the2_4 + 15), the3_4)
                        self.update_plot(0, 0, -30)
                        print("Done_point_4")
                        time.sleep(2)
                    if count_auto == 4:
                        data5 = f'{the1_5} {the2_5} {the3_5} {1}'
                        self.ser.write(data5.encode())
                        ##
                        dk_1 = format(round(the1_5, 2), '.2f')
                        dk_2 = format(round(the2_5, 2), '.2f')
                        dk_3 = format(round(the3_5, 2), '.2f')
                        for k in range(5):
                            read_serial = self.ser.readline().decode('utf-8').strip('\r\n')
                            print(read_serial)
                            if read_serial == f"the1: {dk_1} the2: {dk_2} the3: {dk_3}":
                                break
                        time.sleep(2)
                        data5_up = f"{the1_5} {the2_5 + 15} {the3_5} {1}"
                        self.ser.write(data5_up.encode())
                        dk_22 = format(round(the2_5 + 15, 2), '.2f')
                        for k in range(5):
                            read_serial = self.ser.readline().decode('utf-8').strip('\r\n')
                            print(read_serial)
                            if read_serial == f"the1: {dk_1} the2: {dk_22} the3: {dk_3}":
                                break
                        time.sleep(2)
                        self.ser.write(self.data_box.encode())
                        for k in range(5):
                            read_serial = self.ser.readline().decode('utf-8').strip('\r\n')
                            print(read_serial)
                            if read_serial == 'the1: 0.00 the2: 0.00 the3: -30.00':
                                break
                        count_auto = 5
                        self.update_plot(the1_5, the2_5, the3_5)
                        self.update_plot(the1_5, (the2_5 + 15), the3_5)
                        self.update_plot(0, 0, -30)
                        print("Done_point_5")
                        time.sleep(2)
                    if count_auto == 5:
                        # self.the_1_list, self.the_2_list, self.the_3_list = [], [], []
                        # self.uic.table_the.clearContents()
                        print("Đã hoàn thành xong 5 điểm")
                else:
                    QMessageBox.critical(self.second_win, "Robot", "Không đúng 5 bộ nghiệm")
        except (Exception, ValueError, TypeError) as e:
            print(f"Def_Run_Auto -- Error: {e}")

    def send_value_manual_auto(self):
        try:
            if self.mode_ser:
                if not self.mode_send:
                    QMessageBox.critical(self.second_win, "Lỗi", "Vui lòng chọn chế độ")
                else:
                    # send value Manual
                    if self.mode_manual:
                        if self.forward_mode:  # ĐHT
                            the1 = self.uic.theta1.text()
                            the2 = self.uic.theta2.text()
                            the3 = self.uic.theta3.text()
                            if not get_value(the1) or not get_value(the2) or not get_value(the3):
                                QMessageBox.critical(self.second_win, "Lỗi", "Vui lòng nhập giá trị hợp lệ!")
                                self.uic.theta1.setText("")
                                self.uic.theta2.setText("")
                                self.uic.theta3.setText("")
                            else:
                                # Tính toán giá trị x, y, z từ the1, the2, the3 bằng hàm fw_kinematics
                                x, y, z = fw_kinematics(float(the1), float(the2), float(the3))
                                # Update giá trị x, y, z lên GUI
                                self.uic.Px.setText(str(x))
                                self.uic.Py.setText(str(y))
                                self.uic.Pz.setText(str(z))
                                self.plot_3dof(str(the1), str(the2), str(the3))
                                self.update_plot(the1, the2, the3)
                                # Gửi giá trị từ Python tới Arduino
                                data_send = f"{the1} {the2} {the3} {1}"
                                self.ser.write(data_send.encode())
                                # Đọc kết quả từ Arduino
                        else:  # ĐHN
                            x = self.uic.Px.text()
                            y = self.uic.Py.text()
                            z = self.uic.Pz.text()
                            if not get_value(x) or not get_value(y) or not get_value(z):
                                QMessageBox.critical(self.second_win, "Robot", "Vui lòng nhập giá trị hợp lệ!")
                                self.uic.Px.setText("")
                                self.uic.Py.setText("")
                                self.uic.Pz.setText("")
                            else:
                                # Tính toán giá trị x, y, z từ the1, the2, the3 bằng hàm fw_kinematics
                                calc_inv = inv_kinematics(float(x), float(y), float(z))
                                if calc_inv is not None:
                                    the1, the2, the3 = calc_inv
                                    # Update giá trị theta lên
                                    self.uic.theta1.setText(str(the1))
                                    self.uic.theta2.setText(str(the2))
                                    self.uic.theta3.setText(str(the3))
                                    self.plot_3dof(str(the1), str(the2), str(the3))
                                    self.update_plot(the1, the2, the3)
                                    # Gửi giá trị từ Python tới Arduino
                                    data_send_inv = f"{the1} {the2} {the3} {1}"
                                    self.ser.write(data_send_inv.encode())
                                else:
                                    QMessageBox.critical(self.second_win, "Robot", "Giá trị không hợp lệ!")
                                    self.uic.Px.setText("")
                                    self.uic.Py.setText("")
                                    self.uic.Pz.setText("")
                    # # send value Auto
                    if self.mode_auto:
                        self.run_auto()
            else:
                QMessageBox.critical(self.second_win, "Robot", "Chưa kết nối Arduino")
        except (ValueError, TypeError, Exception) as e:
            print(f"Error -- Hàm Send_Value -- tính toán: {e}")

    def set_box_robot(self):
        if self.mode_ser:
            try:
                theta_1 = float(self.uic.theta1.text())
                theta_2 = float(self.uic.theta2.text())
                theta_3 = float(self.uic.theta3.text())
                dk1 = format(round(theta_1, 2), '.2f')
                dk2 = format(round(theta_2, 2), '.2f')
                dk3 = format(round(theta_3, 2), '.2f')
                if theta_1 == 0 and theta_2 == 0 and theta_3 == -30:
                    QMessageBox.about(self.second_win, "Robot", "Đang ở Box")
                else:
                    self.uic.Return_box.setEnabled(False)
                    for i in range(5):
                        read_serial = self.ser.readline().decode('utf-8').strip('\r\n')
                        print(read_serial)
                        if read_serial == f'the1: {dk1} the2: {dk2} the3: {dk3}':
                            break
                    print("Set_home + 15")
                    data1 = f"{theta_1} {theta_2 + 15} {theta_3} {1}"
                    self.ser.write(data1.encode())
                    time.sleep(2)
                    #
                    dk1 = format(round(theta_1, 2), '.2f')
                    dk2 = format(round(theta_2 + 15, 2), '.2f')
                    dk3 = format(round(theta_3, 2), '.2f')
                    for i in range(5):
                        read_serial = self.ser.readline().decode('utf-8').strip('\r\n')
                        print(read_serial)
                        if read_serial == f'the1: {dk1} the2: {dk2} the3: {dk3}':
                            break
                    print("Set_home final")
                    time.sleep(2)
                    self.ser.write(self.data_box.encode())
                    for i in range(5):
                        read_serial = self.ser.readline().decode('utf-8').strip('\r\n')
                        print(read_serial)
                        if read_serial == 'the1: 0.00 the2: 0.00 the3: -30.00':
                            break
                    QMessageBox.about(self.second_win, "Robot", "Set Box Ok")
                    self.uic.Run.setEnabled(True)
                    self.uic.Return_box.setEnabled(True)
                    self.uic.theta1.setText("0")
                    self.uic.theta2.setText("0")
                    self.uic.theta3.setText("-30")
                    self.update_plot(theta_1, (theta_2 + 15), theta_3)
                    self.update_plot(0, 0, -30)
            except (Exception, ValueError,TypeError) as e:
                self.ser.write(self.data_box.encode())
                self.uic.Return_box.setEnabled(True)
                self.uic.Run.setEnabled(True)
                self.uic.Return_box.setEnabled(True)
                self.uic.theta1.setText("0")
                self.uic.theta2.setText("0")
                self.uic.theta3.setText("-30")
                x, y, z = fw_kinematics(0, 0, -30)
                self.uic.Px.setText(str(x))
                self.uic.Py.setText(str(y))
                self.uic.Pz.setText(str(z))
                self.update_plot(0, 0, -30)

                QMessageBox.about(self.second_win, "Robot", "Set Box Ok")
                print(f'Return_box -- Error: {e}')
        else:
            QMessageBox.critical(self.second_win, "Robot", "Chưa kết nối Arduino")

    def show_login(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.page_login)

    def show_setting(self):
        try:
            # self.login.hide()
            self.uic.table_the.hide()
            self.port_check = list_com_ports()
            self.uic.Port_2.addItem(self.port_check)
            self.uic.stackedWidget.setCurrentWidget(self.uic.page_setting)
        except (Exception, ValueError, TypeError) as e:
            print(f"Error port -- {e} ")

    def show_graph(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.page_graph)

    def show_manual(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.page_Manual)
        if self.mode_ser:
            self.uic.led_on_off.setStyleSheet('background-color: green;border-radius: 5px; border: 1px solid black;')
        else:
            self.uic.led_on_off.setStyleSheet('background-color: gray;border-radius: 5px; border: 1px solid black;')

    def animate_button(self):
        # animation1, animation2, animation3, animation4 = None, None, None, None
        # animation5, animation6, animation7 = None, None, None
        if self.Side_Menu_num == 0:
            self.animation1 = QtCore.QPropertyAnimation(self.uic.frame, b"geometry")
            self.animation1.setDuration(200)  # Duration of animation in milliseconds
            self.animation1.setStartValue(QtCore.QRect(40, 60, 91, 652))
            self.animation1.setEndValue(QtCore.QRect(40, 60, 201, 652))
            self.animation1.start()

            self.animation2 = QtCore.QPropertyAnimation(self.uic.Home, b"geometry")
            self.animation2.setDuration(200)
            self.animation2.setStartValue(QtCore.QRect(20, 80, 50, 45))
            self.animation2.setEndValue(QtCore.QRect(20, 80, 170, 45))
            self.animation2.start()

            self.animation3 = QtCore.QPropertyAnimation(self.uic.Setting, b"geometry")
            self.animation3.setDuration(200)  # Duration of animation in milliseconds
            self.animation3.setStartValue(QtCore.QRect(20, 140, 50, 45))
            self.animation3.setEndValue(QtCore.QRect(20, 140, 170, 45))
            self.animation3.start()

            self.animation4 = QtCore.QPropertyAnimation(self.uic.Manual, b"geometry")
            self.animation4.setDuration(200)
            self.animation4.setStartValue(QtCore.QRect(20, 200, 50, 45))
            self.animation4.setEndValue(QtCore.QRect(20, 200, 170, 45))
            self.animation4.start()

            self.animation5 = QtCore.QPropertyAnimation(self.uic.graph, b"geometry")
            self.animation5.setDuration(200)
            self.animation5.setStartValue(QtCore.QRect(20, 260, 50, 45))
            self.animation5.setEndValue(QtCore.QRect(20, 260, 170, 45))
            self.animation5.start()

            self.animation6 = QtCore.QPropertyAnimation(self.uic.Camera, b"geometry")
            self.animation6.setDuration(200)
            self.animation6.setStartValue(QtCore.QRect(20, 320, 50, 45))
            self.animation6.setEndValue(QtCore.QRect(20, 320, 170, 45))
            self.animation6.start()

            self.animation7 = QtCore.QPropertyAnimation(self.uic.Menu, b"geometry")
            self.animation7.setDuration(200)
            self.animation7.setStartValue(QtCore.QRect(20, 20, 50, 45))
            self.animation7.setEndValue(QtCore.QRect(20, 20, 170, 45))
            self.animation7.start()

            self.Side_Menu_num = 1

        else:
            self.animation1 = QtCore.QPropertyAnimation(self.uic.frame, b"geometry")
            self.animation1.setDuration(200)  # Duration of animation in milliseconds
            self.animation1.setStartValue(QtCore.QRect(40, 60, 201, 652))
            self.animation1.setEndValue(QtCore.QRect(40, 60, 91, 652))
            self.animation1.start()

            self.animation2 = QtCore.QPropertyAnimation(self.uic.Home, b"geometry")
            self.animation2.setDuration(200)
            self.animation2.setStartValue(QtCore.QRect(20, 80, 170, 45))
            self.animation2.setEndValue(QtCore.QRect(20, 80, 50, 45))
            self.animation2.start()

            self.animation3 = QtCore.QPropertyAnimation(self.uic.Setting, b"geometry")
            self.animation3.setDuration(200)  # Duration of animation in milliseconds
            self.animation3.setStartValue(QtCore.QRect(20, 140, 170, 45))
            self.animation3.setEndValue(QtCore.QRect(20, 140, 50, 45))
            self.animation3.start()

            self.animation4 = QtCore.QPropertyAnimation(self.uic.Manual, b"geometry")
            self.animation4.setDuration(200)
            self.animation4.setStartValue(QtCore.QRect(20, 200, 170, 45))
            self.animation4.setEndValue(QtCore.QRect(20, 200, 50, 45))
            self.animation4.start()

            self.animation5 = QtCore.QPropertyAnimation(self.uic.graph, b"geometry")
            self.animation5.setDuration(200)
            self.animation5.setStartValue(QtCore.QRect(20, 260, 170, 45))
            self.animation5.setEndValue(QtCore.QRect(20, 260, 50, 45))
            self.animation5.start()

            self.animation6 = QtCore.QPropertyAnimation(self.uic.Camera, b"geometry")
            self.animation6.setDuration(200)
            self.animation6.setStartValue(QtCore.QRect(20, 320, 170, 45))
            self.animation6.setEndValue(QtCore.QRect(20, 320, 50, 45))
            self.animation6.start()

            self.animation7 = QtCore.QPropertyAnimation(self.uic.Menu, b"geometry")
            self.animation7.setDuration(200)
            self.animation7.setStartValue(QtCore.QRect(20, 20, 170, 45))
            self.animation7.setEndValue(QtCore.QRect(20, 20, 50, 45))
            self.animation7.start()

            self.Side_Menu_num = 0

    def plot_3dof(self, the1, the2, the3, l1=L1, l2=L2, lx=Lx, ly=Ly):
        the1_rad = radians(float(the1))
        the2_rad = radians(float(the2))
        the3_rad = radians(float(the3))

        self.ax.clear()

        # dof 1
        x1, y1, z1 = (cos(the1_rad) * l1,
                      sin(the1_rad) * l1,
                      d1 * cos(pi / 4))
        # dof 2
        x2, y2, z2 = (cos(the1_rad) * (l1 + l2 * cos(the2_rad)),
                      sin(the1_rad) * (l1 + l2 * cos(the2_rad)),
                      l2 * sin(the2_rad))
        # dof 3
        x3, y3, z3 = (cos(the1_rad) * (l1 + lx * cos(the2_rad + the3_rad) - ly * sin(the2_rad + the3_rad)
                                       + l2 * cos(the2_rad)) + 1.6,
                      sin(the1_rad) * (l1 + lx * cos(the2_rad + the3_rad) - ly * sin(the2_rad + the3_rad)
                                       + l2 * cos(the2_rad)) - 0.5,
                      ly * cos(the2_rad + the3_rad) + lx * sin(the2_rad + the3_rad) + l2 * sin(the2_rad))

        # Vẽ từ đế tới gốc màu hồng
        self.ax.plot([0, 0], [0, 0], [0, -(12.3 + 5.2 + 0.3)], 'm-', linewidth=3, marker='o')

        # Vẽ  từ gốc đến vị trí x1 màu blue
        self.ax.plot([0, x1], [0, y1], [0, z1], 'b-', linewidth=3, marker='o')

        # Vẽ từ x1 tới x2 màu đỏ
        self.ax.plot([x1, x2], [y1, y2], [z1, z2], 'r-', linewidth=3, marker='o')

        # Vẽ từ x2 tới x3 màu đen
        self.ax.plot([x2, x3], [y2, y3], [z2, z3], 'k-', linewidth=3, marker='o')

        self.ax.set_xlim([-40, 40])
        self.ax.set_ylim([-40, 40])
        self.ax.set_zlim([-40, 40])
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        # text_place = f'{x3: .2f}, {y3:.2f}, {z3:.2f})'
        # self.ax.text(x3, y3, z3, text_place, color='red')
        self.ax.grid(True)
        self.canvas.draw()

    def update_plot(self, the_1, the_2, the_3):
        try:
            # Time
            the1_val = float(the_1)
            the2_val = float(the_2)
            the3_val = float(the_3)
            self.the1_grap.append(the1_val)
            self.the2_grap.append(the2_val)
            self.the3_grap.append(the3_val)
            # print(len(self.the1))
            # Get old value
            if len(self.the1_grap) > 1 and len(self.the2_grap) > 1 and len(self.the3_grap) > 1:
                the1_old = float(self.the1_grap[-2])
                the2_old = float(self.the2_grap[-2])
                the3_old = float(self.the3_grap[-2])
            else:
                the1_old, the2_old, the3_old = 0, 0, 0

            # Plot theta_value
            self.ax_1.plot([len(self.the1_grap) - 1, len(self.the1_grap)], [the1_old, the1_val], marker='o',color='b')
            self.ax_2.plot([len(self.the2_grap) - 1, len(self.the2_grap)], [the2_old, the2_val], marker='o',color='m')
            self.ax_3.plot([len(self.the3_grap) - 1, len(self.the3_grap)], [the3_old, the3_val], marker='o',color='g')
            # Set tittle
            self.ax_1.set_title('Theta 1')
            self.ax_1.set_ylabel('Giá trị 1')
            self.ax_2.set_title('Theta 2')
            self.ax_2.set_ylabel('Giá trị 2')
            self.ax_3.set_title('Theta 3')
            self.ax_3.set_ylabel('Giá trị 3')
            # Set_text với ha: căn lề cho text, va: vị trí cho text
            # color, ha, va = 'red', 'center', 'bottom'
            # a = 1
            # self.ax_1.text(len(self.the1_grap), the1_val, f'{the1_val:.4f}', color=color, ha=ha, va=va, alpha=a)
            # self.ax_2.text(len(self.the2_grap), the2_val, f'{the2_val:.4f}', color=color, ha=ha, va=va, alpha=a)
            # self.ax_3.text(len(self.the3_grap), the3_val, f'{the3_val:.4f}', color=color, ha=ha, va=va, alpha=a)
            # Set Grid
            self.ax_1.grid(True)
            self.ax_2.grid(True)
            self.ax_3.grid(True)
            self.canvas_2d.figure.tight_layout()
            self.canvas_2d.draw()
        except Exception as e:
            print("Plot_update -- ", e)

    def show_camera(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.page_cam)

    def set_robot_cam(self):
        try:
            if self.mode_ser:
                data_set = f'{50} {10} {-20} {0}'
                self.ser.write(data_set.encode())
                self.plot_3dof(str(50),str(10),str(-20))
                self.update_plot(50, 10, -20)
            else:
                QMessageBox.critical(self.second_win, "Robot", "Chưa kết nối Arduino")
        except Exception as e:
            print(f"Error -- Def_set_robot_cam: {e}")

    def show_wed_cam(self, frame):
        try:
            if self.mode_ser:
                self.mode_cam = True
                rgb_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_img.shape
                byte_line = ch * w
                cnv_to_qt = QImage(bytes(rgb_img.data), w, h, byte_line, QImage.Format_RGB888)
                p = cnv_to_qt.scaled(800, 600, Qt.KeepAspectRatio)
                self.frame_img = QPixmap.fromImage(p)
                self.uic.screen_cam.setPixmap(self.frame_img)

            else:
                QMessageBox.critical(self.second_win, "Robot", "Chưa kết nối Arduino")
        except Exception as e:
            print(f"Error -- Def_show_wed_cam: {e}")

    def stop_camera(self):
        try:
            # self.mode_cam = False
            self.thread[2].stop()
            self.uic.screen_cam.clear()
            # data_home = f"{0} {0} {0} {0}"
            # self.ser.write(data_home.encode())
        except Exception as e:
            print(f"Error -- Def_stop_camera: {e}")

    def scan_cam(self, frame):
        # pass
        try:
            if not self.mode_cam:
                QMessageBox.critical(self.second_win, "Robot", "Chưa bật cam")
            else:
                frame = cv2.convertScaleAbs(frame)
                rgb_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                circle_object_position = detect_circle_object(rgb_img)
                red_object_position = detect_red_object(rgb_img)
                h, w, ch = rgb_img.shape
                byte_line = ch * w
                q_img = QImage(bytes(rgb_img.data), w, h, byte_line, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(q_img)
                self.uic.screen_cam.setPixmap(pixmap)
                real_width_cm = 37.8  # Kích thước x
                real_height_cm = 29.2  # Kích thước y
                kalman_filter = KalmanFilter(state_dim=4, measurement_dim=2)  # 4D state: x, y, vx, vy
                image_width = frame.shape[1]
                image_height = frame.shape[0]
                calibration_factor_x = real_width_cm / image_width
                calibration_factor_y = real_height_cm / image_height
                x_values = []
                y_values = []
                processing_circle = False
                count = 0
                if not processing_circle and count == 0:
                    if circle_object_position is not None and red_object_position is not None:
                        # Xác định vị trí của vật màu đỏ (đã biết)
                        red_known_position = (15, 0)
                        x_circle_cm, y_circle_cm = pixel_to_cm(circle_object_position[0], circle_object_position[1],
                                                               calibration_factor_x, calibration_factor_y)
                        x_red_cm, y_red_cm = pixel_to_cm(red_object_position[0], red_object_position[1],
                                                         calibration_factor_x, calibration_factor_y)
                        measurement = np.array([x_circle_cm, y_circle_cm], dtype=np.float32)
                        kalman_filter.update(measurement)
                        # Tính sự chênh lệch giữa vị trí của vật tròn và vật màu đỏ
                        diff_x_cm = x_circle_cm - x_red_cm
                        diff_y_cm = y_red_cm - y_circle_cm
                        # Áp dụng chênh lệch này vào vị trí đã biết của vật màu đỏ để tìm vị trí của vật tròn
                        x_circle_known = red_known_position[0] + diff_x_cm
                        y_circle_known = red_known_position[1] + diff_y_cm
                        x_values.append(x_circle_known)
                        y_values.append(y_circle_known)
                        print(x_circle_known, y_circle_known)
                        self.uic.Px_cam.setText(str(round(x_circle_known, 3)))
                        self.uic.Py_cam.setText(str(round(y_circle_known, 3)))
                        self.uic.Pz_cam.setText(str(round(0)))
        except (Exception, ValueError, TypeError) as e:
            print(f"Error -- Def_Scan_cam: {e}")

    def send_value_cam(self):
        if not self.mode_cam:
            QMessageBox.critical(self.second_win, "Robot", "Chưa bật cam")
        else:
            x_cam = self.uic.Px_cam.text()
            y_cam = self.uic.Py_cam.text()
            z_cam = self.uic.Pz_cam.text()
            the1_cam, the2_cam, the3_cam = inv_kinematics(float(x_cam),float(y_cam),float(z_cam))
            print(the1_cam, the2_cam, the3_cam)
            time.sleep(2)
            data_cam = f'{the1_cam} {the2_cam} {the3_cam} {1}'
            self.ser.write(data_cam.encode())
            dk_cam1 = format(round(the1_cam, 2), '.2f')
            dk_cam2 = format(round(the2_cam, 2), '.2f')
            dk_cam3 = format(round(the3_cam, 2), '.2f')
            for i in range(5):
                read_serial = self.ser.readline().decode('utf-8').strip('\r\n')
                print(read_serial)
                if read_serial == f'the1: {dk_cam1} the2: {dk_cam2} the3: {dk_cam3}':
                    break
            time.sleep(3)
            print("Set_box final")
            self.ser.write(self.data_box.encode())
            time.sleep(3)
            for i in range(5):
                read_serial = self.ser.readline().decode('utf-8').strip('\r\n')
                print(read_serial)
                if read_serial == 'the1: 0.00 the2: 0.00 the3: -30.00':
                    break
            print("pass")
            self.uic.theta1.setText("0")
            self.uic.theta2.setText("0")
            self.uic.theta3.setText("-30")
            x, y, z = fw_kinematics(0, 0, -30)
            self.uic.Px.setText(str(x))
            self.uic.Py.setText(str(y))
            self.uic.Pz.setText(str(z))
            self.update_plot(0, 0, -30)
            QMessageBox.about(self.second_win, "Robot", "Cập nhật giá trị thành công!")


class ThreadClass(QtCore.QThread):
    signal = pyqtSignal(str)
    frame_update = pyqtSignal(np.ndarray)

    def __init__(self, index=0, ser_1=None):
        super().__init__()
        self.index = index
        self.ser_1 = ser_1
        self.is_runing = False
        self.paused = False  # Biến cờ để kiểm soát việc tạm dừng
        print(f"Start...thread-{self.index}")

    def run(self):
        self.is_runing = True
        if self.index == 1:
            while self.is_runing:
                if not self.is_runing:
                    break
                else:
                    result = self.ser_1.readline().decode('utf-8').strip('\r\n')
                    print(result)
                    self.signal.emit(result)
                    if result == 'the1: 0.00 the2: -151.50 the3: 150.00':
                        break
        if self.index == 2:
            cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
            while self.is_runing:
                if not self.is_runing:
                    cap.release()
                    break
                else:
                    ret, frame = cap.read()
                    if ret:
                        self.frame_update.emit(frame)

    def stop(self):
        print(f"Stopping...thread-{self.index}:", )
        self.is_runing = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    # main_win.show()
    sys.exit(app.exec())
