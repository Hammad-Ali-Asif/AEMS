# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_page.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
from psycopg2 import connect, sql

class Ui_Login_page(object):
    def setupUi(self, Login_page):
        if not Login_page.objectName():
            Login_page.setObjectName(u"Login_page")
        Login_page.resize(1280, 720)
        Login_page.setMinimumSize(QSize(1280, 720))
        Login_page.setMaximumSize(QSize(1280, 720))
        Login_page.setMouseTracking(False)
        Login_page.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(Login_page)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1280, 920))
        self.centralwidget.setMaximumSize(QSize(1280, 920))
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.login_image = QLabel(self.centralwidget)
        self.login_image.setObjectName(u"login_image")
        self.login_image.setGeometry(QRect(530, 0, 751, 721))
        self.login_image.setPixmap(QPixmap(u"Images/login_image.jpg"))
        self.login_image.setScaledContents(True)
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(-10, 40, 531, 251))
        self.logo.setPixmap(QPixmap(u"Images/logo.png"))
        self.logo.setScaledContents(True)
        self.sign_in_text = QLabel(self.centralwidget)
        self.sign_in_text.setObjectName(u"sign_in_text")
        self.sign_in_text.setGeometry(QRect(200, 260, 111, 41))
        font = QFont()
        font.setFamilies([u"Ebrima"])
        font.setPointSize(20)
        font.setBold(True)
        self.sign_in_text.setFont(font)
        self.sign_in_text.setStyleSheet(u"color: rgb(103, 49, 71);")
        self.HR_ID = QLabel(self.centralwidget)
        self.HR_ID.setObjectName(u"HR_ID")
        self.HR_ID.setGeometry(QRect(120, 340, 71, 21))
        font1 = QFont()
        font1.setFamilies([u"Catamaran ExtraLight"])
        font1.setPointSize(13)
        font1.setBold(True)
        self.HR_ID.setFont(font1)
        self.HR_ID.setStyleSheet(u"color: rgb(103, 49, 71);")
        self.Password = QLabel(self.centralwidget)
        self.Password.setObjectName(u"Password")
        self.Password.setGeometry(QRect(40, 430, 201, 21))
        font2 = QFont()
        font2.setFamilies([u"Catamaran ExtraLight"])
        font2.setPointSize(15)
        font2.setBold(True)
        self.Password.setFont(font2)
        self.Password.setStyleSheet(u"margin-left:76px;\n"
"color: rgb(103, 49, 71);")
        self.HR_ID_BOX = QLineEdit(self.centralwidget)
        self.HR_ID_BOX.setObjectName(u"HR_ID_BOX")
        self.HR_ID_BOX.setGeometry(QRect(40, 380, 350, 30))
        self.HR_ID_BOX.setMinimumSize(QSize(350, 25))
        self.HR_ID_BOX.setMaximumSize(QSize(350, 30))
        self.HR_ID_BOX.setStyleSheet(u"margin-left:80px;\n"
"border:1px solid;\n"
"border-radius:10px\n"
"")
        self.password_box = QLineEdit(self.centralwidget)
        self.password_box.setObjectName(u"password_box")
        self.password_box.setGeometry(QRect(40, 460, 350, 30))
        self.password_box.setMaximumSize(QSize(350, 30))
        self.password_box.setStyleSheet(u"margin-left:80px;\n"
"border:1px solid;\n"
"border-radius:10px")
        self.password_box.setEchoMode(QLineEdit.Password)
        self.Sign_in_button = QPushButton(self.centralwidget)
        self.Sign_in_button.setObjectName(u"Sign_in_button")
        self.Sign_in_button.setGeometry(QRect(190, 530, 111, 41))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.Sign_in_button.setFont(font3)
        self.Sign_in_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.Sign_in_button.setStyleSheet(u"border:2px solid;\n"
"border-radius:10px;\n"
"background-color:rgb(103, 49, 71);\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"")
        Login_page.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login_page)

        QMetaObject.connectSlotsByName(Login_page)
    # setupUi

    def retranslateUi(self, Login_page):
        Login_page.setWindowTitle(QCoreApplication.translate("Login_page", u"MainWindow", None))
        self.login_image.setText("")
        self.logo.setText("")
        self.sign_in_text.setText(QCoreApplication.translate("Login_page", u"Sign In", None))
        self.HR_ID.setText(QCoreApplication.translate("Login_page", u"HR ID.", None))
        self.Password.setText(QCoreApplication.translate("Login_page", u"Password.", None))
        self.HR_ID_BOX.setPlaceholderText(QCoreApplication.translate("Login_page", u"Enter your ID", None))
        self.password_box.setPlaceholderText(QCoreApplication.translate("Login_page", u"Enter password", None))
        self.Sign_in_button.setText(QCoreApplication.translate("Login_page", u"Sign In", None))

    # retranslateUi


class LoginPage(QMainWindow, Ui_Login_page):
    def __init__(self):
        super(LoginPage, self).__init__()
        self.setupUi(self)

        

    def check_credentials(self):
        # Get HR ID and Password from the input boxes
        hr_id = self.HR_ID_BOX.text()
        password = self.password_box.text()

        # Example query (replace with your actual query)
        query = sql.SQL("SELECT * FROM users WHERE user_id = {} AND password = {};").format(
            sql.Literal(hr_id), sql.Literal(password)
        )

        # Execute the query
        self.cursor.execute(query)

        # Fetch the result
        result = self.cursor.fetchone()

        if result:
            print("Login Successful")
            # Add your logic for a successful login here
        else:
            print("Login Failed")
            # Add your logic for a failed login here

    def closeEvent(self, event):
        # Close the database connection when the application is closed
        self.cursor.close()
        self.connection.close()

if __name__ == "__main__":
    app = QApplication([])
    login_page = LoginPage()
    login_page.show()
    app.exec_()