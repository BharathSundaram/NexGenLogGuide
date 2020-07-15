# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NextGenLogGuide.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog, QAction
from PyQt5.QtGui import QIcon
from utils import *

__author__ = "Bharath Shanmugasundaram"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "bharath.inmail@gmail.com"
__status__ = "Production"

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        width,height = get_screen_resolution()
        MainWindow.resize(width-5, int(height - (height*(15/100))))# 90 % of screen height
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setObjectName("treeWidget")
        #self.treeWidget.headerItem().setText(0, "1")
        self.verticalLayout.addWidget(self.treeWidget)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 807, 21))
        self.menubar.setObjectName("menubar")
        self.menuOpenfile = QtWidgets.QMenu(self.menubar)
        self.menuOpenfile.setObjectName("menuOpenfile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpenFile = QtWidgets.QAction(MainWindow)
        self.actionOpenFile.setObjectName("actionOpenFile")
        self.actionOpenFolder = QtWidgets.QAction(MainWindow)
        self.actionOpenFolder.setObjectName("actionOpenFolder")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuOpenfile.addAction(self.actionOpenFile)
        self.menuOpenfile.addAction(self.actionOpenFolder)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuOpenfile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", str ( 'NexGenLogGuide ' +'-' + __version__)))
        self.label.setText(_translate("MainWindow", "List of files"))
        self.label_2.setText(_translate("MainWindow", "Initial log information"))
        self.pushButton.setText(_translate("MainWindow", "Open File"))
        self.pushButton_2.setText(_translate("MainWindow", "Open Folder"))
        self.menuOpenfile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpenFile.setText(_translate("MainWindow", "OpenFile"))
        self.actionOpenFolder.setText(_translate("MainWindow", "OpenFolder"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        # Till this it was generated by pyuic5.exe

        scriptDir = os.path.dirname(os.path.realpath(__file__))
        MainWindow.setWindowIcon(QIcon(scriptDir + os.path.sep + 'res' + os.path.sep + 'index.png'))
        MainWindow.statusBar().showMessage('Ready')
        self.actionOpenFile.setToolTip('Open NexGen Log File for parsing')
        self.actionOpenFolder.setToolTip('Open folder contains Log File(s) for parsing')
        self.pushButton.setToolTip('Open NexGen Log File for parsing')
        self.menuOpenfile.setToolTipsVisible(True)
        self.pushButton_2.setToolTip('Open folder contains Log File(s) for parsing')

        self.treeWidget.setColumnCount(2)
        self.treeWidget.setHeaderLabels(["File Name", "Size"])
        twidth = self.treeWidget.sizeHint().width() - int((self.treeWidget.sizeHint().width() / 3))
        self.treeWidget.header().resizeSection(0,twidth)
        self.treeWidget.header().setStretchLastSection(False)
        self.treeWidget.header().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

    def OpenFileDialog(self):
        file_name = QFileDialog.getOpenFileName(None, 'Open NextGen Log files',
                                    'c:\\', "NextGen Log files (*.log)")
    def OpenFolderDialog(self):
        folder_name = str(QFileDialog.getExistingDirectory(None, "Select Directory"))

    def add_signals(self):
        self.pushButton.clicked.connect(self.OpenFileDialog)
        self.pushButton_2.clicked.connect(self.OpenFolderDialog)
        self.actionOpenFile.triggered.connect(self.OpenFileDialog)
        self.actionOpenFolder.triggered.connect(self.OpenFolderDialog)


