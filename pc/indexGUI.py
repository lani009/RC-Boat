import sys
import threading
from winsound import Beep

from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

UIFILE = "./ui/index.ui"
ICON = None

class App(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initLogic()
        self.initUI()
        
    def initUI(self):
        self.ui = uic.loadUi(UIFILE, self)
        self.setWindowTitle("RC-Boat")
        self.setWindowIcon(QIcon(ICON))
        self.show()

    def initLogic(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
