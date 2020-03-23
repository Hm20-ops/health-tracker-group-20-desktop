import sys
from functools import partial

from PyQt5.QtCore import pyqtSlot
import User
from CustomGoal import *
from BasicGoal import *
from goalView import Ui_Goal
from helper import display_message


class goalPresenter:
    # constructor
    # parent: widget that holds the view i.e. the stackWidget in main
    def __init__(self, parent, username):
        self._user = username
        # get all models required
        self._basic_goal_model = BasicGoal()
        self._user_custom_goal_model = CustomGoal()

        # get data from model
        user_goals = self._user_custom_goal_model.get(username)
        basic_goal = self._basic_goal_model.get(username)
        # initialize the view and pass the above above data to the view
        self._view = Ui_Goal(parent, basic_goal, user_goals)

        # connect all signals to the functions in this presenter
        self._view.add_basic_goal.clicked.connect(lambda: self.make_basic_goal())
        self._view.add_custom_goal.clicked.connect(lambda: self.make_custom_goal())

    def make_basic_goal(self):
        # get data from the view
        weight_goal = self._view.lose_weight_goal.value()
        complete_date = self._view.basic_goal_completion_date.date().toPyDate()
        # pass them to model to create basic goal
        try:
            self._basic_goal_model.create_basic_goal(self._user, weight_goal, complete_date)
            display_message('Basic goal created', 'You have just created a basic goal', False)
        except Exception as e:
            print(e)
            display_message('Fail to create basic goal',
                            'Please check if you have already created a new basic goal')

    def make_custom_goal(self):
        # get data from the view
        description = self._view.goal_description.toPlainText()
        days = self._view.days.value()
        period = self._view.period.value()
        complete_date = self._view.completion_date.date().toPyDate()
        # pass them to model to create custom goal
        try:
            self._user_custom_goal_model.create_custom_goal(self._user, description, complete_date,
                                                        checkin_interval=days, act_period_length=period)
            display_message('Custom goal created', 'You have just created a new custom goal', False)
        except Exception as e:
            print(e)
            display_message('Fail to create custom goal',
                            'Please check if you have already created a new basic goal')



    # accessor function for the view to allow main presenter to change the view to this
    # (get the main widget like scrollArea/frame to fit into main view)
    def page(self):
        return self._view.scrollArea