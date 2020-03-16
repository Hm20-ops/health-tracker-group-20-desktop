import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from validate_email import validate_email
import User
import MainPresenter
from User import User
from functools import partial
from sqlalchemy.orm import sessionmaker
from signinView import Ui_signinWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtCore import pyqtSlot
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

        print('adding user')
        # obtain all information inputted on the view
        name = self._view.name.text()
        gender = self._view.gender.currentText().lower()
        dob = self._view.dob.text()
        username = self._view.username.text()
        password = self._view.password.text()
        email = self._view.email.text()
        height = int(self._view.height.text())
        weight = int(self._view.weight.text())
        print(username, email, password, name, dob, weight, height, gender)

        # try to add new user to database
        try:
            if not _add_validation():
                return
            # ask model to create a new user
            self._model.create_user(username, email, password, name, dob, weight, height, gender)
            # send verification email to the email provided
            send_email_to(email)
            # display success message
            display_message("Account created successfully!",
                            "Please check your email to verify your account", False)
        except Exception as e:
            print(e)
            # display error message
            display_message("Error creating user!",
                            "Please check if you enter a valid data!")


    '''
    A helper function to display message box when an error occurs or 
    give success information to user
    '''
    # def _display_message(self, title, text, error=True):
    #     msg = QMessageBox()
    #     msg_type = QMessageBox.Critical if error else QMessageBox.Information
    #     msg.setWindowTitle(title)
    #     msg.setText(text)
    #     msg.setIcon(msg_type)
    #     msg.setStandardButtons(QMessageBox.Ok)
    #     msg.exec_()

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
        # if len(username) == 0 or len(password) == 0:
        #     check = False
        # else:
        #     check = session.query(User).filter(User.username == username, User.password == password).first()
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



    '''
    A helper function to send email to an email address, that is used for when creating account 
    and invite a user to a group and notify group members of archiving group goal or a new group goal
    '''
    # def send_email_to(self, email_to):
    #     email = 'emailforadvertsandtests@gmail.com'
    #     password = 'doonrkovjqdmmqow'
    #     send_to_email = email_to
    #     subject = 'Verification needed to complete health tracker registration'  # The subject line
    #     message = 'Thanks for registering. Please click the following link to complete the registration\n' \
    #               'https://healthtracker.io/verify/325455632'
    #
    #     # creating the email instance(MIMEMultipart) and set header fields
    #     msg = MIMEMultipart()
    #     msg['From'] = email
    #     msg['To'] = send_to_email
    #     msg['Subject'] = subject
    #
    #     # Attach the message to the email object
    #     msg.attach(MIMEText(message, 'plain'))
    #
    #     # Login to the email server with TLS and send email
    #     server = smtplib.SMTP('smtp.gmail.com', 587)
    #     server.starttls()
    #     server.login(email, password)
    #     text = msg.as_string()  # convert the email object to a string to send
    #     server.sendmail(email, send_to_email, text)
    #     server.quit()


class MainWindow(QMainWindow, Ui_signinWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    RegisterPresenter()

    app.exec()
