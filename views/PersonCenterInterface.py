from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget
from qfluentwidgets import (FluentIcon)

from views.UI_personCenter import Ui_personCenter
from utils.file_location import getUserIconPath


class PersonCenterInterface(Ui_personCenter, QWidget):
    def __init__(self,username,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.avatar_path = getUserIconPath()
        print(self.avatar_path)
        self.avatarwidget.setPixmap(QPixmap(self.avatar_path))
        self.avatarwidget.setRadius(64)
        self.avatarlabel.setText(f"欢迎{username}")
        self.changepwdtoolButton.setIcon(FluentIcon.EDIT)
        self.changepwdtoolButton.setText("修改密码")