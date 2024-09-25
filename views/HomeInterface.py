from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor,QPixmap,QTextCharFormat
from PyQt6.QtWidgets import QWidget, QGraphicsDropShadowEffect,QHBoxLayout,QWidgetItem,QSizePolicy
from qfluentwidgets import (FluentIcon, InfoBar,CardWidget,
                            CheckBox,LineEdit,ToolButton,BodyLabel)

from views.UI_HomeInterface import Ui_HomeInterface
from views.infoDetailsInterface import infoDetailsInterface
from utils.nowTime import Time
from utils.weatherToicon import weatherToicon
from utils.file_location import getSysIconPath

class HomeInterface(Ui_HomeInterface, QWidget):
    def __init__(self,username, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        # 初始化任务卡片图标
        self.TaskCardAddtoolButton.setIcon(FluentIcon.ADD)
        self.TaskCardDeltoolButton.setIcon(FluentIcon.DELETE)
        self.toolButton.setIcon(FluentIcon.SAVE)
        self.toolButton_2.setIcon(FluentIcon.SAVE)
        self.toolButton_3.setIcon(FluentIcon.SAVE)

        
        
        self.sysIconPath = getSysIconPath()
        self.label_27.setPixmap(QPixmap(self.sysIconPath).scaled(120,120, Qt.AspectRatioMode.KeepAspectRatio))
        
        self.currentTime = Time().get_current_time()
        self.WelCardTimeLabel.setText(self.currentTime)
        self.WelCardTextLabel.setText("欢迎回来，" + username)
        self.WelCardTextLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.province = weatherToicon().province
        self.label.setText(self.province) 
        
        self.iconPath = weatherToicon().iconPath
        for i in range(len(self.iconPath)):
            if i == 0:
                self.WeaCardIcon0.setPixmap(QPixmap(self.iconPath[i]).scaled(60,60, Qt.AspectRatioMode.KeepAspectRatio))
                self.WeaCardIcon1.setPixmap(QPixmap(self.iconPath[i]).scaled(40, 40, Qt.AspectRatioMode.KeepAspectRatio))
            elif i == 1:
                self.WeaCardIcon2.setPixmap(QPixmap(self.iconPath[i]).scaled(40, 40, Qt.AspectRatioMode.KeepAspectRatio))
            elif i == 2:
                self.WeaCardIcon3.setPixmap(QPixmap(self.iconPath[i]).scaled(40, 40, Qt.AspectRatioMode.KeepAspectRatio))
            elif i == 3:
                self.WeaCardIcon4.setPixmap(QPixmap(self.iconPath[i]).scaled(40, 40, Qt.AspectRatioMode.KeepAspectRatio))
            elif i == 4:
                self.WeaCardIcon5.setPixmap(QPixmap(self.iconPath[i]).scaled(40, 40, Qt.AspectRatioMode.KeepAspectRatio))
               
        # 新增任务按钮
        self.TaskCardAddtoolButton.clicked.connect(self.TaskCardAddtoolButtonClicked)
        self.TaskCardDeltoolButton.clicked.connect(self.TaskCardDeltoolButtonClicked)

        # 详情点击跳转
        self.label_18.mousePressEvent = self.openInfoDetailsInterface
        self.label_21.mousePressEvent = self.openInfoDetailsInterface2

        # add shadow effect to card
        self.setShadowEffect(self.WeaCard)
        self.setShadowEffect(self.WelCard)
        self.setShadowEffect(self.NoticeCard)
        self.setShadowEffect(self.TaskCard)
        

    def setShadowEffect(self, card: QWidget):
        shadowEffect = QGraphicsDropShadowEffect(self)
        shadowEffect.setColor(QColor(0, 0, 0, 15))
        shadowEffect.setBlurRadius(10)
        shadowEffect.setOffset(0, 0)
        card.setGraphicsEffect(shadowEffect)
    
    # 打开通知详情窗口
    def openInfoDetailsInterface(self,event):
        print("openInfoDetailsInterface")
        self.detail_window = infoDetailsInterface()
        self.detail_window.show()

    # 打开通知详情窗口2--临时
    def openInfoDetailsInterface2(self,event):
        print("openInfoDetailsInterface2")
        self.detail_window = infoDetailsInterface()
        self.detail_window.plainTextEdit.setPlainText("尊敬的全体同学：\n\n为了保证期末考试的顺利进行，现将相关事项通知如下：\n\n考试时间：XX年XX月XX日至XX月XX日。\n\n考试科目：请各位同学提前查看考试安排，确认各科目的具体时间及地点。\n\n注意事项：\n请携带学生证及相关考试用品。\n考试期间保持安静，不得携带电子设备入场。\n\n如有疑问，请及时与老师联系。祝大家考试顺利！\n\n\n\n教务处")
        self.detail_window.titleLabel.setText("考试通知")
        self.detail_window.show()

    
    # 新增任务
    def TaskCardAddtoolButtonClicked(self):
        itemEditing = False
        for i in range(self.verticalLayout_12.count()):
            item = self.verticalLayout_12.itemAt(i)
            if isinstance(item, QWidgetItem):
                textEdit = item.widget().findChild(LineEdit)
                if textEdit:
                    itemEditing = True
        
        if not itemEditing:
            taskCardNum = self.verticalLayout_12.count()
            taskCard = newTaskCard(taskCardNum)
            taskCard.taskFinishButton.clicked.connect(self.TaskCardFinishButtonClicked)
            self.verticalLayout_12.insertWidget(0, taskCard)
        else:
            InfoBar.error(
                title='错误',
                content="请先输入当前任务",
                isClosable=True,
                duration=2000,
                parent=self
            )
        
    
    # 保存任务
    def TaskCardFinishButtonClicked(self):
        textEdit = self.verticalLayout_12.itemAt(0).widget().findChild(LineEdit)
        text = textEdit.text()
        if text != "":
            taskLabel = BodyLabel(text)
            # 设置标签格式确保和之前相同
            taskLabel.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            taskLabel.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
            # 替换lineEdit为Label
            taskCard = self.verticalLayout_12.itemAt(0).widget()
            taskCard.taskEdit.deleteLater()
            taskCard.hBoxLayout.insertWidget(1, taskLabel)
        else:
            print("Please enter the task")

    
    # 删除任务
    def TaskCardDeltoolButtonClicked(self):
        itemsToRemove = []
        for i in range(self.verticalLayout_12.count()):
            item = self.verticalLayout_12.itemAt(i)
            if isinstance(item, QWidgetItem):
                checkbox = item.widget().findChild(CheckBox)
                if checkbox.isChecked():
                    itemsToRemove.append(item.widget())

        if len(itemsToRemove) == 0:
            InfoBar.error(
                title='错误',
                content="请选择要删除的任务",
                isClosable=True,
                duration=2000,
                parent=self
            )       
                
        for item in itemsToRemove:
            self.verticalLayout_12.removeWidget(item)
            item.deleteLater()




class newTaskCard(CardWidget):
    
    def __init__(self, index,parent=None):
        super().__init__(parent=parent)
        
        self.index = index
        self.taskCheckBox = CheckBox(self)
        self.taskEdit = LineEdit(self)
        self.taskFinishButton = ToolButton(self)
        self.taskFinishButton.setIcon(FluentIcon.SAVE)

        self.taskCheckBox.checkStateChanged.connect(self.finishTaskCheckBox)
        
        self.hBoxLayout = QHBoxLayout(self)
        
        self.initLayout()
    
    def initLayout(self):
        self.hBoxLayout.addWidget(self.taskCheckBox)
        self.hBoxLayout.addWidget(self.taskEdit)
        self.hBoxLayout.addWidget(self.taskFinishButton)
        self.hBoxLayout.setContentsMargins(36, 9, 36, 9)

    def finishTaskCheckBox(self):
        print(f"finish task{self.index}")   

