# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_item_list.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_select_item_list(QtWidgets.QWidget):
    def setupUi(self, select_item_list):
        self.gridLayout_2 = QtWidgets.QGridLayout(select_item_list)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(2)
        self.gridLayout.setVerticalSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(select_item_list)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1, QtCore.Qt.AlignRight)
        self.items_list_widget = QtWidgets.QListWidget(select_item_list)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.items_list_widget.sizePolicy().hasHeightForWidth())
        self.items_list_widget.setSizePolicy(sizePolicy)
        self.items_list_widget.setObjectName("items_list_widget")
        self.gridLayout.addWidget(self.items_list_widget, 0, 0, 1, 1)
        self.gridLayout.setRowMinimumHeight(0, 5)
        self.gridLayout.setRowMinimumHeight(1, 5)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(select_item_list)
        QtCore.QMetaObject.connectSlotsByName(select_item_list)

    def retranslateUi(self, select_item_list):
        _translate = QtCore.QCoreApplication.translate
        select_item_list.setWindowTitle(_translate("select_item_list", "Form"))
        self.pushButton.setText(_translate("select_item_list", "PushButton"))
