# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AttendancencRtUh.ui'
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
    QLabel, QPushButton, QSizePolicy, QStackedWidget,
    QTableWidget, QTableWidgetItem, QWidget)

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
        icon.addFile(u"../Project & Assignments/Semester 5/SDA/AEMS/Images/sign out-grey.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u"../Project & Assignments/Semester 5/SDA/AEMS/Images/sign out-grey.png", QSize(), QIcon.Normal, QIcon.On)
        self.sign_out.setIcon(icon)
        self.sign_out.setIconSize(QSize(30, 30))
        self.march = QPushButton(Dialog)
        self.march.setObjectName(u"march")
        self.march.setGeometry(QRect(820, 120, 90, 30))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.march.setFont(font)
        self.march.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: rgb(230, 230, 230);\n"
"border:1px solid;\n"
"border-radius: 10px\n"
"")
        self.oct = QPushButton(Dialog)
        self.oct.setObjectName(u"oct")
        self.oct.setGeometry(QRect(970, 160, 90, 30))
        self.oct.setFont(font)
        self.oct.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: rgb(230, 230, 230);\n"
"border:1px solid;\n"
"border-radius: 10px")
        self.may = QPushButton(Dialog)
        self.may.setObjectName(u"may")
        self.may.setGeometry(QRect(1020, 120, 90, 30))
        self.may.setFont(font)
        self.may.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: rgb(230, 230, 230);\n"
"border:1px solid;\n"
"border-radius: 10px")
        self.stackedWidget = QStackedWidget(Dialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(380, 220, 741, 481))
        self.stackedWidget.setStyleSheet(u"QHeaderView::section {\n"
"    background-color: rgb(50, 84, 110); /* Set your desired background color */\n"
"    color: rgb(230, 230, 230); /* Set the text color */\n"
"};\n"
"background-color: rgb(230, 230, 230);\n"
"color: rgb(50, 84, 110);")
        self.first_page = QWidget()
        self.first_page.setObjectName(u"first_page")
        self.table_start = QTableWidget(self.first_page)
        if (self.table_start.columnCount() < 2):
            self.table_start.setColumnCount(2)
        brush = QBrush(QColor(50, 84, 110, 255))
        brush.setStyle(Qt.SolidPattern)
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        __qtablewidgetitem.setBackground(QColor(85, 55, 89));
        __qtablewidgetitem.setForeground(brush);
        self.table_start.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        __qtablewidgetitem1.setBackground(QColor(85, 55, 89));
        __qtablewidgetitem1.setForeground(brush);
        self.table_start.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.table_start.setObjectName(u"table_start")
        self.table_start.setGeometry(QRect(110, 30, 621, 441))
        self.table_start.setStyleSheet(u"background-color: rgb(230, 230, 230);\n"
"color: rgb(50, 84, 110);\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(50, 84, 110); /* Set your desired background color */\n"
"    color: rgb(230, 230, 230); /* Set the text color */\n"
"};")
        self.table_start.horizontalHeader().setMinimumSectionSize(96)
        self.table_start.horizontalHeader().setDefaultSectionSize(305)
        self.stackedWidget.addWidget(self.first_page)
        self.second_page = QWidget()
        self.second_page.setObjectName(u"second_page")
        self.table_end = QTableWidget(self.second_page)
        if (self.table_end.columnCount() < 2):
            self.table_end.setColumnCount(2)
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setKerning(True)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        __qtablewidgetitem2.setBackground(QColor(230, 230, 230, 10));
        __qtablewidgetitem2.setForeground(brush);
        self.table_end.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        __qtablewidgetitem3.setBackground(QColor(230, 230, 230));
        __qtablewidgetitem3.setForeground(brush);
        self.table_end.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.table_end.setObjectName(u"table_end")
        self.table_end.setGeometry(QRect(110, 30, 621, 441))
        self.table_end.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.table_end.horizontalHeader().setDefaultSectionSize(305)
        self.stackedWidget.addWidget(self.second_page)
        self.april = QPushButton(Dialog)
        self.april.setObjectName(u"april")
        self.april.setGeometry(QRect(920, 120, 90, 30))
        self.april.setFont(font)
        self.april.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: rgb(230, 230, 230);\n"
"border:1px solid;\n"
"border-radius: 10px")
        self.aug = QPushButton(Dialog)
        self.aug.setObjectName(u"aug")
        self.aug.setGeometry(QRect(770, 160, 90, 30))
        self.aug.setFont(font)
        self.aug.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: rgb(230, 230, 230);\n"
"border:1px solid;\n"
"border-radius: 10px")
        self.sep = QPushButton(Dialog)
        self.sep.setObjectName(u"sep")
        self.sep.setGeometry(QRect(869, 160, 92, 30))
        self.sep.setFont(font)
        self.sep.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: rgb(230, 230, 230);\n"
"border:1px solid;\n"
"border-radius: 10px")
        self.feb = QPushButton(Dialog)
        self.feb.setObjectName(u"feb")
        self.feb.setGeometry(QRect(720, 120, 90, 30))
        self.feb.setFont(font)
        self.feb.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: rgb(230, 230, 230);\n"
"border:1px solid;\n"
"border-radius: 10px")
        self.jan = QPushButton(Dialog)
        self.jan.setObjectName(u"jan")
        self.jan.setGeometry(QRect(620, 120, 90, 30))
        self.jan.setFont(font)
        self.jan.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: rgb(230, 230, 230);\n"
"border:1px solid;\n"
"border-radius: 10px")
        self.nov = QPushButton(Dialog)
        self.nov.setObjectName(u"nov")
        self.nov.setGeometry(QRect(1070, 160, 90, 30))
        self.nov.setFont(font)
        self.nov.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: rgb(230, 230, 230);\n"
"border:1px solid;\n"
"border-radius: 10px")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(350, 20, 915, 65))
        font3 = QFont()
        font3.setPointSize(25)
        font3.setBold(True)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        font3.setKerning(True)
        self.label.setFont(font3)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"background-color: rgb(50, 84, 110);")
        self.july = QPushButton(Dialog)
        self.july.setObjectName(u"july")
        self.july.setGeometry(QRect(670, 160, 90, 30))
        self.july.setFont(font)
        self.july.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: rgb(230, 230, 230);\n"
"border:1px solid;\n"
"border-radius: 10px")
        self.june = QPushButton(Dialog)
        self.june.setObjectName(u"june")
        self.june.setGeometry(QRect(1120, 120, 90, 30))
        self.june.setFont(font)
        self.june.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: rgb(230, 230, 230);\n"
"border:1px solid;\n"
"border-radius: 10px\n"
"")
        self.dec = QPushButton(Dialog)
        self.dec.setObjectName(u"dec")
        self.dec.setGeometry(QRect(1170, 160, 90, 30))
        self.dec.setFont(font)
        self.dec.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: rgb(230, 230, 230);\n"
"border:1px solid;\n"
"border-radius: 10px")

        self.retranslateUi(Dialog)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.side_bar.setTitle("")
        self.logo.setText("")
        self.profile.setText(QCoreApplication.translate("Dialog", u"Leave Application", None))
        self.leave_report.setText(QCoreApplication.translate("Dialog", u"Profile", None))
        self.leave_application.setText(QCoreApplication.translate("Dialog", u"Salary", None))
        self.salary.setText(QCoreApplication.translate("Dialog", u"Leave Report", None))
        self.attendance.setText(QCoreApplication.translate("Dialog", u"Attendance", None))
        self.sign_out.setText(QCoreApplication.translate("Dialog", u"  Sign Out ", None))
        self.march.setText(QCoreApplication.translate("Dialog", u"March", None))
        self.oct.setText(QCoreApplication.translate("Dialog", u"October", None))
        self.may.setText(QCoreApplication.translate("Dialog", u"May", None))
        ___qtablewidgetitem = self.table_start.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Date", None));
        ___qtablewidgetitem1 = self.table_start.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Status", None));
        ___qtablewidgetitem2 = self.table_end.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Date", None));
        ___qtablewidgetitem3 = self.table_end.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Status", None));
        self.april.setText(QCoreApplication.translate("Dialog", u"April", None))
        self.aug.setText(QCoreApplication.translate("Dialog", u"August", None))
        self.sep.setText(QCoreApplication.translate("Dialog", u"September", None))
        self.feb.setText(QCoreApplication.translate("Dialog", u"February", None))
        self.jan.setText(QCoreApplication.translate("Dialog", u"January", None))
        self.nov.setText(QCoreApplication.translate("Dialog", u"November", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" color:#e6e6e6;\">Employee Attendance</span></p></body></html>", None))
        self.july.setText(QCoreApplication.translate("Dialog", u"July", None))
        self.june.setText(QCoreApplication.translate("Dialog", u"June", None))
        self.dec.setText(QCoreApplication.translate("Dialog", u"December", None))
    # retranslateUi

