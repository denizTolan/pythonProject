import sys
from login import *
from mainform import *

def main():
    App = QApplication(sys.argv)
    window = Login()
    #window = MainWindow()
    window.show()
    sys.exit(App.exec())

if __name__ == "__main__":
    main()

