# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'download.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_download(object):
    def setupUi(self, download):
        download.setObjectName("download")
        download.resize(608, 372)
        self.gridLayout_2 = QtWidgets.QGridLayout(download)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(download)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(download)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(download)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(download)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.radioButton = QtWidgets.QRadioButton(download)
        self.radioButton.setEnabled(True)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(download)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 5, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(download)
        self.pushButton.clicked.connect(download.StartAll)
        self.pushButton_3.clicked.connect(download.StopAll)
        self.pushButton_2.clicked.connect(download.StartConvertAll)
        self.pushButton_4.clicked.connect(download.StopConvertAll)
        self.radioButton.clicked.connect(download.SetAutoConvert)
        QtCore.QMetaObject.connectSlotsByName(download)

    def retranslateUi(self, download):
        _translate = QtCore.QCoreApplication.translate
        download.setWindowTitle(_translate("download", "Form"))
        self.pushButton.setText(_translate("download", "全部开始"))
        self.pushButton_3.setText(_translate("download", "全部暂停"))
        self.pushButton_2.setText(_translate("download", "开始转码"))
        self.pushButton_4.setText(_translate("download", "暂停转码"))
        self.radioButton.setText(_translate("download", "下载完自动转码"))