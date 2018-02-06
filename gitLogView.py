# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gitLogView.ui'
#
# Andrew Ward - for T
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import os
import sys
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from pygit2 import Repository
from pygit2 import GIT_SORT_TOPOLOGICAL, GIT_SORT_REVERSE
from PyQt5.QtGui import QStandardItemModel
import datetime

os.environ['PAGER'] = 'cat'
# os.chdir("/Users/award/Source/Photon/Particle-NeoPixel")


class Ui_GitLogViewer(object):
    DATE, AUTHOR, MESSAGE = range(3)

    def setupUi(self, GitLogViewer):
        GitLogViewer.setObjectName("GitLogViewer")
        GitLogViewer.resize(1056, 726)
        self.label = QtWidgets.QLabel(GitLogViewer)
        self.label.setGeometry(QtCore.QRect(30, 30, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(GitLogViewer)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 151, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(GitLogViewer)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 70, 641, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.treeView = QtWidgets.QTreeView(GitLogViewer)
        self.treeView.setGeometry(QtCore.QRect(20, 110, 1021, 601))
        self.treeView.setObjectName("treeView")

        self.widget = QtWidgets.QWidget(GitLogViewer)
        self.widget.setGeometry(QtCore.QRect(100, 20, 941, 52))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.dirName =os.getcwd()
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText(self.dirName)
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.retranslateUi(GitLogViewer)
        QtCore.QMetaObject.connectSlotsByName(GitLogViewer)

    def retranslateUi(self, GitLogViewer):
        _translate = QtCore.QCoreApplication.translate
        GitLogViewer.setWindowTitle(_translate("GitLogViewer", "Form"))
        GitLogViewer.setAccessibleName(_translate("GitLogViewer", "glv"))
        self.label.setText(_translate("GitLogViewer", "Directory:"))
        self.label_2.setText(_translate("GitLogViewer", "Search param (optional)"))
        self.pushButton_2.setText(_translate("GitLogViewer", "View Log"))
        self.pushButton.setText(_translate("GitLogViewer", "Select Directory"))
        self.pushButton.clicked.connect(self.dir_sel_clicked)
        self.pushButton_2.clicked.connect(self.viewIt)

    def dir_sel_clicked(self):
        self.dirName = QtWidgets.QFileDialog.getExistingDirectory(GitLogViewer,
                      "Open Directory", self.dirName)

        self.lineEdit.setText(self.dirName)
            
    def viewIt(self):
        os.chdir(self.dirName)

        repo = Repository('.git')

        self.treeView.setRootIsDecorated(False)
        self.model = self.createGLmodel(None)
        self.treeView.setModel(self.model)

        for idx, commit in enumerate(repo.walk(repo.head.target, GIT_SORT_TOPOLOGICAL)):
            self.addCommit(self.model, 
                           datetime.datetime.fromtimestamp(int(commit.commit_time)).strftime('%Y-%m-%d %H:%M:%S'),
                           commit.author.name,
                           commit.message.strip().replace('\n\n', '\n').replace('\n', ' '))

        self.treeView.clicked.connect(self.cellClick)
        

    def createGLmodel(self, parent):
        model = QStandardItemModel(0, 3, parent)
        model.setHeaderData(self.DATE, QtCore.Qt.Horizontal, "Commit Date")
        model.setHeaderData(self.AUTHOR, QtCore.Qt.Horizontal, "Author")
        model.setHeaderData(self.MESSAGE, QtCore.Qt.Horizontal, "Message")
        return model



    def addCommit(self, model, date, auth, msg):
        model.insertRow(0)
        model.setData(model.index(0, self.DATE), date)
        model.setData(model.index(0, self.AUTHOR), auth)
        model.setData(model.index(0, self.MESSAGE), msg)
 
    def cellClick(self, itm_idx):
        parent = self.model.itemFromIndex(itm_idx)
        # print("Row %r,   Column %r" % (parent.row(), parent.column()))
        msg_str = str(parent.data(role=QtCore.Qt.DisplayRole))
        self.showdialog(msg_str) 

     
    def showdialog(self, user_info):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)

        msg.setText("Details from commit:")
        msg.setInformativeText(user_info)
        # msg.setWindowTitle("Details...")
        # msg.setDetailedText("The details are as follows:")
        # msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.buttonClicked.connect(self.msgbtn)
             
        retval = msg.exec_()
        # print("value of pressed message box button: %r"% (retval))
            
    def msgbtn(self, i):
        print("Button pressed is: %s " % (i.text()))
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GitLogViewer = QtWidgets.QWidget()
    ui = Ui_GitLogViewer()
    ui.setupUi(GitLogViewer)
    GitLogViewer.show()
    sys.exit(app.exec_())

