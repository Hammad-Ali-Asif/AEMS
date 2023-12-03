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
    QTextEdit, QWidget)

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
        self.Profile_Page_2 = QWidget()
        self.Profile_Page_2.setObjectName(u"Profile_Page_2")
        self.l_name_2 = QGroupBox(self.Profile_Page_2)
        self.l_name_2.setObjectName(u"l_name_2")
        self.l_name_2.setGeometry(QRect(450, 230, 121, 41))
        self.l_name_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_11 = QHBoxLayout(self.l_name_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.address_2 = QGroupBox(self.Profile_Page_2)
        self.address_2.setObjectName(u"address_2")
        self.address_2.setGeometry(QRect(10, 350, 121, 40))
        self.address_2.setMinimumSize(QSize(0, 40))
        self.address_2.setMaximumSize(QSize(16777215, 40))
        self.address_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_13 = QHBoxLayout(self.address_2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.salary_input_2 = QGroupBox(self.Profile_Page_2)
        self.salary_input_2.setObjectName(u"salary_input_2")
        self.salary_input_2.setGeometry(QRect(570, 410, 300, 40))
        self.salary_input_2.setMinimumSize(QSize(300, 40))
        self.salary_input_2.setMaximumSize(QSize(300, 40))
        self.salary_input_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_17 = QHBoxLayout(self.salary_input_2)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.absent_input_2 = QGroupBox(self.Profile_Page_2)
        self.absent_input_2.setObjectName(u"absent_input_2")
        self.absent_input_2.setGeometry(QRect(130, 640, 100, 40))
        self.absent_input_2.setMinimumSize(QSize(100, 40))
        self.absent_input_2.setMaximumSize(QSize(100, 40))
        self.absent_input_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_49 = QHBoxLayout(self.absent_input_2)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.pending_applications_input_2 = QGroupBox(self.Profile_Page_2)
        self.pending_applications_input_2.setObjectName(u"pending_applications_input_2")
        self.pending_applications_input_2.setGeometry(QRect(770, 580, 100, 40))
        self.pending_applications_input_2.setMinimumSize(QSize(100, 40))
        self.pending_applications_input_2.setMaximumSize(QSize(100, 40))
        self.pending_applications_input_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_50 = QHBoxLayout(self.pending_applications_input_2)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.f_name_input_2 = QGroupBox(self.Profile_Page_2)
        self.f_name_input_2.setObjectName(u"f_name_input_2")
        self.f_name_input_2.setGeometry(QRect(130, 230, 320, 40))
        self.f_name_input_2.setMinimumSize(QSize(320, 40))
        self.f_name_input_2.setMaximumSize(QSize(290, 40))
        self.f_name_input_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_18 = QHBoxLayout(self.f_name_input_2)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.f_name_2 = QGroupBox(self.Profile_Page_2)
        self.f_name_2.setObjectName(u"f_name_2")
        self.f_name_2.setGeometry(QRect(10, 230, 121, 40))
        self.f_name_2.setMinimumSize(QSize(0, 40))
        self.f_name_2.setMaximumSize(QSize(16777215, 40))
        self.f_name_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_19 = QHBoxLayout(self.f_name_2)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.l_name_input_2 = QGroupBox(self.Profile_Page_2)
        self.l_name_input_2.setObjectName(u"l_name_input_2")
        self.l_name_input_2.setGeometry(QRect(570, 230, 300, 40))
        self.l_name_input_2.setMinimumSize(QSize(300, 40))
        self.l_name_input_2.setMaximumSize(QSize(300, 40))
        self.l_name_input_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_20 = QHBoxLayout(self.l_name_input_2)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.pending_applications_2 = QGroupBox(self.Profile_Page_2)
        self.pending_applications_2.setObjectName(u"pending_applications_2")
        self.pending_applications_2.setGeometry(QRect(500, 580, 261, 41))
        self.pending_applications_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_51 = QHBoxLayout(self.pending_applications_2)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.salary_4 = QGroupBox(self.Profile_Page_2)
        self.salary_4.setObjectName(u"salary_4")
        self.salary_4.setGeometry(QRect(450, 410, 121, 40))
        self.salary_4.setMinimumSize(QSize(0, 40))
        self.salary_4.setMaximumSize(QSize(16777215, 40))
        self.salary_4.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_21 = QHBoxLayout(self.salary_4)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.email_2 = QGroupBox(self.Profile_Page_2)
        self.email_2.setObjectName(u"email_2")
        self.email_2.setGeometry(QRect(10, 290, 121, 40))
        self.email_2.setMinimumSize(QSize(0, 40))
        self.email_2.setMaximumSize(QSize(16777215, 40))
        self.email_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_22 = QHBoxLayout(self.email_2)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.leave_2 = QGroupBox(self.Profile_Page_2)
        self.leave_2.setObjectName(u"leave_2")
        self.leave_2.setGeometry(QRect(250, 640, 121, 41))
        self.leave_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_52 = QHBoxLayout(self.leave_2)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.name_2 = QTextEdit(self.Profile_Page_2)
        self.name_2.setObjectName(u"name_2")
        self.name_2.setGeometry(QRect(20, 20, 651, 61))
        self.name_2.setMinimumSize(QSize(0, 61))
        self.name_2.setMaximumSize(QSize(16777215, 16777215))
        self.name_2.setStyleSheet(u"color: rgb(44, 72, 97);")
        self.contact_2 = QGroupBox(self.Profile_Page_2)
        self.contact_2.setObjectName(u"contact_2")
        self.contact_2.setGeometry(QRect(450, 290, 121, 41))
        self.contact_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_23 = QHBoxLayout(self.contact_2)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.department_st_2 = QTextEdit(self.Profile_Page_2)
        self.department_st_2.setObjectName(u"department_st_2")
        self.department_st_2.setGeometry(QRect(20, 70, 651, 51))
        self.department_st_2.setMinimumSize(QSize(0, 0))
        self.department_st_2.setMaximumSize(QSize(16777215, 16777215))
        self.department_st_2.setStyleSheet(u"color: rgb(44, 72, 97);")
        self.present_2 = QGroupBox(self.Profile_Page_2)
        self.present_2.setObjectName(u"present_2")
        self.present_2.setGeometry(QRect(250, 580, 121, 41))
        self.present_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_53 = QHBoxLayout(self.present_2)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.current_deduction_2 = QGroupBox(self.Profile_Page_2)
        self.current_deduction_2.setObjectName(u"current_deduction_2")
        self.current_deduction_2.setGeometry(QRect(500, 640, 261, 41))
        self.current_deduction_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_54 = QHBoxLayout(self.current_deduction_2)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.contact_input_2 = QGroupBox(self.Profile_Page_2)
        self.contact_input_2.setObjectName(u"contact_input_2")
        self.contact_input_2.setGeometry(QRect(570, 290, 300, 40))
        self.contact_input_2.setMinimumSize(QSize(300, 40))
        self.contact_input_2.setMaximumSize(QSize(300, 40))
        self.contact_input_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_24 = QHBoxLayout(self.contact_input_2)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.general_info_2 = QTextEdit(self.Profile_Page_2)
        self.general_info_2.setObjectName(u"general_info_2")
        self.general_info_2.setGeometry(QRect(0, 150, 921, 51))
        self.general_info_2.setStyleSheet(u"background-color: rgb(50, 82, 110);\n"
"color: rgb(230, 230, 230);")
        self.email_input_2 = QGroupBox(self.Profile_Page_2)
        self.email_input_2.setObjectName(u"email_input_2")
        self.email_input_2.setGeometry(QRect(130, 290, 320, 40))
        self.email_input_2.setMinimumSize(QSize(320, 40))
        self.email_input_2.setMaximumSize(QSize(320, 40))
        self.email_input_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_25 = QHBoxLayout(self.email_input_2)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.month_details_2 = QTextEdit(self.Profile_Page_2)
        self.month_details_2.setObjectName(u"month_details_2")
        self.month_details_2.setGeometry(QRect(0, 510, 921, 51))
        self.month_details_2.setStyleSheet(u"background-color: rgb(50, 82, 110);\n"
"color: rgb(230, 230, 230);")
        self.department_2 = QGroupBox(self.Profile_Page_2)
        self.department_2.setObjectName(u"department_2")
        self.department_2.setGeometry(QRect(10, 410, 121, 40))
        self.department_2.setMinimumSize(QSize(0, 40))
        self.department_2.setMaximumSize(QSize(16777215, 40))
        self.department_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_26 = QHBoxLayout(self.department_2)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.current_deduction_input_2 = QGroupBox(self.Profile_Page_2)
        self.current_deduction_input_2.setObjectName(u"current_deduction_input_2")
        self.current_deduction_input_2.setGeometry(QRect(770, 640, 100, 40))
        self.current_deduction_input_2.setMinimumSize(QSize(100, 40))
        self.current_deduction_input_2.setMaximumSize(QSize(100, 40))
        self.current_deduction_input_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_55 = QHBoxLayout(self.current_deduction_input_2)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.department_input_2 = QGroupBox(self.Profile_Page_2)
        self.department_input_2.setObjectName(u"department_input_2")
        self.department_input_2.setGeometry(QRect(130, 410, 320, 40))
        self.department_input_2.setMinimumSize(QSize(320, 40))
        self.department_input_2.setMaximumSize(QSize(320, 40))
        self.department_input_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_27 = QHBoxLayout(self.department_input_2)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.leave_input_2 = QGroupBox(self.Profile_Page_2)
        self.leave_input_2.setObjectName(u"leave_input_2")
        self.leave_input_2.setGeometry(QRect(370, 640, 100, 40))
        self.leave_input_2.setMinimumSize(QSize(100, 40))
        self.leave_input_2.setMaximumSize(QSize(100, 40))
        self.leave_input_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_56 = QHBoxLayout(self.leave_input_2)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.absent_2 = QGroupBox(self.Profile_Page_2)
        self.absent_2.setObjectName(u"absent_2")
        self.absent_2.setGeometry(QRect(10, 640, 121, 40))
        self.absent_2.setMinimumSize(QSize(0, 40))
        self.absent_2.setMaximumSize(QSize(16777215, 40))
        self.absent_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_57 = QHBoxLayout(self.absent_2)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.address_input_2 = QGroupBox(self.Profile_Page_2)
        self.address_input_2.setObjectName(u"address_input_2")
        self.address_input_2.setGeometry(QRect(130, 350, 750, 40))
        self.address_input_2.setMinimumSize(QSize(750, 40))
        self.address_input_2.setMaximumSize(QSize(750, 40))
        self.address_input_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_28 = QHBoxLayout(self.address_input_2)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.present_input_2 = QGroupBox(self.Profile_Page_2)
        self.present_input_2.setObjectName(u"present_input_2")
        self.present_input_2.setGeometry(QRect(370, 580, 100, 40))
        self.present_input_2.setMinimumSize(QSize(100, 40))
        self.present_input_2.setMaximumSize(QSize(100, 40))
        self.present_input_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_58 = QHBoxLayout(self.present_input_2)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.total_days_2 = QGroupBox(self.Profile_Page_2)
        self.total_days_2.setObjectName(u"total_days_2")
        self.total_days_2.setGeometry(QRect(10, 580, 121, 40))
        self.total_days_2.setMinimumSize(QSize(0, 40))
        self.total_days_2.setMaximumSize(QSize(16777215, 40))
        self.total_days_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_59 = QHBoxLayout(self.total_days_2)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.total_days_input_2 = QGroupBox(self.Profile_Page_2)
        self.total_days_input_2.setObjectName(u"total_days_input_2")
        self.total_days_input_2.setGeometry(QRect(130, 580, 100, 40))
        self.total_days_input_2.setMinimumSize(QSize(100, 40))
        self.total_days_input_2.setMaximumSize(QSize(100, 40))
        self.total_days_input_2.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_60 = QHBoxLayout(self.total_days_input_2)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.Pages.addWidget(self.Profile_Page_2)
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
        self.l_name_2.setTitle(QCoreApplication.translate("Employee_Page", u"Last Name", None))
        self.address_2.setTitle(QCoreApplication.translate("Employee_Page", u"Address", None))
        self.salary_input_2.setTitle(QCoreApplication.translate("Employee_Page", u"Rs. 355000", None))
        self.absent_input_2.setTitle(QCoreApplication.translate("Employee_Page", u"2", None))
        self.pending_applications_input_2.setTitle(QCoreApplication.translate("Employee_Page", u"1", None))
        self.f_name_input_2.setTitle(QCoreApplication.translate("Employee_Page", u"Aatiqa", None))
        self.f_name_2.setTitle(QCoreApplication.translate("Employee_Page", u"First Name", None))
        self.l_name_input_2.setTitle(QCoreApplication.translate("Employee_Page", u"Hussain", None))
        self.pending_applications_2.setTitle(QCoreApplication.translate("Employee_Page", u"Pending Leave Applications", None))
        self.salary_4.setTitle(QCoreApplication.translate("Employee_Page", u"Salary", None))
        self.email_2.setTitle(QCoreApplication.translate("Employee_Page", u"Email", None))
        self.leave_2.setTitle(QCoreApplication.translate("Employee_Page", u"Leave", None))
        self.name_2.setHtml(QCoreApplication.translate("Employee_Page", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:28pt; font-weight:696;\">Aatiqa Hussain</span></p></body></html>", None))
        self.contact_2.setTitle(QCoreApplication.translate("Employee_Page", u"Contact", None))
        self.department_st_2.setHtml(QCoreApplication.translate("Employee_Page", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:16pt;\">Accounts Department</span></p></body></html>", None))
        self.present_2.setTitle(QCoreApplication.translate("Employee_Page", u"Present", None))
        self.current_deduction_2.setTitle(QCoreApplication.translate("Employee_Page", u"Current Salary Deduction", None))
        self.contact_input_2.setTitle(QCoreApplication.translate("Employee_Page", u"0333-8629629", None))
        self.general_info_2.setHtml(QCoreApplication.translate("Employee_Page", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:20pt; font-weight:696;\">General Information</span></p></body></html>", None))
        self.email_input_2.setTitle(QCoreApplication.translate("Employee_Page", u"aatiqahussain@gmail.com", None))
        self.month_details_2.setHtml(QCoreApplication.translate("Employee_Page", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:20pt; font-weight:696;\">Current Month Details</span></p></body></html>", None))
        self.department_2.setTitle(QCoreApplication.translate("Employee_Page", u"Department", None))
        self.current_deduction_input_2.setTitle(QCoreApplication.translate("Employee_Page", u"Rs. 23666", None))
        self.department_input_2.setTitle(QCoreApplication.translate("Employee_Page", u"Accounts", None))
        self.leave_input_2.setTitle(QCoreApplication.translate("Employee_Page", u"1", None))
        self.absent_2.setTitle(QCoreApplication.translate("Employee_Page", u"Absent", None))
        self.address_input_2.setTitle(QCoreApplication.translate("Employee_Page", u"852-B Milaad Street, Faisal Town, Lahore", None))
        self.present_input_2.setTitle(QCoreApplication.translate("Employee_Page", u"21", None))
        self.total_days_2.setTitle(QCoreApplication.translate("Employee_Page", u"Total Days", None))
        self.total_days_input_2.setTitle(QCoreApplication.translate("Employee_Page", u"24", None))
    # retranslateUi

