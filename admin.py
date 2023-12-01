from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QToolBox,
    QWidget,QMessageBox,QTableWidget, QTableWidgetItem,QVBoxLayout)
import re
import psycopg2
def is_valid_email(email):
    # Define a regular expression pattern for a basic email validation
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # Use re.match to check if the email matches the pattern
    match = re.match(pattern, email)

    # If there is a match, the email is valid
    return match is not None

class Sidebar(QGroupBox):
    def __init__(self,Page):
        super(Sidebar, self).__init__(Page)
        self.setObjectName(u"side_bar")
        self.setGeometry(0, -10, 291, 731)
        self.setStyleSheet(u"background-color: rgb(88, 55, 89);")

        self.Dashboard_button = QPushButton(self)
        self.Dashboard_button.setObjectName(u"Dashboard_button")
        self.Dashboard_button.setGeometry(QRect(-10, 137, 301, 81))
        font = QFont()
        font.setFamilies([u"Book Antiqua"])
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        self.Dashboard_button.setFont(font)
        self.Dashboard_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.Dashboard_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                            
"font: 15pt \"Book Antiqua\";")
        icon = QIcon()
        icon.addFile(u"Images/Dashboard.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Dashboard_button.setIcon(icon)
        self.Dashboard_button.setIconSize(QSize(25, 25))
        

        self.attendance = QPushButton(self)
        self.attendance.setObjectName(u"attendance")
        self.attendance.setGeometry(QRect(0, 218, 291, 81))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.attendance.setFont(font1)
        self.attendance.setCursor(QCursor(Qt.PointingHandCursor))
        self.attendance.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u"Images/attendance.png", QSize(), QIcon.Normal, QIcon.Off)
        self.attendance.setIcon(icon1)
        self.attendance.setIconSize(QSize(25, 25))
        self.attendance.setAutoDefault(False)
        self.attendance.setFlat(False)


        self.EandL = QToolBox(self)
        self.EandL.setObjectName(u"EandL")
        self.EandL.setEnabled(True)
        self.EandL.setGeometry(QRect(0, 300, 291, 350))
        self.EandL.setMinimumSize(QSize(250, 300))
        self.EandL.setMaximumSize(QSize(300, 350))
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.EandL.setFont(font2)
        self.EandL.setCursor(QCursor(Qt.PointingHandCursor))
        self.EandL.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.EandL.setFrameShape(QFrame.NoFrame)
        self.EandL.setFrameShadow(QFrame.Plain)
        self.EandL.setLineWidth(0)
        self.Employee = QWidget()
        self.Employee.setObjectName(u"Employee")
        self.Employee.setGeometry(QRect(0, 0, 291, 256))
        self.list_employee = QPushButton(self.Employee)
        self.list_employee.setObjectName(u"list_employee")
        self.list_employee.setGeometry(QRect(0, 0, 291, 71))
        font3 = QFont()
        font3.setPointSize(15)
        self.list_employee.setFont(font3)
        self.list_employee.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"Images/list.png", QSize(), QIcon.Normal, QIcon.Off)
        self.list_employee.setIcon(icon2)
        self.list_employee.setIconSize(QSize(30, 30))
        self.Add_employee = QPushButton(self.Employee)
        self.Add_employee.setObjectName(u"Add_employee")
        self.Add_employee.setGeometry(QRect(0, 70, 291, 81))
        self.Add_employee.setFont(font3)
        self.Add_employee.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"Images/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Add_employee.setIcon(icon3)
        self.Add_employee.setIconSize(QSize(30, 30))
        self.Remove_employee = QPushButton(self.Employee)
        self.Remove_employee.setObjectName(u"Remove_employee")
        self.Remove_employee.setGeometry(QRect(0, 150, 291, 71))
        self.Remove_employee.setFont(font3)
        self.Remove_employee.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"Images/remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Remove_employee.setIcon(icon4)
        self.Remove_employee.setIconSize(QSize(30, 30))
        icon5 = QIcon()
        icon5.addFile(u"Images/Employee.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.EandL.addItem(self.Employee, icon5, u"Employee")
        self.Leave = QWidget()
        self.Leave.setObjectName(u"Leave")
        self.Leave.setGeometry(QRect(0, 0, 291, 256))
        self.Pending = QPushButton(self.Leave)
        self.Pending.setObjectName(u"Pending")
        self.Pending.setGeometry(QRect(0, 0, 291, 81))
        self.Pending.setFont(font3)
        self.Pending.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u"Images/pending.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Pending.setIcon(icon6)
        self.Pending.setIconSize(QSize(30, 30))
        self.Approve = QPushButton(self.Leave)
        self.Approve.setObjectName(u"Approve")
        self.Approve.setGeometry(QRect(0, 80, 291, 81))
        self.Approve.setFont(font3)
        self.Approve.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u"Images/approve.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Approve.setIcon(icon7)
        self.Approve.setIconSize(QSize(30, 30))
        self.Decline = QPushButton(self.Leave)
        self.Decline.setObjectName(u"Decline")
        self.Decline.setGeometry(QRect(0, 160, 291, 81))
        self.Decline.setFont(font3)
        self.Decline.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u"Images/decline.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Decline.setIcon(icon8)
        self.Decline.setIconSize(QSize(30, 30))
        icon9 = QIcon()
        icon9.addFile(u"Images/leave.png", QSize(), QIcon.Normal, QIcon.Off)
        self.EandL.addItem(self.Leave, icon9, u"Leave")
        self.Logo = QLabel(self)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setGeometry(QRect(0, 10, 290, 131))
        self.Logo.setPixmap(QPixmap(u"Images/logo.png"))
        self.Logo.setScaledContents(True)
    def setup_connections(self, stacked_widget):
        # Connect the Dashboard_button click signal to show_dashboard_page function
        self.Dashboard_button.clicked.connect(lambda: stacked_widget.setCurrentIndex(0))
        self.list_employee.clicked.connect(lambda:stacked_widget.setCurrentIndex(1))
        self.Add_employee.clicked.connect(lambda: stacked_widget.setCurrentIndex(2))
        

class Add_Employee_page(QWidget):
    def __init__(self,Page):
        super(Add_Employee_page, self).__init__(Page)

        self.setObjectName(u"AddEmployee_Page")
        self.new_employee_title_bar = QGroupBox(self)
        self.new_employee_title_bar.setObjectName(u"new_employee_title_bar")
        self.new_employee_title_bar.setGeometry(QRect(0, 20, 991, 80))
        self.new_employee_title_bar.setStyleSheet(u"background-color: rgb(88, 55, 89);")
        self.new_employee_text = QLabel(self.new_employee_title_bar)
        self.new_employee_text.setObjectName(u"new_employee_text")
        self.new_employee_text.setGeometry(QRect(33, 22, 261, 31))
        font10 = QFont()
        font10.setPointSize(18)
        self.new_employee_text.setFont(font10)
        self.new_employee_text.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Department = QComboBox(self)
        self.Department.addItem("")
        self.Department.addItem("")
        self.Department.addItem("")
        self.Department.addItem("")
        self.Department.addItem("")
        self.Department.setObjectName(u"Department")
        self.Department.setGeometry(QRect(210, 160, 210, 30))
        font6=QFont()
        font6.setPointSize(13)
        self.Department.setFont(font6)
        self.Department.setStyleSheet(u"border:1px solid;\n"
"border-radius:15px;")
        self.Employee_id = QLineEdit(self)
        self.Employee_id.setObjectName(u"Employee_id")
        self.Employee_id.setGeometry(QRect(660, 160, 210, 30))
        self.Employee_id.setStyleSheet(u"border:1px solid;\n"
"border-radius:15px;\n"
"")
        self.Contact = QLineEdit(self)
        self.Contact.setObjectName(u"Contact")
        self.Contact.setGeometry(QRect(210, 380, 211, 31))
        self.Contact.setStyleSheet(u"border:1px solid;\n"
"border-radius:15px;\n"
"")
        self.Lname = QLineEdit(self)
        self.Lname.setObjectName(u"Lname")
        self.Lname.setGeometry(QRect(660, 270, 211, 31))
        self.Lname.setStyleSheet(u"border:1px solid;\n"
"border-radius:15px;\n"
"")
        self.Fname = QLineEdit(self )
        self.Fname.setObjectName(u"Fname")
        self.Fname.setGeometry(QRect(210, 270, 211, 31))
        self.Fname.setStyleSheet(u"border:1px solid;\n"
"border-radius:15px;\n"
"")
        self.Address = QLineEdit(self )
        self.Address.setObjectName(u"Address")
        self.Address.setGeometry(QRect(660, 380, 211, 31))
        self.Address.setStyleSheet(u"border:1px solid;\n"
"border-radius:15px;\n"
"")
        self.Email = QLineEdit(self )
        self.Email.setObjectName(u"Email")
        self.Email.setGeometry(QRect(210, 490, 211, 31))
        self.Email.setStyleSheet(u"border:1px solid;\n"
"border-radius:15px;\n"
"")
        self.password = QLineEdit(self )
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(660, 490, 211, 31))
        self.password.setStyleSheet(u"border:1px solid;\n"
"border-radius:15px;\n"
"")
        self.password.setEchoMode(QLineEdit.Password)
        self.Department_Text = QLabel(self )
        self.Department_Text.setObjectName(u"Department_Text")
        self.Department_Text.setGeometry(QRect(90, 165, 111, 21))
        font11 = QFont()
        font11.setPointSize(13)
        font11.setBold(True)
        self.Department_Text.setFont(font11)
        self.Employee_id_text = QLabel(self )
        self.Employee_id_text.setObjectName(u"Employee_id_text")
        self.Employee_id_text.setGeometry(QRect(530, 165, 121, 21))
        self.Employee_id_text.setFont(font11)
        self.Fname_text = QLabel(self )
        self.Fname_text.setObjectName(u"Fname_text")
        self.Fname_text.setGeometry(QRect(90, 275, 101, 21))
        self.Fname_text.setFont(font11)
        self.Lname_text = QLabel(self )
        self.Lname_text.setObjectName(u"Lname_text")
        self.Lname_text.setGeometry(QRect(530, 275, 101, 21))
        self.Lname_text.setFont(font11)
        self.Contact_text = QLabel(self )
        self.Contact_text.setObjectName(u"Contact_text")
        self.Contact_text.setGeometry(QRect(90, 385, 101, 21))
        self.Contact_text.setFont(font11)
        self.Address_text = QLabel(self )
        self.Address_text.setObjectName(u"Address_text")
        self.Address_text.setGeometry(QRect(530, 385, 101, 21))
        self.Address_text.setFont(font11)
        self.Email_text = QLabel(self )
        self.Email_text.setObjectName(u"Email_text")
        self.Email_text.setGeometry(QRect(90, 495, 101, 21))
        self.Email_text.setFont(font11)
        self.Password_text = QLabel(self )
        self.Password_text.setObjectName(u"Password_text")
        self.Password_text.setGeometry(QRect(530, 495, 101, 21))
        self.Password_text.setFont(font11)
        
        self.Salary_text = QLabel(self)
        self.Salary_text.setObjectName(u"Salary_text")
        self.Salary_text.setGeometry(QRect(310, 580, 101, 21))
        self.Salary_text.setFont(font11)
        self.Salary = QLineEdit(self)
        self.Salary.setObjectName(u"Salary")
        self.Salary.setGeometry(QRect(390, 575, 211, 31))
        self.Salary.setStyleSheet(u"border:1px solid;\n"
"border-radius:15px;\n"
"")
        
        self.add_button = QPushButton(self)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setGeometry(QRect(420, 650, 111, 31))
        font12 = QFont()
        font12.setPointSize(10)
        font12.setBold(True)
        self.add_button.setFont(font12)
        self.add_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_button.setStyleSheet(u"border-radius:15px;\n"
"background-color: rgb(88, 55, 89);\n"
"color: rgb(255, 255, 255);")
        self.add_button.clicked.connect(self.add_employee_to_database)
    

    def add_employee_to_database(self):
        # Get employee data from the form
        department = self.Department.currentText()
        employee_id = self.Employee_id.text()
        fname = self.Fname.text()
        lname = self.Lname.text()
        contact = self.Contact.text()
        address = self.Address.text()
        email = self.Email.text()
        password = self.password.text()
        salary=self.Salary.text()

        

        # You can validate the data here before inserting it into the database

        # Create a dictionary to hold employee data
        employee_data = {
            "department": department,
            "employee_id": employee_id,
            "fname": fname,
            "lname": lname,
            "contact": contact,
            "address": address,
            "email": email,
            "password": password,
            "salary":salary
        }
        empty_fields = [key.capitalize() for key, value in employee_data.items() if not value]
        if empty_fields:
            error_message = f"Please fill in the following fields: {', '.join(empty_fields)}"
            self.show_error_message(error_message)
            return

        if not is_valid_email(email):
            error_message = "Invalid email address. Please enter a valid email."
            self.show_error_message(error_message)
            return
        if not contact.isdigit():
            error_message = "Contact number should be an numbers."
            self.show_error_message(error_message)
            return
        if len(contact)!=11:
            error_message = "Contact number should be of 11 digits."
            self.show_error_message(error_message)
            return
        
        if not salary.isdigit():
            error_message = "Salary number should be an numbers."
            self.show_error_message(error_message)
            return
        try:
            connection = psycopg2.connect(
                user="postgres",
                password="zendagimigzara",
                host="localhost",
                port="5432",
                database="AEMS"
            )
            cursor = connection.cursor()
            existing_id_query = f"SELECT * FROM Employee WHERE id = '{self.Employee_id.text()}'"
            cursor.execute(existing_id_query)
            existing_id = cursor.fetchone()

            if existing_id:
                error_message = "Employee ID already exists. Please use a different ID."
                self.show_error_message(error_message)
                return

            # Check if the email already exists in the database
            existing_email_query = f"SELECT * FROM Employee WHERE email = '{self.Email.text()}'"
            cursor.execute(existing_email_query)
            existing_email = cursor.fetchone()

            if existing_email:
                error_message = "Email already exists. Please use a different email."
                self.show_error_message(error_message)
                return
                # Insert the employee data into the Employee table
            cursor.execute("""
                INSERT INTO Employee (id, department, Fname, Lname, contact, address, email, password,salary)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s)
            """, (employee_id, department, fname, lname, contact, address, email, password,salary))

            connection.commit()
            # Close the cursor and connection
            cursor.close()
            connection.close()
            success_message = "Employee added successfully!"
            self.show_success_message(success_message)
            # Reset the form
            self.reset_form()

        except (Exception, psycopg2.Error) as error:
            # Handle database errors
            error_message = f"Error adding employee to the database: {error}"
            self.show_error_message(error_message)
        self.reset_form()

    def reset_form(self):
        # Clear input fields
        self.Department.setCurrentIndex(0)
        self.Employee_id.clear()
        self.Fname.clear()
        self.Lname.clear()
        self.Contact.clear()
        self.Address.clear()
        self.Email.clear()
        self.password.clear()
        self.Salary.clear()
    
    def show_error_message(self, message):
        # Create a QMessageBox to show the error message
        error_box = QMessageBox()
        error_box.setWindowTitle("Error")
        error_box.setText(message)
        error_box.setIcon(QMessageBox.Warning)
        error_box.setStandardButtons(QMessageBox.Ok)

        # Set the window modality to make it a blocking message box
        error_box.setWindowModality(Qt.WindowModal)

        # Show the message box
        error_box.exec_()
    
    def show_success_message(self, message):
        QMessageBox.information(self, "Success", message, QMessageBox.Ok)
class Employee_list_page(QWidget):
    def __init__(self, Page):
        super(Employee_list_page, self).__init__(Page)
        self.setObjectName(u"Employeelist_page")
        self.List_title_bar = QGroupBox(self)
        self.List_title_bar.setObjectName(u"List_title_bar")
        self.List_title_bar.setGeometry(QRect(0, 40, 991, 80))
        self.List_title_bar.setStyleSheet(u"background-color: rgb(88, 55, 89);")
        self.List_employee_text = QLabel(self.List_title_bar)
        self.List_employee_text.setObjectName(u"List_employee_text")
        self.List_employee_text.setGeometry(QRect(33, 22, 261, 31))
        font10 = QFont()
        font10.setPointSize(18)
        self.List_employee_text.setFont(font10)
        self.List_employee_text.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.List = QTableWidget(self)
        self.setupTable()
        self.adjustTableHeightAndWidth()

        # Add a refresh button
        self.refresh_button = QPushButton("Refresh", self)
        self.refresh_button.setGeometry(QRect(25, 180, 80, 30))
        self.refresh_button.setStyleSheet(u"background-color: rgb(88, 55, 89);\n" "color: rgb(255, 255, 255);" "border-radius:10px;")
        self.refresh_button.clicked.connect(self.refreshDataFromDatabase)

    def setupTable(self):
        if (self.List.columnCount() < 4):
            self.List.setColumnCount(4)
        font11 = QFont()
        font11.setPointSize(14)
        font11.setBold(True)
        for col, header_text in enumerate(["ID", "First Name", "Last Name", "Department"]):
            header_item = QTableWidgetItem(header_text)
            header_item.setFont(font11)
            self.List.setHorizontalHeaderItem(col, header_item)

        self.List.setObjectName(u"List")
        self.List.setGeometry(QRect(25, 221, 940, 331))
        self.List.setStyleSheet(u"QHeaderView::section {\n"
                                "    background-color: rgb(88, 55, 89);\n"
                                "    color: white;\n"
                                "    border: 1px solid rgb(88, 55, 89);\n"
                                "}")
        self.List.setShowGrid(True)
        self.List.setSortingEnabled(False)
        self.List.setRowCount(0)
        self.List.horizontalHeader().setCascadingSectionResizes(False)
        self.List.horizontalHeader().setDefaultSectionSize(230)
        self.List.horizontalHeader().setHighlightSections(False)
        self.List.horizontalHeader().setProperty("showSortIndicator", False)
        self.List.horizontalHeader().setStretchLastSection(False)
        self.List.verticalHeader().setCascadingSectionResizes(False)
        self.List.verticalHeader().setMinimumSectionSize(25)
        self.List.verticalHeader().setProperty("showSortIndicator", False)
        self.List.verticalHeader().setStretchLastSection(False)

    def refreshDataFromDatabase(self):
        # Clear existing data
        self.setupTable()
        self.adjustTableHeightAndWidth()
        self.List.setRowCount(0)

        try:
            connection = psycopg2.connect(
                user="postgres",
                password="zendagimigzara",
                host="localhost",
                port="5432",
                database="AEMS"
            )
            cursor = connection.cursor()

            # Execute a query to fetch employee data
            cursor.execute("SELECT id, Fname, Lname, email FROM Employee")
            data = cursor.fetchall()

            # Populate the QTableWidget with fetched data
            for row_num, row_data in enumerate(data):
                self.List.insertRow(row_num)
                for col, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    font = QFont()
                    font.setPointSize(13)
                    item.setFont(font)
                    self.List.setItem(row_num, col, item)

            connection.commit()
            cursor.close()

        except Exception as e:
            print("Error:", e)

        # Adjust table height and width after fetching new data
        self.adjustTableHeightAndWidth()

    def adjustTableHeightAndWidth(self):
        # Adjust the height of the table according to the number of rows
        total_height = sum(self.List.rowHeight(row) for row in range(self.List.rowCount()))
        # Add some extra height to account for header and spacing
        total_height += self.List.horizontalHeader().height() + 10
        # Set the height of the table
        self.List.setFixedHeight(total_height)

        # Adjust the width of the table according to the content
        for col in range(self.List.columnCount()):
            max_width = max(self.List.sizeHintForColumn(col), self.List.columnWidth(col))
            max_width -= 2
            self.List.setColumnWidth(col, max_width)
class DashboardPage(QWidget):
    def __init__(self,Page):
        super(DashboardPage, self).__init__(Page)

        self.setObjectName(u"dashboard_page")
        self.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.title_bar = QGroupBox(self)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setGeometry(QRect(0, 60, 991, 80))
        self.Dashboard_text = QLabel(self.title_bar)
        self.Dashboard_text.setObjectName(u"Dashboard_text")
        self.Dashboard_text.setGeometry(QRect(30, 20, 181, 31))
        font4 = QFont()
        font4.setPointSize(20)
        self.Dashboard_text.setFont(font4)
        self.home_text = QLabel(self.title_bar)
        self.home_text.setObjectName(u"home_text")
        self.home_text.setGeometry(QRect(220, 27, 91, 21))
        font5 = QFont()
        font5.setPointSize(14)
        font5.setBold(True)
        self.home_text.setFont(font5)
        self.home_text.setStyleSheet(u"color: rgb(88, 55, 89);")
        self. Admin_dashboard_text = QLabel(self.title_bar)
        self. Admin_dashboard_text.setObjectName(u" Admin_dashboard_text")
        self. Admin_dashboard_text.setGeometry(QRect(320, 27, 171, 21))
        font6 = QFont()
        font6.setPointSize(13)
        self. Admin_dashboard_text.setFont(font6)
        

        self.active_employee = QGroupBox(self)
        # ... (Rest of the initialization code for active_employee group box)
        self.active_employee.setObjectName(u"active_employee")
        self.active_employee.setGeometry(QRect(80, 190, 350, 200))
        self.active_employee.setStyleSheet(u"background-color:rgb(169,169,169);\n"
"\n"
"border-radius:30px;\n"
"")
        self.active_employee_text = QLabel(self.active_employee)
        self.active_employee_text.setObjectName(u"active_employee_text")
        self.active_employee_text.setGeometry(QRect(70, 20, 271, 41))
        font7 = QFont()
        font7.setPointSize(25)
        font7.setBold(False)
        self.active_employee_text.setFont(font7)
        self.active_employee_text.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);")
        self.active_employee_count = QLabel(self.active_employee)
        self.active_employee_count.setObjectName(u"active_employee_count")
        self.active_employee_count.setGeometry(QRect(140, 80, 81, 91))
        font8 = QFont()
        font8.setPointSize(50)
        self.active_employee_count.setFont(font8)
        self.active_employee_count.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);")
        self.active_employee_logo = QLabel(self.active_employee)
        self.active_employee_logo.setObjectName(u"active_employee_logo")
        self.active_employee_logo.setGeometry(QRect(10, 20, 51, 41))
        self.active_employee_logo.setPixmap(QPixmap(u"Images/toppng.com-free-twitter-white-icon-employee-icon-white-537x501.png"))
        self.active_employee_logo.setScaledContents(True)
        

        self.pending_leaves = QGroupBox(self)
        # ... (Rest of the initialization code for pending_leaves group box)
        self.pending_leaves.setObjectName(u"pending_leaves")
        self.pending_leaves.setGeometry(QRect(540, 190, 350, 200))
        self.pending_leaves.setStyleSheet(u"\n"
"background-color: rgb(116, 118, 128);\n"
"border-radius:30px;")
        self.pending_leaves_text = QLabel(self.pending_leaves)
        self.pending_leaves_text.setObjectName(u"pending_leaves_text")
        self.pending_leaves_text.setGeometry(QRect(90, 20, 241, 41))
        font9 = QFont()
        font9.setPointSize(25)
        self.pending_leaves_text.setFont(font9)
        self.pending_leaves_text.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pending_leaves_logo = QLabel(self.pending_leaves)
        self.pending_leaves_logo.setObjectName(u"pending_leaves_logo")
        self.pending_leaves_logo.setGeometry(QRect(20, 20, 47, 41))
        self.pending_leaves_logo.setPixmap(QPixmap(u"Images/pending_logo.png"))
        self.pending_leaves_logo.setScaledContents(True)
        self.pending_leaves_count = QLabel(self.pending_leaves)
        self.pending_leaves_count.setObjectName(u"pending_leaves_count")
        self.pending_leaves_count.setGeometry(QRect(150, 100, 101, 61))
        self.pending_leaves_count.setFont(font8)
        self.pending_leaves_count.setStyleSheet(u"color: rgb(255, 255, 255);")
        

        self.approved_leaves = QGroupBox(self)
        # ... (Rest of the initialization code for approved_leaves group box)
        self.approved_leaves.setObjectName(u"approved_leaves")
        self.approved_leaves.setGeometry(QRect(80, 460, 350, 200))
        self.approved_leaves.setStyleSheet(u"background-color: rgb(140, 146, 172);\n"
"border-radius:30px;")
        self.approved_leaves_logo = QLabel(self.approved_leaves)
        self.approved_leaves_logo.setObjectName(u"approved_leaves_logo")
        self.approved_leaves_logo.setGeometry(QRect(10, 20, 47, 41))
        self.approved_leaves_logo.setPixmap(QPixmap(u"Images/approve_logo.png"))
        self.approved_leaves_logo.setScaledContents(True)
        self.approved_leaves_text = QLabel(self.approved_leaves)
        self.approved_leaves_text.setObjectName(u"approved_leaves_text")
        self.approved_leaves_text.setGeometry(QRect(70, 20, 261, 41))
        self.approved_leaves_text.setFont(font9)
        self.approved_leaves_text.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.approved_leaves_count = QLabel(self.approved_leaves)
        self.approved_leaves_count.setObjectName(u"approved_leaves_count")
        self.approved_leaves_count.setGeometry(QRect(150, 80, 61, 81))
        self.approved_leaves_count.setFont(font8)
        self.approved_leaves_count.setStyleSheet(u"color: rgb(255, 255, 255);")
        

        self.declined_leaves = QGroupBox(self)
        # ... (Rest of the initialization code for declined_leaves group box)
        self.declined_leaves.setObjectName(u"declined_leaves")
        self.declined_leaves.setGeometry(QRect(540, 460, 350, 200))
        self.declined_leaves.setStyleSheet(u"background-color: rgb(98, 112, 156);\n"
"border-radius:30px;")
        self.declined_leaves_logo = QLabel(self.declined_leaves)
        self.declined_leaves_logo.setObjectName(u"declined_leaves_logo")
        self.declined_leaves_logo.setGeometry(QRect(10, 10, 61, 51))
        self.declined_leaves_logo.setPixmap(QPixmap(u"Images/Decline_logo.png"))
        self.declined_leaves_logo.setScaledContents(True)
        self.declined_leaves_text = QLabel(self.declined_leaves)
        self.declined_leaves_text.setObjectName(u"declined_leaves_text")
        self.declined_leaves_text.setGeometry(QRect(70, 10, 251, 51))
        self.declined_leaves_text.setFont(font9)
        self.declined_leaves_text.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.declined_leaves_count = QLabel(self.declined_leaves)
        self.declined_leaves_count.setObjectName(u"declined_leaves_count")
        self.declined_leaves_count.setGeometry(QRect(140, 90, 91, 61))
        self.declined_leaves_count.setFont(font8)
        self.declined_leaves_count.setStyleSheet(u"color: rgb(255, 255, 255);")

        
    
        

class  AdminPage(QMainWindow):
    def __init__(self):
        super( AdminPage, self).__init__()

        self.setObjectName(u" Admin_Page")
        self.resize(1280, 720)
        self.setMinimumSize(QSize(1280, 720))
        self.setMaximumSize(QSize(1280, 720))
        self.PAGE = QWidget(self)
        self.PAGE.setObjectName(u"PAGE")


        # Create instances of your pages
        


        self.side_bar = Sidebar(self.PAGE)
        self.Main_pages = QStackedWidget(self.PAGE)
        self.Main_pages.setObjectName(u"Main_pages")
        self.Main_pages.setEnabled(True)
        self.Main_pages.setGeometry(QRect(290, 0, 990, 720))
        self.Main_pages.setMinimumSize(QSize(990, 720))
        self.dashboard_page = DashboardPage(self.PAGE)
        self.listemployee_page=Employee_list_page(self.PAGE)
        self.addEmployee_page =Add_Employee_page(self.PAGE)
        
        self.Main_pages.addWidget(self.dashboard_page)
        self.Main_pages.addWidget(self.listemployee_page )
        self.Main_pages.addWidget(self.addEmployee_page )
        self.side_bar.setup_connections(self.Main_pages)
        self.setCentralWidget(self.PAGE)

        self.retranslateUi()

    def retranslateUi(self):
        # ... (Rest of the retranslation code)
        self.setWindowTitle(QCoreApplication.translate(" Admin_Page", u"MainWindow", None))
        self.side_bar.setTitle(QCoreApplication.translate(" Admin_Page", u"GroupBox", None))
        self.side_bar.Dashboard_button.setText(QCoreApplication.translate(" Admin_Page", u"Dashboard", None))
        self.side_bar.attendance.setText(QCoreApplication.translate(" Admin_Page", u"Attendance", None))
        self.side_bar.list_employee.setText(QCoreApplication.translate(" Admin_Page", u"List of Employee", None))
        self.side_bar.Add_employee.setText(QCoreApplication.translate(" Admin_Page", u"Add Employee", None))
        self.side_bar.Remove_employee.setText(QCoreApplication.translate(" Admin_Page", u"Remove Employee", None))
        self.side_bar.EandL.setItemText(self.side_bar.EandL.indexOf(self.side_bar.Employee), QCoreApplication.translate(" Admin_Page", u"Employee", None))
        self.side_bar.Pending.setText(QCoreApplication.translate(" Admin_Page", u"Pending", None))
        self.side_bar.Approve.setText(QCoreApplication.translate(" Admin_Page", u"Approved", None))
        self.side_bar.Decline.setText(QCoreApplication.translate(" Admin_Page", u"Declined", None))
        self.side_bar.EandL.setItemText(self.side_bar.EandL.indexOf(self.side_bar.Leave), QCoreApplication.translate(" Admin_Page", u"Leave", None))
        self.side_bar.Logo.setText("")
        self.dashboard_page.title_bar.setTitle("")
        self.dashboard_page.Dashboard_text.setText(QCoreApplication.translate(" Admin_Page", u"Dashboard", None))
        self.dashboard_page.home_text.setText(QCoreApplication.translate(" Admin_Page", u"Home  /", None))
        self.dashboard_page. Admin_dashboard_text.setText(QCoreApplication.translate(" Admin_Page", u" Admin's  Dashboard", None))
        self.dashboard_page.active_employee.setTitle("")
        self.dashboard_page.active_employee_text.setText(QCoreApplication.translate(" Admin_Page", u"Active Employees", None))
        self.dashboard_page.active_employee_count.setText(QCoreApplication.translate(" Admin_Page", u"10", None))
        self.dashboard_page.active_employee_logo.setText("")
        self.dashboard_page.pending_leaves.setTitle("")
        self.dashboard_page.pending_leaves_text.setText(QCoreApplication.translate(" Admin_Page", u"Pending Leaves", None))
        self.dashboard_page.pending_leaves_logo.setText("")
        self.dashboard_page.pending_leaves_count.setText(QCoreApplication.translate(" Admin_Page", u"4", None))
        self.dashboard_page.approved_leaves.setTitle("")
        self.dashboard_page.approved_leaves_logo.setText("")
        self.dashboard_page.approved_leaves_text.setText(QCoreApplication.translate(" Admin_Page", u"Approved Leaves", None))
        self.dashboard_page.approved_leaves_count.setText(QCoreApplication.translate(" Admin_Page", u"5", None))
        self.dashboard_page.declined_leaves.setTitle("")
        self.dashboard_page.declined_leaves_logo.setText("")
        self.dashboard_page.declined_leaves_text.setText(QCoreApplication.translate(" Admin_Page", u"Declined Leaves", None))
        self.dashboard_page.declined_leaves_count.setText(QCoreApplication.translate(" Admin_Page", u"11", None))
        
        self.addEmployee_page.new_employee_title_bar.setTitle("")
        self.addEmployee_page.new_employee_text.setText(QCoreApplication.translate(" Admin_Page", u"Add New Employee", None))
        self.addEmployee_page.Department.setItemText(0, QCoreApplication.translate(" Admin_Page", u"    Marketing", None))
        self.addEmployee_page.Department.setItemText(1, QCoreApplication.translate(" Admin_Page", u"    Accounts", None))
        self.addEmployee_page.Department.setItemText(2, QCoreApplication.translate(" Admin_Page", u"    Sales", None))
        self.addEmployee_page.Department.setItemText(3, QCoreApplication.translate(" Admin_Page", u"    Finance", None))
        self.addEmployee_page.Department.setItemText(4, QCoreApplication.translate(" Admin_Page", u"    Research", None))

        self.addEmployee_page.Department_Text.setText(QCoreApplication.translate(" Admin_Page", u"Department:", None))
        self.addEmployee_page.Employee_id_text.setText(QCoreApplication.translate(" Admin_Page", u"Employee ID:", None))
        self.addEmployee_page.Fname_text.setText(QCoreApplication.translate(" Admin_Page", u"First Name:", None))
        self.addEmployee_page.Lname_text.setText(QCoreApplication.translate(" Admin_Page", u"Last Name:", None))
        self.addEmployee_page.Contact_text.setText(QCoreApplication.translate(" Admin_Page", u"Contact #:", None))
        self.addEmployee_page.Address_text.setText(QCoreApplication.translate(" Admin_Page", u"Address:", None))
        self.addEmployee_page.Email_text.setText(QCoreApplication.translate(" Admin_Page", u"Email:", None))
        self.addEmployee_page.Password_text.setText(QCoreApplication.translate(" Admin_Page", u"Password:", None))
        self.addEmployee_page.add_button.setText(QCoreApplication.translate(" Admin_Page", u"ADD", None))
        self.addEmployee_page.Salary_text.setText(QCoreApplication.translate(" Admin_Page", u"Salary:", None))
        self.listemployee_page.List_title_bar.setTitle("")
        self.listemployee_page.List_employee_text.setText(QCoreApplication.translate("HR_Page", u"List of Employess", None))
        ___qtablewidgetitem = self.listemployee_page.List.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("HR_Page", u"Employee ID", None))
        ___qtablewidgetitem1 = self.listemployee_page.List.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("HR_Page", u"First Name", None))
        ___qtablewidgetitem2 = self.listemployee_page.List.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("HR_Page", u"Last Name", None))
        ___qtablewidgetitem3 = self.listemployee_page.List.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("HR_Page", u"Email", None))
        
    # retranslateUi



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window =  AdminPage()
    window.show()
    sys.exit(app.exec_())
