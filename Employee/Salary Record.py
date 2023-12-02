# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Salary RecordUGUJfV.ui'
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
        self.salary_record_heading = QLabel(Dialog)
        self.salary_record_heading.setObjectName(u"salary_record_heading")
        self.salary_record_heading.setGeometry(QRect(350, 50, 925, 81))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.salary_record_heading.setFont(font)
        self.salary_record_heading.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: rgb(230, 230, 230);")
        self.salaryrecord = QTableWidget(Dialog)
        if (self.salaryrecord.columnCount() < 6):
            self.salaryrecord.setColumnCount(6)
        brush = QBrush(QColor(230, 230, 230, 255))
        brush.setStyle(Qt.SolidPattern)
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        __qtablewidgetitem.setBackground(QColor(50, 84, 110));
        __qtablewidgetitem.setForeground(brush);
        self.salaryrecord.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        __qtablewidgetitem1.setBackground(QColor(50, 84, 110));
        __qtablewidgetitem1.setForeground(brush);
        self.salaryrecord.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        __qtablewidgetitem2.setBackground(QColor(50, 84, 110));
        __qtablewidgetitem2.setForeground(brush);
        self.salaryrecord.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        brush1 = QBrush(QColor(230, 230, 230, 255))
        brush1.setStyle(Qt.NoBrush)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        __qtablewidgetitem3.setBackground(QColor(50, 84, 110));
        __qtablewidgetitem3.setForeground(brush1);
        self.salaryrecord.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        brush2 = QBrush(QColor(230, 230, 230, 255))
        brush2.setStyle(Qt.NoBrush)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        __qtablewidgetitem4.setBackground(QColor(50, 84, 110, 251));
        __qtablewidgetitem4.setForeground(brush2);
        self.salaryrecord.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        brush3 = QBrush(QColor(230, 230, 230, 255))
        brush3.setStyle(Qt.NoBrush)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        __qtablewidgetitem5.setBackground(QColor(50, 84, 110));
        __qtablewidgetitem5.setForeground(brush3);
        self.salaryrecord.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.salaryrecord.rowCount() < 12):
            self.salaryrecord.setRowCount(12)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.salaryrecord.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.salaryrecord.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.salaryrecord.setItem(0, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.salaryrecord.setItem(0, 3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.salaryrecord.setItem(0, 4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.salaryrecord.setItem(0, 5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.salaryrecord.setItem(1, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.salaryrecord.setItem(2, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.salaryrecord.setItem(3, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.salaryrecord.setItem(4, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.salaryrecord.setItem(5, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.salaryrecord.setItem(6, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.salaryrecord.setItem(7, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.salaryrecord.setItem(8, 0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.salaryrecord.setItem(9, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.salaryrecord.setItem(10, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.salaryrecord.setItem(11, 0, __qtablewidgetitem22)
        self.salaryrecord.setObjectName(u"salaryrecord")
        self.salaryrecord.setGeometry(QRect(350, 170, 931, 411))
        self.salaryrecord.setMinimumSize(QSize(931, 0))
        self.salaryrecord.setMaximumSize(QSize(16777215, 501))
        self.salaryrecord.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"background-color: rgb(230, 230, 230);\n"
"color: rgb(50, 84, 110);")
        self.salaryrecord.horizontalHeader().setDefaultSectionSize(150)

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
        self.salary_record_heading.setText(QCoreApplication.translate("Dialog", u"                                   Past Year Salary Record", None))
        ___qtablewidgetitem = self.salaryrecord.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Month", None));
        ___qtablewidgetitem1 = self.salaryrecord.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Issuance Date", None));
        ___qtablewidgetitem2 = self.salaryrecord.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Amount", None));
        ___qtablewidgetitem3 = self.salaryrecord.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Deduction", None));
        ___qtablewidgetitem4 = self.salaryrecord.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Total", None));
        ___qtablewidgetitem5 = self.salaryrecord.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"Details", None));

        __sortingEnabled = self.salaryrecord.isSortingEnabled()
        self.salaryrecord.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.salaryrecord.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"January", None));
        ___qtablewidgetitem7 = self.salaryrecord.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", u"05/02/2023", None));
        ___qtablewidgetitem8 = self.salaryrecord.item(0, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Dialog", u"Rs. 354000", None));
        ___qtablewidgetitem9 = self.salaryrecord.item(0, 3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Dialog", u"Rs. 4000", None));
        ___qtablewidgetitem10 = self.salaryrecord.item(0, 4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Dialog", u"Rs. 350000", None));
        ___qtablewidgetitem11 = self.salaryrecord.item(0, 5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Dialog", u"Details", None));
        ___qtablewidgetitem12 = self.salaryrecord.item(1, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Dialog", u"February", None));
        ___qtablewidgetitem13 = self.salaryrecord.item(2, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Dialog", u"March", None));
        ___qtablewidgetitem14 = self.salaryrecord.item(3, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Dialog", u"April", None));
        ___qtablewidgetitem15 = self.salaryrecord.item(4, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Dialog", u"May", None));
        ___qtablewidgetitem16 = self.salaryrecord.item(5, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Dialog", u"June", None));
        ___qtablewidgetitem17 = self.salaryrecord.item(6, 0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Dialog", u"July", None));
        ___qtablewidgetitem18 = self.salaryrecord.item(7, 0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Dialog", u"August", None));
        ___qtablewidgetitem19 = self.salaryrecord.item(8, 0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Dialog", u"September", None));
        ___qtablewidgetitem20 = self.salaryrecord.item(9, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Dialog", u"October", None));
        ___qtablewidgetitem21 = self.salaryrecord.item(10, 0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Dialog", u"November", None));
        ___qtablewidgetitem22 = self.salaryrecord.item(11, 0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Dialog", u"December", None));
        self.salaryrecord.setSortingEnabled(__sortingEnabled)

#if QT_CONFIG(whatsthis)
        self.salaryrecord.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
    # retranslateUi

