from PyQt5 import QtCore, QtGui, QtWidgets
import info
User  = []
Password = []
Port = []
Default_Password = "anonymous@"
Default_user = "anonymous"
Default_port = int(21)
import sys 


class Info(QtWidgets.QMainWindow, info.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.okay_button.clicked.connect(self.get_info)

	def get_info(self):
		self.inf = self.user_edit.text()
		self.pas = self.pass_edit.text()
		self.port = self.port_edit.text()
		if self.inf == "":
			User.clear()
			User.append(Default_user)
		else:
			User.clear()
			User.append(self.inf)


		if self.port == "":
			Port.clear()
			Port.append(Default_port)
		else:
			Port.clear()
			Port.append(self.port)


		if self.pas == "":
			Password.clear()
			Password.append(Default_Password)
		else:
			Password.clear()
			Password.append(self.pas)

		self.close()

		


	def user(self):
		return User


	def password(self):
		return Password

	def port(self):
		return Port