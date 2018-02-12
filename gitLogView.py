# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gitLogView.ui'
#
# Andrew Ward - for T
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


import os
import sys
import time
import datetime
import dateparser
from dateparser import parse as date_parse
from PyQt5 import QtCore, QtGui, QtWidgets
from pygit2 import Repository
from pygit2 import GIT_SORT_TOPOLOGICAL, GIT_SORT_REVERSE
from PyQt5.QtGui import QStandardItemModel 
from gitLogViewInfo2 import Ui_Dialog as gitLogInfoDialog
import re

# os.environ['PAGER'] = 'cat'
# os.chdir("/Users/award/Source/Photon/Particle-NeoPixel")

class Ui_GitLogViewer(object):
    DATE, AUTHOR, MESSAGE, SHA1 = range(4)

    def setupUi(self, GitLogViewer):
        GitLogViewer.setObjectName("GitLogViewer")
        GitLogViewer.resize(1056, 726)
        self.labelDir = QtWidgets.QLabel(GitLogViewer)
        self.labelDir.setGeometry(QtCore.QRect(30, 30, 60, 16))
        self.labelDir.setOpenExternalLinks(True)
        self.labelDir.setObjectName("labelDir")

        self.lableSearch = QtWidgets.QLabel(GitLogViewer)
        self.lableSearch.setGeometry(QtCore.QRect(10, 70, 91, 16))
        self.lableSearch.setOpenExternalLinks(True)
        self.lableSearch.setObjectName("lableSearch")

        self.searchParam = QtWidgets.QLineEdit(GitLogViewer)
        self.searchParam.setGeometry(QtCore.QRect(100, 70, 691, 21))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.searchParam.setFont(font)
        self.searchParam.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.searchParam.setAcceptDrops(False)
        self.searchParam.setToolTipDuration(5)
        self.searchParam.setAccessibleDescription("")
        self.searchParam.setText("")
        self.searchParam.setMaxLength(32763)
        self.searchParam.setCursorPosition(0)
        self.searchParam.setClearButtonEnabled(True)
        self.searchParam.setObjectName("searchParam")

        self.treeView = QtWidgets.QTreeView(GitLogViewer)
        self.treeView.setGeometry(QtCore.QRect(20, 130, 1021, 581))
        self.treeView.setToolTip("")
        self.treeView.setAccessibleDescription("")
        self.treeView.setAutoExpandDelay(-2)
        self.treeView.setIndentation(5)
        self.treeView.setObjectName("treeView")
        self.treeView.header().setDefaultSectionSize(107)

        self.layoutWidget = QtWidgets.QWidget(GitLogViewer)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 20, 941, 52))
        self.layoutWidget.setObjectName("layoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.pushButtonViewLog = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonViewLog.setAutoRepeatDelay(302)
        self.pushButtonViewLog.setObjectName("pushButtonViewLog")
        self.gridLayout.addWidget(self.pushButtonViewLog, 0, 2, 1, 1)

        self.pushButtonSelectDir = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonSelectDir.setObjectName("pushButtonSelectDir")
        self.gridLayout.addWidget(self.pushButtonSelectDir, 0, 1, 1, 1)

        self.gitBaseDirectory = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gitBaseDirectory.setFont(font)
        self.gitBaseDirectory.setTabletTracking(True)
        self.gitBaseDirectory.setToolTip("")
        self.gitBaseDirectory.setToolTipDuration(2)
        self.gitBaseDirectory.setStatusTip("")
        self.gitBaseDirectory.setCursorPosition(0)
        self.gitBaseDirectory.setObjectName("gitBaseDirectory")
        self.gridLayout.addWidget(self.gitBaseDirectory, 0, 0, 1, 1)

        self.lableSearchHintText = QtWidgets.QLabel(GitLogViewer)
        self.lableSearchHintText.setGeometry(QtCore.QRect(80, 100, 811, 16))
        self.lableSearchHintText.setToolTipDuration(-2)
        self.lableSearchHintText.setStyleSheet("font: 13pt \"Courier\";")
        self.lableSearchHintText.setMidLineWidth(13)
        self.lableSearchHintText.setTextFormat(QtCore.Qt.AutoText)
        self.lableSearchHintText.setObjectName("lableSearchHintText")
        self.lableSearchHint = QtWidgets.QLabel(GitLogViewer)
        self.lableSearchHint.setGeometry(QtCore.QRect(20, 100, 60, 16))
        self.lableSearchHint.setObjectName("lableSearchHint")

        self.retranslateUi(GitLogViewer)
        QtCore.QMetaObject.connectSlotsByName(GitLogViewer)

    def retranslateUi(self, GitLogViewer):
        _translate = QtCore.QCoreApplication.translate
        GitLogViewer.setWindowTitle(_translate("GitLogViewer", "Form"))
        GitLogViewer.setAccessibleName(_translate("GitLogViewer", "glv"))
        self.labelDir.setText(_translate("GitLogViewer", "Directory:"))
        self.lableSearch.setText(_translate("GitLogViewer", "Search param:"))
        self.searchParam.setToolTip(_translate("GitLogViewer", "search field tool tip"))
        self.searchParam.setPlaceholderText(_translate("GitLogViewer", "enter optional search term (see below)"))
        self.treeView.setWhatsThis(_translate("GitLogViewer", "This is the thing Tesla wants"))
        self.pushButtonViewLog.setText(_translate("GitLogViewer", "View Log"))
        self.pushButtonSelectDir.setText(_translate("GitLogViewer", "Select Directory"))
        self.gitBaseDirectory.setPlaceholderText(_translate("GitLogViewer", "Enter path or click \"Select Directory\" for git base directory"))
        self.lableSearchHintText.setText(_translate("GitLogViewer", "<html><head/><body><p>[&lt;<span style=\" font-style:italic;\">sha</span>&gt;] | [<span style=\" font-weight:600;\">&quot;</span><span style=\" font-style:italic;\">comment search partial text</span><span style=\" font-weight:600;\">&quot;</span>] | [ &lt;<span style=\" font-weight:600;\">before</span> | <span style=\" font-weight:600;\">on</span> | <span style=\" font-weight:600;\">since</span>&gt; &lt;<span style=\" font-style:italic;\">exact</span> | <span style=\" font-style:italic;\">fuzzy date specification</span>&gt;]  </p></body></html>"))
        self.lableSearchHint.setText(_translate("GitLogViewer", "Search:"))
        self.pushButtonSelectDir.clicked.connect(self.dir_sel_clicked)
        self.pushButtonViewLog.clicked.connect(self.viewIt)
        self.dirName =os.getcwd()
        self.gitBaseDirectory.setText(self.dirName)
        self.treeView.clicked.connect(self.cellClick)
        #self.gitBaseDirectory.clicked.connect(self.dir_field_clicked)
        self.gitBaseDirectory.textChanged.connect(self.dir_field_changed)

    def dir_sel_clicked(self):
        self.dirName = QtWidgets.QFileDialog.getExistingDirectory(GitLogViewer,
                      "Open Directory", self.dirName)

        print("newish self.dirName is <%s>" % (self.dirName))
        self.gitBaseDirectory.setText(self.dirName)

    def dir_field_changed(self):
        self.dirName = self.gitBaseDirectory.text().strip()

            
    def viewIt(self):
        gitSearchComment = None
        gitSearchDate = None
        gitSearchDateType = None
        gitSearchSha1 = None

        os.chdir(self.dirName)

        searchReq = self.searchParam.text()
        # See if user is requesting a search param
        while len(searchReq):
            # Look for quoted string (indicating text in comment to search for)
            searchComment = re.match(r"^\"(.*)\"$", searchReq)
            if searchComment:
                gitSearchComment = searchComment.group(1)
                # print('comment search for <{}>'.format(searchComment.group(1)))
                break

            # Look for keywords indicating a date 'on', 'before', 'since' 
            searchDate = re.search(r"^(on|before|since|after)\s*(.*)", searchReq, re.IGNORECASE)
            if searchDate:
                gitSearchDateType = searchDate.group(1).lower()
                gitSearchDate = searchDate.group(2)
                searchDatePoint = date_parse(gitSearchDate)
                # print('date search [{}] is <{}>'.format(gitSearchDateType, gitSearchDate))
                # print('searchDatePoint is {}'.format(searchDatePoint))
                break

            # Look for something resembling a SHA
            if len(searchReq) == 40:
                gitSearchSha1 = searchReq
                break

            # User did not enter a proper search... Tell them
            self.showBadSearchMsgWin()
            return
        
        try:
            repo = Repository('.git')
        except:
            self.showBadGitDirMsgWin()
            return

        try:
            self.model.clear() 
        except AttributeError:
            pass
            
        self.treeView.setRootIsDecorated(False)
        self.model = self.createGLmodel(None)
        self.treeView.setModel(self.model)
        self.treeView.hideColumn(3)

        """
        members of items from repo.walk are:

           'author',
           'commit_time',
           'commit_time_offset',
           'committer',
           'hex',
           'id',
           'message',
           'message_encoding',
           'oid',
           'parent_ids',
           'parents',
           'peel',
           'raw_message',
           'read_raw',
           'tree',
           'tree_id',
           'type'
        """
        for idx, commit in enumerate(repo.walk(repo.head.target, GIT_SORT_TOPOLOGICAL)):
            if gitSearchComment:
                if re.search(gitSearchComment, commit.message):
                    self.addCommit(self.model, commit)
            elif gitSearchDateType:
                if gitSearchDateType in ['since', 'after']:
                    if datetime.datetime.fromtimestamp(int(commit.commit_time)) > searchDatePoint:  
                        self.addCommit(self.model, commit)
                elif gitSearchDateType == 'before':
                    if datetime.datetime.fromtimestamp(int(commit.commit_time)) < searchDatePoint:  
                        self.addCommit(self.model, commit)
                elif gitSearchDateType == 'on':
                    commitDay_str = datetime.datetime.fromtimestamp(int(commit.commit_time)).strftime('%Y-%m-%d')
                    # commitDay = strptime(commitDay_str, '%Y-%m-%d')
                    commitDay = datetime.datetime(*(time.strptime(commitDay_str, '%Y-%m-%d')[0:6]))
                    if commitDay == searchDatePoint:  
                        self.addCommit(self.model, commit)

                    # A less elegant solution would involve manipulating the string directly.

                    # testeddate = '4/25/2015'
                    # month, day, year = testeddate.split('/')
                    # testeddate = '-'.join([year, month, day]) + ' 00:00:00'

            elif gitSearchSha1:
                if gitSearchSha1 == str(commit.oid):
                    self.addCommit(self.model, commit)
            else:
                self.addCommit(self.model, commit)

        self.treeView.resizeColumnToContents(0)
        

    def createGLmodel(self, parent):
        model = QStandardItemModel(0, 4, parent)
        model.setHeaderData(self.DATE, QtCore.Qt.Horizontal, "Commit Date")
        model.setHeaderData(self.AUTHOR, QtCore.Qt.Horizontal, "Author")
        model.setHeaderData(self.MESSAGE, QtCore.Qt.Horizontal, "Message")
        return model



    def addCommit(self, model, commit):
        model.insertRow(0)
        model.setData(model.index(0, self.DATE), 
                     datetime.datetime.fromtimestamp(int(commit.commit_time)).strftime('%Y-%m-%d %H:%M:%S'))
        model.setData(model.index(0, self.AUTHOR), 
                     commit.author.name)
        model.setData(model.index(0, self.MESSAGE), 
                     commit.message.strip().replace('\n\n', '\n').replace('\n', ' '))
        model.setData(model.index(0, self.SHA1), 
                     commit.oid)
 

    def cellClick(self, itm_idx):
        # print("cellClick itm_tdx row(): %r" % (itm_idx.row()))

        displayable_info = {'sha1': str(itm_idx.sibling(itm_idx.row(), self.SHA1).data()),
                            'date':     itm_idx.sibling(itm_idx.row(), self.DATE).data(),
                            'comment':  itm_idx.sibling(itm_idx.row(), self.MESSAGE).data(), 
                            'author':   itm_idx.sibling(itm_idx.row(), self.AUTHOR).data()}

        self.open_info_dialog(displayable_info)

    def showBadSearchMsgWin(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Mistaken Search Syntax")
        msg.setInformativeText("You have made the silly mistake of not using proper search syntax")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.buttonClicked.connect(self.msgbtn)
        msg.exec_()

            
    def showBadGitDirMsgWin(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Invalid git repo base dir")
        msg.setInformativeText("You gotta find the base directory where a git repo is stored. "
                               "(Hint... Those directories have a '.git' file.)")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.buttonClicked.connect(self.msgbtn)
        msg.exec_()

            
    def msgbtn(self, i):
        #print("Button pressed is: %s " % (i.text()))
        pass
            
     
    def showdialog(self, user_info):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)

        msg.setText("Details from commit:")
        msg.setInformativeText(user_info)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.buttonClicked.connect(self.msgbtn)
             
        retval = msg.exec_()
        # print("value of pressed message box button: %r"% (retval))
            


    def open_info_dialog(self, displayable_info):
        dialog = gitLogInfoDialog(displayable_info)
        dialog.exec_()

            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GitLogViewer = QtWidgets.QWidget()
    ui = Ui_GitLogViewer()
    ui.setupUi(GitLogViewer)
    GitLogViewer.show()
    sys.exit(app.exec_())

