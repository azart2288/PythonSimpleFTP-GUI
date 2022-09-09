from PyQt5 import QtCore, QtGui, QtWidgets
import form 
import interface
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget  ,QListWidget, QListWidgetItem, QAbstractItemView
from PyQt5.QtGui import QPixmap
import newinterface
from ftplib import FTP
from os import path
import options
import ru_options
import ru_form
import ru_interface
import ru_newinterface
import ru_interface
from form_main import Form

#Ftp_url = []




class ExampleApp(QtWidgets.QMainWindow, interface.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.openfolder_button.clicked.connect(self.browsefolder)
        self.about_button.clicked.connect(self.showdialog)
        self.ftpbutton.clicked.connect(self.showftp)
        self.f1 = Form()
        #ftp = FTP()
        self.reloadbutton.clicked.connect(self.reload)
        self.save_button.clicked.connect(self.savefile)
        self.option_button.clicked.connect(self.options)
        self.back_button.clicked.connect(self.backdir)
        self.home_button.clicked.connect(self.homedir)
        self.next_button.clicked.connect(self.nextdir)
        self.upload_button.clicked.connect(self.upload)


        #self.serverlist.itemSelectionChanged.connect(self.savefile)
        self.serverlist.itemDoubleClicked.connect(self.changedir)

    
    def upload(self):
        try:
            
            self.select = (self.locallist.currentItem().text())
            self.full_select = (self.directory + "/" + self.select)
        except:
            pass

        try:

            with open(self.full_select , "rb") as up_file:
                self.ftp.storbinary('STOR %s' % self.select, up_file)
        except:
            pass







    def nextdir(self):
        self.serverlist.clear()
        self.ftp.cwd(self.ftp_path)
        self.files.clear()
        self.ftp.retrlines("NLST" , self.files.append)

        for filenames in self.files:
            self.stringfiles=''.join(map(str,filenames))
            self.serverlist.addItem(self.stringfiles)

        



    def homedir(self):
        default_home = "/"
        self.ftp.cwd(default_home)
        self.serverlist.clear()
        self.files.clear()
        self.ftp.retrlines("NLST" , self.files.append)

        for filenames in self.files:
            self.stringfiles=''.join(map(str,filenames))
            self.serverlist.addItem(self.stringfiles)

    def options(self):
        from options_main import Options , Ru_options
        self.op1 = Options()
        #print(self.op1.toggled())
        self.op1.show()

    def changedir(self):
        doublefilename = (self.serverlist.currentItem().text())
        try:
            self.ftp.cwd(doublefilename)
        except:
            pass
        self.serverlist.clear()
        self.files.clear()
        self.ftp.retrlines("NLST" , self.files.append)

        for filenames in self.files:
            self.stringfiles=''.join(map(str,filenames))
            self.serverlist.addItem(self.stringfiles)



    def backdir(self):
        self.serverlist.clear()
        self.ftp_path = (f"{self.ftp.pwd()}")
        ftp_path = ('/'.join(self.ftp_path.split('/')[:-1]))
        self.ftp.cwd(ftp_path)
        self.files.clear()
        self.ftp.retrlines("NLST" , self.files.append)

        for filenames in self.files:
            self.stringfiles=''.join(map(str,filenames))
            self.serverlist.addItem(self.stringfiles)




    def savefile(self):
        filename = (self.serverlist.currentItem().text())
        filepath = os.path.join(self.directory, filename)

        with open(filepath , 'wb') as f:
            self.ftp.retrbinary('RETR ' + filename, f.write)
            self.locallist.addItem(filename)

        self.locallist.repaint()


    def reload(self):
        try:
            self.serverlist.clear()
            self.f1 = Form()
            #self.Ftp_url = Ftp_url()
            self.ftp_url=''.join(map(str, self.f1.list()))
            self.ftp = FTP(self.ftp_url)
            self.ftp.login()
            self.files = []
            self.ftp.retrlines("NLST",self.files.append)
            #self.ftp.close()
        except:
            pass


        try:
            for filenames in self.files:
                self.stringfiles=''.join(map(str,filenames))
                self.serverlist.addItem(self.stringfiles)
        except:
            pass

    def browsefolder(self):
        self.locallist.clear()
        self.directory = QtWidgets.QFileDialog.getExistingDirectory(self , "open folder" , 'F://' ,  QtWidgets.QFileDialog.ShowDirsOnly)
        

        if self.directory:
            for file_name in os.listdir(self.directory):

                self.locallist.addItem(file_name)


    def showdialog(self):
        self.d1 = Dialog()
        self.d1.show()

    def showftp(self):
        self.f1 = Form()
        self.f1.show()





class Dialog(QtWidgets.QMainWindow, newinterface.Ui_SecondWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)








def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
