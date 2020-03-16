import sys
from functools import partial

from PyQt5.QtCore import pyqtSlot
import User
from Diet import *
from profileView import Ui_Profile
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox


class profilePresenter:
    def __init__(self, parent, username):
        #self._redirect_to = None
        self._user_model = User.User()
        self._user = username
        self._user_data = self._user_model.get_user(username)
        self._view = Ui_Profile(parent, self._user_data)
        self._view.edit_info.clicked.connect(lambda :self.edit_details(self._user))

    @pyqtSlot()
    def edit_details(self, user):
        # get all data from the view
        new_username = self._view.username.text()
        new_name = self._view.name.text()
        new_dob = self._view.dob.text()
        new_gender = self._view.gender.currentText().lower()
        new_weight = self._view.weight.value()
        new_height = self._view.height.value()
        new_email = self._view.email.text()
        # push changes to the database
        self._user_model.edit_details(user, new_username, new_name, new_dob, new_gender, new_weight, new_height, new_email)


    def page(self):
        return self._view.frame