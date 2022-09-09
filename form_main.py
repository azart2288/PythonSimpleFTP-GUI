from PyQt5 import QtCore, QtGui, QtWidgets
import form
import ru_form
Ftp_url = []




class Form(QtWidgets.QMainWindow, form.Ui_MainWindow ):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connect_button.clicked.connect(self.ftpconnect)
        self.cancel_button.clicked.connect(self.close)

    def list(self):
    	return Ftp_url



    def ftpconnect(self):
        #self.ex1 = ExampleApp()
        Ftp_url.clear()
        self.x = self.ftp_edit.text()
        #self.Ftp_url = Ftp_url()

        Ftp_url.append(self.x)

        self.close()


class Ru_Form(QtWidgets.QMainWindow, ru_form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


    def list(self):
        return Ftp_url


    def ftpconnect(self):
        #self.ex1 = ExampleApp()
        self.x = self.ftp_edit.text()
        #self.Ftp_url = Ftp_url()

        Ftp_url.append(self.x)

        self.close()
