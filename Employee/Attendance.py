# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AttendanceXSAwVX.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QStackedWidget,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setMaximumSize(QSize(1280, 720))
        font = QFont()
        font.setPointSize(16)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(530, 30, 351, 51))
        font1 = QFont()
        font1.setPointSize(25)
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.label.setFont(font1)
        self.label.setAutoFillBackground(False)
        self.jan = QPushButton(self.centralwidget)
        self.jan.setObjectName(u"jan")
        self.jan.setGeometry(QRect(520, 90, 91, 31))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.jan.setFont(font2)
        self.jan.setStyleSheet(u"background-color: rgb(85, 55, 89);\n"
"color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius: 10px")
        self.feb = QPushButton(self.centralwidget)
        self.feb.setObjectName(u"feb")
        self.feb.setGeometry(QRect(620, 90, 91, 31))
        self.feb.setFont(font2)
        self.feb.setStyleSheet(u"background-color: rgb(85, 55, 89);\n"
"color: rgb(255, 255, 255);\n"
"border:1px;\n"
"border-radius:10px;")
        self.march = QPushButton(self.centralwidget)
        self.march.setObjectName(u"march")
        self.march.setGeometry(QRect(720, 90, 81, 31))
        self.march.setFont(font2)
        self.march.setStyleSheet(u"background-color: rgb(85, 55, 89);\n"
"color: rgb(255, 255, 255);\n"
"border:1px;\n"
"border-radius:10px;\n"
"")
        self.april = QPushButton(self.centralwidget)
        self.april.setObjectName(u"april")
        self.april.setGeometry(QRect(810, 90, 91, 31))
        self.april.setFont(font2)
        self.april.setStyleSheet(u"background-color: rgb(85, 55, 89);\n"
"color: rgb(255, 255, 255);\n"
"border:1px;\n"
"border-radius:10px;")
        self.may = QPushButton(self.centralwidget)
        self.may.setObjectName(u"may")
        self.may.setGeometry(QRect(910, 90, 81, 31))
        self.may.setFont(font2)
        self.may.setStyleSheet(u"background-color: rgb(85, 55, 89);\n"
"color: rgb(255, 255, 255);\n"
"border:1px;\n"
"border-radius:10px;")
        self.june = QPushButton(self.centralwidget)
        self.june.setObjectName(u"june")
        self.june.setGeometry(QRect(1000, 90, 91, 31))
        self.june.setFont(font2)
        self.june.setStyleSheet(u"background-color: rgb(85, 55, 89);\n"
"color: rgb(255, 255, 255);\n"
"border:1px;\n"
"border-radius:10px;\n"
"")
        self.july = QPushButton(self.centralwidget)
        self.july.setObjectName(u"july")
        self.july.setGeometry(QRect(1104, 88, 81, 31))
        self.july.setFont(font2)
        self.july.setStyleSheet(u"background-color: rgb(85, 55, 89);\n"
"color: rgb(255, 255, 255);\n"
"border:1px;\n"
"border-radius:10px;")
        self.aug = QPushButton(self.centralwidget)
        self.aug.setObjectName(u"aug")
        self.aug.setGeometry(QRect(700, 130, 81, 31))
        self.aug.setFont(font2)
        self.aug.setStyleSheet(u"background-color: rgb(85, 55, 89);\n"
"color: rgb(255, 255, 255);\n"
"border:1px;\n"
"border-radius:10px;")
        self.sep = QPushButton(self.centralwidget)
        self.sep.setObjectName(u"sep")
        self.sep.setGeometry(QRect(790, 130, 101, 31))
        self.sep.setFont(font2)
        self.sep.setStyleSheet(u"background-color: rgb(85, 55, 89);\n"
"color: rgb(255, 255, 255);\n"
"border:1px;\n"
"border-radius:10px;")
        self.oct = QPushButton(self.centralwidget)
        self.oct.setObjectName(u"oct")
        self.oct.setGeometry(QRect(900, 130, 81, 31))
        self.oct.setFont(font2)
        self.oct.setStyleSheet(u"background-color: rgb(85, 55, 89);\n"
"color: rgb(255, 255, 255);\n"
"border:1px;\n"
"border-radius:10px;")
        self.nov = QPushButton(self.centralwidget)
        self.nov.setObjectName(u"nov")
        self.nov.setGeometry(QRect(990, 130, 101, 31))
        self.nov.setFont(font2)
        self.nov.setStyleSheet(u"background-color: rgb(85, 55, 89);\n"
"color: rgb(255, 255, 255);\n"
"border:1px;\n"
"border-radius:10px;")
        self.dec = QPushButton(self.centralwidget)
        self.dec.setObjectName(u"dec")
        self.dec.setGeometry(QRect(1098, 128, 91, 31))
        self.dec.setFont(font2)
        self.dec.setStyleSheet(u"background-color: rgb(85, 55, 89);\n"
"color: rgb(255, 255, 255);\n"
"border:1px;\n"
"border-radius:10px;")
        self.Percentage = QProgressBar(self.centralwidget)
        self.Percentage.setObjectName(u"Percentage")
        self.Percentage.setGeometry(QRect(850, 170, 381, 24))
        self.Percentage.setStyleSheet(u"selection-background-color: rgb(85, 55, 89);")
        self.Percentage.setValue(24)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(410, 220, 651, 461))
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.tableWidget = QTableWidget(self.page_3)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        brush = QBrush(QColor(85, 55, 89, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        __qtablewidgetitem.setBackground(QColor(85, 55, 89));
        __qtablewidgetitem.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        __qtablewidgetitem1.setBackground(QColor(85, 55, 89));
        __qtablewidgetitem1.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(30, 20, 581, 431))
        self.tableWidget.horizontalHeader().setMinimumSectionSize(96)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(305)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.tableWidget_2 = QTableWidget(self.page_4)
        if (self.tableWidget_2.columnCount() < 2):
            self.tableWidget_2.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        __qtablewidgetitem2.setBackground(QColor(85, 55, 89));
        __qtablewidgetitem2.setForeground(brush);
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font2);
        __qtablewidgetitem3.setForeground(brush);
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(35, 21, 581, 421))
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(305)
        self.stackedWidget.addWidget(self.page_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#553759;\">Employee Attendance</span></p></body></html>", None))
        self.jan.setText(QCoreApplication.translate("MainWindow", u"January", None))
        self.feb.setText(QCoreApplication.translate("MainWindow", u"February", None))
        self.march.setText(QCoreApplication.translate("MainWindow", u"March", None))
        self.april.setText(QCoreApplication.translate("MainWindow", u"April", None))
        self.may.setText(QCoreApplication.translate("MainWindow", u"May", None))
        self.june.setText(QCoreApplication.translate("MainWindow", u"June", None))
        self.july.setText(QCoreApplication.translate("MainWindow", u"July", None))
        self.aug.setText(QCoreApplication.translate("MainWindow", u"August", None))
        self.sep.setText(QCoreApplication.translate("MainWindow", u"September", None))
        self.oct.setText(QCoreApplication.translate("MainWindow", u"October", None))
        self.nov.setText(QCoreApplication.translate("MainWindow", u"November", None))
        self.dec.setText(QCoreApplication.translate("MainWindow", u"December", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Status", None));
    # retranslateUi


class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()

        # Create an instance of the UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect button signals to corresponding functions
        self.ui.jan.clicked.connect(self.show_january_data)
        # Connect other buttons in a similar way

    def show_january_data(self):
        # Implement the functionality to show January data here
        # For example, switch to the appropriate page in the stacked widget
        self.ui.stackedWidget.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication([])
    main_window = MyMainWindow()
    main_window.show()
    app.exec()
