# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Salary ReportRRKruo.ui'
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
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setMaximumSize(QSize(1280, 720))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(590, 50, 481, 61))
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(85, 55, 89);")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        brush = QBrush(QColor(85, 55, 89, 255))
        brush.setStyle(Qt.SolidPattern)
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        __qtablewidgetitem.setBackground(QColor(85, 55, 89));
        __qtablewidgetitem.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        __qtablewidgetitem1.setBackground(QColor(85, 55, 89));
        __qtablewidgetitem1.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        __qtablewidgetitem2.setBackground(QColor(85, 55, 89));
        __qtablewidgetitem2.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        __qtablewidgetitem3.setBackground(QColor(85, 55, 89));
        __qtablewidgetitem3.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        __qtablewidgetitem4.setBackground(QColor(85, 55, 89));
        __qtablewidgetitem4.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.tableWidget.rowCount() < 12):
            self.tableWidget.setRowCount(12)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem16)
        font2 = QFont()
        font2.setPointSize(12)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font2);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font2);
        self.tableWidget.setItem(1, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font2);
        self.tableWidget.setItem(2, 0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font2);
        self.tableWidget.setItem(3, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font2);
        self.tableWidget.setItem(4, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font2);
        self.tableWidget.setItem(5, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font2);
        self.tableWidget.setItem(6, 0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font2);
        self.tableWidget.setItem(7, 0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setFont(font2);
        self.tableWidget.setItem(8, 0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setFont(font2);
        self.tableWidget.setItem(9, 0, __qtablewidgetitem26)
        font3 = QFont()
        font3.setPointSize(13)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setFont(font3);
        self.tableWidget.setItem(10, 0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setFont(font2);
        self.tableWidget.setItem(11, 0, __qtablewidgetitem28)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(380, 210, 841, 391))
        self.tableWidget.horizontalHeader().setDefaultSectionSize(162)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(410, 130, 91, 21))
        font4 = QFont()
        font4.setPointSize(16)
        font4.setBold(True)
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"color: rgb(85, 55, 89);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(500, 130, 261, 21))
        font5 = QFont()
        font5.setPointSize(16)
        font5.setBold(True)
        font5.setUnderline(False)
        self.label_3.setFont(font5)
        self.label_3.setStyleSheet(u"color: rgb(85, 55, 89);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(410, 160, 151, 31))
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"color: rgb(85, 55, 89);")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(550, 160, 141, 31))
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"color: rgb(85, 55, 89);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Annual Salary Report", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Months", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Bonus", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Deduction", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Salary", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Total Wage", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"1.", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"2.", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"3.", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"4.", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"5.", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"6.", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"7.", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"8.", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"9.", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"10.", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"11.", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"12.", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem17 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"January", None));
        ___qtablewidgetitem18 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Febuary", None));
        ___qtablewidgetitem19 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"March", None));
        ___qtablewidgetitem20 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"April", None));
        ___qtablewidgetitem21 = self.tableWidget.item(4, 0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"May", None));
        ___qtablewidgetitem22 = self.tableWidget.item(5, 0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"June", None));
        ___qtablewidgetitem23 = self.tableWidget.item(6, 0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"July", None));
        ___qtablewidgetitem24 = self.tableWidget.item(7, 0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"August", None));
        ___qtablewidgetitem25 = self.tableWidget.item(8, 0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"September", None));
        ___qtablewidgetitem26 = self.tableWidget.item(9, 0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"October", None));
        ___qtablewidgetitem27 = self.tableWidget.item(10, 0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"November", None));
        ___qtablewidgetitem28 = self.tableWidget.item(11, 0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"December", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Name :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Becca J.Reed", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Department :", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Mangement", None))
    # retranslateUi

