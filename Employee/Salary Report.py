# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Salary ReportBDaDzS.ui'
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
        self.department_input = QLabel(Dialog)
        self.department_input.setObjectName(u"department_input")
        self.department_input.setGeometry(QRect(580, 180, 500, 30))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.department_input.setFont(font)
        self.department_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";")
        self.name = QLabel(Dialog)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(400, 140, 150, 30))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(16)
        font1.setWeight(QFont.Black)
        font1.setItalic(False)
        self.name.setFont(font1)
        self.name.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 900 16pt \"Segoe UI\";")
        self.title = QLabel(Dialog)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(600, 60, 481, 61))
        font2 = QFont()
        font2.setPointSize(26)
        font2.setBold(True)
        self.title.setFont(font2)
        self.title.setStyleSheet(u"color: rgb(50, 84, 110);")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(400, 180, 150, 30))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 900 16pt \"Segoe UI\";")
        self.name_input = QLabel(Dialog)
        self.name_input.setObjectName(u"name_input")
        self.name_input.setGeometry(QRect(580, 140, 500, 30))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setUnderline(False)
        self.name_input.setFont(font3)
        self.name_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";")
        self.tableWidget = QTableWidget(Dialog)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        brush = QBrush(QColor(230, 230, 230, 255))
        brush.setStyle(Qt.SolidPattern)
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font4);
        __qtablewidgetitem.setBackground(QColor(50, 84, 110));
        __qtablewidgetitem.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font4);
        __qtablewidgetitem1.setBackground(QColor(50, 84, 110));
        __qtablewidgetitem1.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font4);
        __qtablewidgetitem2.setBackground(QColor(50, 84, 110));
        __qtablewidgetitem2.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font4);
        __qtablewidgetitem3.setBackground(QColor(50, 84, 110));
        __qtablewidgetitem3.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignHCenter|Qt.AlignTop);
        __qtablewidgetitem4.setFont(font4);
        __qtablewidgetitem4.setBackground(QColor(50, 84, 110));
        __qtablewidgetitem4.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.tableWidget.rowCount() < 12):
            self.tableWidget.setRowCount(12)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem16)
        font5 = QFont()
        font5.setPointSize(12)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font5);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font5);
        self.tableWidget.setItem(1, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font5);
        self.tableWidget.setItem(2, 0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font5);
        self.tableWidget.setItem(3, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font5);
        self.tableWidget.setItem(4, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font5);
        self.tableWidget.setItem(5, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font5);
        self.tableWidget.setItem(6, 0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font5);
        self.tableWidget.setItem(7, 0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setFont(font5);
        self.tableWidget.setItem(8, 0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setFont(font5);
        self.tableWidget.setItem(9, 0, __qtablewidgetitem26)
        font6 = QFont()
        font6.setPointSize(13)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setFont(font6);
        self.tableWidget.setItem(10, 0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setFont(font5);
        self.tableWidget.setItem(11, 0, __qtablewidgetitem28)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(390, 240, 841, 401))
        self.tableWidget.setStyleSheet(u"QHeaderView::section {\n"
"    background-color: rgb(50, 84, 110); /* Set your desired background color */\n"
"    color: rgb(230, 230, 230); /* Set the text color */\n"
"};\n"
"color: rgb(50, 84, 110);\n"
"background-color: rgb(230, 230, 230);\n"
"\n"
"\n"
"\n"
"")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(162)

        self.retranslateUi(Dialog)

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
        self.department_input.setText(QCoreApplication.translate("Dialog", u"Accounts", None))
        self.name.setText(QCoreApplication.translate("Dialog", u"Name :", None))
        self.title.setText(QCoreApplication.translate("Dialog", u"Annual Salary Report", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Department :", None))
        self.name_input.setText(QCoreApplication.translate("Dialog", u"Aatiqa Hussain", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Months", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Issuance Date", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Deduction", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Salary", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Total Wage", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"1.", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"2.", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", u"3.", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Dialog", u"4.", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Dialog", u"5.", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Dialog", u"6.", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Dialog", u"7.", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Dialog", u"8.", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Dialog", u"9.", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Dialog", u"10.", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Dialog", u"11.", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Dialog", u"12.", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem17 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Dialog", u"January", None));
        ___qtablewidgetitem18 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Dialog", u"Febuary", None));
        ___qtablewidgetitem19 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Dialog", u"March", None));
        ___qtablewidgetitem20 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Dialog", u"April", None));
        ___qtablewidgetitem21 = self.tableWidget.item(4, 0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Dialog", u"May", None));
        ___qtablewidgetitem22 = self.tableWidget.item(5, 0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Dialog", u"June", None));
        ___qtablewidgetitem23 = self.tableWidget.item(6, 0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Dialog", u"July", None));
        ___qtablewidgetitem24 = self.tableWidget.item(7, 0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Dialog", u"August", None));
        ___qtablewidgetitem25 = self.tableWidget.item(8, 0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Dialog", u"September", None));
        ___qtablewidgetitem26 = self.tableWidget.item(9, 0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("Dialog", u"October", None));
        ___qtablewidgetitem27 = self.tableWidget.item(10, 0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("Dialog", u"November", None));
        ___qtablewidgetitem28 = self.tableWidget.item(11, 0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("Dialog", u"December", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi

