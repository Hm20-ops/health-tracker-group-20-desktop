import sys
from functools import partial

from PyQt5.QtCore import pyqtSlot

import User
from BasicGoal import BasicGoal
from CustomGoal import *
from Group import Group
from Diet import *
import RegisterPresenter
from mainView import Ui_Health_tracker
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from homeView import Ui_Home
import CustomGoal

class homePresenter:
	def __init__(self, parent, username):
		#self._redirect_to = None
		self._user_model = User.User()
		self._user = username
		self._group_model = Group()
		# self._basic_goal_model = BasicGoal()
		self._custom_goal_model = CustomGoal.UserCustomGoal()
		goals = self._custom_goal_model.get_recent(username)
		# _basic_goals = [{'username': self._user, 'target_weight': 50, 'date': date.today(), 'isMet': True},
		# 				{'username': self._user, 'target_weight': 30, 'date': '01/04/2020', 'isMet': False},
		# 				{'username': self._user, 'target_weight': 50, 'date': date.today(), 'isMet': True}
		# 				]
		self._view = Ui_Home(parent, goals).scrollArea

	def page(self):
		return self._view