# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ac_config.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
# -*- coding: utf-8 -*-
import os
import struct
import time

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


# SPDX-License-Identifier: GPL-2.0-or-later
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal, QObject, QSize,Qt,QCoreApplication
from PyQt5.QtGui import QColor, QFont, QPalette
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QSizePolicy, QGridLayout, QLabel, QSlider, \
    QComboBox, QColorDialog, QCheckBox, QLineEdit, QButtonGroup, QRadioButton, QFileDialog, QMessageBox
from PyQt5.QtGui import QColor,QImage,QPixmap
from basic_editor import BasicEditor
from Send_alarm import SendAlarm
from PIL import Image
import cv2
tr = QCoreApplication.translate

class switch_config(BasicEditor):
    def __init__(self):
        super().__init__()
        self.data = dict()
        self.mode = 1

        w = QWidget()
        w.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.container = QVBoxLayout()

        w.setLayout(self.container)
        self.addWidget(w)
        self.setupUi(w,self.container)


    def setupUi(self,Form,contain):

        self.label = QLabel("按钮")
        self.testButton = QPushButton("单击按钮")

        self.testButton.clicked.connect(self.on_btn_test_clicked)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayout.addWidget(self.testButton)
        contain.addLayout(self.horizontalLayout)

    def on_btn_test_clicked(self):
        QMessageBox.information(None, "测试", "单击了按钮")
        #在该函数下添加你想要做的操作代码


 # layout 移除所有控件
    def remove_all_controls(self,layout):
        while layout.count():
            child = layout.takeAt(0)
            if child is not None:
                if child.widget() is not None:
                    child.widget().deleteLater()
                elif child.layout() is not None:
                    self.clear_layout(child.layout())

    def clear_layout(self,layout):
        while layout is not None and layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                self.clear_layout(item.layout())



    def valid(self):
        # return isinstance(self.device, VialKeyboard)
        return 1

    def rebuild(self, device):
        super().rebuild(device)

        for h in self.handlers:
            h.set_device(device)

        if not self.valid():
            return
        if len(device.kmapcustom):
            print(device.kmapcustom)

