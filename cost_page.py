# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cost_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_cost_page(object):
    def setupUi(self, cost_page):
        cost_page.setObjectName("cost_page")
        cost_page.resize(545, 507)
        self.gridLayout = QtWidgets.QGridLayout(cost_page)
        self.gridLayout.setObjectName("gridLayout")
        self.cost_tree = QtWidgets.QTreeWidget(cost_page)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.cost_tree.setFont(font)
        self.cost_tree.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.cost_tree.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.cost_tree.setObjectName("cost_tree")
        self.cost_tree.headerItem().setText(0, "1")
        self.gridLayout.addWidget(self.cost_tree, 0, 0, 1, 1)

        self.retranslateUi(cost_page)
        QtCore.QMetaObject.connectSlotsByName(cost_page)

    def retranslateUi(self, cost_page):
        _translate = QtCore.QCoreApplication.translate
        cost_page.setWindowTitle(_translate("cost_page", "Frame"))
