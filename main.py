import query_item_id
from Paissa import Ui_mainWindow
import query_item_id
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

# class MainWindow(Ui_MainWindow):




app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QMainWindow()
ui = Ui_mainWindow()
ui.setupUi(widget)
widget.show()
query_item = query_item_id.Ui_query_item_id()
query_item.setupUi(ui.show_data_box)
sys.exit(app.exec_())

