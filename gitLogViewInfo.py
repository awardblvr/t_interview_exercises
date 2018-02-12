# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gitLogViewInfo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

# class SubDialog(QtGui.QDialog, Ui_MyDialog): 
class Ui_Dialog(QtGui.QDialog, Ui_MyDialog): 
    def __init__(self, some_list, parent=None): 
        QtGui.QDialog.__init__(self, parent) 
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        # self.tableCo.setColumnCount(len(some_list))           
        # self.tableCo.setHorizontalHeaderLabels(some_list)

#class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(755, 556)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 751, 541))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.labelDate = QtWidgets.QLabel(self.frame)
        self.labelDate.setGeometry(QtCore.QRect(20, 21, 81, 16))
        self.labelDate.setMidLineWidth(4)
        self.labelDate.setObjectName("labelDate")
        self.lineEditDate = QtWidgets.QLineEdit(self.frame)
        self.lineEditDate.setGeometry(QtCore.QRect(110, 20, 241, 21))
        self.lineEditDate.setReadOnly(True)
        self.lineEditDate.setObjectName("lineEditDate")
        self.labelSHA1 = QtWidgets.QLabel(self.frame)
        self.labelSHA1.setGeometry(QtCore.QRect(360, 20, 41, 16))
        self.labelSHA1.setObjectName("labelSHA1")
        self.lineEditSHA1 = QtWidgets.QLineEdit(self.frame)
        self.lineEditSHA1.setGeometry(QtCore.QRect(400, 20, 341, 21))
        self.lineEditSHA1.setReadOnly(True)
        self.lineEditSHA1.setObjectName("lineEditSHA1")
        self.plainTextEditComment = QtWidgets.QPlainTextEdit(self.frame)
        self.plainTextEditComment.setGeometry(QtCore.QRect(10, 110, 721, 351))
        self.plainTextEditComment.setReadOnly(True)
        self.plainTextEditComment.setObjectName("plainTextEditComment")
        self.labelAuthor = QtWidgets.QLabel(self.frame)
        self.labelAuthor.setGeometry(QtCore.QRect(50, 60, 41, 16))
        self.labelAuthor.setObjectName("labelAuthor")
        self.lineEditAuthor = QtWidgets.QLineEdit(self.frame)
        self.lineEditAuthor.setGeometry(QtCore.QRect(110, 60, 241, 21))
        self.lineEditAuthor.setReadOnly(True)
        self.lineEditAuthor.setObjectName("lineEditAuthor")
        self.pushButtonDone = QtWidgets.QPushButton(self.frame)
        self.pushButtonDone.setGeometry(QtCore.QRect(310, 490, 113, 32))
        self.pushButtonDone.setStyleSheet("font: 18pt \".SF NS Text\";")
        self.pushButtonDone.setObjectName("pushButtonDone")

        # self.setAttribute(QtGui.Qt.WA_DeleteOnClose)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelDate.setText(_translate("Dialog", "Commit Date"))
        self.labelSHA1.setText(_translate("Dialog", "SHA1"))
        self.labelAuthor.setText(_translate("Dialog", "Author"))
        self.pushButtonDone.setText(_translate("Dialog", "Done"))
        # self.pushButtonDone.clicked.connect(self.accept)
        self.pushButtonDone.clicked.connect(self.allDone)
        # self.pushButtonDone.clicked.connect(self.close)
        print("leaving gLVInfo.retrans...()")

    def allDone(self):
        self.accept() 



"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
"""

