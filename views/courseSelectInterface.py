from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor,QPixmap,QStandardItemModel,QStandardItem
from PyQt6.QtWidgets import (QWidget,QAbstractItemView,QTableWidgetItem)
from qfluentwidgets import (FluentIcon, setFont, PrimaryPushButton, MessageBox,InfoBarIcon,InfoBar)

from views.UI_courseSelectInterface import Ui_courseSelectInterface
from utils.myCourse import myCourse
from utils.course import course

class courseSelectInterface(QWidget, Ui_courseSelectInterface):
    def __init__(self, userid,role):
        super().__init__()
        self.setupUi(self)
        self.userid = userid
        self.role = role  
        # 初始化分段导航
        self.SegmentedWidget.insertItem(0, "myCourse", "我的课程", self.on_home_click)
        self.SegmentedWidget.insertItem(1, "courseSelect", "选课", self.on_settings_click)

        # 实例化course
        self.course = course()

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
        
        
        # 初始化开放课程列表
        self.initOpenList()

        # 初始化未开放选课列表
        self.initNoOpenList()

    def on_home_click(self):
        self.stackedWidget.setCurrentIndex(0)

    def on_settings_click(self):
        self.stackedWidget.setCurrentIndex(1)

    def initMyCourseList(self):
        self.myCourseScore = 0
        self.totalScore = 30

        # 清空现有的表格内容
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)

        print("我的课程列表初始化中...")
        
        # 初始化表头
        headers = ["学生ID","课程ID","课程编号", "课程名称", "学院", "学生数量", "课程状态", "学分","教师","教师ID"]
        self.tableWidget.setHorizontalHeaderLabels(headers)
        
        # 获取我的课程数据
        self.courseList = course().myCourse(self.userid)
        self.myCourseNum = len(self.courseList)

        # 渲染我的课程列表
        self.tableWidget.setRowCount(self.myCourseNum)
        for i in range(len(self.courseList)):
            row_data = self.courseList[i]
            for j in range(len(row_data)):
                value = row_data[j]
                if j == 6:
                    value = self.status_to_text(int(value))
                if j == 7:
                    self.myCourseScore += value
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))
        
        # 隐藏ID列
        self.tableWidget.setColumnHidden(0, True)
        self.tableWidget.setColumnHidden(1, True)
        self.tableWidget.setColumnHidden(9, True)

        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
    
    def status_to_text(self,status):
        if status == 1:
            return "选课中"
        elif status == 0:
            return "选课结束"
        else:
            return str(status)
    
    def initCourseBoard(self):

        # 清空现有的显示内容
        self.label.setText("")
        self.label_4.setText("")
        self.label_6.setText("")
        self.label_8.setText("")
        print("课程看板初始化中...")
        
        self.label.setText(str(self.myCourseNum))
        self.label_4.setText(str(self.myCourseScore))
        self.label_6.setText(str(self.totalScore))
        self.remainScore = self.totalScore - self.myCourseScore
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
            self.progressBar.setValue(int(self.myCourseScore))

    def on_listWidget_itemClicked(self, item):
        text = item.text()
        if text == "开放选课":
            self.stackedWidget_2.setCurrentIndex(0)
        elif text == "未开放选课":
            self.stackedWidget_2.setCurrentIndex(1)

    def initOpenList(self):
        self.openModel = QStandardItemModel()
        self.openModel.setHorizontalHeaderLabels(["课程ID","课程编号", "课程名称", "学院", "课程数量", 
                                                "已选数量","开放", "学分","教师","教师ID","选课"])
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
                if j == 6 and row_data[j] == 1:
                    self.openModel.setItem(i, j, QStandardItem("是"))
                else:
                    self.openModel.setItem(i, j, QStandardItem(str(row_data[j])))
            else:
                continue

        # 增加选课按钮
        for i in range(len(openData)):
            submitButton = PrimaryPushButton("选课")
            submitButton.clicked.connect(lambda _, row=i: self.submitButtonClicked(row))
            self.tableView.setIndexWidget(self.openModel.index(i, 10), submitButton)


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

        # 未开放选课数据
        noOpenData = []
        for i in range(len(self.courseData)):
            row_data = self.courseData[i]
            if row_data[6] == 0:
                noOpenData.append(row_data)
                
        # 渲染未开放课程列表
        for i in range(len(noOpenData)):
            row_data = noOpenData[i]
            for j in range(len(row_data)):
                if j == 5 and row_data[j] == 0:
                    self.noOpenModel.setItem(i, j, QStandardItem("否"))
                else:
                    self.noOpenModel.setItem(i, j, QStandardItem(str(row_data[j])))
            else:
                continue

    # 选课提交弹出确认框
    def submitButtonClicked(self,row):
        courseId = int(self.openModel.item(row,0).text())
        studentId = self.userid

        confirMessage = "确认选择:" + "\n" + str(self.openModel.item(row,2).text()) + ","+str(self.openModel.item(row,3).text()) + ","+str(self.openModel.item(row,8).text())+ "吗？"
        messageBox = MessageBox("确认",confirMessage,self)
        messageBox.yesButton.setText("确定")
        messageBox.cancelButton.setText("取消")

        # 提交选课逻辑
        if messageBox.exec():
            """
            提交至Enrollments表中
            """
            if self.role == "student":
                if self.course.seleCourse(studentId,courseId) == True:
                    self.initMyCourseList()
                    self.initCourseBoard()
                    self.initScoreRing()
                    InfoBar.success(
                        title='成功',
                        content="选课成功",
                        isClosable=True,
                        duration=2000,
                        parent=self
                    )
                elif self.course.seleCourse(studentId,courseId) == "重复选课":
                    InfoBar.error(
                        title='选课失败',
                        content="重复选课",
                        isClosable=True,
                        duration=2000,
                        parent=self
                    )
                elif self.course.seleCourse(studentId,courseId) == "课满":
                    InfoBar.error(
                        title='选课失败',
                        content="课程已满",
                        isClosable=True,
                        duration=2000,
                        parent=self
                    )
            else:
                InfoBar.error(
                    title='角色错误',
                    content=f"您当前的角色为{self.role}，无法选课！请切换为学生角色！",
                    isClosable=True,
                    duration=2000,
                    parent=self
                )
        else:
            print("取消选课请求")
        print(courseId)
