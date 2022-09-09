# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 675)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.about_button = QtWidgets.QPushButton(self.centralwidget)
        self.about_button.setObjectName("about_button")
        self.gridLayout.addWidget(self.about_button, 1, 0, 1, 1)
        self.option_button = QtWidgets.QPushButton(self.centralwidget)
        self.option_button.setObjectName("option_button")
        self.gridLayout.addWidget(self.option_button, 1, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.serverlist = QtWidgets.QListWidget(self.centralwidget)
        self.serverlist.setObjectName("serverlist")
        self.horizontalLayout_2.addWidget(self.serverlist)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 4, 1, 3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.locallist = QtWidgets.QListWidget(self.centralwidget)
        self.locallist.setObjectName("locallist")
        self.horizontalLayout.addWidget(self.locallist)
        self.reloadbutton = QtWidgets.QPushButton(self.centralwidget)
        self.reloadbutton.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("GuiFTP/strelka.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reloadbutton.setIcon(icon)
        self.reloadbutton.setObjectName("reloadbutton")
        self.horizontalLayout.addWidget(self.reloadbutton)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 4)
        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("imgs/strelka right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_button.setIcon(icon1)
        self.next_button.setObjectName("next_button")
        self.gridLayout.addWidget(self.next_button, 2, 6, 1, 1)
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("imgs/download_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_button.setIcon(icon2)
        self.save_button.setObjectName("save_button")
        self.gridLayout.addWidget(self.save_button, 1, 2, 1, 1)
        self.ftpbutton = QtWidgets.QPushButton(self.centralwidget)
        self.ftpbutton.setObjectName("ftpbutton")
        self.gridLayout.addWidget(self.ftpbutton, 1, 5, 1, 2)
        self.openfolder_button = QtWidgets.QPushButton(self.centralwidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("imgs/folder_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openfolder_button.setIcon(icon3)
        self.openfolder_button.setObjectName("openfolder_button")
        self.gridLayout.addWidget(self.openfolder_button, 1, 3, 1, 2)
        self.home_button = QtWidgets.QPushButton(self.centralwidget)
        self.home_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("imgs/house.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_button.setIcon(icon4)
        self.home_button.setObjectName("home_button")
        self.gridLayout.addWidget(self.home_button, 2, 5, 1, 1)
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("imgs/strelka left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_button.setIcon(icon5)
        self.back_button.setObjectName("back_button")
        self.gridLayout.addWidget(self.back_button, 2, 4, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 805, 26))
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
        self.about_button.setText(_translate("MainWindow", "Про нас"))
        self.option_button.setText(_translate("MainWindow", "Настройки"))
        self.reloadbutton.setText(_translate("MainWindow", "Обновить"))
        self.save_button.setText(_translate("MainWindow", "Сохранить файл"))
        self.ftpbutton.setText(_translate("MainWindow", "Соединить"))
        self.openfolder_button.setText(_translate("MainWindow", "Открыть папку"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
