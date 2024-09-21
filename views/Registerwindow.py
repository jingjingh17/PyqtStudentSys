from PyQt6.QtWidgets import QApplication
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor,QPixmap
from PyQt6.QtWidgets import QWidget, QGraphicsDropShadowEffect,QHBoxLayout,QWidgetItem,QSizePolicy,QMainWindow
from qfluentwidgets import (FluentIcon, setFont, InfoBarIcon,ScrollArea,ImageLabel,CardWidget,
                            CheckBox,LineEdit,ToolButton,BodyLabel)

from views.UI_RegisterWindow import Ui_Form
from utils.login import Auth

class RegisterWindow(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("注册")

        self.pushButton_2.clicked.connect(self.backLogin)
        self.pushButton.clicked.connect(self.register)

    def backLogin(self):
        self.close()
        from views.LoginWindow import LoginWindow
        self.loginWindow = LoginWindow()
        self.loginWindow.show()
        print("返回登录")

    def register(self):
        self.username = self.lineEdit_3.text()
        self.password = self.lineEdit_4.text()
        self.password2 = self.lineEdit.text()
        if self.username == "" or self.password == "":
            print("用户名或密码为空")
        elif self.password == self.password2:
            auth = Auth()
            if auth.check_user_register(self.username,self.password):
                print("注册成功")
            else:
                print("用户名已存在")
        else:
            print("密码不一致")
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegisterWindow()
    window.show()
    app.exec()
