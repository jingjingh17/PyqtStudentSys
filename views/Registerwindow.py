from PyQt6.QtWidgets import QApplication
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor,QPixmap
from PyQt6.QtWidgets import QWidget, QGraphicsDropShadowEffect,QHBoxLayout,QWidgetItem,QSizePolicy,QMainWindow
from qfluentwidgets import (FluentIcon, setFont, InfoBarIcon,ScrollArea,ImageLabel,CardWidget,
                            CheckBox,LineEdit,ToolButton,BodyLabel)

from views.UI_RegisterWindow import Ui_Form

class RegisterWindow(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("注册")

        self.pushButton_2.clicked.connect(self.backLogin)
        self.pushButton.clicked.connect(self.register)

    def backLogin(self):
        print("返回登录")

    def register(self):
        print("注册提交")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegisterWindow()
    window.show()
    app.exec()
