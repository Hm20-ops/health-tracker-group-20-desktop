import sys
from decimal import Decimal

from PyQt5.QtWidgets import QApplication
from qtpy import QtCore, QtWidgets
from ModelHandler import make_session
from ExerciseDictionary import ExerciseDictionary
from User import User
from exerciseView import Ui_exercise_page
from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex
from PyQt5.QtGui import QColor


class CustomTableModel(QAbstractTableModel):
    def __init__(self, data=None):
        QAbstractTableModel.__init__(self)
        self.load_data(data)

    def load_data(self, data):
        self.column_count = 2
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
        if role == Qt.DisplayRole:
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


class Controller:
    def __init__(self):
        self.data = self.read_data()
        self._app = QApplication(sys.argv)#might break here to check


        self.exercise = QtWidgets.QWidget()
        self.ui = Ui_exercise_page()
        self.ui.setupUi(self.exercise)


        self.proxyModel = SortFilterProxyModel()
        self.model = CustomTableModel(self.data)
        self.proxyModel.setSourceModel(self.model)


        self.ui.exercise_table.setModel(self.proxyModel)
        self.checkExerciseSearch()
        self.ui.exercise_table.clicked.connect(self.displayInQlineEdit)
        self.ui.duration_input.textEdited.connect(self.getCaloricInformation)
        self.ui.add_exercise_3.clicked.connect(self.addNewExercise)

    def read_data(self):
        # Read the CSV content
        data=make_session().query(ExerciseDictionary).all()
        tableData=[]
        for x in range(0,len(data)):
            dictionary=data[x]
            tableData.append((dictionary.specificMotion,dictionary.metValue))
        return tableData

    def displayInQlineEdit(self):
         index = self.ui.exercise_table.currentIndex()
         exerciseName = self.ui.exercise_table.model().index(index.row(), 0)
         metValue = self.ui.exercise_table.model().index(index.row(), 1)
         self.ui.exerciseName_2.setText(exerciseName.data())
         self.ui.duration_input.setText("60")
         self.ui.add_calories_2.setText(str(metValue.data()))

    def checkExerciseSearch(self):
        self.ui.search_input.textEdited.connect(self.filterRegExpChanged)


    def filterRegExpChanged(self):
        syntax = QtCore.QRegExp.PatternSyntax(QtCore.QRegExp.FixedString)

        regExp = QtCore.QRegExp(self.ui.search_input.text(),
                                    QtCore.Qt.CaseInsensitive, syntax)
        self.proxyModel.setFilterRegExp(regExp)

    def getCaloricInformation(self):
        index = self.ui.exercise_table.currentIndex()
        session=make_session()
        metValue=(session.query(ExerciseDictionary).get(index.row()+1).metValue)
        try:
            userInfo=session.query(User).filter(User.username=='Munbodh21')
            userWeight=userInfo[0].weight
            duration=float(self.ui.duration_input.text())
            caloriesBurnt=(duration/60)*metValue*userWeight
            precision=Decimal('0.01')
            caloriesBurnt=Decimal(caloriesBurnt).quantize(precision)
            print(caloriesBurnt)
            self.ui.add_calories_2.setText(str(caloriesBurnt))
        except Exception as e:
            self.ui.add_calories_2.setText(str(0))
            print(e)

        #self.__ui.lineEdit_3.setText(str(50))
        #self.__ui.lineEdit_3.setText(str(round((float(self.__ui.lineEdit_3.text())/100)*float(self.__ui.lineEdit_2.text()),3)))

    def addNewExercise(self):
        if(self.ui.durationLineEdit_5.text()=='' or self.ui.add_calories.text()==''):
            print('not allowed')
        else:
            exerciseName=self.ui.durationLineEdit_5.text()
            calories=self.ui.add_calories.text()
            try:
                activity=None
                ExerciseDictionary.addExercise(activity,exerciseName,calories)
                self.data = self.read_data()
                self.model = CustomTableModel(self.data)
                self.proxyModel.setSourceModel(self.model)
                self.ui.exercise_table.setModel(self.proxyModel)
            except Exception as e:
                print('hello')
                print(e)

    def run(self):
        self.exercise.show()
        return self._app.exec_()

if __name__ == "__main__":
    c=Controller()
    sys.exit(c.run())
