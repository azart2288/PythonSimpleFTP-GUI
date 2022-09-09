from PyQt5 import QtCore, QtGui, QtWidgets
import ru_options
import options
from main import ExampleApp
from ru_main import ExampleApp_RU
#from main_ru_options import main_ru_options






class Options(QtWidgets.QMainWindow, options.Ui_MainWindow , ru_options.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Ru_lang.toggled.connect(self.russian)
        


    def russian(self):
        self.toggle = self.Ru_lang.text()
        self.example = ExampleApp()
        self.ru_example = ExampleApp_RU()
        self.r1 = Ru_options()
        self.r1.show()
        self.close()

    def toggled(self):
        return Lang_Options
        


class Ru_options(QtWidgets.QMainWindow , ru_options.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.English_lang.toggled.connect(self.english)

    def english(self):
        self.p1 = Options()
        self.p1.show()
        self.close()





