# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designeruoSqYD.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import images_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1127, 800)
        Form.setMinimumSize(QSize(1127, 800))
        Form.setWindowOpacity(1.000000000000000)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:none;")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sign_in_panel = QFrame(Form)
        self.sign_in_panel.setObjectName(u"sign_in_panel")
        self.sign_in_panel.setMaximumSize(QSize(450, 16777215))
        self.sign_in_panel.setAutoFillBackground(False)
        self.sign_in_panel.setFrameShape(QFrame.WinPanel)
        self.sign_in_panel.setFrameShadow(QFrame.Raised)
        self.sign_in_panel.setLineWidth(1)
        self.verticalLayout = QVBoxLayout(self.sign_in_panel)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.sign_in_panel)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(0, 250))
        self.logo.setFrameShape(QFrame.WinPanel)
        self.logo.setFrameShadow(QFrame.Raised)
        self.image = QLabel(self.logo)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(-20, 10, 491, 271))
        self.image.setStyleSheet(u"background-image: url(:/images/Images/logo.png);")
        self.image.setPixmap(QPixmap(u":/images/Images/logo.png"))
        self.image.setScaledContents(True)

        self.verticalLayout.addWidget(self.logo)

        self.sign_in_text = QFrame(self.sign_in_panel)
        self.sign_in_text.setObjectName(u"sign_in_text")
        self.sign_in_text.setMaximumSize(QSize(16777215, 80))
        self.sign_in_text.setFrameShape(QFrame.WinPanel)
        self.sign_in_text.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.sign_in_text)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.text = QLabel(self.sign_in_text)
        self.text.setObjectName(u"text")
        font = QFont()
        font.setFamily(u"Ebrima")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.text.setFont(font)
        self.text.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.text)


        self.verticalLayout.addWidget(self.sign_in_text)

        self.contents = QFrame(self.sign_in_panel)
        self.contents.setObjectName(u"contents")
        self.contents.setFrameShape(QFrame.WinPanel)
        self.contents.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.contents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.HR_ID = QLabel(self.contents)
        self.HR_ID.setObjectName(u"HR_ID")
        self.HR_ID.setMaximumSize(QSize(16777215, 35))
        font1 = QFont()
        font1.setFamily(u"Catamaran ExtraLight")
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setWeight(75)
        self.HR_ID.setFont(font1)
        self.HR_ID.setStyleSheet(u"margin-left:56px;\n"
"")
        self.HR_ID.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.HR_ID.setMargin(0)

        self.verticalLayout_3.addWidget(self.HR_ID)

        self.HR_ID_BOX = QLineEdit(self.contents)
        self.HR_ID_BOX.setObjectName(u"HR_ID_BOX")
        self.HR_ID_BOX.setEnabled(True)
        self.HR_ID_BOX.setMinimumSize(QSize(0, 25))
        self.HR_ID_BOX.setMaximumSize(QSize(250, 30))
        self.HR_ID_BOX.setAutoFillBackground(False)
        self.HR_ID_BOX.setStyleSheet(u"margin-left:60px;\n"
"border:1px solid;\n"
"border-radius:10px")
        self.HR_ID_BOX.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.HR_ID_BOX.setClearButtonEnabled(False)

        self.verticalLayout_3.addWidget(self.HR_ID_BOX)

        self.password = QLabel(self.contents)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(0, 5))
        self.password.setMaximumSize(QSize(16777215, 30))
        self.password.setFont(font1)
        self.password.setStyleSheet(u"margin-left:56px")

        self.verticalLayout_3.addWidget(self.password)

        self.password_box = QLineEdit(self.contents)
        self.password_box.setObjectName(u"password_box")
        self.password_box.setMaximumSize(QSize(250, 30))
        self.password_box.setStyleSheet(u"margin-left:60px;\n"
"border:1px solid;\n"
"border-radius:10px")
        self.password_box.setEchoMode(QLineEdit.Password)

        self.verticalLayout_3.addWidget(self.password_box)


        self.verticalLayout.addWidget(self.contents)

        self.frame_4 = QFrame(self.sign_in_panel)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.WinPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.login_button = QPushButton(self.frame_4)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(50, 0, 201, 100))
        icon = QIcon()
        icon.addFile(u"D:/AEMS/Images/login_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.login_button.setIcon(icon)
        self.login_button.setIconSize(QSize(1000, 1000))

        self.verticalLayout.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.sign_in_panel)

        self.Image_container = QFrame(Form)
        self.Image_container.setObjectName(u"Image_container")
        self.Image_container.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.Image_container.setFrameShape(QFrame.WinPanel)
        self.Image_container.setFrameShadow(QFrame.Raised)
        self.login_image = QLabel(self.Image_container)
        self.login_image.setObjectName(u"login_image")
        self.login_image.setGeometry(QRect(-10, 0, 661, 781))
        self.login_image.setStyleSheet(u"background-image: url(:/images/Images/login_image.jpg);\n"
"background-opacity:0;")
        self.login_image.setPixmap(QPixmap(u":/images/Images/login_image.jpg"))
        self.login_image.setScaledContents(True)

        self.horizontalLayout.addWidget(self.Image_container)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.image.setText("")
        self.text.setText(QCoreApplication.translate("Form", u"Sign In", None))
        self.HR_ID.setText(QCoreApplication.translate("Form", u"HR ID.", None))
        self.HR_ID_BOX.setPlaceholderText(QCoreApplication.translate("Form", u"    Enter HR ID", None))
        self.password.setText(QCoreApplication.translate("Form", u"Password.", None))
        self.password_box.setPlaceholderText(QCoreApplication.translate("Form", u"    Enter Password", None))
        self.login_button.setText("")
        self.login_image.setText("")
    # retranslateUi

