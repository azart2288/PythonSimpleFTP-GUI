# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(478, 318)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pass_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_edit.setObjectName("pass_edit")
        self.gridLayout.addWidget(self.pass_edit, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 3)
        self.user_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.user_edit.setObjectName("user_edit")
        self.gridLayout.addWidget(self.user_edit, 0, 0, 1, 1)
        self.port_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.port_edit.setObjectName("port_edit")
        self.gridLayout.addWidget(self.port_edit, 2, 0, 1, 1)
        self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_button.setObjectName("cancel_button")
        self.gridLayout.addWidget(self.cancel_button, 3, 2, 1, 1)
        self.okay_button = QtWidgets.QPushButton(self.centralwidget)
        self.okay_button.setObjectName("okay_button")
        self.gridLayout.addWidget(self.okay_button, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 478, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Password (default anonymous@)"))
        self.label.setText(_translate("MainWindow", "User_Name (default anonymous)"))
        self.cancel_button.setText(_translate("MainWindow", "Cancel"))
        self.okay_button.setText(_translate("MainWindow", "Okay"))
        self.label_3.setText(_translate("MainWindow", "Port  (default 21)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
