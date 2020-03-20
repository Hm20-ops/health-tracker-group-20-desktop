import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from PyQt5.QtTest import QTest
from validate_email import validate_email
import User
import MainPresenter
from User import User
from functools import partial
from sqlalchemy.orm import sessionmaker
from signinView import Ui_signinWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtCore import pyqtSlot, Qt
from helper import *

'''
RegisterPresenter controls the login and registration process of the signin view
'''
class RegisterPresenter:
    def __init__(self):
        self._redirect_to = None
        self._view = MainWindow()
        self._model = User()
        self._view.login.clicked.connect(lambda: self.login())
        self._view.create_account.clicked.connect(partial(self._view.stackedWidget.setCurrentIndex, 1))
        self._view.cancel.clicked.connect(partial(self._view.stackedWidget.setCurrentIndex, 0))
        self._view.signup.clicked.connect(lambda: self.add_user())
        self._view.show()

    '''
    Add a new user to database when new user register a new account on the view
    that takes all the input from the registration form to the database
    '''
    def add_user(self):
        # inner function for data validation when user submit the data
        def _add_validation():
            valid = True
            error_message = ''
            if not validate_email(email):
                valid = False
                error_message = "Please enter a valid email address"
            if height <= 0 or weight <= 0:
                valid = False
                error_message = "height and weight must be greater than 0"

            if not valid:
                display_message('Invalid input data', error_message)
            return valid

        # try to add new user to database
        try:
            print('adding user')
            # obtain all information inputted on the view
            name = self._view.name.text()
            gender = self._view.gender.currentText().lower()
            if gender == 'prefer not to say':
                gender = 'other'
            dob = self._view.dob.text()
            username = self._view.username.text()
            password = self._view.password.text()
            email = self._view.email.text()
            height = int(self._view.height.text())
            weight = int(self._view.weight.text())
            print(username, email, password, name, dob, weight, height, gender)
            if not _add_validation():
                return
            # ask model to create a new user
            self._model.create_user(username, email, password, name, dob, weight, height, gender)
            # send verification email to the email provided
            send_email_to(email,
                          'Verification needed to complete health tracker registration',
                          'Thanks for registering. Please click the following link to complete the registration\n' \
                          'https://healthtracker.io/verify/325455632')
            # display success message
            display_message("Account created successfully!",
                            "Please check your email to verify your account", False)
        except Exception as e:
            print(e)
            # display error message
            display_message("Error creating user!",
                            "Please check if you enter valid data!")

    '''
    function to login to the home screen of the program with the input username and password on the view
    '''
    def login(self):
        # establish connection to the database
        session = self._model.make_session()
        # get username and password from the view
        username = self._view.login_username.text()
        password = self._view.login_password.text()
        # check if username and password are correct
        check = session.query(User).filter(User.username == username, User.password == password).first() \
                if len(username) != 0 or len(password) != 0 else False
        session.close()
        # if the check is successful redirect to the user home page, otherwise display error message
        if check:
            print('login success')
            self._redirect_to = MainPresenter.MainPresenter(username)
            self._view.close()
            return self._redirect_to
        else:
            print('login failed')
            display_message("Login Error",
                            "username or password is incorrect")

    def test_input(self, username, password):
        self._view.login_username.setText(username)
        self._view.login_password.setText(password)
        QTest.mouseClick(self._view.login, Qt.LeftButton)
        return self._redirect_to


class MainWindow(QMainWindow, Ui_signinWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    RegisterPresenter()

    app.exec()
