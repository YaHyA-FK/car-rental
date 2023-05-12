import mysql.connector
from datetime import datetime
from Controllers.User_Controller import login, changepassword
from Controllers.Car_Controller import getallcars, getsomecars, getallmarques, getallcarburants, getalltransmissions

from Controllers.User_Controller import Signup

from Controllers.Car_Controller import changestate

from Controllers.reservationController import savereservation,getDayOfResevationEnd,ReservationDelete



class CarRentalDB:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="carrental"
    )

    def commit(self):
        self.db.commit()

    def login(self, email):
        return login(self.db, email)

    def getallcars(self):
        return getallcars(self.db)

    def getsomecars(self, marque, modele, carburant, place, transmission, prix):
        return getsomecars(self.db, marque, modele, carburant, place, transmission, prix)

    def getmarques(self):
        return getallmarques(self.db)

    def getcarburants(self):
        return getallcarburants(self.db)

    def gettransmissions(self):
        return getalltransmissions(self.db)

    def changepass(self, email, newpass):
        return changepassword(self.db, email, newpass)

    def Signup(self, data):
        return Signup(self.db, data)

    def reservation(self,carid,userid,priceperday,nbrDays):
        changestate(self.db,carid,True)
        return savereservation(self.db,carid,userid,priceperday,nbrDays)
    def checkCarState(self,carid):
        dateFN=getDayOfResevationEnd(self.db,carid)
        if dateFN :
            currentDate = datetime.now().date()
            if currentDate >= dateFN:
                changestate(self.db,carid,False)
                ReservationDelete(self.db,carid)
            else:
                print("car reserved !!!")

