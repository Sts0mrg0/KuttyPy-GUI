# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dio_adcConfig.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(395, 298)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.log_2 = QtWidgets.QCheckBox(Dialog)
        self.log_2.setObjectName("log_2")
        self.gridLayout.addWidget(self.log_2, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 3)
        self.log = QtWidgets.QCheckBox(Dialog)
        self.log.setObjectName("log")
        self.gridLayout.addWidget(self.log, 1, 0, 1, 1)
        self.gauge = Gauge(Dialog)
        self.gauge.setObjectName("gauge")
        self.gridLayout.addWidget(self.gauge, 3, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.options = QtWidgets.QComboBox(Dialog)
        self.options.setObjectName("options")
        self.gridLayout.addWidget(self.options, 0, 1, 1, 2)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.log_2.toggled['bool'].connect(Dialog.changeRange)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ADC Configuration"))
        self.log_2.setText(_translate("Dialog", "0-5000mV Range"))
        self.label.setText(_translate("Dialog", "ADMUX"))
        self.log.setText(_translate("Dialog", "Log Read/Write calls"))

from .gauge import Gauge
