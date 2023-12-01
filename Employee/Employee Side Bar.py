# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AttendanceliUjHo.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1280, 720)
        Dialog.setMinimumSize(QSize(1280, 720))
        Dialog.setMaximumSize(QSize(1280, 720))
        Dialog.setMouseTracking(True)
        Dialog.setTabletTracking(True)
        Dialog.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.side_bar = QGroupBox(Dialog)
        self.side_bar.setObjectName(u"side_bar")
        self.side_bar.setGeometry(QRect(-1, -1, 350, 722))
        self.side_bar.setMinimumSize(QSize(350, 722))
        self.side_bar.setMaximumSize(QSize(350, 722))
        self.side_bar.setStyleSheet(u"background-color: rgb(50, 82, 110);")
        self.logo = QLabel(self.side_bar)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(0, 20, 341, 191))
        self.logo.setPixmap(QPixmap(u"../Project & Assignments/Semester 5/SDA/AEMS/Images/logo-grey.png"))
        self.logo.setScaledContents(True)
        self.profile = QPushButton(self.side_bar)
        self.profile.setObjectName(u"profile")
        self.profile.setGeometry(QRect(0, 470, 348, 65))
        self.profile.setMinimumSize(QSize(348, 65))
        self.profile.setMaximumSize(QSize(348, 65))
        self.profile.setCursor(QCursor(Qt.PointingHandCursor))
        self.profile.setStyleSheet(u"font: 20pt \"Sitka\" rgb(255, 255, 255);\n"
"color: rgb(230, 230, 230);")
        self.profile_2 = QPushButton(self.side_bar)
        self.profile_2.setObjectName(u"profile_2")
        self.profile_2.setGeometry(QRect(0, 210, 348, 65))
        self.profile_2.setMinimumSize(QSize(348, 65))
        self.profile_2.setMaximumSize(QSize(348, 65))
        self.profile_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.profile_2.setStyleSheet(u"font: 20pt \"Sitka\";\n"
"color: rgb(230, 230, 230);")
        self.profile_5 = QPushButton(self.side_bar)
        self.profile_5.setObjectName(u"profile_5")
        self.profile_5.setGeometry(QRect(0, 405, 348, 65))
        self.profile_5.setMinimumSize(QSize(348, 65))
        self.profile_5.setMaximumSize(QSize(348, 65))
        self.profile_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.profile_5.setStyleSheet(u"font: 20pt \"Sitka\" rgb(255, 255, 255);\n"
"color: rgb(230, 230, 230);")
        self.profile_4 = QPushButton(self.side_bar)
        self.profile_4.setObjectName(u"profile_4")
        self.profile_4.setGeometry(QRect(0, 275, 348, 65))
        self.profile_4.setMinimumSize(QSize(348, 65))
        self.profile_4.setMaximumSize(QSize(348, 65))
        self.profile_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.profile_4.setStyleSheet(u"font: 20pt \"Sitka\" rgb(255, 255, 255);\n"
"color: rgb(230, 230, 230);")
        self.profile_3 = QPushButton(self.side_bar)
        self.profile_3.setObjectName(u"profile_3")
        self.profile_3.setGeometry(QRect(0, 340, 348, 65))
        self.profile_3.setMinimumSize(QSize(348, 65))
        self.profile_3.setMaximumSize(QSize(348, 65))
        self.profile_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.profile_3.setStyleSheet(u"font: 20pt \"Sitka\" rgb(255, 255, 255);\n"
"color: rgb(230, 230, 230);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.side_bar.setTitle("")
        self.logo.setText("")
        self.profile.setText(QCoreApplication.translate("Dialog", u"Leave Application", None))
        self.profile_2.setText(QCoreApplication.translate("Dialog", u"Profile", None))
        self.profile_5.setText(QCoreApplication.translate("Dialog", u"Salary", None))
        self.profile_4.setText(QCoreApplication.translate("Dialog", u"Leave Report", None))
        self.profile_3.setText(QCoreApplication.translate("Dialog", u"Attendance", None))
    # retranslateUi

