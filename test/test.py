import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QTableView, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QAbstractItemView
)
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtCore import QModelIndex


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTableView with Always Visible Buttons")
        self.resize(400, 300)

        layout = QVBoxLayout()

        # 创建模型
        self.model = QStandardItemModel(4, 3)
        for row in range(4):
            for column in range(3):
                item = QStandardItem(f"Item {row},{column}")
                self.model.setItem(row, column, item)

        # 创建 QTableView
        self.table_view = QTableView()
        self.table_view.setModel(self.model)
        self.table_view.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        # 在表格的第三列添加按钮
        for row in range(4):
            # 创建按钮
            button = QPushButton("Click")
            button.clicked.connect(lambda _, r=row: self.handleButtonClicked(r))
            # 将按钮放置到表格的第三列
            self.table_view.setIndexWidget(self.model.index(row, 2), button)

        layout.addWidget(self.table_view)
        self.setLayout(layout)

    def handleButtonClicked(self, row):
        print(f"Button clicked at row {row}")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
