from PyQt5 import QtCore, QtGui, QtWidgets
from db_2 import *


class CheckThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def thr_login(self, name, password):
        login(name, password, self.mysignal)

    def thr_register(self, name, password):
        register(name, password, self.mysignal)