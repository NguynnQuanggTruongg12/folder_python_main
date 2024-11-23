# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_them1.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_nhaptenban(object):
    def setupUi(self, Form_nhaptenban):
        Form_nhaptenban.setObjectName("Form_nhaptenban")
        Form_nhaptenban.resize(1010, 693)
        Form_nhaptenban.setStyleSheet("")
        self.frame = QtWidgets.QFrame(Form_nhaptenban)
        self.frame.setGeometry(QtCore.QRect(0, 0, 521, 291))
        self.frame.setMinimumSize(QtCore.QSize(500, 200))
        self.frame.setMaximumSize(QtCore.QSize(750, 550))
        self.frame.setStyleSheet("background-color: rgb(230, 230, 230);\n"
"border-radius: 5px;\n"
"box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5);")
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit_nhaptenban = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_nhaptenban.setGeometry(QtCore.QRect(10, 60, 500, 100))
        self.lineEdit_nhaptenban.setMinimumSize(QtCore.QSize(500, 100))
        self.lineEdit_nhaptenban.setMaximumSize(QtCore.QSize(500, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_nhaptenban.setFont(font)
        self.lineEdit_nhaptenban.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.lineEdit_nhaptenban.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_nhaptenban.setObjectName("lineEdit_nhaptenban")
        self.Button_xacnhan_capnhat = QtWidgets.QPushButton(self.frame)
        self.Button_xacnhan_capnhat.setGeometry(QtCore.QRect(270, 170, 241, 111))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Button_xacnhan_capnhat.setFont(font)
        self.Button_xacnhan_capnhat.setStyleSheet("QPushButton#Button_xacnhan_capnhat\n"
"{\n"
"    border-radius: 20px;\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border: 1px solid rgb(230, 230, 230);\n"
"    background-color: rgb(250, 250, 250);\n"
"/*border: 3px solid rgb(0, 0, 255);*/\n"
"\n"
"}\n"
"\n"
"QPushButton#Button_xacnhan_capnhat:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color:#0e71aa;\n"
"}\n"
"QPushButton#Button_xacnhan_capnhat:checked {\n"
"background-color:#0e71aa;\n"
"\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_xacnhan_capnhat.setIcon(icon)
        self.Button_xacnhan_capnhat.setIconSize(QtCore.QSize(40, 40))
        self.Button_xacnhan_capnhat.setObjectName("Button_xacnhan_capnhat")
        self.Button_huy_capnhat = QtWidgets.QPushButton(self.frame)
        self.Button_huy_capnhat.setGeometry(QtCore.QRect(10, 170, 241, 111))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Button_huy_capnhat.setFont(font)
        self.Button_huy_capnhat.setStyleSheet("QPushButton#Button_huy_capnhat\n"
"{\n"
"    border-radius: 20px;\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border: 1px solid rgb(230, 230, 230);\n"
"    background-color: rgb(250, 250, 250);\n"
"/*border: 3px solid rgb(0, 0, 255);*/\n"
"\n"
"}\n"
"\n"
"QPushButton#Button_huy_capnhat:pressed{\n"
"padding-left :2px;\n"
"padding-top :2px;\n"
"\n"
"    background-color:#0e71aa;\n"
"}\n"
"QPushButton#Button_huy_capnhat:checked {\n"
"background-color: #0e71aa;\n"
"\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_huy_capnhat.setIcon(icon1)
        self.Button_huy_capnhat.setIconSize(QtCore.QSize(40, 40))
        self.Button_huy_capnhat.setObjectName("Button_huy_capnhat")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 500, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
" border-radius: 10px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Form_nhaptenban)
        QtCore.QMetaObject.connectSlotsByName(Form_nhaptenban)

    def retranslateUi(self, Form_nhaptenban):
        _translate = QtCore.QCoreApplication.translate
        Form_nhaptenban.setWindowTitle(_translate("Form_nhaptenban", "Form"))
        self.lineEdit_nhaptenban.setPlaceholderText(_translate("Form_nhaptenban", "   Nhập tên vị trí(1, 2, 3,...)"))
        self.Button_xacnhan_capnhat.setText(_translate("Form_nhaptenban", "  ĐỒNG Ý"))
        self.Button_huy_capnhat.setText(_translate("Form_nhaptenban", "   HỦY"))
        self.label.setText(_translate("Form_nhaptenban", "Vui lòng nhập tên vị trí"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_nhaptenban = QtWidgets.QWidget()
    ui = Ui_Form_nhaptenban()
    ui.setupUi(Form_nhaptenban)
    Form_nhaptenban.show()
    sys.exit(app.exec_())
