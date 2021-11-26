import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://duckduckgo.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navigation bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # the back button
        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        back_btn.setIcon(QIcon("back.png"))
        back_btn.setToolTip("go backwards in your history")
        navbar.addAction(back_btn)

        # the forward button
        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        forward_btn.setToolTip("go forwards in your history")
        forward_btn.setIcon(QIcon("forward.png"))
        navbar.addAction(forward_btn)

        # the reload button
        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        reload_btn.setIcon(QIcon("reload.png"))
        reload_btn.setToolTip("Reload your currently opened page")
        navbar.addAction(reload_btn)

        # the home button
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.nav_home)
        home_btn.setIcon(QIcon("home.png"))
        home_btn.setToolTip("go to your homepage")
        navbar.addAction(home_btn)

    def nav_home(self):
        self.browser.setUrl(QUrl('http://duck.com'))


app = QApplication(sys.argv)
QApplication.setApplicationName('PyBrowser')
app.setWindowIcon(QIcon("Browser.png"))
window = MainWindow()
app.exec_()
