from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,QTimer)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QToolBox,
QWidget,QMessageBox,QTableWidget, QTableWidgetItem,QVBoxLayout,QItemDelegate,QSpinBox,QDateEdit,QAbstractItemView,QTextEdit,QDialog,QHBoxLayout)

import psycopg2
import login_page
class SideBar(QGroupBox):
    def __init__(self,Page,employee_instance):
        super(SideBar, self).__init__(Page)
        self.employee=employee_instance
        self.setObjectName("side_bar")
        self.setGeometry(0, 0, 350, 722)
        self.setMinimumSize(350, 722)
        self.setMaximumSize(350, 722)
        self.setStyleSheet("background-color: rgb(50, 82, 110);")
        self.logo = QLabel(self)
        self.logo.setObjectName(u"logo ")
        self.logo.setGeometry(QRect(0, 20, 341, 191))
        self.logo.setPixmap(QPixmap(u"Images/logo-grey.png"))
        self.logo.setScaledContents(True)
        self.profile = QPushButton(self)
        self.profile.setObjectName(u"profile")
        self.profile.setGeometry(QRect(0, 470, 348, 65))
        self.profile.setMinimumSize(QSize(348, 65))
        self.profile.setMaximumSize(QSize(348, 65))
        self.profile.setCursor(QCursor(Qt.PointingHandCursor))
        self.profile.setStyleSheet(u"font: 20pt \"Sitka\" rgb(255, 255, 255);\n"
"color: rgb(230, 230, 230);")
        self.leave_report = QPushButton(self)
        self.leave_report.setObjectName(u"leave_report")
        self.leave_report.setGeometry(QRect(0, 210, 348, 65))
        self.leave_report.setMinimumSize(QSize(348, 65))
        self.leave_report.setMaximumSize(QSize(348, 65))
        self.leave_report.setCursor(QCursor(Qt.PointingHandCursor))
        self.leave_report.setStyleSheet(u"font: 20pt \"Sitka\";\n"
"color: rgb(230, 230, 230);")
        self.leave_application = QPushButton(self)
        self.leave_application.setObjectName(u"leave_application")
        self.leave_application.setGeometry(QRect(0, 405, 348, 65))
        self.leave_application.setMinimumSize(QSize(348, 65))
        self.leave_application.setMaximumSize(QSize(348, 65))
        self.leave_application.setCursor(QCursor(Qt.PointingHandCursor))
        self.leave_application.setStyleSheet(u"font: 20pt \"Sitka\" rgb(255, 255, 255);\n"
"color: rgb(230, 230, 230);")
        self.salary_3 = QPushButton(self)
        self.salary_3.setObjectName(u"salary_3")
        self.salary_3.setGeometry(QRect(0, 275, 348, 65))
        self.salary_3.setMinimumSize(QSize(348, 65))
        self.salary_3.setMaximumSize(QSize(348, 65))
        self.salary_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.salary_3.setStyleSheet(u"font: 20pt \"Sitka\" rgb(255, 255, 255);\n"
"color: rgb(230, 230, 230);")
        self.attendance = QPushButton(self)
        self.attendance.setObjectName(u"attendance")
        self.attendance.setGeometry(QRect(0, 340, 348, 65))
        self.attendance.setMinimumSize(QSize(348, 65))
        self.attendance.setMaximumSize(QSize(348, 65))
        self.attendance.setCursor(QCursor(Qt.PointingHandCursor))
        self.attendance.setStyleSheet(u"font: 20pt \"Sitka\" rgb(255, 255, 255);\n"
"color: rgb(230, 230, 230);")
        self.sign_out = QPushButton(self)
        self.sign_out.setObjectName(u"sign_out")
        self.sign_out.setGeometry(QRect(0, 660, 348, 65))
        self.sign_out.setMinimumSize(QSize(348, 65))
        self.sign_out.setMaximumSize(QSize(348, 65))
        self.sign_out.setCursor(QCursor(Qt.PointingHandCursor))
        self.sign_out.setStyleSheet(u"font: italic 18pt \"Sitka\" rgb(255, 255, 255);\n"
"color: rgb(230, 230, 230);")
        icon = QIcon()
        icon.addFile(u"Images/sign out-grey.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u"Images/sign out-grey.png", QSize(), QIcon.Normal, QIcon.On)
        self.sign_out.setIcon(icon)
        self.sign_out.setIconSize(QSize(30, 30))
        self.sign_out.clicked.connect(self.employee.signout)
    
    

        


class Profile(QWidget):
    def __init__(self,Page,id):
        super(Profile, self).__init__(Page)
        self.emp_id=id
        self.setObjectName(u"Profile_Page")
        self.l_name = QGroupBox(self)
        self.l_name.setObjectName(u"l_name")
        self.l_name.setGeometry(QRect(450, 230, 121, 41))
        self.l_name.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_11 = QHBoxLayout(self.l_name)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.address = QGroupBox(self)
        self.address.setObjectName(u"address")
        self.address.setGeometry(QRect(10, 350, 121, 40))
        self.address.setMinimumSize(QSize(0, 40))
        self.address.setMaximumSize(QSize(16777215, 40))
        self.address.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_13 = QHBoxLayout(self.address)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.salary_input = QGroupBox(self)
        self.salary_input.setObjectName(u"salary_input")
        self.salary_input.setGeometry(QRect(570, 410, 300, 40))
        self.salary_input.setMinimumSize(QSize(300, 40))
        self.salary_input.setMaximumSize(QSize(300, 40))
        self.salary_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_17 = QHBoxLayout(self.salary_input)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.absent_input = QGroupBox(self)
        self.absent_input.setObjectName(u"absent_input")
        self.absent_input.setGeometry(QRect(130, 640, 100, 40))
        self.absent_input.setMinimumSize(QSize(100, 40))
        self.absent_input.setMaximumSize(QSize(100, 40))
        self.absent_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_49 = QHBoxLayout(self.absent_input)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.pending_applications_input = QGroupBox(self)
        self.pending_applications_input.setObjectName(u"pending_applications_input")
        self.pending_applications_input.setGeometry(QRect(770, 580, 100, 40))
        self.pending_applications_input.setMinimumSize(QSize(100, 40))
        self.pending_applications_input.setMaximumSize(QSize(100, 40))
        self.pending_applications_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_50 = QHBoxLayout(self.pending_applications_input)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.f_name_input = QGroupBox(self)
        self.f_name_input.setObjectName(u"f_name_input")
        self.f_name_input.setGeometry(QRect(130, 230, 320, 40))
        self.f_name_input.setMinimumSize(QSize(320, 40))
        self.f_name_input.setMaximumSize(QSize(290, 40))
        self.f_name_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_18 = QHBoxLayout(self.f_name_input)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.f_name = QGroupBox(self)
        self.f_name.setObjectName(u"f_name")
        self.f_name.setGeometry(QRect(10, 230, 121, 40))
        self.f_name.setMinimumSize(QSize(0, 40))
        self.f_name.setMaximumSize(QSize(16777215, 40))
        self.f_name.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_19 = QHBoxLayout(self.f_name)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.l_name_input = QGroupBox(self)
        self.l_name_input.setObjectName(u"l_name_input")
        self.l_name_input.setGeometry(QRect(570, 230, 300, 40))
        self.l_name_input.setMinimumSize(QSize(300, 40))
        self.l_name_input.setMaximumSize(QSize(300, 40))
        self.l_name_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout0 = QHBoxLayout(self.l_name_input)
        self.horizontalLayout0.setObjectName(u"horizontalLayout0")
        self.pending_applications = QGroupBox(self)
        self.pending_applications.setObjectName(u"pending_applications")
        self.pending_applications.setGeometry(QRect(500, 580, 261, 41))
        self.pending_applications.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_51 = QHBoxLayout(self.pending_applications)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.salary_4 = QGroupBox(self)
        self.salary_4.setObjectName(u"salary_4")
        self.salary_4.setGeometry(QRect(450, 410, 121, 40))
        self.salary_4.setMinimumSize(QSize(0, 40))
        self.salary_4.setMaximumSize(QSize(16777215, 40))
        self.salary_4.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout1 = QHBoxLayout(self.salary_4)
        self.horizontalLayout1.setObjectName(u"horizontalLayout1")
        self.email = QGroupBox(self)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(10, 290, 121, 40))
        self.email.setMinimumSize(QSize(0, 40))
        self.email.setMaximumSize(QSize(16777215, 40))
        self.email.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout2 = QHBoxLayout(self.email)
        self.horizontalLayout2.setObjectName(u"horizontalLayout2")
        self.leave = QGroupBox(self)
        self.leave.setObjectName(u"leave")
        self.leave.setGeometry(QRect(250, 640, 121, 41))
        self.leave.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_52 = QHBoxLayout(self.leave)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.name = QTextEdit(self)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(20, 20, 651, 61))
        self.name.setMinimumSize(QSize(0, 61))
        self.name.setMaximumSize(QSize(16777215, 16777215))
        self.name.setStyleSheet(u"color: rgb(44, 72, 97);")
        self.contact = QGroupBox(self)
        self.contact.setObjectName(u"contact")
        self.contact.setGeometry(QRect(450, 290, 121, 41))
        self.contact.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout3 = QHBoxLayout(self.contact)
        self.horizontalLayout3.setObjectName(u"horizontalLayout3")
        self.department_st = QTextEdit(self)
        self.department_st.setObjectName(u"department_st")
        self.department_st.setGeometry(QRect(20, 70, 651, 51))
        self.department_st.setMinimumSize(QSize(0, 0))
        self.department_st.setMaximumSize(QSize(16777215, 16777215))
        self.department_st.setStyleSheet(u"color: rgb(44, 72, 97);")
        self.present = QGroupBox(self)
        self.present.setObjectName(u"present")
        self.present.setGeometry(QRect(250, 580, 121, 41))
        self.present.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_53 = QHBoxLayout(self.present)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.current_deduction = QGroupBox(self)
        self.current_deduction.setObjectName(u"current_deduction")
        self.current_deduction.setGeometry(QRect(500, 640, 261, 41))
        self.current_deduction.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_54 = QHBoxLayout(self.current_deduction)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.contact_input = QGroupBox(self)
        self.contact_input.setObjectName(u"contact_input")
        self.contact_input.setGeometry(QRect(570, 290, 300, 40))
        self.contact_input.setMinimumSize(QSize(300, 40))
        self.contact_input.setMaximumSize(QSize(300, 40))
        self.contact_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout4 = QHBoxLayout(self.contact_input)
        self.horizontalLayout4.setObjectName(u"horizontalLayout4")
        self.general_info = QTextEdit(self)
        self.general_info.setObjectName(u"general_info")
        self.general_info.setGeometry(QRect(0, 150, 921, 51))
        self.general_info.setStyleSheet(u"background-color: rgb(50, 82, 110);\n"
"color: rgb(230, 230, 230);")
        self.email_input = QGroupBox(self)
        self.email_input.setObjectName(u"email_input")
        self.email_input.setGeometry(QRect(130, 290, 320, 40))
        self.email_input.setMinimumSize(QSize(320, 40))
        self.email_input.setMaximumSize(QSize(320, 40))
        self.email_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout5 = QHBoxLayout(self.email_input)
        self.horizontalLayout5.setObjectName(u"horizontalLayout5")
        self.month_details = QTextEdit(self)
        self.month_details.setObjectName(u"month_details")
        self.month_details.setGeometry(QRect(0, 510, 921, 51))
        self.month_details.setStyleSheet(u"background-color: rgb(50, 82, 110);\n"
"color: rgb(230, 230, 230);")
        self.department = QGroupBox(self)
        self.department.setObjectName(u"department")
        self.department.setGeometry(QRect(10, 410, 121, 40))
        self.department.setMinimumSize(QSize(0, 40))
        self.department.setMaximumSize(QSize(16777215, 40))
        self.department.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout6 = QHBoxLayout(self.department)
        self.horizontalLayout6.setObjectName(u"horizontalLayout6")
        self.current_deduction_input = QGroupBox(self)
        self.current_deduction_input.setObjectName(u"current_deduction_input")
        self.current_deduction_input.setGeometry(QRect(770, 640, 100, 40))
        self.current_deduction_input.setMinimumSize(QSize(100, 40))
        self.current_deduction_input.setMaximumSize(QSize(100, 40))
        self.current_deduction_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_55 = QHBoxLayout(self.current_deduction_input)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.department_input = QGroupBox(self)
        self.department_input.setObjectName(u"department_input")
        self.department_input.setGeometry(QRect(130, 410, 320, 40))
        self.department_input.setMinimumSize(QSize(320, 40))
        self.department_input.setMaximumSize(QSize(320, 40))
        self.department_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout7 = QHBoxLayout(self.department_input)
        self.horizontalLayout7.setObjectName(u"horizontalLayout7")
        self.leave_input = QGroupBox(self)
        self.leave_input.setObjectName(u"leave_input")
        self.leave_input.setGeometry(QRect(370, 640, 100, 40))
        self.leave_input.setMinimumSize(QSize(100, 40))
        self.leave_input.setMaximumSize(QSize(100, 40))
        self.leave_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_56 = QHBoxLayout(self.leave_input)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.absent = QGroupBox(self)
        self.absent.setObjectName(u"absent")
        self.absent.setGeometry(QRect(10, 640, 121, 40))
        self.absent.setMinimumSize(QSize(0, 40))
        self.absent.setMaximumSize(QSize(16777215, 40))
        self.absent.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_57 = QHBoxLayout(self.absent)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.address_input = QGroupBox(self)
        self.address_input.setObjectName(u"address_input")
        self.address_input.setGeometry(QRect(130, 350, 750, 40))
        self.address_input.setMinimumSize(QSize(750, 40))
        self.address_input.setMaximumSize(QSize(750, 40))
        self.address_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout8 = QHBoxLayout(self.address_input)
        self.horizontalLayout8.setObjectName(u"horizontalLayout8")
        self.present_input = QGroupBox(self)
        self.present_input.setObjectName(u"present_input")
        self.present_input.setGeometry(QRect(370, 580, 100, 40))
        self.present_input.setMinimumSize(QSize(100, 40))
        self.present_input.setMaximumSize(QSize(100, 40))
        self.present_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_58 = QHBoxLayout(self.present_input)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.total_days = QGroupBox(self)
        self.total_days.setObjectName(u"total_days")
        self.total_days.setGeometry(QRect(10, 580, 121, 40))
        self.total_days.setMinimumSize(QSize(0, 40))
        self.total_days.setMaximumSize(QSize(16777215, 40))
        self.total_days.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_59 = QHBoxLayout(self.total_days)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.total_days_input = QGroupBox(self)
        self.total_days_input.setObjectName(u"total_days_input")
        self.total_days_input.setGeometry(QRect(130, 580, 100, 40))
        self.total_days_input.setMinimumSize(QSize(100, 40))
        self.total_days_input.setMaximumSize(QSize(100, 40))
        self.total_days_input.setStyleSheet(u"color: rgb(50, 84, 110);\n"
"font: 14pt \"Segoe UI\";\n"
"")
        self.horizontalLayout_60 = QHBoxLayout(self.total_days_input)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.load_employee_data(self.emp_id)
        
    def load_employee_data(self, employee_id):
        # Connect to the PostgreSQL database
        db_connection = psycopg2.connect(
            user="postgres",
            password="12345678",
            host="localhost",
            port="5432",
            database="AEMS"
        )

        # Create a cursor object to interact with the database
        cursor = db_connection.cursor()

        # Fetch employee data based on the provided employee_id
        query = f"SELECT * FROM Employee WHERE id = '{employee_id}';"
        cursor.execute(query)
        employee_data = cursor.fetchone()

        # Close the cursor and database connection
        cursor.close()
        db_connection.close()

        if employee_data:
            # Update the profile page with the retrieved data
            self.name.setPlainText(f"{employee_data[2]} {employee_data[3]}")
            self.department_st.setPlainText(employee_data[1])
            self.f_name_input.setTitle(QCoreApplication.translate("Employee_Page", employee_data[2], None))
            self.l_name_input.setTitle(QCoreApplication.translate("Employee_Page", employee_data[3], None))
            self.address_input.setTitle(QCoreApplication.translate("Employee_Page", employee_data[5], None))
            self.contact_input.setTitle(QCoreApplication.translate("Employee_Page", employee_data[4], None))
            self.email_input.setTitle(QCoreApplication.translate("Employee_Page", employee_data[6], None))
            self.salary_input.setTitle(QCoreApplication.translate("Employee_Page", employee_data[8], None))

class EmployeePage(QDialog):
    def __init__(self,id):
        super(EmployeePage, self).__init__()
        self.emp_id=id
        self.setObjectName(u" Employee_Page")
        self.resize(1280, 720)
        self.setMinimumSize(QSize(1280, 720))
        self.setMaximumSize(QSize(1280, 720))
        self.PAGE = QWidget(self)
        self.PAGE.setObjectName(u"PAGE")

        self.side_bar=SideBar(self.PAGE,self)
        self.Main_pages = QStackedWidget(self.PAGE)
        self.Main_pages.setObjectName(u"Main_pages")
        self.Main_pages.setEnabled(True)
        self.Main_pages.setGeometry(QRect(350, 0, 930, 720))
        self.Main_pages.setMinimumSize(QSize(930, 720))
        self.Profile_page = Profile(self.PAGE,self.emp_id)
        self.Main_pages.addWidget(self.Profile_page)
        self.retranslateUi()
    
    def signout(self):
        self.close()
        login=login_page.LoginPage()
        login.show()
        login.exec_()

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Employee_Page", u"MainWindow", None))
        self.side_bar.setTitle("")
        self.side_bar.logo.setText("")
        self.side_bar.profile.setText(QCoreApplication.translate("Employee_Page", u"Leave Application", None))
        self.side_bar.leave_report.setText(QCoreApplication.translate("Employee_Page", u"Profile", None))
        self.side_bar.leave_application.setText(QCoreApplication.translate("Employee_Page", u"Salary", None))
        self.side_bar.salary_3.setText(QCoreApplication.translate("Employee_Page", u"Leave Report", None))
        self.side_bar.attendance.setText(QCoreApplication.translate("Employee_Page", u"Attendance", None))
        self.side_bar.sign_out.setText(QCoreApplication.translate("Employee_Page", u"  Sign Out ", None))
        self.Profile_page.l_name.setTitle(QCoreApplication.translate("Employee_Page", u"Last Name", None))
        self.Profile_page.address.setTitle(QCoreApplication.translate("Employee_Page", u"Address", None))
        
        self.Profile_page.absent_input.setTitle(QCoreApplication.translate("Employee_Page", u"2", None))
        self.Profile_page.pending_applications_input.setTitle(QCoreApplication.translate("Employee_Page", u"1", None))
       
        self.Profile_page.f_name.setTitle(QCoreApplication.translate("Employee_Page", u"First Name", None))
        
        self.Profile_page.pending_applications.setTitle(QCoreApplication.translate("Employee_Page", u"Pending Leave Applications", None))
        self.Profile_page.salary_4.setTitle(QCoreApplication.translate("Employee_Page", u"Salary", None))
        self.Profile_page.email.setTitle(QCoreApplication.translate("Employee_Page", u"Email", None))
        self.Profile_page.leave.setTitle(QCoreApplication.translate("Employee_Page", u"Leave", None))
        self.Profile_page.name.setHtml(QCoreApplication.translate("Employee_Page", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:28pt; font-weight:696;\">Aatiqa Hussain</span></p></body></html>", None))
        self.Profile_page.contact.setTitle(QCoreApplication.translate("Employee_Page", u"Contact", None))
        self.Profile_page.department_st.setHtml(QCoreApplication.translate("Employee_Page", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:16pt;\">Accounts Department</span></p></body></html>", None))
        self.Profile_page.present.setTitle(QCoreApplication.translate("Employee_Page", u"Present", None))
        self.Profile_page.current_deduction.setTitle(QCoreApplication.translate("Employee_Page", u"Current Salary Deduction", None))
        
        self.Profile_page.general_info.setHtml(QCoreApplication.translate("Employee_Page", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:20pt; font-weight:696;\">General Information</span></p></body></html>", None))
        
        self.Profile_page.month_details.setHtml(QCoreApplication.translate("Employee_Page", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:20pt; font-weight:696;\">Current Month Details</span></p></body></html>", None))
        self.Profile_page.department.setTitle(QCoreApplication.translate("Employee_Page", u"Department", None))
        self.Profile_page.current_deduction_input.setTitle(QCoreApplication.translate("Employee_Page", u"Rs. 23666", None))
        self.Profile_page.department_input.setTitle(QCoreApplication.translate("Employee_Page", u"Accounts", None))
        self.Profile_page.leave_input.setTitle(QCoreApplication.translate("Employee_Page", u"1", None))
        self.Profile_page.absent.setTitle(QCoreApplication.translate("Employee_Page", u"Absent", None))
        
        self.Profile_page.present_input.setTitle(QCoreApplication.translate("Employee_Page", u"21", None))
        self.Profile_page.total_days.setTitle(QCoreApplication.translate("Employee_Page", u"Total Days", None))
        self.Profile_page.total_days_input.setTitle(QCoreApplication.translate("Employee_Page", u"24", None))
        
    

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    global window
    window =  EmployeePage('7')
    window.show()
    sys.exit(app.exec_())
