# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'group2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_group(object):

    def __init__(self, parent, group, all_groups):
        self.setupUi(parent, group, all_groups)

    def setupUi(self, Form, group, all_groups):
        Form.setObjectName("group")
        Form.resize(1382, 857)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(500, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.group_scrollArea = QtWidgets.QWidget()
        self.group_scrollArea.setGeometry(QtCore.QRect(0, 0, 1359, 971))
        self.group_scrollArea.setObjectName("group_scrollArea")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.group_scrollArea)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.group_frame = QtWidgets.QFrame(self.group_scrollArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_frame.sizePolicy().hasHeightForWidth())
        self.group_frame.setSizePolicy(sizePolicy)
        self.group_frame.setStyleSheet("QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"color:rgb(62, 62, 62);\n"
"border: none;\n"
"\n"
"}")
        self.group_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.group_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.group_frame.setObjectName("group_frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.group_frame)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.group_header = QtWidgets.QLabel(self.group_frame)
        self.group_header.setStyleSheet("QLabel{\n"
"background:rgb(218, 0, 0); \n"
"color:rgb(59, 59, 59);\n"
"border: none;\n"
"}")
        self.group_header.setIndent(40)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_header.sizePolicy().hasHeightForWidth())
        self.group_header.setSizePolicy(sizePolicy)
        self.group_header.setObjectName("group_header")
        self.verticalLayout_6.addWidget(self.group_header)
        self.group_add_join = QtWidgets.QFrame(self.group_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_add_join.sizePolicy().hasHeightForWidth())
        self.group_add_join.setSizePolicy(sizePolicy)
        self.group_add_join.setMinimumSize(QtCore.QSize(50, 50))
        self.group_add_join.setStyleSheet("")
        self.group_add_join.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.group_add_join.setFrameShadow(QtWidgets.QFrame.Raised)
        self.group_add_join.setObjectName("group_add_join")
        self.gridLayout = QtWidgets.QGridLayout(self.group_add_join)
        self.gridLayout.setContentsMargins(100, 30, 100, 30)
        self.gridLayout.setObjectName("gridLayout")
        self.search_group_box = QtWidgets.QGroupBox(self.group_add_join)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_group_box.sizePolicy().hasHeightForWidth())
        self.search_group_box.setSizePolicy(sizePolicy)
        self.search_group_box.setMaximumSize(QtCore.QSize(16777213, 16777213))
        self.search_group_box.setStyleSheet("background: rgb(222, 222, 222); \n"
"")
        self.search_group_box.setTitle("")
        self.search_group_box.setObjectName("search_group_box")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.search_group_box)
        self.gridLayout_2.setContentsMargins(30, 40, 30, 40)
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(12)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupGoal_label = QtWidgets.QLabel(self.search_group_box)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupGoal_label.setFont(font)
        self.groupGoal_label.setStyleSheet("background: rgb(222, 222, 222); \n"
"color:rgb(0, 0, 0);\n"
"border: none;\n"
"")
        self.groupGoal_label.setObjectName("groupGoal_label")
        self.gridLayout_2.addWidget(self.groupGoal_label, 3, 0, 1, 1)
        self.group_name_output = QtWidgets.QLineEdit(self.search_group_box)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.group_name_output.setFont(font)
        self.group_name_output.setStyleSheet("border: none;\n"
"background-color: rgb(255, 255, 255);")
        self.group_name_output.setText("")
        self.group_name_output.setObjectName("group_name_output")
        self.gridLayout_2.addWidget(self.group_name_output, 2, 1, 1, 1)
        self.group_table = QtWidgets.QTableView(self.search_group_box)
        self.group_table.setModel(group)
        self.group_table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.group_table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.group_table.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Interactive)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.group_table.setFont(font)
        self.group_table.setStyleSheet("border: none;\n"
"background-color: rgb(255, 255, 255);")
        self.group_table.setObjectName("group_table")
        self.gridLayout_2.addWidget(self.group_table, 1, 0, 1, 2)
        self.groupName_label = QtWidgets.QLabel(self.search_group_box)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupName_label.setFont(font)
        self.groupName_label.setStyleSheet("background: rgb(222, 222, 222); \n"
"color:rgb(0, 0, 0);\n"
"border: none;\n"
"")
        self.groupName_label.setObjectName("groupName_label")
        self.gridLayout_2.addWidget(self.groupName_label, 2, 0, 1, 1)
        self.search_input = QtWidgets.QLineEdit(self.search_group_box)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.search_input.setFont(font)
        self.search_input.setStyleSheet("border: none;\n"
"background-color: rgb(255, 255, 255);")
        self.search_input.setText("")
        self.search_input.setObjectName("search_input")
        self.gridLayout_2.addWidget(self.search_input, 0, 0, 1, 2)
        self.join_group_button = QtWidgets.QPushButton(self.search_group_box)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.join_group_button.setFont(font)
        self.join_group_button.setObjectName("join_group_button")
        self.gridLayout_2.addWidget(self.join_group_button, 4, 0, 1, 2)
        self.group_goal_output = QtWidgets.QLineEdit(self.search_group_box)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.group_goal_output.setFont(font)
        self.group_goal_output.setStyleSheet("border: none;\n"
"background-color: rgb(255, 255, 255);")
        self.group_goal_output.setText("")
        self.group_goal_output.setObjectName("group_goal_output")
        self.gridLayout_2.addWidget(self.group_goal_output, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.search_group_box, 0, 0, 1, 1)
        self.add_group_box = QtWidgets.QGroupBox(self.group_add_join)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_group_box.sizePolicy().hasHeightForWidth())
        self.add_group_box.setSizePolicy(sizePolicy)
        self.add_group_box.setMaximumSize(QtCore.QSize(16777213, 16777213))
        self.add_group_box.setStyleSheet("background: rgb(222, 222, 222); \n"
"")
        self.add_group_box.setTitle("")
        self.add_group_box.setObjectName("add_group_box")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.add_group_box)
        self.gridLayout_3.setContentsMargins(30, 28, 30, 40)
        self.gridLayout_3.setHorizontalSpacing(20)
        self.gridLayout_3.setVerticalSpacing(24)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.group_name_label = QtWidgets.QLabel(self.add_group_box)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.group_name_label.setFont(font)
        self.group_name_label.setStyleSheet("background: rgb(222, 222, 222); \n"
"color:rgb(0, 0, 0);\n"
"border: none;\n"
"")
        self.group_name_label.setObjectName("group_name_label")
        self.gridLayout_3.addWidget(self.group_name_label, 3, 0, 1, 1)
        self.group_type_label = QtWidgets.QLabel(self.add_group_box)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.group_type_label.setFont(font)
        self.group_type_label.setStyleSheet("background: rgb(222, 222, 222); \n"
"color:rgb(0, 0, 0);\n"
"border: none;\n"
"")
        self.group_type_label.setObjectName("group_type_label")
        self.gridLayout_3.addWidget(self.group_type_label, 6, 0, 1, 1)
        self.create_group_button = QtWidgets.QPushButton(self.add_group_box)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.create_group_button.setFont(font)
        self.create_group_button.setObjectName("create_group_button")
        self.gridLayout_3.addWidget(self.create_group_button, 11, 0, 1, 2)
        self.group_goal_label = QtWidgets.QLabel(self.add_group_box)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.group_goal_label.setFont(font)
        self.group_goal_label.setStyleSheet("background: rgb(222, 222, 222); \n"
"color:rgb(0, 0, 0);\n"
"border: none;\n"
"")
        self.group_goal_label.setObjectName("group_goal_label")
        self.gridLayout_3.addWidget(self.group_goal_label, 7, 0, 1, 1)
        self.group_goal_input = QtWidgets.QLineEdit(self.add_group_box)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.group_goal_input.setFont(font)
        self.group_goal_input.setStyleSheet("border: none;\n"
"background-color: rgb(255, 255, 255);")
        self.group_goal_input.setText("")
        self.group_goal_input.setObjectName("group_goal_input")
        self.gridLayout_3.addWidget(self.group_goal_input, 7, 1, 1, 1)
        self.group_type = QtWidgets.QComboBox(self.add_group_box)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.group_type.setFont(font)
        self.group_type.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: none")
        self.group_type.setObjectName("group_type")
        self.group_type.addItem("")
        self.group_type.addItem("")
        self.gridLayout_3.addWidget(self.group_type, 6, 1, 1, 1)
        self.group_name_input = QtWidgets.QLineEdit(self.add_group_box)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.group_name_input.setFont(font)
        self.group_name_input.setStyleSheet("border: none;\n"
"background-color: rgb(255, 255, 255);")
        self.group_name_input.setText("")
        self.group_name_input.setObjectName("group_name_input")
        self.gridLayout_3.addWidget(self.group_name_input, 3, 1, 1, 1)
        self.completion_date = QtWidgets.QDateEdit(self.add_group_box)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.completion_date.setFont(font)
        self.completion_date.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: none;")
        self.completion_date.setObjectName("completion_date")
        self.completion_date.setDateTime(QtCore.QDateTime(
                QtCore.QDate(datetime.today().year, datetime.today().month, datetime.today().day),
                QtCore.QTime(0, 0, 0)))
        self.gridLayout_3.addWidget(self.completion_date, 8, 1, 1, 1)
        self.completion_date_label = QtWidgets.QLabel(self.add_group_box)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.completion_date_label.setFont(font)
        self.completion_date_label.setStyleSheet("background: rgb(222, 222, 222); \n"
"color:rgb(0, 0, 0);\n"
"border: none;\n"
"")
        self.completion_date_label.setObjectName("completion_date_label")
        self.gridLayout_3.addWidget(self.completion_date_label, 8, 0, 1, 1)
        self.create_group_title = QtWidgets.QLabel(self.add_group_box)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.create_group_title.setFont(font)
        self.create_group_title.setStyleSheet("background: rgb(222, 222, 222); \n"
"color:rgb(0, 0, 0);\n"
"border: none;\n"
"")
        self.create_group_title.setObjectName("create_group_title")
        self.gridLayout_3.addWidget(self.create_group_title, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.add_group_box, 0, 1, 1, 1)
        self.verticalLayout_6.addWidget(self.group_add_join)
        self.your_goal_label = QtWidgets.QLabel(self.group_frame)
        self.your_goal_label.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.your_goal_label.sizePolicy().hasHeightForWidth())
        self.your_goal_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.your_goal_label.setFont(font)
        self.your_goal_label.setStyleSheet("QLabel{\n"
"background:rgb(255, 255, 255); \n"
"color:rgb(59, 59, 59);\n"
"border: none;\n"
"}")
        self.your_goal_label.setWordWrap(False)
        self.your_goal_label.setIndent(45)
        self.your_goal_label.setObjectName("your_goal_label")
        self.verticalLayout_6.addWidget(self.your_goal_label)
        self.group_box = QtWidgets.QVBoxLayout()
        self.group_box.setObjectName("group_box")
        self.each_group_layout = QtWidgets.QFrame(self.group_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.each_group_layout.sizePolicy().hasHeightForWidth())
        self.each_group_layout.setSizePolicy(sizePolicy)
        self.each_group_layout.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.each_group_layout.setFrameShadow(QtWidgets.QFrame.Raised)
        self.each_group_layout.setObjectName("each_group_layout")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.each_group_layout)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.display_groups(all_groups)
        self.group_box.addWidget(self.each_group_layout)
        self.verticalLayout_6.addLayout(self.group_box)
        self.horizontalLayout_19.addWidget(self.group_frame)
        self.scrollArea.setWidget(self.group_scrollArea)
        self.horizontalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Form, all_groups)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form, groups):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("group", "Form"))
        self.group_header.setText(_translate("group", "<html><head/><body><p><span style=\" font-family:\'Segoe UI\'; font-size:36pt;\">Group</span></p></body></html>"))
        self.groupGoal_label.setText(_translate("group", "Group Goal"))
        self.groupName_label.setText(_translate("group", "Group Name"))
        self.search_input.setPlaceholderText(_translate("group", "Search for group..."))
        self.join_group_button.setText(_translate("group", "Join selected group"))
        self.group_name_label.setText(_translate("group", "Group Name"))
        self.group_type_label.setText(_translate("group", "Group Type"))
        self.create_group_button.setText(_translate("group", "Create new group"))
        self.group_goal_label.setText(_translate("group", "Group Goal"))
        self.group_goal_input.setPlaceholderText(_translate("group", "goal"))
        self.group_type.setItemText(0, _translate("group", "Open"))
        self.group_type.setItemText(1, _translate("group", "Restricted"))
        self.group_name_input.setPlaceholderText(_translate("group", "name"))
        self.completion_date_label.setText(_translate("group", "Completion Date"))
        self.create_group_title.setText(_translate("group", "Create your own group"))
        self.your_goal_label.setText(_translate("group", "Your Groups"))
        for i in range(len(groups)):
            if hasattr(self, f'group{i}_vertical_layout'):
                getattr(self, f'group{i}_completionDate').setText(_translate("group", f"Completion date: {groups[i].date}"))
                getattr(self, f'leave_group{i}_button').setText(_translate("group", "Leave Group"))
                getattr(self, f'group{i}_name').setText(_translate("group", f"{groups[i].groupName}"))
                getattr(self, f'group{i}_goal').setText(_translate("group", f"{groups[i].goal_description}"))

    def display_groups(self, groups):
        from datetime import datetime
        if len(groups) == 0:
            print('No goals set yet')
            no_group_text = QtWidgets.QLabel(self.each_group_layout)
            no_group_text.setFixedWidth(1000)
            font = QtGui.QFont()
            font.setPointSize(20)
            no_group_text.setFont(font)
            no_group_text.setStyleSheet("background: none; color: grey;")
            no_group_text.setWordWrap(False)
            no_group_text.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            no_group_text.setObjectName("no_group_text")
            no_group_text.setText('No groups yet')
            self.verticalLayout_7.addWidget(no_group_text)
            return

        for i, group in enumerate(groups):
            # add a vertical Layout to the page
            setattr(self, f'group{i}_vertical_layout', QtWidgets.QVBoxLayout())
            mygroup_layout = getattr(self, f'group{i}_vertical_layout')
            mygroup_layout.setObjectName(f"group{i}_vertical_layout")

            setattr(self, f'group{i}', QtWidgets.QGroupBox(self.each_group_layout))
            mygroup = getattr(self, f'group{i}')
            mygroup.setEnabled(True)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                               QtWidgets.QSizePolicy.MinimumExpanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(mygroup.sizePolicy().hasHeightForWidth())
            mygroup.setSizePolicy(sizePolicy)
            mygroup.setMinimumSize(QtCore.QSize(257, 0))
            mygroup.setStyleSheet("QGroupBox{\n"
                                  "background:rgb(217, 217, 217); \n"
                                  "color:rgb(62, 62, 62);\n"
                                  "}")
            mygroup.setTitle("")
            mygroup.setObjectName(f"group{i}")
            self.gridLayout_8 = QtWidgets.QGridLayout(mygroup)
            self.gridLayout_8.setObjectName("gridLayout_8")

            setattr(self, f'group{i}_goal', QtWidgets.QLabel(mygroup))
            mygroup_goal = getattr(self, f'group{i}_goal')
            font = QtGui.QFont()
            font.setPointSize(16)
            mygroup_goal.setFont(font)
            mygroup_goal.setStyleSheet("QLabel{\n"
                                       "background:rgb(217, 217, 217); \n"
                                       "color:rgb(62, 62, 62);\n"
                                       "}")
            mygroup_goal.setWordWrap(False)
            mygroup_goal.setObjectName(f"group{i}_goal")
            self.gridLayout_8.addWidget(mygroup_goal, 1, 0, 1, 1)

            setattr(self, f'leave_group{i}_button', QtWidgets.QPushButton(mygroup))
            mygroup_leave_button = getattr(self, f'leave_group{i}_button')
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(mygroup_leave_button.sizePolicy().hasHeightForWidth())
            mygroup_leave_button.setSizePolicy(sizePolicy)
            mygroup_leave_button.setStyleSheet("padding: 10 15 10 15;")
            icon = QtGui.QIcon.fromTheme("sidebar_icon")
            mygroup_leave_button.setIcon(icon)
            mygroup_leave_button.setObjectName(f"leave_group{i}_button")
            self.gridLayout_8.addWidget(mygroup_leave_button, 0, 1, 1, 1)

            setattr(self, f'group{i}_progressBar', QtWidgets.QProgressBar(mygroup))
            mygroup_goal_progress = getattr(self, f'group{i}_progressBar')
            mygroup_goal_progress.setStyleSheet("QProgressBar::chunk {\n"
                                              "     background-color: #3add36;\n"
                                              "     width: 1px;\n"
                                              " }\n"
                                              "\n"
                                              " QProgressBar {\n"
                                              "     \n"
                                              "     border-radius: 0px;\n"
                                              "     text-align: center;\n"
                                              " }")
            mygroup_goal_progress.setProperty("value", 10)
            mygroup_goal_progress.setInvertedAppearance(False)
            mygroup_goal_progress.setObjectName(f"group{i}_progressBar")
            self.gridLayout_8.addWidget(mygroup_goal_progress, 2, 0, 1, 2)

            setattr(self, f'group{i}_completionDate', QtWidgets.QLabel(mygroup))
            mygroup_goal_completionDate = getattr(self, f'group{i}_completionDate')
            font = QtGui.QFont()
            font.setPointSize(16)
            mygroup_goal_completionDate.setFont(font)
            mygroup_goal_completionDate.setStyleSheet("background: none;")
            mygroup_goal_completionDate.setWordWrap(False)
            mygroup_goal_completionDate.setObjectName(f"group{i}_completionDate")
            self.gridLayout_8.addWidget(mygroup_goal_completionDate, 1, 1, 1, 1)

            setattr(self, f'group{i}_name', QtWidgets.QLabel(mygroup))
            mygroup_name = getattr(self, f'group{i}_name')
            font = QtGui.QFont()
            font.setPointSize(20)
            mygroup_name.setFont(font)
            mygroup_name.setStyleSheet("QLabel{\n"
                                       "background:rgb(217, 217, 217); \n"
                                       "color:rgb(62, 62, 62);\n"
                                       "}")
            mygroup_name.setWordWrap(False)
            mygroup_name.setObjectName(f"group{i}_name")
            self.gridLayout_8.addWidget(mygroup_name, 0, 0, 1, 1)
            mygroup_layout.addWidget(mygroup)
            self.verticalLayout_7.addLayout(mygroup_layout)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_group()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

