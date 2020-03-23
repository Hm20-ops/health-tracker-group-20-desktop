import sys
from functools import partial

from PyQt5.QtCore import pyqtSlot
from validate_email import validate_email

import User
from Diet import *
from helper import display_message
from profileView import Ui_Profile
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox


class profilePresenter:
    # constructor that initializes the model and the view
    def __init__(self, parent, username):
        self._user_model = User.User()
        self._user = username
        self._user_data = self._user_model.get_user(username)
        self._view = Ui_Profile(parent, self._user_data)
        self._view.edit_info.clicked.connect(lambda :self.edit_details(self._user))
        # enable edit info button when user make changes to the fields
        self._view.username.textChanged.connect(partial(self.enable_edit))
        self._view.name.textChanged.connect(partial(self.enable_edit))
        self._view.dob.dateChanged.connect(partial(self.enable_edit))
        self._view.gender.currentTextChanged.connect(partial(self.enable_edit))
        self._view.weight.valueChanged.connect(partial(self.enable_edit))
        self._view.height.valueChanged.connect(partial(self.enable_edit))
        self._view.email.textChanged.connect(partial(self.enable_edit))

    @pyqtSlot()
    def edit_details(self, user):
        valid = True
        # get all data from the view
        new_username = self._view.username.text()
        new_name = self._view.name.text()
        new_dob = self._view.dob.text()
        new_gender = self._view.gender.currentText().lower()
        new_weight = self._view.weight.value()
        new_height = self._view.height.value()
        new_email = self._view.email.text()

        # validate the input
        if len(new_username) == 0:
            display_message('username is empty', 'username cannot be empty')
            valid = False
        if len(new_name) == 0:
            display_message('name is empty', 'name cannot be empty')
            valid = False
        if len(new_email) == 0 or not validate_email(new_email):
            display_message('email is empty or invalid', 'email cannot be empty, please enter a valid email')
            valid = False

        if valid:
            # push changes to the database
            self._user_model.edit_details(user, new_username, new_name, new_dob,
                                          new_gender, new_weight, new_height, new_email)
            display_message('Details editted successfully', 'You have update your details!', False)

    def enable_edit(self):
        if not self._view.edit_info.isEnabled():
            self._view.edit_info.setDisabled(False)

    def page(self):
        return self._view.frame