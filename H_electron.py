# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

R=0.01097773

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(517, 150)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 16))
        self.label.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(130, 20, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 101, 16))
        self.label_2.setObjectName("label_2")
        self.spinBox_2 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_2.setGeometry(QtCore.QRect(130, 50, 42, 22))
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(210, 20, 141, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(210, 40, 141, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(210, 70, 141, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(210, 90, 141, 16))
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 80, 151, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.calc)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(360, 20, 56, 12))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(360, 40, 71, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(440, 40, 56, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(360, 70, 61, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(360, 90, 61, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(20, 120, 221, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(290, 120, 211, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(440, 20, 56, 12))
        self.label_14.setObjectName("label_14")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "수소의 전자 전이 계산기"))
        self.label.setText(_translate("Dialog", "전이 전 주양자수 : "))
        self.label_2.setText(_translate("Dialog", "전이 후 주양자수 : "))
        self.label_3.setText(_translate("Dialog", "방출되는 에너지(kJ/mol)"))
        #self.label_4.setText(_translate("Dialog", "kjpmol"))
        self.label_5.setText(_translate("Dialog", "방출되는 에너지(eV)"))
        #self.label_6.setText(_translate("Dialog", "eV"))
        self.pushButton.setText(_translate("Dialog", "계       산"))
        self.label_7.setText(_translate("Dialog", "계열"))
        #self.label_8.setText(_translate("Dialog", "라이먼 계열"))
        #self.label_9.setText(_translate("Dialog", "자외선"))
        self.label_10.setText(_translate("Dialog", "파장(nm)"))
        #self.label_11.setText(_translate("Dialog", "nm"))
        self.label_12.setText(_translate("Dialog", "contact us : epi00nephrine@gmail.com"))
        self.label_13.setText(_translate("Dialog", "also visit : epi00nephrine.tistory.com"))


    def calc(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        n1=self.spinBox.value()
        n2=self.spinBox_2.value()
        
        if n1>n2 and n2<=3:
            kjpm=(0-((1312)/(n1*n1)))-(0-((1312)/(n2*n2)))
            eV=(0-((13.6)/(n1*n1)))-(0-((13.6)/(n2*n2)))
            lam=1/(R*((1/(n2*n2))-(1/(n1*n1))))
            self.label_11.setText(_translate("Dialog", str(lam)))
            self.label_4.setText(_translate("Dialog", str(kjpm)))
            self.label_6.setText(_translate("Dialog", str(eV)))
            if n2==1:
                self.label_8.setText(_translate("Dialog", "라이먼 계열"))
                self.label_9.setText(_translate("Dialog", "자외선"))
                self.label_14.setText(_translate("Dialog", " "))
            elif n2==2:
                self.label_8.setText(_translate("Dialog", "발머 계열"))
                self.label_9.setText(_translate("Dialog", "가시광선"))
                if lam>=379 and lam<450:
                    self.label_14.setText(_translate("Dialog", "보라색"))
                elif lam>=450 and lam<495:
                    self.label_14.setText(_translate("Dialog", "파랑색"))
                elif lam>=459 and lam<570:
                    self.label_14.setText(_translate("Dialog", "초록색"))
                elif lam>=570 and lam<590:
                    self.label_14.setText(_translate("Dialog", "노랑색"))
                elif lam>=590 and lam<630:
                    self.label_14.setText(_translate("Dialog", "주황색"))
                elif lam>=630 and lam<751:
                    self.label_14.setText(_translate("Dialog", "빨강색"))
            elif n2==3:
                self.label_8.setText(_translate("Dialog", "파셴 계열"))
                self.label_9.setText(_translate("Dialog", "적외선"))
                self.label_14.setText(_translate("Dialog", " "))
        elif n1>n2:
            kjpm=(0-((1312)/(n1*n1)))-(0-((1312)/(n2*n2)))
            eV=(0-((13.6)/(n1*n1)))-(0-((13.6)/(n2*n2)))
            lam=1/(R*((1/(n2*n2))-(1/(n1*n1))))
            self.label_11.setText(_translate("Dialog", str(lam)))
            self.label_4.setText(_translate("Dialog", str(kjpm)))
            self.label_6.setText(_translate("Dialog", str(eV)))
            self.label_8.setText(_translate("Dialog", "N/A"))
            self.label_9.setText(_translate("Dialog", "N/A"))

        elif n1==n2:
            kjpm=0-((1312)/(n1*n1))
            eV=0-((13.6)/(n1*n1))
            self.label_4.setText(_translate("Dialog", str(kjpm)))
            self.label_6.setText(_translate("Dialog", str(eV)))
            self.label_8.setText(_translate("Dialog", "N/A"))
            self.label_9.setText(_translate("Dialog", "N/A"))
            self.label_11.setText(_translate("Dialog", "N/A"))

        else:
            #self.label_11.setText(_translate("Dialog", "N/A"))
            self.label_8.setText(_translate("Dialog", "N/A"))
            self.label_9.setText(_translate("Dialog", "N/A"))
            self.label_6.setText(_translate("Dialog", "N/A"))
            self.label_4.setText(_translate("Dialog", "N/A"))
            self.label_11.setText(_translate("Dialog", "N/A"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
