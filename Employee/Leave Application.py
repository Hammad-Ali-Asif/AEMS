# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Leave ApplicationqqQpSv.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QGroupBox, QLabel, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_leave_application_form(object):
    def setupUi(self, leave_application_form):
        if not leave_application_form.objectName():
            leave_application_form.setObjectName(u"leave_application_form")
        leave_application_form.resize(1280, 720)
        leave_application_form.setMinimumSize(QSize(1280, 720))
        leave_application_form.setMaximumSize(QSize(1280, 720))
        leave_application_form.setMouseTracking(True)
        leave_application_form.setTabletTracking(True)
        leave_application_form.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.side_bar = QGroupBox(leave_application_form)
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
        self.sign_out.setIcon(icon)
        self.sign_out.setIconSize(QSize(30, 30))
        self.start_date = QLabel(leave_application_form)
        self.start_date.setObjectName(u"start_date")
        self.start_date.setGeometry(QRect(400, 160, 131, 31))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        self.start_date.setFont(font)
        self.start_date.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 18pt \"Segoe UI\";")
        self.submit_button = QPushButton(leave_application_form)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setGeometry(QRect(770, 610, 131, 51))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        self.submit_button.setFont(font1)
        self.submit_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.submit_button.setStyleSheet(u"border:2px solid;\n"
"border-radius:20px;\n"
"background-color:rgb(50, 84, 110);\n"
"border-color: rgb(230, 230, 230);\n"
"color: rgb(230, 230, 230);\n"
"font: 700 12pt \"Segoe UI\";")
        self.end_date = QLabel(leave_application_form)
        self.end_date.setObjectName(u"end_date")
        self.end_date.setGeometry(QRect(820, 160, 131, 31))
        self.end_date.setFont(font)
        self.end_date.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 18pt \"Segoe UI\";")
        self.description = QLabel(leave_application_form)
        self.description.setObjectName(u"description")
        self.description.setGeometry(QRect(400, 300, 161, 31))
        self.description.setFont(font)
        self.description.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 18pt \"Segoe UI\";")
        self.category_input = QComboBox(leave_application_form)
        self.category_input.addItem("")
        self.category_input.addItem("")
        self.category_input.setObjectName(u"category_input")
        self.category_input.setGeometry(QRect(610, 230, 151, 31))
        self.category_input.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.start_date_input = QDateEdit(leave_application_form)
        self.start_date_input.setObjectName(u"start_date_input")
        self.start_date_input.setGeometry(QRect(610, 160, 151, 31))
        self.start_date_input.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.description_input = QTextEdit(leave_application_form)
        self.description_input.setObjectName(u"description_input")
        self.description_input.setGeometry(QRect(410, 390, 821, 201))
        self.category = QLabel(leave_application_form)
        self.category.setObjectName(u"category")
        self.category.setGeometry(QRect(400, 220, 141, 41))
        self.category.setFont(font)
        self.category.setStyleSheet(u"font: 700 18pt \"Segoe UI\";\n"
"color: rgb(50, 84, 110);")
        self.exp = QLabel(leave_application_form)
        self.exp.setObjectName(u"exp")
        self.exp.setGeometry(QRect(400, 340, 501, 21))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.exp.setFont(font2)
        self.exp.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 12pt \"Segoe UI\";")
        self.end_date_input = QDateEdit(leave_application_form)
        self.end_date_input.setObjectName(u"end_date_input")
        self.end_date_input.setGeometry(QRect(990, 160, 151, 31))
        self.end_date_input.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.application = QTextEdit(leave_application_form)
        self.application.setObjectName(u"application")
        self.application.setGeometry(QRect(348, 1, 930, 85))
        self.application.setMinimumSize(QSize(930, 85))
        self.application.setMaximumSize(QSize(930, 85))
        self.application.setStyleSheet(u"color: rgb(230, 230, 230);\n"
"background-color: rgb(50, 84, 110);")

        self.retranslateUi(leave_application_form)

        QMetaObject.connectSlotsByName(leave_application_form)
    # setupUi

    def retranslateUi(self, leave_application_form):
        leave_application_form.setWindowTitle(QCoreApplication.translate("leave_application_form", u"Dialog", None))
        self.side_bar.setTitle("")
        self.logo.setText("")
        self.profile.setText(QCoreApplication.translate("leave_application_form", u"Leave Application", None))
        self.leave_report.setText(QCoreApplication.translate("leave_application_form", u"Profile", None))
        self.leave_application.setText(QCoreApplication.translate("leave_application_form", u"Salary", None))
        self.salary.setText(QCoreApplication.translate("leave_application_form", u"Leave Report", None))
        self.attendance.setText(QCoreApplication.translate("leave_application_form", u"Attendance", None))
        self.sign_out.setText(QCoreApplication.translate("leave_application_form", u"  Sign Out ", None))
        self.start_date.setText(QCoreApplication.translate("leave_application_form", u"Start Date", None))
        self.submit_button.setText(QCoreApplication.translate("leave_application_form", u"SUBMIT", None))
        self.end_date.setText(QCoreApplication.translate("leave_application_form", u"End Date", None))
        self.description.setText(QCoreApplication.translate("leave_application_form", u"Description", None))
        self.category_input.setItemText(0, QCoreApplication.translate("leave_application_form", u"General", None))
        self.category_input.setItemText(1, QCoreApplication.translate("leave_application_form", u"Health", None))

        self.category.setText(QCoreApplication.translate("leave_application_form", u"Category", None))
        self.exp.setText(QCoreApplication.translate("leave_application_form", u"(Explain reason for leave in 2-5 lines.)", None))
        self.application.setHtml(QCoreApplication.translate("leave_application_form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt;\">APPLICATION FORM</span></p></body></html>", None))
    # retranslateUi

