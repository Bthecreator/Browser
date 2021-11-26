import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.browser =
        self.showMaximized()


app = QApplication(sys.argv)
QApplication.setApplicationName("Pybrowser")
window=Mainwindow()
app.exec_()