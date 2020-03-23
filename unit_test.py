import sys
from datetime import datetime

import pytest
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication

import ModelHandler
from MainPresenter import MainPresenter
from RegisterPresenter import RegisterPresenter
from User import User

'''
This unit test carries out 4 tests
1. Insertion on database
2. Login with correct username and incorrect password
3. Login with correct username and blank password
4. Login with blank username and blank password

When a message box appears saying login failed, click 'OK' to perform next test.
Otherwise, the application gets stuck in the event loop
'''


@pytest.fixture(scope='module')
def session():
    session = ModelHandler.make_session()  # set up of session
    yield session  # return session
    session.rollback()  # teardown session. Rollback any changes to db
    session.close()  # close session


@pytest.fixture(scope='module')
def dbLength(session):
    rows = session.query(User).count()  # counts number of rows in database before add any data
    print('db length is', rows)
    yield rows  # return number of rows


@pytest.fixture(scope='module')
def add_user(session):
    user = User()
    user.password = 'password'
    user.username = 'Covid19'
    user.email = 'Covid19@gmail.com'
    user.name = 'Coronavirus'
    user.gender = 'other'
    date_object = datetime.strptime('20/11/2019',
                                    '%d/%m/%Y').date()  # converting a date string to date object. See format
    user.dob = date_object
    user.age = user.age_calculator()
    user.weight = 89
    user.height = 190
    session.add(user)  # add this temporary user
    yield session


def test_addedUser(dbLength, add_user):
    rowAfterAdd = add_user.query(User).count()  # count rows after addition of a user
    assert rowAfterAdd == dbLength + 1  # expected is originadbLength+1


def test_invalidLogin():
    app = QApplication(sys.argv)
    registerPresenterWindow = RegisterPresenter()
    result = registerPresenterWindow.test_loginInput(registerPresenterWindow, 'Munbodh21',
                                                     'alddjd')  # valid username but invalid password
    QTest.qWait(2.0 * 1000)  # wait 2 seconds before closing login window
    app.exit()
    # registerPresenterWindow._view.close()
    expected = None
    assert result == expected


def test_blank_password():
    app = QApplication(sys.argv)
    registerPresenterWindow = RegisterPresenter()
    result = registerPresenterWindow.test_loginInput(registerPresenterWindow, 'NodeJS', '')  # blank password
    QTest.qWait(2.0 * 1000)
    app.exit()
    # registerPresenterWindow._view.close()
    expected = None
    assert result == expected


def test_blank():
    app = QApplication(sys.argv)
    registerPresenterWindow = RegisterPresenter()
    result = registerPresenterWindow.test_loginInput(registerPresenterWindow, '', '')  # blank username
    QTest.qWait(2.0 * 1000)
    app.exit()
    # registerPresenterWindow._view.close()
    expected = None
    assert result == expected


def test_validLogin():
    app = QApplication(sys.argv)
    registerPresenterWindow = RegisterPresenter()
    result = registerPresenterWindow.test_loginInput(registerPresenterWindow, 'Munbodh21',
                                                     'Hemal21')  # valid username valid password
    QTest.qWait(2.0 * 1000)  # wait 2 seconds before closing login window
    app.exit()
    expected = MainPresenter('Munbodh21')
    assert result.current_user == expected.current_user


def test_loginWithNoUserName():
    app = QApplication(sys.argv)
    registerPresenterWindow = RegisterPresenter()
    result = registerPresenterWindow.test_loginInput(registerPresenterWindow, '', 'H')
    QTest.qWait(4.0 * 1000)  # wait 2 seconds before closing login window
    assert result == None
