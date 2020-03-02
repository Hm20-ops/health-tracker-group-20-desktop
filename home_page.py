# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home_page.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
from math import floor

from PyQt5 import QtCore, QtGui, QtWidgets
import icons_rc

class Ui_Health_tracker(object):
    def setupUi(self, Health_tracker, basic_goals):
        Health_tracker.setObjectName("Health_tracker")
        Health_tracker.resize(1145, 868)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Health_tracker.sizePolicy().hasHeightForWidth())
        Health_tracker.setSizePolicy(sizePolicy)
        Health_tracker.setMinimumSize(QtCore.QSize(480, 360))
        self.centralwidget = QtWidgets.QWidget(Health_tracker)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.side_nav_bar = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.side_nav_bar.sizePolicy().hasHeightForWidth())
        self.side_nav_bar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.side_nav_bar.setFont(font)
        self.side_nav_bar.setStyleSheet("QListWidget{\n"
"background: rgb(63, 63, 63); \n"
"color:rgb(122, 122, 122);\n"
"border: none;\n"
"\n"
"}\n"
"QListWidget::item { \n"
"margin: 10px;\n"
"padding-top: 20px;\n"
"padding-left: 50px;\n"
"}\n"
"QListWidget::item::icon { \n"
"size: 10px;\n"
"}\n"
"")
        self.side_nav_bar.setProperty("showDropIndicator", True)
        self.side_nav_bar.setIconSize(QtCore.QSize(50, 30))
        self.side_nav_bar.setObjectName("side_nav_bar")
        item = QtWidgets.QListWidgetItem()
        icon = QtGui.QIcon("./sidebar_icon/home.svg")
        item.setIcon(icon)
        self.side_nav_bar.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon = QtGui.QIcon("./sidebar_icon/profile.png")
        item.setIcon(icon)
        self.side_nav_bar.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon = QtGui.QIcon("./sidebar_icon/goal.png")
        item.setIcon(icon)
        self.side_nav_bar.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon = QtGui.QIcon("./sidebar_icon/up, arrow, line, progress png icon.png")
        item.setIcon(icon)
        self.side_nav_bar.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon = QtGui.QIcon("./sidebar_icon/runner.png")
        item.setIcon(icon)
        self.side_nav_bar.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon = QtGui.QIcon("./sidebar_icon/vegetarian-diet.png")
        item.setIcon(icon)
        self.side_nav_bar.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon = QtGui.QIcon("./sidebar_icon/group.png")
        item.setIcon(icon)
        self.side_nav_bar.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        icon = QtGui.QIcon("./sidebar_icon/logout-512.png")
        item.setIcon(icon)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.side_nav_bar.addItem(item)
        self.horizontalLayout.addWidget(self.side_nav_bar)
        self.display_page = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.display_page.sizePolicy().hasHeightForWidth())
        self.display_page.setSizePolicy(sizePolicy)
        self.display_page.setLineWidth(0)
        self.display_page.setObjectName("display_page")
        self.Home = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Home.sizePolicy().hasHeightForWidth())
        self.Home.setSizePolicy(sizePolicy)
        self.Home.setObjectName("Home")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.Home)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.Home_area = QtWidgets.QScrollArea(self.Home)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Home_area.sizePolicy().hasHeightForWidth())
        self.Home_area.setSizePolicy(sizePolicy)
        self.Home_area.setStyleSheet("QScrollBar:vertical {\n"
"    border: 0px solid #999999;\n"
"    border-radius: 5px;\n"
"    background: none;\n"
"    background-color: transparent;\n"
"    width: 10px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background-color: rgba(150, 150, 150, 80);\n"
"    border: 0px solid #999999;\n"
"    border-color: transparent;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    min-height: 0px;\n"
"}\n"
"QScrollBar::handle:vertical::hover {\n"
"    background-color: rgba(100, 100, 100, 230);\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical { \n"
"    height: 0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"    ")
        self.Home_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.Home_area.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Home_area.setWidgetResizable(False)
        self.Home_area.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Home_area.setObjectName("Home_area")
        self.wrapper = QtWidgets.QWidget()
        self.wrapper.setGeometry(QtCore.QRect(0, 0, 923, 843))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wrapper.sizePolicy().hasHeightForWidth())
        self.wrapper.setSizePolicy(sizePolicy)
        self.wrapper.setObjectName("wrapper")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.wrapper)
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Home_frame = QtWidgets.QFrame(self.wrapper)
        self.Home_frame.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Home_frame.sizePolicy().hasHeightForWidth())
        self.Home_frame.setSizePolicy(sizePolicy)
        self.Home_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Home_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Home_frame.setObjectName("Home_frame")
        self.line_2 = QtWidgets.QFrame(self.Home_frame)
        self.line_2.setGeometry(QtCore.QRect(10, 80, 891, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setStyleSheet("background: none")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.graph = QtWidgets.QTextBrowser(self.Home_frame)
        self.graph.setGeometry(QtCore.QRect(80, 350, 571, 201))
        self.graph.setObjectName("graph")
        self.daily_summary = QtWidgets.QGroupBox(self.Home_frame)
        self.daily_summary.setGeometry(QtCore.QRect(80, 130, 571, 141))
        self.daily_summary.setStyleSheet("")
        self.daily_summary.setTitle("")
        self.daily_summary.setCheckable(False)
        self.daily_summary.setObjectName("daily_summary")
        self.net_calorine = QtWidgets.QLabel(self.daily_summary)
        self.net_calorine.setGeometry(QtCore.QRect(260, 40, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.net_calorine.setFont(font)
        self.net_calorine.setStyleSheet("background: none;")
        self.net_calorine.setWordWrap(False)
        self.net_calorine.setObjectName("net_calorine")
        self.calorie_goal = QtWidgets.QLabel(self.daily_summary)
        self.calorie_goal.setGeometry(QtCore.QRect(70, 40, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.calorie_goal.setFont(font)
        self.calorie_goal.setStyleSheet("background: none;")
        self.calorie_goal.setWordWrap(False)
        self.calorie_goal.setObjectName("calorie_goal")
        self.calorine_line = QtWidgets.QFrame(self.daily_summary)
        self.calorine_line.setGeometry(QtCore.QRect(240, 40, 3, 61))
        self.calorine_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.calorine_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.calorine_line.setObjectName("calorine_line")
        self.add_diet = QtWidgets.QPushButton(self.Home_frame)
        self.add_diet.setGeometry(QtCore.QRect(320, 290, 91, 41))
        icon = QtGui.QIcon("./sidebar_icon/plus-304947_640.png")
        self.add_diet.setIcon(icon)
        self.add_diet.setObjectName("add_diet")
        self.day_streak = QtWidgets.QLabel(self.Home_frame)
        self.day_streak.setGeometry(QtCore.QRect(540, 100, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.day_streak.setFont(font)
        self.day_streak.setObjectName("day_streak")
        self.add_exercise = QtWidgets.QPushButton(self.Home_frame)
        self.add_exercise.setGeometry(QtCore.QRect(80, 290, 91, 41))
        icon = QtGui.QIcon("./sidebar_icon/plus-304947_640.png")
        self.add_exercise.setIcon(icon)
        self.add_exercise.setObjectName("add_exercise")
        self.add_weight = QtWidgets.QPushButton(self.Home_frame)
        self.add_weight.setGeometry(QtCore.QRect(560, 290, 91, 41))
        icon = QtGui.QIcon("./sidebar_icon/plus-304947_640.png")
        self.add_weight.setIcon(icon)
        self.add_weight.setObjectName("add_weight")
        self.Daily_summary_header = QtWidgets.QLabel(self.Home_frame)
        self.Daily_summary_header.setGeometry(QtCore.QRect(20, 10, 361, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Daily_summary_header.sizePolicy().hasHeightForWidth())
        self.Daily_summary_header.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)

        self.Daily_summary_header.setFont(font)
        self.Daily_summary_header.setStyleSheet("background: none;")
        self.Daily_summary_header.setWordWrap(False)
        self.Daily_summary_header.setObjectName("Daily_summary_header")
        self.Your_goals_header = QtWidgets.QLabel(self.Home_frame)
        self.Your_goals_header.setGeometry(QtCore.QRect(20, 560, 361, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.Your_goals_header.setFont(font)
        self.Your_goals_header.setStyleSheet("background: none;")
        self.Your_goals_header.setWordWrap(False)
        self.Your_goals_header.setObjectName("Your_goals_header")
        self.line_3 = QtWidgets.QFrame(self.Home_frame)
        self.line_3.setGeometry(QtCore.QRect(20, 620, 891, 20))
        self.line_3.setStyleSheet("background: none")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.goals = QtWidgets.QFrame(self.Home_frame)
        self.goals.setGeometry(QtCore.QRect(10, 640, 831, 151))
        self.goals.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.goals.setFrameShadow(QtWidgets.QFrame.Raised)
        self.goals.setObjectName("goals")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.goals)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.display_all_goal(basic_goals)
#         self.goal_1 = QtWidgets.QGroupBox(self.goals)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.goal_1.sizePolicy().hasHeightForWidth())
#         self.goal_1.setSizePolicy(sizePolicy)
#         self.goal_1.setMinimumSize(QtCore.QSize(257, 0))
#         self.goal_1.setStyleSheet("")
#         self.goal_1.setTitle("")
#         self.goal_1.setObjectName("goal_1")
#         self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.goal_1)
#         self.verticalLayout_4.setObjectName("verticalLayout_4")
#         self.label_9 = QtWidgets.QLabel(self.goal_1)
#         font = QtGui.QFont()
#         font.setPointSize(20)
#         self.label_9.setFont(font)
#         self.label_9.setStyleSheet("background: none;")
#         self.label_9.setWordWrap(False)
#         self.label_9.setObjectName("label_9")
#         self.verticalLayout_4.addWidget(self.label_9)
#         self.label_8 = QtWidgets.QLabel(self.goal_1)
#         font = QtGui.QFont()
#         font.setPointSize(20)
#         self.label_8.setFont(font)
#         self.label_8.setStyleSheet("background: none;")
#         self.label_8.setWordWrap(False)
#         self.label_8.setObjectName("label_8")
#         self.verticalLayout_4.addWidget(self.label_8)
#         self.progressBar_2 = QtWidgets.QProgressBar(self.goal_1)
#         self.progressBar_2.setStyleSheet("QProgressBar::chunk {\n"
# "     background-color: #3add36;\n"
# "     width: 1px;\n"
# " }\n"
# "\n"
# " QProgressBar {\n"
# "     \n"
# "     border-radius: 0px;\n"
# "     text-align: center;\n"
# " }")
#         self.progressBar_2.setProperty("value", 10)
#         self.progressBar_2.setInvertedAppearance(False)
#         self.progressBar_2.setObjectName("progressBar_2")
#         self.verticalLayout_4.addWidget(self.progressBar_2)
#         self.gridLayout_3.addWidget(self.goal_1, 0, 0, 1, 1)
#         self.goal_2 = QtWidgets.QGroupBox(self.goals)
#         self.goal_2.setStyleSheet("")
#         self.goal_2.setTitle("")
#         self.goal_2.setObjectName("goal_2")
#         self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.goal_2)
#         self.verticalLayout_5.setObjectName("verticalLayout_5")
#         self.label_11 = QtWidgets.QLabel(self.goal_2)
#         font = QtGui.QFont()
#         font.setPointSize(20)
#         self.label_11.setFont(font)
#         self.label_11.setStyleSheet("background: none;")
#         self.label_11.setWordWrap(False)
#         self.label_11.setObjectName("label_11")
#         self.verticalLayout_5.addWidget(self.label_11)
#         self.label_10 = QtWidgets.QLabel(self.goal_2)
#         font = QtGui.QFont()
#         font.setPointSize(14)
#         self.label_10.setFont(font)
#         self.label_10.setStyleSheet("background: none;")
#         self.label_10.setWordWrap(False)
#         self.label_10.setObjectName("label_10")
#         self.verticalLayout_5.addWidget(self.label_10)
#         self.progressBar_3 = QtWidgets.QProgressBar(self.goal_2)
#         self.progressBar_3.setStyleSheet("QProgressBar::chunk {\n"
# "     background-color: #3add36;\n"
# "     width: 1px;\n"
# " }\n"
# "\n"
# " QProgressBar {\n"
# "     \n"
# "     border-radius: 0px;\n"
# "     text-align: center;\n"
# " }")
#         self.progressBar_3.setProperty("value", 24)
#         self.progressBar_3.setObjectName("progressBar_3")
#         self.verticalLayout_5.addWidget(self.progressBar_3)
#         self.gridLayout_3.addWidget(self.goal_2, 0, 1, 1, 1)
#         self.goal_3 = QtWidgets.QGroupBox(self.goals)
#         self.goal_3.setStyleSheet("")
#         self.goal_3.setTitle("")
#         self.goal_3.setObjectName("goal_3")
#         self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.goal_3)
#         self.verticalLayout_6.setObjectName("verticalLayout_6")
#         self.label_15 = QtWidgets.QLabel(self.goal_3)
#         font = QtGui.QFont()
#         font.setPointSize(20)
#         self.label_15.setFont(font)
#         self.label_15.setStyleSheet("background: none;")
#         self.label_15.setWordWrap(False)
#         self.label_15.setObjectName("label_15")
#         self.verticalLayout_6.addWidget(self.label_15)
#         self.label_14 = QtWidgets.QLabel(self.goal_3)
#         font = QtGui.QFont()
#         font.setPointSize(14)
#         self.label_14.setFont(font)
#         self.label_14.setStyleSheet("background: none;")
#         self.label_14.setWordWrap(False)
#         self.label_14.setObjectName("label_14")
#         self.verticalLayout_6.addWidget(self.label_14)
#         self.progressBar_5 = QtWidgets.QProgressBar(self.goal_3)
#         self.progressBar_5.setStyleSheet("QProgressBar::chunk {\n"
# "     background-color: #3add36;\n"
# "     width: 1px;\n"
# " }\n"
# "\n"
# " QProgressBar {\n"
# "     \n"
# "     border-radius: 0px;\n"
# "     text-align: center;\n"
# " }")
#         self.progressBar_5.setProperty("value", 24)
#         self.progressBar_5.setObjectName("progressBar_5")
#         self.verticalLayout_6.addWidget(self.progressBar_5)
#         self.gridLayout_3.addWidget(self.goal_3, 0, 2, 1, 1)
        self.gridLayout_4.addWidget(self.Home_frame, 0, 0, 1, 1)
        self.Home_area.setWidget(self.wrapper)
        self.gridLayout_5.addWidget(self.Home_area, 0, 0, 1, 1)
        self.display_page.addWidget(self.Home)

        self.Profile = QtWidgets.QWidget()
        self.Profile.setObjectName("Profile")
        self.display_page.addWidget(self.Profile)
        self.Goal = QtWidgets.QWidget()
        self.Goal.setObjectName("Goal")
        self.display_page.addWidget(self.Goal)
        self.Progress = QtWidgets.QWidget()
        self.Progress.setObjectName("Progress")
        self.display_page.addWidget(self.Progress)
        self.Exercise = QtWidgets.QWidget()
        self.Exercise.setObjectName("Exercise")
        self.display_page.addWidget(self.Exercise)
        self.Diet = QtWidgets.QWidget()
        self.Diet.setObjectName("Diet")
        self.display_page.addWidget(self.Diet)
        self.Group = QtWidgets.QWidget()
        self.Group.setObjectName("Group")
        self.display_page.addWidget(self.Group)
        self.horizontalLayout.addWidget(self.display_page)
        self.gridLayout_6.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        Health_tracker.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Health_tracker)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1145, 21))
        self.menubar.setObjectName("menubar")
        Health_tracker.setMenuBar(self.menubar)

        self.retranslateUi(Health_tracker)
        self.display_page.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Health_tracker)

    def retranslateUi(self, Health_tracker):
        _translate = QtCore.QCoreApplication.translate
        Health_tracker.setWindowTitle(_translate("Health_tracker", "MainWindow"))
        __sortingEnabled = self.side_nav_bar.isSortingEnabled()
        self.side_nav_bar.setSortingEnabled(False)
        item = self.side_nav_bar.item(0)
        item.setText(_translate("Health_tracker", " Home"))
        item = self.side_nav_bar.item(1)
        item.setText(_translate("Health_tracker", " Profile"))
        item = self.side_nav_bar.item(2)
        item.setText(_translate("Health_tracker", " Goal"))
        item = self.side_nav_bar.item(3)
        item.setText(_translate("Health_tracker", " Progress"))
        item = self.side_nav_bar.item(4)
        item.setText(_translate("Health_tracker", " Exercise"))
        item = self.side_nav_bar.item(5)
        item.setText(_translate("Health_tracker", " Diet"))
        item = self.side_nav_bar.item(6)
        item.setText(_translate("Health_tracker", " Group"))
        item = self.side_nav_bar.item(7)
        item.setText(_translate("Health_tracker", " Log out"))
        self.side_nav_bar.setSortingEnabled(__sortingEnabled)
        self.graph.setHtml(_translate("Health_tracker", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600;\">Graph</span></p></body></html>"))
        self.net_calorine.setText(_translate("Health_tracker", "Food - Exercise = Net"))
        self.calorie_goal.setText(_translate("Health_tracker", "Calorie Goal"))
        self.add_diet.setText(_translate("Health_tracker", "Add Diet"))
        self.day_streak.setText(_translate("Health_tracker", "Day Streak 1"))
        self.add_exercise.setText(_translate("Health_tracker", "Add Exercise"))
        self.add_weight.setText(_translate("Health_tracker", "Add Weight"))
        self.Daily_summary_header.setText(_translate("Health_tracker", "Daily Summary"))
        self.Your_goals_header.setText(_translate("Health_tracker", "Your Goals"))
        # self.label_9.setText(_translate("Health_tracker", "Group 1"))
        # self.label_8.setText(_translate("Health_tracker", "lose 10kg"))
        # self.label_11.setText(_translate("Health_tracker", "Group 2"))
        # self.label_10.setText(_translate("Health_tracker", "go to gym at least twice a week"))
        # self.label_15.setText(_translate("Health_tracker", "Group 3"))
        # self.label_14.setText(_translate("Health_tracker", "jogging everyday"))

    def display_all_goal(self, goals):
        if len(goals) == 0 or goals is None:
            print('No goals set yet')
            no_goal_text = QtWidgets.QLabel(self.goals)
            no_goal_text.setFixedWidth(1000)
            font = QtGui.QFont()
            font.setPointSize(10)
            no_goal_text.setFont(font)
            no_goal_text.setStyleSheet("background: none; color: grey;")
            no_goal_text.setWordWrap(False)
            no_goal_text.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            no_goal_text.setObjectName("no_goal_text")
            no_goal_text.setText('No goal was set yet')
            return
        for i, goal in enumerate(goals):
            setattr(self, f'mygoal_{i}', QtWidgets.QGroupBox(self.goals))
            mygoal = getattr(self, f'mygoal_{i}')
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(mygoal.sizePolicy().hasHeightForWidth())
            mygoal.setSizePolicy(sizePolicy)
            mygoal.setMinimumSize(QtCore.QSize(200, 300))
            # self.goal_1.setStyleSheet("")
            # self.goal_1.setTitle("")
            mygoal.setObjectName(f"goal_{i}")
            verticalLayout = QtWidgets.QVBoxLayout(mygoal)
            #self.verticalLayout_4.setObjectName("verticalLayout_4")
            deadline = QtWidgets.QLabel(mygoal)
            font = QtGui.QFont()
            font.setPointSize(20)
            deadline.setFont(font)
            deadline.setStyleSheet("background: none;")
            deadline.setWordWrap(False)
            deadline.setObjectName(f"mygoal_{i}_deadline")
            deadline.setText(str(goal['date']))
            verticalLayout.addWidget(deadline)
            mygoal_title = QtWidgets.QLabel(mygoal)
            font = QtGui.QFont()
            font.setPointSize(20)
            mygoal_title.setFont(font)
            mygoal_title.setStyleSheet("background: none;")
            mygoal_title.setWordWrap(False)
            mygoal_title.setObjectName(f"mygoal_title_{i}")
            mygoal_title.setText(f"get to {goal['target_weight']} kg")
            verticalLayout.addWidget(mygoal_title)
            progressBar = QtWidgets.QProgressBar(mygoal)
            progressBar.setStyleSheet("QProgressBar::chunk {\n"
                                     "     background-color: #3add36;\n"
                                     "     width: 1px;\n"
                                     " }\n"
                                     "\n"
                                     " QProgressBar {\n"
                                     "     \n"
                                     "     border-radius: 0px;\n"
                                     "     text-align: center;\n"
                                     " }")
            progressBar.setProperty("value", 10)
            progressBar.setInvertedAppearance(False)
            progressBar.setObjectName(f"progressBar_{i}")
            verticalLayout.addWidget(progressBar)
            # row = floor(i/3)
            # column = i % 3
            self.gridLayout_3.addWidget(mygoal, *divmod(i, 3))
