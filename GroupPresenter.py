import sys
from functools import partial
from qtpy import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex
from PyQt5.QtGui import QColor

from CustomGoal import CustomGoal
from UserGroup import UserGroup
from groupView import Ui_group
from Group import *
from helper import display_message


class CustomTableModel(QAbstractTableModel):  # custom table for loading model
    def __init__(self, data=None):
        QAbstractTableModel.__init__(self)  # inherit from QAbstractModel
        self.load_data(data)

    def load_data(self, data):
        self.column_count = 2  # specify number of columns to display food name and baseCalorie value
        self.row_count = len(data)
        self.myModel = data

    def rowCount(self, parent=QModelIndex()):
        return self.row_count

    def columnCount(self, parent=QModelIndex()):
        return self.column_count

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return ("Group Name", "Group Goal")[section]
        else:
            return "{}".format(section)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:  # Qt.DisplayRole defines behaviour of an element in the table
            return self.myModel[index.row()][index.column()]  # index of table is row number in table

        elif role == Qt.BackgroundRole:
            return QColor(Qt.white)
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignRight

        return None


class SortFilterProxyModel(QtCore.QSortFilterProxyModel):
    def filterAcceptsRow(self, sourceRow, sourceParent):
        # gets handled for us
        return super(SortFilterProxyModel, self).filterAcceptsRow(sourceRow, sourceParent)


class GroupPresenter:
    def __init__(self, parent, username):
        self._user = username
        self._group_model = Group()
        self._user_group_model = UserGroup()
        self._custom_goal = CustomGoal()

        self.data = self.read_data()
        self.proxyModel = SortFilterProxyModel()  # make a proxy model object
        self.model = CustomTableModel(self.data)
        self.proxyModel.setSourceModel(self.model)

        self.ui = Ui_group(parent, self.proxyModel, self.data)
        #self.ui.group_table.setModel(self.proxyModel)  # At initialisation, the proxyModel is the model itself
        self.checkGroupSearch()  # method for searching the database
        self.ui.group_table.clicked.connect(partial(self.displayInQlineEdit))  # method for displaying text when row is clicked

        #self.ui.group_name_output.textEdited.connect(partial(self.addNewGroup))  # method for editing calorific value when portion changes
        self.ui.create_group_button.clicked.connect(partial(self.addNewGroup))  # method to add new food to database
        self.ui.join_group_button.clicked.connect(partial(self.joinNewGroup))  # method to add new food to database

        # self.ui.setupUi(self.group)  # pass the diet widget to the ui

    def read_data(self):
        session = make_session()
        # query FoodDictionary to fetch all rows   .with_entities(Group.groupName, CustomGoal.goal_description)
        data = session.query(Group).join(CustomGoal) \
            .with_entities(Group.groupName, CustomGoal.goal_description, CustomGoal.date).all()
        session.close()
        return data

    def displayInQlineEdit(self):
        index = self.ui.group_table.currentIndex()  # fetched index of row currently selected in the table
        groupName = self.ui.group_table.model().index(index.row(), 0)
        groupGoal = self.ui.group_table.model().index(index.row(), 1)
        self.ui.group_name_output.setText(groupName.data())  # display selected food name
        self.ui.group_goal_output.setText(groupGoal.data())  # display selected food name

    def checkGroupSearch(self):
        self.ui.search_input.textEdited.connect(
            partial(self.filterRegExpChanged))  # signal to filter table based on search query

    def filterRegExpChanged(self):
        syntax = QtCore.QRegExp.PatternSyntax(QtCore.QRegExp.FixedString)

        regExp = QtCore.QRegExp(self.ui.search_input.text(),
                                QtCore.Qt.CaseInsensitive, syntax)
        self.proxyModel.setFilterRegExp(regExp)


    def addNewGroup(self):
        if (self.ui.group_name_input.text() == '' or self.ui.group_goal_input.text() == ''):  # disallow adding food with empty text
            print('not allowed')
            display_message('Input cannot be empty', 'Please enter valid group name and description')
        else:
            groupName = self.ui.group_name_input.text()
            groupType = self.ui.group_type.currentText().upper()
            groupGoal = self.ui.group_goal_input.text()
            completionDate = self.ui.completion_date.date().toPyDate()
            try:
                groupID = Group.createGroup(groupName, groupType, completionDate)
                self._user_group_model.createUserGroup(self._user, groupID)
                self._custom_goal.create_custom_goal(self._user, groupGoal, date.today(), group_id=groupID)

                self.data = self.read_data()
                self.model = CustomTableModel(self.data)  # reset model
                self.proxyModel.setSourceModel(self.model)  # display added food without a need for refreshing
                self.ui.group_table.setModel(self.proxyModel)
                display_message('New group added', 'You have added a new group successfully', False)
            except Exception as e:
                display_message('Invalid input',
                                'Please enter a valid group name or description!')
                print(e)

    # function to put user into a group
    def joinNewGroup(self):
        groupName = self.ui.group_name_output.text()
        groupGoal = self.ui.group_goal_output.text()
        try:
            self._user_group_model.addUserGroup(self._user, self._group_model.get_id_by_name(groupName))
            self.data = self.read_data()
            self.model = CustomTableModel(self.data)  # reset model
            self.proxyModel.setSourceModel(self.model)  # display added food without a need for refreshing
            self.ui.group_table.setModel(self.proxyModel)
            display_message('Joined group', 'You have joined a new group successfully', False)
        except Exception as e:
            display_message('Fail to join group',
                            'Error joining the group, please check your input and try again!')
            print(e)

    def page(self):
        return self.ui.scrollArea

# # constructor
# # parent: widget that holds the view i.e. the stackWidget in main
# def __init__(self, parent, username):
# 	self._redirect_to = None
# 	self._user = username
# 	# get all models required
# 	self._user_group_model = UserGroup()
# 	# get data from model, functions that do basic conventional stuff(CRUD)
# 	# can be written in model and call here, u can directly query here for more complex actions
# 	user_groups = self._user_group_model.get(username)
#
# 	# initialize the view and pass the above above data to the view
# 	self._view = Ui_group2(parent, user_groups)
# 	self._view.create_group_button.clicked.connect(lambda: self.create_group())
# 	#self._view.join_group_button.clicked.connect(lambda: self.join_group())
#
# def create_group(self):
# 	# get data from the view
# 	# groupName = self._view.group_name_input.value()
# 	# groupType = self._view.group_type.value()
# 	# groupGoal = self._view.group_goal_input.value()
# 	# complete_date = self._view.completion_date.date()
# 	# pass them to model to create basic goal
# 	self._user_group_model.createUserGroup()
# 	# implement this method in basic goal model
#
# def join_group(self):
#     self._user_group_model.addUserGroup()
#
# def page(self):
# 	return self._view.scrollArea

