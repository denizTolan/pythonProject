import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from auth import *
from mainform import *



class Login(QWidget):

    def __init__(self):
        super().__init__()
        self.mainWindow = MainWindow()
        self.setGeometry(300,300,300,300)
        self.setWindowTitle("Python Project Vol 1")
        self.ui()

    def ui(self):
        formLayout = QFormLayout()

        self.userNameLbl=QLabel("User Name")
        self.userNameTxt=QLineEdit()
        self.userNameTxt.setPlaceholderText("Please Enter Your User Name")
        self.passwordLbl=QLabel("Password")
        self.passwordTxt=QLineEdit()
        self.passwordTxt.setPlaceholderText("Please Enter Your Password")
        self.passwordTxt.setEchoMode(QLineEdit.Password)
        self.loginButton=QPushButton("Login")
        self.loginButton.clicked.connect(self.loginButtonClicked)

        formLayout.addRow(self.userNameLbl,self.userNameTxt)
        formLayout.addRow(self.passwordLbl,self.passwordTxt)
        formLayout.addRow(self.loginButton)

        self.setLayout(formLayout)

    def loginButtonClicked(self):
        user = UserAuth()

        if not user.checkUserNameAndPassWord(self.userNameTxt.text(),self.passwordTxt.text()):
            mbox=QMessageBox.question(self, "Warning", "Password not right", QMessageBox.Ok)
            print(f"User Name : {self.userNameTxt.text()} Password : {self.passwordTxt.text()}")

        self.hide()
        ##self.mainWindow.setStyleSheet("background-color: #fff")
        self.mainWindow.show()







