from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5 import uic


class LOGIN(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("loginUi1.ui", self)
