# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setEnabled(True)
        mainWindow.resize(1280, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(900, 600))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.status_bar = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status_bar.sizePolicy().hasHeightForWidth())
        self.status_bar.setSizePolicy(sizePolicy)
        self.status_bar.setMaximumSize(QtCore.QSize(16777215, 70))
        self.status_bar.setObjectName("status_bar")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.status_bar)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.item_icon = QtWidgets.QLabel(self.status_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.item_icon.sizePolicy().hasHeightForWidth())
        self.item_icon.setSizePolicy(sizePolicy)
        self.item_icon.setMinimumSize(QtCore.QSize(50, 50))
        self.item_icon.setMaximumSize(QtCore.QSize(50, 50))
        self.item_icon.setBaseSize(QtCore.QSize(0, 0))
        self.item_icon.setObjectName("item_icon")
        self.horizontalLayout.addWidget(self.item_icon)
        self.jump_to_wiki = QtWidgets.QLabel(self.status_bar)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.jump_to_wiki.setFont(font)
        self.jump_to_wiki.setObjectName("jump_to_wiki")
        self.horizontalLayout.addWidget(self.jump_to_wiki)
        self.show_cost = QtWidgets.QPushButton(self.status_bar)
        self.show_cost.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_cost.sizePolicy().hasHeightForWidth())
        self.show_cost.setSizePolicy(sizePolicy)
        self.show_cost.setMinimumSize(QtCore.QSize(80, 40))
        self.show_cost.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.show_cost.setFont(font)
        self.show_cost.setObjectName("show_cost")
        self.horizontalLayout.addWidget(self.show_cost)
        self.back_query = QtWidgets.QPushButton(self.status_bar)
        self.back_query.setMinimumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.back_query.setFont(font)
        self.back_query.setObjectName("back_query")
        self.horizontalLayout.addWidget(self.back_query)
        self.query_history = QtWidgets.QPushButton(self.status_bar)
        self.query_history.setMinimumSize(QtCore.QSize(80, 40))
        self.query_history.setObjectName("query_history")
        self.horizontalLayout.addWidget(self.query_history)
        self.show_text_uptime = QtWidgets.QLabel(self.status_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.show_text_uptime.sizePolicy().hasHeightForWidth())
        self.show_text_uptime.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.show_text_uptime.setFont(font)
        self.show_text_uptime.setObjectName("show_text_uptime")
        self.horizontalLayout.addWidget(self.show_text_uptime, 0, QtCore.Qt.AlignRight)
        self.show_update_time = QtWidgets.QLabel(self.status_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.show_update_time.sizePolicy().hasHeightForWidth())
        self.show_update_time.setSizePolicy(sizePolicy)
        self.show_update_time.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.show_update_time.setFont(font)
        self.show_update_time.setObjectName("show_update_time")
        self.horizontalLayout.addWidget(self.show_update_time, 0, QtCore.Qt.AlignLeft)
        self.show_text_server = QtWidgets.QLabel(self.status_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.show_text_server.sizePolicy().hasHeightForWidth())
        self.show_text_server.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.show_text_server.setFont(font)
        self.show_text_server.setObjectName("show_text_server")
        self.horizontalLayout.addWidget(self.show_text_server, 0, QtCore.Qt.AlignRight)
        self.show_server = QtWidgets.QLabel(self.status_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.show_server.sizePolicy().hasHeightForWidth())
        self.show_server.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.show_server.setFont(font)
        self.show_server.setObjectName("show_server")
        self.horizontalLayout.addWidget(self.show_server, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout.setStretch(5, 10)
        self.horizontalLayout.setStretch(6, 1)
        self.horizontalLayout.setStretch(7, 2)
        self.horizontalLayout.setStretch(8, 1)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.status_bar, 0, 0, 1, 1)
        self.show_data_area = QtWidgets.QGridLayout()
        self.show_data_area.setObjectName("show_data_area")
        self.show_data_box = QtWidgets.QStackedWidget(self.centralwidget)
        self.show_data_box.setObjectName("show_data_box")
        self.query_item = QtWidgets.QWidget()
        self.query_item.setObjectName("query_item")
        self.show_data_box.addWidget(self.query_item)
        self.select_item = QtWidgets.QWidget()
        self.select_item.setObjectName("select_item")
        self.show_data_box.addWidget(self.select_item)
        self.show_price = QtWidgets.QWidget()
        self.show_price.setObjectName("show_price")
        self.show_data_box.addWidget(self.show_price)
        self.show_craft = QtWidgets.QWidget()
        self.show_craft.setObjectName("show_craft")
        self.show_data_box.addWidget(self.show_craft)
        self.loading_ui = QtWidgets.QWidget()
        self.loading_ui.setObjectName("loading_ui")
        self.show_data_box.addWidget(self.loading_ui)
        self.show_data_area.addWidget(self.show_data_box, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.show_data_area, 1, 0, 1, 1)
        self.gridLayout.setRowMinimumHeight(0, 30)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 20)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.server = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.server.setFont(font)
        self.server.setObjectName("server")
        self.server_luxingniao = QtWidgets.QMenu(self.server)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.server_luxingniao.setFont(font)
        self.server_luxingniao.setObjectName("server_luxingniao")
        self.server_moguli = QtWidgets.QMenu(self.server)
        self.server_moguli.setObjectName("server_moguli")
        self.server_maoxiaopang = QtWidgets.QMenu(self.server)
        self.server_maoxiaopang.setObjectName("server_maoxiaopang")
        self.server_doudouchai = QtWidgets.QMenu(self.server)
        self.server_doudouchai.setObjectName("server_doudouchai")
        self.about = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.about.setFont(font)
        self.about.setObjectName("about")
        mainWindow.setMenuBar(self.menubar)
        self.select_server_all = QtWidgets.QAction(mainWindow)
        self.select_server_all.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.select_server_all.setFont(font)
        self.select_server_all.setObjectName("select_server_all")
        self.select_server_hongyuhai = QtWidgets.QAction(mainWindow)
        self.select_server_hongyuhai.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.select_server_hongyuhai.setFont(font)
        self.select_server_hongyuhai.setObjectName("select_server_hongyuhai")
        self.select_server_shenyizhidi = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.select_server_shenyizhidi.setFont(font)
        self.select_server_shenyizhidi.setObjectName("select_server_shenyizhidi")
        self.select_server_lanuoxiya = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.select_server_lanuoxiya.setFont(font)
        self.select_server_lanuoxiya.setObjectName("select_server_lanuoxiya")
        self.select_server_huanyignqundao = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.select_server_huanyignqundao.setFont(font)
        self.select_server_huanyignqundao.setObjectName("select_server_huanyignqundao")
        self.select_server_mengyachi = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.select_server_mengyachi.setFont(font)
        self.select_server_mengyachi.setObjectName("select_server_mengyachi")
        self.select_server_yuzhouheyin = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.select_server_yuzhouheyin.setFont(font)
        self.select_server_yuzhouheyin.setObjectName("select_server_yuzhouheyin")
        self.select_server_woxianxiran = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.select_server_woxianxiran.setFont(font)
        self.select_server_woxianxiran.setObjectName("select_server_woxianxiran")
        self.select_server_chenxiwangzuo = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.select_server_chenxiwangzuo.setFont(font)
        self.select_server_chenxiwangzuo.setObjectName("select_server_chenxiwangzuo")
        self.select_server_baiyinxiang = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.select_server_baiyinxiang.setFont(font)
        self.select_server_baiyinxiang.setObjectName("select_server_baiyinxiang")
        self.select_server_baijinhuanxiang = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.select_server_baijinhuanxiang.setFont(font)
        self.select_server_baijinhuanxiang.setObjectName("select_server_baijinhuanxiang")
        self.select_server_shenquanhen = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.select_server_shenquanhen.setFont(font)
        self.select_server_shenquanhen.setObjectName("select_server_shenquanhen")
        self.select_server_chaofengting = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.select_server_chaofengting.setFont(font)
        self.select_server_chaofengting.setObjectName("select_server_chaofengting")
        self.select_server_lvrenzhanqiao = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.select_server_lvrenzhanqiao.setFont(font)
        self.select_server_lvrenzhanqiao.setObjectName("select_server_lvrenzhanqiao")
        self.select_server_fuxiaozhijian = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.select_server_fuxiaozhijian.setFont(font)
        self.select_server_fuxiaozhijian.setObjectName("select_server_fuxiaozhijian")
        self.select_server_longchaoshendian = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.select_server_longchaoshendian.setFont(font)
        self.select_server_longchaoshendian.setObjectName("select_server_longchaoshendian")
        self.select_server_mengyubaojing = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.select_server_mengyubaojing.setFont(font)
        self.select_server_mengyubaojing.setObjectName("select_server_mengyubaojing")
        self.select_server_zishuizhanqiao = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.select_server_zishuizhanqiao.setFont(font)
        self.select_server_zishuizhanqiao.setObjectName("select_server_zishuizhanqiao")
        self.select_server_yanxia = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.select_server_yanxia.setFont(font)
        self.select_server_yanxia.setObjectName("select_server_yanxia")
        self.select_server_jingyuzhuagnyuan = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.select_server_jingyuzhuagnyuan.setFont(font)
        self.select_server_jingyuzhuagnyuan.setObjectName("select_server_jingyuzhuagnyuan")
        self.select_server_moduna = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.select_server_moduna.setFont(font)
        self.select_server_moduna.setObjectName("select_server_moduna")
        self.select_server_haimaochawu = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.select_server_haimaochawu.setFont(font)
        self.select_server_haimaochawu.setObjectName("select_server_haimaochawu")
        self.select_server_roufenghaiwan = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.select_server_roufenghaiwan.setFont(font)
        self.select_server_roufenghaiwan.setObjectName("select_server_roufenghaiwan")
        self.select_server_hupoyuan = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.select_server_hupoyuan.setFont(font)
        self.select_server_hupoyuan.setObjectName("select_server_hupoyuan")
        self.select_server_shuijingta = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.select_server_shuijingta.setFont(font)
        self.select_server_shuijingta.setObjectName("select_server_shuijingta")
        self.select_server_yinleihu = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.select_server_yinleihu.setFont(font)
        self.select_server_yinleihu.setObjectName("select_server_yinleihu")
        self.select_server_taiyanghaian = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.select_server_taiyanghaian.setFont(font)
        self.select_server_taiyanghaian.setObjectName("select_server_taiyanghaian")
        self.select_server_yixiujiade = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.select_server_yixiujiade.setFont(font)
        self.select_server_yixiujiade.setObjectName("select_server_yixiujiade")
        self.select_server_hongchachuan = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.select_server_hongchachuan.setFont(font)
        self.select_server_hongchachuan.setObjectName("select_server_hongchachuan")
        self.select_server_luxingniao = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.select_server_luxingniao.setFont(font)
        self.select_server_luxingniao.setObjectName("select_server_luxingniao")
        self.select_server_moguli = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.select_server_moguli.setFont(font)
        self.select_server_moguli.setObjectName("select_server_moguli")
        self.select_server_maoxiaopang = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.select_server_maoxiaopang.setFont(font)
        self.select_server_maoxiaopang.setObjectName("select_server_maoxiaopang")
        self.select_server_doudouchai = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.select_server_doudouchai.setFont(font)
        self.select_server_doudouchai.setObjectName("select_server_doudouchai")
        self.use_static_file = QtWidgets.QAction(mainWindow)
        self.use_static_file.setCheckable(True)
        self.use_static_file.setChecked(True)
        self.use_static_file.setEnabled(True)
        self.use_static_file.setObjectName("use_static_file")
        self.check_update = QtWidgets.QAction(mainWindow)
        self.check_update.setObjectName("check_update")
        self.use_proxy_universalis = QtWidgets.QAction(mainWindow)
        self.use_proxy_universalis.setCheckable(True)
        self.use_proxy_universalis.setEnabled(True)
        self.use_proxy_universalis.setObjectName("use_proxy_universalis")
        self.filter_item = QtWidgets.QAction(mainWindow)
        self.filter_item.setCheckable(True)
        self.filter_item.setChecked(True)
        self.filter_item.setObjectName("filter_item")
        self.server_luxingniao.addAction(self.select_server_luxingniao)
        self.server_luxingniao.addAction(self.select_server_hongyuhai)
        self.server_luxingniao.addAction(self.select_server_shenyizhidi)
        self.server_luxingniao.addAction(self.select_server_lanuoxiya)
        self.server_luxingniao.addAction(self.select_server_huanyignqundao)
        self.server_luxingniao.addAction(self.select_server_mengyachi)
        self.server_luxingniao.addAction(self.select_server_yuzhouheyin)
        self.server_luxingniao.addAction(self.select_server_woxianxiran)
        self.server_luxingniao.addAction(self.select_server_chenxiwangzuo)
        self.server_moguli.addAction(self.select_server_moguli)
        self.server_moguli.addAction(self.select_server_baiyinxiang)
        self.server_moguli.addAction(self.select_server_baijinhuanxiang)
        self.server_moguli.addAction(self.select_server_shenquanhen)
        self.server_moguli.addAction(self.select_server_chaofengting)
        self.server_moguli.addAction(self.select_server_lvrenzhanqiao)
        self.server_moguli.addAction(self.select_server_fuxiaozhijian)
        self.server_moguli.addAction(self.select_server_longchaoshendian)
        self.server_moguli.addAction(self.select_server_mengyubaojing)
        self.server_maoxiaopang.addAction(self.select_server_maoxiaopang)
        self.server_maoxiaopang.addAction(self.select_server_zishuizhanqiao)
        self.server_maoxiaopang.addAction(self.select_server_yanxia)
        self.server_maoxiaopang.addAction(self.select_server_jingyuzhuagnyuan)
        self.server_maoxiaopang.addAction(self.select_server_moduna)
        self.server_maoxiaopang.addAction(self.select_server_haimaochawu)
        self.server_maoxiaopang.addAction(self.select_server_roufenghaiwan)
        self.server_maoxiaopang.addAction(self.select_server_hupoyuan)
        self.server_doudouchai.addAction(self.select_server_doudouchai)
        self.server_doudouchai.addAction(self.select_server_shuijingta)
        self.server_doudouchai.addAction(self.select_server_yinleihu)
        self.server_doudouchai.addAction(self.select_server_taiyanghaian)
        self.server_doudouchai.addAction(self.select_server_yixiujiade)
        self.server_doudouchai.addAction(self.select_server_hongchachuan)
        self.server.addAction(self.select_server_all)
        self.server.addAction(self.server_luxingniao.menuAction())
        self.server.addAction(self.server_moguli.menuAction())
        self.server.addAction(self.server_maoxiaopang.menuAction())
        self.server.addAction(self.server_doudouchai.menuAction())
        self.about.addAction(self.use_static_file)
        self.about.addAction(self.use_proxy_universalis)
        self.about.addAction(self.filter_item)
        self.about.addAction(self.check_update)
        self.menubar.addAction(self.server.menuAction())
        self.menubar.addAction(self.about.menuAction())

        self.retranslateUi(mainWindow)
        self.show_data_box.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "猴面雀 - FF14市场查询工具"))
        self.item_icon.setText(_translate("mainWindow", "物品图片 "))
        self.jump_to_wiki.setText(_translate("mainWindow", "在灰机wiki中查看"))
        self.show_cost.setText(_translate("mainWindow", "成本计算"))
        self.back_query.setText(_translate("mainWindow", "查询其他"))
        self.query_history.setText(_translate("mainWindow", "历史查询"))
        self.show_text_uptime.setText(_translate("mainWindow", "数据更新时间："))
        self.show_update_time.setText(_translate("mainWindow", "N/A"))
        self.show_text_server.setText(_translate("mainWindow", "当前查询服务器："))
        self.show_server.setText(_translate("mainWindow", "猫小胖"))
        self.server.setTitle(_translate("mainWindow", "服务器"))
        self.server_luxingniao.setTitle(_translate("mainWindow", "陆行鸟"))
        self.server_moguli.setTitle(_translate("mainWindow", "莫古力"))
        self.server_maoxiaopang.setTitle(_translate("mainWindow", "猫小胖"))
        self.server_doudouchai.setTitle(_translate("mainWindow", "豆豆柴"))
        self.about.setTitle(_translate("mainWindow", "其他"))
        self.select_server_all.setText(_translate("mainWindow", "国服"))
        self.select_server_hongyuhai.setText(_translate("mainWindow", "红玉海"))
        self.select_server_shenyizhidi.setText(_translate("mainWindow", "神意之地"))
        self.select_server_lanuoxiya.setText(_translate("mainWindow", "拉诺西亚"))
        self.select_server_huanyignqundao.setText(_translate("mainWindow", "幻影群岛"))
        self.select_server_mengyachi.setText(_translate("mainWindow", "萌芽池"))
        self.select_server_yuzhouheyin.setText(_translate("mainWindow", "宇宙和音"))
        self.select_server_woxianxiran.setText(_translate("mainWindow", "沃仙曦染"))
        self.select_server_chenxiwangzuo.setText(_translate("mainWindow", "晨曦王座"))
        self.select_server_baiyinxiang.setText(_translate("mainWindow", "白银乡"))
        self.select_server_baijinhuanxiang.setText(_translate("mainWindow", "白金幻象"))
        self.select_server_shenquanhen.setText(_translate("mainWindow", "神拳痕"))
        self.select_server_chaofengting.setText(_translate("mainWindow", "潮风亭"))
        self.select_server_lvrenzhanqiao.setText(_translate("mainWindow", "旅人栈桥"))
        self.select_server_fuxiaozhijian.setText(_translate("mainWindow", "拂晓之间"))
        self.select_server_longchaoshendian.setText(_translate("mainWindow", "龙巢神殿"))
        self.select_server_mengyubaojing.setText(_translate("mainWindow", "梦羽宝境"))
        self.select_server_zishuizhanqiao.setText(_translate("mainWindow", "紫水栈桥"))
        self.select_server_yanxia.setText(_translate("mainWindow", "延夏"))
        self.select_server_jingyuzhuagnyuan.setText(_translate("mainWindow", "静语庄园"))
        self.select_server_moduna.setText(_translate("mainWindow", "摩杜纳"))
        self.select_server_haimaochawu.setText(_translate("mainWindow", "海猫茶屋"))
        self.select_server_roufenghaiwan.setText(_translate("mainWindow", "柔风海湾"))
        self.select_server_hupoyuan.setText(_translate("mainWindow", "琥珀原"))
        self.select_server_shuijingta.setText(_translate("mainWindow", "水晶塔"))
        self.select_server_shuijingta.setToolTip(_translate("mainWindow", "水晶塔"))
        self.select_server_yinleihu.setText(_translate("mainWindow", "银泪湖"))
        self.select_server_yinleihu.setToolTip(_translate("mainWindow", "银泪湖"))
        self.select_server_taiyanghaian.setText(_translate("mainWindow", "太阳海岸"))
        self.select_server_taiyanghaian.setToolTip(_translate("mainWindow", "太阳海岸"))
        self.select_server_yixiujiade.setText(_translate("mainWindow", "伊修加德"))
        self.select_server_yixiujiade.setToolTip(_translate("mainWindow", "伊修加德"))
        self.select_server_hongchachuan.setText(_translate("mainWindow", "红茶川"))
        self.select_server_hongchachuan.setToolTip(_translate("mainWindow", "红茶川"))
        self.select_server_luxingniao.setText(_translate("mainWindow", "陆行鸟(全区服)"))
        self.select_server_moguli.setText(_translate("mainWindow", "莫古力(全区服)"))
        self.select_server_maoxiaopang.setText(_translate("mainWindow", "猫小胖(全区服)"))
        self.select_server_doudouchai.setText(_translate("mainWindow", "豆豆柴(全区服)"))
        self.use_static_file.setText(_translate("mainWindow", "使用静态资源加速"))
        self.check_update.setText(_translate("mainWindow", "关于"))
        self.use_proxy_universalis.setText(_translate("mainWindow", "使用反向代理查询价格"))
        self.filter_item.setText(_translate("mainWindow", "过滤不可在市场出售的物品"))
