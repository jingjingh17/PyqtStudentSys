from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor,QPixmap
from PyQt6.QtWidgets import QWidget, QGraphicsDropShadowEffect,QHBoxLayout,QWidgetItem,QSizePolicy
from qfluentwidgets import (FluentIcon, setFont, InfoBarIcon,ScrollArea,ImageLabel,CardWidget,
                            CheckBox,LineEdit,ToolButton,BodyLabel)

from views.UI_LoginWindow import Ui_Form

from utils.login import Auth

class LoginWindow(Ui_Form, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.setWindowTitle("登录")

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
            print("登录失败")

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
        print("注册窗口打开")
