# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alexey\Documents\GitHub\CGScripting\13. Image Converter\widgets\imageConverter.ui'
#
# Created: Thu Feb 08 20:46:52 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_imageConverter(object):
    def setupUi(self, imageConverter):
        imageConverter.setObjectName("imageConverter")
        imageConverter.resize(1047, 850)
        self.centralwidget = QtGui.QWidget(imageConverter)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.imageMagick_gbox = QtGui.QGroupBox(self.centralwidget)
        self.imageMagick_gbox.setFlat(False)
        self.imageMagick_gbox.setObjectName("imageMagick_gbox")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.imageMagick_gbox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.imagemagick_lb = QtGui.QLabel(self.imageMagick_gbox)
        self.imagemagick_lb.setObjectName("imagemagick_lb")
        self.horizontalLayout.addWidget(self.imagemagick_lb)
        self.browseImagemagick_btn = QtGui.QPushButton(self.imageMagick_gbox)
        self.browseImagemagick_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.browseImagemagick_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.browseImagemagick_btn.setObjectName("browseImagemagick_btn")
        self.horizontalLayout.addWidget(self.browseImagemagick_btn)
        self.horizontalLayout_5.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addWidget(self.imageMagick_gbox)
        self.sources_gbox = QtGui.QGroupBox(self.centralwidget)
        self.sources_gbox.setObjectName("sources_gbox")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.sources_gbox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.files_ly = QtGui.QVBoxLayout()
        self.files_ly.setObjectName("files_ly")
        self.verticalLayout_2.addLayout(self.files_ly)
        self.subfolders_chb = QtGui.QCheckBox(self.sources_gbox)
        self.subfolders_chb.setChecked(True)
        self.subfolders_chb.setObjectName("subfolders_chb")
        self.verticalLayout_2.addWidget(self.subfolders_chb)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.addFolder_btn = QtGui.QPushButton(self.sources_gbox)
        self.addFolder_btn.setStyleSheet("Text-align:left")
        self.addFolder_btn.setIconSize(QtCore.QSize(32, 32))
        self.addFolder_btn.setObjectName("addFolder_btn")
        self.verticalLayout.addWidget(self.addFolder_btn)
        self.addImage_btn = QtGui.QPushButton(self.sources_gbox)
        self.addImage_btn.setStyleSheet("Text-align:left")
        self.addImage_btn.setIconSize(QtCore.QSize(32, 32))
        self.addImage_btn.setObjectName("addImage_btn")
        self.verticalLayout.addWidget(self.addImage_btn)
        self.remove_btn = QtGui.QPushButton(self.sources_gbox)
        self.remove_btn.setStyleSheet("Text-align:left")
        self.remove_btn.setIconSize(QtCore.QSize(32, 32))
        self.remove_btn.setObjectName("remove_btn")
        self.verticalLayout.addWidget(self.remove_btn)
        self.showPaths_btn = QtGui.QPushButton(self.sources_gbox)
        self.showPaths_btn.setStyleSheet("Text-align:left")
        self.showPaths_btn.setIconSize(QtCore.QSize(32, 32))
        self.showPaths_btn.setCheckable(True)
        self.showPaths_btn.setObjectName("showPaths_btn")
        self.verticalLayout.addWidget(self.showPaths_btn)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_4.addWidget(self.sources_gbox)
        self.destination_gbox = QtGui.QGroupBox(self.centralwidget)
        self.destination_gbox.setObjectName("destination_gbox")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.destination_gbox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.out_le = QtGui.QLineEdit(self.destination_gbox)
        self.out_le.setObjectName("out_le")
        self.horizontalLayout_2.addWidget(self.out_le)
        self.browseOut_btn = QtGui.QPushButton(self.destination_gbox)
        self.browseOut_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.browseOut_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.browseOut_btn.setObjectName("browseOut_btn")
        self.horizontalLayout_2.addWidget(self.browseOut_btn)
        self.clearOut_btn = QtGui.QPushButton(self.destination_gbox)
        self.clearOut_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.clearOut_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.clearOut_btn.setObjectName("clearOut_btn")
        self.horizontalLayout_2.addWidget(self.clearOut_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.formatOut_cbox = QtGui.QComboBox(self.destination_gbox)
        self.formatOut_cbox.setObjectName("formatOut_cbox")
        self.formatOut_cbox.addItem("")
        self.formatOut_cbox.addItem("")
        self.formatOut_cbox.addItem("")
        self.formatOut_cbox.addItem("")
        self.formatOut_cbox.addItem("")
        self.horizontalLayout_4.addWidget(self.formatOut_cbox)
        self.label = QtGui.QLabel(self.destination_gbox)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.replace_rbtn = QtGui.QRadioButton(self.destination_gbox)
        self.replace_rbtn.setObjectName("replace_rbtn")
        self.horizontalLayout_4.addWidget(self.replace_rbtn)
        self.skip_rbtn = QtGui.QRadioButton(self.destination_gbox)
        self.skip_rbtn.setObjectName("skip_rbtn")
        self.horizontalLayout_4.addWidget(self.skip_rbtn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.addWidget(self.destination_gbox)
        self.horizontalLayout_1 = QtGui.QHBoxLayout()
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.start_btn = QtGui.QPushButton(self.centralwidget)
        self.start_btn.setMinimumSize(QtCore.QSize(0, 32))
        self.start_btn.setIconSize(QtCore.QSize(32, 32))
        self.start_btn.setObjectName("start_btn")
        self.horizontalLayout_1.addWidget(self.start_btn)
        self.stop_btn = QtGui.QPushButton(self.centralwidget)
        self.stop_btn.setMinimumSize(QtCore.QSize(0, 32))
        self.stop_btn.setIconSize(QtCore.QSize(32, 32))
        self.stop_btn.setObjectName("stop_btn")
        self.horizontalLayout_1.addWidget(self.stop_btn)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_1.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_1)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_4.addWidget(self.progressBar)
        imageConverter.setCentralWidget(self.centralwidget)

        self.retranslateUi(imageConverter)
        QtCore.QMetaObject.connectSlotsByName(imageConverter)

    def retranslateUi(self, imageConverter):
        imageConverter.setWindowTitle(QtGui.QApplication.translate("imageConverter", "Image Cоnverter", None, QtGui.QApplication.UnicodeUTF8))
        self.imageMagick_gbox.setTitle(QtGui.QApplication.translate("imageConverter", "ImageMagick", None, QtGui.QApplication.UnicodeUTF8))
        self.imagemagick_lb.setText(QtGui.QApplication.translate("imageConverter", "Select magick.exe file", None, QtGui.QApplication.UnicodeUTF8))
        self.browseImagemagick_btn.setText(QtGui.QApplication.translate("imageConverter", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.sources_gbox.setTitle(QtGui.QApplication.translate("imageConverter", "Source folders and files", None, QtGui.QApplication.UnicodeUTF8))
        self.subfolders_chb.setText(QtGui.QApplication.translate("imageConverter", "Include subfolders", None, QtGui.QApplication.UnicodeUTF8))
        self.addFolder_btn.setToolTip(QtGui.QApplication.translate("imageConverter", "Select a folder with images to be converted", None, QtGui.QApplication.UnicodeUTF8))
        self.addFolder_btn.setText(QtGui.QApplication.translate("imageConverter", "Add Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.addImage_btn.setToolTip(QtGui.QApplication.translate("imageConverter", "Select images to be converted", None, QtGui.QApplication.UnicodeUTF8))
        self.addImage_btn.setText(QtGui.QApplication.translate("imageConverter", "Add Image", None, QtGui.QApplication.UnicodeUTF8))
        self.remove_btn.setToolTip(QtGui.QApplication.translate("imageConverter", "Exclude folders and images from convertation", None, QtGui.QApplication.UnicodeUTF8))
        self.remove_btn.setText(QtGui.QApplication.translate("imageConverter", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.showPaths_btn.setToolTip(QtGui.QApplication.translate("imageConverter", "Show/hide full paths", None, QtGui.QApplication.UnicodeUTF8))
        self.showPaths_btn.setText(QtGui.QApplication.translate("imageConverter", "Show paths", None, QtGui.QApplication.UnicodeUTF8))
        self.destination_gbox.setTitle(QtGui.QApplication.translate("imageConverter", "Destination folder", None, QtGui.QApplication.UnicodeUTF8))
        self.out_le.setToolTip(QtGui.QApplication.translate("imageConverter", "All converted images will be saved in this folder. If the folder is not specified, they will be saved in the same folders as the source images.", None, QtGui.QApplication.UnicodeUTF8))
        self.browseOut_btn.setText(QtGui.QApplication.translate("imageConverter", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.clearOut_btn.setText(QtGui.QApplication.translate("imageConverter", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.formatOut_cbox.setItemText(0, QtGui.QApplication.translate("imageConverter", "JPEG", None, QtGui.QApplication.UnicodeUTF8))
        self.formatOut_cbox.setItemText(1, QtGui.QApplication.translate("imageConverter", "PNG", None, QtGui.QApplication.UnicodeUTF8))
        self.formatOut_cbox.setItemText(2, QtGui.QApplication.translate("imageConverter", "TIFF", None, QtGui.QApplication.UnicodeUTF8))
        self.formatOut_cbox.setItemText(3, QtGui.QApplication.translate("imageConverter", "ICO", None, QtGui.QApplication.UnicodeUTF8))
        self.formatOut_cbox.setItemText(4, QtGui.QApplication.translate("imageConverter", "SVG", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("imageConverter", "Name collision resolution:", None, QtGui.QApplication.UnicodeUTF8))
        self.replace_rbtn.setText(QtGui.QApplication.translate("imageConverter", "Replace", None, QtGui.QApplication.UnicodeUTF8))
        self.skip_rbtn.setText(QtGui.QApplication.translate("imageConverter", "Skip", None, QtGui.QApplication.UnicodeUTF8))
        self.start_btn.setText(QtGui.QApplication.translate("imageConverter", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.stop_btn.setText(QtGui.QApplication.translate("imageConverter", "Stop", None, QtGui.QApplication.UnicodeUTF8))

