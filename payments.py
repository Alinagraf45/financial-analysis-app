# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'payments.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Payments(object):
    def setupUi(self, Payments):
        Payments.setObjectName("Payments")
        Payments.resize(734, 550)
        Payments.setStyleSheet("background-color: #EC933B    ")
        self.label = QtWidgets.QLabel(Payments)
        self.label.setGeometry(QtCore.QRect(290, 40, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #FFFFFF")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Payments)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 470, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: #FFFFFF;\n"
"color: #5C2E00")
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(Payments)
        self.comboBox.setGeometry(QtCore.QRect(400, 160, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("color: #5C2E00")
        self.comboBox.setObjectName("comboBox")
        self.textEdit = QtWidgets.QTextEdit(Payments)
        self.textEdit.setGeometry(QtCore.QRect(90, 140, 241, 61))
        self.textEdit.setStyleSheet("background-color: #FFFFFF;\n"
"color: #5C2E00")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_3 = QtWidgets.QTextEdit(Payments)
        self.textEdit_3.setGeometry(QtCore.QRect(90, 350, 241, 41))
        self.textEdit_3.setStyleSheet("background-color: #FFFFFF;\n"
"color: #5C2E00")
        self.textEdit_3.setObjectName("textEdit_3")
        self.dateEdit = QtWidgets.QDateEdit(Payments)
        self.dateEdit.setGeometry(QtCore.QRect(400, 350, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Payments)
        self.textEdit_2.setGeometry(QtCore.QRect(90, 260, 241, 41))
        self.textEdit_2.setStyleSheet("background-color: #FFFFFF;\n"
"color: #5C2E00")
        self.textEdit_2.setObjectName("textEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(Payments)
        self.lineEdit.setGeometry(QtCore.QRect(400, 260, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: #5C2E00")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_3 = QtWidgets.QPushButton(Payments)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 470, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: #FFFFFF;\n"
"color: #5C2E00")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Payments)
        QtCore.QMetaObject.connectSlotsByName(Payments)

    def retranslateUi(self, Payments):
        _translate = QtCore.QCoreApplication.translate
        Payments.setWindowTitle(_translate("Payments", "Form"))
        self.label.setText(_translate("Payments", "Расходы"))
        self.pushButton_2.setText(_translate("Payments", "Сохранить"))
        self.textEdit.setHtml(_translate("Payments", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Выберите сферу расходов для внесения платежа:</span></p></body></html>"))
        self.textEdit_3.setHtml(_translate("Payments", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Выберите дату:</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("Payments", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Внесите сумму платежа:</span></p></body></html>"))
        self.pushButton_3.setText(_translate("Payments", "Меню"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Payments = QtWidgets.QWidget()
    ui = Ui_Payments()
    ui.setupUi(Payments)
    Payments.show()
    sys.exit(app.exec_())