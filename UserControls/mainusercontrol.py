import sys
from PyQt5.QtWidgets import *

class MainControl(QWidget):

    def __init__(self,parent=None):
        super(MainControl,self).__init__(parent)
        self.ui()

    def ui(self):
        self.namelbl=QLabel("main",self)