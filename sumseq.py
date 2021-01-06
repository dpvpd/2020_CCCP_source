# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import re

def pow(a,b):
    r=1
    for i in range(0,b):
        r*=a
    return r


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(282, 213)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 180, 221, 20))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 131, 16))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(20, 40, 241, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 81, 16))
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(100, 80, 71, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(180, 90, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 160, 241, 21))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 120, 241, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.calc)
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(150, 20, 51, 16))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(210, 20, 51, 16))
        self.radioButton_2.setObjectName("radioButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "수열의 합 계산기"))
        self.label_2.setText(_translate("Dialog", "contact us : epi00nephrine@gmail.com"))
        self.label.setText(_translate("Dialog", "일반항 a[n]="))
        self.label_3.setText(_translate("Dialog", "첫째 항 부터"))
        self.label_4.setText(_translate("Dialog", "째 항까지의 합"))
        self.label_5.setText(_translate("Dialog", "결과값"))
        self.pushButton.setText(_translate("Dialog", "계                   산"))
        self.radioButton.setText(_translate("Dialog", "등차"))
        self.radioButton_2.setText(_translate("Dialog", "등비"))

    def calc(self,Dialog):
        _translate = QtCore.QCoreApplication.translate
        txt=self.textEdit.toPlainText()
        nums=re.findall("\d+",txt)
        a=0
        d=0
        r=0
        n=0
        l=0
        if self.radioButton.isChecked():
            d=int(nums[1])
            a=int(nums[0])+d
            n=int(self.textEdit_2.toPlainText())
            l=a+(d*(n-1))
            self.label_5.setText(_translate("Dialog", "결과값 : "+str(n*(a+l)/2)))
            

        elif self.radioButton_2.isChecked():
            #a * r ^ (n -1)
            a=int(nums[0])
            r=int(nums[1])
            n=int(self.textEdit_2.toPlainText())
            if r==1:
                self.label_5.setText(_translate("Dialog","결과값 : "+str(n*a)))
            else:
                self.label_5.setText(_translate("Dialog", "결과값 : "+str((a*(pow(r,n)-1)/(r-1)))))
            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())