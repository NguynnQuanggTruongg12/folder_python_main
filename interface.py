# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Display1.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2011, 1061)
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
        self.label_16.setGeometry(QtCore.QRect(10, 360, 1811, 121))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color:#0e659a;")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.login)
        self.label_17.setGeometry(QtCore.QRect(10, 250, 1811, 80))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color:#0e659a;")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_19 = QtWidgets.QLabel(self.login)
        self.label_19.setGeometry(QtCore.QRect(650, 50, 581, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:#0e659a;\n"
"\n"
"padding-bottom:7px;")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.login)
        self.label_20.setGeometry(QtCore.QRect(750, 130, 521, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color:#0e659a;")
        self.label_20.setObjectName("label_20")
        self.start = QtWidgets.QPushButton(self.login)
        self.start.setGeometry(QtCore.QRect(1480, 730, 191, 71))
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
"border-radius:5px;\n"
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
        self.label_21.setGeometry(QtCore.QRect(120, 50, 131, 171))
        self.label_21.setStyleSheet("image: url(:/icon/download.png);")
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap(":/icon/icon/download.png"))
        self.label_21.setScaledContents(True)
        self.label_21.setObjectName("label_21")
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../backup_robot_tieptan/letan_10062024/list_table.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon1, "")
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../backup_robot_tieptan/letan_10062024/table_else.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon2, "")
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
        self.listWidget_ds.setGeometry(QtCore.QRect(39, 100, 231, 331))
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/document.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.thutu.setIcon(icon3)
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.frame_6.raise_()
        self.frame_4.raise_()
        self.Button_Quaylai.raise_()
        self.frame_chua.raise_()
        self.Button_done_2.raise_()
        self.stackedWidget.addWidget(self.page_2)
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
        self.screen_cam_3.setGeometry(QtCore.QRect(20, 25, 1501, 950))
        self.screen_cam_3.setStyleSheet("border: 2px solid black;\n"
"border-radius:10px;")
        self.screen_cam_3.setText("")
        self.screen_cam_3.setObjectName("screen_cam_3")
        self.Button_done = QtWidgets.QPushButton(self.Display_setting)
        self.Button_done.setGeometry(QtCore.QRect(1560, 360, 220, 100))
        self.Button_done.setMinimumSize(QtCore.QSize(220, 100))
        self.Button_done.setMaximumSize(QtCore.QSize(220, 100))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Button_done.setFont(font)
        self.Button_done.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Button_done.setStyleSheet("QPushButton#Button_done{\n"
"    border-radius: 25px;\n"
"    font: 75 16pt \"MS Shell Dlg 2\";\n"
"    border: 1px solid #CCFFFF;\n"
"    background-color: #CCFFFF;\n"
"}\n"
"\n"
"QPushButton#Button_done:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color: rgb(58, 192, 240);\n"
"}\n"
"QPushButton#Button_done:checked {\n"
"background-color: rgb(58, 192, 255);\n"
"\n"
"}\n"
"")
        self.Button_done.setIcon(icon4)
        self.Button_done.setIconSize(QtCore.QSize(40, 50))
        self.Button_done.setObjectName("Button_done")
        self.Button_huy = QtWidgets.QPushButton(self.Display_setting)
        self.Button_huy.setGeometry(QtCore.QRect(1560, 500, 220, 100))
        self.Button_huy.setMinimumSize(QtCore.QSize(220, 100))
        self.Button_huy.setMaximumSize(QtCore.QSize(220, 100))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Button_huy.setFont(font)
        self.Button_huy.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Button_huy.setStyleSheet("QPushButton#Button_huy{\n"
"    border-radius: 25px;\n"
"    font: 75 16pt \"MS Shell Dlg 2\";\n"
"    border: 1px solid #CCFFFF;\n"
"    background-color: #CCFFFF;\n"
"\n"
"}\n"
"\n"
"QPushButton#Button_huy:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color: rgb(58, 192, 240);\n"
"}\n"
"QPushButton#Button_huy:checked {\n"
"background-color: rgb(58, 192, 255);\n"
"\n"
"}\n"
"")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icon/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_huy.setIcon(icon5)
        self.Button_huy.setIconSize(QtCore.QSize(40, 50))
        self.Button_huy.setObjectName("Button_huy")
        self.stackedWidget.addWidget(self.page_setting)
        self.page_Manual = QtWidgets.QWidget()
        self.page_Manual.setObjectName("page_Manual")
        self.Display_Manual = QtWidgets.QWidget(self.page_Manual)
        self.Display_Manual.setGeometry(QtCore.QRect(0, 0, 1781, 981))
        self.Display_Manual.setStyleSheet("background-color:rgba(255,255,255,255);")
        self.Display_Manual.setObjectName("Display_Manual")
        self.groupBox = QtWidgets.QGroupBox(self.Display_Manual)
        self.groupBox.setGeometry(QtCore.QRect(30, 100, 600, 370))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("gridline-color: rgb(0, 0, 0);\n"
"selection-color: rgb(85, 170, 255);\n"
"border: 1px solid black;\n"
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
        self.label_23.setGeometry(QtCore.QRect(390, 10, 47, 13))
        self.label_23.setObjectName("label_23")
        self.groupBox_2 = QtWidgets.QGroupBox(self.Display_Manual)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 550, 600, 370))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("gridline-color: rgb(0, 0, 0);\n"
"selection-color: rgb(85, 170, 255);\n"
"border: 1px solid black;\n"
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
        self.label_24.setGeometry(QtCore.QRect(410, 10, 47, 13))
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.widget_3 = QtWidgets.QWidget(self.Display_Manual)
        self.widget_3.setGeometry(QtCore.QRect(910, 720, 691, 191))
        self.widget_3.setStyleSheet("border: 1px solid ;\n"
"")
        self.widget_3.setObjectName("widget_3")
        self.Return_box = QtWidgets.QPushButton(self.widget_3)
        self.Return_box.setGeometry(QtCore.QRect(20, 70, 161, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Return_box.setFont(font)
        self.Return_box.setStyleSheet("\n"
"\n"
"QPushButton#Return_box{\n"
"\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(10, 90, 190, 229), stop: 1 rgba(85, 98, 112,\n"
"\n"
"226));\n"
"\n"
"color:rgba(255, 255, 255, 210);\n"
"\n"
"border-radius:5px;\n"
"\n"
"}\n"
"\n"
"QPushButton#Return_box:hover{\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84,\n"
"\n"
"226));\n"
"}\n"
"\n"
"QPushButton#Return_box:pressed{\n"
"\n"
"padding-left:5px;\n"
"\n"
"padding-top:5px;\n"
" background-color:rgba(150, 123, 111, 255);\n"
"}`\n"
"")
        self.Return_box.setObjectName("Return_box")
        self.forward = QtWidgets.QPushButton(self.widget_3)
        self.forward.setGeometry(QtCore.QRect(20, 140, 161, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.forward.setFont(font)
        self.forward.setStyleSheet("\n"
"\n"
"QPushButton#forward{\n"
"\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(10, 90, 190, 229), stop: 1 rgba(85, 98, 112,\n"
"\n"
"226));\n"
"\n"
"color:rgba(255, 255, 255, 210);\n"
"\n"
"border-radius:5px;\n"
"\n"
"}\n"
"\n"
"QPushButton#forward:hover{\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84,\n"
"\n"
"226));\n"
"}\n"
"\n"
"QPushButton#forward:pressed{\n"
"\n"
"padding-left:5px;\n"
"\n"
"padding-top:5px;\n"
" background-color:rgba(150, 123, 111, 255);\n"
"}`\n"
"")
        self.forward.setObjectName("forward")
        self.Run = QtWidgets.QPushButton(self.widget_3)
        self.Run.setGeometry(QtCore.QRect(200, 70, 160, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Run.setFont(font)
        self.Run.setStyleSheet("\n"
"\n"
"QPushButton#Run{\n"
"\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(10, 90, 190, 229), stop: 1 rgba(85, 98, 112,\n"
"\n"
"226));\n"
"\n"
"color:rgba(255, 255, 255, 210);\n"
"\n"
"border-radius:5px;\n"
"\n"
"}\n"
"\n"
"QPushButton#Run:hover{\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84,\n"
"\n"
"226));\n"
"}\n"
"\n"
"QPushButton#Run:pressed{\n"
"\n"
"padding-left:5px;\n"
"\n"
"padding-top:5px;\n"
" background-color:rgba(150, 123, 111, 255);\n"
"}`\n"
"")
        self.Run.setObjectName("Run")
        self.Inverse = QtWidgets.QPushButton(self.widget_3)
        self.Inverse.setGeometry(QtCore.QRect(200, 140, 160, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Inverse.setFont(font)
        self.Inverse.setStyleSheet("\n"
"\n"
"QPushButton#Inverse{\n"
"\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(10, 90, 190, 229), stop: 1 rgba(85, 98, 112,\n"
"\n"
"226));\n"
"\n"
"color:rgba(255, 255, 255, 210);\n"
"\n"
"border-radius:5px;\n"
"\n"
"}\n"
"\n"
"QPushButton#Inverse:hover{\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84,\n"
"\n"
"226));\n"
"}\n"
"\n"
"QPushButton#Inverse:pressed{\n"
"\n"
"padding-left:5px;\n"
"\n"
"padding-top:5px;\n"
" background-color:rgba(150, 123, 111, 255);\n"
"}`\n"
"")
        self.Inverse.setObjectName("Inverse")
        self.Calc = QtWidgets.QPushButton(self.widget_3)
        self.Calc.setGeometry(QtCore.QRect(380, 70, 160, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Calc.setFont(font)
        self.Calc.setStyleSheet("\n"
"\n"
"QPushButton#Calc{\n"
"\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(10, 90, 190, 229), stop: 1 rgba(85, 98, 112,\n"
"\n"
"226));\n"
"\n"
"color:rgba(255, 255, 255, 210);\n"
"\n"
"border-radius:5px;\n"
"\n"
"}\n"
"\n"
"QPushButton#attract:hover{\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84,\n"
"\n"
"226));\n"
"}\n"
"\n"
"QPushButton#Calc:pressed{\n"
"\n"
"padding-left:5px;\n"
"\n"
"padding-top:5px;\n"
" background-color:rgba(150, 123, 111, 255);\n"
"}`\n"
"")
        self.Calc.setObjectName("Calc")
        self.clear_row = QtWidgets.QPushButton(self.widget_3)
        self.clear_row.setGeometry(QtCore.QRect(380, 140, 160, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.clear_row.setFont(font)
        self.clear_row.setStyleSheet("\n"
"\n"
"QPushButton#clear_row{\n"
"\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(10, 90, 190, 229), stop: 1 rgba(85, 98, 112,\n"
"\n"
"226));\n"
"\n"
"color:rgba(255, 255, 255, 210);\n"
"\n"
"border-radius:5px;\n"
"\n"
"}\n"
"\n"
"QPushButton#clear_row:hover{\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84,\n"
"\n"
"226));\n"
"}\n"
"\n"
"QPushButton#clear_row:pressed{\n"
"\n"
"padding-left:5px;\n"
"\n"
"padding-top:5px;\n"
" background-color:rgba(150, 123, 111, 255);\n"
"}`\n"
"")
        self.clear_row.setObjectName("clear_row")
        self.label_5 = QtWidgets.QLabel(self.widget_3)
        self.label_5.setGeometry(QtCore.QRect(30, 30, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.Mic = QtWidgets.QPushButton(self.widget_3)
        self.Mic.setGeometry(QtCore.QRect(580, 90, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Mic.setFont(font)
        self.Mic.setStyleSheet("\n"
"\n"
"\n"
"QPushButton#Mic{\n"
"\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(10, 90, 190, 229), stop: 1 rgba(85, 98, 112,\n"
"\n"
"226));\n"
"\n"
"color:rgba(255, 255, 255, 210);\n"
"image: url(:/icon/mic (1).svg);\n"
"border-radius:35px;\n"
"\n"
"}\n"
"\n"
"QPushButton#Mic:hover{\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84,\n"
"\n"
"226));\n"
"}\n"
"\n"
"QPushButton#Mic:pressed{\n"
"\n"
"padding-left:5px;\n"
"\n"
"padding-top:5px;\n"
" background-color:rgba(150, 123, 111, 255);\n"
"}`\n"
"")
        self.Mic.setText("")
        self.Mic.setIconSize(QtCore.QSize(40, 40))
        self.Mic.setObjectName("Mic")
        self.frame_2 = QtWidgets.QFrame(self.Display_Manual)
        self.frame_2.setGeometry(QtCore.QRect(980, 160, 691, 381))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 641, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.Screen_diagram = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.Screen_diagram.setContentsMargins(0, 0, 0, 0)
        self.Screen_diagram.setSpacing(0)
        self.Screen_diagram.setObjectName("Screen_diagram")
        self.table_the = QtWidgets.QTableWidget(self.frame_2)
        self.table_the.setGeometry(QtCore.QRect(190, 50, 321, 201))
        self.table_the.setObjectName("table_the")
        self.table_the.setColumnCount(3)
        self.table_the.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.table_the.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_the.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_the.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_the.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_the.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_the.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_the.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_the.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_the.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_the.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_the.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_the.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_the.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_the.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_the.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_the.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_the.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_the.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_the.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_the.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_the.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_the.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_the.setItem(4, 2, item)
        self.manual_auto = QtWidgets.QWidget(self.Display_Manual)
        self.manual_auto.setGeometry(QtCore.QRect(1060, 50, 321, 61))
        self.manual_auto.setObjectName("manual_auto")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.manual_auto)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mode_manual = QtWidgets.QPushButton(self.manual_auto)
        self.mode_manual.setMaximumSize(QtCore.QSize(300, 30))
        self.mode_manual.setStyleSheet("\n"
"\n"
"QPushButton#mode_manual{\n"
"\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(10, 90, 190, 229), stop: 1 rgba(85, 98, 112,\n"
"\n"
"226));\n"
"\n"
"color:rgba(255, 255, 255, 210);\n"
"\n"
"border-radius:5px;\n"
"\n"
"}\n"
"\n"
"QPushButton#mode_manual:hover{\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84,\n"
"\n"
"226));\n"
"}\n"
"\n"
"QPushButton#mode_manual:pressed{\n"
"\n"
"padding-left:5px;\n"
"\n"
"padding-top:5px;\n"
" background-color:rgba(150, 123, 111, 255);\n"
"}`\n"
"")
        self.mode_manual.setObjectName("mode_manual")
        self.horizontalLayout.addWidget(self.mode_manual)
        self.mode_auto = QtWidgets.QPushButton(self.manual_auto)
        self.mode_auto.setMaximumSize(QtCore.QSize(300, 30))
        self.mode_auto.setStyleSheet("\n"
"QPushButton#mode_auto{\n"
"\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(10, 90, 190, 229), stop: 1 rgba(85, 98, 112,\n"
"\n"
"226));\n"
"\n"
"color:rgba(255, 255, 255, 210);\n"
"\n"
"border-radius:5px;\n"
"\n"
"}\n"
"\n"
"QPushButton#mode_auto:hover{\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84,\n"
"\n"
"226));\n"
"}\n"
"\n"
"QPushButton#mode_auto:pressed{\n"
"\n"
"padding-left:5px;\n"
"\n"
"padding-top:5px;\n"
" background-color:rgba(150, 123, 111, 255);\n"
"}`\n"
"")
        self.mode_auto.setObjectName("mode_auto")
        self.horizontalLayout.addWidget(self.mode_auto)
        self.frame_led = QtWidgets.QFrame(self.Display_Manual)
        self.frame_led.setGeometry(QtCore.QRect(1530, 70, 131, 37))
        self.frame_led.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_led.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_led.setObjectName("frame_led")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_led)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.led_manual = QtWidgets.QLabel(self.frame_led)
        self.led_manual.setStyleSheet("border-radius: 5px;\n"
"border: 1px solid black;\n"
"background-color: gray")
        self.led_manual.setText("")
        self.led_manual.setObjectName("led_manual")
        self.horizontalLayout_5.addWidget(self.led_manual)
        self.led_auto = QtWidgets.QLabel(self.frame_led)
        self.led_auto.setStyleSheet("border-radius: 5px;\n"
"border: 1px solid black;\n"
"background-color: gray")
        self.led_auto.setText("")
        self.led_auto.setObjectName("led_auto")
        self.horizontalLayout_5.addWidget(self.led_auto)
        self.led_on_off = QtWidgets.QLabel(self.frame_led)
        self.led_on_off.setStyleSheet("border-radius: 5px;\n"
"border: 1px solid black;\n"
"background-color: gray")
        self.led_on_off.setText("")
        self.led_on_off.setObjectName("led_on_off")
        self.horizontalLayout_5.addWidget(self.led_on_off)
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
        self.stackedWidget.addWidget(self.page_Manual)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.frame_3 = QtWidgets.QFrame(self.page)
        self.frame_3.setGeometry(QtCore.QRect(10, 80, 671, 804))
        self.frame_3.setStyleSheet("border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.Button_RIGHT = QtWidgets.QPushButton(self.frame_3)
        self.Button_RIGHT.setGeometry(QtCore.QRect(460, 240, 150, 150))
        self.Button_RIGHT.setMinimumSize(QtCore.QSize(150, 150))
        self.Button_RIGHT.setMaximumSize(QtCore.QSize(150, 150))
        self.Button_RIGHT.setStyleSheet("QPushButton#Button_RIGHT{\n"
"    border-radius: 5px;\n"
"    font: 75 9pt \"MS Shell Dlg 2\";\n"
"    border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton#Button_RIGHT:pressed{\n"
"padding-left :5px;\n"
"padding-top :5px;\n"
"\n"
"\n"
"}\n"
"\n"
"")
        self.Button_RIGHT.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../../../backup_robot_tieptan/letan_10062024/phai_20_09.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_RIGHT.setIcon(icon6)
        self.Button_RIGHT.setIconSize(QtCore.QSize(140, 140))
        self.Button_RIGHT.setObjectName("Button_RIGHT")
        self.Button_UP = QtWidgets.QPushButton(self.frame_3)
        self.Button_UP.setGeometry(QtCore.QRect(259, 63, 150, 150))
        self.Button_UP.setMinimumSize(QtCore.QSize(150, 150))
        self.Button_UP.setMaximumSize(QtCore.QSize(150, 150))
        self.Button_UP.setStyleSheet("QPushButton#Button_UP{\n"
"    border-radius: 5px;\n"
"    font: 75 9pt \"MS Shell Dlg 2\";\n"
"    border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"    border:none;\n"
"    \n"
"}\n"
"\n"
"QPushButton#Button_UP:pressed{\n"
"padding-left :5px;\n"
"padding-top :5px;\n"
"\n"
"\n"
"}\n"
"QPushButton#Button_UP:checked {\n"
"background-color: rgb(58, 192, 255);\n"
"\n"
"}\n"
"")
        self.Button_UP.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../../../backup_robot_tieptan/letan_10062024/muitenlen_20_09.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_UP.setIcon(icon7)
        self.Button_UP.setIconSize(QtCore.QSize(140, 140))
        self.Button_UP.setObjectName("Button_UP")
        self.Button_DOWN = QtWidgets.QPushButton(self.frame_3)
        self.Button_DOWN.setGeometry(QtCore.QRect(259, 475, 150, 150))
        self.Button_DOWN.setMinimumSize(QtCore.QSize(150, 150))
        self.Button_DOWN.setMaximumSize(QtCore.QSize(150, 150))
        self.Button_DOWN.setStyleSheet("QPushButton#Button_DOWN{\n"
"    border-radius: 5px;\n"
"    font: 75 9pt \"MS Shell Dlg 2\";\n"
"    border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton#Button_DOWN:pressed{\n"
"padding-left :5px;\n"
"padding-top :5px;\n"
"\n"
"\n"
"}\n"
"\n"
"")
        self.Button_DOWN.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../../../backup_robot_tieptan/letan_10062024/pnd_down_21_09.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_DOWN.setIcon(icon8)
        self.Button_DOWN.setIconSize(QtCore.QSize(140, 140))
        self.Button_DOWN.setObjectName("Button_DOWN")
        self.Button_STOP = QtWidgets.QPushButton(self.frame_3)
        self.Button_STOP.setGeometry(QtCore.QRect(259, 269, 150, 150))
        self.Button_STOP.setMinimumSize(QtCore.QSize(150, 150))
        self.Button_STOP.setMaximumSize(QtCore.QSize(150, 150))
        self.Button_STOP.setStyleSheet("QPushButton#Button_STOP{\n"
"    border-radius: 5px;\n"
"    font: 75 9pt \"MS Shell Dlg 2\";\n"
"border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton#Button_STOP:pressed{\n"
"padding-left :5px;\n"
"padding-top :5px;\n"
"\n"
"\n"
"}\n"
"\n"
"")
        self.Button_STOP.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../../../backup_robot_tieptan/letan_10062024/circle_21_09.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_STOP.setIcon(icon9)
        self.Button_STOP.setIconSize(QtCore.QSize(140, 140))
        self.Button_STOP.setObjectName("Button_STOP")
        self.Button_LEFT = QtWidgets.QPushButton(self.frame_3)
        self.Button_LEFT.setGeometry(QtCore.QRect(58, 269, 150, 150))
        self.Button_LEFT.setMinimumSize(QtCore.QSize(150, 150))
        self.Button_LEFT.setMaximumSize(QtCore.QSize(150, 150))
        self.Button_LEFT.setStyleSheet("QPushButton#Button_LEFT{\n"
"    border-radius: 5px;\n"
"    font: 75 9pt \"MS Shell Dlg 2\";\n"
"    border: 3px solid rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton#Button_LEFT:pressed{\n"
"padding-left :5px;\n"
"padding-top :5px;\n"
"\n"
"\n"
"}\n"
"\n"
"")
        self.Button_LEFT.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../../../backup_robot_tieptan/letan_10062024/trai_20_09.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_LEFT.setIcon(icon10)
        self.Button_LEFT.setIconSize(QtCore.QSize(140, 140))
        self.Button_LEFT.setObjectName("Button_LEFT")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(50, 680, 71, 61))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:none;")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../../../backup_robot_tieptan/letan_10062024/xoafotn_velocyty.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
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
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icon/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_capnhat.setIcon(icon11)
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
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icon/location.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_luuMap.setIcon(icon12)
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
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("icon/minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_xoa.setIcon(icon13)
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
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("icon/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_add.setIcon(icon14)
        self.Button_add.setIconSize(QtCore.QSize(50, 50))
        self.Button_add.setObjectName("Button_add")
        self.gridLayout_5.addWidget(self.Button_add, 1, 0, 1, 1)
        self.listWidget_dsban = QtWidgets.QListWidget(self.page)
        self.listWidget_dsban.setGeometry(QtCore.QRect(1109, 173, 641, 571))
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
        self.frame_11.setObjectName("frame_11")
        self.frame_10 = QtWidgets.QFrame(self.frame_11)
        self.frame_10.setGeometry(QtCore.QRect(270, 350, 1211, 358))
        self.frame_10.setMinimumSize(QtCore.QSize(1200, 358))
        self.frame_10.setMaximumSize(QtCore.QSize(12432324, 16777215))
        self.frame_10.setStyleSheet("")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.Button_Auto_2 = QtWidgets.QPushButton(self.frame_10)
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
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("../../backup_robot_tieptan/letan_10062024/xoafont_auto.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_Auto_2.setIcon(icon15)
        self.Button_Auto_2.setIconSize(QtCore.QSize(160, 160))
        self.Button_Auto_2.setObjectName("Button_Auto_2")
        self.gridLayout_7.addWidget(self.Button_Auto_2, 1, 1, 1, 1)
        self.Button_Manu_2 = QtWidgets.QPushButton(self.frame_10)
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
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("../../backup_robot_tieptan/letan_10062024/xoafont_dieukhien.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_Manu_2.setIcon(icon16)
        self.Button_Manu_2.setIconSize(QtCore.QSize(100, 100))
        self.Button_Manu_2.setObjectName("Button_Manu_2")
        self.gridLayout_7.addWidget(self.Button_Manu_2, 1, 0, 1, 1)
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
        self.Button_Quaylai_3.setGeometry(QtCore.QRect(5, 5, 150, 60))
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
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("../../backup_robot_tieptan/letan_10062024/close_screen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_close_event.setIcon(icon17)
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
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("../../backup_robot_tieptan/letan_10062024/maximize_flaticon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_thuphong.setIcon(icon18)
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
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("../../backup_robot_tieptan/letan_10062024/mimiiii_flaticon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_hide.setIcon(icon19)
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
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("icon/icons8-news-feed-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Menu.setIcon(icon20)
        self.Menu.setIconSize(QtCore.QSize(50, 50))
        self.Menu.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.Menu.setObjectName("Menu")
        self.Setting = QtWidgets.QToolButton(self.frame)
        self.Setting.setGeometry(QtCore.QRect(20, 140, 50, 45))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Setting.setFont(font)
        self.Setting.setStyleSheet("url: /icon/icons8-settings-50 (1).png")
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("icon/icons8-settings-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Setting.setIcon(icon21)
        self.Setting.setIconSize(QtCore.QSize(50, 50))
        self.Setting.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.Setting.setObjectName("Setting")
        self.Manual = QtWidgets.QToolButton(self.frame)
        self.Manual.setGeometry(QtCore.QRect(20, 210, 50, 45))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Manual.setFont(font)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("icon/icons8-robotic-arm-52.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Manual.setIcon(icon22)
        self.Manual.setIconSize(QtCore.QSize(50, 50))
        self.Manual.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.Manual.setObjectName("Manual")
        self.Camera = QtWidgets.QToolButton(self.frame)
        self.Camera.setGeometry(QtCore.QRect(20, 280, 50, 45))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Camera.setFont(font)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap("icon/camera.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Camera.setIcon(icon23)
        self.Camera.setIconSize(QtCore.QSize(50, 50))
        self.Camera.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.Camera.setObjectName("Camera")
        self.Home = QtWidgets.QToolButton(self.frame)
        self.Home.setGeometry(QtCore.QRect(20, 70, 50, 45))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Home.setFont(font)
        self.Home.setStyleSheet("url: /icon/icons8-settings-50 (1).png")
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap("icon/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Home.setIcon(icon24)
        self.Home.setIconSize(QtCore.QSize(50, 50))
        self.Home.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.Home.setObjectName("Home")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(6)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FANUC ROBOT"))
        self.label_16.setText(_translate("MainWindow", "THIẾT KẾ MÔ HÌNH ROBOT TỰ HÀNH KẾT HỢP CÁNH TAY\n"
" ROBOT TRONG VẬN CHUYỂN"))
        self.label_17.setText(_translate("MainWindow", "BÁO CÁO ĐỒ ÁN TỐT NGHIỆP"))
        self.label_19.setText(_translate("MainWindow", "TRƯỜNG ĐẠI HỌC SƯ PHẠM KỸ THUẬT TP.HCM "))
        self.label_20.setText(_translate("MainWindow", "BỘ MÔN TỰ ĐỘNG ĐIỀU KHIỂN \n"
"       KHOA ĐIỆN - ĐIỆN TỬ"))
        self.start.setText(_translate("MainWindow", "START"))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", " DANH SÁCH PHÒNG"))
        self.Button_khuvuccho_2.setText(_translate("MainWindow", "HOME"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "  KHÁC   "))
        self.thutu.setText(_translate("MainWindow", "   Thứ tự"))
        self.Button_done_2.setText(_translate("MainWindow", "Bắt đầu"))
        self.Button_done.setText(_translate("MainWindow", "   Đồng ý"))
        self.Button_huy.setText(_translate("MainWindow", "    Hủy"))
        self.groupBox.setTitle(_translate("MainWindow", "Prameter Of Joints"))
        self.label_2.setText(_translate("MainWindow", "Theta3"))
        self.label_3.setText(_translate("MainWindow", "Theta2"))
        self.label_4.setText(_translate("MainWindow", "Theta1"))
        self.label_23.setText(_translate("MainWindow", "Degrees"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Position"))
        self.label_7.setText(_translate("MainWindow", "Px"))
        self.label_8.setText(_translate("MainWindow", "Pz "))
        self.label_9.setText(_translate("MainWindow", "Py"))
        self.label_24.setText(_translate("MainWindow", "Cm"))
        self.Return_box.setText(_translate("MainWindow", "Return Box"))
        self.forward.setText(_translate("MainWindow", "Forward"))
        self.Run.setText(_translate("MainWindow", "Run"))
        self.Inverse.setText(_translate("MainWindow", "Inverse"))
        self.Calc.setText(_translate("MainWindow", "Calc_The"))
        self.clear_row.setText(_translate("MainWindow", "Home"))
        self.label_5.setText(_translate("MainWindow", "MODE"))
        item = self.table_the.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.table_the.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.table_the.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.table_the.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.table_the.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.table_the.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Theta 1"))
        item = self.table_the.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Theta 2"))
        item = self.table_the.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Theta 3"))
        __sortingEnabled = self.table_the.isSortingEnabled()
        self.table_the.setSortingEnabled(False)
        self.table_the.setSortingEnabled(__sortingEnabled)
        self.mode_manual.setText(_translate("MainWindow", "Manual"))
        self.mode_auto.setText(_translate("MainWindow", "Auto"))
        self.Button_capnhat.setText(_translate("MainWindow", " Cập nhật"))
        self.Button_luuMap.setText(_translate("MainWindow", " Lưu Map"))
        self.Button_xoa.setText(_translate("MainWindow", "       Bớt"))
        self.Button_add.setText(_translate("MainWindow", "    Thêm "))
        self.Button_Auto_2.setText(_translate("MainWindow", "TỰ ĐỘNG"))
        self.Button_Manu_2.setText(_translate("MainWindow", " THỦ  CÔNG"))
        self.label_chonchedo.setText(_translate("MainWindow", "CHỌN CHẾ ĐỘ"))
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
