# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class Ui_Home(object):
    def __init__(self, parent, goals, food_calorie=0, calorie_burnt=0, data=[]):
        self.setupUi(parent, goals, food_calorie, calorie_burnt, data)

    def setupUi(self, Home, goals, food_calorie, calorie_burnt, data):
        Home.setObjectName("Home")
        Home.resize(1500, 794)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Home)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        # main content area
        self.scrollArea = QtWidgets.QScrollArea(Home)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setStyleSheet("QScrollBar:vertical {\n"
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
                                      "}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1084, 792))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        # content wrapper
        self.wrapper = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wrapper.sizePolicy().hasHeightForWidth())
        self.wrapper.setSizePolicy(sizePolicy)
        self.wrapper.setStyleSheet("QFrame{\n"
                                   "background-color: rgb(255, 255, 255);\n"
                                   "color:rgb(62, 62, 62);\n"
                                   "border: none;\n"
                                   "\n"
                                   "}")
        self.wrapper.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.wrapper.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wrapper.setObjectName("wrapper")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.wrapper)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        # color daily summary header
        self.header = QtWidgets.QLabel(self.wrapper)
        self.header.setStyleSheet("QLabel{\n"
                                  "background:rgb(218, 0, 0); \n"
                                  "color:rgb(59, 59, 59);\n"
                                  "border: none;\n"
                                  "}")
        self.header.setIndent(40)
        self.header.setObjectName("header")
        self.verticalLayout.addWidget(self.header)
        self.daily_summary = QtWidgets.QFrame(self.wrapper)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.daily_summary.sizePolicy().hasHeightForWidth())
        self.daily_summary.setSizePolicy(sizePolicy)
        self.daily_summary.setStyleSheet("")
        self.daily_summary.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.daily_summary.setFrameShadow(QtWidgets.QFrame.Raised)
        self.daily_summary.setObjectName("daily_summary")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.daily_summary)
        self.verticalLayout_2.setContentsMargins(100, 30, 100, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.day_streak = QtWidgets.QLabel(self.daily_summary)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.day_streak.setFont(font)
        self.day_streak.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.day_streak.setObjectName("day_streak")
        self.verticalLayout_2.addWidget(self.day_streak)

        # box that contains calorie goal info
        self.calorie_tracker = QtWidgets.QGroupBox(self.daily_summary)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.calorie_tracker.sizePolicy().hasHeightForWidth())
        self.calorie_tracker.setSizePolicy(sizePolicy)
        self.calorie_tracker.setStyleSheet("QGroupBox{\n"
                                           "background: rgb(222, 222, 222); \n"
                                           "color:rgb(122, 122, 122);\n"
                                           "\n"
                                           "\n"
                                           "}")
        self.calorie_tracker.setTitle("")
        self.calorie_tracker.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.calorie_tracker.setCheckable(False)
        self.calorie_tracker.setObjectName("calorie_tracker")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.calorie_tracker)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.food_label = QtWidgets.QLabel(self.calorie_tracker)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.food_label.setFont(font)
        self.food_label.setStyleSheet("background: none;")
        self.food_label.setWordWrap(False)
        self.food_label.setObjectName("food_label")
        self.gridLayout_4.addWidget(self.food_label, 0, 5, 1, 2, QtCore.Qt.AlignRight)
        self.food = QtWidgets.QLCDNumber(self.calorie_tracker)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 222, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 62, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 62, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 222, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 222, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 222, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 62, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 62, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 222, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 222, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 62, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 222, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 62, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 62, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 222, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 222, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.food.setPalette(palette)
        self.food.setStyleSheet("QLCDNumber{\n"
                                "background:rgb(222, 222, 222); \n"
                                "color:rgb(62, 62, 62);\n"
                                "border: none;\n"
                                "\n"
                                "}")
        self.food.setProperty("intValue", food_calorie)
        self.food.setObjectName("food")
        self.gridLayout_4.addWidget(self.food, 1, 6, 1, 1, QtCore.Qt.AlignHCenter)
        self.exercise_label = QtWidgets.QLabel(self.calorie_tracker)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.exercise_label.setFont(font)
        self.exercise_label.setStyleSheet("background: none;")
        self.exercise_label.setWordWrap(False)
        self.exercise_label.setObjectName("exercise_label")
        self.gridLayout_4.addWidget(self.exercise_label, 0, 7, 1, 1, QtCore.Qt.AlignRight)
        self.net_calorie_label = QtWidgets.QLabel(self.calorie_tracker)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.net_calorie_label.setFont(font)
        self.net_calorie_label.setStyleSheet("background: none;")
        self.net_calorie_label.setWordWrap(False)
        self.net_calorie_label.setObjectName("net_calorie_label")
        self.gridLayout_4.addWidget(self.net_calorie_label, 0, 8, 1, 1, QtCore.Qt.AlignHCenter)
        self.exercise = QtWidgets.QLCDNumber(self.calorie_tracker)
        self.exercise.setPalette(palette)
        self.exercise.setStyleSheet("QLCDNumber{\n"
                                    "background:rgb(222, 222, 222); \n"
                                    "color:rgb(62, 62, 62);\n"
                                    "border: none;\n"
                                    "\n"
                                    "}")
        self.exercise.setProperty("intValue", calorie_burnt)
        self.exercise.setObjectName("exercise")
        self.gridLayout_4.addWidget(self.exercise, 1, 7, 1, 1, QtCore.Qt.AlignHCenter)
        self.calorine_progress = QtWidgets.QProgressBar(self.calorie_tracker)
        self.calorine_progress.setStyleSheet("QProgressBar::chunk {\n"
                                             "     background-color: #3add36;\n"
                                             "     width: 1px;\n"
                                             " }\n"
                                             "\n"
                                             " QProgressBar {\n"
                                             "     \n"
                                             "     border-radius: 0px;\n"
                                             "     text-align: center;\n"
                                             " }")
        self.calorine_progress.setProperty("value", 0)
        self.calorine_progress.setObjectName("calorine_progress")
        self.gridLayout_4.addWidget(self.calorine_progress, 2, 0, 1, 9)
        self.net_calorie = QtWidgets.QLCDNumber(self.calorie_tracker)
        self.net_calorie.setPalette(palette)
        self.net_calorie.setStyleSheet("QLCDNumber{\n"
                                       "background:rgb(222, 222, 222); \n"
                                       "color:rgb(62, 62, 62);\n"
                                       "border: none;\n"
                                       "\n"
                                       "}")
        self.net_calorie.setProperty("intValue", food_calorie - calorie_burnt)
        self.net_calorie.setObjectName("net_calorie")
        self.gridLayout_4.addWidget(self.net_calorie, 1, 8, 1, 1, QtCore.Qt.AlignHCenter)
        self.line = QtWidgets.QFrame(self.calorie_tracker)
        self.line.setEnabled(True)
        self.line.setStyleSheet("background: none;")
        self.line.setLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 0, 4, 1, 1)
        self.verticalLayout_2.addWidget(self.calorie_tracker)
        self.button_frame = QtWidgets.QFrame(self.daily_summary)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_frame.sizePolicy().hasHeightForWidth())
        self.button_frame.setSizePolicy(sizePolicy)
        self.button_frame.setStyleSheet("")
        self.button_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_frame.setObjectName("button_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.button_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(250)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.add_exercise = QtWidgets.QPushButton(self.button_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_exercise.sizePolicy().hasHeightForWidth())
        self.add_exercise.setSizePolicy(sizePolicy)
        self.add_exercise.setStyleSheet("padding: 10 15 10 15;")
        icon = QtGui.QIcon("./sidebar_icon/plus.png")
        self.add_exercise.setIcon(icon)
        self.add_exercise.setObjectName("add_exercise")
        self.horizontalLayout_3.addWidget(self.add_exercise)
        self.add_diet = QtWidgets.QPushButton(self.button_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_diet.sizePolicy().hasHeightForWidth())
        self.add_diet.setSizePolicy(sizePolicy)
        self.add_diet.setStyleSheet("padding: 10 25 10 25;")
        icon = QtGui.QIcon("./sidebar_icon/plus.png")
        self.add_diet.setIcon(icon)
        self.add_diet.setObjectName("add_diet")
        self.horizontalLayout_3.addWidget(self.add_diet)
        self.add_weight = QtWidgets.QPushButton(self.button_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_weight.sizePolicy().hasHeightForWidth())
        self.add_weight.setSizePolicy(sizePolicy)
        self.add_weight.setStyleSheet("padding: 10 15 10 15;")
        icon = QtGui.QIcon("./sidebar_icon/plus.png")
        self.add_weight.setIcon(icon)
        self.add_weight.setObjectName("add_weight")
        self.horizontalLayout_3.addWidget(self.add_weight)
        self.verticalLayout_2.addWidget(self.button_frame)

        # show graph
        self.graph = PlotCanvas(self.daily_summary, data)

        self.verticalLayout_2.addWidget(self.graph)
        self.verticalLayout.addWidget(self.daily_summary)
        self.recent_goals = QtWidgets.QLabel(self.wrapper)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recent_goals.sizePolicy().hasHeightForWidth())
        self.recent_goals.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.recent_goals.setFont(font)
        self.recent_goals.setStyleSheet("QLabel{\n"
                                        "background:rgb(255, 255, 255); \n"
                                        "color:rgb(59, 59, 59);\n"
                                        "border: none;\n"
                                        "}")
        self.recent_goals.setWordWrap(False)
        self.recent_goals.setIndent(45)
        self.recent_goals.setObjectName("recent_goals")
        self.verticalLayout.addWidget(self.recent_goals)
        self.goals_frame = QtWidgets.QFrame(self.wrapper)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.goals_frame.sizePolicy().hasHeightForWidth())
        self.goals_frame.setSizePolicy(sizePolicy)
        self.goals_frame.setStyleSheet("QLabel{\n"
                                       "background:rgb(218, 0, 0);\n"
                                       "color:rgb(59, 59, 59);\n"
                                       "border: none;\n"
                                       "}")
        self.goals_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.goals_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.goals_frame.setObjectName("goals_frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.goals_frame)
        self.gridLayout_5.setVerticalSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.display_recent_goals(goals)

        self.verticalLayout.addWidget(self.goals_frame)
        self.horizontalLayout_4.addWidget(self.wrapper)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)

        self.retranslateUi(Home, goals)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home, goals):
        from datetime import datetime
        _translate = QtCore.QCoreApplication.translate
        Home.setWindowTitle(_translate("Home", "Form"))
        self.header.setText(_translate("Home",
                                       "<html><head/><body><p><span style=\" font-family:\'Segoe UI\'; font-size:36pt;\">      Daily Summary</span></p></body></html>"))
        self.day_streak.setText(_translate("Home", "Day Streak 1"))
        self.food_label.setText(_translate("Home", "Food  - "))
        self.exercise_label.setText(_translate("Home", "Exercise ="))
        self.net_calorie_label.setText(_translate("Home", "net calorie"))
        self.add_exercise.setText(_translate("Home", "Add Exercise"))
        self.add_diet.setText(_translate("Home", "Add Diet"))
        self.add_weight.setText(_translate("Home", "Add Weight"))
        self.recent_goals.setText(_translate("Home", "Recent Goals"))
        for i in range(len(goals)):
            if hasattr(self, f'goal_{i + 1}'):
                recent_goal_date = getattr(self, f'goal{i + 1}_date')
                recent_goal_description = getattr(self, f'goal{i + 1}_description')
                recent_goal_date.setText(_translate("Home", datetime.strftime(goals[i].date, '%d/%m/%Y')))
                recent_goal_description.setText(_translate("Home", goals[i].goal_description))


    def display_recent_goals(self, goals):
        if len(goals) == 0:
            print('No goals set yet')
            no_goal_text = QtWidgets.QLabel(self.goals_frame)
            no_goal_text.setFixedWidth(1000)
            font = QtGui.QFont()
            font.setPointSize(20)
            no_goal_text.setFont(font)
            no_goal_text.setStyleSheet("background: none; color: grey;")
            no_goal_text.setWordWrap(False)
            no_goal_text.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            no_goal_text.setObjectName("no_goal_text")
            no_goal_text.setText('No goal was set yet')
            self.gridLayout_5.addWidget(no_goal_text, 0, 0, 1, 1)
            return
        for i, goal in enumerate(goals):
            setattr(self, f'goal_{i + 1}', QtWidgets.QGroupBox(self.goals_frame))
            mygoal = getattr(self, f'goal_{i + 1}')
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(mygoal.sizePolicy().hasHeightForWidth())
            mygoal.setSizePolicy(sizePolicy)
            mygoal.setMinimumSize(QtCore.QSize(200, 0))
            mygoal.setStyleSheet("QGroupBox{\n"
                                 "background:rgb(217, 217, 217); \n"
                                 "color:rgb(62, 62, 62);\n"
                                 "}")
            mygoal.setObjectName(f"goal_{i + 1}")
            verticalLayout = QtWidgets.QVBoxLayout(mygoal)
            setattr(self, f'goal{i + 1}_date', QtWidgets.QLabel(mygoal))
            deadline = getattr(self, f'goal{i + 1}_date')
            font = QtGui.QFont()
            font.setPointSize(15)
            deadline.setFont(font)
            deadline.setStyleSheet("background: none;\n"
                                   "padding: 0 0 0 0;")
            deadline.setWordWrap(False)
            deadline.setObjectName(f"goal{i + 1}_date")
            deadline.setText(str(goal.date))
            verticalLayout.addWidget(deadline)
            setattr(self, f'goal{i + 1}_description', QtWidgets.QLabel(mygoal))
            mygoal_description = getattr(self, f'goal{i + 1}_description')
            font = QtGui.QFont()
            font.setPointSize(20)
            mygoal_description.setFont(font)
            mygoal_description.setStyleSheet("background: none;")
            mygoal_description.setWordWrap(False)
            mygoal_description.setObjectName(f"mygoal_title_{i + 1}")
            mygoal_description.setText(f"{goal.goal_description}")
            verticalLayout.addWidget(mygoal_description)
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
            progressBar.setObjectName(f"goal{i + 1}_progress")
            verticalLayout.addWidget(progressBar)

            self.gridLayout_5.addWidget(mygoal, 0, i, 1, 1)


'''
a canvas class for displaying the graph
'''

class PlotCanvas(FigureCanvas):
    def __init__(self,  parent=None, data=[],width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.data = data

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.MinimumExpanding,
                                   QtWidgets.QSizePolicy.MinimumExpanding)
        FigureCanvas.updateGeometry(self)
        self.plot()

    def plot(self):
        # import random
        # data = [65, 64.9, 64.6, 64.5, 64.5, 64.3, 64.2]  # [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)
        ax.plot(self.data, 'r-')
        ax.set_title('Weight trend')
        plt.setp(ax, xlabel='Day', ylabel='Weight(kg)')
        self.draw()
