from PyQt6.QtWidgets import QApplication
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor,QPixmap,QIcon
from PyQt6.QtWidgets import QWidget, QGraphicsDropShadowEffect,QHBoxLayout,QWidgetItem,QSizePolicy,QMainWindow
from qfluentwidgets import (InfoBar)

from views.UI_RegisterWindow import Ui_Form
from utils.login import Auth
from utils.file_location import getSysIconPath


class RegisterWindow(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.sysicon = getSysIconPath()
        self.setWindowTitle("注册")
        self.setWindowIcon(QIcon(self.sysicon))
        
        self.label.setPixmap(QPixmap(self.sysicon).scaled(300,300, Qt.AspectRatioMode.KeepAspectRatio))
        self.label_2.setPixmap(QPixmap(self.sysicon))

        self.pushButton_2.clicked.connect(self.backLogin)
        self.pushButton.clicked.connect(self.register)

    def backLogin(self):
        self.close()
        from views.LoginWindow import LoginWindow
        self.loginWindow = LoginWindow()
        self.loginWindow.show()

    def register(self):
        self.username = self.lineEdit_3.text()
        self.password = self.lineEdit_4.text()
        self.password2 = self.lineEdit.text()
        if self.username == "" or self.password == "":
            InfoBar.error(
                title='用户名或密码为空',
                content="请检查后注册",
                isClosable=True,
                duration=2000,
                parent=self
            )
        elif self.password == self.password2:
            auth = Auth()
            if auth.check_user_register(self.username,self.password):
                InfoBar.success(
                title='注册成功',
                content="请登录",
                isClosable=True,
                duration=2000,
                parent=self
            )
            else:
                InfoBar.error(
                title='用户名已存在',
                content="请更换用户名",
                isClosable=True,
                duration=2000,
                parent=self
            )
        else:
            InfoBar.error(
                title='密码不一致',
                content="请检查后输入",
                isClosable=True,
                duration=2000,
                parent=self
            )

        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegisterWindow()
    window.show()
    app.exec()
