# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_save.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_save_setting(object):
    def setupUi(self, Form_save_setting):
        Form_save_setting.setObjectName("Form_save_setting")
        Form_save_setting.resize(500, 201)
        Form_save_setting.setStyleSheet("")
        self.frame = QtWidgets.QFrame(Form_save_setting)
        self.frame.setGeometry(QtCore.QRect(0, 0, 500, 201))
        self.frame.setMinimumSize(QtCore.QSize(500, 200))
        self.frame.setMaximumSize(QtCore.QSize(750, 550))
        self.frame.setStyleSheet("background-color: rgb(230, 230, 230);\n"
"border-radius: 5px;\n"
"box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5);")
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Button_xacnhan_capnhat = QtWidgets.QPushButton(self.frame)
        self.Button_xacnhan_capnhat.setGeometry(QtCore.QRect(10, 10, 481, 181))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Button_xacnhan_capnhat.setFont(font)
        self.Button_xacnhan_capnhat.setStyleSheet("QPushButton#Button_xacnhan_capnhat\n"
"{\n"
"    border-radius: 20px;\n"
"    font: 75 22pt \"MS Shell Dlg 2\";\n"
"    border: 1px solid rgb(230, 230, 230);\n"
"    background-color: rgb(250, 250, 250);\n"
"/*border: 3px solid rgb(0, 0, 255);*/\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_xacnhan_capnhat.setIcon(icon)
        self.Button_xacnhan_capnhat.setIconSize(QtCore.QSize(80, 80))
        self.Button_xacnhan_capnhat.setObjectName("Button_xacnhan_capnhat")

        self.retranslateUi(Form_save_setting)
        QtCore.QMetaObject.connectSlotsByName(Form_save_setting)

    def retranslateUi(self, Form_save_setting):
        _translate = QtCore.QCoreApplication.translate
        Form_save_setting.setWindowTitle(_translate("Form_save_setting", "Form"))
        self.Button_xacnhan_capnhat.setText(_translate("Form_save_setting", "  Đã hoàn tất thay đổi."))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_save_setting = QtWidgets.QWidget()
    ui = Ui_Form_save_setting()
    ui.setupUi(Form_save_setting)
    Form_save_setting.show()
    sys.exit(app.exec_())
