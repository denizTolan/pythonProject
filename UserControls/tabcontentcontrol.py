import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from UserControls.imagecontrol import *


class TabContentControl(QWidget):

    tab_name = "Tab"
    form_image = None

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.tab_name = f"Tab : {random.randint(1, 1000)}"
        # Tab Content
        self.layout = QVBoxLayout(self)

        print(type(parent))
        # Add Button
        push_button = QPushButton(f"{self.tab_name} button")
        push_button.clicked.connect(self.on_click)
        self.layout.addWidget(push_button)

        self.lbl_image = ImageWidget()
        self.layout.addWidget(self.lbl_image)

        self.setLayout(self.layout)

    def on_click(self):
        print(f"{self.sender().text()} clicked")

        # Add Image

        self.form_image = QPixmap(f"images/{random.randint(1,4)}.jpg")
        self.lbl_image.setPixmap(self.form_image)
        self.lbl_image.resize(self.form_image.width(), self.form_image.height())