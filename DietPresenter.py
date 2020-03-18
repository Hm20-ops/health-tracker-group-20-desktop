import sys
from functools import partial
from PyQt5 import QtCore, QtWidgets
from ModelHandler import make_session
from FoodDictionary import FoodDictionary
from dietView import Ui_diet
from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex
from PyQt5.QtGui import QColor
from helper import *

class CustomTableModel(QAbstractTableModel):#custom table for loading model
    def __init__(self, data=None):
        QAbstractTableModel.__init__(self)#inherit from QAbstractModel
        self.load_data(data)

    def load_data(self, data):
        self.column_count = 2#specify number of columns to display food name and baseCalorie value
        self.row_count = len(data)
        self.myModel=data
    def rowCount(self,parent=QModelIndex()):
        return self.row_count

    def columnCount(self,parent=QModelIndex()):
        return self.column_count

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return ("Food Name", "Calories")[section]
        else:
            return "{}".format(section)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:#Qt.DisplayRole defines behaviour of an element in the table
            return self.myModel[index.row()][index.column()]#index of table is row number in table

        elif role == Qt.BackgroundRole:
            return QColor(Qt.white)
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignRight

        return None


class SortFilterProxyModel(QtCore.QSortFilterProxyModel):
    def filterAcceptsRow(self, sourceRow, sourceParent):
        # gets handled for us
        return super(SortFilterProxyModel, self).filterAcceptsRow(sourceRow, sourceParent)


class DietPresenter:
    def __init__(self, parent, username):
        self.data = self.read_data()
        self._user = username


        self.proxyModel = SortFilterProxyModel()#make a proxy model object
        self.model = CustomTableModel(self.data)
        self.proxyModel.setSourceModel(self.model)

        self.ui = Ui_diet(parent, self.proxyModel)

        self.checkExerciseSearch()#method for searching the database
        self.ui.food_database.clicked.connect(partial(self.displayInQlineEdit))#method for displaying text when row is clicked
        self.ui.portion_input.textEdited.connect(partial(self.getCaloricInformation))#method for editing calorific value when portion changes
        self.ui.add_food.clicked.connect(partial(self.addNewFood))#method to add new food to database

    def read_data(self):
        data=make_session().query(FoodDictionary).all()#query FoodDictionary to fetch all rows
        tableData=[]
        '''
        Storing result of queries in suitable format to be displayed by table
        '''
        for x in range(0,len(data)):
            dictionary=data[x]
            tableData.append((dictionary.foodName,dictionary.calories))
        return tableData

    def displayInQlineEdit(self):
         index = self.ui.food_database.currentIndex()#fetched index of row currently selected in the table
         foodName = self.ui.food_database.model().index(index.row(), 0)
         baseCalories = self.ui.food_database.model().index(index.row(), 1)
         self.ui.lineEdit_2.setText(foodName.data())#display selected food name
         self.ui.portion_input.setText("100")
         self.ui.calories_output.setText(str(baseCalories.data()))#display calorie

    def checkExerciseSearch(self):
        self.ui.search_food_2.textEdited.connect(partial(self.filterRegExpChanged))#signal to filter table based on search query


    def filterRegExpChanged(self):
        syntax = QtCore.QRegExp.PatternSyntax(QtCore.QRegExp.FixedString)

        regExp = QtCore.QRegExp(self.ui.search_food_2.text(),
                                    QtCore.Qt.CaseInsensitive, syntax)
        self.proxyModel.setFilterRegExp(regExp)

    def getCaloricInformation(self):
        index = self.ui.food_database.currentIndex()
        session=make_session()
        baseCalorie=(session.query(FoodDictionary).get(index.row()+1).calories)#for an index in table, query correspoding baseCalorie
        session.close()
        try:
            # TODO fetch username passed as argument
            # Show a label if an input is not allowed
            '''
            calorieIntake=(portion in gram input/100g)*baseCalorie
            display calorieIntake
            '''
            self.ui.calories_output.setText(str(round((float(self.ui.portion_input.text())/100)*float(baseCalorie),3)))
        except Exception as e:
            #if input is empty. Display 0
            self.ui.calories_output.setText(str(0))
            print(e)#display exception on console for debugging

    def addNewFood(self):
        if(self.ui.name_input.text()=='' or self.ui.calories_input.text()==''):#disallow adding food with empty text
            print('not allowed')
            display_message('Input cannot be empty', 'Please enter valid food name and calories')
        else:
            foodName=self.ui.name_input.text()
            calories=self.ui.calories_input.text()
            try:
                FoodDictionary.addFood(foodName,calories)
                self.data = self.read_data()
                self.model = CustomTableModel(self.data)#reset model
                self.proxyModel.setSourceModel(self.model)#display added food without a need for refreshing
                self.ui.food_database.setModel(self.proxyModel)
            except Exception as e:
                print(e)

    def page(self):
        return self.ui.scrollArea
