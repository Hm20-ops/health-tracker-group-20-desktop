# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profile.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Profile(object):
	def __init__(self, parent, user_data=()):
		self.setupUi(parent, user_data)

	def setupUi(self, Form, user_data):
		Form.setObjectName("Form")
		Form.resize(969, 813)
		self.verticalLayout = QtWidgets.QVBoxLayout(Form)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setSpacing(0)
		self.verticalLayout.setObjectName("verticalLayout")

		self.frame = QtWidgets.QFrame(Form)
		self.frame.setStyleSheet("QFrame{\n"
								 "background-color: rgb(255, 255, 255);\n"
								 "color:rgb(62, 62, 62);\n"
								 "border: none;\n"
								 "}")
		self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame.setObjectName("frame")
		self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame)
		self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_10.setSpacing(0)
		self.verticalLayout_10.setObjectName("verticalLayout_10")
		self.header = QtWidgets.QLabel(self.frame)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(1)
		sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())

		self.header.setSizePolicy(sizePolicy)
		self.header.setStyleSheet("QLabel{\n"
								  "background:rgb(218, 0, 0); \n"
								  "color:rgb(59, 59, 59);\n"
								  "border: none;\n"
								  "}")
		self.header.setIndent(40)
		self.header.setObjectName("header")
		self.verticalLayout_10.addWidget(self.header)
		self.wrapper = QtWidgets.QFrame(self.frame)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(9)
		sizePolicy.setHeightForWidth(self.wrapper.sizePolicy().hasHeightForWidth())
		self.wrapper.setSizePolicy(sizePolicy)
		self.wrapper.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.wrapper.setFrameShadow(QtWidgets.QFrame.Raised)
		self.wrapper.setObjectName("wrapper")
		self.gridLayout = QtWidgets.QGridLayout(self.wrapper)
		self.gridLayout.setContentsMargins(95, 100, 300, 300)
		self.gridLayout.setHorizontalSpacing(45)
		self.gridLayout.setVerticalSpacing(30)
		self.gridLayout.setObjectName("gridLayout")
		self.user_data = QtWidgets.QFrame(self.wrapper)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(18)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.user_data.sizePolicy().hasHeightForWidth())
		self.user_data.setSizePolicy(sizePolicy)
		self.user_data.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.user_data.setFrameShadow(QtWidgets.QFrame.Raised)
		self.user_data.setObjectName("user_data")
		self.formLayout = QtWidgets.QFormLayout(self.user_data)
		self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
		self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
		self.formLayout.setContentsMargins(0, 0, 0, 0)
		self.formLayout.setHorizontalSpacing(0)
		self.formLayout.setVerticalSpacing(20)
		self.formLayout.setObjectName("formLayout")
		self.name_label = QtWidgets.QLineEdit(self.user_data)
		self.name_label.setStyleSheet("QLineEdit{\n"
									  "background: rgb(222, 222, 222); \n"
									  "color:rgb(0, 0, 0);\n"
									  "}")
		self.name_label.setReadOnly(True)
		self.name_label.setObjectName("name_label")
		self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.name_label)
		self.name = QtWidgets.QLineEdit(self.user_data)
		self.name.setText(user_data.name)
		self.name.setObjectName("name")
		self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name)
		self.username_label = QtWidgets.QLineEdit(self.user_data)
		self.username_label.setStyleSheet("QLineEdit{\n"
										  "background: rgb(222, 222, 222); \n"
										  "color:rgb(0, 0, 0);\n"
										  "}")
		self.username_label.setReadOnly(True)
		self.username_label.setObjectName("username_label")
		self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.username_label)
		self.username = QtWidgets.QLineEdit(self.user_data)
		self.username.setText(user_data.username)
		self.username.setObjectName("username")
		self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.username)
		self.dob_label = QtWidgets.QLineEdit(self.user_data)
		self.dob_label.setStyleSheet("QLineEdit{\n"
									 "background: rgb(222, 222, 222); \n"
									 "color:rgb(0, 0, 0);\n"
									 "}")
		self.dob_label.setReadOnly(True)
		self.dob_label.setObjectName("dob_label")
		self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.dob_label)
		self.dob = QtWidgets.QDateEdit(self.user_data)
		self.dob.setDateTime(QtCore.QDateTime(QtCore.QDate(user_data.dob.year, user_data.dob.month, user_data.dob.day), QtCore.QTime(0, 0, 0)))
		self.dob.setMinimumDate(QtCore.QDate(1900, 1, 1))
		self.dob.setMaximumDate(QtCore.QDate(QtCore.QDate.currentDate().year() - 8, 12, 31))
		self.dob.setObjectName("dob")
		self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dob)
		self.gender_label = QtWidgets.QLineEdit(self.user_data)
		self.gender_label.setStyleSheet("QLineEdit{\n"
										"background: rgb(222, 222, 222); \n"
										"color:rgb(0, 0, 0);\n"
										"}")
		self.gender_label.setReadOnly(True)
		self.gender_label.setObjectName("gender_label")
		self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.gender_label)
		self.gender = QtWidgets.QComboBox(self.user_data)
		self.gender.setObjectName("gender")
		self.gender.addItem("")
		self.gender.addItem("")
		self.gender.addItem("")
		self.gender.setCurrentText(user_data.gender)
		self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.gender)
		self.weight_label = QtWidgets.QLineEdit(self.user_data)
		self.weight_label.setStyleSheet("QLineEdit{\n"
										"background: rgb(222, 222, 222); \n"
										"color:rgb(0, 0, 0);\n"
										"}")
		self.weight_label.setReadOnly(True)
		self.weight_label.setObjectName("weight_label")
		self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.weight_label)
		self.weight = QtWidgets.QDoubleSpinBox(self.user_data)
		self.weight.setDecimals(1)
		self.weight.setMinimum(0.0)
		self.weight.setProperty("value", user_data.weight)
		self.weight.setObjectName("weight")
		self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.weight)
		self.height_label = QtWidgets.QLineEdit(self.user_data)
		self.height_label.setStyleSheet("QLineEdit{\n"
										"background: rgb(222, 222, 222); \n"
										"color:rgb(0, 0, 0);\n"
										"}")
		self.height_label.setReadOnly(True)
		self.height_label.setObjectName("height_label")
		self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.height_label)
		self.height = QtWidgets.QSpinBox(self.user_data)
		self.height.setMaximum(250)
		self.height.setSingleStep(0)
		self.height.setProperty("value", user_data.height)
		self.height.setObjectName("height")
		self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.height)
		self.email_label = QtWidgets.QLineEdit(self.user_data)
		self.email_label.setStyleSheet("QLineEdit{\n"
									   "background: rgb(222, 222, 222); \n"
									   "color:rgb(0, 0, 0);\n"
									   "}")
		self.email_label.setReadOnly(True)
		self.email_label.setObjectName("email_label")
		self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.email_label)
		self.email = QtWidgets.QLineEdit(self.user_data)
		self.email.setText(user_data.email)
		self.email.setObjectName("email")
		self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.email)
		self.gridLayout.addWidget(self.user_data, 0, 1, 1, 1)
		self.profile_picture = QtWidgets.QGraphicsView(self.wrapper)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.profile_picture.sizePolicy().hasHeightForWidth())
		self.profile_picture.setSizePolicy(sizePolicy)
		self.profile_picture.setStyleSheet("QGraphicsView{\n"
										   "background: rgb(222, 222, 222); \n"
										   "color:rgb(0, 0, 0);\n"
										   "}")
		self.profile_picture.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.profile_picture.setObjectName("profile_picture")
		self.gridLayout.addWidget(self.profile_picture, 0, 0, 1, 1)

		self.edit_info = QtWidgets.QPushButton(self.wrapper)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.edit_info.sizePolicy().hasHeightForWidth())
		self.edit_info.setSizePolicy(sizePolicy)
		self.edit_info.setStyleSheet("padding: 10 30 10 30;")
		self.edit_info.setObjectName("edit_info")
		self.edit_info.setDisabled(True)
		self.gridLayout.addWidget(self.edit_info, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
		self.upload_photo = QtWidgets.QPushButton(self.wrapper)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.upload_photo.sizePolicy().hasHeightForWidth())
		self.upload_photo.setSizePolicy(sizePolicy)
		self.upload_photo.setStyleSheet("padding: 10 30 10 30;\n")
		icon = QtGui.QIcon("./sidebar_icon/plus.png")
		self.upload_photo.setIcon(icon)
		self.upload_photo.setObjectName("upload_photo")
		self.gridLayout.addWidget(self.upload_photo, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
		self.gridLayout.setColumnStretch(0, 3)
		self.gridLayout.setColumnStretch(1, 4)
		self.gridLayout.setRowStretch(0, 5)
		self.verticalLayout_10.addWidget(self.wrapper)
		self.verticalLayout.addWidget(self.frame)

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Form"))
		self.header.setText(_translate("Form",
									   "<html><head/><body><p><span style=\" font-family:\'Segoe UI\'; font-size:36pt;\">Profile</span></p></body></html>"))
		self.name_label.setText(_translate("Form", "Name"))
		self.username_label.setText(_translate("Form", "Username"))
		self.dob_label.setText(_translate("Form", "Date of birth"))
		self.gender_label.setText(_translate("Form", "Gender"))
		self.gender.setItemText(0, _translate("Form", "Male"))
		self.gender.setItemText(1, _translate("Form", "Female"))
		self.gender.setItemText(2, _translate("Form", "Prefer not to say"))
		self.weight_label.setText(_translate("Form", "Weight (kg)"))
		self.height_label.setText(_translate("Form", "Height (cm)"))
		self.email_label.setText(_translate("Form", "E-mail"))
		self.edit_info.setText(_translate("Form", "Edit Information"))
		self.upload_photo.setText(_translate("Form", "Upload Photo"))
