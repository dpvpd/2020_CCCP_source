# -*- coding: utf-8 -*-

import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(271, 222)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 101, 16))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(160, 10, 101, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(160, 50, 101, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 151, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 90, 251, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.calc)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 221, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 190, 221, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 140, 56, 12))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(50, 140, 121, 16))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "pH계산기"))
        self.label.setText(_translate("Dialog", "용액의 부피(㎖) : "))
        self.label_2.setText(_translate("Dialog", "하이드로늄이온의 수(몰) : "))
        self.pushButton.setText(_translate("Dialog", "계        산"))
        self.label_3.setText(_translate("Dialog", "contact us : epi00nephrine@gmail.com"))
        self.label_4.setText(_translate("Dialog", "visit also : epi00nephrine.tistory.com"))
        self.label_5.setText(_translate("Dialog", "pH : "))
        #self.label_6.setText(_translate("Dialog", "계산 결과"))

    def calc(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        mililiter=int(self.textEdit.toPlainText())
        print(mililiter)
        ionmole=int(self.textEdit_2.toPlainText())
        print(ionmole)
        liter=float(mililiter/1000)
        print(liter)
        molarity=ionmole / liter
        print(molarity)
        pH=np.log10(molarity)*(0-1)
        print(pH)
        self.label_6.setText(_translate("Dialog", str(pH)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
