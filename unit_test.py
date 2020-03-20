import sys
import unittest

from PyQt5.QtWidgets import QApplication

from RegisterPresenter import RegisterPresenter
from MainPresenter import MainPresenter
from PyQt5.QtTest import QTest


class MyTestCase(unittest.TestCase):
	app = QApplication(sys.argv)
	def test_success(self):
		x = RegisterPresenter()
		result = x.test_input('Munbodh21', 'Hemal21')
		expected = MainPresenter('Munbodh21')
		self.assertEqual(result.current_user, expected.current_user)
		#app.exec_()

	def test_fail(self):
		x = RegisterPresenter()
		result = x.test_input('Munbodh21', 'alddjd')
		expected = None
		self.assertEqual(result, expected)

	def test_blank_password(self):
		x = RegisterPresenter()
		result = x.test_input('NodeJS', '')
		expected = None
		self.assertEqual(result, expected)

	def test_blank(self):
		x = RegisterPresenter()
		result = x.test_input('', '')
		expected = None
		self.assertEqual(result, expected)

if __name__ == '__main__':
	unittest.main()
