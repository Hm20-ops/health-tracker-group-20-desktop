import sys
from functools import partial
import User
from BasicGoal import BasicGoal
from CustomGoal import CustomGoal
from Group import Group
from Diet import *
from home_page import Ui_Health_tracker
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox


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
        self._view.show()

    def init_goal(self):
        # session = self._basic_goal_model.make_session()
        # basic_goals = session.query(BasicGoal).filter(BasicGoal.username=self._user)
        basic_goals = {{'username': self._user, 'target_weight': 50, 'date': date.today(), 'isMet': False}}
        self._view.display_all_goal(basic_goals)


class MainWindow(QMainWindow, Ui_Health_tracker):
    def __init__(self, goal_list, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self, goal_list)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    x = MainPresenter('user')

    app.exec()
