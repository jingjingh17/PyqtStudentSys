import sys

from PyQt6.QtWidgets import QApplication
from views.LoginWindow import LoginWindow

class mainLogin(LoginWindow):
    def __init__(self):
        super().__init__()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Logwindow = mainLogin()
    Logwindow.show()
    app.exec()