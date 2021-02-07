import sys
from PyQt5.QtWidgets import *

class FileControl(QWidget):

    def __init__(self,parent=None):
        super(FileControl,self).__init__(parent)
        self.ui()

    def ui(self):
        self.namelbl=QLabel("file",self)