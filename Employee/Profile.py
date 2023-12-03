# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProfileTYcClu.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QWidget)

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
        self.sign_out.setIcon(icon)
        self.sign_out.setIconSize(QSize(30, 30))
        self.f_name = QGroupBox(Dialog)
        self.f_name.setObjectName(u"f_name")
        self.f_name.setGeometry(QRect(360, 220, 121, 40))
        self.f_name.setMinimumSize(QSize(0, 40))
        self.f_name.setMaximumSize(QSize(16777215, 40))
        self.f_name.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout = QHBoxLayout(self.f_name)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.address = QGroupBox(Dialog)
        self.address.setObjectName(u"address")
        self.address.setGeometry(QRect(360, 340, 121, 40))
        self.address.setMinimumSize(QSize(0, 40))
        self.address.setMaximumSize(QSize(16777215, 40))
        self.address.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(self.address)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.email = QGroupBox(Dialog)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(360, 280, 121, 40))
        self.email.setMinimumSize(QSize(0, 40))
        self.email.setMaximumSize(QSize(16777215, 40))
        self.email.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.email)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.contact = QGroupBox(Dialog)
        self.contact.setObjectName(u"contact")
        self.contact.setGeometry(QRect(800, 280, 121, 41))
        self.contact.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_4 = QHBoxLayout(self.contact)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.l_name = QGroupBox(Dialog)
        self.l_name.setObjectName(u"l_name")
        self.l_name.setGeometry(QRect(800, 220, 121, 41))
        self.l_name.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_5 = QHBoxLayout(self.l_name)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.department = QGroupBox(Dialog)
        self.department.setObjectName(u"department")
        self.department.setGeometry(QRect(360, 400, 121, 40))
        self.department.setMinimumSize(QSize(0, 40))
        self.department.setMaximumSize(QSize(16777215, 40))
        self.department.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_6 = QHBoxLayout(self.department)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.salary_2 = QGroupBox(Dialog)
        self.salary_2.setObjectName(u"salary_2")
        self.salary_2.setGeometry(QRect(800, 400, 121, 40))
        self.salary_2.setMinimumSize(QSize(0, 40))
        self.salary_2.setMaximumSize(QSize(16777215, 40))
        self.salary_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_7 = QHBoxLayout(self.salary_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.f_name_input = QGroupBox(Dialog)
        self.f_name_input.setObjectName(u"f_name_input")
        self.f_name_input.setGeometry(QRect(480, 220, 320, 40))
        self.f_name_input.setMinimumSize(QSize(320, 40))
        self.f_name_input.setMaximumSize(QSize(290, 40))
        self.f_name_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_8 = QHBoxLayout(self.f_name_input)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.email_input = QGroupBox(Dialog)
        self.email_input.setObjectName(u"email_input")
        self.email_input.setGeometry(QRect(480, 280, 320, 40))
        self.email_input.setMinimumSize(QSize(320, 40))
        self.email_input.setMaximumSize(QSize(320, 40))
        self.email_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_9 = QHBoxLayout(self.email_input)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.address_input = QGroupBox(Dialog)
        self.address_input.setObjectName(u"address_input")
        self.address_input.setGeometry(QRect(480, 340, 750, 40))
        self.address_input.setMinimumSize(QSize(750, 40))
        self.address_input.setMaximumSize(QSize(750, 40))
        self.address_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_10 = QHBoxLayout(self.address_input)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.department_input = QGroupBox(Dialog)
        self.department_input.setObjectName(u"department_input")
        self.department_input.setGeometry(QRect(480, 400, 320, 40))
        self.department_input.setMinimumSize(QSize(320, 40))
        self.department_input.setMaximumSize(QSize(320, 40))
        self.department_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_12 = QHBoxLayout(self.department_input)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.l_name_input = QGroupBox(Dialog)
        self.l_name_input.setObjectName(u"l_name_input")
        self.l_name_input.setGeometry(QRect(920, 220, 300, 40))
        self.l_name_input.setMinimumSize(QSize(300, 40))
        self.l_name_input.setMaximumSize(QSize(300, 40))
        self.l_name_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_14 = QHBoxLayout(self.l_name_input)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.contact_input = QGroupBox(Dialog)
        self.contact_input.setObjectName(u"contact_input")
        self.contact_input.setGeometry(QRect(920, 280, 300, 40))
        self.contact_input.setMinimumSize(QSize(300, 40))
        self.contact_input.setMaximumSize(QSize(300, 40))
        self.contact_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_15 = QHBoxLayout(self.contact_input)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.salary_input = QGroupBox(Dialog)
        self.salary_input.setObjectName(u"salary_input")
        self.salary_input.setGeometry(QRect(920, 400, 300, 40))
        self.salary_input.setMinimumSize(QSize(300, 40))
        self.salary_input.setMaximumSize(QSize(300, 40))
        self.salary_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_16 = QHBoxLayout(self.salary_input)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.present_input = QGroupBox(Dialog)
        self.present_input.setObjectName(u"present_input")
        self.present_input.setGeometry(QRect(720, 570, 100, 40))
        self.present_input.setMinimumSize(QSize(100, 40))
        self.present_input.setMaximumSize(QSize(100, 40))
        self.present_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_37 = QHBoxLayout(self.present_input)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.absent_input = QGroupBox(Dialog)
        self.absent_input.setObjectName(u"absent_input")
        self.absent_input.setGeometry(QRect(480, 630, 100, 40))
        self.absent_input.setMinimumSize(QSize(100, 40))
        self.absent_input.setMaximumSize(QSize(100, 40))
        self.absent_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_38 = QHBoxLayout(self.absent_input)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.total_days = QGroupBox(Dialog)
        self.total_days.setObjectName(u"total_days")
        self.total_days.setGeometry(QRect(360, 570, 121, 40))
        self.total_days.setMinimumSize(QSize(0, 40))
        self.total_days.setMaximumSize(QSize(16777215, 40))
        self.total_days.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_39 = QHBoxLayout(self.total_days)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.leave_input = QGroupBox(Dialog)
        self.leave_input.setObjectName(u"leave_input")
        self.leave_input.setGeometry(QRect(720, 630, 100, 40))
        self.leave_input.setMinimumSize(QSize(100, 40))
        self.leave_input.setMaximumSize(QSize(100, 40))
        self.leave_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_40 = QHBoxLayout(self.leave_input)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.present = QGroupBox(Dialog)
        self.present.setObjectName(u"present")
        self.present.setGeometry(QRect(600, 570, 121, 41))
        self.present.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_41 = QHBoxLayout(self.present)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.absent = QGroupBox(Dialog)
        self.absent.setObjectName(u"absent")
        self.absent.setGeometry(QRect(360, 630, 121, 40))
        self.absent.setMinimumSize(QSize(0, 40))
        self.absent.setMaximumSize(QSize(16777215, 40))
        self.absent.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_42 = QHBoxLayout(self.absent)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.leave = QGroupBox(Dialog)
        self.leave.setObjectName(u"leave")
        self.leave.setGeometry(QRect(600, 630, 121, 41))
        self.leave.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_43 = QHBoxLayout(self.leave)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.total_days_input = QGroupBox(Dialog)
        self.total_days_input.setObjectName(u"total_days_input")
        self.total_days_input.setGeometry(QRect(480, 570, 100, 40))
        self.total_days_input.setMinimumSize(QSize(100, 40))
        self.total_days_input.setMaximumSize(QSize(100, 40))
        self.total_days_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_44 = QHBoxLayout(self.total_days_input)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.pending_applications = QGroupBox(Dialog)
        self.pending_applications.setObjectName(u"pending_applications")
        self.pending_applications.setGeometry(QRect(850, 570, 261, 41))
        self.pending_applications.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_45 = QHBoxLayout(self.pending_applications)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.pending_applications_input = QGroupBox(Dialog)
        self.pending_applications_input.setObjectName(u"pending_applications_input")
        self.pending_applications_input.setGeometry(QRect(1120, 570, 100, 40))
        self.pending_applications_input.setMinimumSize(QSize(100, 40))
        self.pending_applications_input.setMaximumSize(QSize(100, 40))
        self.pending_applications_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_46 = QHBoxLayout(self.pending_applications_input)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.current_deduction = QGroupBox(Dialog)
        self.current_deduction.setObjectName(u"current_deduction")
        self.current_deduction.setGeometry(QRect(850, 630, 261, 41))
        self.current_deduction.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_47 = QHBoxLayout(self.current_deduction)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.current_deduction_input = QGroupBox(Dialog)
        self.current_deduction_input.setObjectName(u"current_deduction_input")
        self.current_deduction_input.setGeometry(QRect(1120, 630, 100, 40))
        self.current_deduction_input.setMinimumSize(QSize(100, 40))
        self.current_deduction_input.setMaximumSize(QSize(100, 40))
        self.current_deduction_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_48 = QHBoxLayout(self.current_deduction_input)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.f_name_2 = QGroupBox(Dialog)
        self.f_name_2.setObjectName(u"f_name_2")
        self.f_name_2.setGeometry(QRect(360, 20, 561, 40))
        self.f_name_2.setMinimumSize(QSize(0, 40))
        self.f_name_2.setMaximumSize(QSize(16777215, 40))
        self.f_name_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 24pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_11 = QHBoxLayout(self.f_name_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.f_name_3 = QGroupBox(Dialog)
        self.f_name_3.setObjectName(u"f_name_3")
        self.f_name_3.setGeometry(QRect(360, 60, 561, 40))
        self.f_name_3.setMinimumSize(QSize(0, 40))
        self.f_name_3.setMaximumSize(QSize(16777215, 40))
        self.f_name_3.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 500 18pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_13 = QHBoxLayout(self.f_name_3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.title = QLabel(Dialog)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(350, 130, 925, 60))
        font = QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: \"#e6e6e6\";")
        self.title_2 = QLabel(Dialog)
        self.title_2.setObjectName(u"title_2")
        self.title_2.setGeometry(QRect(350, 480, 925, 60))
        self.title_2.setFont(font)
        self.title_2.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: \"#e6e6e6\";")

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
        self.f_name.setTitle(QCoreApplication.translate("Dialog", u"First Name", None))
        self.address.setTitle(QCoreApplication.translate("Dialog", u"Address", None))
        self.email.setTitle(QCoreApplication.translate("Dialog", u"Email", None))
        self.contact.setTitle(QCoreApplication.translate("Dialog", u"Contact", None))
        self.l_name.setTitle(QCoreApplication.translate("Dialog", u"Last Name", None))
        self.department.setTitle(QCoreApplication.translate("Dialog", u"Department", None))
        self.salary_2.setTitle(QCoreApplication.translate("Dialog", u"Salary", None))
        self.f_name_input.setTitle(QCoreApplication.translate("Dialog", u"Aatiqa", None))
        self.email_input.setTitle(QCoreApplication.translate("Dialog", u"aatiqahussain@gmail.com", None))
        self.address_input.setTitle(QCoreApplication.translate("Dialog", u"852-B Milaad Street, Faisal Town, Lahore", None))
        self.department_input.setTitle(QCoreApplication.translate("Dialog", u"Accounts", None))
        self.l_name_input.setTitle(QCoreApplication.translate("Dialog", u"Hussain", None))
        self.contact_input.setTitle(QCoreApplication.translate("Dialog", u"0333-8629629", None))
        self.salary_input.setTitle(QCoreApplication.translate("Dialog", u"Rs. 355000", None))
        self.present_input.setTitle(QCoreApplication.translate("Dialog", u"21", None))
        self.absent_input.setTitle(QCoreApplication.translate("Dialog", u"2", None))
        self.total_days.setTitle(QCoreApplication.translate("Dialog", u"Total Days", None))
        self.leave_input.setTitle(QCoreApplication.translate("Dialog", u"1", None))
        self.present.setTitle(QCoreApplication.translate("Dialog", u"Present", None))
        self.absent.setTitle(QCoreApplication.translate("Dialog", u"Absent", None))
        self.leave.setTitle(QCoreApplication.translate("Dialog", u"Leave", None))
        self.total_days_input.setTitle(QCoreApplication.translate("Dialog", u"24", None))
        self.pending_applications.setTitle(QCoreApplication.translate("Dialog", u"Pending Leave Applications", None))
        self.pending_applications_input.setTitle(QCoreApplication.translate("Dialog", u"1", None))
        self.current_deduction.setTitle(QCoreApplication.translate("Dialog", u"Current Salary Deduction", None))
        self.current_deduction_input.setTitle(QCoreApplication.translate("Dialog", u"Rs. 23666", None))
        self.f_name_2.setTitle(QCoreApplication.translate("Dialog", u"Aatiqa Hussain", None))
        self.f_name_3.setTitle(QCoreApplication.translate("Dialog", u"Accounts", None))
        self.title.setText(QCoreApplication.translate("Dialog", u"                                  General Information", None))
        self.title_2.setText(QCoreApplication.translate("Dialog", u"                                Current Month Details", None))
    # retranslateUi

