# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TILER4.3.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os
import cv2 as cv
import numpy as np
import tensorflow as tf
from PyQt5.QtWidgets import QFileDialog, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets


class FileExplorerWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialog'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.openFileNameDialog()
        # self.openFileNamesDialog()
        # self.saveFileDialog()
        self.show()

    def openFileNameDialog(self):
        global file_path
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        # dialog.setNameFilter(tr("Images (*.png *.xpm *.jpg)"))
        fileName, _ = QFileDialog.getOpenFileName(self, "Select Tile", "", "All Files (*)", options=options)
        file_path = fileName  # set imported file path
        if fileName:
            print(fileName)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(963, 845)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 331, 768))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_19.setMaximumSize(QtCore.QSize(16777215, 16))
        self.label_19.setObjectName("label_19")
        self.verticalLayout_7.addWidget(self.label_19)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setMouseTracking(True)
        self.label_9.setAutoFillBackground(True)
        self.label_9.setFrameShape(QtWidgets.QFrame.Box)
        self.label_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_9.setLineWidth(2)
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("../../../../../Tese/workspace/stone_floor_256x256.png"))
        self.label_9.setObjectName("label_9")
        self.verticalLayout_7.addWidget(self.label_9)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_2.addWidget(self.label_18)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(256, 256))
        self.label_3.setMaximumSize(QtCore.QSize(256, 256))
        self.label_3.setSizeIncrement(QtCore.QSize(1, 1))
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../../../../Tese/workspace/black.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 10, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(150, 10, 55, 16))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.widget)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_2.addWidget(self.label_17)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setMinimumSize(QtCore.QSize(256, 256))
        self.label_16.setMaximumSize(QtCore.QSize(256, 256))
        self.label_16.setSizeIncrement(QtCore.QSize(1, 1))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("../../../../../Tese/workspace/black.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_2.addWidget(self.label_16)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.ImGen_tab = QtWidgets.QWidget()
        self.ImGen_tab.setObjectName("ImGen_tab")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.ImGen_tab)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.groupBox_4 = QtWidgets.QGroupBox(self.ImGen_tab)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_22 = QtWidgets.QLabel(self.groupBox_4)
        self.label_22.setMinimumSize(QtCore.QSize(64, 64))
        self.label_22.setMaximumSize(QtCore.QSize(64, 64))
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap("../../../../../Tese/workspace/concrete.png"))
        self.label_22.setScaledContents(True)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout.addWidget(self.label_22)
        self.frame_3 = QtWidgets.QFrame(self.groupBox_4)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_23 = QtWidgets.QLabel(self.frame_3)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_6.addWidget(self.label_23)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_6.addWidget(self.pushButton_2)
        self.horizontalLayout.addWidget(self.frame_3)
        self.verticalLayout_8.addWidget(self.groupBox_4)
        self.groupBox = QtWidgets.QGroupBox(self.ImGen_tab)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setObjectName("label_20")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.spinBox_5 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_5.setMaximum(99999)
        self.spinBox_5.setProperty("value", 256)
        self.spinBox_5.setObjectName("spinBox_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox_5)
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setObjectName("label_21")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.spinBox_6 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_6.setMaximum(99999)
        self.spinBox_6.setProperty("value", 512)
        self.spinBox_6.setObjectName("spinBox_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBox_6)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setObjectName("pushButton_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pushButton_4)
        self.verticalLayout_8.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.ImGen_tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox.setMaximum(1920)
        self.spinBox.setProperty("value", 256)
        self.spinBox.setObjectName("spinBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_2.setMaximum(100000)
        self.spinBox_2.setProperty("value", 256)
        self.spinBox_2.setObjectName("spinBox_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBox_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pushButton_5)
        self.verticalLayout_8.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.ImGen_tab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox_3)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.spinBox_3 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_3.setObjectName("spinBox_3")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox_3)
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.spinBox_7 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_7.setProperty("value", 1)
        self.spinBox_7.setObjectName("spinBox_7")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBox_7)
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.spinBox_4 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_4.setMaximum(999999)
        self.spinBox_4.setProperty("value", 1000)
        self.spinBox_4.setObjectName("spinBox_4")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBox_4)
        self.verticalLayout_8.addWidget(self.groupBox_3)
        self.pushButton = QtWidgets.QPushButton(self.ImGen_tab)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_8.addWidget(self.pushButton)
        self.progressBar = QtWidgets.QProgressBar(self.ImGen_tab)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_8.addWidget(self.progressBar)
        self.tabWidget.addTab(self.ImGen_tab, "")
        self.net_train_tab = QtWidgets.QWidget()
        self.net_train_tab.setObjectName("net_train_tab")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.net_train_tab)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.groupBox_5 = QtWidgets.QGroupBox(self.net_train_tab)
        self.groupBox_5.setObjectName("groupBox_5")
        self.formLayout_4 = QtWidgets.QFormLayout(self.groupBox_5)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_24 = QtWidgets.QLabel(self.groupBox_5)
        self.label_24.setObjectName("label_24")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_6.setObjectName("pushButton_6")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pushButton_6)
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_9.setObjectName("pushButton_9")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.pushButton_9)
        self.verticalLayout_9.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.net_train_tab)
        self.groupBox_6.setObjectName("groupBox_6")
        self.formLayout_5 = QtWidgets.QFormLayout(self.groupBox_6)
        self.formLayout_5.setObjectName("formLayout_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_7.setObjectName("pushButton_7")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pushButton_7)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_3.setObjectName("pushButton_3")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pushButton_3)
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_8.setObjectName("pushButton_8")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pushButton_8)
        self.verticalLayout_9.addWidget(self.groupBox_6)
        self.tabWidget.addTab(self.net_train_tab, "")
        self.results_tab = QtWidgets.QWidget()
        self.results_tab.setObjectName("results_tab")

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.results_tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_7 = QtWidgets.QGroupBox(self.results_tab)
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.listView = QtWidgets.QListView(self.groupBox_7)
        self.listView.setViewMode(QtWidgets.QListView.IconMode)
        self.listView.setModelColumn(0)
        self.listView.setObjectName("listView")
        self.horizontalLayout_3.addWidget(self.listView)
        self.verticalLayout_4.addWidget(self.groupBox_7)
        self.groupBox_8 = QtWidgets.QGroupBox(self.results_tab)
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_4.addWidget(self.groupBox_8)
        self.tabWidget.addTab(self.results_tab, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 963, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton_2.clicked.connect(self.update_tile)
        self.pushButton.clicked.connect(self.save_images)
        self.pushButton_5.clicked.connect(self.update_capture_preview_img)
        self.pushButton_4.clicked.connect(self.update_roll)
        self.pushButton_6.clicked.connect(self.load_network_model)
        self.pushButton_3.clicked.connect(self.auto_mode)
        self.pushButton_7.clicked.connect(self.next_sim_step)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TILER_3.0"))
        self.label_19.setText(_translate("MainWindow", "Roller"))
        self.label_18.setText(_translate("MainWindow", "Capture"))
        self.label.setText(_translate("MainWindow", "MSE:"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_17.setText(_translate("MainWindow", "Model Generated Image"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Load Tile"))
        self.label_23.setText(_translate("MainWindow", "Selected Image"))
        self.pushButton_2.setText(_translate("MainWindow", "Select Tile"))
        self.groupBox.setTitle(_translate("MainWindow", "Roller"))
        self.label_20.setText(_translate("MainWindow", "Roller Width"))
        self.label_21.setText(_translate("MainWindow", "Roller Height"))
        self.pushButton_4.setText(_translate("MainWindow", "Preview Roll"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Capture"))
        self.label_4.setText(_translate("MainWindow", "Capture Width"))
        self.label_5.setText(_translate("MainWindow", "Capture Height"))
        self.pushButton_5.setText(_translate("MainWindow", "Preview Capture"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Timeframe"))
        self.label_6.setText(_translate("MainWindow", "Roller speed (pixels/sec)"))
        self.label_7.setText(_translate("MainWindow", "Capture frequency (pix/s)"))
        self.label_8.setText(_translate("MainWindow", "#images"))
        self.pushButton.setText(_translate("MainWindow", "Generate Images"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ImGen_tab), _translate("MainWindow", "ImGen"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Load Model"))
        self.label_24.setText(_translate("MainWindow", "Current Model"))

        self.pushButton_6.setText(_translate("MainWindow", "Load Model"))
        self.pushButton_9.setText(_translate("MainWindow", "Copy model input settings"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Simulation"))
        self.pushButton_7.setText(_translate("MainWindow", "Next step"))
        self.pushButton_3.setText(_translate("MainWindow", "Auto"))
        self.pushButton_8.setText(_translate("MainWindow", "Stop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.net_train_tab), _translate("MainWindow", "Model"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Batch used for current prediction"))
        self.groupBox_8.setTitle(_translate("MainWindow", "GroupBox"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.results_tab), _translate("MainWindow", "Results"))

    def update_roll(self):
        """updates roll preview img and roll_array global var"""

        global roll_array
        roller_width = self.spinBox_5.value()
        roller_height = self.spinBox_6.value()
        img = tile_array
        print(img.shape)
        # im_height, im_width, im_channels = img.shape
        # roller = np.zeros([im_height, im_width, im_channels], dtype=np.uint8)
        horizontal_slice = img

        while (horizontal_slice.shape[1] < roller_width):
            horizontal_slice = np.concatenate((horizontal_slice, img), axis=1)  # ---tile horizontally if necessary
            print('tiling horizontally')
            print(horizontal_slice.shape)

        if roll_array.shape[1] < roller_width:
            roll_array = horizontal_slice
            print(roll_array.shape)
        while (roll_array.shape[0] < roller_height):
            roll_array = np.concatenate((roll_array, horizontal_slice),
                                        axis=0)  # ---tile vertically if necessary
            print('tiling verticaly')
            print(roll_array.shape)

        masked_array = roll_array

        # convert roll_array to qpixmap
        height, width, channels = masked_array.shape  # height, width, channel
        bytesPerLine = width * channels  # *3 for RGB
        qImg = QtGui.QImage(masked_array.data, width, height, bytesPerLine,
                            QtGui.QImage.Format_RGB888)  # convert to QImg

        self.label_9.setPixmap(QtGui.QPixmap(qImg))  # show img

    def save_images(self):

        capture_width = self.spinBox.value()
        capture_height = self.spinBox_2.value()
        roller_speed = self.spinBox_3.value()
        N_SAMPLES = self.spinBox_4.value()

        ROLLER_SPEED = 7
        global BATCH_SIZE

        # capture = np.zeros([capture_height, capture_width, channels], dtype=np.uint8)
        # roller_y = 0

        # roller = np.zeros([im_height, im_width, im_channels], dtype=np.uint8)
        global roller
        roller = tile_array

        # print('original image shape:', img.shape)

        for k in range(N_SAMPLES):
            while (roller.shape[1] < capture_width):
                roller = np.concatenate((roller, tile), axis=1)  # ---tile horizontally if necessary
                # print('tiling horizontally')
                # print(roller.shape)

            while (roller.shape[0] < capture_height):
                roller = np.concatenate((roller, tile), axis=0)  # ---tile vertically if necessary
                # print('tiling verticaly')
                # print(roller.shape)

            # ---take screenshot---
            capture_to_save = roller[0:capture_height, 0:capture_width, ::]
            # print('taking capture')

            # ---roll roller---
            # for i in range(roller_speed):
            roller = roller[ROLLER_SPEED:]  # delete old capture space in roller
            print('shape after delete:', roller.shape)

            if not os.path.exists('imgs'):
                os.makedirs('imgs')

            filename = 'imgs/img_' + '%03d' % k + '.png'
            cv.imwrite(filename, capture_to_save)

    def update_capture_array(self):
        global capture_array
        capture_width = self.spinBox.value()
        capture_height = self.spinBox_2.value()
        capture_array = roll_array[0:capture_height, 0:capture_width]
        # roller_speed = self.spinBox_3.value()

    def update_capture_preview_img(self):
        # global capture_preview
        capture_width = self.spinBox.value()
        capture_height = self.spinBox_2.value()
        roller_speed = self.spinBox_3.value()
        capture_preview = roll_array[0:capture_height, 0:capture_width]
        print(capture_preview.shape)

        # convert capture_array to qpixmap
        capture_preview = cv.cvtColor(capture_preview, cv.COLOR_BGR2RGB)
        height, width, channels = capture_preview.shape  # height, width, channel
        bytesPerLine = width * channels  # *3 for RGB
        qImg2 = QtGui.QImage(capture_preview.data, width, height, bytesPerLine,
                             QtGui.QImage.Format_RGB888)  # convert to QImg
        self.label_3.setPixmap(QtGui.QPixmap(qImg2))  # show img

    def update_tile(self):
        widget1 = FileExplorerWidget()
        global tile, tile_array, tile_width, tile_height, tile_n_channels  # get tile data variables
        tile_path = file_path
        tile = cv.imread(str(tile_path))  # open new tile
        tile = tile.convert('RGB')
        tile_array = np.array(tile)  # get array from new tile
        (tile_width, tile_height, tile_n_channels) = tile_array.shape  # update tile data variables
        self.label_22.setPixmap(QtGui.QPixmap(str(tile_path)))  # update tile thumbnail
        self.update_roll()
        self.update_capture_preview_img()

    def load_network_model(self):
        widget2 = FileExplorerWidget()
        global model_path, model_input_height, model_input_width, model_batch_size, loaded_model
        model_path = file_path
        loaded_model = tf.keras.models.load_model(str(model_path))
        # loaded_model.load_weights()
        # loaded_model = tf.train.Checkpoint.restore(model_path)
        # print(loaded_model.summary())
        model_input_height = loaded_model.get_layer(index=0).get_config()['batch_input_shape'][2]  # input height
        model_input_width = loaded_model.get_layer(index=0).get_config()['batch_input_shape'][3]  # input width
        model_batch_size = loaded_model.get_layer(index=0).get_config()['batch_input_shape'][1]  # input batch size

        self.spinBox_2.setProperty("value", model_input_height)  # update capture height to model input height
        self.spinBox.setProperty("value", model_input_width)  # update capture width to model input width
        self.spinBox_4.setProperty("value", model_batch_size + 1)  # update number of images to model_batch_size


    def auto_mode(self):
        global prediction_array, img_batch
        img_batch = generate_first_capture_batch()

        prediction_tensor = loaded_model.predict(img_batch, batch_size=BATCH_SIZE)
        # print('prediction_tensor:', prediction_tensor.shape)
        prediction_array = prediction_tensor * 255
        prediction_array = np.array(prediction_array, dtype=np.uint8)  # back to uint8
        prediction_array = prediction_array[0]

        self.update_prediction_window()
        # predict next image and update window
        # generate next image and update window
        # compare(mse)
        # update_capture_batch()
        # wait a second

    def update_prediction_window(self):
        prediction_rgb = cv.cvtColor(prediction_array, cv.COLOR_BGR2RGB)
        height, width, channels = prediction_rgb.shape  # height, width, channel
        bytesPerLine = width * channels  # *3 for RGB
        qImg1 = QtGui.QImage(prediction_rgb.data, width, height, bytesPerLine,
                             QtGui.QImage.Format_RGB888)  # convert to QImg
        self.label_16.setPixmap(QtGui.QPixmap(qImg1))  # show img

    def next_sim_step(self):
        # generate next image and batch
        # self.generate_next_sim_capture
        # global capture_batch
        capture_batch = self.generate_next_capture_batch()

        prediction_tensor = loaded_model.predict(capture_batch, batch_size=BATCH_SIZE)
        # print('prediction_tensor:', prediction_tensor.shape)
        prediction_array = prediction_tensor * 255
        prediction_array = np.array(prediction_array, dtype=np.uint8)  # back to uint8
        # print('prediction_array:', prediction_array.shape)
        prediction_array = prediction_array[0]

        self.update_prediction_window()
        self.update_roll()
        self.update_capture_preview_img()

    def generate_next_capture_batch(self):
        global img_batch
        new_img_batch = img_batch[::, 1:, ::, ::, ::]  # copy old batch
        # new_img_batch = np.delete(new_img_batch, 0, axis=0)#delete first image of old batch
        # self.generate_next_sim_capture() #generate next capture
        self.generate_next_sim_capture()
        input_array = capture_array
        input_array = input_array / 255
        input_array = np.expand_dims(input_array, axis=0)  # add dimension in order to add to batch
        new_img_batch = np.squeeze(new_img_batch, axis=0)  # remove the 1 from first position
        new_img_batch = np.concatenate((new_img_batch, input_array), axis=0)  # add new capture to batch
        new_img_batch = np.expand_dims(new_img_batch,
                                       axis=0)  # add dimension to batch to get (None, batch_size, img_height, img_width, channels)
        print("New image batch shape:", new_img_batch.shape)
        img_batch = new_img_batch
        return new_img_batch

    def generate_next_sim_capture(self):
        capture_width = self.spinBox.value()
        capture_height = self.spinBox_2.value()
        roller_speed = self.spinBox_3.value()
        global roll_array, capture_array

        # ---roll roller---#
        roll_array = roll_array[roller_speed:]  # delete old capture space in roller

        # ---update roll preview---#
        # self.update_roll
        # self.update_capture_preview_img

        # ---take screenshot---#
        capture_array = roll_array[0:capture_height, 0:capture_width, ::]
        return capture_array

    # def update_prediction(self):


# ----------------------------------------------------------------------------------------------------------

def generate_first_capture_batch():
    global roll_array
    img_batch = np.zeros([1, model_input_height, model_input_width, 3], dtype=np.uint8)

    for k in range(model_batch_size):
        ui.update_capture_array()
        input_arr = capture_array
        input_arr = input_arr / 255
        input_arr = np.expand_dims(input_arr, axis=0)
        # img_batch = np.squeeze(img_batch, axis = 0)
        img_batch = np.concatenate((img_batch, input_arr), axis=0)
        roll_array = roll_array[roller_speed:]
        print(img_batch.shape)

    img_batch = np.delete(img_batch, 0, axis=0)
    img_batch = np.array(img_batch, dtype='float32')
    img_batch = np.expand_dims(img_batch, axis=0)
    print('first capture batch shape:', img_batch.shape)

    return img_batch


def tensor_to_image(tensor):
    tensor = tensor * 255
    tensor = np.array(tensor, dtype=np.uint8)
    if np.ndim(tensor) > 3:
        assert tensor.shape[0] == 1
        tensor = tensor[0]
        print(tensor.shape)
    return tensor


if __name__ == "__main__":
    import sys

    global tile, tile_array
    tile_path = str('Decking_300x300.png')  # set initial tile path
    tile = cv.imread(str(tile_path))
    tile = cv.cvtColor(tile, cv.COLOR_BGR2RGB)
    tile_array = np.array(tile)  # get tile path array
    (tile_width, tile_height, tile_n_channels) = tile_array.shape  # get tile width, size and number of chanels
    roller_speed = 7

    roll_array = np.zeros([2, 2, 2], dtype=np.uint8)
    capture_array = np.zeros([2, 2, 2], dtype=np.uint8)
    current_iteration = 0
    BATCH_SIZE = 1

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.update_roll()
    ui.update_capture_preview_img()

    sys.exit(app.exec_())
