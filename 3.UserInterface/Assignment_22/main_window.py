# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(521, 415)
        font = QFont()
        font.setFamilies([u"Dosis ExtraBold"])
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(206, 254, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Dosis ExtraBold"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.high = QRadioButton(self.centralwidget)
        self.high.setObjectName(u"high")
        font2 = QFont()
        font2.setFamilies([u"Dosis ExtraBold"])
        font2.setPointSize(11)
        font2.setBold(True)
        self.high.setFont(font2)

        self.gridLayout.addWidget(self.high, 6, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)

        self.Low = QRadioButton(self.centralwidget)
        self.Low.setObjectName(u"Low")
        self.Low.setFont(font2)
        self.Low.setChecked(True)

        self.gridLayout.addWidget(self.Low, 7, 0, 1, 1)

        self.tb_new_task_description = QTextEdit(self.centralwidget)
        self.tb_new_task_description.setObjectName(u"tb_new_task_description")
        self.tb_new_task_description.setFont(font)
        self.tb_new_task_description.setStyleSheet(u"background-color: rgb(172, 212, 255);\n"
"border-radius: 20px;")

        self.gridLayout.addWidget(self.tb_new_task_description, 2, 0, 1, 2)

        self.btn_new_task = QPushButton(self.centralwidget)
        self.btn_new_task.setObjectName(u"btn_new_task")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_new_task.sizePolicy().hasHeightForWidth())
        self.btn_new_task.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"Dosis ExtraBold"])
        font3.setPointSize(20)
        font3.setBold(True)
        self.btn_new_task.setFont(font3)
        self.btn_new_task.setStyleSheet(u"background-color: rgb(110, 192, 255);")
        self.btn_new_task.setAutoDefault(True)
        self.btn_new_task.setFlat(False)

        self.gridLayout.addWidget(self.btn_new_task, 1, 1, 1, 1)

        self.time = QDateTimeEdit(self.centralwidget)
        self.time.setObjectName(u"time")
        self.time.setFont(font)
        self.time.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.time.setDateTime(QDateTime(QDate(2024, 1, 25), QTime(0, 0, 0)))

        self.gridLayout.addWidget(self.time, 4, 0, 1, 1)

        self.gl_tasks = QGridLayout()
        self.gl_tasks.setObjectName(u"gl_tasks")

        self.gridLayout.addLayout(self.gl_tasks, 0, 0, 1, 2)

        self.tb_new_task = QLineEdit(self.centralwidget)
        self.tb_new_task.setObjectName(u"tb_new_task")
        font4 = QFont()
        font4.setFamilies([u"Dosis ExtraBold"])
        font4.setPointSize(16)
        font4.setBold(True)
        self.tb_new_task.setFont(font4)
        self.tb_new_task.setStyleSheet(u"background-color: rgb(172, 212, 255);\n"
"border-radius: 10px;")

        self.gridLayout.addWidget(self.tb_new_task, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 521, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.btn_new_task.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ToDoList", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Set Time For new Task:", None))
        self.high.setText(QCoreApplication.translate("MainWindow", u"High", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Priority:", None))
        self.Low.setText(QCoreApplication.translate("MainWindow", u"Low", None))
        self.btn_new_task.setText(QCoreApplication.translate("MainWindow", u"+", None))
    # retranslateUi

