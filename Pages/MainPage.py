from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from Database.CarRental_database import CarRentalDB
from Helpers.MessageBox import msgbox
from Dialogs.LoginPage import LoginDialog
from Pages.CarPage import CarPage
from Helpers.ImageLabel import getImageLabel
from Pages.SignUpPage import SignupWindow
import bcrypt


class MainWindow(QDialog):
    def __init__(self, widget):
        super(MainWindow, self).__init__()
        loadUi("./UI/tabw.ui", self)
        self.widget = widget
        self.currentuser = "Guest"
        self.db = CarRentalDB()
        self.carpagecounter = 0
        self.cars = []
        self.selected = None
        self.loaddata()
        self.loadparametrs()
        self.Filter.clicked.connect(self.filter)
        self.loginbutton.clicked.connect(self.login)
        self.tableWidget.itemClicked.connect(self.select)
        self.reserveButton.clicked.connect(self.switchpage)
        self.Signupbtnpush.clicked.connect(self.signupfunction)
    def loaddata(self):
        self.cars = self.db.getallcars()
        carids = [self.cars[0] for self.cars in self.cars]
        for car in carids:
            self.db.checkCarState(int(car))
        self.cars = self.db.getallcars()
        self.showdata(self.cars)

    def loaddata2(self, marque, modele, carburant, place, transmission, prix):
        self.cars = self.db.getsomecars(marque, modele, carburant, place, transmission, prix)
        self.showdata(self.cars)

    def loadparametrs(self):
        marque = self.marque
        carburant = self.carburant
        transmission = self.transmission
        marques = self.db.getmarques()
        transmissions = self.db.gettransmissions()
        carburants = self.db.getcarburants()
        for choice in marques:
            marque.addItem(choice[0])
        for choice in transmissions:
            transmission.addItem(choice[0])
        for choice in carburants:
            carburant.addItem(choice[0])

    def showdata(self, cars):
        for row_number, row_data in enumerate(cars):
            self.tableWidget.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                item = str(column_data)
                if column_number == 1:
                    item = getImageLabel(self, column_data)
                    self.tableWidget.setCellWidget(row_number, column_number, item)
                elif column_number == 7:
                    if item == "1":
                        self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem("Available"))
                    else:
                        self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem("Reserved"))
                else:
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(item))
        self.tableWidget.verticalHeader().setDefaultSectionSize(80)

    def filter(self):
        marque = self.marque.currentText()
        modele = self.modele.text()
        carburant = self.carburant.currentText()
        place = self.place.text()
        transmission = self.transmission.currentText()
        prix = self.prix.text()
        if marque == "none" and transmission == "none" and carburant == "none" and prix == "" and place == "" and modele == "":
            self.cleartable()
            self.loaddata()
        else:
            self.cleartable()
            self.loaddata2(marque, modele, carburant, place, transmission, prix)

    def select(self):
        self.selected = self.tableWidget.currentRow()

    def switchpage(self):
        if self.currentuser != "Guest":
            if self.selected is not None:
                carpage = CarPage(self)
                self.carpagecounter += 1
                self.widget.addWidget(carpage)
                self.widget.setCurrentIndex(self.carpagecounter)
            else:
                msgbox("Error", "Select a car")
        else:
            msgbox("Error", "You have to sign in")


    def login(self):
        logdialog = LoginDialog(db=self.db)
        logdialog.setFixedHeight(400)
        logdialog.setFixedWidth(711)
        logdialog.setWindowTitle("Login Page")
        response = logdialog.exec()
        if response:
            email = logdialog.getemail()
            password = logdialog.getpassword()
            user = self.db.login(email)
            global userid
            userid = user[0]
            if user:
                password = password.encode('utf-8')
                hashed = user[4]
                hashed = hashed.encode('utf-8')
                if bcrypt.checkpw(password, hashed):
                    self.currentuser = user
                    self.loginbutton.move(1500, 1500)
                    self.Signupbtnpush.move(1500, 1500)
                    txt = "Good Morning " + user[2] + " " + user[1] + "!"
                    self.label.setText(txt)
                else:
                    msgbox("Login", "Password Incorrect")
            else:
                msgbox("Login", "Cannot login")

    def cleartable(self):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(
            ['Id', 'Image', 'Marque', 'Modele', 'Carburant', 'Places', 'Transmission', 'State', 'Price per day'])

    def signupfunction(self):
        signupdialog = SignupWindow()
        response = signupdialog.exec()
        if response:
            data = signupdialog.datagets()
            self.db.Signup(data)
            self.db.commit()
            msgbox("Account Created", "Your account has been created!")
