# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exprm.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
# from homePresenter import homePresenter

class Ui_Health_tracker(object):
	def setupUi(self, Healthtracker):
		Healthtracker.setObjectName("Healthtracker")
		Healthtracker.resize(1600, 900)
		self.centralwidget = QtWidgets.QWidget(Healthtracker)
		self.centralwidget.setObjectName("centralwidget")
		self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
		self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_4.setSpacing(0)
		self.verticalLayout_4.setObjectName("verticalLayout_4")
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setSpacing(0)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.side_nav_bar = QtWidgets.QListWidget(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(2)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.side_nav_bar.sizePolicy().hasHeightForWidth())
		self.side_nav_bar.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setPointSize(16)
		self.side_nav_bar.setFont(font)
		self.side_nav_bar.setStyleSheet("QListWidget{\n"
										"background: rgb(63, 63, 63); \n"
										"color:rgb(122, 122, 122);\n"
										"border: none;\n"
										"\n"
										"}\n"
										"QListWidget::item { \n"
										"margin: 10px;\n"
										"padding-top: 20px;\n"
										"padding-left: 40px;\n"
										"}\n"
										"QListWidget::item::icon { \n"
										"size: 10px;\n"
										"}")
		self.side_nav_bar.setAutoScroll(False)
		self.side_nav_bar.setProperty("showDropIndicator", True)
		self.side_nav_bar.setIconSize(QtCore.QSize(50, 30))
		self.side_nav_bar.setObjectName("side_nav_bar")
		item = QtWidgets.QListWidgetItem()
		icon = QtGui.QIcon("./sidebar_icon/home.svg")
		item.setIcon(icon)
		self.side_nav_bar.addItem(item)
		item = QtWidgets.QListWidgetItem()
		icon = QtGui.QIcon("./sidebar_icon/profile.png")
		item.setIcon(icon)
		self.side_nav_bar.addItem(item)
		item = QtWidgets.QListWidgetItem()
		icon = QtGui.QIcon("./sidebar_icon/goal.png")
		item.setIcon(icon)
		self.side_nav_bar.addItem(item)
		item = QtWidgets.QListWidgetItem()
		icon = QtGui.QIcon("./sidebar_icon/runner.png")
		item.setIcon(icon)
		self.side_nav_bar.addItem(item)
		item = QtWidgets.QListWidgetItem()
		icon = QtGui.QIcon("./sidebar_icon/diet.png")
		item.setIcon(icon)
		self.side_nav_bar.addItem(item)
		item = QtWidgets.QListWidgetItem()
		icon = QtGui.QIcon("./sidebar_icon/group.png")
		item.setIcon(icon)
		self.side_nav_bar.addItem(item)
		item = QtWidgets.QListWidgetItem()
		item.setTextAlignment(int(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter))
		icon = QtGui.QIcon("./sidebar_icon/logout.png")
		item.setIcon(icon)
		brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
		brush.setStyle(QtCore.Qt.NoBrush)
		item.setBackground(brush)
		brush = QtGui.QBrush(QtGui.QColor(184, 0, 0))
		brush.setStyle(QtCore.Qt.NoBrush)
		item.setForeground(brush)
		self.side_nav_bar.addItem(item)
		self.horizontalLayout.addWidget(self.side_nav_bar)
		self.display_page = QtWidgets.QStackedWidget(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(9)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.display_page.sizePolicy().hasHeightForWidth())
		self.display_page.setSizePolicy(sizePolicy)
		self.display_page.setObjectName("display_page")
		self.horizontalLayout.addWidget(self.display_page)
		self.verticalLayout_4.addLayout(self.horizontalLayout)
		Healthtracker.setCentralWidget(self.centralwidget)

		self.retranslateUi(Healthtracker)
		QtCore.QMetaObject.connectSlotsByName(Healthtracker)

	def retranslateUi(self, Healthtracker):
		_translate = QtCore.QCoreApplication.translate
		Healthtracker.setWindowTitle(_translate("Healthtracker", "MainWindow"))
		__sortingEnabled = self.side_nav_bar.isSortingEnabled()
		self.side_nav_bar.setSortingEnabled(False)
		item = self.side_nav_bar.item(0)
		item.setText(_translate("Healthtracker", " Home"))
		item = self.side_nav_bar.item(1)
		item.setText(_translate("Healthtracker", " Profile"))
		item = self.side_nav_bar.item(2)
		item.setText(_translate("Healthtracker", " Goal"))
		item = self.side_nav_bar.item(3)
		item.setText(_translate("Healthtracker", " Exercise"))
		item = self.side_nav_bar.item(4)
		item.setText(_translate("Healthtracker", " Diet"))
		item = self.side_nav_bar.item(5)
		item.setText(_translate("Healthtracker", " Group"))
		item = self.side_nav_bar.item(6)
		item.setText(_translate("Healthtracker", " Log out"))
		self.side_nav_bar.setSortingEnabled(__sortingEnabled)
