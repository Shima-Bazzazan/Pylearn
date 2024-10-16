# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'palam_polum_pillish.ui'
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
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(541, 627)
        font = QFont()
        font.setPointSize(5)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"border-color: rgb(0, 67, 49);\n"
"background-color: rgb(180, 255, 226);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.win_btn = QPushButton(self.centralwidget)
        self.win_btn.setObjectName(u"win_btn")
        self.win_btn.setGeometry(QRect(10, 230, 511, 51))
        font1 = QFont()
        font1.setFamilies([u"Dosis ExtraBold"])
        font1.setPointSize(15)
        self.win_btn.setFont(font1)
        self.win_btn.setStyleSheet(u"border-radius: 15px;\n"
"color: rgb(182, 182, 182);\n"
"background-color: rgb(0, 63, 46);")
        self.back_hand_btn = QPushButton(self.centralwidget)
        self.back_hand_btn.setObjectName(u"back_hand_btn")
        self.back_hand_btn.setGeometry(QRect(100, 490, 141, 81))
        font2 = QFont()
        font2.setPointSize(30)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.back_hand_btn.setFont(font2)
        self.back_hand_btn.setStyleSheet(u"border-radius: 39px;\n"
"color: rgb(0, 145, 0);\n"
"background-color: rgb(0, 67, 49);")
        self.front_hand_btn = QPushButton(self.centralwidget)
        self.front_hand_btn.setObjectName(u"front_hand_btn")
        self.front_hand_btn.setGeometry(QRect(320, 490, 141, 81))
        font3 = QFont()
        font3.setPointSize(30)
        self.front_hand_btn.setFont(font3)
        self.front_hand_btn.setStyleSheet(u"border-radius: 39px;\n"
"color: rgb(0, 145, 0);\n"
"background-color: rgb(0, 67, 49);")
        self.player_score_btn = QPushButton(self.centralwidget)
        self.player_score_btn.setObjectName(u"player_score_btn")
        self.player_score_btn.setGeometry(QRect(170, 440, 211, 51))
        self.player_score_btn.setFont(font1)
        self.player_score_btn.setStyleSheet(u"border-radius: 15px;\n"
"color: rgb(50, 50, 50);")
        self.computer1_score = QPushButton(self.centralwidget)
        self.computer1_score.setObjectName(u"computer1_score")
        self.computer1_score.setGeometry(QRect(30, 20, 211, 51))
        font4 = QFont()
        font4.setFamilies([u"Dosis ExtraBold"])
        font4.setPointSize(15)
        font4.setBold(True)
        self.computer1_score.setFont(font4)
        self.computer1_score.setStyleSheet(u"border-radius: 15px;\n"
"color: rgb(50, 50, 50);")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(50, 80, 171, 131))
        self.frame_2.setStyleSheet(u"border :2px ;\n"
"border-color: rgb(170, 0, 127);\n"
"border-style : dashed;\n"
"border-radius: 38px;\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.computer1_choice = QPushButton(self.frame_2)
        self.computer1_choice.setObjectName(u"computer1_choice")
        self.computer1_choice.setGeometry(QRect(0, 0, 171, 131))
        font5 = QFont()
        font5.setPointSize(43)
        self.computer1_choice.setFont(font5)
        self.computer1_choice.setStyleSheet(u"border :2px solid purple;\n"
"border-style : dashed;\n"
"border-radius: 38px;\n"
"border-color: rgb(0, 67, 49);\n"
"")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(300, 79, 171, 131))
        self.frame_3.setStyleSheet(u"border :2px ;\n"
"border-color: rgb(170, 0, 127);\n"
"border-style : dashed;\n"
"border-radius: 38px;\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.computer2_choice = QPushButton(self.frame_3)
        self.computer2_choice.setObjectName(u"computer2_choice")
        self.computer2_choice.setGeometry(QRect(0, 0, 171, 131))
        self.computer2_choice.setFont(font5)
        self.computer2_choice.setStyleSheet(u"border :2px solid purple;\n"
"border-style : dashed;\n"
"border-radius: 38px;\n"
"border-color: rgb(0, 67, 49);\n"
"")
        self.computer2_score = QPushButton(self.centralwidget)
        self.computer2_score.setObjectName(u"computer2_score")
        self.computer2_score.setGeometry(QRect(280, 20, 211, 51))
        self.computer2_score.setFont(font1)
        self.computer2_score.setStyleSheet(u"border-radius: 15px;\n"
"color: rgb(50, 50, 50);")
        self.player_choice = QPushButton(self.centralwidget)
        self.player_choice.setObjectName(u"player_choice")
        self.player_choice.setGeometry(QRect(190, 310, 171, 131))
        self.player_choice.setFont(font5)
        self.player_choice.setStyleSheet(u"border :2px solid purple;\n"
"border-style : dashed;\n"
"border-radius: 38px;\n"
"border-color: rgb(0, 67, 49);\n"
"\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 541, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.win_btn.setText("")
        self.back_hand_btn.setText(QCoreApplication.translate("MainWindow", u"\ud83e\udd1a\ud83c\udffb", None))
        self.front_hand_btn.setText(QCoreApplication.translate("MainWindow", u"\u270b\ud83c\udffb", None))
        self.player_score_btn.setText(QCoreApplication.translate("MainWindow", u"Your Score", None))
        self.computer1_score.setText(QCoreApplication.translate("MainWindow", u"Computer1 Score ", None))
        self.computer1_choice.setText("")
        self.computer2_choice.setText("")
        self.computer2_score.setText(QCoreApplication.translate("MainWindow", u"Computer2 Score", None))
        self.player_choice.setText("")
    # retranslateUi

