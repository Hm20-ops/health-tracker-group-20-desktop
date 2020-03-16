# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'goal.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox


class Ui_Goal(object):
    # view constructor for calling setupUi and passing model data to view
    def __init__(self, parent, user_goals):
        self.setupUi(parent, user_goals)

    def setupUi(self, Form, user_goals):
        Form.setObjectName("Form")
        Form.resize(1077, 810)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 1075, 808))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.wrapper = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
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
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.wrapper)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.header = QtWidgets.QLabel(self.wrapper)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.header.setFont(font)
        self.header.setStyleSheet("background:rgb(218, 0, 0); \n"
                                  "color:rgb(63, 63, 63);\n"
                                  "border: none;\n"
                                  "")
        self.header.setIndent(40)
        self.header.setObjectName("header")
        self.verticalLayout_22.addWidget(self.header)
        self.goal = QtWidgets.QFrame(self.wrapper)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.goal.sizePolicy().hasHeightForWidth())
        self.goal.setSizePolicy(sizePolicy)
        self.goal.setMinimumSize(QtCore.QSize(50, 50))
        self.goal.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.goal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.goal.setObjectName("goal")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.goal)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.basic_goal = QtWidgets.QGroupBox(self.goal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.basic_goal.sizePolicy().hasHeightForWidth())
        self.basic_goal.setSizePolicy(sizePolicy)
        self.basic_goal.setTitle("")
        self.basic_goal.setObjectName("basic_goal")
        self.lose_weight_goal = QtWidgets.QDoubleSpinBox(self.basic_goal)
        self.lose_weight_goal.setGeometry(QtCore.QRect(250, 90, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lose_weight_goal.setFont(font)
        self.lose_weight_goal.setDecimals(1)
        self.lose_weight_goal.setProperty("value", 68.5)
        self.lose_weight_goal.setObjectName("lose_weight_goal")
        self.basic_goal_completion_date = QtWidgets.QDateEdit(self.basic_goal)
        self.basic_goal_completion_date.setGeometry(QtCore.QRect(250, 140, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.basic_goal_completion_date.setFont(font)
        self.basic_goal_completion_date.setObjectName("basic_goal_completion_date")
        self.lose_weight_goal_label = QtWidgets.QLineEdit(self.basic_goal)
        self.lose_weight_goal_label.setGeometry(QtCore.QRect(10, 90, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lose_weight_goal_label.setFont(font)
        self.lose_weight_goal_label.setStyleSheet("QLineEdit{\n"
                                                  "background: rgb(222, 222, 222); \n"
                                                  "color:rgb(0, 0, 0);\n"
                                                  "\n"
                                                  "\n"
                                                  "}")
        self.lose_weight_goal_label.setReadOnly(True)
        self.lose_weight_goal_label.setObjectName("lose_weight_goal_label")
        self.basic_goal_completion_date_label = QtWidgets.QLineEdit(self.basic_goal)
        self.basic_goal_completion_date_label.setGeometry(QtCore.QRect(10, 140, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.basic_goal_completion_date_label.setFont(font)
        self.basic_goal_completion_date_label.setStyleSheet("QLineEdit{\n"
                                                            "background: rgb(222, 222, 222); \n"
                                                            "color:rgb(0, 0, 0);\n"
                                                            "\n"
                                                            "\n"
                                                            "}")
        self.basic_goal_completion_date_label.setReadOnly(True)
        self.basic_goal_completion_date_label.setObjectName("basic_goal_completion_date_label")
        self.add_basic_goal = QtWidgets.QPushButton(self.basic_goal)
        self.add_basic_goal.setGeometry(QtCore.QRect(380, 20, 141, 41))
        icon = QtGui.QIcon.fromTheme("sidebar_icon")
        self.add_basic_goal.setIcon(icon)
        self.add_basic_goal.setObjectName("add_basic_goal")
        self.horizontalLayout_9.addWidget(self.basic_goal)
        self.custom_goal = QtWidgets.QGroupBox(self.goal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.custom_goal.sizePolicy().hasHeightForWidth())
        self.custom_goal.setSizePolicy(sizePolicy)
        self.custom_goal.setTitle("")
        self.custom_goal.setObjectName("custom_goal")
        self.goal_description = QtWidgets.QTextEdit(self.custom_goal)
        self.goal_description.setGeometry(QtCore.QRect(250, 70, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.goal_description.setFont(font)
        self.goal_description.setStyleSheet("QTextEdit{\n"
                                            "background-color: rgb(255, 255, 255);\n"
                                            "color:rgb(62, 62, 62);\n"
                                            "border: 1px solid black;\n"
                                            "\n"
                                            "}")
        self.goal_description.setTabStopWidth(80)
        self.goal_description.setObjectName("goal_description")
        self.goal_description_label = QtWidgets.QLineEdit(self.custom_goal)
        self.goal_description_label.setGeometry(QtCore.QRect(10, 70, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.goal_description_label.setFont(font)
        self.goal_description_label.setStyleSheet("QLineEdit{\n"
                                                  "background: rgb(222, 222, 222); \n"
                                                  "color:rgb(0, 0, 0);\n"
                                                  "\n"
                                                  "\n"
                                                  "}")
        self.goal_description_label.setReadOnly(True)
        self.goal_description_label.setObjectName("goal_description_label")
        self.add_custom_goal = QtWidgets.QPushButton(self.custom_goal)
        self.add_custom_goal.setGeometry(QtCore.QRect(380, 20, 141, 41))
        icon = QtGui.QIcon.fromTheme("sidebar_icon")
        self.add_custom_goal.setIcon(icon)
        self.add_custom_goal.setObjectName("add_custom_goal")
        self.completion_date_label = QtWidgets.QLineEdit(self.custom_goal)
        self.completion_date_label.setGeometry(QtCore.QRect(10, 310, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.completion_date_label.setFont(font)
        self.completion_date_label.setStyleSheet("QLineEdit{\n"
                                                 "background: rgb(222, 222, 222); \n"
                                                 "color:rgb(0, 0, 0);\n"
                                                 "\n"
                                                 "\n"
                                                 "}")
        self.completion_date_label.setReadOnly(True)
        self.completion_date_label.setObjectName("completion_date_label")
        self.completion_date = QtWidgets.QDateEdit(self.custom_goal)
        self.completion_date.setGeometry(QtCore.QRect(250, 310, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.completion_date.setFont(font)
        self.completion_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 4, 21), QtCore.QTime(0, 0, 0)))
        self.completion_date.setObjectName("completion_date")
        self.days_label = QtWidgets.QLineEdit(self.custom_goal)
        self.days_label.setGeometry(QtCore.QRect(10, 230, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.days_label.setFont(font)
        self.days_label.setStyleSheet("QLineEdit{\n"
                                      "background: rgb(222, 222, 222); \n"
                                      "color:rgb(0, 0, 0);\n"
                                      "\n"
                                      "\n"
                                      "}")
        self.days_label.setReadOnly(True)
        self.days_label.setObjectName("days_label")
        self.period_label = QtWidgets.QLineEdit(self.custom_goal)
        self.period_label.setGeometry(QtCore.QRect(10, 270, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.period_label.setFont(font)
        self.period_label.setStyleSheet("QLineEdit{\n"
                                        "background: rgb(222, 222, 222); \n"
                                        "color:rgb(0, 0, 0);\n"
                                        "\n"
                                        "\n"
                                        "}")
        self.period_label.setReadOnly(True)
        self.period_label.setObjectName("period_label")
        self.days = QtWidgets.QSpinBox(self.custom_goal)
        self.days.setGeometry(QtCore.QRect(250, 230, 271, 31))
        self.days.setProperty("value", 3)
        self.days.setObjectName("days")
        self.period = QtWidgets.QSpinBox(self.custom_goal)
        self.period.setGeometry(QtCore.QRect(250, 270, 271, 31))
        self.period.setProperty("value", 7)
        self.period.setObjectName("period")
        self.info_text = QtWidgets.QLabel(self.custom_goal)
        self.info_text.setGeometry(QtCore.QRect(70, 170, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.info_text.setFont(font)
        self.info_text.setObjectName("info_text")
        self.horizontalLayout_9.addWidget(self.custom_goal)
        self.verticalLayout_22.addWidget(self.goal)
        self.Your_goals_header = QtWidgets.QLabel(self.wrapper)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Your_goals_header.sizePolicy().hasHeightForWidth())
        self.Your_goals_header.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Your_goals_header.setFont(font)
        self.Your_goals_header.setStyleSheet("QLabel{\n"
                                             "background:rgb(255, 255, 255); \n"
                                             "color:rgb(59, 59, 59);\n"
                                             "border: none;\n"
                                             "}")
        self.Your_goals_header.setWordWrap(False)
        self.Your_goals_header.setObjectName("Your_goals_header")
        self.verticalLayout_22.addWidget(self.Your_goals_header)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.your_goals_frame = QtWidgets.QFrame(self.wrapper)
        self.your_goals_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.your_goals_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.your_goals_frame.setObjectName("your_goals_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.your_goals_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.display_goals(user_goals)
        self.verticalLayout_2.addWidget(self.your_goals_frame)
        self.verticalLayout_22.addLayout(self.verticalLayout_2)
        self.horizontalLayout_14.addWidget(self.wrapper)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.header.setText(_translate("Form", "Goal"))
        self.lose_weight_goal_label.setText(_translate("Form", "Lose Weight Goal (kg)"))
        self.basic_goal_completion_date_label.setText(_translate("Form", "Completion Date"))
        self.add_basic_goal.setText(_translate("Form", "Add Basic Goal"))
        self.goal_description.setHtml(_translate("Form",
                                                 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                 "p, li { white-space: pre-wrap; }\n"
                                                 "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                                 "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.goal_description.setPlaceholderText(_translate("Form", "Enter goal description"))
        self.goal_description_label.setText(_translate("Form", "Goal Description"))
        self.add_custom_goal.setText(_translate("Form", "Add Custom Goal"))
        self.completion_date_label.setText(_translate("Form", "Completion Date"))
        self.days_label.setText(_translate("Form", "Days"))
        self.period_label.setText(_translate("Form", "Period"))
        self.info_text.setText(_translate("Form", "Explain how many days per period do you want to repeat this goal"))
        self.Your_goals_header.setText(_translate("Form", "Your Goals"))


    def display_goals(self, goals):
        from datetime import datetime
        if goals is None:
            print('No goals set yet')
            no_goal_text = QtWidgets.QLabel(self.your_goals_frame)
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
            # set up the goal box
            setattr(self, f'goal_{i + 1}', QtWidgets.QGroupBox(self.your_goals_frame))
            mygoal = getattr(self, f'goal_{i + 1}')
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                               QtWidgets.QSizePolicy.MinimumExpanding)
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

            # set goal completion date
            setattr(self, f'goal{i + 1}_date', QtWidgets.QLabel(mygoal))
            deadline = getattr(self, f'goal{i + 1}_date')
            font = QtGui.QFont()
            font.setPointSize(15)
            deadline.setFont(font)
            deadline.setStyleSheet("background: none;")
            deadline.setWordWrap(False)
            deadline.setObjectName(f"goal{i + 1}_deadline")
            deadline.setText('Completion date: ' + datetime.strftime(goal.date, '%d/%m/%Y'))
            verticalLayout.addWidget(deadline)

            # set goal description
            setattr(self, f'goal{i + 1}_description', QtWidgets.QLabel(mygoal))
            mygoal_description = getattr(self, f'goal{i + 1}_description')
            font = QtGui.QFont()
            font.setPointSize(20)
            mygoal_description.setFont(font)
            mygoal_description.setStyleSheet("QLabel{\n"
                                             "background:rgb(217, 217, 217); \n"
                                             "color:rgb(62, 62, 62);\n"
                                             "}")
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
            self.verticalLayout_3.addWidget(mygoal)
