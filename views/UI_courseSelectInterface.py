# Form implementation generated from reading ui file 'courseSelectInterface.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_courseSelectInterface(object):
    def setupUi(self, courseSelectInterface):
        courseSelectInterface.setObjectName("courseSelectInterface")
        courseSelectInterface.resize(777, 609)
        self.verticalLayout = QtWidgets.QVBoxLayout(courseSelectInterface)
        self.verticalLayout.setObjectName("verticalLayout")
        self.SegmentedWidget = SegmentedWidget(parent=courseSelectInterface)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SegmentedWidget.sizePolicy().hasHeightForWidth())
        self.SegmentedWidget.setSizePolicy(sizePolicy)
        self.SegmentedWidget.setMinimumSize(QtCore.QSize(0, 50))
        self.SegmentedWidget.setMaximumSize(QtCore.QSize(16777215, 200))
        self.SegmentedWidget.setObjectName("SegmentedWidget")
        self.verticalLayout.addWidget(self.SegmentedWidget)
        self.stackedWidget = QtWidgets.QStackedWidget(parent=courseSelectInterface)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = ScrollArea(parent=self.page)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 739, 515))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.myInfoCardWidget = CardWidget(parent=self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.myInfoCardWidget.sizePolicy().hasHeightForWidth())
        self.myInfoCardWidget.setSizePolicy(sizePolicy)
        self.myInfoCardWidget.setMinimumSize(QtCore.QSize(200, 50))
        self.myInfoCardWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.myInfoCardWidget.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.myInfoCardWidget.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.myInfoCardWidget.setObjectName("myInfoCardWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.myInfoCardWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_9 = StrongBodyLabel(parent=self.myInfoCardWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(20, 20))
        self.label_9.setMaximumSize(QtCore.QSize(500, 50))
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.label = BodyLabel(parent=self.myInfoCardWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 8)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = StrongBodyLabel(parent=self.myInfoCardWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.label_4 = BodyLabel(parent=self.myInfoCardWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 8)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = StrongBodyLabel(parent=self.myInfoCardWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.label_6 = BodyLabel(parent=self.myInfoCardWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 8)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = StrongBodyLabel(parent=self.myInfoCardWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.label_8 = BodyLabel(parent=self.myInfoCardWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 8)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(50, -1, 30, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.progressBar = ProgressRing(parent=self.myInfoCardWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QtCore.QSize(150, 150))
        self.progressBar.setMaximumSize(QtCore.QSize(220, 220))
        self.progressBar.setMaximum(35)
        self.progressBar.setProperty("value", 30)
        self.progressBar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_7.addWidget(self.progressBar)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_4.addWidget(self.myInfoCardWidget)
        self.tableCardWidget = CardWidget(parent=self.scrollAreaWidgetContents)
        self.tableCardWidget.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.tableCardWidget.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.tableCardWidget.setObjectName("tableCardWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tableCardWidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.tableCardWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.verticalLayout_5.addWidget(self.tableWidget)
        self.verticalLayout_4.addWidget(self.tableCardWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.courseSelectCard = QtWidgets.QFrame(parent=self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.courseSelectCard.sizePolicy().hasHeightForWidth())
        self.courseSelectCard.setSizePolicy(sizePolicy)
        self.courseSelectCard.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.courseSelectCard.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.courseSelectCard.setObjectName("courseSelectCard")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.courseSelectCard)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_3 = LargeTitleLabel(parent=self.courseSelectCard)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.listWidget = ListWidget(parent=self.courseSelectCard)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.listWidget.addItem(item)
        self.verticalLayout_10.addWidget(self.listWidget)
        self.horizontalLayout_6.addLayout(self.verticalLayout_10)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(parent=self.courseSelectCard)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.openCoursePage = QtWidgets.QWidget()
        self.openCoursePage.setObjectName("openCoursePage")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.openCoursePage)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.collegeLineEdit = LineEdit(parent=self.openCoursePage)
        self.collegeLineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.collegeLineEdit.setObjectName("collegeLineEdit")
        self.horizontalLayout_10.addWidget(self.collegeLineEdit)
        self.doubleSpinBox = DoubleSpinBox(parent=self.openCoursePage)
        self.doubleSpinBox.setDecimals(1)
        self.doubleSpinBox.setSingleStep(0.5)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout_10.addWidget(self.doubleSpinBox)
        self.openCourseBox = ComboBox(parent=self.openCoursePage)
        self.openCourseBox.setCurrentText("")
        self.openCourseBox.setObjectName("openCourseBox")
        self.horizontalLayout_10.addWidget(self.openCourseBox)
        self.openCourseSearchButton = ToolButton(parent=self.openCoursePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openCourseSearchButton.sizePolicy().hasHeightForWidth())
        self.openCourseSearchButton.setSizePolicy(sizePolicy)
        self.openCourseSearchButton.setMaximumSize(QtCore.QSize(50, 50))
        self.openCourseSearchButton.setText("")
        self.openCourseSearchButton.setObjectName("openCourseSearchButton")
        self.horizontalLayout_10.addWidget(self.openCourseSearchButton)
        self.verticalLayout_11.addLayout(self.horizontalLayout_10)
        self.tableView = TableView(parent=self.openCoursePage)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_11.addWidget(self.tableView)
        self.stackedWidget_2.addWidget(self.openCoursePage)
        self.notOpenCoursePage = QtWidgets.QWidget()
        self.notOpenCoursePage.setObjectName("notOpenCoursePage")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.notOpenCoursePage)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lineEdit = LineEdit(parent=self.notOpenCoursePage)
        self.lineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_9.addWidget(self.lineEdit)
        self.doubleSpinBox_2 = DoubleSpinBox(parent=self.notOpenCoursePage)
        self.doubleSpinBox_2.setDecimals(1)
        self.doubleSpinBox_2.setSingleStep(0.5)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.horizontalLayout_9.addWidget(self.doubleSpinBox_2)
        self.comboBox = ComboBox(parent=self.notOpenCoursePage)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_9.addWidget(self.comboBox)
        self.notOpenSearchButton = ToolButton(parent=self.notOpenCoursePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notOpenSearchButton.sizePolicy().hasHeightForWidth())
        self.notOpenSearchButton.setSizePolicy(sizePolicy)
        self.notOpenSearchButton.setMaximumSize(QtCore.QSize(50, 50))
        self.notOpenSearchButton.setText("")
        self.notOpenSearchButton.setObjectName("notOpenSearchButton")
        self.horizontalLayout_9.addWidget(self.notOpenSearchButton)
        self.verticalLayout_12.addLayout(self.horizontalLayout_9)
        self.tableView_2 = TableView(parent=self.notOpenCoursePage)
        self.tableView_2.setObjectName("tableView_2")
        self.verticalLayout_12.addWidget(self.tableView_2)
        self.stackedWidget_2.addWidget(self.notOpenCoursePage)
        self.verticalLayout_9.addWidget(self.stackedWidget_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_9)
        self.horizontalLayout_6.setStretch(0, 2)
        self.horizontalLayout_6.setStretch(1, 8)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 9)
        self.verticalLayout_3.addWidget(self.courseSelectCard)
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(courseSelectInterface)
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(courseSelectInterface)

    def retranslateUi(self, courseSelectInterface):
        _translate = QtCore.QCoreApplication.translate
        courseSelectInterface.setWindowTitle(_translate("courseSelectInterface", "Form"))
        self.label_9.setText(_translate("courseSelectInterface", "已选课程"))
        self.label.setText(_translate("courseSelectInterface", "7"))
        self.label_2.setText(_translate("courseSelectInterface", "我的总学分"))
        self.label_4.setText(_translate("courseSelectInterface", "26"))
        self.label_5.setText(_translate("courseSelectInterface", "要求学分"))
        self.label_6.setText(_translate("courseSelectInterface", "35"))
        self.label_7.setText(_translate("courseSelectInterface", "需选学分"))
        self.label_8.setText(_translate("courseSelectInterface", "9"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("courseSelectInterface", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("courseSelectInterface", "课程名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("courseSelectInterface", "所属学院"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("courseSelectInterface", "主讲老师"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("courseSelectInterface", "课程数量"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("courseSelectInterface", "是否开课"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("courseSelectInterface", "是否结课"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("courseSelectInterface", "课程学分"))
        self.label_3.setText(_translate("courseSelectInterface", "2024-2025课程选择"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("courseSelectInterface", "开放选课"))
        item = self.listWidget.item(1)
        item.setText(_translate("courseSelectInterface", "未开放选课"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
from qfluentwidgets import BodyLabel, CardWidget, ComboBox, DoubleSpinBox, LargeTitleLabel, LineEdit, ListWidget, ProgressRing, ScrollArea, SegmentedWidget, StrongBodyLabel, TableView, ToolButton
