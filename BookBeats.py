# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'BookBeats.ui'
##
# Created by: Qt User Interface Compiler version 6.9.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
                               QMainWindow, QMenuBar, QPushButton, QSizePolicy,
                               QStatusBar, QWidget)


class Ui_BookBeats(object):
    def setupUi(self, BookBeats):
        if not BookBeats.objectName():
            BookBeats.setObjectName(u"BookBeats")
        BookBeats.resize(800, 687)
        font = QFont()
        font.setPointSize(7)
        BookBeats.setFont(font)
        BookBeats.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.centralwidget = QWidget(BookBeats)
        self.centralwidget.setObjectName(u"centralwidget")
        self.navbar = QWidget(self.centralwidget)
        self.navbar.setObjectName(u"navbar")
        self.navbar.setGeometry(QRect(10, 0, 771, 91))
        self.navbar.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(0, 0, 0, 108));\n"
                                  "color: rgb(255, 255, 255);")
        self.logo = QLabel(self.navbar)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(30, 10, 131, 81))
        self.logo.setStyleSheet(u"background:transparent;")
        self.logo.setPixmap(QPixmap(u"img/logo.png"))
        self.logo.setScaledContents(True)
        self.appName = QLabel(self.navbar)
        self.appName.setObjectName(u"appName")
        self.appName.setGeometry(QRect(230, 10, 221, 61))
        font1 = QFont()
        font1.setPointSize(22)
        self.appName.setFont(font1)
        self.appName.setStyleSheet(u"background:transparent;")
        self.appName.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.linkedin_btn = QPushButton(self.navbar)
        self.linkedin_btn.setObjectName(u"linkedin_btn")
        self.linkedin_btn.setGeometry(QRect(490, 50, 131, 41))
        font2 = QFont()
        font2.setPointSize(17)
        font2.setItalic(True)
        font2.setUnderline(True)
        self.linkedin_btn.setFont(font2)
        self.linkedin_btn.setStyleSheet(u"background:transparent;\n"
                                        "border:0;")
        self.github_btn = QPushButton(self.navbar)
        self.github_btn.setObjectName(u"github_btn")
        self.github_btn.setGeometry(QRect(630, 50, 131, 41))
        self.github_btn.setFont(font2)
        self.github_btn.setStyleSheet(u"background:transparent;\n"
                                      "border:0;")
        self.content = QWidget(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setGeometry(QRect(50, 120, 701, 381))
        self.content.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(0, 0, 0, 108));")
        self.label = QLabel(self.content)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 20, 541, 61))
        font3 = QFont()
        font3.setPointSize(17)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                 "border-radius5px;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.openfile = QPushButton(self.content)
        self.openfile.setObjectName(u"openfile")
        self.openfile.setGeometry(QRect(20, 110, 181, 61))
        font4 = QFont()
        font4.setPointSize(18)
        self.openfile.setFont(font4)
        self.openfile.setStyleSheet(u"background-color: rgb(0, 0, 127);\n"
                                    "border-radius:5px;")
        self.LanguageList = QComboBox(self.content)
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.addItem("")
        self.LanguageList.setObjectName(u"LanguageList")
        self.LanguageList.setGeometry(QRect(389, 120, 241, 41))
        font5 = QFont()
        font5.setPointSize(13)
        self.LanguageList.setFont(font5)
        self.LanguageList.setStyleSheet(u"background:white;\n"
                                        "color:black;\n"
                                        "border:1px solid black;\n"
                                        "\n"
                                        "padding:5px;\n"
                                        "padding-left:15px;")
        self.LanguageList.setIconSize(QSize(21, 21))
        self.select_lang = QLabel(self.content)
        self.select_lang.setObjectName(u"select_lang")
        self.select_lang.setGeometry(QRect(230, 120, 181, 41))
        self.select_lang.setFont(font5)
        self.select_lang.setStyleSheet(u"background:transparent;\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "border:0;")
        self.select_lang.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lfileName = QLabel(self.content)
        self.lfileName.setObjectName(u"lfileName")
        self.lfileName.setGeometry(QRect(20, 190, 281, 51))
        font6 = QFont()
        font6.setPointSize(14)
        self.lfileName.setFont(font6)
        self.lfileName.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                     "background:0;")
        self.lfileName.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.audiofilename = QLineEdit(self.content)
        self.audiofilename.setObjectName(u"audiofilename")
        self.audiofilename.setGeometry(QRect(320, 190, 331, 51))
        self.audiofilename.setFont(font5)
        self.audiofilename.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                         "padding:3px;\n"
                                         "padding-left:15px;\n"
                                         "color:black;")
        self.Download = QPushButton(self.content)
        self.Download.setObjectName(u"Download")
        self.Download.setGeometry(QRect(30, 300, 311, 61))
        self.Download.setFont(font1)
        self.Download.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(77, 231, 113);\n"
                                    "border-radius:5px;")
        self.label_7 = QLabel(self.content)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(350, 310, 321, 41))
        font7 = QFont()
        font7.setPointSize(14)
        font7.setUnderline(False)
        self.label_7.setFont(font7)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                   "\n"
                                   "background:0;")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 520, 381, 21))
        self.label_3.setFont(font5)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 550, 381, 21))
        self.label_4.setFont(font5)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 580, 401, 21))
        self.label_5.setFont(font5)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 600, 781, 41))
        font8 = QFont()
        font8.setPointSize(13)
        font8.setBold(True)
        font8.setItalic(True)
        self.label_6.setFont(font8)
        self.label_6.setStyleSheet(u"color:red;")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        BookBeats.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(BookBeats)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        BookBeats.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(BookBeats)
        self.statusbar.setObjectName(u"statusbar")
        BookBeats.setStatusBar(self.statusbar)

        self.retranslateUi(BookBeats)

        self.LanguageList.setCurrentIndex(11)

        QMetaObject.connectSlotsByName(BookBeats)
    # setupUi

    def retranslateUi(self, BookBeats):
        BookBeats.setWindowTitle(QCoreApplication.translate(
            "BookBeats", u"MainWindow", None))
        self.logo.setText("")
        self.appName.setText(QCoreApplication.translate(
            "BookBeats", u"<html><head/><body><p> BookBeats<sup>(BB)</sup></p></body></html>", None))
        self.linkedin_btn.setText(
            QCoreApplication.translate("BookBeats", u"Linkedin", None))
        self.github_btn.setText(
            QCoreApplication.translate("BookBeats", u"Github", None))
        self.label.setText(QCoreApplication.translate(
            "BookBeats", u"PDF into Audio MP3 File", None))
        self.openfile.setText(QCoreApplication.translate(
            "BookBeats", u"Open File", None))
        self.LanguageList.setItemText(
            0, QCoreApplication.translate("BookBeats", u"Afrikaans", None))
        self.LanguageList.setItemText(
            1, QCoreApplication.translate("BookBeats", u"Arabic", None))
        self.LanguageList.setItemText(
            2, QCoreApplication.translate("BookBeats", u"Bengali", None))
        self.LanguageList.setItemText(
            3, QCoreApplication.translate("BookBeats", u"Bosnian", None))
        self.LanguageList.setItemText(
            4, QCoreApplication.translate("BookBeats", u"Bulgarian", None))
        self.LanguageList.setItemText(
            5, QCoreApplication.translate("BookBeats", u"Catalan", None))
        self.LanguageList.setItemText(
            6, QCoreApplication.translate("BookBeats", u"Chinese ", None))
        self.LanguageList.setItemText(
            7, QCoreApplication.translate("BookBeats", u"Croatian", None))
        self.LanguageList.setItemText(
            8, QCoreApplication.translate("BookBeats", u"Czech", None))
        self.LanguageList.setItemText(
            9, QCoreApplication.translate("BookBeats", u"Danish", None))
        self.LanguageList.setItemText(
            10, QCoreApplication.translate("BookBeats", u"Dutch", None))
        self.LanguageList.setItemText(11, QCoreApplication.translate(
            "BookBeats", u"English (Australia)", None))
        self.LanguageList.setItemText(12, QCoreApplication.translate(
            "BookBeats", u"English (India)", None))
        self.LanguageList.setItemText(
            13, QCoreApplication.translate("BookBeats", u"English (UK)", None))
        self.LanguageList.setItemText(
            14, QCoreApplication.translate("BookBeats", u"English (US)", None))
        self.LanguageList.setItemText(
            15, QCoreApplication.translate("BookBeats", u"Filipino", None))
        self.LanguageList.setItemText(
            16, QCoreApplication.translate("BookBeats", u"Finnish", None))
        self.LanguageList.setItemText(
            17, QCoreApplication.translate("BookBeats", u"French", None))
        self.LanguageList.setItemText(
            18, QCoreApplication.translate("BookBeats", u"German", None))
        self.LanguageList.setItemText(
            19, QCoreApplication.translate("BookBeats", u"Greek", None))
        self.LanguageList.setItemText(
            20, QCoreApplication.translate("BookBeats", u"Gujarati", None))
        self.LanguageList.setItemText(
            21, QCoreApplication.translate("BookBeats", u"Hebrew", None))
        self.LanguageList.setItemText(
            22, QCoreApplication.translate("BookBeats", u"Hindi", None))
        self.LanguageList.setItemText(
            23, QCoreApplication.translate("BookBeats", u"Hungarian", None))
        self.LanguageList.setItemText(
            24, QCoreApplication.translate("BookBeats", u"Icelandic", None))
        self.LanguageList.setItemText(
            25, QCoreApplication.translate("BookBeats", u"Indonesian", None))
        self.LanguageList.setItemText(
            26, QCoreApplication.translate("BookBeats", u"Italian", None))
        self.LanguageList.setItemText(
            27, QCoreApplication.translate("BookBeats", u"Japanese", None))
        self.LanguageList.setItemText(
            28, QCoreApplication.translate("BookBeats", u"Javanese", None))
        self.LanguageList.setItemText(
            29, QCoreApplication.translate("BookBeats", u"Kannada", None))
        self.LanguageList.setItemText(
            30, QCoreApplication.translate("BookBeats", u"Khmer", None))
        self.LanguageList.setItemText(
            31, QCoreApplication.translate("BookBeats", u"Korean", None))
        self.LanguageList.setItemText(
            32, QCoreApplication.translate("BookBeats", u"Latvian", None))
        self.LanguageList.setItemText(
            33, QCoreApplication.translate("BookBeats", u"Lithuanian", None))
        self.LanguageList.setItemText(
            34, QCoreApplication.translate("BookBeats", u"Malayalam", None))
        self.LanguageList.setItemText(
            35, QCoreApplication.translate("BookBeats", u"Marathi", None))
        self.LanguageList.setItemText(
            36, QCoreApplication.translate("BookBeats", u"Nepali", None))
        self.LanguageList.setItemText(37, QCoreApplication.translate(
            "BookBeats", u"Portuguese (Brazil)", None))
        self.LanguageList.setItemText(38, QCoreApplication.translate(
            "BookBeats", u"Portuguese (Portugal)", None))
        self.LanguageList.setItemText(
            39, QCoreApplication.translate("BookBeats", u"Punjabi", None))
        self.LanguageList.setItemText(
            40, QCoreApplication.translate("BookBeats", u"Romanian", None))
        self.LanguageList.setItemText(
            41, QCoreApplication.translate("BookBeats", u"Russian", None))
        self.LanguageList.setItemText(
            42, QCoreApplication.translate("BookBeats", u"Serbian", None))
        self.LanguageList.setItemText(
            43, QCoreApplication.translate("BookBeats", u"Sinhala", None))
        self.LanguageList.setItemText(
            44, QCoreApplication.translate("BookBeats", u"Slovenian", None))
        self.LanguageList.setItemText(
            45, QCoreApplication.translate("BookBeats", u"Spanish", None))
        self.LanguageList.setItemText(
            46, QCoreApplication.translate("BookBeats", u"Sundanese", None))
        self.LanguageList.setItemText(
            47, QCoreApplication.translate("BookBeats", u"Swahili", None))
        self.LanguageList.setItemText(
            48, QCoreApplication.translate("BookBeats", u"Swedish", None))
        self.LanguageList.setItemText(
            49, QCoreApplication.translate("BookBeats", u"Tamil", None))
        self.LanguageList.setItemText(
            50, QCoreApplication.translate("BookBeats", u"Telugu", None))
        self.LanguageList.setItemText(
            51, QCoreApplication.translate("BookBeats", u"Thai", None))
        self.LanguageList.setItemText(
            52, QCoreApplication.translate("BookBeats", u"Turkish", None))
        self.LanguageList.setItemText(
            53, QCoreApplication.translate("BookBeats", u"Ukrainian", None))
        self.LanguageList.setItemText(
            54, QCoreApplication.translate("BookBeats", u"Urdu", None))
        self.LanguageList.setItemText(
            55, QCoreApplication.translate("BookBeats", u"Vietnamese", None))
        self.LanguageList.setItemText(
            56, QCoreApplication.translate("BookBeats", u"Welsh", None))
        self.LanguageList.setItemText(
            57, QCoreApplication.translate("BookBeats", u"Xhosa", None))
        self.LanguageList.setItemText(
            58, QCoreApplication.translate("BookBeats", u"Zulu", None))

        self.LanguageList.setPlaceholderText("")
        self.select_lang.setText(QCoreApplication.translate(
            "BookBeats", u"Select Language :", None))
        self.lfileName.setText(QCoreApplication.translate(
            "BookBeats", u"Enter Name For Audio File *.MP3", None))
        self.Download.setText(QCoreApplication.translate(
            "BookBeats", u"Download ", None))
        self.label_7.setText(QCoreApplication.translate(
            "BookBeats", u"After Downloaded it will Start Playing", None))
        self.label_3.setText(QCoreApplication.translate(
            "BookBeats", u"1.Open Pdf File .", None))
        self.label_4.setText(QCoreApplication.translate(
            "BookBeats", u"2.Select Language.", None))
        self.label_5.setText(QCoreApplication.translate(
            "BookBeats", u"3. Enter Audio file Name and  Click  Download Button.", None))
        self.label_6.setText(QCoreApplication.translate(
            "BookBeats", u"<html><head/><body><p>Please Wait for minute for Processing form every word to audio it will take few minutes.</p></body></html>", None))
    # retranslateUi
