# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(296, 255)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 231, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 56, 12))
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(60, 80, 71, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(150, 90, 56, 12))
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(180, 80, 71, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 130, 56, 12))
        self.label_4.setObjectName("label_4")
        self.textEdit_3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(60, 120, 71, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(150, 130, 56, 12))
        self.label_5.setObjectName("label_5")
        self.textEdit_4 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_4.setGeometry(QtCore.QRect(180, 120, 71, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 170, 261, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.showsine)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 230, 221, 16))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "사인 그래프 그리기"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt;\">y = a sin( bx + c ) + d</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "a ="))
        self.textEdit.setHtml(_translate("Dialog", "1"))
        self.label_3.setText(_translate("Dialog", "b ="))
        self.textEdit_2.setHtml(_translate("Dialog", "1"))
        self.label_4.setText(_translate("Dialog", "c ="))
        self.textEdit_3.setHtml(_translate("Dialog", "0"))
        self.label_5.setText(_translate("Dialog", "d ="))
        self.textEdit_4.setHtml(_translate("Dialog", "0"))
        self.pushButton.setText(_translate("Dialog", "그래프 그리기"))
        self.label_6.setText(_translate("Dialog", "contact us : epi00nephrine@gmail.com"))

    def showsine(self):
        a=int(self.textEdit.toPlainText())
        b=int(self.textEdit_2.toPlainText())
        c=int(self.textEdit_3.toPlainText())
        d=int(self.textEdit_4.toPlainText())
        x = np.arange(0, 4*np.pi, 0.0001)
        y = a*np.sin(b*x+c)+d
        plt.plot(x, y)
        plt.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
