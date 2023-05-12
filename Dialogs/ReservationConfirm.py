from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog


class ResCon(QDialog):
    def __init__(self, total, parent=None):
        super().__init__(parent)
        loadUi("./UI/ReservConfirm.ui", self)
        self.label.setText("The total price is "+ str(total))
        self.no.clicked.connect(self.reject)
        self.yes.clicked.connect(self.accept)
