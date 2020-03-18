import sys
from decimal import Decimal
from functools import partial

from PyQt5.QtWidgets import QApplication
from qtpy import QtCore, QtWidgets
from ModelHandler import make_session
from ExerciseDictionary import ExerciseDictionary
from User import User
from ExerciseView import Ui_exercise_page
from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex
from PyQt5.QtGui import QColor

from helper import display_message


class CustomTableModel(QAbstractTableModel):#custom table for loading model
    def __init__(self, data=None):
        QAbstractTableModel.__init__(self)#inherit from QAbstractModel
        self.load_data(data)

    def load_data(self, data):
        self.column_count = 2#specify number of columns to display exercise name and MET value
        self.row_count = len(data)
        self.myModel=data
    def rowCount(self, parent=QModelIndex()):
        return self.row_count

    def columnCount(self, parent=QModelIndex()):
        return self.column_count

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return ("Exercise Name", "MET value")[section]
        else:
            return "{}".format(section)

    def data(self, index, role=Qt.DisplayRole):
        #print(self.myModel[index.row()][index.column()])#not getting here
        if role == Qt.DisplayRole:#Qt.DisplayRole defines behaviour of an element in the table
            return self.myModel[index.row()][index.column()]

        elif role == Qt.BackgroundRole:
            return QColor(Qt.white)
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignRight

        return None


class SortFilterProxyModel(QtCore.QSortFilterProxyModel):
    def filterAcceptsRow(self, sourceRow, sourceParent):
        # gets handled for us
        return super(SortFilterProxyModel, self).filterAcceptsRow(sourceRow, sourceParent)


class ExercisePresenter:
    def __init__(self, parent, username):
        self._user = username
        self._exercise_model = ExerciseDictionary()
        self._user_model = User()

        self.data = self._exercise_model.get_all_exercises()
        self.proxyModel = SortFilterProxyModel()#make a proxy model object
        self.model = CustomTableModel(self.data)
        self.proxyModel.setSourceModel(self.model)

        self.ui = Ui_exercise_page(parent, self.proxyModel)
        self.ui.exercise_table.setModel(self.proxyModel)#At initialisation, the proxyModel is the model itself
        self.checkExerciseSearch()#method for searching the database
        self.ui.exercise_table.clicked.connect(partial(self.displayInQlineEdit))#method for displaying text when row is clicked
        self.ui.duration_input.textEdited.connect(partial(self.getCaloricInformation))#method for editing calorific value when duration changes
        self.ui.add_exercise_3.clicked.connect(partial(self.addNewExercise))#add new exercise to the database

    # def read_data(self):
    #     data=make_session().query(ExerciseDictionary).all()#query ExerciseDictionary to fetch all rows
    #     tableData=[]
    #     for x in range(0,len(data)):
    #         dictionary=data[x]
    #         tableData.append((dictionary.specificMotion,dictionary.metValue))
    #     return tableData

    def displayInQlineEdit(self):
         index = self.ui.exercise_table.currentIndex()#fetched index of row currently selected in the table
         exerciseName = self.ui.exercise_table.model().index(index.row(), 0)
         metValue = self.ui.exercise_table.model().index(index.row(), 1)
         self.ui.exerciseName_2.setText(exerciseName.data())#display selected exercise name
         self.ui.duration_input.setText("60")
         self.ui.add_calories_2.setText(str(metValue.data()))#display calorie

    def checkExerciseSearch(self):
        self.ui.search_input.textEdited.connect(partial(self.filterRegExpChanged))#signal to filter table based on search query


    def filterRegExpChanged(self):
        syntax = QtCore.QRegExp.PatternSyntax(QtCore.QRegExp.FixedString)

        regExp = QtCore.QRegExp(self.ui.search_input.text(),
                                    QtCore.Qt.CaseInsensitive, syntax)
        self.proxyModel.setFilterRegExp(regExp)

    def getCaloricInformation(self):
        index = self.ui.exercise_table.currentIndex().row() + 1
        # session=make_session()
        # metValue=(session.query(ExerciseDictionary).get(index).metValue)#for an index in table, query correspoding MET
        metValue = self._exercise_model.get(index).metValue
        caloriesBurnt = 0
        try:
            #TODO fetch username passed as argument
            # Show a label if an input is not allowed
            # userInfo=session.query(User).filter(User.username=='Munbodh21')
            # userWeight=userInfo[0].weight
            userInfo = self._user_model.get_user(self._user)
            userWeight = userInfo.weight

            duration=float(self.ui.duration_input.text())
            caloriesBurnt=(duration/60)*metValue*userWeight
            precision=Decimal('0.01')#rounding of caloriesBurnt to 2 d.p
            caloriesBurnt=Decimal(caloriesBurnt).quantize(precision)
            #self.ui.add_calories_2.setText(str(caloriesBurnt))
        except Exception as e:
            #self.ui.add_calories_2.setText(str(0))
            print(e)
        finally:
            self.ui.add_calories_2.setText(f'{caloriesBurnt}')

    def addNewExercise(self):
        if(self.ui.durationLineEdit_5.text()=='' or self.ui.add_calories.text()==''):#disallow adding food with empty text
            #TODO to be printed in the GUI as a label
            # Find a more efficient way to refresh page after model is updated
            print('not allowed')
            display_message('Input cannot be empty', 'Please enter valid exercise duration and calories')
        else:
            exerciseName=self.ui.durationLineEdit_5.text()
            calories=self.ui.add_calories.text()
            try:
                activity=None
                ExerciseDictionary.addExercise(activity,exerciseName,calories)
                self.data = self._exercise_model.get_all_exercises()
                self.model = CustomTableModel(self.data)#reset model
                self.proxyModel.setSourceModel(self.model)#display added food without a need for refreshing
                self.ui.exercise_table.setModel(self.proxyModel)
                display_message('New exercise added', 'You have added a new exercise successfully', False)
            except Exception as e:
                display_message('Invalid duration/calories input',
                                'Please enter valid exercise duration and calories burnt!')
                print(e)

    def page(self):
        return self.ui.scrollArea


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    c = ExercisePresenter(QtWidgets.QWidget(), '')
    sys.exit(app.exec_())
