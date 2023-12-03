# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Employee_pagebCwhJg.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QWidget)

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
        self.profile_page = QWidget()
        self.profile_page.setObjectName(u"profile_page")
        self.General_info = QLabel(self.profile_page)
        self.General_info.setObjectName(u"General_info")
        self.General_info.setGeometry(QRect(0, 130, 925, 60))
        font = QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.General_info.setFont(font)
        self.General_info.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: \"#e6e6e6\";")
        self.General_info.setAlignment(Qt.AlignCenter)
        self.f_name_input = QGroupBox(self.profile_page)
        self.f_name_input.setObjectName(u"f_name_input")
        self.f_name_input.setGeometry(QRect(130, 220, 320, 40))
        self.f_name_input.setMinimumSize(QSize(320, 40))
        self.f_name_input.setMaximumSize(QSize(290, 40))
        self.f_name_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_17 = QHBoxLayout(self.f_name_input)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.department_input = QGroupBox(self.profile_page)
        self.department_input.setObjectName(u"department_input")
        self.department_input.setGeometry(QRect(130, 400, 320, 40))
        self.department_input.setMinimumSize(QSize(320, 40))
        self.department_input.setMaximumSize(QSize(320, 40))
        self.department_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_18 = QHBoxLayout(self.department_input)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.leave_input = QGroupBox(self.profile_page)
        self.leave_input.setObjectName(u"leave_input")
        self.leave_input.setGeometry(QRect(370, 630, 100, 40))
        self.leave_input.setMinimumSize(QSize(100, 40))
        self.leave_input.setMaximumSize(QSize(100, 40))
        self.leave_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_44 = QHBoxLayout(self.leave_input)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.pending_applications_input = QGroupBox(self.profile_page)
        self.pending_applications_input.setObjectName(u"pending_applications_input")
        self.pending_applications_input.setGeometry(QRect(770, 570, 100, 40))
        self.pending_applications_input.setMinimumSize(QSize(100, 40))
        self.pending_applications_input.setMaximumSize(QSize(100, 40))
        self.pending_applications_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_49 = QHBoxLayout(self.pending_applications_input)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.salary_input = QGroupBox(self.profile_page)
        self.salary_input.setObjectName(u"salary_input")
        self.salary_input.setGeometry(QRect(570, 400, 300, 40))
        self.salary_input.setMinimumSize(QSize(300, 40))
        self.salary_input.setMaximumSize(QSize(300, 40))
        self.salary_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_19 = QHBoxLayout(self.salary_input)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.f_name = QGroupBox(self.profile_page)
        self.f_name.setObjectName(u"f_name")
        self.f_name.setGeometry(QRect(10, 220, 121, 40))
        self.f_name.setMinimumSize(QSize(0, 40))
        self.f_name.setMaximumSize(QSize(16777215, 40))
        self.f_name.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_20 = QHBoxLayout(self.f_name)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.absent = QGroupBox(self.profile_page)
        self.absent.setObjectName(u"absent")
        self.absent.setGeometry(QRect(10, 630, 121, 40))
        self.absent.setMinimumSize(QSize(0, 40))
        self.absent.setMaximumSize(QSize(16777215, 40))
        self.absent.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_50 = QHBoxLayout(self.absent)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.current_deduction_input = QGroupBox(self.profile_page)
        self.current_deduction_input.setObjectName(u"current_deduction_input")
        self.current_deduction_input.setGeometry(QRect(770, 630, 100, 40))
        self.current_deduction_input.setMinimumSize(QSize(100, 40))
        self.current_deduction_input.setMaximumSize(QSize(100, 40))
        self.current_deduction_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_51 = QHBoxLayout(self.current_deduction_input)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.contact_input = QGroupBox(self.profile_page)
        self.contact_input.setObjectName(u"contact_input")
        self.contact_input.setGeometry(QRect(570, 280, 300, 40))
        self.contact_input.setMinimumSize(QSize(300, 40))
        self.contact_input.setMaximumSize(QSize(300, 40))
        self.contact_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_21 = QHBoxLayout(self.contact_input)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.current_deduction = QGroupBox(self.profile_page)
        self.current_deduction.setObjectName(u"current_deduction")
        self.current_deduction.setGeometry(QRect(500, 630, 261, 41))
        self.current_deduction.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_52 = QHBoxLayout(self.current_deduction)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.department_title = QGroupBox(self.profile_page)
        self.department_title.setObjectName(u"department_title")
        self.department_title.setGeometry(QRect(10, 60, 561, 40))
        self.department_title.setMinimumSize(QSize(0, 40))
        self.department_title.setMaximumSize(QSize(16777215, 40))
        self.department_title.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 500 18pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_22 = QHBoxLayout(self.department_title)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.l_name_input = QGroupBox(self.profile_page)
        self.l_name_input.setObjectName(u"l_name_input")
        self.l_name_input.setGeometry(QRect(570, 220, 300, 40))
        self.l_name_input.setMinimumSize(QSize(300, 40))
        self.l_name_input.setMaximumSize(QSize(300, 40))
        self.l_name_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_23 = QHBoxLayout(self.l_name_input)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.present_input = QGroupBox(self.profile_page)
        self.present_input.setObjectName(u"present_input")
        self.present_input.setGeometry(QRect(370, 570, 100, 40))
        self.present_input.setMinimumSize(QSize(100, 40))
        self.present_input.setMaximumSize(QSize(100, 40))
        self.present_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_39 = QHBoxLayout(self.present_input)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.salary_2 = QGroupBox(self.profile_page)
        self.salary_2.setObjectName(u"salary_2")
        self.salary_2.setGeometry(QRect(450, 400, 121, 40))
        self.salary_2.setMinimumSize(QSize(0, 40))
        self.salary_2.setMaximumSize(QSize(16777215, 40))
        self.salary_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_24 = QHBoxLayout(self.salary_2)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.address = QGroupBox(self.profile_page)
        self.address.setObjectName(u"address")
        self.address.setGeometry(QRect(10, 340, 121, 40))
        self.address.setMinimumSize(QSize(0, 40))
        self.address.setMaximumSize(QSize(16777215, 40))
        self.address.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_25 = QHBoxLayout(self.address)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.Current_Month = QLabel(self.profile_page)
        self.Current_Month.setObjectName(u"Current_Month")
        self.Current_Month.setGeometry(QRect(0, 480, 925, 60))
        self.Current_Month.setFont(font)
        self.Current_Month.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: \"#e6e6e6\";")
        self.Current_Month.setAlignment(Qt.AlignCenter)
        self.l_name = QGroupBox(self.profile_page)
        self.l_name.setObjectName(u"l_name")
        self.l_name.setGeometry(QRect(450, 220, 121, 41))
        self.l_name.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_26 = QHBoxLayout(self.l_name)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.pending_applications = QGroupBox(self.profile_page)
        self.pending_applications.setObjectName(u"pending_applications")
        self.pending_applications.setGeometry(QRect(500, 570, 261, 41))
        self.pending_applications.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_53 = QHBoxLayout(self.pending_applications)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.present = QGroupBox(self.profile_page)
        self.present.setObjectName(u"present")
        self.present.setGeometry(QRect(250, 570, 121, 41))
        self.present.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_54 = QHBoxLayout(self.present)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.email_input = QGroupBox(self.profile_page)
        self.email_input.setObjectName(u"email_input")
        self.email_input.setGeometry(QRect(130, 280, 320, 40))
        self.email_input.setMinimumSize(QSize(320, 40))
        self.email_input.setMaximumSize(QSize(320, 40))
        self.email_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_27 = QHBoxLayout(self.email_input)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.leave = QGroupBox(self.profile_page)
        self.leave.setObjectName(u"leave")
        self.leave.setGeometry(QRect(250, 630, 121, 41))
        self.leave.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_55 = QHBoxLayout(self.leave)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.contact = QGroupBox(self.profile_page)
        self.contact.setObjectName(u"contact")
        self.contact.setGeometry(QRect(450, 280, 121, 41))
        self.contact.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_28 = QHBoxLayout(self.contact)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.department = QGroupBox(self.profile_page)
        self.department.setObjectName(u"department")
        self.department.setGeometry(QRect(10, 400, 121, 40))
        self.department.setMinimumSize(QSize(0, 40))
        self.department.setMaximumSize(QSize(16777215, 40))
        self.department.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_29 = QHBoxLayout(self.department)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.address_input = QGroupBox(self.profile_page)
        self.address_input.setObjectName(u"address_input")
        self.address_input.setGeometry(QRect(130, 340, 750, 40))
        self.address_input.setMinimumSize(QSize(750, 40))
        self.address_input.setMaximumSize(QSize(750, 40))
        self.address_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_30 = QHBoxLayout(self.address_input)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.name_2 = QGroupBox(self.profile_page)
        self.name_2.setObjectName(u"name_2")
        self.name_2.setGeometry(QRect(10, 20, 561, 40))
        self.name_2.setMinimumSize(QSize(0, 40))
        self.name_2.setMaximumSize(QSize(16777215, 40))
        self.name_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 24pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_31 = QHBoxLayout(self.name_2)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.email = QGroupBox(self.profile_page)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(10, 280, 121, 40))
        self.email.setMinimumSize(QSize(0, 40))
        self.email.setMaximumSize(QSize(16777215, 40))
        self.email.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_32 = QHBoxLayout(self.email)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.absent_input = QGroupBox(self.profile_page)
        self.absent_input.setObjectName(u"absent_input")
        self.absent_input.setGeometry(QRect(130, 630, 100, 40))
        self.absent_input.setMinimumSize(QSize(100, 40))
        self.absent_input.setMaximumSize(QSize(100, 40))
        self.absent_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_56 = QHBoxLayout(self.absent_input)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.present_2 = QGroupBox(self.profile_page)
        self.present_2.setObjectName(u"present_2")
        self.present_2.setGeometry(QRect(10, 570, 121, 41))
        self.present_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_57 = QHBoxLayout(self.present_2)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.present_input_2 = QGroupBox(self.profile_page)
        self.present_input_2.setObjectName(u"present_input_2")
        self.present_input_2.setGeometry(QRect(130, 570, 100, 40))
        self.present_input_2.setMinimumSize(QSize(100, 40))
        self.present_input_2.setMaximumSize(QSize(100, 40))
        self.present_input_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_40 = QHBoxLayout(self.present_input_2)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.Pages.addWidget(self.profile_page)
        self.leave_report = QWidget()
        self.leave_report.setObjectName(u"leave_report")
        self.title = QLabel(self.leave_report)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(0, 30, 925, 60))
        self.title.setFont(font)
        self.title.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: \"#e6e6e6\";")
        self.remaining_health = QLabel(self.leave_report)
        self.remaining_health.setObjectName(u"remaining_health")
        self.remaining_health.setGeometry(QRect(570, 160, 30, 41))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(16)
        font1.setWeight(QFont.DemiBold)
        font1.setItalic(False)
        self.remaining_health.setFont(font1)
        self.remaining_health.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"\n"
"font: 600 16pt \"Segoe UI\";")
        self.total = QLabel(self.leave_report)
        self.total.setObjectName(u"total")
        self.total.setGeometry(QRect(290, 130, 120, 40))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(16)
        font2.setWeight(QFont.Black)
        font2.setItalic(False)
        self.total.setFont(font2)
        self.total.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 900 16pt \"Segoe UI\";")
        self.total_general = QLabel(self.leave_report)
        self.total_general.setObjectName(u"total_general")
        self.total_general.setGeometry(QRect(450, 130, 30, 40))
        self.total_general.setFont(font1)
        self.total_general.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 600 16pt \"Segoe UI\";")
        self.health = QLabel(self.leave_report)
        self.health.setObjectName(u"health")
        self.health.setGeometry(QRect(550, 100, 100, 40))
        self.health.setFont(font2)
        self.health.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 900 16pt \"Segoe UI\";")
        self.remaining_general = QLabel(self.leave_report)
        self.remaining_general.setObjectName(u"remaining_general")
        self.remaining_general.setGeometry(QRect(450, 160, 30, 41))
        self.remaining_general.setFont(font1)
        self.remaining_general.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"\n"
"font: 600 16pt \"Segoe UI\";")
        self.remaing = QLabel(self.leave_report)
        self.remaing.setObjectName(u"remaing")
        self.remaing.setGeometry(QRect(270, 160, 120, 41))
        self.remaing.setFont(font2)
        self.remaing.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 900 16pt \"Segoe UI\";")
        self.general = QLabel(self.leave_report)
        self.general.setObjectName(u"general")
        self.general.setGeometry(QRect(420, 100, 100, 40))
        self.general.setFont(font2)
        self.general.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 900 16pt \"Segoe UI\";")
        self.total_health = QLabel(self.leave_report)
        self.total_health.setObjectName(u"total_health")
        self.total_health.setGeometry(QRect(570, 130, 30, 40))
        self.total_health.setFont(font1)
        self.total_health.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 600 16pt \"Segoe UI\";")
        self.leave_record = QTableWidget(self.leave_report)
        if (self.leave_record.columnCount() < 3):
            self.leave_record.setColumnCount(3)
        brush = QBrush(QColor(85, 55, 89, 255))
        brush.setStyle(Qt.SolidPattern)
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3);
        __qtablewidgetitem.setBackground(QColor(85, 55, 89));
        __qtablewidgetitem.setForeground(brush);
        self.leave_record.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font3);
        __qtablewidgetitem1.setBackground(QColor(85, 55, 89));
        __qtablewidgetitem1.setForeground(brush);
        self.leave_record.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font3);
        __qtablewidgetitem2.setBackground(QColor(85, 55, 89));
        __qtablewidgetitem2.setForeground(brush);
        self.leave_record.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.leave_record.setObjectName(u"leave_record")
        self.leave_record.setGeometry(QRect(100, 220, 721, 461))
        self.leave_record.setStyleSheet(u"QHeaderView::section {\n"
"    background-color: rgb(50, 84, 110); /* Set your desired background color */\n"
"    color: rgb(230, 230, 230); /* Set the text color */\n"
"};\n"
"\n"
"\n"
"color: rgb(50, 84, 110);\n"
"background-color: rgb(230, 230, 230);")
        self.leave_record.horizontalHeader().setDefaultSectionSize(237)
        self.Pages.addWidget(self.leave_report)
        self.attendance = QWidget()
        self.attendance.setObjectName(u"attendance")
        self.dec = QPushButton(self.attendance)
        self.dec.setObjectName(u"dec")
        self.dec.setGeometry(QRect(830, 170, 90, 30))
        self.dec.setFont(font3)
        self.dec.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: rgb(230, 230, 230);\n"
"border:1px solid;\n"
"border-radius: 10px")
        self.sep = QPushButton(self.attendance)
        self.sep.setObjectName(u"sep")
        self.sep.setGeometry(QRect(529, 170, 92, 30))
        self.sep.setFont(font3)
        self.sep.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: rgb(230, 230, 230);\n"
"border:1px solid;\n"
"border-radius: 10px")
        self.april = QPushButton(self.attendance)
        self.april.setObjectName(u"april")
        self.april.setGeometry(QRect(580, 130, 90, 30))
        self.april.setFont(font3)
        self.april.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: rgb(230, 230, 230);\n"
"border:1px solid;\n"
"border-radius: 10px")
        self.march = QPushButton(self.attendance)
        self.march.setObjectName(u"march")
        self.march.setGeometry(QRect(480, 130, 90, 30))
        self.march.setFont(font3)
        self.march.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: rgb(230, 230, 230);\n"
"border:1px solid;\n"
"border-radius: 10px\n"
"")
        self.oct = QPushButton(self.attendance)
        self.oct.setObjectName(u"oct")
        self.oct.setGeometry(QRect(630, 170, 90, 30))
        self.oct.setFont(font3)
        self.oct.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: rgb(230, 230, 230);\n"
"border:1px solid;\n"
"border-radius: 10px")
        self.feb = QPushButton(self.attendance)
        self.feb.setObjectName(u"feb")
        self.feb.setGeometry(QRect(380, 130, 90, 30))
        self.feb.setFont(font3)
        self.feb.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: rgb(230, 230, 230);\n"
"border:1px solid;\n"
"border-radius: 10px")
        self.jan = QPushButton(self.attendance)
        self.jan.setObjectName(u"jan")
        self.jan.setGeometry(QRect(280, 130, 90, 30))
        self.jan.setFont(font3)
        self.jan.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: rgb(230, 230, 230);\n"
"border:1px solid;\n"
"border-radius: 10px")
        self.stackedWidget = QStackedWidget(self.attendance)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(40, 230, 741, 481))
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
        brush1 = QBrush(QColor(50, 84, 110, 255))
        brush1.setStyle(Qt.SolidPattern)
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font4);
        __qtablewidgetitem3.setBackground(QColor(85, 55, 89));
        __qtablewidgetitem3.setForeground(brush1);
        self.table_start.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        __qtablewidgetitem4.setBackground(QColor(85, 55, 89));
        __qtablewidgetitem4.setForeground(brush1);
        self.table_start.setHorizontalHeaderItem(1, __qtablewidgetitem4)
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
        font5 = QFont()
        font5.setPointSize(14)
        font5.setBold(True)
        font5.setKerning(True)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font5);
        __qtablewidgetitem5.setBackground(QColor(230, 230, 230, 10));
        __qtablewidgetitem5.setForeground(brush1);
        self.table_end.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font4);
        __qtablewidgetitem6.setBackground(QColor(230, 230, 230));
        __qtablewidgetitem6.setForeground(brush1);
        self.table_end.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        self.table_end.setObjectName(u"table_end")
        self.table_end.setGeometry(QRect(110, 30, 621, 441))
        self.table_end.setStyleSheet(u"background-color: rgb(230, 230, 230);\n"
"color: rgb(50, 84, 110);")
        self.table_end.horizontalHeader().setDefaultSectionSize(305)
        self.stackedWidget.addWidget(self.second_page)
        self.label = QLabel(self.attendance)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 915, 65))
        font6 = QFont()
        font6.setPointSize(25)
        font6.setBold(True)
        font6.setUnderline(False)
        font6.setStrikeOut(False)
        font6.setKerning(True)
        self.label.setFont(font6)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"background-color: rgb(50, 84, 110);")
        self.may = QPushButton(self.attendance)
        self.may.setObjectName(u"may")
        self.may.setGeometry(QRect(680, 130, 90, 30))
        self.may.setFont(font3)
        self.may.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: rgb(230, 230, 230);\n"
"border:1px solid;\n"
"border-radius: 10px")
        self.june = QPushButton(self.attendance)
        self.june.setObjectName(u"june")
        self.june.setGeometry(QRect(780, 130, 90, 30))
        self.june.setFont(font3)
        self.june.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: rgb(230, 230, 230);\n"
"border:1px solid;\n"
"border-radius: 10px\n"
"")
        self.july = QPushButton(self.attendance)
        self.july.setObjectName(u"july")
        self.july.setGeometry(QRect(330, 170, 90, 30))
        self.july.setFont(font3)
        self.july.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: rgb(230, 230, 230);\n"
"border:1px solid;\n"
"border-radius: 10px")
        self.aug = QPushButton(self.attendance)
        self.aug.setObjectName(u"aug")
        self.aug.setGeometry(QRect(430, 170, 90, 30))
        self.aug.setFont(font3)
        self.aug.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: rgb(230, 230, 230);\n"
"border:1px solid;\n"
"border-radius: 10px")
        self.nov = QPushButton(self.attendance)
        self.nov.setObjectName(u"nov")
        self.nov.setGeometry(QRect(730, 170, 90, 30))
        self.nov.setFont(font3)
        self.nov.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: rgb(230, 230, 230);\n"
"border:1px solid;\n"
"border-radius: 10px")
        self.Pages.addWidget(self.attendance)
        self.salary_report = QWidget()
        self.salary_report.setObjectName(u"salary_report")
        self.salary_record = QTableWidget(self.salary_report)
        if (self.salary_record.columnCount() < 5):
            self.salary_record.setColumnCount(5)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font4);
        __qtablewidgetitem7.setBackground(QColor(85, 55, 89));
        __qtablewidgetitem7.setForeground(brush1);
        self.salary_record.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font4);
        __qtablewidgetitem8.setBackground(QColor(85, 55, 89));
        __qtablewidgetitem8.setForeground(brush1);
        self.salary_record.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font4);
        __qtablewidgetitem9.setBackground(QColor(85, 55, 89));
        __qtablewidgetitem9.setForeground(brush1);
        self.salary_record.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font4);
        __qtablewidgetitem10.setBackground(QColor(81, 55, 89));
        __qtablewidgetitem10.setForeground(brush1);
        self.salary_record.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignHCenter|Qt.AlignTop);
        __qtablewidgetitem11.setFont(font4);
        __qtablewidgetitem11.setBackground(QColor(85, 55, 89));
        __qtablewidgetitem11.setForeground(brush1);
        self.salary_record.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        if (self.salary_record.rowCount() < 12):
            self.salary_record.setRowCount(12)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.salary_record.setVerticalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.salary_record.setVerticalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.salary_record.setVerticalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.salary_record.setVerticalHeaderItem(3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.salary_record.setVerticalHeaderItem(4, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.salary_record.setVerticalHeaderItem(5, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.salary_record.setVerticalHeaderItem(6, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.salary_record.setVerticalHeaderItem(7, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.salary_record.setVerticalHeaderItem(8, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.salary_record.setVerticalHeaderItem(9, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.salary_record.setVerticalHeaderItem(10, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.salary_record.setVerticalHeaderItem(11, __qtablewidgetitem23)
        font7 = QFont()
        font7.setPointSize(12)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font7);
        self.salary_record.setItem(0, 0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setFont(font7);
        self.salary_record.setItem(1, 0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setFont(font7);
        self.salary_record.setItem(2, 0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setFont(font7);
        self.salary_record.setItem(3, 0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setFont(font7);
        self.salary_record.setItem(4, 0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setFont(font7);
        self.salary_record.setItem(5, 0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setFont(font7);
        self.salary_record.setItem(6, 0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setFont(font7);
        self.salary_record.setItem(7, 0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setFont(font7);
        self.salary_record.setItem(8, 0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setFont(font7);
        self.salary_record.setItem(9, 0, __qtablewidgetitem33)
        font8 = QFont()
        font8.setPointSize(13)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setFont(font8);
        self.salary_record.setItem(10, 0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setFont(font7);
        self.salary_record.setItem(11, 0, __qtablewidgetitem35)
        self.salary_record.setObjectName(u"salary_record")
        self.salary_record.setGeometry(QRect(50, 230, 841, 401))
        self.salary_record.setStyleSheet(u"QHeaderView::section {\n"
"    background-color: rgb(50, 84, 110); /* Set your desired background color */\n"
"    color: rgb(230, 230, 230); /* Set the text color */\n"
"};\n"
"\n"
"color: rgb(50, 84, 110);\n"
"background-color: rgb(230, 230, 230);\n"
"\n"
"")
        self.salary_record.horizontalHeader().setDefaultSectionSize(162)
        self.name_input = QLabel(self.salary_report)
        self.name_input.setObjectName(u"name_input")
        self.name_input.setGeometry(QRect(240, 130, 500, 30))
        font9 = QFont()
        font9.setFamilies([u"Segoe UI"])
        font9.setPointSize(14)
        font9.setBold(True)
        font9.setItalic(False)
        font9.setUnderline(False)
        self.name_input.setFont(font9)
        self.name_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";")
        self.department_input_2 = QLabel(self.salary_report)
        self.department_input_2.setObjectName(u"department_input_2")
        self.department_input_2.setGeometry(QRect(240, 170, 500, 30))
        font10 = QFont()
        font10.setFamilies([u"Segoe UI"])
        font10.setPointSize(14)
        font10.setBold(True)
        font10.setItalic(False)
        self.department_input_2.setFont(font10)
        self.department_input_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";")
        self.title_2 = QLabel(self.salary_report)
        self.title_2.setObjectName(u"title_2")
        self.title_2.setGeometry(QRect(0, 30, 925, 61))
        font11 = QFont()
        font11.setPointSize(26)
        font11.setBold(True)
        self.title_2.setFont(font11)
        self.title_2.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: rgb(230, 230, 230);")
        self.name = QLabel(self.salary_report)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(60, 130, 150, 30))
        self.name.setFont(font2)
        self.name.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 900 16pt \"Segoe UI\";")
        self.department_2 = QLabel(self.salary_report)
        self.department_2.setObjectName(u"department_2")
        self.department_2.setGeometry(QRect(60, 170, 150, 30))
        self.department_2.setFont(font2)
        self.department_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 900 16pt \"Segoe UI\";")
        self.Pages.addWidget(self.salary_report)
        self.leave_application = QWidget()
        self.leave_application.setObjectName(u"leave_application")
        self.description = QLabel(self.leave_application)
        self.description.setObjectName(u"description")
        self.description.setGeometry(QRect(50, 310, 161, 31))
        font12 = QFont()
        font12.setFamilies([u"Segoe UI"])
        font12.setPointSize(18)
        font12.setBold(True)
        font12.setItalic(False)
        self.description.setFont(font12)
        self.description.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 18pt \"Segoe UI\";")
        self.end_date = QLabel(self.leave_application)
        self.end_date.setObjectName(u"end_date")
        self.end_date.setGeometry(QRect(470, 170, 131, 31))
        self.end_date.setFont(font12)
        self.end_date.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 18pt \"Segoe UI\";")
        self.description_input = QTextEdit(self.leave_application)
        self.description_input.setObjectName(u"description_input")
        self.description_input.setGeometry(QRect(60, 400, 821, 201))
        self.exp = QLabel(self.leave_application)
        self.exp.setObjectName(u"exp")
        self.exp.setGeometry(QRect(50, 350, 501, 21))
        font13 = QFont()
        font13.setFamilies([u"Segoe UI"])
        font13.setPointSize(12)
        font13.setBold(False)
        font13.setItalic(False)
        self.exp.setFont(font13)
        self.exp.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 12pt \"Segoe UI\";")
        self.category_input = QComboBox(self.leave_application)
        self.category_input.addItem("")
        self.category_input.addItem("")
        self.category_input.setObjectName(u"category_input")
        self.category_input.setGeometry(QRect(260, 240, 151, 31))
        self.category_input.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.end_date_input = QDateEdit(self.leave_application)
        self.end_date_input.setObjectName(u"end_date_input")
        self.end_date_input.setGeometry(QRect(640, 170, 151, 31))
        self.end_date_input.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.submit_button = QPushButton(self.leave_application)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setGeometry(QRect(420, 620, 131, 51))
        font14 = QFont()
        font14.setFamilies([u"Segoe UI"])
        font14.setPointSize(12)
        font14.setBold(True)
        font14.setItalic(False)
        self.submit_button.setFont(font14)
        self.submit_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.submit_button.setStyleSheet(u"border:2px solid;\n"
"border-radius:20px;\n"
"background-color:rgb(50, 84, 110);\n"
"border-color: rgb(230, 230, 230);\n"
"color: rgb(230, 230, 230);\n"
"font: 700 12pt \"Segoe UI\";")
        self.category = QLabel(self.leave_application)
        self.category.setObjectName(u"category")
        self.category.setGeometry(QRect(50, 230, 141, 41))
        self.category.setFont(font12)
        self.category.setStyleSheet(u"font: 700 18pt \"Segoe UI\";\n"
"color: rgb(50, 84, 110);")
        self.start_date_input = QDateEdit(self.leave_application)
        self.start_date_input.setObjectName(u"start_date_input")
        self.start_date_input.setGeometry(QRect(260, 170, 151, 31))
        self.start_date_input.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.start_date = QLabel(self.leave_application)
        self.start_date.setObjectName(u"start_date")
        self.start_date.setGeometry(QRect(50, 170, 131, 31))
        self.start_date.setFont(font12)
        self.start_date.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 18pt \"Segoe UI\";")
        self.title_3 = QLabel(self.leave_application)
        self.title_3.setObjectName(u"title_3")
        self.title_3.setGeometry(QRect(0, 30, 925, 80))
        font15 = QFont()
        font15.setFamilies([u"Segoe UI"])
        font15.setPointSize(32)
        font15.setBold(True)
        font15.setItalic(False)
        self.title_3.setFont(font15)
        self.title_3.setStyleSheet(u"background-color: rgb(50, 84, 110);\n"
"color: rgb(230, 230, 230);\n"
"font: 700 32pt \"Segoe UI\";")
        self.Pages.addWidget(self.leave_application)
        Employee_Page.setCentralWidget(self.Page)

        self.retranslateUi(Employee_Page)

        self.Pages.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)


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
        self.department_title.setTitle(QCoreApplication.translate("Employee_Page", u"Accounts", None))
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
        self.name_2.setTitle(QCoreApplication.translate("Employee_Page", u"Aatiqa Hussain", None))
        self.email.setTitle(QCoreApplication.translate("Employee_Page", u"Email", None))
        self.absent_input.setTitle(QCoreApplication.translate("Employee_Page", u"2", None))
        self.present_2.setTitle(QCoreApplication.translate("Employee_Page", u"Total", None))
        self.present_input_2.setTitle(QCoreApplication.translate("Employee_Page", u"24", None))
        self.title.setText(QCoreApplication.translate("Employee_Page", u"                                         Leave Report", None))
        self.remaining_health.setText(QCoreApplication.translate("Employee_Page", u"15", None))
        self.total.setText(QCoreApplication.translate("Employee_Page", u"Total", None))
        self.total_general.setText(QCoreApplication.translate("Employee_Page", u"10", None))
        self.health.setText(QCoreApplication.translate("Employee_Page", u"Health", None))
        self.remaining_general.setText(QCoreApplication.translate("Employee_Page", u"8", None))
        self.remaing.setText(QCoreApplication.translate("Employee_Page", u"Remaining", None))
        self.general.setText(QCoreApplication.translate("Employee_Page", u"General", None))
        self.total_health.setText(QCoreApplication.translate("Employee_Page", u"15", None))
        ___qtablewidgetitem = self.leave_record.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Employee_Page", u"Date", None));
        ___qtablewidgetitem1 = self.leave_record.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Employee_Page", u"Type", None));
        ___qtablewidgetitem2 = self.leave_record.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Employee_Page", u"Status", None));
        self.dec.setText(QCoreApplication.translate("Employee_Page", u"December", None))
        self.sep.setText(QCoreApplication.translate("Employee_Page", u"September", None))
        self.april.setText(QCoreApplication.translate("Employee_Page", u"April", None))
        self.march.setText(QCoreApplication.translate("Employee_Page", u"March", None))
        self.oct.setText(QCoreApplication.translate("Employee_Page", u"October", None))
        self.feb.setText(QCoreApplication.translate("Employee_Page", u"February", None))
        self.jan.setText(QCoreApplication.translate("Employee_Page", u"January", None))
        ___qtablewidgetitem3 = self.table_start.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Employee_Page", u"Date", None));
        ___qtablewidgetitem4 = self.table_start.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Employee_Page", u"Status", None));
        ___qtablewidgetitem5 = self.table_end.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Employee_Page", u"Date", None));
        ___qtablewidgetitem6 = self.table_end.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Employee_Page", u"Status", None));
        self.label.setText(QCoreApplication.translate("Employee_Page", u"<html><head/><body><p align=\"center\"><span style=\" color:#e6e6e6;\">Employee Attendance</span></p></body></html>", None))
        self.may.setText(QCoreApplication.translate("Employee_Page", u"May", None))
        self.june.setText(QCoreApplication.translate("Employee_Page", u"June", None))
        self.july.setText(QCoreApplication.translate("Employee_Page", u"July", None))
        self.aug.setText(QCoreApplication.translate("Employee_Page", u"August", None))
        self.nov.setText(QCoreApplication.translate("Employee_Page", u"November", None))
        ___qtablewidgetitem7 = self.salary_record.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Employee_Page", u"Months", None));
        ___qtablewidgetitem8 = self.salary_record.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Employee_Page", u"Issuance Date", None));
        ___qtablewidgetitem9 = self.salary_record.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Employee_Page", u"Deduction", None));
        ___qtablewidgetitem10 = self.salary_record.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Employee_Page", u"Salary", None));
        ___qtablewidgetitem11 = self.salary_record.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Employee_Page", u"Total Wage", None));
        ___qtablewidgetitem12 = self.salary_record.verticalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Employee_Page", u"1.", None));
        ___qtablewidgetitem13 = self.salary_record.verticalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Employee_Page", u"2.", None));
        ___qtablewidgetitem14 = self.salary_record.verticalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Employee_Page", u"3.", None));
        ___qtablewidgetitem15 = self.salary_record.verticalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Employee_Page", u"4.", None));
        ___qtablewidgetitem16 = self.salary_record.verticalHeaderItem(4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Employee_Page", u"5.", None));
        ___qtablewidgetitem17 = self.salary_record.verticalHeaderItem(5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Employee_Page", u"6.", None));
        ___qtablewidgetitem18 = self.salary_record.verticalHeaderItem(6)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Employee_Page", u"7.", None));
        ___qtablewidgetitem19 = self.salary_record.verticalHeaderItem(7)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Employee_Page", u"8.", None));
        ___qtablewidgetitem20 = self.salary_record.verticalHeaderItem(8)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Employee_Page", u"9.", None));
        ___qtablewidgetitem21 = self.salary_record.verticalHeaderItem(9)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Employee_Page", u"10.", None));
        ___qtablewidgetitem22 = self.salary_record.verticalHeaderItem(10)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Employee_Page", u"11.", None));
        ___qtablewidgetitem23 = self.salary_record.verticalHeaderItem(11)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Employee_Page", u"12.", None));

        __sortingEnabled = self.salary_record.isSortingEnabled()
        self.salary_record.setSortingEnabled(False)
        ___qtablewidgetitem24 = self.salary_record.item(0, 0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Employee_Page", u"January", None));
        ___qtablewidgetitem25 = self.salary_record.item(1, 0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Employee_Page", u"Febuary", None));
        ___qtablewidgetitem26 = self.salary_record.item(2, 0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("Employee_Page", u"March", None));
        ___qtablewidgetitem27 = self.salary_record.item(3, 0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("Employee_Page", u"April", None));
        ___qtablewidgetitem28 = self.salary_record.item(4, 0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("Employee_Page", u"May", None));
        ___qtablewidgetitem29 = self.salary_record.item(5, 0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("Employee_Page", u"June", None));
        ___qtablewidgetitem30 = self.salary_record.item(6, 0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("Employee_Page", u"July", None));
        ___qtablewidgetitem31 = self.salary_record.item(7, 0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("Employee_Page", u"August", None));
        ___qtablewidgetitem32 = self.salary_record.item(8, 0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("Employee_Page", u"September", None));
        ___qtablewidgetitem33 = self.salary_record.item(9, 0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("Employee_Page", u"October", None));
        ___qtablewidgetitem34 = self.salary_record.item(10, 0)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("Employee_Page", u"November", None));
        ___qtablewidgetitem35 = self.salary_record.item(11, 0)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("Employee_Page", u"December", None));
        self.salary_record.setSortingEnabled(__sortingEnabled)

        self.name_input.setText(QCoreApplication.translate("Employee_Page", u"Aatiqa Hussain", None))
        self.department_input_2.setText(QCoreApplication.translate("Employee_Page", u"Accounts", None))
        self.title_2.setText(QCoreApplication.translate("Employee_Page", u"                                Annual Salary Report", None))
        self.name.setText(QCoreApplication.translate("Employee_Page", u"Name :", None))
        self.department_2.setText(QCoreApplication.translate("Employee_Page", u"Department :", None))
        self.description.setText(QCoreApplication.translate("Employee_Page", u"Description", None))
        self.end_date.setText(QCoreApplication.translate("Employee_Page", u"End Date", None))
        self.exp.setText(QCoreApplication.translate("Employee_Page", u"(Explain reason for leave in 2-5 lines.)", None))
        self.category_input.setItemText(0, QCoreApplication.translate("Employee_Page", u"General", None))
        self.category_input.setItemText(1, QCoreApplication.translate("Employee_Page", u"Health", None))

        self.submit_button.setText(QCoreApplication.translate("Employee_Page", u"SUBMIT", None))
        self.category.setText(QCoreApplication.translate("Employee_Page", u"Category", None))
        self.start_date.setText(QCoreApplication.translate("Employee_Page", u"Start Date", None))
        self.title_3.setText(QCoreApplication.translate("Employee_Page", u"                         Leave Application", None))
    # retranslateUi

