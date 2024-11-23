# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_emergency.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_emergency(object):
    def setupUi(self, Form_emergency):
        Form_emergency.setObjectName("Form_emergency")
        Form_emergency.resize(1010, 719)
        Form_emergency.setStyleSheet("")
        self.frame = QtWidgets.QFrame(Form_emergency)
        self.frame.setGeometry(QtCore.QRect(0, 0, 521, 291))
        self.frame.setMinimumSize(QtCore.QSize(500, 200))
        self.frame.setMaximumSize(QtCore.QSize(750, 550))
        self.frame.setStyleSheet("background-color: rgb(230, 230, 230);\n"
"border-radius: 5px;\n"
"box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5);")
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 130, 500, 151))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
" border-radius: 10px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.Button_xacnhan_capnhat = QtWidgets.QPushButton(self.frame)
        self.Button_xacnhan_capnhat.setGeometry(QtCore.QRect(10, 10, 501, 111))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Button_xacnhan_capnhat.setFont(font)
        self.Button_xacnhan_capnhat.setStyleSheet("QPushButton#Button_xacnhan_capnhat\n"
"{\n"
"    border-radius: 10px;\n"
"    font: 75 24pt \"MS Shell Dlg 2\";\n"
"    border: 1px solid rgb(230, 230, 230);\n"
"    background-color: rgb(250, 250, 250);\n"
"/*border: 3px solid rgb(0, 0, 255);*/\n"
"\n"
"}\n"
"\n"
"\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/warning.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_xacnhan_capnhat.setIcon(icon)
        self.Button_xacnhan_capnhat.setIconSize(QtCore.QSize(100, 100))
        self.Button_xacnhan_capnhat.setObjectName("Button_xacnhan_capnhat")

        self.retranslateUi(Form_emergency)
        QtCore.QMetaObject.connectSlotsByName(Form_emergency)

    def retranslateUi(self, Form_emergency):
        _translate = QtCore.QCoreApplication.translate
        Form_emergency.setWindowTitle(_translate("Form_emergency", "Form"))
        self.label.setText(_translate("Form_emergency", "ROBOT ĐANG DI CHUYỂN"))
        self.Button_xacnhan_capnhat.setText(_translate("Form_emergency", " CẢNH BÁO "))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_emergency = QtWidgets.QWidget()
    ui = Ui_Form_emergency()
    ui.setupUi(Form_emergency)
    Form_emergency.show()
    sys.exit(app.exec_())
