# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show_price.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_show_price(object):
    def setupUi(self, show_price):
        show_price.setObjectName("show_price")
        show_price.resize(984, 590)
        self.gridLayout = QtWidgets.QGridLayout(show_price)
        self.gridLayout.setObjectName("gridLayout")
        self.show_sale = QtWidgets.QGroupBox(show_price)
        self.show_sale.setObjectName("show_sale")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.show_sale)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.sale_list = QtWidgets.QTableWidget(self.show_sale)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sale_list.setFont(font)
        self.sale_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.sale_list.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.sale_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.sale_list.setShowGrid(False)
        self.sale_list.setRowCount(30)
        self.sale_list.setObjectName("sale_list")
        self.sale_list.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.sale_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.sale_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.sale_list.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.sale_list.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.sale_list.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.sale_list.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.sale_list.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.sale_list.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.sale_list.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.sale_list.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.sale_list.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.sale_list.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.sale_list.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.sale_list.setItem(0, 6, item)
        self.gridLayout_3.addWidget(self.sale_list, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.show_sale, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.seven_day = QtWidgets.QLabel(show_price)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.seven_day.setFont(font)
        self.seven_day.setObjectName("seven_day")
        self.horizontalLayout.addWidget(self.seven_day)
        self.sale_velocity = QtWidgets.QLabel(show_price)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.sale_velocity.setFont(font)
        self.sale_velocity.setObjectName("sale_velocity")
        self.horizontalLayout.addWidget(self.sale_velocity, 0, QtCore.Qt.AlignLeft)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.show_min_price = QtWidgets.QGroupBox(show_price)
        self.show_min_price.setObjectName("show_min_price")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.show_min_price)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.all_server = QtWidgets.QTableWidget(self.show_min_price)
        self.all_server.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.all_server.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.all_server.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.all_server.setShowGrid(False)
        self.all_server.setRowCount(8)
        self.all_server.setObjectName("all_server")
        self.all_server.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.all_server.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.all_server.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.all_server.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.all_server.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.all_server.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.all_server.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.all_server.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.all_server.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.all_server.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.all_server.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.all_server.setItem(2, 0, item)
        self.gridLayout_2.addWidget(self.all_server, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.show_min_price, 2, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 7)
        self.gridLayout.setRowStretch(2, 5)

        self.retranslateUi(show_price)
        QtCore.QMetaObject.connectSlotsByName(show_price)

    def retranslateUi(self, show_price):
        _translate = QtCore.QCoreApplication.translate
        show_price.setWindowTitle(_translate("show_price", "Form"))
        self.show_sale.setTitle(_translate("show_price", "正在出售"))
        item = self.sale_list.horizontalHeaderItem(0)
        item.setText(_translate("show_price", "单价"))
        item = self.sale_list.horizontalHeaderItem(2)
        item.setText(_translate("show_price", "数量"))
        item = self.sale_list.horizontalHeaderItem(3)
        item.setText(_translate("show_price", "总价"))
        item = self.sale_list.horizontalHeaderItem(4)
        item.setText(_translate("show_price", "服务器"))
        item = self.sale_list.horizontalHeaderItem(5)
        item.setText(_translate("show_price", "雇员"))
        item = self.sale_list.horizontalHeaderItem(6)
        item.setText(_translate("show_price", "更新时间"))
        __sortingEnabled = self.sale_list.isSortingEnabled()
        self.sale_list.setSortingEnabled(False)
        self.sale_list.setSortingEnabled(__sortingEnabled)
        self.seven_day.setText(_translate("show_price", "当前大区近七天平均售出价格：N/A"))
        self.sale_velocity.setText(_translate("show_price", "走货量指数"))
        self.show_min_price.setTitle(_translate("show_price", "全服比价"))
        item = self.all_server.horizontalHeaderItem(0)
        item.setText(_translate("show_price", "服务器"))
        item = self.all_server.horizontalHeaderItem(1)
        item.setText(_translate("show_price", "单价"))
        item = self.all_server.horizontalHeaderItem(3)
        item.setText(_translate("show_price", "数量"))
        item = self.all_server.horizontalHeaderItem(4)
        item.setText(_translate("show_price", "总价"))
        item = self.all_server.horizontalHeaderItem(5)
        item.setText(_translate("show_price", "雇员"))
        item = self.all_server.horizontalHeaderItem(6)
        item.setText(_translate("show_price", "更新时间"))
        __sortingEnabled = self.all_server.isSortingEnabled()
        self.all_server.setSortingEnabled(False)
        self.all_server.setSortingEnabled(__sortingEnabled)
