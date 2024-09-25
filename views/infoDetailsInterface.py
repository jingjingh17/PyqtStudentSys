import sys
from PyQt6.QtWidgets import QApplication,QWidget

from views.UI_infoDetails import Ui_inforDetail

class infoDetailsInterface(Ui_inforDetail, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.plainTextEdit.setReadOnly(True)
        self.retranslateUi(self)
        self.setWindowTitle("详情")
        


if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    win = infoDetailsInterface()
    win.show()
    sys.exit(app.exec())
    