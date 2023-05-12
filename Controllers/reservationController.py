from datetime import datetime,timedelta
def savereservation(db,carid,userid,priceperday,nbrDays):
    cursor = db.cursor()
    prix=calculTotalPrice(int(nbrDays),float(priceperday))
    sql = f"insert into reservations(date,nbrDays,iduser,idvoiture,prix) values(now(),{nbrDays},{userid},{carid},{prix}) "
    cursor.execute(sql)
    db.commit()
def calculTotalPrice(nbrDays,prixperday):
    return nbrDays*prixperday

def getDayOfResevationEnd(db,carid):
    cursor = db.cursor()
    sql=f"select nbrDays,DATE_FORMAT(date, '%d-%m-%Y') from reservations where idvoiture={carid}"
    cursor.execute(sql)
    table=cursor.fetchall()
    if len(table)!= 0 :
        date=table[0][1]
        nbrDays=table[0][0]
        dateFN = datetime.strptime(date, '%d-%m-%Y').date()
        newDateFN = dateFN + timedelta(days=nbrDays)
        return newDateFN
def ReservationDelete(db,carid) :
    cursor = db.cursor()
    sql = f"DELETE FROM reservations WHERE idvoiture={carid}"
    cursor.execute(sql)
    db.commit()