# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Leave ReportZDqzRf.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

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
        self.logo.setPixmap(QPixmap(u"../Images/logo-grey.png"))
        self.logo.setScaledContents(True)
        self.profile = QPushButton(self.side_bar)
        self.profile.setObjectName(u"profile")
        self.profile.setGeometry(QRect(0, 470, 348, 65))
        self.profile.setMinimumSize(QSize(348, 65))
        self.profile.setMaximumSize(QSize(348, 65))
        self.profile.setCursor(QCursor(Qt.PointingHandCursor))
        self.profile.setStyleSheet(u"font: 20pt \"Sitka\" rgb(255, 255, 255);\n"
"color: rgb(230, 230, 230);")
        self.leave_report = QPushButton(self.side_bar)
        self.leave_report.setObjectName(u"leave_report")
        self.leave_report.setGeometry(QRect(0, 210, 348, 65))
        self.leave_report.setMinimumSize(QSize(348, 65))
        self.leave_report.setMaximumSize(QSize(348, 65))
        self.leave_report.setCursor(QCursor(Qt.PointingHandCursor))
        self.leave_report.setStyleSheet(u"font: 20pt \"Sitka\";\n"
"color: rgb(230, 230, 230);")
        self.leave_application = QPushButton(self.side_bar)
        self.leave_application.setObjectName(u"leave_application")
        self.leave_application.setGeometry(QRect(0, 405, 348, 65))
        self.leave_application.setMinimumSize(QSize(348, 65))
        self.leave_application.setMaximumSize(QSize(348, 65))
        self.leave_application.setCursor(QCursor(Qt.PointingHandCursor))
        self.leave_application.setStyleSheet(u"font: 20pt \"Sitka\" rgb(255, 255, 255);\n"
"color: rgb(230, 230, 230);")
        self.salary = QPushButton(self.side_bar)
        self.salary.setObjectName(u"salary")
        self.salary.setGeometry(QRect(0, 275, 348, 65))
        self.salary.setMinimumSize(QSize(348, 65))
        self.salary.setMaximumSize(QSize(348, 65))
        self.salary.setCursor(QCursor(Qt.PointingHandCursor))
        self.salary.setStyleSheet(u"font: 20pt \"Sitka\" rgb(255, 255, 255);\n"
"color: rgb(230, 230, 230);")
        self.attendance = QPushButton(self.side_bar)
        self.attendance.setObjectName(u"attendance")
        self.attendance.setGeometry(QRect(0, 340, 348, 65))
        self.attendance.setMinimumSize(QSize(348, 65))
        self.attendance.setMaximumSize(QSize(348, 65))
        self.attendance.setCursor(QCursor(Qt.PointingHandCursor))
        self.attendance.setStyleSheet(u"font: 20pt \"Sitka\" rgb(255, 255, 255);\n"
"color: rgb(230, 230, 230);")
        self.sign_out = QPushButton(self.side_bar)
        self.sign_out.setObjectName(u"sign_out")
        self.sign_out.setGeometry(QRect(0, 660, 348, 65))
        self.sign_out.setMinimumSize(QSize(348, 65))
        self.sign_out.setMaximumSize(QSize(348, 65))
        self.sign_out.setCursor(QCursor(Qt.PointingHandCursor))
        self.sign_out.setStyleSheet(u"font: italic 18pt \"Sitka\" rgb(255, 255, 255);\n"
"color: rgb(230, 230, 230);")
        icon = QIcon()
        icon.addFile(u"../Images/sign out-grey.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u"../Images/sign out-grey.png", QSize(), QIcon.Normal, QIcon.On)
        self.sign_out.setIcon(icon)
        self.sign_out.setIconSize(QSize(30, 30))
        self.title = QLabel(Dialog)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(350, 30, 925, 60))
        font = QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: \"#e6e6e6\";")
        self.remaing = QLabel(Dialog)
        self.remaing.setObjectName(u"remaing")
        self.remaing.setGeometry(QRect(620, 160, 120, 41))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(16)
        font1.setWeight(QFont.Black)
        font1.setItalic(False)
        self.remaing.setFont(font1)
        self.remaing.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 900 16pt \"Segoe UI\";")
        self.leave_record = QTableWidget(Dialog)
        if (self.leave_record.columnCount() < 3):
            self.leave_record.setColumnCount(3)
        brush = QBrush(QColor(85, 55, 89, 255))
        brush.setStyle(Qt.SolidPattern)
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        __qtablewidgetitem.setBackground(QColor(85, 55, 89));
        __qtablewidgetitem.setForeground(brush);
        self.leave_record.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        __qtablewidgetitem1.setBackground(QColor(85, 55, 89));
        __qtablewidgetitem1.setForeground(brush);
        self.leave_record.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        __qtablewidgetitem2.setBackground(QColor(85, 55, 89));
        __qtablewidgetitem2.setForeground(brush);
        self.leave_record.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.leave_record.setObjectName(u"leave_record")
        self.leave_record.setGeometry(QRect(450, 220, 721, 461))
        self.leave_record.setStyleSheet(u"QHeaderView::section {\n"
"    background-color: rgb(50, 84, 110); /* Set your desired background color */\n"
"    color: rgb(230, 230, 230); /* Set the text color */\n"
"}\n"
"\n"
"\n"
"color: rgb(50, 84, 110);\n"
"background-color: rgb(230, 230, 230);")
        self.leave_record.horizontalHeader().setDefaultSectionSize(237)
        self.total = QLabel(Dialog)
        self.total.setObjectName(u"total")
        self.total.setGeometry(QRect(640, 130, 120, 40))
        self.total.setFont(font1)
        self.total.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 900 16pt \"Segoe UI\";")
        self.remaining_general = QLabel(Dialog)
        self.remaining_general.setObjectName(u"remaining_general")
        self.remaining_general.setGeometry(QRect(800, 160, 30, 41))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(16)
        font3.setWeight(QFont.DemiBold)
        font3.setItalic(False)
        self.remaining_general.setFont(font3)
        self.remaining_general.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"\n"
"font: 600 16pt \"Segoe UI\";")
        self.general = QLabel(Dialog)
        self.general.setObjectName(u"general")
        self.general.setGeometry(QRect(770, 100, 100, 40))
        self.general.setFont(font1)
        self.general.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 900 16pt \"Segoe UI\";")
        self.total_general = QLabel(Dialog)
        self.total_general.setObjectName(u"total_general")
        self.total_general.setGeometry(QRect(800, 130, 30, 40))
        self.total_general.setFont(font3)
        self.total_general.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 600 16pt \"Segoe UI\";")
        self.remaining_health = QLabel(Dialog)
        self.remaining_health.setObjectName(u"remaining_health")
        self.remaining_health.setGeometry(QRect(920, 160, 30, 41))
        self.remaining_health.setFont(font3)
        self.remaining_health.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"\n"
"font: 600 16pt \"Segoe UI\";")
        self.health = QLabel(Dialog)
        self.health.setObjectName(u"health")
        self.health.setGeometry(QRect(900, 100, 100, 40))
        self.health.setFont(font1)
        self.health.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 900 16pt \"Segoe UI\";")
        self.total_health = QLabel(Dialog)
        self.total_health.setObjectName(u"total_health")
        self.total_health.setGeometry(QRect(920, 130, 30, 40))
        self.total_health.setFont(font3)
        self.total_health.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 600 16pt \"Segoe UI\";")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.side_bar.setTitle("")
        self.logo.setText("")
        self.profile.setText(QCoreApplication.translate("Dialog", u"Leave Application", None))
        self.leave_report.setText(QCoreApplication.translate("Dialog", u"Profile", None))
        self.leave_application.setText(QCoreApplication.translate("Dialog", u" Salary", None))
        self.salary.setText(QCoreApplication.translate("Dialog", u"Leave Report", None))
        self.attendance.setText(QCoreApplication.translate("Dialog", u"Attendance", None))
        self.sign_out.setText(QCoreApplication.translate("Dialog", u"  Sign Out ", None))
        self.title.setText(QCoreApplication.translate("Dialog", u"                                         Leave Report", None))
        self.remaing.setText(QCoreApplication.translate("Dialog", u"Remaining", None))
        ___qtablewidgetitem = self.leave_record.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Date", None));
        ___qtablewidgetitem1 = self.leave_record.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Type", None));
        ___qtablewidgetitem2 = self.leave_record.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Status", None));
        self.total.setText(QCoreApplication.translate("Dialog", u"Total", None))
        self.remaining_general.setText(QCoreApplication.translate("Dialog", u"8", None))
        self.general.setText(QCoreApplication.translate("Dialog", u"General", None))
        self.total_general.setText(QCoreApplication.translate("Dialog", u"10", None))
        self.remaining_health.setText(QCoreApplication.translate("Dialog", u"15", None))
        self.health.setText(QCoreApplication.translate("Dialog", u"Health", None))
        self.total_health.setText(QCoreApplication.translate("Dialog", u"15", None))
    # retranslateUi

