import sys
from datetime import datetime, timedelta, date

import RegisterPresenter
from CustomGoal import CustomGoal
from mainView import Ui_Health_tracker
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QListWidgetItem, QMessageBox
from homePresenter import homePresenter
from profilePresenter import profilePresenter
from goalPresenter import goalPresenter
from DietPresenter import DietPresenter
from ExercisePresenter import ExercisePresenter
from GroupPresenter import GroupPresenter

nav_bar_map = ['HOME', 'PROFILE', 'GOAL', 'EXERCISE', 'DIET', 'GROUP', 'LOGOUT']

'''
This presenter is master presenter with the side bar 
that governs the display of pages and switching controllers
'''
class MainPresenter:
    def __init__(self, username):
        self._redirect_to = None
        self._user = username
        self.goal_model = CustomGoal()

        self._view = MainWindow()
        self._view.side_nav_bar.itemClicked.connect(lambda :self.navigate())
        self.view_page = self._view.display_page

        self._view.side_nav_bar.setCurrentItem(QListWidgetItem(" Home"))
        self.view_page.addWidget(self.home())
        self._view.show()
        self.goal_check()


    @pyqtSlot()
    def navigate(self):
        row = nav_bar_map[self._view.side_nav_bar.currentIndex().row()]
        self._redirect_to = {'HOME': self.home,
                             'PROFILE': self.profile,
                             'GOAL': self.goal,
                             'EXERCISE': self.exercise,
                             'DIET': self.diet,
                             'GROUP': self.group,
                             'LOGOUT': self.logout
                             }[row]()
        if row != 'LOGOUT':
            self.view_page.addWidget(self._redirect_to)
            self.view_page.setCurrentWidget(self._redirect_to)

    def home(self):
        return homePresenter(self.view_page, self._user).page()

    def profile(self):
        return profilePresenter(self.view_page, self._user).page()

    def goal(self):
        return goalPresenter(self.view_page, self._user).page()

    def exercise(self):
        return ExercisePresenter(self.view_page, self._user).page()

    def diet(self):
        return DietPresenter(self.view_page, self._user).page()

    def group(self):
        return GroupPresenter(self.view_page, self._user).page()

    def logout(self):
        self._view.close()
        return RegisterPresenter.RegisterPresenter()
    @property
    def current_user(self):
        return self._user

    def goal_check(self):
        goals = self.goal_model.get(self._user)
        for goal in goals:
            if goal.date == date.today():
                answer = QMessageBox() \
                        .question(self._view,
                                  'Goal checking',
                                  f'Have you met your goal: \n{goal.goal_description}?',
                                  QMessageBox.Yes | QMessageBox.No
                                  )
                if answer == QMessageBox.Yes:
                    self.goal_model.goal_archived(goal.id)

                description = 'do 20 times push up everyday'
                new_date = goal.date + timedelta(days=7)
                add = QMessageBox() \
                      .question(self._view,
                                'New goal suggestion',
                                f'Would you like to add a new goal on top tof this goal?\n'
                                f'goal: {description} \n date: {new_date}',
                                QMessageBox.Yes | QMessageBox.No
                                )
                if add == QMessageBox.Yes:
                    self.goal_model.create_custom_goal(self._user, description, new_date)

class MainWindow(QMainWindow, Ui_Health_tracker):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

# testing
if __name__ == '__main__':
    app = QApplication(sys.argv)

    x = MainPresenter('Munbodh21')

    app.exec()
