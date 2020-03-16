import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from qtpy import QtCore, QtWidgets
from ModelHandler import make_session
from FoodDictionary import FoodDictionary
from dietView import Ui_diet
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
            return ("Food Name", "Calories")[section]
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


        self.diet = QtWidgets.QWidget()
        self.ui = Ui_diet()
        self.ui.setupUi(self.diet)


        self.proxyModel = SortFilterProxyModel()
        self.model = CustomTableModel(self.data)
        self.proxyModel.setSourceModel(self.model)


        self.ui.food_database.setModel(self.proxyModel)
        self.checkExerciseSearch()
        self.ui.food_database.clicked.connect(self.displayInQlineEdit)
        self.ui.portion_input.textEdited.connect(self.getCaloricInformation)
        self.ui.add_food.clicked.connect(self.addNewFood)

    def read_data(self):
        # Read the CSV content
        data=make_session().query(FoodDictionary).all()
        tableData=[]
        for x in range(0,len(data)):
            dictionary=data[x]
            tableData.append((dictionary.foodName,dictionary.calories))
        return tableData

    def displayInQlineEdit(self):
         index = self.ui.food_database.currentIndex()
         foodName = self.ui.food_database.model().index(index.row(), 0)
         baseCalories = self.ui.food_database.model().index(index.row(), 1)
         self.ui.lineEdit_2.setText(foodName.data())
         self.ui.portion_input.setText("100")
         self.ui.calories_output.setText(str(baseCalories.data()))

    def checkExerciseSearch(self):
        self.ui.search_food_2.textEdited.connect(self.filterRegExpChanged)


    def filterRegExpChanged(self):
        syntax = QtCore.QRegExp.PatternSyntax(QtCore.QRegExp.FixedString)

        regExp = QtCore.QRegExp(self.ui.search_food_2.text(),
                                    QtCore.Qt.CaseInsensitive, syntax)
        self.proxyModel.setFilterRegExp(regExp)

    def getCaloricInformation(self):
        index = self.ui.food_database.currentIndex()
        session=make_session()
        baseCalorie=(session.query(FoodDictionary).get(index.row()+1).calories)
        try:
            self.ui.calories_output.setText(str(round((float(self.ui.portion_input.text())/100)*float(baseCalorie),3)))
        except Exception as e:
            self.ui.calories_output.setText(str(0))
            print(e)

        #self.__ui.lineEdit_3.setText(str(50))
        #self.__ui.lineEdit_3.setText(str(round((float(self.__ui.lineEdit_3.text())/100)*float(self.__ui.lineEdit_2.text()),3)))

    def addNewFood(self):
        if(self.ui.name_input.text()=='' or self.ui.calories_input.text()==''):
            print('not allowed')
        else:
            foodName=self.ui.name_input.text()
            calories=self.ui.calories_input.text()
            try:
                FoodDictionary.addFood(foodName,calories)
                self.data = self.read_data()
                self.model = CustomTableModel(self.data)
                self.proxyModel.setSourceModel(self.model)
                self.ui.food_database.setModel(self.proxyModel)


            except Exception as e:
                print('hello')
                print(e)

    def run(self):
        self.diet.show()
        return self._app.exec_()

if __name__ == "__main__":
    c=Controller()
    sys.exit(c.run())
