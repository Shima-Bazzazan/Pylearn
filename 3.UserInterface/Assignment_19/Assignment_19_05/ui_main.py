# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QMainWindow, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(538, 485)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Dosis ExtraBold"])
        font.setPointSize(20)
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(126, 126, 126);")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_guess = QPushButton(self.centralwidget)
        self.btn_guess.setObjectName(u"btn_guess")
        self.btn_guess.setGeometry(QRect(140, 320, 261, 71))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_guess.sizePolicy().hasHeightForWidth())
        self.btn_guess.setSizePolicy(sizePolicy1)
        self.btn_guess.setFont(font)
        self.btn_guess.setStyleSheet(u"border-radius: 25px;\n"
"color: rgb(255, 170, 127);\n"
"background-color: rgb(57, 57, 57);")
        self.btn_number = QPlainTextEdit(self.centralwidget)
        self.btn_number.setObjectName(u"btn_number")
        self.btn_number.setGeometry(QRect(220, 120, 101, 61))
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_number.sizePolicy().hasHeightForWidth())
        self.btn_number.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setFamilies([u"Dosis ExtraBold"])
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.btn_number.setFont(font1)
        self.btn_number.setMouseTracking(False)
        self.btn_number.setFocusPolicy(Qt.ClickFocus)
        self.btn_number.setToolTipDuration(4)
        self.btn_number.setStyleSheet(u"background-color: rgb(255, 225, 201);\n"
"color: rgb(57, 57, 57);\n"
"border-radius: 15px;")
        self.btn_number.setFrameShape(QFrame.Box)
        self.btn_number.setLineWidth(5)
        self.btn_number.setMidLineWidth(5)
        self.btn_number.setBackgroundVisible(False)
        self.btn_number.setCenterOnScroll(False)
        self.btn_result = QPushButton(self.centralwidget)
        self.btn_result.setObjectName(u"btn_result")
        self.btn_result.setGeometry(QRect(170, 200, 201, 81))
        sizePolicy1.setHeightForWidth(self.btn_result.sizePolicy().hasHeightForWidth())
        self.btn_result.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"Dosis ExtraBold"])
        font2.setPointSize(19)
        font2.setBold(True)
        self.btn_result.setFont(font2)
        self.btn_result.setStyleSheet(u"border-radius: 15px;\n"
"color: rgb(57, 57, 57);\n"
"background-color: rgb(255, 225, 201);\n"
"")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 20, 361, 71))
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setFamilies([u"Dosis ExtraBold"])
        font3.setPointSize(40)
        font3.setBold(True)
        self.pushButton.setFont(font3)
        self.pushButton.setStyleSheet(u"border-radius: 10px;\n"
"color: rgb(255, 170, 127);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 538, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Guess_Number", None))
        self.btn_guess.setText(QCoreApplication.translate("MainWindow", u"Guess", None))
#if QT_CONFIG(tooltip)
        self.btn_number.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_number.setPlainText("")
        self.btn_result.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"GUESS NUMBER ", None))
    # retranslateUi

