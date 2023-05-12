from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPixmap
from Pages.reservation import ReservationDialog
from Dialogs.ReservationConfirm import ResCon


class CarPage(QDialog):
    def __init__(self, main):
        super(CarPage, self).__init__()
        loadUi("./UI/carpage.ui", self)
        self.main = main
        self.car = main.cars[main.selected]
        self.backButton.clicked.connect(self.goback)
        self.reserveButton.clicked.connect(self.reserveit)
        self.filldata()

    def goback(self):
        self.main.widget.setCurrentIndex(0)

    def filldata(self):
        pixmap = QPixmap()
        pixmap.loadFromData(self.car[1], 'jpg')
        self.imagelabel.setPixmap(pixmap)
        self.marquelabel.setText(self.car[2])
        self.modelelabel.setText(self.car[3])
        self.carburantlabel.setText(self.car[4])
        self.placeslabel.setText(str(self.car[5]))
        self.transmissionlabel.setText(self.car[6])
        if str(self.car[7]) == "1":
            self.statelabel.setText("Available")
            self.statelabel.setStyleSheet("color:rgb(50,205,50)")
        else:
            self.statelabel.setText("Reserved")
            self.statelabel.setStyleSheet("color:rgb(255, 0, 0)")
        self.pricelabel.setText(str(self.car[8]) + " DH")

    def reserveit(self):
        state = str(self.car[7])
        if state == "1":
            revdialog = ReservationDialog()
            res = revdialog.exec()
            if res:
                days = revdialog.getDays()
                user = self.main.currentuser[0]
                carid = self.car[0]
                priceperday = self.car[8]
                rescon = ResCon(float(priceperday)*float(days))
                res2 = rescon.exec()
                if res2:
                    self.main.db.reservation(carid, user, priceperday, days)
