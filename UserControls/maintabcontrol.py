import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from UserControls.tabcontentcontrol import *


class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()

        self.tabs.resize(300, 200)

        # Add Close Button
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab_button)

        # Add tabs
        self.add_tab()
        self.add_tab()

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def add_tab(self):

        tab = TabContentControl(self)
        self.tabs.addTab(tab, tab.tab_name)





    def close_tab_button(self, currentIndex):
        currentQWidget = self.tabs.widget(currentIndex)
        currentQWidget.deleteLater()
        self.tabs.removeTab(currentIndex)

