import sys
from PyQt5.QtWidgets import *
from UserControls.maintabcontrol import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(300,300,300,300)
        self.setWindowTitle("Menu Form")

        self.verticalBox = QHBoxLayout(self)
        self.ui()

    def ui(self):
        ################ Menu Bar ###################
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        about = menubar.addMenu("About")

        ################# Sub Menu Bar ###############
        new=QAction("New Project", self)
        new.triggered.connect(self.new_project_onclick)
        file.addAction(new)
        secondone = QAction("About2", self)
        about.addAction(secondone)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

    def new_project_onclick(self):
        #self.verticalBox = None
        self.table_widget.add_tab()

