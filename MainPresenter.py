import sys
from functools import partial

from PyQt5.QtCore import pyqtSlot

import User
from BasicGoal import BasicGoal
from CustomGoal import *
from Group import Group
from Diet import *
import RegisterPresenter
from home_page import Ui_Health_tracker
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

nav_bar_map = ['HOME', 'PROFILE', 'GOAL', 'EXERCISE', 'DIET', 'GROUP', 'LOGOUT']

class MainPresenter:
    def __init__(self, username):
        self._redirect_to = None
        self._user_model = User.User()
        self._user = username
        self._group_model = Group()
        #self._basic_goal_model = BasicGoal()
        #self._custom_goal_model = CustomGoal()
        _basic_goals = [{'username': self._user, 'target_weight': 50, 'date': date.today(), 'isMet': True},
                        {'username': self._user, 'target_weight': 30, 'date': '01/04/2020', 'isMet': False},
                        {'username': self._user, 'target_weight': 50, 'date': date.today(), 'isMet': True},
                        {'username': self._user, 'target_weight': 30, 'date': '01/04/2020', 'isMet': False}
                        ]
        #self.init_goal()
        self._view = MainWindow(_basic_goals)
        # self._view.create_account.clicked.connect(partial(self._view.stackedWidget.setCurrentIndex, 1))
        # self._view.cancel.clicked.connect(partial(self._view.stackedWidget.setCurrentIndex, 0))
        self._view.side_nav_bar.itemClicked.connect(lambda :self.navigate())

        self._view.show()

    @pyqtSlot(int)
    def navigate(self):
        row = nav_bar_map[self._view.side_nav_bar.currentIndex().row()]
        return {'HOME': self.stub,
                'PROFILE': self.stub,
                'GOAL': self.stub,
                'EXERCISE': self.stub,
                'DIET': self.stub,
                'GROUP': self.stub,
                'LOGOUT': self.logout
                }[row]()


    def logout(self):
        self._redirect_to = RegisterPresenter.RegisterPresenter()
        self._view.close()
        return self._redirect_to

    def init_goal(self):
        # session = self._basic_goal_model.make_session()
        # basic_goals = session.query(BasicGoal).filter(BasicGoal.username=self._user, BasicGoal.isMet is False)
        basic_goals = {{'username': self._user, 'target_weight': 50, 'date': date.today(), 'isMet': False}}
        self._view.display_all_goal(basic_goals)

    def stub(self):
        pass

class MainWindow(QMainWindow, Ui_Health_tracker):
    def __init__(self, goal_list, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self, goal_list)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    x = MainPresenter('user')

    app.exec()
