# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Display2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1958, 960)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-20, 0, 2000, 1500))
        self.widget.setStyleSheet("background-color:rgba(255,255,255,255);")
        self.widget.setObjectName("widget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget)
        self.stackedWidget.setGeometry(QtCore.QRect(110, 55, 1825, 1000))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.Panel)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_login = QtWidgets.QWidget()
        self.page_login.setObjectName("page_login")
        self.login = QtWidgets.QWidget(self.page_login)
        self.login.setGeometry(QtCore.QRect(0, -20, 1821, 1001))
        self.login.setStyleSheet("background-color:rgba(255,255,255,255)")
        self.login.setObjectName("login")
        self.label_16 = QtWidgets.QLabel(self.login)
        self.label_16.setGeometry(QtCore.QRect(360, 450, 1121, 121))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color:#0e659a;")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.login)
        self.label_17.setGeometry(QtCore.QRect(20, 280, 1811, 111))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color:#0e659a;")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_19 = QtWidgets.QLabel(self.login)
        self.label_19.setGeometry(QtCore.QRect(540, 40, 791, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:3px solid rgba(46, 82, 101, 200);\n"
"color:#0e659a;\n"
"\n"
"")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.login)
        self.label_20.setGeometry(QtCore.QRect(750, 130, 381, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color:#0e659a;")
        self.label_20.setObjectName("label_20")
        self.start = QtWidgets.QPushButton(self.login)
        self.start.setGeometry(QtCore.QRect(1500, 800, 230, 110))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.start.setFont(font)
        self.start.setStyleSheet("\n"
"\n"
"QPushButton#start{\n"
"\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(10, 90, 190, 229), stop: 1 rgba(85, 98, 112,\n"
"\n"
"226));\n"
"\n"
"color:rgba(255, 255, 255, 210);\n"
"\n"
"border-radius:15px;\n"
"\n"
"}\n"
"\n"
"QPushButton#start:hover{\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84,\n"
"\n"
"226));\n"
"}\n"
"\n"
"QPushButton#start:pressed{\n"
"\n"
"padding-left:5px;\n"
"\n"
"padding-top:5px;\n"
" background-color:rgba(150, 123, 111, 255);\n"
"}`\n"
"")
        self.start.setObjectName("start")
        self.label_21 = QtWidgets.QLabel(self.login)
        self.label_21.setGeometry(QtCore.QRect(50, 50, 121, 111))
        self.label_21.setStyleSheet("image: url(:/icon/download.png);")
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("icon/download.png"))
        self.label_21.setScaledContents(True)
        self.label_21.setObjectName("label_21")
        self.label_29 = QtWidgets.QLabel(self.login)
        self.label_29.setGeometry(QtCore.QRect(210, 40, 151, 121))
        self.label_29.setText("")
        self.label_29.setPixmap(QtGui.QPixmap("icon/logo_khoa_dien.png"))
        self.label_29.setScaledContents(True)
        self.label_29.setObjectName("label_29")
        self.label_35 = QtWidgets.QLabel(self.login)
        self.label_35.setGeometry(QtCore.QRect(1480, 40, 131, 121))
        self.label_35.setText("")
        self.label_35.setPixmap(QtGui.QPixmap("icon/download (1).png"))
        self.label_35.setScaledContents(True)
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.login)
        self.label_36.setGeometry(QtCore.QRect(1650, 50, 131, 111))
        self.label_36.setText("")
        self.label_36.setPixmap(QtGui.QPixmap("icon/logo_sr.png"))
        self.label_36.setScaledContents(True)
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.login)
        self.label_37.setGeometry(QtCore.QRect(50, 690, 571, 51))
        self.label_37.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.login)
        self.label_38.setGeometry(QtCore.QRect(50, 740, 811, 51))
        self.label_38.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.login)
        self.label_39.setGeometry(QtCore.QRect(370, 790, 571, 51))
        self.label_39.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.login)
        self.label_40.setGeometry(QtCore.QRect(370, 840, 571, 51))
        self.label_40.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.label_40.setObjectName("label_40")
        self.stackedWidget.addWidget(self.page_login)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.Button_Quaylai_5 = QtWidgets.QPushButton(self.page_3)
        self.Button_Quaylai_5.setGeometry(QtCore.QRect(10, 5, 150, 60))
        self.Button_Quaylai_5.setMinimumSize(QtCore.QSize(20, 20))
        self.Button_Quaylai_5.setMaximumSize(QtCore.QSize(190, 60))
        self.Button_Quaylai_5.setAutoFillBackground(False)
        self.Button_Quaylai_5.setStyleSheet("QPushButton#Button_Quaylai_5{\n"
"       border-bottom-right-radius :20px;\n"
"    font: 75 17pt \"MS Shell Dlg 2\";\n"
"    \n"
"    /*border: 3px solid rgb(230, 230, 230);*/\n"
"    color: rgb(0, 0, 0);\n"
"    \n"
"    background-color: rgb(220, 220, 220);\n"
"    background-color: #CCFFFF;\n"
"\n"
"}\n"
"QPushButton#Button_Quaylai_5:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color: #0e71aa;\n"
"}\n"
"")
        self.Button_Quaylai_5.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_Quaylai_5.setIcon(icon)
        self.Button_Quaylai_5.setIconSize(QtCore.QSize(50, 50))
        self.Button_Quaylai_5.setObjectName("Button_Quaylai_5")
        self.frame_7 = QtWidgets.QFrame(self.page_3)
        self.frame_7.setGeometry(QtCore.QRect(70, 110, 1700, 720))
        self.frame_7.setStyleSheet(" background-color: rgb(230, 230, 230);\n"
" border-radius: 10px;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.frame_9 = QtWidgets.QFrame(self.frame_7)
        self.frame_9.setGeometry(QtCore.QRect(1420, 560, 1421, 901))
        self.frame_9.setStyleSheet(" background-color: rgb(230, 230, 230);\n"
" border-radius: 10px;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.frame_8 = QtWidgets.QFrame(self.page_3)
        self.frame_8.setGeometry(QtCore.QRect(80, 120, 1681, 701))
        self.frame_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tabWidget_3.setFont(font)
        self.tabWidget_3.setStyleSheet("")
        self.tabWidget_3.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_3.setIconSize(QtCore.QSize(30, 60))
        self.tabWidget_3.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget_3.setUsesScrollButtons(True)
        self.tabWidget_3.setMovable(False)
        self.tabWidget_3.setTabBarAutoHide(True)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setStyleSheet("  border-radius: 30px;\n"
"border:none;")
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.frame_12 = QtWidgets.QFrame(self.tab_5)
        self.frame_12.setStyleSheet(" background-color: rgb(255,255,255);\n"
" border-radius: 10px;")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame_12)
        self.groupBox_4.setGeometry(QtCore.QRect(100, 40, 671, 301))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet("gridline-color: rgb(0, 0, 0);\n"
"selection-color: rgb(85, 170, 255);\n"
"border: 1px solid black;\n"
"border-radius: 5px;")
        self.groupBox_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_4.setObjectName("groupBox_4")
        self.widget_14 = QtWidgets.QWidget(self.groupBox_4)
        self.widget_14.setGeometry(QtCore.QRect(10, 30, 170, 250))
        self.widget_14.setObjectName("widget_14")
        self.label_6 = QtWidgets.QLabel(self.widget_14)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 150, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_18 = QtWidgets.QLabel(self.widget_14)
        self.label_18.setGeometry(QtCore.QRect(10, 80, 150, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_27 = QtWidgets.QLabel(self.widget_14)
        self.label_27.setGeometry(QtCore.QRect(10, 140, 150, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.widget_14)
        self.label_28.setGeometry(QtCore.QRect(10, 200, 150, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.widget_5 = QtWidgets.QWidget(self.groupBox_4)
        self.widget_5.setGeometry(QtCore.QRect(190, 30, 461, 251))
        self.widget_5.setObjectName("widget_5")
        self.min_vel_x = QtWidgets.QLineEdit(self.widget_5)
        self.min_vel_x.setGeometry(QtCore.QRect(20, 20, 420, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.min_vel_x.setFont(font)
        self.min_vel_x.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
"padding-bottom:7px;")
        self.min_vel_x.setAlignment(QtCore.Qt.AlignCenter)
        self.min_vel_x.setObjectName("min_vel_x")
        self.max_vel_x = QtWidgets.QLineEdit(self.widget_5)
        self.max_vel_x.setGeometry(QtCore.QRect(20, 80, 420, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.max_vel_x.setFont(font)
        self.max_vel_x.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
"padding-bottom:7px;")
        self.max_vel_x.setAlignment(QtCore.Qt.AlignCenter)
        self.max_vel_x.setObjectName("max_vel_x")
        self.min_vel_theta = QtWidgets.QLineEdit(self.widget_5)
        self.min_vel_theta.setGeometry(QtCore.QRect(20, 140, 420, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.min_vel_theta.setFont(font)
        self.min_vel_theta.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
"padding-bottom:7px;")
        self.min_vel_theta.setAlignment(QtCore.Qt.AlignCenter)
        self.min_vel_theta.setObjectName("min_vel_theta")
        self.max_vel_theta = QtWidgets.QLineEdit(self.widget_5)
        self.max_vel_theta.setGeometry(QtCore.QRect(20, 200, 420, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.max_vel_theta.setFont(font)
        self.max_vel_theta.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
"padding-bottom:7px;")
        self.max_vel_theta.setAlignment(QtCore.Qt.AlignCenter)
        self.max_vel_theta.setObjectName("max_vel_theta")
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame_12)
        self.groupBox_5.setGeometry(QtCore.QRect(100, 380, 671, 191))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setStyleSheet("gridline-color: rgb(0, 0, 0);\n"
"selection-color: rgb(85, 170, 255);\n"
"border: 1px solid black;\n"
"border-radius: 5px;")
        self.groupBox_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_5.setObjectName("groupBox_5")
        self.widget_17 = QtWidgets.QWidget(self.groupBox_5)
        self.widget_17.setGeometry(QtCore.QRect(10, 30, 170, 141))
        self.widget_17.setObjectName("widget_17")
        self.label_30 = QtWidgets.QLabel(self.widget_17)
        self.label_30.setGeometry(QtCore.QRect(10, 20, 150, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.widget_17)
        self.label_31.setGeometry(QtCore.QRect(10, 80, 150, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.widget_6 = QtWidgets.QWidget(self.groupBox_5)
        self.widget_6.setGeometry(QtCore.QRect(190, 30, 461, 141))
        self.widget_6.setObjectName("widget_6")
        self.acc_lim_x = QtWidgets.QLineEdit(self.widget_6)
        self.acc_lim_x.setGeometry(QtCore.QRect(20, 20, 420, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.acc_lim_x.setFont(font)
        self.acc_lim_x.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
"padding-bottom:7px;")
        self.acc_lim_x.setAlignment(QtCore.Qt.AlignCenter)
        self.acc_lim_x.setObjectName("acc_lim_x")
        self.acc_lim_theta = QtWidgets.QLineEdit(self.widget_6)
        self.acc_lim_theta.setGeometry(QtCore.QRect(20, 80, 420, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.acc_lim_theta.setFont(font)
        self.acc_lim_theta.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
"padding-bottom:7px;")
        self.acc_lim_theta.setAlignment(QtCore.Qt.AlignCenter)
        self.acc_lim_theta.setObjectName("acc_lim_theta")
        self.groupBox_6 = QtWidgets.QGroupBox(self.frame_12)
        self.groupBox_6.setGeometry(QtCore.QRect(850, 120, 671, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setStyleSheet("gridline-color: rgb(0, 0, 0);\n"
"selection-color: rgb(85, 170, 255);\n"
"border: 1px solid black;\n"
"border-radius: 5px;")
        self.groupBox_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_6.setObjectName("groupBox_6")
        self.widget_18 = QtWidgets.QWidget(self.groupBox_6)
        self.widget_18.setGeometry(QtCore.QRect(10, 30, 181, 81))
        self.widget_18.setObjectName("widget_18")
        self.label_32 = QtWidgets.QLabel(self.widget_18)
        self.label_32.setGeometry(QtCore.QRect(5, 20, 171, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.widget_7 = QtWidgets.QWidget(self.groupBox_6)
        self.widget_7.setGeometry(QtCore.QRect(200, 30, 461, 81))
        self.widget_7.setObjectName("widget_7")
        self.lower_threshold = QtWidgets.QLineEdit(self.widget_7)
        self.lower_threshold.setGeometry(QtCore.QRect(30, 20, 420, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lower_threshold.setFont(font)
        self.lower_threshold.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
"padding-bottom:7px;")
        self.lower_threshold.setAlignment(QtCore.Qt.AlignCenter)
        self.lower_threshold.setObjectName("lower_threshold")
        self.groupBox_7 = QtWidgets.QGroupBox(self.frame_12)
        self.groupBox_7.setGeometry(QtCore.QRect(850, 410, 671, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setStyleSheet("gridline-color: rgb(0, 0, 0);\n"
"selection-color: rgb(85, 170, 255);\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"")
        self.groupBox_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_7.setObjectName("groupBox_7")
        self.widget_21 = QtWidgets.QWidget(self.groupBox_7)
        self.widget_21.setGeometry(QtCore.QRect(10, 30, 181, 81))
        self.widget_21.setObjectName("widget_21")
        self.label_33 = QtWidgets.QLabel(self.widget_21)
        self.label_33.setGeometry(QtCore.QRect(10, 20, 161, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.widget_8 = QtWidgets.QWidget(self.groupBox_7)
        self.widget_8.setGeometry(QtCore.QRect(200, 30, 461, 81))
        self.widget_8.setObjectName("widget_8")
        self.port_usb = QtWidgets.QLabel(self.widget_8)
        self.port_usb.setGeometry(QtCore.QRect(20, 20, 430, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.port_usb.setFont(font)
        self.port_usb.setStyleSheet("border: 1px solid black;\n"
"border-radius: 5px;")
        self.port_usb.setText("")
        self.port_usb.setAlignment(QtCore.Qt.AlignCenter)
        self.port_usb.setObjectName("port_usb")
        self.update_setting = QtWidgets.QPushButton(self.frame_12)
        self.update_setting.setGeometry(QtCore.QRect(1560, 40, 81, 61))
        self.update_setting.setMinimumSize(QtCore.QSize(0, 0))
        self.update_setting.setMaximumSize(QtCore.QSize(220, 100))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.update_setting.setFont(font)
        self.update_setting.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.update_setting.setStyleSheet("QPushButton#update_setting{\n"
"    border-radius: 15px;\n"
"    font: 75 16pt \"MS Shell Dlg 2\";\n"
"    border: 1px solid #CCFFFF;\n"
"    background-color: #CCFFFF;\n"
"}\n"
"\n"
"QPushButton#update_setting:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color:#0e71aa;\n"
"}\n"
"QPushButton#update_setting:checked {\n"
"background-color:#0e71aa;\n"
"\n"
"}\n"
"")
        self.update_setting.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.update_setting.setIcon(icon1)
        self.update_setting.setIconSize(QtCore.QSize(40, 50))
        self.update_setting.setObjectName("update_setting")
        self.gridLayout_14.addWidget(self.frame_12, 0, 0, 1, 1)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("D:/backup_robot_tieptan/letan_10062024/list_table.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_3.addTab(self.tab_5, icon2, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setStyleSheet("border:none;")
        self.tab_6.setObjectName("tab_6")
        self.frame_15 = QtWidgets.QFrame(self.tab_6)
        self.frame_15.setGeometry(QtCore.QRect(0, 0, 1655, 608))
        self.frame_15.setStyleSheet(" background-color: rgb(255,255,255);\n"
" border-radius: 10px;")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.groupBox_16 = QtWidgets.QGroupBox(self.frame_15)
        self.groupBox_16.setGeometry(QtCore.QRect(500, 100, 671, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_16.setFont(font)
        self.groupBox_16.setStyleSheet("gridline-color: rgb(0, 0, 0);\n"
"selection-color: rgb(85, 170, 255);\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"")
        self.groupBox_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_16.setObjectName("groupBox_16")
        self.widget_38 = QtWidgets.QWidget(self.groupBox_16)
        self.widget_38.setGeometry(QtCore.QRect(10, 30, 181, 81))
        self.widget_38.setObjectName("widget_38")
        self.label_50 = QtWidgets.QLabel(self.widget_38)
        self.label_50.setGeometry(QtCore.QRect(10, 20, 161, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_50.setFont(font)
        self.label_50.setObjectName("label_50")
        self.widget_39 = QtWidgets.QWidget(self.groupBox_16)
        self.widget_39.setGeometry(QtCore.QRect(200, 30, 461, 81))
        self.widget_39.setObjectName("widget_39")
        self.widget_40 = QtWidgets.QWidget(self.widget_39)
        self.widget_40.setGeometry(QtCore.QRect(20, 20, 431, 35))
        self.widget_40.setObjectName("widget_40")
        self.groupBox_17 = QtWidgets.QGroupBox(self.frame_15)
        self.groupBox_17.setGeometry(QtCore.QRect(500, 300, 671, 191))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_17.setFont(font)
        self.groupBox_17.setStyleSheet("gridline-color: rgb(0, 0, 0);\n"
"selection-color: rgb(85, 170, 255);\n"
"border: 1px solid black;\n"
"border-radius: 5px;")
        self.groupBox_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_17.setObjectName("groupBox_17")
        self.widget_41 = QtWidgets.QWidget(self.groupBox_17)
        self.widget_41.setGeometry(QtCore.QRect(10, 30, 181, 141))
        self.widget_41.setObjectName("widget_41")
        self.label_51 = QtWidgets.QLabel(self.widget_41)
        self.label_51.setGeometry(QtCore.QRect(10, 20, 150, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_51.setFont(font)
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self.widget_41)
        self.label_52.setGeometry(QtCore.QRect(10, 80, 150, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_52.setFont(font)
        self.label_52.setObjectName("label_52")
        self.widget_42 = QtWidgets.QWidget(self.groupBox_17)
        self.widget_42.setGeometry(QtCore.QRect(200, 30, 461, 141))
        self.widget_42.setObjectName("widget_42")
        self.widget_43 = QtWidgets.QWidget(self.widget_42)
        self.widget_43.setGeometry(QtCore.QRect(20, 20, 431, 35))
        self.widget_43.setObjectName("widget_43")
        self.widget_44 = QtWidgets.QWidget(self.widget_42)
        self.widget_44.setGeometry(QtCore.QRect(20, 80, 431, 35))
        self.widget_44.setObjectName("widget_44")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("D:/backup_robot_tieptan/letan_10062024/table_else.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_3.addTab(self.tab_6, icon3, "")
        self.gridLayout_13.addWidget(self.tabWidget_3, 0, 1, 1, 1)
        self.Button_done_4 = QtWidgets.QPushButton(self.page_3)
        self.Button_done_4.setGeometry(QtCore.QRect(1550, 850, 220, 100))
        self.Button_done_4.setMinimumSize(QtCore.QSize(220, 100))
        self.Button_done_4.setMaximumSize(QtCore.QSize(220, 100))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Button_done_4.setFont(font)
        self.Button_done_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Button_done_4.setStyleSheet("QPushButton#Button_done_4{\n"
"    border-radius: 25px;\n"
"    font: 75 16pt \"MS Shell Dlg 2\";\n"
"    border: 1px solid #CCFFFF;\n"
"    background-color: #CCFFFF;\n"
"}\n"
"\n"
"QPushButton#Button_done_4:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color:#0e71aa;\n"
"}\n"
"QPushButton#Button_done_4:checked {\n"
"background-color:#0e71aa;\n"
"\n"
"}\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_done_4.setIcon(icon4)
        self.Button_done_4.setIconSize(QtCore.QSize(40, 50))
        self.Button_done_4.setObjectName("Button_done_4")
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.frame_4 = QtWidgets.QFrame(self.page_2)
        self.frame_4.setGeometry(QtCore.QRect(20, 80, 1400, 881))
        self.frame_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tabWidget = QtWidgets.QTabWidget(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(30, 60))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("  border-radius: 30px;\n"
"border:none;")
        self.tab.setObjectName("tab")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab)
        self.scrollArea_2.setStyleSheet("")
        self.scrollArea_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea_2.setLineWidth(0)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1362, 818))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_9.setObjectName("gridLayout_9")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_9.addItem(spacerItem, 6, 0, 1, 1)
        self.Button_9_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.Button_9_2.setMinimumSize(QtCore.QSize(300, 100))
        self.Button_9_2.setMaximumSize(QtCore.QSize(300, 100))
        self.Button_9_2.setStyleSheet("QPushButton#Button_9_2{\n"
"  border-radius: 20px;\n"
"    font: 75 28pt \"MS Shell Dlg 2\";\n"
"    border: 1px solid #CCFFFF;\n"
"    background-color: #CCFFFF;\n"
"\n"
"}\n"
"QPushButton#Button_9_2:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color: #0e71aa;\n"
"}\n"
"QPushButton#Button_9_2:checked {\n"
"background-color: #0e71aa;\n"
"\n"
"}\n"
"")
        self.Button_9_2.setObjectName("Button_9_2")
        self.gridLayout_9.addWidget(self.Button_9_2, 10, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_9.addItem(spacerItem1, 9, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_9.addItem(spacerItem2, 9, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_9.addItem(spacerItem3, 6, 2, 1, 1)
        self.Button_10_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.Button_10_2.setMinimumSize(QtCore.QSize(300, 100))
        self.Button_10_2.setMaximumSize(QtCore.QSize(300, 100))
        self.Button_10_2.setStyleSheet("QPushButton#Button_10_2{\n"
"    border-radius: 20px;\n"
"    font: 75 28pt \"MS Shell Dlg 2\";\n"
"    border: 1px solid #CCFFFF;\n"
"    background-color: #CCFFFF;\n"
"\n"
"}\n"
"\n"
"QPushButton#Button_10_2:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color: #0e71aa;\n"
"}\n"
"QPushButton#Button_10_2:checked {\n"
"background-color: #0e71aa;\n"
"\n"
"}\n"
"")
        self.Button_10_2.setObjectName("Button_10_2")
        self.gridLayout_9.addWidget(self.Button_10_2, 10, 2, 1, 1)
        self.Button_7_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.Button_7_2.setMinimumSize(QtCore.QSize(300, 100))
        self.Button_7_2.setMaximumSize(QtCore.QSize(300, 100))
        self.Button_7_2.setStyleSheet("QPushButton#Button_7_2{\n"
"     border-radius: 20px;\n"
"    font: 75 28pt \"MS Shell Dlg 2\";\n"
"    border: 1px solid #CCFFFF;\n"
"    background-color: #CCFFFF;\n"
"\n"
"}\n"
"\n"
"QPushButton#Button_7_2:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color: #0e71aa;\n"
"}\n"
"QPushButton#Button_7_2:checked {\n"
"background-color: #0e71aa;\n"
"\n"
"}\n"
"")
        self.Button_7_2.setObjectName("Button_7_2")
        self.gridLayout_9.addWidget(self.Button_7_2, 8, 0, 1, 1)
        self.Button_2_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.Button_2_2.setMinimumSize(QtCore.QSize(300, 100))
        self.Button_2_2.setMaximumSize(QtCore.QSize(300, 100))
        self.Button_2_2.setStyleSheet("QPushButton#Button_2_2{\n"
"     border-radius: 20px;\n"
"    font: 75 28pt \"MS Shell Dlg 2\";\n"
"    border: 1px solid #CCFFFF;\n"
"    background-color: #CCFFFF;\n"
"\n"
"}\n"
"\n"
"QPushButton#Button_2_2:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color: #0e71aa;\n"
"}\n"
"QPushButton#Button_2_2:checked {\n"
"background-color: #0e71aa;\n"
"\n"
"}\n"
"")
        self.Button_2_2.setObjectName("Button_2_2")
        self.gridLayout_9.addWidget(self.Button_2_2, 1, 2, 1, 1)
        self.Button_5_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.Button_5_2.setMinimumSize(QtCore.QSize(300, 100))
        self.Button_5_2.setMaximumSize(QtCore.QSize(300, 100))
        self.Button_5_2.setStyleSheet("QPushButton#Button_5_2{\n"
"     border-radius: 20px;\n"
"    font: 75 28pt \"MS Shell Dlg 2\";\n"
"    border: 1px solid #CCFFFF;\n"
"background-color:#CCFFFF;\n"
"}\n"
"\n"
"QPushButton#Button_5_2:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color: #0e71aa;\n"
"}\n"
"QPushButton#Button_5_2:checked {\n"
"background-color: #0e71aa;\n"
"\n"
"}\n"
"")
        self.Button_5_2.setObjectName("Button_5_2")
        self.gridLayout_9.addWidget(self.Button_5_2, 5, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_9.addItem(spacerItem4, 4, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_9.addItem(spacerItem5, 4, 0, 1, 1)
        self.Button_6_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.Button_6_2.setMinimumSize(QtCore.QSize(300, 100))
        self.Button_6_2.setMaximumSize(QtCore.QSize(300, 100))
        self.Button_6_2.setStyleSheet("QPushButton#Button_6_2\n"
"{\n"
"     border-radius: 20px;\n"
"    font: 75 28pt \"MS Shell Dlg 2\";\n"
"    border: 1px solid #CCFFFF;\n"
"    background-color: #CCFFFF;\n"
"\n"
"}\n"
"\n"
"QPushButton#Button_6_2:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color: #0e71aa;\n"
"}\n"
"QPushButton#Button_6_2:checked {\n"
"background-color: #0e71aa;\n"
"\n"
"}\n"
"")
        self.Button_6_2.setObjectName("Button_6_2")
        self.gridLayout_9.addWidget(self.Button_6_2, 5, 2, 1, 1)
        self.Button_8_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.Button_8_2.setMinimumSize(QtCore.QSize(300, 100))
        self.Button_8_2.setMaximumSize(QtCore.QSize(300, 100))
        self.Button_8_2.setStyleSheet("QPushButton#Button_8_2{\n"
"     border-radius: 20px;\n"
"    font: 75 28pt \"MS Shell Dlg 2\";\n"
"    border: 1px solid #CCFFFF;\n"
"    background-color: #CCFFFF;\n"
"\n"
"}\n"
"\n"
"QPushButton#Button_8_2:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color: #0e71aa;\n"
"}\n"
"QPushButton#Button_8_2:checked {\n"
"background-color: #0e71aa;\n"
"\n"
"}\n"
"")
        self.Button_8_2.setObjectName("Button_8_2")
        self.gridLayout_9.addWidget(self.Button_8_2, 8, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_9.addItem(spacerItem6, 0, 2, 1, 1)
        self.Button_4_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.Button_4_2.setMinimumSize(QtCore.QSize(300, 100))
        self.Button_4_2.setMaximumSize(QtCore.QSize(300, 100))
        self.Button_4_2.setStyleSheet("QPushButton#Button_4_2{\n"
"     border-radius: 20px;\n"
"    font: 75 28pt \"MS Shell Dlg 2\";\n"
"    border: 1px solid #CCFFFF;\n"
"background-color: #CCFFFF;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#Button_4_2:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color: #0e71aa;\n"
"}\n"
"QPushButton#Button_4_2:checked {\n"
"background-color: #0e71aa;\n"
"\n"
"}\n"
"")
        self.Button_4_2.setObjectName("Button_4_2")
        self.gridLayout_9.addWidget(self.Button_4_2, 3, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_9.addItem(spacerItem7, 11, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_9.addItem(spacerItem8, 2, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_9.addItem(spacerItem9, 11, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_9.addItem(spacerItem10, 2, 2, 1, 1)
        self.Button_3_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.Button_3_2.setMinimumSize(QtCore.QSize(300, 100))
        self.Button_3_2.setMaximumSize(QtCore.QSize(300, 100))
        self.Button_3_2.setStyleSheet("QPushButton#Button_3_2{\n"
"     border-radius: 20px;\n"
"    font: 75 28pt \"MS Shell Dlg 2\";\n"
"    border: 1px solid #CCFFFF;\n"
"    background-color:#CCFFFF;\n"
"}\n"
"\n"
"QPushButton#Button_3_2:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color: #0e71aa;\n"
"}\n"
"QPushButton#Button_3_2:checked {\n"
"background-color: \n"
"\n"
"}\n"
"")
        self.Button_3_2.setObjectName("Button_3_2")
        self.gridLayout_9.addWidget(self.Button_3_2, 3, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem11, 1, 1, 1, 1)
        self.Button_1_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.Button_1_2.setMinimumSize(QtCore.QSize(300, 100))
        self.Button_1_2.setMaximumSize(QtCore.QSize(300, 100))
        self.Button_1_2.setStyleSheet("QPushButton#Button_1_2{\n"
"    border-radius: 20px;\n"
"    font: 75 28pt \"MS Shell Dlg 2\";\n"
"    border: 1px solid #CCFFFF;\n"
"\n"
"    background-color: #CCFFFF;\n"
"\n"
"}\n"
"\n"
"QPushButton#Button_1_2:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color: #0e71aa;\n"
"}\n"
"QPushButton#Button_1_2:checked {\n"
"background-color: #0e71aa;\n"
"\n"
"}\n"
"")
        self.Button_1_2.setObjectName("Button_1_2")
        self.gridLayout_9.addWidget(self.Button_1_2, 1, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_9.addItem(spacerItem12, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_10.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../../../../backup_robot_tieptan/letan_10062024/list_table.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon5, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setStyleSheet("border:none;")
        self.tab_2.setObjectName("tab_2")
        self.Button_khuvuccho_2 = QtWidgets.QPushButton(self.tab_2)
        self.Button_khuvuccho_2.setGeometry(QtCore.QRect(500, 300, 300, 100))
        self.Button_khuvuccho_2.setMinimumSize(QtCore.QSize(300, 100))
        self.Button_khuvuccho_2.setMaximumSize(QtCore.QSize(300, 100))
        self.Button_khuvuccho_2.setStyleSheet("QPushButton#Button_khuvuccho_2{\n"
"    border-radius: 20px;\n"
"    font: 75 20pt \"MS Shell Dlg 2\";\n"
"    border: 1px solid rgb(230, 230, 230);\n"
"\n"
"background-color: #CCFFFF;\n"
"\n"
"}\n"
"\n"
"QPushButton#Button_khuvuccho_2:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color: #0e71aa;\n"
"}\n"
"QPushButton#Button_khuvuccho_2:checked {\n"
"background-color: #0e71aa;\n"
"\n"
"}\n"
"")
        self.Button_khuvuccho_2.setObjectName("Button_khuvuccho_2")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../../../../backup_robot_tieptan/letan_10062024/table_else.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon6, "")
        self.gridLayout_6.addWidget(self.tabWidget, 0, 1, 1, 1)
        self.Button_Quaylai = QtWidgets.QPushButton(self.page_2)
        self.Button_Quaylai.setGeometry(QtCore.QRect(10, 5, 150, 60))
        self.Button_Quaylai.setMinimumSize(QtCore.QSize(20, 20))
        self.Button_Quaylai.setMaximumSize(QtCore.QSize(190, 60))
        self.Button_Quaylai.setAutoFillBackground(False)
        self.Button_Quaylai.setStyleSheet("QPushButton#Button_Quaylai{\n"
"       border-bottom-right-radius :20px;\n"
"    font: 75 17pt \"MS Shell Dlg 2\";\n"
"    \n"
"    /*border: 3px solid rgb(230, 230, 230);*/\n"
"    color: rgb(0, 0, 0);\n"
"    \n"
"    background-color: rgb(220, 220, 220);\n"
"    background-color: #CCFFFF;\n"
"\n"
"}\n"
"QPushButton#Button_Quaylai:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color: #0e71aa;\n"
"}\n"
"")
        self.Button_Quaylai.setText("")
        self.Button_Quaylai.setIcon(icon)
        self.Button_Quaylai.setIconSize(QtCore.QSize(50, 50))
        self.Button_Quaylai.setObjectName("Button_Quaylai")
        self.frame_chua = QtWidgets.QFrame(self.page_2)
        self.frame_chua.setGeometry(QtCore.QRect(1470, 180, 301, 461))
        self.frame_chua.setStyleSheet(" background-color: rgb(230, 230, 230);\n"
" border-radius: 10px;")
        self.frame_chua.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_chua.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_chua.setObjectName("frame_chua")
        self.listWidget_ds = QtWidgets.QListWidget(self.frame_chua)
        self.listWidget_ds.setGeometry(QtCore.QRect(19, 100, 261, 331))
        self.listWidget_ds.setStyleSheet("\n"
" border-radius: 20px;\n"
" background-color: rgb(230, 230, 230);\n"
" font: 75 30pt \"MS Shell Dlg 2\";")
        self.listWidget_ds.setObjectName("listWidget_ds")
        self.thutu = QtWidgets.QPushButton(self.frame_chua)
        self.thutu.setGeometry(QtCore.QRect(10, 10, 271, 60))
        self.thutu.setMinimumSize(QtCore.QSize(100, 10))
        self.thutu.setMaximumSize(QtCore.QSize(300, 100))
        self.thutu.setStyleSheet("QPushButton#thutu{\n"
"     border-radius: 10px;\n"
"    font: 60 20pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(255,255,255);\n"
"\n"
"}\n"
"\n"
"\n"
"")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icon/document.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.thutu.setIcon(icon7)
        self.thutu.setIconSize(QtCore.QSize(50, 50))
        self.thutu.setObjectName("thutu")
        self.Button_done_2 = QtWidgets.QPushButton(self.page_2)
        self.Button_done_2.setGeometry(QtCore.QRect(1470, 670, 301, 131))
        self.Button_done_2.setMinimumSize(QtCore.QSize(220, 100))
        self.Button_done_2.setMaximumSize(QtCore.QSize(400, 200))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Button_done_2.setFont(font)
        self.Button_done_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Button_done_2.setStyleSheet("QPushButton#Button_done_2{\n"
"    border-radius: 25px;\n"
"    font: 75 25pt \"MS Shell Dlg 2\";\n"
"    border: 1px solid #CCFFFF;\n"
"    background-color: #CCFFFF;\n"
"}\n"
"\n"
"QPushButton#Button_done_2:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color: #0e71aa;\n"
"}\n"
"QPushButton#Button_done_:checked {\n"
"background-color: #0e71aa;\n"
"}\n"
"")
        self.Button_done_2.setIcon(icon4)
        self.Button_done_2.setIconSize(QtCore.QSize(40, 50))
        self.Button_done_2.setObjectName("Button_done_2")
        self.frame_6 = QtWidgets.QFrame(self.page_2)
        self.frame_6.setGeometry(QtCore.QRect(10, 70, 1421, 901))
        self.frame_6.setStyleSheet(" background-color: rgb(230, 230, 230);\n"
" border-radius: 10px;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.Button_LoadMap = QtWidgets.QPushButton(self.page_2)
        self.Button_LoadMap.setGeometry(QtCore.QRect(1510, 70, 220, 80))
        self.Button_LoadMap.setMinimumSize(QtCore.QSize(0, 0))
        self.Button_LoadMap.setMaximumSize(QtCore.QSize(220, 100))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Button_LoadMap.setFont(font)
        self.Button_LoadMap.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Button_LoadMap.setStyleSheet("QPushButton#Button_LoadMap{\n"
"    border-radius: 15px;\n"
"    font: 75 16pt \"MS Shell Dlg 2\";\n"
"    border: 1px solid #CCFFFF;\n"
"    background-color: #CCFFFF;\n"
"}\n"
"\n"
"QPushButton#Button_LoadMap:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color:#0e71aa;\n"
"}\n"
"QPushButton#Button_LoadMap:checked {\n"
"background-color:#0e71aa;\n"
"\n"
"}\n"
"")
        self.Button_LoadMap.setIcon(icon1)
        self.Button_LoadMap.setIconSize(QtCore.QSize(40, 50))
        self.Button_LoadMap.setObjectName("Button_LoadMap")
        self.frame_6.raise_()
        self.frame_4.raise_()
        self.Button_Quaylai.raise_()
        self.frame_chua.raise_()
        self.Button_done_2.raise_()
        self.Button_LoadMap.raise_()
        self.stackedWidget.addWidget(self.page_2)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_11 = QtWidgets.QLabel(self.page_4)
        self.label_11.setGeometry(QtCore.QRect(580, 5, 611, 101))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_final = QtWidgets.QLabel(self.page_4)
        self.label_final.setGeometry(QtCore.QRect(580, 130, 610, 151))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.label_final.setFont(font)
        self.label_final.setStyleSheet("border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.label_final.setText("")
        self.label_final.setAlignment(QtCore.Qt.AlignCenter)
        self.label_final.setObjectName("label_final")
        self.screen_cam_4 = QtWidgets.QLabel(self.page_4)
        self.screen_cam_4.setGeometry(QtCore.QRect(100, 300, 750, 600))
        self.screen_cam_4.setStyleSheet("border: 2px solid black;\n"
"border-radius:10px;\n"
"")
        self.screen_cam_4.setText("")
        self.screen_cam_4.setObjectName("screen_cam_4")
        self.screen_cam_5 = QtWidgets.QLabel(self.page_4)
        self.screen_cam_5.setGeometry(QtCore.QRect(950, 300, 750, 600))
        self.screen_cam_5.setStyleSheet("border: 2px solid black;\n"
"border-radius:10px;\n"
"")
        self.screen_cam_5.setText("")
        self.screen_cam_5.setObjectName("screen_cam_5")
        self.stackedWidget.addWidget(self.page_4)
        self.page_setting = QtWidgets.QWidget()
        self.page_setting.setObjectName("page_setting")
        self.Display_setting = QtWidgets.QWidget(self.page_setting)
        self.Display_setting.setGeometry(QtCore.QRect(0, 0, 1821, 981))
        self.Display_setting.setStyleSheet("background-color:rgba(255,255,255,255)")
        self.Display_setting.setObjectName("Display_setting")
        self.label_15 = QtWidgets.QLabel(self.Display_setting)
        self.label_15.setGeometry(QtCore.QRect(290, 440, 131, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.label_10 = QtWidgets.QLabel(self.Display_setting)
        self.label_10.setGeometry(QtCore.QRect(530, 120, 55, 16))
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.Arrow_vinh = QtWidgets.QLabel(self.Display_setting)
        self.Arrow_vinh.setGeometry(QtCore.QRect(440, 170, 111, 71))
        self.Arrow_vinh.setStyleSheet("")
        self.Arrow_vinh.setText("")
        self.Arrow_vinh.setObjectName("Arrow_vinh")
        self.screen_cam_3 = QtWidgets.QLabel(self.Display_setting)
        self.screen_cam_3.setGeometry(QtCore.QRect(250, 100, 1300, 800))
        self.screen_cam_3.setStyleSheet("border: 2px solid black;\n"
"border-radius:10px;")
        self.screen_cam_3.setText("")
        self.screen_cam_3.setObjectName("screen_cam_3")
        self.Button_Quaylai_6 = QtWidgets.QPushButton(self.Display_setting)
        self.Button_Quaylai_6.setGeometry(QtCore.QRect(10, 5, 150, 60))
        self.Button_Quaylai_6.setMinimumSize(QtCore.QSize(20, 20))
        self.Button_Quaylai_6.setMaximumSize(QtCore.QSize(190, 60))
        self.Button_Quaylai_6.setAutoFillBackground(False)
        self.Button_Quaylai_6.setStyleSheet("QPushButton#Button_Quaylai_6{\n"
"       border-bottom-right-radius :20px;\n"
"    font: 75 17pt \"MS Shell Dlg 2\";\n"
"    \n"
"    /*border: 3px solid rgb(230, 230, 230);*/\n"
"    color: rgb(0, 0, 0);\n"
"    \n"
"    background-color: rgb(220, 220, 220);\n"
"    background-color: #CCFFFF;\n"
"\n"
"}\n"
"QPushButton#Button_Quaylai_6:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color: #0e71aa;\n"
"}\n"
"")
        self.Button_Quaylai_6.setText("")
        self.Button_Quaylai_6.setIcon(icon)
        self.Button_Quaylai_6.setIconSize(QtCore.QSize(50, 50))
        self.Button_Quaylai_6.setObjectName("Button_Quaylai_6")
        self.stackedWidget.addWidget(self.page_setting)
        self.page_Manual = QtWidgets.QWidget()
        self.page_Manual.setObjectName("page_Manual")
        self.Display_Manual = QtWidgets.QWidget(self.page_Manual)
        self.Display_Manual.setGeometry(QtCore.QRect(0, 0, 1781, 981))
        self.Display_Manual.setStyleSheet("background-color:rgba(255,255,255,255);")
        self.Display_Manual.setObjectName("Display_Manual")
        self.Button_Quaylai_4 = QtWidgets.QPushButton(self.Display_Manual)
        self.Button_Quaylai_4.setGeometry(QtCore.QRect(10, 5, 150, 60))
        self.Button_Quaylai_4.setMinimumSize(QtCore.QSize(20, 20))
        self.Button_Quaylai_4.setMaximumSize(QtCore.QSize(190, 60))
        self.Button_Quaylai_4.setAutoFillBackground(False)
        self.Button_Quaylai_4.setStyleSheet("QPushButton#Button_Quaylai_4{\n"
"       border-bottom-right-radius :20px;\n"
"    font: 75 17pt \"MS Shell Dlg 2\";\n"
"    \n"
"    /*border: 3px solid rgb(230, 230, 230);*/\n"
"    color: rgb(0, 0, 0);\n"
"    \n"
"    background-color: rgb(220, 220, 220);\n"
"    background-color: #CCFFFF;\n"
"\n"
"}\n"
"QPushButton#Button_Quaylai_4:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color: #0e71aa;\n"
"}\n"
"")
        self.Button_Quaylai_4.setText("")
        self.Button_Quaylai_4.setIcon(icon)
        self.Button_Quaylai_4.setIconSize(QtCore.QSize(50, 50))
        self.Button_Quaylai_4.setObjectName("Button_Quaylai_4")
        self.frame_13 = QtWidgets.QFrame(self.Display_Manual)
        self.frame_13.setGeometry(QtCore.QRect(200, 100, 1431, 751))
        self.frame_13.setStyleSheet(" background-color: rgb(230, 230, 230);\n"
" border-radius: 10px;")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.frame_14 = QtWidgets.QFrame(self.frame_13)
        self.frame_14.setGeometry(QtCore.QRect(1420, 560, 1421, 901))
        self.frame_14.setStyleSheet(" background-color: rgb(230, 230, 230);\n"
" border-radius: 10px;")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_13)
        self.groupBox_2.setGeometry(QtCore.QRect(810, 20, 600, 370))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("gridline-color: rgb(0, 0, 0);\n"
" background-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"")
        self.groupBox_2.setObjectName("groupBox_2")
        self.widget_15 = QtWidgets.QWidget(self.groupBox_2)
        self.widget_15.setGeometry(QtCore.QRect(12, 20, 91, 341))
        self.widget_15.setObjectName("widget_15")
        self.label_7 = QtWidgets.QLabel(self.widget_15)
        self.label_7.setGeometry(QtCore.QRect(10, 50, 71, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget_15)
        self.label_8.setGeometry(QtCore.QRect(10, 250, 71, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget_15)
        self.label_9.setGeometry(QtCore.QRect(10, 150, 72, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.widget_16 = QtWidgets.QWidget(self.groupBox_2)
        self.widget_16.setGeometry(QtCore.QRect(108, 20, 481, 341))
        self.widget_16.setObjectName("widget_16")
        self.Px = QtWidgets.QLineEdit(self.widget_16)
        self.Px.setGeometry(QtCore.QRect(10, 50, 460, 36))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Px.setFont(font)
        self.Px.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
"padding-bottom:7px;")
        self.Px.setAlignment(QtCore.Qt.AlignCenter)
        self.Px.setObjectName("Px")
        self.Py = QtWidgets.QLineEdit(self.widget_16)
        self.Py.setGeometry(QtCore.QRect(10, 150, 460, 36))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Py.setFont(font)
        self.Py.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.Py.setAlignment(QtCore.Qt.AlignCenter)
        self.Py.setObjectName("Py")
        self.Pz = QtWidgets.QLineEdit(self.widget_16)
        self.Pz.setGeometry(QtCore.QRect(10, 250, 460, 36))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Pz.setFont(font)
        self.Pz.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.Pz.setAlignment(QtCore.Qt.AlignCenter)
        self.Pz.setObjectName("Pz")
        self.label_24 = QtWidgets.QLabel(self.widget_16)
        self.label_24.setGeometry(QtCore.QRect(400, 10, 70, 20))
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.groupBox = QtWidgets.QGroupBox(self.frame_13)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 600, 370))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("gridline-color: rgb(0, 0, 0);\n"
" background-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.groupBox.setObjectName("groupBox")
        self.widget_13 = QtWidgets.QWidget(self.groupBox)
        self.widget_13.setGeometry(QtCore.QRect(10, 20, 91, 341))
        self.widget_13.setObjectName("widget_13")
        self.label_2 = QtWidgets.QLabel(self.widget_13)
        self.label_2.setGeometry(QtCore.QRect(10, 250, 70, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget_13)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 70, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget_13)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 70, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.widget_2 = QtWidgets.QWidget(self.groupBox)
        self.widget_2.setGeometry(QtCore.QRect(108, 20, 481, 341))
        self.widget_2.setObjectName("widget_2")
        self.theta1 = QtWidgets.QLineEdit(self.widget_2)
        self.theta1.setGeometry(QtCore.QRect(10, 50, 460, 36))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.theta1.setFont(font)
        self.theta1.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
"padding-bottom:7px;")
        self.theta1.setAlignment(QtCore.Qt.AlignCenter)
        self.theta1.setObjectName("theta1")
        self.theta2 = QtWidgets.QLineEdit(self.widget_2)
        self.theta2.setGeometry(QtCore.QRect(10, 150, 460, 36))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.theta2.setFont(font)
        self.theta2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.theta2.setAlignment(QtCore.Qt.AlignCenter)
        self.theta2.setObjectName("theta2")
        self.theta3 = QtWidgets.QLineEdit(self.widget_2)
        self.theta3.setGeometry(QtCore.QRect(10, 250, 460, 36))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.theta3.setFont(font)
        self.theta3.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.theta3.setAlignment(QtCore.Qt.AlignCenter)
        self.theta3.setObjectName("theta3")
        self.label_23 = QtWidgets.QLabel(self.widget_2)
        self.label_23.setGeometry(QtCore.QRect(400, 10, 70, 20))
        self.label_23.setObjectName("label_23")
        self.widget_3 = QtWidgets.QWidget(self.frame_13)
        self.widget_3.setGeometry(QtCore.QRect(400, 450, 650, 281))
        self.widget_3.setStyleSheet("border: 1px solid ;\n"
" background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"")
        self.widget_3.setObjectName("widget_3")
        self.Return_box = QtWidgets.QPushButton(self.widget_3)
        self.Return_box.setGeometry(QtCore.QRect(20, 80, 180, 60))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Return_box.setFont(font)
        self.Return_box.setStyleSheet("QPushButton#Return_box\n"
"{\n"
"    border-radius: 10px;\n"
"    font: 75 16pt \"MS Shell Dlg 2\";\n"
"    border: 1px solid #CCFFFF;\n"
"    background-color: #CCFFFF;\n"
"\n"
"}\n"
"\n"
"QPushButton#Return_box:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color:  #0e71aa;\n"
"}\n"
"QPushButton#Return_box:checked {\n"
"background-color:  #0e71aa;\n"
"\n"
"}\n"
"")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icon/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Return_box.setIcon(icon8)
        self.Return_box.setIconSize(QtCore.QSize(40, 40))
        self.Return_box.setObjectName("Return_box")
        self.forward = QtWidgets.QPushButton(self.widget_3)
        self.forward.setGeometry(QtCore.QRect(20, 180, 180, 60))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.forward.setFont(font)
        self.forward.setStyleSheet("QPushButton#forward\n"
"{\n"
"    border-radius: 10px;\n"
"    font: 75 16pt \"MS Shell Dlg 2\";\n"
"    border: 1px solid #CCFFFF;\n"
"    background-color: #CCFFFF;\n"
"\n"
"}\n"
"\n"
"QPushButton#forward:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color:  #0e71aa;\n"
"}\n"
"QPushButton#forward:checked {\n"
"background-color:  #0e71aa;\n"
"\n"
"}\n"
"")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icon/robotics.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.forward.setIcon(icon9)
        self.forward.setIconSize(QtCore.QSize(40, 40))
        self.forward.setObjectName("forward")
        self.Run = QtWidgets.QPushButton(self.widget_3)
        self.Run.setGeometry(QtCore.QRect(235, 80, 180, 60))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Run.setFont(font)
        self.Run.setStyleSheet("QPushButton#Run\n"
"{\n"
"    border-radius: 10px;\n"
"    font: 75 16pt \"MS Shell Dlg 2\";\n"
"    border: 1px solid #CCFFFF;\n"
"    background-color: #CCFFFF;\n"
"\n"
"}\n"
"\n"
"QPushButton#Run:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color:  #0e71aa;\n"
"}\n"
"QPushButton#Run:checked {\n"
"background-color:  #0e71aa;\n"
"\n"
"}\n"
"")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icon/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Run.setIcon(icon10)
        self.Run.setIconSize(QtCore.QSize(40, 40))
        self.Run.setObjectName("Run")
        self.Inverse = QtWidgets.QPushButton(self.widget_3)
        self.Inverse.setGeometry(QtCore.QRect(235, 180, 180, 60))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Inverse.setFont(font)
        self.Inverse.setStyleSheet("QPushButton#Inverse\n"
"{\n"
"    border-radius: 10px;\n"
"    font: 75 16pt \"MS Shell Dlg 2\";\n"
"    border: 1px solid #CCFFFF;\n"
"    background-color: #CCFFFF;\n"
"\n"
"}\n"
"\n"
"QPushButton#Inverse:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color:  #0e71aa;\n"
"}\n"
"QPushButton#Inverse:checked {\n"
"background-color:  #0e71aa;\n"
"\n"
"}\n"
"")
        self.Inverse.setIcon(icon9)
        self.Inverse.setIconSize(QtCore.QSize(40, 40))
        self.Inverse.setObjectName("Inverse")
        self.Delete = QtWidgets.QPushButton(self.widget_3)
        self.Delete.setGeometry(QtCore.QRect(450, 80, 180, 60))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Delete.setFont(font)
        self.Delete.setStyleSheet("QPushButton#Delete\n"
"{\n"
"    border-radius: 10px;\n"
"    font: 75 16pt \"MS Shell Dlg 2\";\n"
"    border: 1px solid #CCFFFF;\n"
"    background-color: #CCFFFF;\n"
"\n"
"}\n"
"\n"
"QPushButton#Delete:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color:  #0e71aa;\n"
"}\n"
"QPushButton#Delete:checked {\n"
"background-color:  #0e71aa;\n"
"\n"
"}\n"
"")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icon/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Delete.setIcon(icon11)
        self.Delete.setIconSize(QtCore.QSize(40, 40))
        self.Delete.setObjectName("Delete")
        self.home = QtWidgets.QPushButton(self.widget_3)
        self.home.setGeometry(QtCore.QRect(450, 180, 180, 60))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.home.setFont(font)
        self.home.setStyleSheet("QPushButton#home\n"
"{\n"
"    border-radius: 10px;\n"
"    font: 75 16pt \"MS Shell Dlg 2\";\n"
"    border: 1px solid #CCFFFF;\n"
"    background-color: #CCFFFF;\n"
"\n"
"}\n"
"\n"
"QPushButton#home:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color:  #0e71aa;\n"
"}\n"
"QPushButton#home:checked {\n"
"background-color:  #0e71aa;\n"
"\n"
"}\n"
"")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icon/home-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home.setIcon(icon12)
        self.home.setIconSize(QtCore.QSize(40, 40))
        self.home.setObjectName("home")
        self.label_5 = QtWidgets.QLabel(self.widget_3)
        self.label_5.setGeometry(QtCore.QRect(30, 30, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.page_Manual)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.frame_5 = QtWidgets.QFrame(self.page)
        self.frame_5.setGeometry(QtCore.QRect(690, 80, 380, 804))
        self.frame_5.setStyleSheet("border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.Button_capnhat = QtWidgets.QPushButton(self.frame_5)
        self.Button_capnhat.setMinimumSize(QtCore.QSize(220, 100))
        self.Button_capnhat.setMaximumSize(QtCore.QSize(220, 100))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Button_capnhat.setFont(font)
        self.Button_capnhat.setStyleSheet("QPushButton#Button_capnhat\n"
"{\n"
"    border-radius: 25px;\n"
"    font: 75 16pt \"MS Shell Dlg 2\";\n"
"    border: 1px solid #CCFFFF;\n"
"    background-color: #CCFFFF;\n"
"\n"
"}\n"
"\n"
"QPushButton#Button_capnhat:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color:  #0e71aa;\n"
"}\n"
"QPushButton#Button_capnhat:checked {\n"
"background-color:  #0e71aa;\n"
"\n"
"}\n"
"")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("icon/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_capnhat.setIcon(icon13)
        self.Button_capnhat.setIconSize(QtCore.QSize(50, 50))
        self.Button_capnhat.setObjectName("Button_capnhat")
        self.gridLayout_5.addWidget(self.Button_capnhat, 0, 0, 1, 1)
        self.Button_luuMap = QtWidgets.QPushButton(self.frame_5)
        self.Button_luuMap.setMinimumSize(QtCore.QSize(220, 100))
        self.Button_luuMap.setMaximumSize(QtCore.QSize(220, 100))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Button_luuMap.setFont(font)
        self.Button_luuMap.setStyleSheet("QPushButton#Button_luuMap{\n"
"     border-radius: 25px;\n"
"    font: 75 16pt \"MS Shell Dlg 2\";\n"
"    border: 1px solid #CCFFFF;\n"
"    background-color: #CCFFFF;\n"
"\n"
"}\n"
"\n"
"QPushButton#Button_luuMap:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color: rgb(58, 192, 240);\n"
"}\n"
"QPushButton#Button_luuMap:checked {\n"
"background-color: rgb(58, 192, 255);\n"
"\n"
"}\n"
"")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("icon/gps.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_luuMap.setIcon(icon14)
        self.Button_luuMap.setIconSize(QtCore.QSize(50, 50))
        self.Button_luuMap.setObjectName("Button_luuMap")
        self.gridLayout_5.addWidget(self.Button_luuMap, 4, 0, 1, 1)
        self.Button_xoa = QtWidgets.QPushButton(self.frame_5)
        self.Button_xoa.setMinimumSize(QtCore.QSize(220, 100))
        self.Button_xoa.setMaximumSize(QtCore.QSize(220, 100))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Button_xoa.setFont(font)
        self.Button_xoa.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Button_xoa.setStyleSheet("QPushButton#Button_xoa\n"
"{\n"
"    border-radius: 25px;\n"
"    font: 75 16pt \"MS Shell Dlg 2\";\n"
"    border: 1px solid #CCFFFF;\n"
"    background-color: #CCFFFF;\n"
"\n"
"}\n"
"\n"
"QPushButton#Button_xoa:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color:  #0e71aa;\n"
"}\n"
"QPushButton#Button_xoa:checked {\n"
"background-color:  #0e71aa;\n"
"\n"
"}\n"
"")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("icon/minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_xoa.setIcon(icon15)
        self.Button_xoa.setIconSize(QtCore.QSize(50, 50))
        self.Button_xoa.setObjectName("Button_xoa")
        self.gridLayout_5.addWidget(self.Button_xoa, 2, 0, 1, 1)
        self.Button_add = QtWidgets.QPushButton(self.frame_5)
        self.Button_add.setMinimumSize(QtCore.QSize(220, 100))
        self.Button_add.setMaximumSize(QtCore.QSize(220, 100))
        self.Button_add.setStyleSheet("QPushButton#Button_add\n"
"{\n"
"    border-radius: 25px;\n"
"    font: 75 16pt \"MS Shell Dlg 2\";\n"
"    border: 1px solid #CCFFFF;\n"
"    background-color: #CCFFFF;\n"
"\n"
"}\n"
"\n"
"QPushButton#Button_add:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color:  #0e71aa;\n"
"}\n"
"QPushButton#Button_add:checked {\n"
"background-color:  #0e71aa;\n"
"\n"
"}\n"
"")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("icon/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_add.setIcon(icon16)
        self.Button_add.setIconSize(QtCore.QSize(50, 50))
        self.Button_add.setObjectName("Button_add")
        self.gridLayout_5.addWidget(self.Button_add, 1, 0, 1, 1)
        self.listWidget_dsban = QtWidgets.QListWidget(self.page)
        self.listWidget_dsban.setGeometry(QtCore.QRect(1200, 250, 500, 550))
        self.listWidget_dsban.setStyleSheet("font: 30pt \"MS Shell Dlg 2\";\n"
"border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.listWidget_dsban.setObjectName("listWidget_dsban")
        self.Button_Quaylai_2 = QtWidgets.QPushButton(self.page)
        self.Button_Quaylai_2.setGeometry(QtCore.QRect(10, 5, 150, 60))
        self.Button_Quaylai_2.setMinimumSize(QtCore.QSize(20, 20))
        self.Button_Quaylai_2.setMaximumSize(QtCore.QSize(190, 60))
        self.Button_Quaylai_2.setAutoFillBackground(False)
        self.Button_Quaylai_2.setStyleSheet("QPushButton#Button_Quaylai_2{\n"
"       border-bottom-right-radius :20px;\n"
"    font: 75 17pt \"MS Shell Dlg 2\";\n"
"    \n"
"    /*border: 3px solid rgb(230, 230, 230);*/\n"
"    color: rgb(0, 0, 0);\n"
"    \n"
"    background-color: rgb(220, 220, 220);\n"
"    background-color: #CCFFFF;\n"
"\n"
"}\n"
"QPushButton#Button_Quaylai_2:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color: #0e71aa;\n"
"}\n"
"")
        self.Button_Quaylai_2.setText("")
        self.Button_Quaylai_2.setIcon(icon)
        self.Button_Quaylai_2.setIconSize(QtCore.QSize(50, 50))
        self.Button_Quaylai_2.setObjectName("Button_Quaylai_2")
        self.label_xe_3 = QtWidgets.QLabel(self.page)
        self.label_xe_3.setGeometry(QtCore.QRect(120, 200, 500, 500))
        self.label_xe_3.setMinimumSize(QtCore.QSize(500, 200))
        self.label_xe_3.setMaximumSize(QtCore.QSize(500, 804))
        self.label_xe_3.setMouseTracking(False)
        self.label_xe_3.setToolTipDuration(7)
        self.label_xe_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_xe_3.setAutoFillBackground(False)
        self.label_xe_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"border: 3px solid rgb(255, 255, 255);")
        self.label_xe_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_xe_3.setText("")
        self.label_xe_3.setPixmap(QtGui.QPixmap("icon/deme_241121 (1).png"))
        self.label_xe_3.setScaledContents(True)
        self.label_xe_3.setWordWrap(False)
        self.label_xe_3.setObjectName("label_xe_3")
        self.label_14 = QtWidgets.QLabel(self.page)
        self.label_14.setGeometry(QtCore.QRect(50, 710, 601, 120))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_34 = QtWidgets.QLabel(self.page)
        self.label_34.setGeometry(QtCore.QRect(1250, 150, 390, 70))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("font: 30pt \"MS Shell Dlg 2\";\n"
"border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.label_34.setObjectName("label_34")
        self.stackedWidget.addWidget(self.page)
        self.page_graph = QtWidgets.QWidget()
        self.page_graph.setObjectName("page_graph")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.page_graph)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 1791, 891))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.Screen_graph = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.Screen_graph.setContentsMargins(0, 0, 0, 0)
        self.Screen_graph.setSpacing(0)
        self.Screen_graph.setObjectName("Screen_graph")
        self.frame_11 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setLineWidth(0)
        self.frame_11.setObjectName("frame_11")
        self.label_chonchedo = QtWidgets.QLabel(self.frame_11)
        self.label_chonchedo.setGeometry(QtCore.QRect(630, 50, 520, 200))
        self.label_chonchedo.setMaximumSize(QtCore.QSize(800, 200))
        self.label_chonchedo.setSizeIncrement(QtCore.QSize(800, 200))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.label_chonchedo.setFont(font)
        self.label_chonchedo.setStyleSheet("")
        self.label_chonchedo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_chonchedo.setObjectName("label_chonchedo")
        self.Button_Manu_2 = QtWidgets.QPushButton(self.frame_11)
        self.Button_Manu_2.setGeometry(QtCore.QRect(350, 350, 500, 250))
        self.Button_Manu_2.setMinimumSize(QtCore.QSize(500, 250))
        self.Button_Manu_2.setMaximumSize(QtCore.QSize(500, 250))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Button_Manu_2.setFont(font)
        self.Button_Manu_2.setStyleSheet("QPushButton#Button_Manu_2{\n"
"    border-radius: 30px;\n"
"    font: 75 26pt \"MS Shell Dlg 2\";\n"
"    border: 1px solid #CCFFFF;\n"
"    background-color: #CCFFFF;\n"
"/*border: 3px solid rgb(0, 0, 255);*/\n"
"\n"
"}\n"
"\n"
"QPushButton#Button_Manu_2:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color: #0e71aa;\n"
"}\n"
"QPushButton#Button_Manu_2:checked {\n"
"background-color: #0e71aa;\n"
"\n"
"}\n"
"")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("icon/xoafont_dieukhien.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_Manu_2.setIcon(icon17)
        self.Button_Manu_2.setIconSize(QtCore.QSize(100, 100))
        self.Button_Manu_2.setObjectName("Button_Manu_2")
        self.Button_Auto_2 = QtWidgets.QPushButton(self.frame_11)
        self.Button_Auto_2.setGeometry(QtCore.QRect(950, 350, 500, 250))
        self.Button_Auto_2.setMinimumSize(QtCore.QSize(500, 250))
        self.Button_Auto_2.setMaximumSize(QtCore.QSize(500, 250))
        self.Button_Auto_2.setStyleSheet("QPushButton#Button_Auto_2{\n"
"    border-radius: 30px;\n"
"    font: 75 26pt \"MS Shell Dlg 2\";\n"
"    border: 1px solid #CCFFFF;\n"
"    background-color: #CCFFFF;\n"
"    /*border: 3px solid rgb(0, 0, 255);*/\n"
"\n"
"}\n"
"QPushButton#Button_Auto_2:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"background-color:#0e71aa;\n"
"}\n"
"\n"
"")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("icon/xoafont_auto.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_Auto_2.setIcon(icon18)
        self.Button_Auto_2.setIconSize(QtCore.QSize(160, 160))
        self.Button_Auto_2.setObjectName("Button_Auto_2")
        self.Screen_graph.addWidget(self.frame_11)
        self.stackedWidget.addWidget(self.page_graph)
        self.page_cam = QtWidgets.QWidget()
        self.page_cam.setObjectName("page_cam")
        self.groupBox_3 = QtWidgets.QGroupBox(self.page_cam)
        self.groupBox_3.setGeometry(QtCore.QRect(750, 280, 281, 341))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("gridline-color: rgb(0, 0, 0);\n"
"selection-color: rgb(85, 170, 255);\n"
"border: 1px solid black;")
        self.groupBox_3.setObjectName("groupBox_3")
        self.widget_19 = QtWidgets.QWidget(self.groupBox_3)
        self.widget_19.setGeometry(QtCore.QRect(12, 33, 91, 291))
        self.widget_19.setObjectName("widget_19")
        self.label_26 = QtWidgets.QLabel(self.widget_19)
        self.label_26.setGeometry(QtCore.QRect(10, 50, 71, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.label_22 = QtWidgets.QLabel(self.widget_19)
        self.label_22.setGeometry(QtCore.QRect(10, 130, 72, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.label_25 = QtWidgets.QLabel(self.widget_19)
        self.label_25.setGeometry(QtCore.QRect(10, 210, 71, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.widget_20 = QtWidgets.QWidget(self.groupBox_3)
        self.widget_20.setGeometry(QtCore.QRect(108, 33, 161, 291))
        self.widget_20.setObjectName("widget_20")
        self.Px_cam = QtWidgets.QLineEdit(self.widget_20)
        self.Px_cam.setGeometry(QtCore.QRect(11, 44, 134, 36))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Px_cam.setFont(font)
        self.Px_cam.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
"padding-bottom:7px;")
        self.Px_cam.setAlignment(QtCore.Qt.AlignCenter)
        self.Px_cam.setObjectName("Px_cam")
        self.Py_cam = QtWidgets.QLineEdit(self.widget_20)
        self.Py_cam.setGeometry(QtCore.QRect(11, 120, 134, 36))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Py_cam.setFont(font)
        self.Py_cam.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.Py_cam.setAlignment(QtCore.Qt.AlignCenter)
        self.Py_cam.setObjectName("Py_cam")
        self.Pz_cam = QtWidgets.QLineEdit(self.widget_20)
        self.Pz_cam.setGeometry(QtCore.QRect(10, 200, 134, 36))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Pz_cam.setFont(font)
        self.Pz_cam.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.Pz_cam.setAlignment(QtCore.Qt.AlignCenter)
        self.Pz_cam.setObjectName("Pz_cam")
        self.screen_cam = QtWidgets.QLabel(self.page_cam)
        self.screen_cam.setGeometry(QtCore.QRect(20, 150, 700, 700))
        self.screen_cam.setStyleSheet("border: 2px solid black;\n"
"border-bottom-right-radius:10px;\n"
"border-bottom-left-radius:10px;")
        self.screen_cam.setText("")
        self.screen_cam.setObjectName("screen_cam")
        self.screen_cam_2 = QtWidgets.QLabel(self.page_cam)
        self.screen_cam_2.setGeometry(QtCore.QRect(1060, 150, 700, 700))
        self.screen_cam_2.setStyleSheet("border: 2px solid black;\n"
"border-bottom-right-radius:10px;\n"
"border-bottom-left-radius:10px;")
        self.screen_cam_2.setText("")
        self.screen_cam_2.setObjectName("screen_cam_2")
        self.label_12 = QtWidgets.QLabel(self.page_cam)
        self.label_12.setGeometry(QtCore.QRect(1060, 100, 700, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: #CCFFFF;\n"
"border-top-right-radius: 10px;\n"
"border-top-left-radius:10px;\n"
"border: 2px solid black;")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.page_cam)
        self.label_13.setGeometry(QtCore.QRect(20, 100, 700, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: #CCFFFF;\n"
"border-top-right-radius: 10px;\n"
"border-top-left-radius:10px;\n"
"border: 2px solid black;")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.Button_Quaylai_3 = QtWidgets.QPushButton(self.page_cam)
        self.Button_Quaylai_3.setGeometry(QtCore.QRect(10, 5, 150, 60))
        self.Button_Quaylai_3.setMinimumSize(QtCore.QSize(20, 20))
        self.Button_Quaylai_3.setMaximumSize(QtCore.QSize(190, 60))
        self.Button_Quaylai_3.setAutoFillBackground(False)
        self.Button_Quaylai_3.setStyleSheet("QPushButton#Button_Quaylai_3{\n"
"       border-bottom-right-radius :20px;\n"
"    font: 75 17pt \"MS Shell Dlg 2\";\n"
"    \n"
"    /*border: 3px solid rgb(230, 230, 230);*/\n"
"    color: rgb(0, 0, 0);\n"
"    \n"
"    background-color: rgb(220, 220, 220);\n"
"    background-color: #CCFFFF;\n"
"\n"
"}\n"
"QPushButton#Button_Quaylai_3:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color: #0e71aa;\n"
"}\n"
"")
        self.Button_Quaylai_3.setText("")
        self.Button_Quaylai_3.setIcon(icon)
        self.Button_Quaylai_3.setIconSize(QtCore.QSize(50, 50))
        self.Button_Quaylai_3.setObjectName("Button_Quaylai_3")
        self.stackedWidget.addWidget(self.page_cam)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setGeometry(QtCore.QRect(25, 5, 1910, 51))
        self.widget_4.setStyleSheet("background-color:  #0e71aa;\n"
"border-top-left-radius:20px;\n"
"border-top-right-radius:20px;\n"
"border-top-left-radius:20px;")
        self.widget_4.setObjectName("widget_4")
        self.label = QtWidgets.QLabel(self.widget_4)
        self.label.setGeometry(QtCore.QRect(820, 10, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.Button_close_event = QtWidgets.QPushButton(self.widget_4)
        self.Button_close_event.setGeometry(QtCore.QRect(1830, 10, 50, 30))
        self.Button_close_event.setMinimumSize(QtCore.QSize(50, 30))
        self.Button_close_event.setMaximumSize(QtCore.QSize(50, 30))
        self.Button_close_event.setStyleSheet("QPushButton#Button_close_event{\n"
"border-radius: 10px;\n"
"background-color: rgb(230, 230, 230);\n"
"\n"
"}\n"
"\n"
"QPushButton#Button_close_event:hover{\n"
"border: 2px;\n"
"background-color: rgb(255,0,0);\n"
"\n"
"\n"
"\n"
"}\n"
"QPushButton#Button_close_event:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color: rgb(255,0,0);\n"
"}")
        self.Button_close_event.setText("")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("icon/close_screen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_close_event.setIcon(icon19)
        self.Button_close_event.setIconSize(QtCore.QSize(30, 30))
        self.Button_close_event.setObjectName("Button_close_event")
        self.Button_thuphong = QtWidgets.QPushButton(self.widget_4)
        self.Button_thuphong.setGeometry(QtCore.QRect(1770, 10, 50, 30))
        self.Button_thuphong.setMinimumSize(QtCore.QSize(50, 30))
        self.Button_thuphong.setMaximumSize(QtCore.QSize(50, 30))
        self.Button_thuphong.setStyleSheet("QPushButton#Button_thuphong{\n"
"   border-radius:10px;\n"
"background-color: rgb(230, 230, 230);\n"
"\n"
"}\n"
"\n"
"QPushButton#Button_thuphong:hover{\n"
"\n"
"    background-color: rgb(58,192,240);\n"
"}\n"
"QPushButton#Button_thuphong:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color: rgb(220, 220, 220);\n"
"}\n"
"")
        self.Button_thuphong.setText("")
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("icon/minimize_flaticon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_thuphong.setIcon(icon20)
        self.Button_thuphong.setIconSize(QtCore.QSize(30, 30))
        self.Button_thuphong.setObjectName("Button_thuphong")
        self.Button_hide = QtWidgets.QPushButton(self.widget_4)
        self.Button_hide.setGeometry(QtCore.QRect(1710, 10, 50, 30))
        self.Button_hide.setMinimumSize(QtCore.QSize(50, 30))
        self.Button_hide.setMaximumSize(QtCore.QSize(50, 30))
        self.Button_hide.setStyleSheet("QPushButton#Button_hide{\n"
"   border-radius:10px;\n"
"background-color: rgb(230, 230, 230);\n"
"\n"
"}\n"
"\n"
"QPushButton#Button_hide:hover{\n"
"\n"
"    background-color: rgb(58,192,240);\n"
"}\n"
"QPushButton#Button_hide:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color: rgb(220, 220, 220);\n"
"}\n"
"")
        self.Button_hide.setText("")
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("icon/mimiiii_flaticon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_hide.setIcon(icon21)
        self.Button_hide.setIconSize(QtCore.QSize(40, 40))
        self.Button_hide.setObjectName("Button_hide")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(25, 55, 91, 1000))
        self.frame.setStyleSheet("background-color:  #0e71aa;\n"
"\n"
"border-bottom-left-radius:20px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Menu = QtWidgets.QToolButton(self.frame)
        self.Menu.setGeometry(QtCore.QRect(20, 10, 50, 45))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Menu.setFont(font)
        self.Menu.setStyleSheet("url:/icon/icons8-news-feed-48.png")
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("icon/icons8-news-feed-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Menu.setIcon(icon22)
        self.Menu.setIconSize(QtCore.QSize(50, 50))
        self.Menu.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.Menu.setObjectName("Menu")
        self.Setting = QtWidgets.QToolButton(self.frame)
        self.Setting.setGeometry(QtCore.QRect(20, 140, 50, 45))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Setting.setFont(font)
        self.Setting.setStyleSheet("url: /icon/icons8-settings-50 (1).png")
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap("icon/icons8-settings-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Setting.setIcon(icon23)
        self.Setting.setIconSize(QtCore.QSize(50, 50))
        self.Setting.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.Setting.setObjectName("Setting")
        self.Manual = QtWidgets.QToolButton(self.frame)
        self.Manual.setGeometry(QtCore.QRect(20, 210, 50, 45))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Manual.setFont(font)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap("icon/icons8-robotic-arm-52.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Manual.setIcon(icon24)
        self.Manual.setIconSize(QtCore.QSize(50, 50))
        self.Manual.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.Manual.setObjectName("Manual")
        self.Camera = QtWidgets.QToolButton(self.frame)
        self.Camera.setGeometry(QtCore.QRect(20, 280, 50, 45))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Camera.setFont(font)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap("icon/camera.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Camera.setIcon(icon25)
        self.Camera.setIconSize(QtCore.QSize(50, 50))
        self.Camera.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.Camera.setObjectName("Camera")
        self.Home = QtWidgets.QToolButton(self.frame)
        self.Home.setGeometry(QtCore.QRect(20, 70, 50, 45))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Home.setFont(font)
        self.Home.setStyleSheet("url: /icon/icons8-settings-50 (1).png")
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap("icon/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Home.setIcon(icon26)
        self.Home.setIconSize(QtCore.QSize(50, 50))
        self.Home.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.Home.setObjectName("Home")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FANUC ROBOT"))
        self.label_16.setText(_translate("MainWindow", "THIẾT KẾ MÔ HÌNH ROBOT TỰ HÀNH KẾT HỢP CÁNH TAY\n"
" ROBOT TRONG VẬN CHUYỂN"))
        self.label_17.setText(_translate("MainWindow", "BÁO CÁO ĐỒ ÁN TỐT NGHIỆP"))
        self.label_19.setText(_translate("MainWindow", "TRƯỜNG ĐẠI HỌC SƯ PHẠM KỸ THUẬT THÀNH PHỐ HỒ CHÍ MINH"))
        self.label_20.setText(_translate("MainWindow", "BỘ MÔN TỰ ĐỘNG ĐIỀU KHIỂN \n"
"       KHOA ĐIỆN - ĐIỆN TỬ"))
        self.start.setText(_translate("MainWindow", "START"))
        self.label_37.setText(_translate("MainWindow", "Giảng viên hướng dẫn: TS Đặng Xuân Ba"))
        self.label_38.setText(_translate("MainWindow", "Sinh viên thực hiện:      Nguyễn Thanh Bình       20151340"))
        self.label_39.setText(_translate("MainWindow", "Nguyễn Quang Trường  20151424"))
        self.label_40.setText(_translate("MainWindow", "Nguyễn Xuân Vinh        20151431"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Vx, Vw"))
        self.label_6.setText(_translate("MainWindow", "  min_vel_x"))
        self.label_18.setText(_translate("MainWindow", "   max vel_x"))
        self.label_27.setText(_translate("MainWindow", "min_vel_theta"))
        self.label_28.setText(_translate("MainWindow", "max_vel_theta"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Err Vx, Vw"))
        self.label_30.setText(_translate("MainWindow", "  acc_lim_x"))
        self.label_31.setText(_translate("MainWindow", "acc_lim_theta"))
        self.groupBox_6.setTitle(_translate("MainWindow", "threshold"))
        self.label_32.setText(_translate("MainWindow", "lower_threshold"))
        self.groupBox_7.setTitle(_translate("MainWindow", "USB"))
        self.label_33.setText(_translate("MainWindow", "   port_usb"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), _translate("MainWindow", "      XE      "))
        self.groupBox_16.setTitle(_translate("MainWindow", "USB"))
        self.label_50.setText(_translate("MainWindow", "   port_usb"))
        self.groupBox_17.setTitle(_translate("MainWindow", "Camera"))
        self.label_51.setText(_translate("MainWindow", "   camera_1"))
        self.label_52.setText(_translate("MainWindow", "   camera_2"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), _translate("MainWindow", "    ROBOT  "))
        self.Button_done_4.setText(_translate("MainWindow", "Lưu thay đổi"))
        self.Button_9_2.setText(_translate("MainWindow", "Điểm đến 9"))
        self.Button_10_2.setText(_translate("MainWindow", "Điểm đến 10"))
        self.Button_7_2.setText(_translate("MainWindow", "Điểm đến 7"))
        self.Button_2_2.setText(_translate("MainWindow", "Điểm đến 2"))
        self.Button_5_2.setText(_translate("MainWindow", "Điểm đến 5"))
        self.Button_6_2.setText(_translate("MainWindow", "Điểm đến 6"))
        self.Button_8_2.setText(_translate("MainWindow", "Điểm đến 8"))
        self.Button_4_2.setText(_translate("MainWindow", "Điểm đến 4"))
        self.Button_3_2.setText(_translate("MainWindow", "Điểm đến 3"))
        self.Button_1_2.setText(_translate("MainWindow", "Điểm đến 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", " DANH SÁCH"))
        self.Button_khuvuccho_2.setText(_translate("MainWindow", "HOME"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "  KHÁC   "))
        self.thutu.setText(_translate("MainWindow", "   Thứ tự"))
        self.Button_done_2.setText(_translate("MainWindow", "Bắt đầu"))
        self.Button_LoadMap.setText(_translate("MainWindow", "Load Map"))
        self.label_11.setText(_translate("MainWindow", "ROBOT ĐANG DI CHUYỂN ĐẾN:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Position"))
        self.label_7.setText(_translate("MainWindow", "Px"))
        self.label_8.setText(_translate("MainWindow", "Pz "))
        self.label_9.setText(_translate("MainWindow", "Py"))
        self.label_24.setText(_translate("MainWindow", "Cm"))
        self.groupBox.setTitle(_translate("MainWindow", "Prameter Of Joints"))
        self.label_2.setText(_translate("MainWindow", "Theta3"))
        self.label_3.setText(_translate("MainWindow", "Theta2"))
        self.label_4.setText(_translate("MainWindow", "Theta1"))
        self.label_23.setText(_translate("MainWindow", "Degrees"))
        self.Return_box.setText(_translate("MainWindow", " Return"))
        self.forward.setText(_translate("MainWindow", " Forward"))
        self.Run.setText(_translate("MainWindow", "  Run"))
        self.Inverse.setText(_translate("MainWindow", " Inverse"))
        self.Delete.setText(_translate("MainWindow", " Delete"))
        self.home.setText(_translate("MainWindow", " Home"))
        self.label_5.setText(_translate("MainWindow", "MODE"))
        self.Button_capnhat.setText(_translate("MainWindow", " Cập nhật"))
        self.Button_luuMap.setText(_translate("MainWindow", " Lưu Map"))
        self.Button_xoa.setText(_translate("MainWindow", "       Bớt"))
        self.Button_add.setText(_translate("MainWindow", "    Thêm "))
        self.label_14.setText(_translate("MainWindow", "Vui lòng quét mã QR để sử dụng \n"
" chế độ điều khiển Manual"))
        self.label_34.setText(_translate("MainWindow", "Danh sách đã lưu:"))
        self.label_chonchedo.setText(_translate("MainWindow", "CHỌN CHẾ ĐỘ"))
        self.Button_Manu_2.setText(_translate("MainWindow", " THỦ CÔNG"))
        self.Button_Auto_2.setText(_translate("MainWindow", "TỰ ĐỘNG"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Position"))
        self.label_26.setText(_translate("MainWindow", "Px"))
        self.label_22.setText(_translate("MainWindow", "Py"))
        self.label_25.setText(_translate("MainWindow", "Pz "))
        self.label_12.setText(_translate("MainWindow", "Camera 2"))
        self.label_13.setText(_translate("MainWindow", "Camera 1"))
        self.label.setText(_translate("MainWindow", "ROBOT CONTROLLING INTERFACE"))
        self.Menu.setText(_translate("MainWindow", "  Menu"))
        self.Setting.setText(_translate("MainWindow", "  Setting Connect"))
        self.Manual.setText(_translate("MainWindow", "  Manual Mode"))
        self.Camera.setText(_translate("MainWindow", "  Camera"))
        self.Home.setText(_translate("MainWindow", "  Home"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
