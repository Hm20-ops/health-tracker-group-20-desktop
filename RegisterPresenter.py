import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from validate_email import validate_email
import User
from User import User
from functools import partial
from sqlalchemy.orm import sessionmaker
from signinView import Ui_signinWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox


class RegisterPresenter:
    def __init__(self):
        self._view = MainWindow()
        self._model = User()
        self._view.login.clicked.connect(lambda: self.login())
        self._view.signup.clicked.connect(lambda: self.add_user())
        self._view.show()

    def add_user(self):
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
                self._display_message('Invalid input data', error_message)
            return valid

        print('adding user')
        name = self._view.name.text()
        gender = self._view.gender.currentText()
        dob = self._view.dob.text()
        username = self._view.username.text()
        password = self._view.password.text()
        email = self._view.email.text()
        height = int(self._view.height.text())
        weight = int(self._view.weight.text())
        print(username, email, password, name, dob, weight, height, gender)

        try:
            if not _add_validation():
                return
            self._model.create_user(username, email, password, name, dob, weight, height, gender)
            self.send_email_to(email)
            self._display_message("Account created successfully!",
                                  "Please check your email to verify your account", False)
        except Exception as e:
            print(e)
            self._display_message("Error creating user!",
                                  "Please check if you enter a valid data!")



    def _display_message(self, title, text, error=True):
        msg = QMessageBox()
        msg_type = QMessageBox.Critical if error else QMessageBox.Information
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(msg_type)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def login(self):
        session = self._model.make_session()
        username = self._view.login_username.text()
        password = self._view.login_password.text()
        check = session.query(User).filter(User.username == username, User.password == password)

        if check.first():
            print('is valid')
        else:
            print('is not valid')
            msg = QMessageBox()
            msg.setWindowTitle("Login Error")
            msg.setText("username or password is incorrect")
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        session.close()

    def send_email_to(self, email_to):
        email = 'emailforadvertsandtests@gmail.com'
        password = 'doonrkovjqdmmqow'
        send_to_email = email_to
        subject = 'Verification needed to complete health tracker registration'  # The subject line
        message = 'Thanks for registering. Please click the following link to complete the registration\n' \
                  'https://healthtracker.io/verify/325455632'

        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = send_to_email
        msg['Subject'] = subject

        # Attach the message to the MIMEMultipart object
        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        text = msg.as_string()  # You now need to convert the MIMEMultipart object to a string to send
        server.sendmail(email, send_to_email, text)
        server.quit()


class MainWindow(QMainWindow, Ui_signinWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    x = RegisterPresenter()

    app.exec()
