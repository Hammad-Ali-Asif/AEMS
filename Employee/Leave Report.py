# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Leave ReportKdCrOE.ui'
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
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

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
        self.label.setGeometry(QRect(700, 40, 361, 51))
        font = QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(85, 55, 89);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(500, 110, 151, 51))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(85, 55, 89);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(500, 170, 201, 41))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(85, 55, 89);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(640, 110, 101, 51))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(85, 55, 89);")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(700, 170, 101, 41))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgb(85, 55, 89);")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        brush = QBrush(QColor(85, 55, 89, 255))
        brush.setStyle(Qt.SolidPattern)
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
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
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        __qtablewidgetitem2.setBackground(QColor(85, 55, 89));
        __qtablewidgetitem2.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(480, 220, 711, 461))
        self.tableWidget.horizontalHeader().setDefaultSectionSize(237)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Leave Report", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Total Leaves :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Reamining Leaves :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"18", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Status", None));
    # retranslateUi

