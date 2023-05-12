def getallcars(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT id,image,marque,modele,carburant,places,transmission,state,prixParJour FROM voiture")
    return mycursor.fetchall()


def getsomecars(db, marque, modele, carburant, place, transmission, prix):
    mycursor = db.cursor()
    sql = "SELECT id,image,marque,modele,carburant,places,transmission,state,prixParJour FROM voiture WHERE"
    if marque != "none":
        sql += f" lower(marque) like '{marque.lower()}' AND"
    if modele != "":
        sql += f" lower(modele) like '{modele.lower()}' AND"
    if carburant != "none":
        sql += f" lower(carburant) like '{carburant.lower()}' AND"
    if place != "":
        sql += f" lower(places) like '{place.lower()}' AND"
    if transmission != "none":
        sql += f" lower(transmission) like '{transmission.lower()}' AND"
    if prix != "":
        sql += f" prixParJour <= {prix} AND"
    if sql.endswith("AND"):
        sql = sql[:-4]
        print(sql)
    mycursor.execute(sql)
    return mycursor.fetchall()

def changestate(db,carid,number):
    mycursor = db.cursor()
    if number:
        sql=f"UPDATE voiture SET state = '0' WHERE id ={carid}"
        mycursor.execute(sql)
        db.commit()
    else:
        sql=f"UPDATE voiture SET state = '1' WHERE id ={carid}"
        mycursor.execute(sql)
        db.commit()


def getallmarques(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT distinct marque FROM voiture where marque IS NOT NULL")
    return mycursor.fetchall()


def getalltransmissions(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT distinct transmission  FROM voiture where transmission is not NULL")
    return mycursor.fetchall()


def getallcarburants(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT distinct carburant  FROM voiture where carburant is not NULL")
    return mycursor.fetchall()

