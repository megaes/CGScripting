# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alexey\Documents\GitHub\CGScripting\9. Project Manager\widgets\projectManager.ui'
#
# Created: Thu Aug 24 20:20:38 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_projectManager(object):
    def setupUi(self, projectManager):
        projectManager.setObjectName("projectManager")
        projectManager.resize(800, 593)
        self.centralwidget = QtGui.QWidget(projectManager)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter_2 = QtGui.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.verticalLayoutWidget = QtGui.QWidget(self.splitter_2)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.projectList_ly = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.projectList_ly.setContentsMargins(0, 0, 0, 0)
        self.projectList_ly.setObjectName("projectList_ly")
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.create_btn = QtGui.QPushButton(self.layoutWidget)
        self.create_btn.setObjectName("create_btn")
        self.verticalLayout.addWidget(self.create_btn)
        self.update_btn = QtGui.QPushButton(self.layoutWidget)
        self.update_btn.setObjectName("update_btn")
        self.verticalLayout.addWidget(self.update_btn)
        self.line = QtGui.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backup_btn = QtGui.QPushButton(self.layoutWidget)
        self.backup_btn.setObjectName("backup_btn")
        self.horizontalLayout.addWidget(self.backup_btn)
        self.openBackup_btn = QtGui.QPushButton(self.layoutWidget)
        self.openBackup_btn.setMinimumSize(QtCore.QSize(40, 0))
        self.openBackup_btn.setMaximumSize(QtCore.QSize(40, 16777215))
        self.openBackup_btn.setObjectName("openBackup_btn")
        self.horizontalLayout.addWidget(self.openBackup_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_2 = QtGui.QFrame(self.layoutWidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.archive_btn = QtGui.QPushButton(self.layoutWidget)
        self.archive_btn.setObjectName("archive_btn")
        self.horizontalLayout_2.addWidget(self.archive_btn)
        self.openArchive_btn = QtGui.QPushButton(self.layoutWidget)
        self.openArchive_btn.setMinimumSize(QtCore.QSize(40, 0))
        self.openArchive_btn.setMaximumSize(QtCore.QSize(40, 16777215))
        self.openArchive_btn.setObjectName("openArchive_btn")
        self.horizontalLayout_2.addWidget(self.openArchive_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.templateEditor_btn = QtGui.QPushButton(self.layoutWidget)
        self.templateEditor_btn.setObjectName("templateEditor_btn")
        self.verticalLayout.addWidget(self.templateEditor_btn)
        self.info_gb = QtGui.QGroupBox(self.layoutWidget)
        self.info_gb.setObjectName("info_gb")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.info_gb)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.info_lb = QtGui.QLabel(self.info_gb)
        self.info_lb.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.info_lb.setObjectName("info_lb")
        self.verticalLayout_3.addWidget(self.info_lb)
        self.verticalLayout.addWidget(self.info_gb)
        self.refresh_btn = QtGui.QPushButton(self.layoutWidget)
        self.refresh_btn.setObjectName("refresh_btn")
        self.verticalLayout.addWidget(self.refresh_btn)
        self.settings_btn = QtGui.QPushButton(self.layoutWidget)
        self.settings_btn.setObjectName("settings_btn")
        self.verticalLayout.addWidget(self.settings_btn)
        self.verticalLayout_2.addWidget(self.splitter_2)
        projectManager.setCentralWidget(self.centralwidget)

        self.retranslateUi(projectManager)
        QtCore.QMetaObject.connectSlotsByName(projectManager)

    def retranslateUi(self, projectManager):
        projectManager.setWindowTitle(QtGui.QApplication.translate("projectManager", "Project Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.create_btn.setText(QtGui.QApplication.translate("projectManager", "Create Project", None, QtGui.QApplication.UnicodeUTF8))
        self.update_btn.setText(QtGui.QApplication.translate("projectManager", "Update Project", None, QtGui.QApplication.UnicodeUTF8))
        self.backup_btn.setText(QtGui.QApplication.translate("projectManager", "Move to BACKUP", None, QtGui.QApplication.UnicodeUTF8))
        self.openBackup_btn.setText(QtGui.QApplication.translate("projectManager", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.archive_btn.setText(QtGui.QApplication.translate("projectManager", "Move to ARCHIVE", None, QtGui.QApplication.UnicodeUTF8))
        self.openArchive_btn.setText(QtGui.QApplication.translate("projectManager", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.templateEditor_btn.setText(QtGui.QApplication.translate("projectManager", "Template Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.info_gb.setTitle(QtGui.QApplication.translate("projectManager", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.info_lb.setText(QtGui.QApplication.translate("projectManager", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.refresh_btn.setText(QtGui.QApplication.translate("projectManager", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.settings_btn.setText(QtGui.QApplication.translate("projectManager", "Settings", None, QtGui.QApplication.UnicodeUTF8))

