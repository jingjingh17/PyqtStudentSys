from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor,QPixmap,QStandardItemModel,QStandardItem
from PyQt6.QtWidgets import (QWidget, QGraphicsDropShadowEffect,QHBoxLayout,QWidgetItem,QSizePolicy,
                             QAbstractItemView,QTableWidgetItem)
from qfluentwidgets import (FluentIcon, setFont, InfoBarIcon,ScrollArea,ImageLabel,CardWidget,
                            CheckBox,LineEdit,ToolButton,BodyLabel,ProgressRing)

from views.UI_courseSelectInterface import Ui_courseSelectInterface
from utils.myCourse import myCourse
from utils.courseData import courseData
from utils.course import course

class courseSelectInterface(QWidget, Ui_courseSelectInterface):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
        # 初始化分段导航
        self.SegmentedWidget.insertItem(0, "myCourse", "我的课程", self.on_home_click)
        self.SegmentedWidget.insertItem(1, "courseSelect", "选课", self.on_settings_click)

        # 初始化我的课程列表
        self.initMyCourseList()

        # 初始化课程看板
        self.initCourseBoard()

        # 初始化学分进度环
        self.initScoreRing()

        # 初始化选课列表点击事件
        self.listWidget.itemClicked.connect(self.on_listWidget_itemClicked)

        # 初始化搜索图标
        self.openCourseSearchButton.setIcon(FluentIcon.SEARCH)
        self.notOpenSearchButton.setIcon(FluentIcon.SEARCH)

        # 初始化搜索条件
        self.lineEdit.setPlaceholderText('输入课程名称')
        self.collegeLineEdit.setPlaceholderText('输入课程名称')
        self.colleges = myCourse().getColleges(self.courseList)
        self.openCourseBox.addItems(self.colleges)
        self.comboBox.addItems(self.colleges)
        
        # 初始化开放课程列表
        self.initOpenList()

        # 初始化未开放选课列表
        self.initNoOpenList()

    def on_home_click(self):
        self.stackedWidget.setCurrentIndex(0)

    def on_settings_click(self):
        self.stackedWidget.setCurrentIndex(1)

    def initMyCourseList(self):
        # 课程总数，已选学分，课程信息
        self.courseNum,self.score,self.courseList = myCourse().getCourse()
        self.totalScore = myCourse().totalScore
        
        self.tableWidget.setRowCount(self.courseNum)
        for i in range(len(self.courseList)):
            row_data = self.courseList[i]
            for j,key in enumerate(row_data):
                value = row_data[key]
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))
    
    def initCourseBoard(self):
        self.label.setText(str(self.courseNum))
        self.label_4.setText(str(self.score))
        self.label_6.setText(str(self.totalScore))
        self.remainScore = self.totalScore - self.score
        self.label_8.setText(
            f'学分已满，超出 {abs(self.remainScore)} 分' if self.remainScore < 0 else
            '学分已满' if self.remainScore == 0 else
            str(self.remainScore)
        )

    def initScoreRing(self):
        setFont(self.progressBar,24)
        self.progressBar.setTextVisible(True)
        self.progressBar.setRange(0, self.totalScore)
        if self.remainScore <=0 :
            self.progressBar.setValue(self.totalScore)
        else:
            self.progressBar.setValue(self.score)

    def on_listWidget_itemClicked(self, item):
        text = item.text()
        if text == "开放选课":
            self.stackedWidget_2.setCurrentIndex(0)
        elif text == "未开放选课":
            self.stackedWidget_2.setCurrentIndex(1)

    def initOpenList(self):
        self.openModel = QStandardItemModel()
        self.openModel.setHorizontalHeaderLabels(["课程ID","课程编号", "课程名称", "学院", "课程数量", 
                                                "已选数量","开放", "学分","教师","教师ID"])
        self.tableView.setModel(self.openModel)
        # 表格不可编辑
        self.tableView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        
        # 隐藏ID列
        self.tableView.setColumnWidth(0,0)
        self.tableView.setColumnWidth(9,0)

        # 所有课程数据
        self.courseData = course().inquireCourse()

        # 开放选课数据
        openData = []
        for i in range(len(self.courseData)):
            row_data = self.courseData[i]
            if row_data[6] == 1:
                openData.append(row_data)
                
        # 渲染开放课程列表
        for i in range(len(openData)):
            row_data = openData[i]
            for j in range(len(row_data)):
                if j == 5 and row_data[j] == 1:
                    self.openModel.setItem(i, j, QStandardItem("是"))
                else:
                    self.openModel.setItem(i, j, QStandardItem(str(row_data[j])))
            else:
                continue


    def initNoOpenList(self):
        self.noOpenModel = QStandardItemModel()
        self.noOpenModel.setHorizontalHeaderLabels(["课程ID","课程编号", "课程名称", "学院", "课程数量", 
                                                    "已选数量","开放", "学分","教师","教师ID"])
        self.tableView_2.setModel(self.noOpenModel)
        # 表格不可编辑
        self.tableView_2.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        
        # 隐藏ID列
        self.tableView_2.setColumnWidth(0,0)
        self.tableView_2.setColumnWidth(9,0)
        
        # 所有课程数据
        self.courseData = course().inquireCourse()

        # 开放选课数据
        noOpenData = []
        for i in range(len(self.courseData)):
            row_data = self.courseData[i]
            if row_data[6] == 0:
                noOpenData.append(row_data)
                
        # 渲染开放课程列表
        for i in range(len(noOpenData)):
            row_data = noOpenData[i]
            for j in range(len(row_data)):
                if j == 5 and row_data[j] == 0:
                    self.noOpenModel.setItem(i, j, QStandardItem("否"))
                else:
                    self.noOpenModel.setItem(i, j, QStandardItem(str(row_data[j])))
            else:
                continue

                