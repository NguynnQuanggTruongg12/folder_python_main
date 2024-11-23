# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_err_dh.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_err_dh(object):
    def setupUi(self, Form_err_dh):
        Form_err_dh.setObjectName("Form_err_dh")
        Form_err_dh.resize(500, 201)
        Form_err_dh.setStyleSheet("")
        self.frame = QtWidgets.QFrame(Form_err_dh)
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
        self.Button_xacnhan_capnhat.setGeometry(QtCore.QRect(0, 0, 501, 201))
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
        icon.addPixmap(QtGui.QPixmap("icon/corrupted-file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_xacnhan_capnhat.setIcon(icon)
        self.Button_xacnhan_capnhat.setIconSize(QtCore.QSize(80, 80))
        self.Button_xacnhan_capnhat.setObjectName("Button_xacnhan_capnhat")

        self.retranslateUi(Form_err_dh)
        QtCore.QMetaObject.connectSlotsByName(Form_err_dh)

    def retranslateUi(self, Form_err_dh):
        _translate = QtCore.QCoreApplication.translate
        Form_err_dh.setWindowTitle(_translate("Form_err_dh", "Form"))
        self.Button_xacnhan_capnhat.setText(_translate("Form_err_dh", "Vui lòng thử lại."))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_err_dh = QtWidgets.QWidget()
    ui = Ui_Form_err_dh()
    ui.setupUi(Form_err_dh)
    Form_err_dh.show()
    sys.exit(app.exec_())
