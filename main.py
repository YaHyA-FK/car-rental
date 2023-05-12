import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
import pyqtcss
from Pages.MainPage import MainWindow

style = open("./styles/QSS/AMOLED.qss", "r")
stylesheet = style.read()
style_string = pyqtcss.get_style("dark_orange")
65
app = QApplication(sys.argv)
app.setStyleSheet(stylesheet)
widget = QtWidgets.QStackedWidget()
mainwindow = MainWindow(widget)
widget.addWidget(mainwindow)
widget.setWindowTitle("Car Rental App")
widget.setWindowIcon(QtGui.QIcon('car-rental.png'))
widget.setFixedHeight(600)
widget.setFixedWidth(1067)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
