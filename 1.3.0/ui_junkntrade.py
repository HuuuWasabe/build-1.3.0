# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'junkntradeaWtFWN.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
import sqlite3
from Custom_Widgets.Widgets import QCustomSlideMenu

import icons_rc
import logos_rc


# create database
db = sqlite3.connect('wasteManagement.db')
cursor = db.cursor()

# creating member table
cursor.execute("CREATE TABLE IF NOT EXISTS member \
        (memberID INTEGER PRIMARY KEY, firstName TEXT, lastName TEXT, \
               contactNumber TEXT, emailAddress TEXT, username TEXT NOT NULL, password TEXT NOT NULL, \
               rewardPoints INT)")

# creating shops table
cursor.execute("CREATE TABLE IF NOT EXISTS shops (shopID INT PRIMARY KEY, shopAddress TEXT NOT NULL,\
                shopBranch TEXT NOT NULL)")

# creating junks table
cursor.execute("CREATE TABLE IF NOT EXISTS junks (junkID INT PRIMARY KEY, junkName TEXT, junkType TEXT,\
                description TEXT)")

# creating records table
cursor.execute("CREATE TABLE IF NOT EXISTS records (recordID INT PRIMARY KEY, memberID INT NOT NULL, \
           shopID INT NOT NULL, junkID INT NOT NULL, quantity INT NOT NULL, rewardAmount INT NOT NULL, date TEXT,\
           processedIN TEXT NOT NULL, FOREIGN KEY(memberID) REFERENCES member(memberID),\
           FOREIGN KEY(shopID) REFERENCES shops(shopID), FOREIGN KEY(junkID) REFERENCES junks(junkID)\
           FOREIGN KEY(processedIN) REFERENCES shops(shopBranch))")



db.commit()
print("Database creation success.")


# ----------------------------------------------------------------------------------------------------------------------


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1012, 685)
        MainWindow.setMaximumSize(QSize(1280, 720))
        MainWindow.setStyleSheet(u"* {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"#header {\n"
"	background-color:  rgb(45, 60, 81);\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"#centralwidget {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(44, 0, 		    		134, 255), stop:1 rgba(28, 124, 31, 255));\n"
"	border-radius: 20px;\n"
"	\n"
"}\n"
"\n"
"#sideMenu {\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"}\n"
"\n"
"QLabel {\n"
"	color: #fff\n"
"}\n"
"QPushButton {\n"
"	padding: 10px;\n"
"	background-color: rgb(85, 85, 127);\n"
"	border-radius: 5px;\n"
"	color: #fff;\n"
"}\n"
"\n"
"#mainMenu {\n"
"	background-color: #1f232a;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(30, 215, 96);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTextEdit {\n"
"	color: #fff;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 60))
        self.header.setMaximumSize(QSize(16777215, 70))
        self.header.setFrameShape(QFrame.Box)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setMinimumSize(QSize(0, 30))
        self.menuBtn.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.menuBtn.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.menuBtn)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignLeft)

        self.frame_3 = QFrame(self.header)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.appname = QLabel(self.frame_3)
        self.appname.setObjectName(u"appname")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setWeight(75)
        self.appname.setFont(font1)
        self.appname.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.appname)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sideMenu = QCustomSlideMenu(self.frame_2)
        self.sideMenu.setObjectName(u"sideMenu")
        sizePolicy.setHeightForWidth(self.sideMenu.sizePolicy().hasHeightForWidth())
        self.sideMenu.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.sideMenu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 0, 15, 15)
        self.appIcon = QFrame(self.sideMenu)
        self.appIcon.setObjectName(u"appIcon")
        self.appIcon.setFrameShape(QFrame.StyledPanel)
        self.appIcon.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.appIcon)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.appIcon)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"image: url(:/logo/logo/logo_1.2.png);")

        self.verticalLayout_11.addWidget(self.label_10)


        self.verticalLayout_2.addWidget(self.appIcon)

        self.frame_4 = QFrame(self.sideMenu)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(150, 0))
        self.frame_4.setMaximumSize(QSize(150, 16777215))
        font2 = QFont()
        font2.setKerning(True)
        self.frame_4.setFont(font2)
        self.frame_4.setFrameShape(QFrame.Box)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 15, 0, 0)
        self.homeBtn = QPushButton(self.frame_4)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.homeBtn)

        self.profileBtn = QPushButton(self.frame_4)
        self.profileBtn.setObjectName(u"profileBtn")
        self.profileBtn.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profileBtn.setIcon(icon2)
        self.profileBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.profileBtn)

        self.redeemBtn = QPushButton(self.frame_4)
        self.redeemBtn.setObjectName(u"redeemBtn")
        self.redeemBtn.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/shopping-bag.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.redeemBtn.setIcon(icon3)
        self.redeemBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.redeemBtn)

        self.junkBtn = QPushButton(self.frame_4)
        self.junkBtn.setObjectName(u"junkBtn")
        self.junkBtn.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/map-pin.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.junkBtn.setIcon(icon4)
        self.junkBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.junkBtn)


        self.verticalLayout_2.addWidget(self.frame_4, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout.addWidget(self.sideMenu)

        self.mainMenu = QFrame(self.frame_2)
        self.mainMenu.setObjectName(u"mainMenu")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainMenu.sizePolicy().hasHeightForWidth())
        self.mainMenu.setSizePolicy(sizePolicy2)
        self.verticalLayout_5 = QVBoxLayout(self.mainMenu)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.mainMenu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.verticalLayout_12 = QVBoxLayout(self.home)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_7 = QWidget(self.home)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_13 = QVBoxLayout(self.widget_7)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_7 = QFrame(self.widget_7)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 70))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_7)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.homeName = QLabel(self.frame_7)
        self.homeName.setObjectName(u"homeName")
        font3 = QFont()
        font3.setPointSize(25)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setWeight(75)
        self.homeName.setFont(font3)
        self.homeName.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.homeName)


        self.verticalLayout_13.addWidget(self.frame_7)

        self.stack_holder = QFrame(self.widget_7)
        self.stack_holder.setObjectName(u"stack_holder")
        self.stack_holder.setStyleSheet(u"#stack_holder {\n"
"	background-color:  rgb(45, 60, 81);\n"
"	border-radius: 20px;\n"
"}")
        self.stack_holder.setFrameShape(QFrame.StyledPanel)
        self.stack_holder.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.stack_holder)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.stackedWidget_2 = QStackedWidget(self.stack_holder)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.description = QWidget()
        self.description.setObjectName(u"description")
        self.verticalLayout_10 = QVBoxLayout(self.description)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_11 = QLabel(self.description)
        self.label_11.setObjectName(u"label_11")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_11.setFont(font4)

        self.verticalLayout_10.addWidget(self.label_11)

        self.textEdit = QTextEdit(self.description)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_10.addWidget(self.textEdit)

        self.frame_6 = QFrame(self.description)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 50))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.rewardBtn = QPushButton(self.frame_6)
        self.rewardBtn.setObjectName(u"rewardBtn")
        self.rewardBtn.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/tool.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.rewardBtn.setIcon(icon5)

        self.horizontalLayout_7.addWidget(self.rewardBtn)


        self.verticalLayout_10.addWidget(self.frame_6, 0, Qt.AlignHCenter)

        self.stackedWidget_2.addWidget(self.description)
        self.reward = QWidget()
        self.reward.setObjectName(u"reward")
        self.verticalLayout_17 = QVBoxLayout(self.reward)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_5 = QLabel(self.reward)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setMaximumSize(QSize(16777215, 40))
        self.label_5.setFont(font4)

        self.verticalLayout_17.addWidget(self.label_5)

        self.scrollArea = QScrollArea(self.reward)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1605, 2263))
        self.horizontalLayout_8 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setPixmap(QPixmap(u"logo/misc/white_reward.png"))

        self.horizontalLayout_8.addWidget(self.label_12)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_17.addWidget(self.scrollArea)

        self.frame_8 = QFrame(self.reward)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_8)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.wnBtn = QPushButton(self.frame_8)
        self.wnBtn.setObjectName(u"wnBtn")
        self.wnBtn.setFont(font)
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/check-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.wnBtn.setIcon(icon6)

        self.verticalLayout_18.addWidget(self.wnBtn)


        self.verticalLayout_17.addWidget(self.frame_8, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidget_2.addWidget(self.reward)

        self.verticalLayout_15.addWidget(self.stackedWidget_2)


        self.verticalLayout_13.addWidget(self.stack_holder)


        self.verticalLayout_12.addWidget(self.widget_7)

        self.stackedWidget.addWidget(self.home)
        self.profile = QWidget()
        self.profile.setObjectName(u"profile")
        self.verticalLayout_6 = QVBoxLayout(self.profile)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_5 = QFrame(self.profile)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 30))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.profileTitle = QLabel(self.frame_5)
        self.profileTitle.setObjectName(u"profileTitle")
        self.profileTitle.setFont(font1)

        self.horizontalLayout_6.addWidget(self.profileTitle, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.frame_5)

        self.widget_5 = QWidget(self.profile)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_7 = QVBoxLayout(self.widget_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.details = QFrame(self.widget_5)
        self.details.setObjectName(u"details")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.details.sizePolicy().hasHeightForWidth())
        self.details.setSizePolicy(sizePolicy3)
        self.details.setFrameShape(QFrame.StyledPanel)
        self.details.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.details)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.columnA = QFrame(self.details)
        self.columnA.setObjectName(u"columnA")
        self.columnA.setMaximumSize(QSize(150, 16777215))
        self.columnA.setFrameShape(QFrame.StyledPanel)
        self.columnA.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.columnA)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, -1, 9, -1)
        self.label = QLabel(self.columnA)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout_9.addWidget(self.label)

        self.label_2 = QLabel(self.columnA)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_9.addWidget(self.label_2)

        self.label_6 = QLabel(self.columnA)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout_9.addWidget(self.label_6)

        self.label_8 = QLabel(self.columnA)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout_9.addWidget(self.label_8)

        self.label_7 = QLabel(self.columnA)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.verticalLayout_9.addWidget(self.label_7)

        self.label_9 = QLabel(self.columnA)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.verticalLayout_9.addWidget(self.label_9)


        self.horizontalLayout_4.addWidget(self.columnA, 0, Qt.AlignHCenter)

        self.columnB = QFrame(self.details)
        self.columnB.setObjectName(u"columnB")
        self.columnB.setStyleSheet(u"QLineEdit {\n"
"	background-color: #fff;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:Focus {\n"
"	border: 2px solid #0000ff;\n"
"}")
        self.columnB.setFrameShape(QFrame.StyledPanel)
        self.columnB.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.columnB)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.memLine = QLineEdit(self.columnB)
        self.memLine.setObjectName(u"memLine")
        self.memLine.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_8.addWidget(self.memLine)

        self.userLine = QLineEdit(self.columnB)
        self.userLine.setObjectName(u"userLine")
        self.userLine.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_8.addWidget(self.userLine)

        self.fnLine = QLineEdit(self.columnB)
        self.fnLine.setObjectName(u"fnLine")
        self.fnLine.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_8.addWidget(self.fnLine)

        self.lnLine = QLineEdit(self.columnB)
        self.lnLine.setObjectName(u"lnLine")
        self.lnLine.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_8.addWidget(self.lnLine)

        self.contLine = QLineEdit(self.columnB)
        self.contLine.setObjectName(u"contLine")
        self.contLine.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_8.addWidget(self.contLine)

        self.emailLine = QLineEdit(self.columnB)
        self.emailLine.setObjectName(u"emailLine")
        self.emailLine.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_8.addWidget(self.emailLine)


        self.horizontalLayout_4.addWidget(self.columnB)


        self.verticalLayout_7.addWidget(self.details)

        self.logout = QFrame(self.widget_5)
        self.logout.setObjectName(u"logout")
        self.logout.setMaximumSize(QSize(16777215, 55))
        self.logout.setFrameShape(QFrame.StyledPanel)
        self.logout.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.logout)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.logOut = QPushButton(self.logout)
        self.logOut.setObjectName(u"logOut")
        self.logOut.setFont(font)
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logOut.setIcon(icon7)

        self.horizontalLayout_5.addWidget(self.logOut)

        self.updBtn = QPushButton(self.logout)
        self.updBtn.setObjectName(u"updBtn")
        self.updBtn.setFont(font)
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.updBtn.setIcon(icon8)

        self.horizontalLayout_5.addWidget(self.updBtn)

        self.pushButton = QPushButton(self.logout)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon9)

        self.horizontalLayout_5.addWidget(self.pushButton)


        self.verticalLayout_7.addWidget(self.logout, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.widget_5)

        self.stackedWidget.addWidget(self.profile)
        self.redeem = QWidget()
        self.redeem.setObjectName(u"redeem")
        self.verticalLayout_16 = QVBoxLayout(self.redeem)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_3 = QLabel(self.redeem)
        self.label_3.setObjectName(u"label_3")
        font5 = QFont()
        font5.setPointSize(30)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_3.setFont(font5)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_3)

        self.stackedWidget.addWidget(self.redeem)
        self.shops = QWidget()
        self.shops.setObjectName(u"shops")
        self.label_4 = QLabel(self.shops)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(190, 90, 331, 111))
        self.label_4.setFont(font5)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.shops)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.mainMenu)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuBtn.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.appname.setText(QCoreApplication.translate("MainWindow", u"Junk N' Trade", None))
        self.label_10.setText("")
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.profileBtn.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.redeemBtn.setText(QCoreApplication.translate("MainWindow", u"Redeem", None))
        self.junkBtn.setText(QCoreApplication.translate("MainWindow", u"Junk Shops", None))
        self.homeName.setText(QCoreApplication.translate("MainWindow", u"WELCOME TO JUNK N' TRADE!", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Whats's Junk n Trade?", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Junk n' Trade is a waste management system that can help citizens be responsible for their waste disposal and benefit society and the environment. This could start a movement for consumers to be held accountable for every waste they create. The introduction of the reward system in our program will help motivate people to manage their waste properly.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\""
                        "><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">What's new in 1. something?</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">- Added Delete Feature</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">- Added Reward System</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">- Added Junk Shop locations</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragr"
                        "aph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>", None))
        self.rewardBtn.setText(QCoreApplication.translate("MainWindow", u"Reward System", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Reward System", None))
        self.label_12.setText("")
        self.wnBtn.setText(QCoreApplication.translate("MainWindow", u"What's JNT?", None))
        self.profileTitle.setText(QCoreApplication.translate("MainWindow", u"PROFILE", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Member ID:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"First Name:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Last name:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Contact No.:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Email Address:", None))
        # self.memLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"eg. 0001", None))
        self.memLine.setEnabled(False)
        # self.userLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"admin", None))
        self.userLine.setEnabled(False)
        self.fnLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Victor", None))
        self.lnLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Magtanggol", None))
        self.contLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"09123244127", None))
        self.emailLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"sample123@gmail.com", None))
        self.logOut.setText(QCoreApplication.translate("MainWindow", u"LOG OUT", None))
        self.updBtn.setText(QCoreApplication.translate("MainWindow", u"UPDATE PROFILE", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"DELETE ACCOUNT", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"REDEEM", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"JUNK SHOPS", None))
    # retranslateUi



