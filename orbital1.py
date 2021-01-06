# -*- coding: utf-8 -*-

import pickle
import re

from PyQt5 import QtCore, QtGui, QtWidgets


#with open('data.dll','wb') as file:
#    pickle.dump(orbital,file)
#    pickle.dump(ptable,file)
#    pickle.dump(elctrn,file)
with open('data\\data.dll','rb') as file:
    orbital=pickle.load(file)
    ptable=pickle.load(file)
    elctrn=pickle.load(file)
   
#ptable=pt
#orbital=orbt

#elctrn = {0:'1s1', 1:'2s2', 2:'[He] 2s1', 3:'[He] 2s2', 4:'[He] 2s2 2p1', 5:'[He] 2s2 2p2', 6:'[He] 2s2 2p3', 7:'[He] 2s2 2p4', 8:'[He] 2s2 2p5',9:'[He] 2s2 2p6',10:'[Ne] 3s1',11:'[Ne] 3s2',12:'[Ne] 3s2 3p1',13:'[Ne] 3s2 3p2',14:'[Ne] 3s2 3p3',15:'[Ne] 3s2 3p4',16:'[Ne] 3s2 3p5',17:'[Ne] 3s2 3p6',18:'[Ar] 4s1',19:'[Ar] 4s2',20:'[Ar] 3d1 4s2',21:'[Ar] 3d2 4s2',22:'[Ar] 3d3 4s2',23:'[Ar] 3d5 4s1',24:'[Ar] 3d5 4s2',25:'[Ar] 3d6 4s2',26:'[Ar] 3d7 4s2',27:'[Ar] 3d8 4s2',28:'[Ar] 3d10 4s1',29:'[Ar] 3d10 4s2',30:'[Ar] 3d10 4s2 4p1',31:'[Ar] 3d10 4s2 4p2',32:'[Ar] 3d10 4s2 4p3',33:'[Ar] 3d10 4s2 4p4',34:'[Ar] 3d10 4s2 4p5',35:'[Ar] 3d10 4s2 4p6',36:'[Kr] 5s1',37:'[Kr] 5s2',38:'[Kr] 4d1 5s2',39:'[Kr] 4d2 5s2',40:'[Kr] 4d4 5s1',41:'[Kr] 4d5 5s1',42:'[Kr] 4d5 5s2',43:'[Kr] 4d7 5s1',44:'[Kr] 4d8 5s1',45:'[Kr] 4d10',46:'[Kr] 4d10 5s1',47:'[Kr] 4d10 5s2',48:'[Kr] 4d10 5s2 5p1',49:'[Kr] 4d10 5s2 5p2',50:'[Kr] 4d10 5s2 5p3',51:'[Kr] 4d10 5s2 5p4',52:'[Kr] 4d10 5s2 5p5',53:'[Kr] 4d10 5s2 5p6',54:'[Xe] 6s1',55:'[Xe] 6s2',56:'[Xe] 5d1 6s2',57:'[Xe] 4f1 5d1 6s2',58:'[Xe] 4f3 6s2',59:'[Xe] 4f4 6s2',60:'[Xe] 4f5 6s2',61:'[Xe] 4f6 6s2',62:'[Xe] 4f7 6s2',63:'[Xe] 4f7 5d1 6s2',64:'[Xe] 4f9 6s2',65:'[Xe] 4f10 5d1 6s2',66:'[Xe] 4f11 6s2',67:'[Xe] 4f12 6s2',68:'[Xe] 4f13 6s2',69:'[Xe] 4f14 6s2',70:'[Xe] 4f14 5d1 6s2',71:'[Xe] 4f14 5d2 6s2',72:'[Xe] 4f14 5d3 6s2',73:'[Xe] 4f14 5d4 6s2',74:'[Xe] 4f14 5d5 6s2',75:'[Xe] 4f14 5d6 6s2',76:'[Xe] 4f14 5d7 6s2',77:'[Xe] 4f14 5d9 6s1',78:'[Xe] 4f14 5d10 6s1',79:'[Xe] 4f14 5d10 6s2',80:'[Xe] 4f14 5d10 6s2 6p1',81:'[Xe] 4f14 5d10 6s2 6p2',82:'[Xe] 4f14 5d10 6s2 6p3',83:'[Xe] 4f14 5d10 6s2 6p4',84:'[Xe] 4f14 5d10 6s2 6p5',85:'[Xe] 4f14 5d10 6s2 6p6',86:'[Rn] 7s1',87:'[Rn] 7s2',88:'[Rn] 6d1 7s2',89:'[Rn] 6d2 7s2',90:'[Rn] 5f2 6d1 7s2',91:'[Rn] 5f3 6d1 7s2',92:'[Rn] 5f4 6d1 7s2',93:'[Rn] 5f6 7s2',94:'[Rn] 5f7 7s2',95:'[Rn] 5f7 6d1 7s2',96:'[Rn] 5f9 7s2',97:'[Rn] 5f10 7s2',98:'[Rn] 5f11 7s2',99:'[Rn] 5f12 7s2',100:'[Rn] 5f13 7s2',101:'[Rn] 5f14 7s2',102:'[Rn] 5f14 6d1 7s2',103:'[Rn] 5f14 6d2 7s2',104:'[Rn] 5f14 6d3 7s2',105:'[Rn] 5f14 6d4 7s2',106:'[Rn] 5f14 6d5 7s2',107:'[Rn] 5f14 6d6 7s2',108:'[Rn] 5f14 6d7 7s2',109:'[Rn] 5f14 6d9 7s1',110:'[Rn] 5f14 6d9 7s2',111:'[Rn] 5f14 6d10 7s2',112:'[Rn] 5f14 6d10 7s2 7p1',113:'[Rn] 5f14 6d10 7s2 7p2',114:'[Rn] 5f14 6d10 7s2 7p3',115:'[Rn] 5f14 6d10 7s2 7p4',116:'[Rn] 5f14 6d10 7s2 7p5',117:'[Rn] 5f14 6d10 7s2 7p6',118:'N/A'}

#with open('data\\data.dll','wt') as file:
#    orbt=pickle.load(file)
#    pt=pickle.load(file)
#with open('data1.dll','wb') as file:
#    pickle.dump(orbital,file)
#    pickle.dump(ptable,file)
#    pickle.dump(elctrn,file)


def orbitaltonum(txt):
    n=re.findall("\d+",txt)
    a=0
    for i in range(0,len(n)):
        if i%2==1:
            a+=int(n[i])
    return a

p=['N/A']
ptable.extend(p)
def nametonum(name):
    for i in range(0,118):
        if name == ptable[i]:
            return i
    return 118

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(669, 400)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(20, 20, 291, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(320, 20, 75, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.calc)
        self.pushButton_1 = QtWidgets.QPushButton(Dialog)
        self.pushButton_1.setGeometry(QtCore.QRect(580, 360, 75, 31))
        self.pushButton_1.setObjectName("pushButton")
        #self.pushButton_1.clicked.connect(self.readme)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(400, 20, 261, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 291, 291))
        self.label_2.setObjectName("label_2")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(20, 70, 90, 16))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(110, 70, 101, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(210, 70, 101, 16))
        self.radioButton_3.setObjectName("radioButton_3")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(330, 90, 91, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(440, 90, 81, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(330, 120, 41, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(440, 120, 41, 21))
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(330, 160, 131, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(330, 190, 321, 21))
        self.label_10.setObjectName("label_10")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.textEdit, self.pushButton)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "오비탈 계산기"))
        self.pushButton.setText(_translate("Dialog", "계산"))
        self.label.setText(_translate("Dialog", "contact us : epi00nephrine@gmail.com"))
        self.radioButton.setText(_translate("Dialog", "오비탈 입력"))
        self.radioButton_2.setText(_translate("Dialog", "원소기호 입력"))
        self.radioButton_3.setText(_translate("Dialog", "원자번호 입력"))
        #pixmap=QtGui.QPixmap("data\\image\\Oganesson.png")
        #pixmap = pixmap.scaledToWidth(291)
        #self.label_2.setPixmap(QtGui.QPixmap(pixmap))
        self.label_3.setText(_translate("Dialog", "원소 기호"))
        self.label_4.setText(_translate("Dialog", "원자 번호"))
        self.label_9.setText(_translate("Dialog", "바닥 상태 전자 배열"))
        #self.label_5.setText(_translate("Dialog", "He"))
        #self.label_6.setText(_translate("Dialog", "2"))
        #self.label_10.setText(_translate("Dialog", "[Rn] 5f14 6d10 7s2 7p6"))

    def calc(self,Dialog):
        _translate = QtCore.QCoreApplication.translate
        i=self.textEdit.toPlainText()
        #self.label_5.setText(_translate("Dialog", i))

        if self.radioButton.isChecked():
            e=orbitaltonum(i)-1
            #self.label_10.setText(_translate("Dialog", i))
            #orbitaltonum(i)
            self.label_5.setText(_translate("Dialog", ptable[e]))
            self.label_6.setText(_translate("Dialog", str(e+1)))
            self.label_10.setText(_translate("Dialog", elctrn[e]))
            pixmap=QtGui.QPixmap("data\\image\\"+ptable[e]+".png")
            pixmap = pixmap.scaledToWidth(291)
            self.label_2.setPixmap(QtGui.QPixmap(pixmap))

        elif self.radioButton_2.isChecked():
            self.label_5.setText(_translate("Dialog", ptable[nametonum(i)]))

            if nametonum(i)==118:
                self.label_6.setText(_translate("Dialog", 'N/A'))

            else:
                self.label_6.setText(_translate("Dialog", str(nametonum(i)+1)))

            self.label_10.setText(_translate("Dialog", elctrn[nametonum(i)]))
            pixmap=QtGui.QPixmap("data\\image\\"+ptable[nametonum(i)]+".png")
            pixmap = pixmap.scaledToWidth(291)
            self.label_2.setPixmap(QtGui.QPixmap(pixmap))

        elif self.radioButton_3.isChecked():
            if int(i)>118 or int(i)<0:
                self.label_5.setText(_translate("Dialog", 'N/A'))
                self.label_6.setText(_translate("Dialog", 'N/A'))
                self.label_10.setText(_translate("Dialog", 'N/A'))

            else:
                self.label_5.setText(_translate("Dialog", ptable[int(i)-1]))
                self.label_6.setText(_translate("Dialog", i))
                self.label_10.setText(_translate("Dialog", elctrn[int(i)-1]))
                pixmap=QtGui.QPixmap("data\\image\\"+ptable[int(i)-1]+".png")
                pixmap = pixmap.scaledToWidth(291)
                self.label_2.setPixmap(QtGui.QPixmap(pixmap))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


