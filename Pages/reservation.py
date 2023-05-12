from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog


class ReservationDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("./UI/reservation.ui", self)

        self.reserve.clicked.connect(self.Reserve)
        self.cancel.clicked.connect(self.reject)

    def Reserve(self):
        # Days Conditions
        self.accept()

    def getDays(self):
        return int(self.days.text())
