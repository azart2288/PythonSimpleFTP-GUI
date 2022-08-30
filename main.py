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

Ftp_url = []




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


        #self.serverlist.itemSelectionChanged.connect(self.savefile)
        self.serverlist.itemDoubleClicked.connect(self.changedir)

    


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
        self.op1 = Options()
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



        #for ftpbacks in ftp_path:

        

    def savefile(self):
        filename = (self.serverlist.currentItem().text())
        filepath = os.path.join(self.directory, filename)




        #file = names.data()
        #file.append(names)
        #files=''.join(map(str,file))

        #path = []
        #path.append(self.directory)
        #print(path)

        with open(filepath , 'wb') as f:
            self.ftp.retrbinary('RETR ' + filename, f.write)
            self.locallist.addItem(filename)

        self.locallist.repaint()









    def reload(self):
        self.serverlist.clear()
        #f = open("log.txt")
        #x = f.read()
        try:
            self.ftp_url=''.join(map(str, Ftp_url))
            self.ftp = FTP(self.ftp_url)
            self.ftp.login()
            self.files = []
            self.ftp.retrlines("NLST",self.files.append)
        except:
            pass

        try:
            for filenames in self.files:
                self.stringfiles=''.join(map(str,filenames))
                self.serverlist.addItem(self.stringfiles)
        except:
            pass
        #stringfiles2=''.join(map(str,elem2))
        #self.serverlist.addItem(stringfiles)
        #self.serverlist.addItem(stringfiles2)

            
        #self.ex1.serverlist.addItem(self.logic)



        

        

    def browsefolder(self):
        self.locallist.clear()
        self.directory = QtWidgets.QFileDialog.getExistingDirectory(self , "open folder" , 'F://' ,  QtWidgets.QFileDialog.ShowDirsOnly)
        

        if self.directory:
            for file_name in os.listdir(self.directory):

                self.locallist.addItem(file_name)

                #print(currectfiles_list)


        #n = 10
        #currect_files = []
        #currect_files.append(self.directory)
        #for i in range(1 , n):
            #i = os.listdir(self.directory)
            #if i:

                #f = ''.join(map(str,i))
                #self.locallist.addItem(f)







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

class Form(QtWidgets.QMainWindow, form.Ui_MainWindow, interface.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connect_button.clicked.connect(self.ftpconnect)
        self.cancel_button.clicked.connect(self.close)


    def ftpconnect(self , x):
        self.ex1 = ExampleApp()
        self.x = self.ftp_edit.text()

        #with open('log.txt' , 'wb') as f:
            #f.write(self.x.encode('utf-8'))
        Ftp_url.append(self.x)

        #ftp = FTP(x)
        #ftp.login()
        #line = ftp.retrlines("NLST",self.files.append)
        #self.ex1.serverlist.addItem(self.logic)
        #self.ex1.serverlist.repaint()

        self.close()


class Options(QtWidgets.QMainWindow, options.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Ru_lang.toggled.connect(self.russian)

    def russian(self):
        print("sus")


        








def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()