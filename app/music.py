# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'muiscApp.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QListWidget,
    QListWidgetItem, QProgressBar, QPushButton, QSizePolicy,
    QWidget)
import img_rc
import img_rc

class Ui_MusicApp(object):
    def setupUi(self, MusicApp):
        if not MusicApp.objectName():
            MusicApp.setObjectName(u"MusicApp")
        MusicApp.resize(955, 628)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(95)
        sizePolicy.setVerticalStretch(62)
        sizePolicy.setHeightForWidth(MusicApp.sizePolicy().hasHeightForWidth())
        MusicApp.setSizePolicy(sizePolicy)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaOptical))
        MusicApp.setWindowIcon(icon)
        MusicApp.setStyleSheet(u"background-image: url(:/newPrefix/background.png) ;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.991266 rgba(15, 15, 34, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"background-repeat:no-repeat;\n"
"background-position:center;")
        self.open_btn = QPushButton(MusicApp)
        self.open_btn.setObjectName(u"open_btn")
        self.open_btn.setGeometry(QRect(10, 20, 201, 53))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(14)
        font.setItalic(False)
        self.open_btn.setFont(font)
        self.open_btn.setStyleSheet(u"border:1px solid gray;\n"
"border-radius:8px;\n"
"color:white;\n"
"background:transparent;")
        self.widget = QWidget(MusicApp)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(580, 40, 351, 451))
        self.widget.setStyleSheet(u"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(0, 0, 0, 120));\n"
"border-radius:10px")
        self.current_track = QLabel(self.widget)
        self.current_track.setObjectName(u"current_track")
        self.current_track.setGeometry(QRect(20, 360, 311, 71))
        font1 = QFont()
        font1.setFamilies([u"Microsoft Sans Serif"])
        font1.setPointSize(12)
        self.current_track.setFont(font1)
        self.current_track.setStyleSheet(u"color:white; \n"
"background:transparent;\n"
"color: rgb(174, 11, 255);")
        self.current_track.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cover_img = QLabel(self.widget)
        self.cover_img.setObjectName(u"cover_img")
        self.cover_img.setGeometry(QRect(70, 60, 221, 271))
        self.cover_img.setFrameShape(QFrame.Shape.NoFrame)
        self.cover_img.setFrameShadow(QFrame.Shadow.Plain)
        self.cover_img.setLineWidth(1)
        self.cover_img.setPixmap(QPixmap(u":/newPrefix/C:/Users/Lenovo/Pictures/taylor-swift-wallpaper-preview.jpg"))
        self.cover_img.setScaledContents(True)
        self.audio_list = QListWidget(MusicApp)
        self.audio_list.setObjectName(u"audio_list")
        self.audio_list.setGeometry(QRect(40, 88, 481, 521))
        self.audio_list.setStyleSheet(u"padding:20px;\n"
"color: rgb(140, 40, 88);\n"
"font: 12pt \"Microsoft Sans Serif\";\n"
"background:transparent;\n"
"border:0px;")
        self.audio_list.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.audio_list.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.widget_2 = QWidget(MusicApp)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(580, 510, 361, 81))
        self.widget_2.setStyleSheet(u"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(0, 0, 0, 120));\n"
"border-radius:10px")
        self.play_btn = QPushButton(self.widget_2)
        self.play_btn.setObjectName(u"play_btn")
        self.play_btn.setEnabled(True)
        self.play_btn.setGeometry(QRect(190, 50, 31, 33))
        self.play_btn.setStyleSheet(u"background-image: url(:/newPrefix/Play.png);\n"
"background-repeat:no-repeat;\n"
"background-color:transparent;\n"
"padding:2px;\n"
"")
        self.play_btn.setIconSize(QSize(20, 20))
        self.play_btn.setCheckable(False)
        self.next_btn = QPushButton(self.widget_2)
        self.next_btn.setObjectName(u"next_btn")
        self.next_btn.setEnabled(True)
        self.next_btn.setGeometry(QRect(240, 50, 32, 28))
        self.next_btn.setStyleSheet(u"\n"
"background-image: url(:/newPrefix/Skip Fwd.png);\n"
"background-repeat:no-repeat;\n"
"background-color:transparent;\n"
"padding:2px;")
        self.next_btn.setIconSize(QSize(40, 40))
        self.next_btn.setCheckable(False)
        self.prev_btn = QPushButton(self.widget_2)
        self.prev_btn.setObjectName(u"prev_btn")
        self.prev_btn.setEnabled(True)
        self.prev_btn.setGeometry(QRect(80, 50, 31, 33))
        self.prev_btn.setStyleSheet(u"background-image: url(:/newPrefix/Skip Back.png);\n"
"background-repeat:no-repeat;\n"
"background-color:transparent;\n"
"padding:2px;\n"
"")
        self.prev_btn.setIconSize(QSize(20, 20))
        self.prev_btn.setCheckable(False)
        self.paush_btn = QPushButton(self.widget_2)
        self.paush_btn.setObjectName(u"paush_btn")
        self.paush_btn.setEnabled(True)
        self.paush_btn.setGeometry(QRect(140, 50, 31, 33))
        self.paush_btn.setStyleSheet(u"\n"
"background-image: url(:/newPrefix/Pause.png);\n"
"background-repeat:no-repeat;\n"
"background-color:transparent;\n"
"padding:2px;\n"
"")
        self.paush_btn.setIconSize(QSize(20, 20))
        self.paush_btn.setCheckable(False)
        self.vol_dec_btn = QPushButton(self.widget_2)
        self.vol_dec_btn.setObjectName(u"vol_dec_btn")
        self.vol_dec_btn.setEnabled(True)
        self.vol_dec_btn.setGeometry(QRect(20, 50, 31, 33))
        self.vol_dec_btn.setStyleSheet(u"background-image: url(:/newPrefix/Volume Down.png);\n"
"background-repeat:no-repeat;\n"
"background-color:transparent;\n"
"padding:2px;")
        self.vol_dec_btn.setIconSize(QSize(20, 20))
        self.vol_dec_btn.setCheckable(False)
        self.vol_inc_btn_2 = QPushButton(self.widget_2)
        self.vol_inc_btn_2.setObjectName(u"vol_inc_btn_2")
        self.vol_inc_btn_2.setEnabled(True)
        self.vol_inc_btn_2.setGeometry(QRect(300, 50, 31, 33))
        self.vol_inc_btn_2.setStyleSheet(u"background-image: url(:/newPrefix/Volume Up.png);\n"
"background-repeat:no-repeat;\n"
"background-color:transparent;\n"
"padding:2px;")
        self.vol_inc_btn_2.setIconSize(QSize(20, 20))
        self.vol_inc_btn_2.setCheckable(False)
        self.timebar = QProgressBar(self.widget_2)
        self.timebar.setObjectName(u"timebar")
        self.timebar.setGeometry(QRect(20, 25, 328, 6))
        self.timebar.setStyleSheet(u"")
        self.timebar.setValue(0)
        self.timebar.setTextVisible(False)
        self.linkedln = QLabel(MusicApp)
        self.linkedln.setObjectName(u"linkedln")
        self.linkedln.setGeometry(QRect(240, 30, 101, 31))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI"])
        font2.setPointSize(12)
        font2.setUnderline(True)
        self.linkedln.setFont(font2)
        self.linkedln.setStyleSheet(u"background:transparent;\n"
"color:white")
        self.linkedln.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.github = QLabel(MusicApp)
        self.github.setObjectName(u"github")
        self.github.setGeometry(QRect(350, 30, 101, 31))
        self.github.setFont(font2)
        self.github.setStyleSheet(u"background:transparent;\n"
"color:white;")
        self.github.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(MusicApp)

        QMetaObject.connectSlotsByName(MusicApp)
    # setupUi

    def retranslateUi(self, MusicApp):
        MusicApp.setWindowTitle(QCoreApplication.translate("MusicApp", u"Muisc Player", None))
        self.open_btn.setText(QCoreApplication.translate("MusicApp", u"Open Library", None))
        self.current_track.setText(QCoreApplication.translate("MusicApp", u"Lover.mp3", None))
        self.cover_img.setText("")
        self.play_btn.setText("")
        self.next_btn.setText("")
        self.prev_btn.setText("")
        self.paush_btn.setText("")
        self.vol_dec_btn.setText("")
        self.vol_inc_btn_2.setText("")
        self.linkedln.setText(QCoreApplication.translate("MusicApp", u"Linkedln", None))
        self.github.setText(QCoreApplication.translate("MusicApp", u"Github", None))
    # retranslateUi

