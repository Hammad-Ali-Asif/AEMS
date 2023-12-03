# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Employee_page.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QWidget)

class Ui_Employee_Page(object):
    def setupUi(self, Employee_Page):
        if not Employee_Page.objectName():
            Employee_Page.setObjectName(u"Employee_Page")
        Employee_Page.resize(1280, 720)
        Employee_Page.setMinimumSize(QSize(1280, 720))
        Employee_Page.setSizeIncrement(QSize(1280, 720))
        self.Page = QWidget(Employee_Page)
        self.Page.setObjectName(u"Page")
        self.Page.setMinimumSize(QSize(1280, 720))
        self.Page.setMaximumSize(QSize(1280, 720))
        self.side_bar = QGroupBox(self.Page)
        self.side_bar.setObjectName(u"side_bar")
        self.side_bar.setGeometry(QRect(0, 0, 350, 722))
        self.side_bar.setMinimumSize(QSize(350, 722))
        self.side_bar.setMaximumSize(QSize(350, 722))
        self.side_bar.setStyleSheet(u"background-color: rgb(50, 82, 110);")
        self.logo_2 = QLabel(self.side_bar)
        self.logo_2.setObjectName(u"logo_2")
        self.logo_2.setGeometry(QRect(0, 20, 341, 191))
        self.logo_2.setPixmap(QPixmap(u"Images/logo-grey.png"))
        self.logo_2.setScaledContents(True)
        self.profile_2 = QPushButton(self.side_bar)
        self.profile_2.setObjectName(u"profile_2")
        self.profile_2.setGeometry(QRect(0, 470, 348, 65))
        self.profile_2.setMinimumSize(QSize(348, 65))
        self.profile_2.setMaximumSize(QSize(348, 65))
        self.profile_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.profile_2.setStyleSheet(u"font: 20pt \"Sitka\" rgb(255, 255, 255);\n"
"color: rgb(230, 230, 230);")
        self.leave_report_2 = QPushButton(self.side_bar)
        self.leave_report_2.setObjectName(u"leave_report_2")
        self.leave_report_2.setGeometry(QRect(0, 210, 348, 65))
        self.leave_report_2.setMinimumSize(QSize(348, 65))
        self.leave_report_2.setMaximumSize(QSize(348, 65))
        self.leave_report_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.leave_report_2.setStyleSheet(u"font: 20pt \"Sitka\";\n"
"color: rgb(230, 230, 230);")
        self.leave_application_2 = QPushButton(self.side_bar)
        self.leave_application_2.setObjectName(u"leave_application_2")
        self.leave_application_2.setGeometry(QRect(0, 405, 348, 65))
        self.leave_application_2.setMinimumSize(QSize(348, 65))
        self.leave_application_2.setMaximumSize(QSize(348, 65))
        self.leave_application_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.leave_application_2.setStyleSheet(u"font: 20pt \"Sitka\" rgb(255, 255, 255);\n"
"color: rgb(230, 230, 230);")
        self.salary_3 = QPushButton(self.side_bar)
        self.salary_3.setObjectName(u"salary_3")
        self.salary_3.setGeometry(QRect(0, 275, 348, 65))
        self.salary_3.setMinimumSize(QSize(348, 65))
        self.salary_3.setMaximumSize(QSize(348, 65))
        self.salary_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.salary_3.setStyleSheet(u"font: 20pt \"Sitka\" rgb(255, 255, 255);\n"
"color: rgb(230, 230, 230);")
        self.attendance_2 = QPushButton(self.side_bar)
        self.attendance_2.setObjectName(u"attendance_2")
        self.attendance_2.setGeometry(QRect(0, 340, 348, 65))
        self.attendance_2.setMinimumSize(QSize(348, 65))
        self.attendance_2.setMaximumSize(QSize(348, 65))
        self.attendance_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.attendance_2.setStyleSheet(u"font: 20pt \"Sitka\" rgb(255, 255, 255);\n"
"color: rgb(230, 230, 230);")
        self.sign_out_2 = QPushButton(self.side_bar)
        self.sign_out_2.setObjectName(u"sign_out_2")
        self.sign_out_2.setGeometry(QRect(0, 660, 348, 65))
        self.sign_out_2.setMinimumSize(QSize(348, 65))
        self.sign_out_2.setMaximumSize(QSize(348, 65))
        self.sign_out_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.sign_out_2.setStyleSheet(u"font: italic 18pt \"Sitka\" rgb(255, 255, 255);\n"
"color: rgb(230, 230, 230);")
        icon = QIcon()
        icon.addFile(u"Images/sign out-grey.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u"Images/sign out-grey.png", QSize(), QIcon.Normal, QIcon.On)
        self.sign_out_2.setIcon(icon)
        self.sign_out_2.setIconSize(QSize(30, 30))
        self.Pages = QStackedWidget(self.Page)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setGeometry(QRect(350, 0, 930, 720))
        self.Profile_Page = QWidget()
        self.Profile_Page.setObjectName(u"Profile_Page")
        self.General_info = QLabel(self.Profile_Page)
        self.General_info.setObjectName(u"General_info")
        self.General_info.setGeometry(QRect(0, 130, 925, 60))
        font = QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.General_info.setFont(font)
        self.General_info.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: \"#e6e6e6\";")
        self.General_info.setAlignment(Qt.AlignCenter)
        self.f_name_input = QGroupBox(self.Profile_Page)
        self.f_name_input.setObjectName(u"f_name_input")
        self.f_name_input.setGeometry(QRect(130, 220, 320, 40))
        self.f_name_input.setMinimumSize(QSize(320, 40))
        self.f_name_input.setMaximumSize(QSize(290, 40))
        self.f_name_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_17 = QHBoxLayout(self.f_name_input)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.department_input = QGroupBox(self.Profile_Page)
        self.department_input.setObjectName(u"department_input")
        self.department_input.setGeometry(QRect(130, 400, 320, 40))
        self.department_input.setMinimumSize(QSize(320, 40))
        self.department_input.setMaximumSize(QSize(320, 40))
        self.department_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_18 = QHBoxLayout(self.department_input)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.leave_input = QGroupBox(self.Profile_Page)
        self.leave_input.setObjectName(u"leave_input")
        self.leave_input.setGeometry(QRect(370, 630, 100, 40))
        self.leave_input.setMinimumSize(QSize(100, 40))
        self.leave_input.setMaximumSize(QSize(100, 40))
        self.leave_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_44 = QHBoxLayout(self.leave_input)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.pending_applications_input = QGroupBox(self.Profile_Page)
        self.pending_applications_input.setObjectName(u"pending_applications_input")
        self.pending_applications_input.setGeometry(QRect(770, 570, 100, 40))
        self.pending_applications_input.setMinimumSize(QSize(100, 40))
        self.pending_applications_input.setMaximumSize(QSize(100, 40))
        self.pending_applications_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_49 = QHBoxLayout(self.pending_applications_input)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.salary_input = QGroupBox(self.Profile_Page)
        self.salary_input.setObjectName(u"salary_input")
        self.salary_input.setGeometry(QRect(570, 400, 300, 40))
        self.salary_input.setMinimumSize(QSize(300, 40))
        self.salary_input.setMaximumSize(QSize(300, 40))
        self.salary_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_19 = QHBoxLayout(self.salary_input)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.f_name = QGroupBox(self.Profile_Page)
        self.f_name.setObjectName(u"f_name")
        self.f_name.setGeometry(QRect(10, 220, 121, 40))
        self.f_name.setMinimumSize(QSize(0, 40))
        self.f_name.setMaximumSize(QSize(16777215, 40))
        self.f_name.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_20 = QHBoxLayout(self.f_name)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.absent = QGroupBox(self.Profile_Page)
        self.absent.setObjectName(u"absent")
        self.absent.setGeometry(QRect(10, 630, 121, 40))
        self.absent.setMinimumSize(QSize(0, 40))
        self.absent.setMaximumSize(QSize(16777215, 40))
        self.absent.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_50 = QHBoxLayout(self.absent)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.current_deduction_input = QGroupBox(self.Profile_Page)
        self.current_deduction_input.setObjectName(u"current_deduction_input")
        self.current_deduction_input.setGeometry(QRect(770, 630, 100, 40))
        self.current_deduction_input.setMinimumSize(QSize(100, 40))
        self.current_deduction_input.setMaximumSize(QSize(100, 40))
        self.current_deduction_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_51 = QHBoxLayout(self.current_deduction_input)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.contact_input = QGroupBox(self.Profile_Page)
        self.contact_input.setObjectName(u"contact_input")
        self.contact_input.setGeometry(QRect(570, 280, 300, 40))
        self.contact_input.setMinimumSize(QSize(300, 40))
        self.contact_input.setMaximumSize(QSize(300, 40))
        self.contact_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_21 = QHBoxLayout(self.contact_input)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.current_deduction = QGroupBox(self.Profile_Page)
        self.current_deduction.setObjectName(u"current_deduction")
        self.current_deduction.setGeometry(QRect(500, 630, 261, 41))
        self.current_deduction.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_52 = QHBoxLayout(self.current_deduction)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.head_dep = QGroupBox(self.Profile_Page)
        self.head_dep.setObjectName(u"head_dep")
        self.head_dep.setGeometry(QRect(10, 60, 561, 40))
        self.head_dep.setMinimumSize(QSize(0, 40))
        self.head_dep.setMaximumSize(QSize(16777215, 40))
        self.head_dep.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 500 18pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_22 = QHBoxLayout(self.head_dep)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.l_name_input = QGroupBox(self.Profile_Page)
        self.l_name_input.setObjectName(u"l_name_input")
        self.l_name_input.setGeometry(QRect(570, 220, 300, 40))
        self.l_name_input.setMinimumSize(QSize(300, 40))
        self.l_name_input.setMaximumSize(QSize(300, 40))
        self.l_name_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_23 = QHBoxLayout(self.l_name_input)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.present_input = QGroupBox(self.Profile_Page)
        self.present_input.setObjectName(u"present_input")
        self.present_input.setGeometry(QRect(370, 570, 100, 40))
        self.present_input.setMinimumSize(QSize(100, 40))
        self.present_input.setMaximumSize(QSize(100, 40))
        self.present_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_39 = QHBoxLayout(self.present_input)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.salary_2 = QGroupBox(self.Profile_Page)
        self.salary_2.setObjectName(u"salary_2")
        self.salary_2.setGeometry(QRect(450, 400, 121, 40))
        self.salary_2.setMinimumSize(QSize(0, 40))
        self.salary_2.setMaximumSize(QSize(16777215, 40))
        self.salary_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_24 = QHBoxLayout(self.salary_2)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.address = QGroupBox(self.Profile_Page)
        self.address.setObjectName(u"address")
        self.address.setGeometry(QRect(10, 340, 121, 40))
        self.address.setMinimumSize(QSize(0, 40))
        self.address.setMaximumSize(QSize(16777215, 40))
        self.address.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_25 = QHBoxLayout(self.address)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.Current_Month = QLabel(self.Profile_Page)
        self.Current_Month.setObjectName(u"Current_Month")
        self.Current_Month.setGeometry(QRect(0, 480, 925, 60))
        self.Current_Month.setFont(font)
        self.Current_Month.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: \"#e6e6e6\";")
        self.Current_Month.setAlignment(Qt.AlignCenter)
        self.l_name = QGroupBox(self.Profile_Page)
        self.l_name.setObjectName(u"l_name")
        self.l_name.setGeometry(QRect(450, 220, 121, 41))
        self.l_name.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_26 = QHBoxLayout(self.l_name)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.pending_applications = QGroupBox(self.Profile_Page)
        self.pending_applications.setObjectName(u"pending_applications")
        self.pending_applications.setGeometry(QRect(500, 570, 261, 41))
        self.pending_applications.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_53 = QHBoxLayout(self.pending_applications)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.present = QGroupBox(self.Profile_Page)
        self.present.setObjectName(u"present")
        self.present.setGeometry(QRect(250, 570, 121, 41))
        self.present.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_54 = QHBoxLayout(self.present)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.email_input = QGroupBox(self.Profile_Page)
        self.email_input.setObjectName(u"email_input")
        self.email_input.setGeometry(QRect(130, 280, 320, 40))
        self.email_input.setMinimumSize(QSize(320, 40))
        self.email_input.setMaximumSize(QSize(320, 40))
        self.email_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_27 = QHBoxLayout(self.email_input)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.leave = QGroupBox(self.Profile_Page)
        self.leave.setObjectName(u"leave")
        self.leave.setGeometry(QRect(250, 630, 121, 41))
        self.leave.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_55 = QHBoxLayout(self.leave)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.contact = QGroupBox(self.Profile_Page)
        self.contact.setObjectName(u"contact")
        self.contact.setGeometry(QRect(450, 280, 121, 41))
        self.contact.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_28 = QHBoxLayout(self.contact)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.department = QGroupBox(self.Profile_Page)
        self.department.setObjectName(u"department")
        self.department.setGeometry(QRect(10, 400, 121, 40))
        self.department.setMinimumSize(QSize(0, 40))
        self.department.setMaximumSize(QSize(16777215, 40))
        self.department.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_29 = QHBoxLayout(self.department)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.address_input = QGroupBox(self.Profile_Page)
        self.address_input.setObjectName(u"address_input")
        self.address_input.setGeometry(QRect(130, 340, 750, 40))
        self.address_input.setMinimumSize(QSize(750, 40))
        self.address_input.setMaximumSize(QSize(750, 40))
        self.address_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_30 = QHBoxLayout(self.address_input)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.Head_name = QGroupBox(self.Profile_Page)
        self.Head_name.setObjectName(u"Head_name")
        self.Head_name.setGeometry(QRect(10, 20, 561, 40))
        self.Head_name.setMinimumSize(QSize(0, 40))
        self.Head_name.setMaximumSize(QSize(16777215, 40))
        self.Head_name.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 24pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_31 = QHBoxLayout(self.Head_name)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.email = QGroupBox(self.Profile_Page)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(10, 280, 121, 40))
        self.email.setMinimumSize(QSize(0, 40))
        self.email.setMaximumSize(QSize(16777215, 40))
        self.email.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_32 = QHBoxLayout(self.email)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.absent_input = QGroupBox(self.Profile_Page)
        self.absent_input.setObjectName(u"absent_input")
        self.absent_input.setGeometry(QRect(130, 630, 100, 40))
        self.absent_input.setMinimumSize(QSize(100, 40))
        self.absent_input.setMaximumSize(QSize(100, 40))
        self.absent_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_56 = QHBoxLayout(self.absent_input)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.Pages.addWidget(self.Profile_Page)
        Employee_Page.setCentralWidget(self.Page)

        self.retranslateUi(Employee_Page)

        self.Pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Employee_Page)
    # setupUi

    def retranslateUi(self, Employee_Page):
        Employee_Page.setWindowTitle(QCoreApplication.translate("Employee_Page", u"MainWindow", None))
        self.side_bar.setTitle("")
        self.logo_2.setText("")
        self.profile_2.setText(QCoreApplication.translate("Employee_Page", u"Leave Application", None))
        self.leave_report_2.setText(QCoreApplication.translate("Employee_Page", u"Profile", None))
        self.leave_application_2.setText(QCoreApplication.translate("Employee_Page", u"Salary", None))
        self.salary_3.setText(QCoreApplication.translate("Employee_Page", u"Leave Report", None))
        self.attendance_2.setText(QCoreApplication.translate("Employee_Page", u"Attendance", None))
        self.sign_out_2.setText(QCoreApplication.translate("Employee_Page", u"  Sign Out ", None))
        self.General_info.setText(QCoreApplication.translate("Employee_Page", u" General Information", None))
        self.f_name_input.setTitle(QCoreApplication.translate("Employee_Page", u"Aatiqa", None))
        self.department_input.setTitle(QCoreApplication.translate("Employee_Page", u"Accounts", None))
        self.leave_input.setTitle(QCoreApplication.translate("Employee_Page", u"1", None))
        self.pending_applications_input.setTitle(QCoreApplication.translate("Employee_Page", u"1", None))
        self.salary_input.setTitle(QCoreApplication.translate("Employee_Page", u"Rs. 355000", None))
        self.f_name.setTitle(QCoreApplication.translate("Employee_Page", u"First Name", None))
        self.absent.setTitle(QCoreApplication.translate("Employee_Page", u"Absent", None))
        self.current_deduction_input.setTitle(QCoreApplication.translate("Employee_Page", u"Rs. 23666", None))
        self.contact_input.setTitle(QCoreApplication.translate("Employee_Page", u"0333-8629629", None))
        self.current_deduction.setTitle(QCoreApplication.translate("Employee_Page", u"Current Salary Deduction", None))
        self.head_dep.setTitle(QCoreApplication.translate("Employee_Page", u"Accounts", None))
        self.l_name_input.setTitle(QCoreApplication.translate("Employee_Page", u"Hussain", None))
        self.present_input.setTitle(QCoreApplication.translate("Employee_Page", u"21", None))
        self.salary_2.setTitle(QCoreApplication.translate("Employee_Page", u"Salary", None))
        self.address.setTitle(QCoreApplication.translate("Employee_Page", u"Address", None))
        self.Current_Month.setText(QCoreApplication.translate("Employee_Page", u"Current Month Details", None))
        self.l_name.setTitle(QCoreApplication.translate("Employee_Page", u"Last Name", None))
        self.pending_applications.setTitle(QCoreApplication.translate("Employee_Page", u"Pending Leave Applications", None))
        self.present.setTitle(QCoreApplication.translate("Employee_Page", u"Present", None))
        self.email_input.setTitle(QCoreApplication.translate("Employee_Page", u"aatiqahussain@gmail.com", None))
        self.leave.setTitle(QCoreApplication.translate("Employee_Page", u"Leave", None))
        self.contact.setTitle(QCoreApplication.translate("Employee_Page", u"Contact", None))
        self.department.setTitle(QCoreApplication.translate("Employee_Page", u"Department", None))
        self.address_input.setTitle(QCoreApplication.translate("Employee_Page", u"852-B Milaad Street, Faisal Town, Lahore", None))
        self.Head_name.setTitle(QCoreApplication.translate("Employee_Page", u"Aatiqa Hussain", None))
        self.email.setTitle(QCoreApplication.translate("Employee_Page", u"Email", None))
        self.absent_input.setTitle(QCoreApplication.translate("Employee_Page", u"2", None))
    # retranslateUi

