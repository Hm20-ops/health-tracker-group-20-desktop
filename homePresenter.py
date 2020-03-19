import sys
from functools import partial

from PyQt5.QtCore import pyqtSlot

import User
from BasicGoal import BasicGoal
from CustomGoal import *
from DietPresenter import DietPresenter
from ExercisePresenter import ExercisePresenter
from Group import Group
from Diet import *
from UserExercise import UserExercise
from helper import display_message
from mainView import Ui_Health_tracker
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog
from homeView import Ui_Home
from CustomGoal import CustomGoal

class homePresenter:
	def __init__(self, parent, username):
		self.parent = parent
		self._user_model = User.User()
		self._user = username
		self._exercise_model = UserExercise()
		self._diet_model = UserMeal()
		self._food_calorie = int(self._diet_model.totalCalorieToday(username))
		self._calorie_burnt = int(self._exercise_model.totalCaloriesBurnt(username))
		self._custom_goal_model = CustomGoal()
		goals = self._custom_goal_model.get_recent(username)
		self.data = [65, 64.9, 64.6, 64.5, 64.5, 64.3, 64.2]
		self._view = Ui_Home(parent, goals, self._food_calorie, self._calorie_burnt, self.data)
		self._view.add_exercise.clicked.connect(lambda: self.to_exercise())
		self._view.add_diet.clicked.connect(lambda: self.to_diet())
		self._view.add_weight.clicked.connect(lambda: self.update_weight())

	def to_exercise(self):
		redirect = ExercisePresenter(self.parent, self._user).page()
		self.parent.addWidget(redirect)
		self.parent.setCurrentWidget(redirect)
		return redirect

	def to_diet(self):
		redirect = DietPresenter(self.parent, self._user).page()
		self.parent.addWidget(redirect)
		self.parent.setCurrentWidget(redirect)
		return redirect

	def update_weight(self):
		num, ok = QInputDialog.getDouble(self.page(), "Update weight", "Enter your new weight", 65, 60, 80)

		if ok:
			self.data.append(num)
			self._user_model.update_weight(self._user, num)
			self.parent.update()

			display_message('Weight added successfully', f'Good work! You are now {num} kg', False)


	def page(self):
		return self._view.scrollArea