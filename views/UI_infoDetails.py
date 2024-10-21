# Form implementation generated from reading ui file 'infoDetails.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_inforDetail(object):
    def setupUi(self, inforDetail):
        inforDetail.setObjectName("inforDetail")
        inforDetail.resize(630, 516)
        self.verticalLayout = QtWidgets.QVBoxLayout(inforDetail)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(parent=inforDetail)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 610, 496))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titleLabel = LargeTitleLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        self.titleLabel.setMaximumSize(QtCore.QSize(16777215, 80))
        self.titleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout_2.addWidget(self.titleLabel)
        self.line = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.authorLabel = BodyLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.authorLabel.sizePolicy().hasHeightForWidth())
        self.authorLabel.setSizePolicy(sizePolicy)
        self.authorLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.authorLabel.setObjectName("authorLabel")
        self.verticalLayout_2.addWidget(self.authorLabel)
        self.line_2 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.plainTextEdit = PlainTextEdit(parent=self.scrollAreaWidgetContents)
        self.plainTextEdit.setOverwriteMode(False)
        self.plainTextEdit.setBackgroundVisible(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_2.addWidget(self.plainTextEdit)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(inforDetail)
        QtCore.QMetaObject.connectSlotsByName(inforDetail)

    def retranslateUi(self, inforDetail):
        _translate = QtCore.QCoreApplication.translate
        inforDetail.setWindowTitle(_translate("inforDetail", "Form"))
        self.titleLabel.setText(_translate("inforDetail", "关于2024国庆放假通知"))
        self.authorLabel.setText(_translate("inforDetail", "NYM编辑员  2024-9-21 编辑于 北京"))
        self.plainTextEdit.setPlainText(_translate("inforDetail", "各单位：\n"
"根据《国务院办公厅关于2024年部分节假日安排的通知》（国办发明电〔2023〕7号）和我校工作实际，现将学校2024年国庆节放假相关事宜通知如下。\n"
"10月1日（星期二）至7日（星期一）放假调休，共7天。9月29日（星期日）、10月12日（星期六）上班，并分别安排10月4日（星期五）、10月7日（星期一）的教学活动。\n"
"各单位要妥善安排好值班值守和安全保卫相关工作，确保责任到人。遇有重大突发事件，要按规定及时报告并妥善处置，确保全校师生平安祥和度过假期。\n"
""))
from qfluentwidgets import BodyLabel, LargeTitleLabel, PlainTextEdit