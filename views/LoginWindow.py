from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor,QPixmap,QIcon
from PyQt6.QtWidgets import QWidget, QGraphicsDropShadowEffect,QHBoxLayout,QWidgetItem,QSizePolicy
from qfluentwidgets import (InfoBar)

from views.UI_LoginWindow import Ui_Form

from utils.login import Auth
from utils.file_location import getSysIconPath

class LoginWindow(Ui_Form, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        
        self.sysicon = getSysIconPath()
        self.setWindowTitle("登录")
        self.setWindowIcon(QIcon(self.sysicon))
        
        self.label.setPixmap(QPixmap(self.sysicon).scaled(300,300, Qt.AspectRatioMode.KeepAspectRatio))
        self.label_2.setPixmap(QPixmap(self.sysicon))

        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.register)

    def login(self):
        usename = self.lineEdit_3.text()
        password = self.lineEdit_4.text()
        if Auth().check_user_login(usename,password):
            print("登录成功","用户名",usename,"密码",password)
            self.close()
            self.showMainWindow()
        else:
            InfoBar.error(
                title='用户名或密码错误',
                content="请检查",
                isClosable=True,
                duration=2000,
                parent=self
            )

    def register(self):
        self.close()
        self.showRegisterWindow()

    def showMainWindow(self):
        from main_window import Window
        mainWindow = Window()
        mainWindow.show()

    def showRegisterWindow(self):
        from views.Registerwindow import RegisterWindow
        # 这里必须用self.registerWindow,如果使用registerWindow当作变量名，执行完后他会销毁导致窗口闪退(局部变量)
        self.registerWindow = RegisterWindow()
        self.registerWindow.show()
