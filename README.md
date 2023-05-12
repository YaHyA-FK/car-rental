
# Application de location de voitures

## Introduction

Nous visons à développer une application de gestion de location de voiture.

✔ Nous avons utilisé une approche orientée objet pour faciliter la maintenance et l'évolutivité du code.

✔ Nous stockons les informations sur la voiture et l'utilisateur dans une base de données relationnelle.

✔ Nous avons créé une interface utilisateur conviviale pour faciliter l'utilisation de l'application.

Table des matières
=================


   * [Inroduction](#Introduction)
   * [Fonctionnalités](#Fonctionnalités)
   * [Technologies](#Technologies)
   * [Auteurs](#Auteurs)
   * [Installation](#Installation)
   * [Diagramme de cas d'utilisation](#Diagramme-de-cas-d'utilisation)
   * [Diagramme de classe](#Diagramme-de-classe)
   * [Consultaion des voitures](#Consultaion-des-voitures)
   * [Sign Up](#Sign-Up)
   * [Sign In](#Sign-In)
   * [Mot de passe oublier](#Mot-de-passe-oublier)
   * [le Remplissage des QComboBox](#le-Remplissage-des-QComboBox)
   * [Filtrage](#Filtrage)
   * [Fonction du Filtrage](#Fonction-du-Filtrage)
   * [Reservation](#Reservation)
   * [Verifier les Reservation](#Verifier-les-Reservation)


## Fonctionnalités

➖ L'application permet aux utilisateurs de créer un compte avec un e-mail et un mot de passe. Elle vérifie l'e-mail en lui envoyant un code.

➖ Permet aux utilisateurs de se connecter avec leur email et leur mot de passe.

➖ Permet aux utilisateurs de réinitialiser leur mot de passe à l'aide de leur adresse e-mail.

➖ Affiche les voitures avec tous les détails dans la page principale.

➖ L'utilisateur peut filtrer les voitures par marque, modèle, carburant, lieux, transmission ou prix par jour.

➖ l'utilisateur peut sélectionner une voiture, aller sur sa page et la réserver.

## Technologies

* **pyqt5:** PyQt est une bibliothèque qui vous permet d'utiliser le framework Qt GUI de Python.

* **mysql:** MySQL est un systéme de gestion de base de données.

* **SendGrid:** nous permet d'envoyer des e-mails sans avoir à maintenir des serveurs de messagerie.

* **Adobe Photoshop:** utilisé pour créer l'interface de l'application.

## Auteurs

- [@Bilal Motassim](https://www.github.com/Rolerdxx)
- [@Hamza Elbouzidi](https://www.github.com/Hamza-Elbouzidi)
- [@Yahya Fekrane](https://www.github.com/YaHyA-FK)


## Installation

cloner le projet

```bash
  git clone https://github.com/Rolerdxx/Car-Rental.git
```

Aller dans le répertoire du projet

```bash
  cd Car-Rental
```

Installer l'environnement virtuel python:

```bash
  python3 -m venv venv
```

Exécutez l'environnement virtuel:

```bash
  ./venv/Scripts/activate
```

si vous rencontrez une erreur d'autorisation, exécutez cette commande et réessayez:

```bash
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Lorsque vous êtes dans l'environnement virtuel, exécutez la commande suivante pour installer tous les packages:

```bash
  pip install -r requirements.txt
```

Importez ceci dans la base de données sur votre serveur mysql:

- [CarRental](https://drive.google.com/file/d/1eN3Br_AKC32_MxGc4jAwT8MxK_w7zsWx/view?usp=sharing)

Pour exécuter ce projet, vous devrez ajouter les variables d'environnement suivantes à votre fichier .env :

- [.env](https://drive.google.com/file/d/1608vGivclNjdVUZhPBUzuGLRsOoqVt_r/view?usp=share_link)

Exécutez l'application:

```bash
  py main.py
```

Login test:

* **email**: c
* **password**: d


    
## Diagramme de cas d'utilisation

  ![](https://i.imgur.com/Nm6Hx2Y.png)

## Diagramme de classe

  ![](https://i.imgur.com/JjoBUPf.png)

## Consultaion des voitures
* Diagramme de sequence:

  ![](https://i.imgur.com/HBH13wT.png)

* lorsque l'utilisateur ouvre l'application, il demande toutes les voitures de `mysql` et les affiche dans un `TableWidget`

  ![](https://i.imgur.com/JFBIW9p.png)

* La fonction qui récupère toutes les voitures de la base de données:

```python
def getallcars(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT id,image,marque,modele,carburant,places,transmission,state,prixParJour FROM voiture")
    return mycursor.fetchall()
```

* La fonction qui affiche les données dans le `TableWidget`, la fonction `getImageLabel` Transforme les octets de l'image en une `QLabel` qui peut être affichée dans le tableau:

```python
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
```







## Sign In

* diagramme de sequence

  ![](https://i.imgur.com/rZecaoq.png)

* Image du fenetre

  ![](https://i.imgur.com/LcRC9MH.png)


* l'utilisateur remplit les champs email et mot de passe et clique sur ok, et quand il le fait l'application vérifie si l'email existe

```python
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
            if user:
                if CheckPass(password, user[4]):
                    self.currentuser = user
                    self.loginbutton.move(1500, 1500)
                    self.Signupbtnpush.move(1500, 1500)
                    txt = "Good Morning " + user[2] + " " + user[1] + "!"
                    self.label.setText(txt)
                else:
                    msgbox("Login", "Password Incorrect")
            else:
                msgbox("Login", "Cannot login")
```

* fonction `self.db.login(email)` renvoie les informations de l'utilisateur

```python
def login(db, email):
    mycursor = db.cursor()
    query = "SELECT * FROM userr WHERE email='" + email + "'"
    mycursor.execute(query)
    return mycursor.fetchone()
```

* si l'utilisateur existe, il compare le mot de passe avec le mot de passe chiffré renvoyé par la fonction `self.db.login()`.

* si le mot de passe est correct, il l'envoie à la page principale avec un message de bienvenue


## Mot de passe oublier

* Diagramme de sequence:

  ![](https://i.imgur.com/XgSmSf5.png)

* si l'utilisateur oublie son mot de passe, il peut le récupérer à l'aide de son e-mail, il doit d'abord cliquer sur le bouton `forgot password?` dans la page `SignIn`

* Fenêtre d'insertion d'email:

  ![](https://i.imgur.com/8Fsr1NB.png)

* l'utilisateur doit saisir son e-mail, l'application vérifie si l'e-mail existe, et si c'est le cas, elle lui envoie un e-mail avec un code à l'aide de l'API `SendGrid`.

* fonction de mot de passe oublier:

```python
    def forgotpass(self):
        emailgetter = EmailGetterDialog()
        res1 = emailgetter.exec()
        if res1:
            email = emailgetter.getemail()
            self.user = self.db.login(email)
            if self.user is not None:
                codesender = CodeSenderDialog(email=email)
                res = codesender.exec()
                if res:
                    if codesender.getcode() == codesender.getcodeentered():
                        changepass = ChangePassDialog(email=email, db=self.db)
                        res = changepass.exec()
                        if res:
                            msgbox("Success", "Pass changed")
                        else:
                            msgbox("Error", "something went wrong")
            else:
                msgbox("Error", "User doesnt exist")
```

* `CodeSender`, cette boîte de dialogue génère un code et lui envoie l'e-mail:

  ![](https://i.imgur.com/8P5PWiF.png)

* `get_random_string` fonction, il génère des lettres aléatoires avec une longueur donnée:

```python
def get_random_string(length):
    letters = string.ascii_uppercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
```

* `SendEmail` fonction, il envoie un e-mail à l'aide d'une API `sendGrid`, il prend `towho`, `subject`, `message` comme paramètres:

```python
def SendEmail(towho, subject, message):
    message = Mail(
        from_email='carrentalapp123@gmail.com',
        to_emails=towho,
        subject=subject,
        html_content=message)
    sg = SendGridAPIClient(api_key=os.getenv("emailkey"))
    sg.send(message)
```

* si le code est correct, il l'amène à la page `ChangePassPage`:

   ![](https://i.imgur.com/YFC2S0a.png)



## Sign Up

* Diagramme de sequence:

  ![](https://i.imgur.com/n1aOviL.png)

* Fenetre `SignUp`:

  ![](https://i.imgur.com/U1U6ylC.png)

* En tant que groupe, nous avons développé une interface graphique d'inscription en utilisant `PyQt5` pour notre projet informatique. Le code présenté est une classe `SignupWindow` qui hérite de la classe `QDialog` de la bibliothèque `PyQt`. Cette classe est utilisée pour créer une fenêtre de dialogue de formulaire d'inscription à une application. Le constructeur `__init__` de la classe charge l'interface utilisateur de la fenêtre de dialogue à partir d'un fichier .ui en utilisant la méthode `loadUi()` de la bibliothèque `PyQt`. Il définit également le mode d'écho pour le champ de mot de passe de l'utilisateur en utilisant la méthode `setEchoMode()`. Les boutons de la fenêtre de dialogue sont connectés à des fonctions en utilisant la méthode `connect()`. Lorsque le bouton "S'inscrire" est cliqué, la fonction `passwordvalidation()` est appelée pour vérifier si les informations saisies par l'utilisateur sont valides. Si les informations sont valides, un message de réussite est affiché. Si les informations sont invalides, un message d'erreur est affiché. Le bouton "Annuler" est connecté à la méthode `reject()` pour fermer la fenêtre de dialogue sans enregistrer les informations saisies. Dans l'ensemble, cette classe est un élément clé de la fonctionnalité d'inscription de l'application et permet à l'utilisateur de saisir ses informations de manière sécurisée et de vérifier si elles sont valides avant de les enregistrer dans la base de données.

```python
class SignupWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("./UI/Singup.ui", self)
        self.mdpline.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Sibtn.clicked.connect(self.passwordvalidation)
        self.Cnclbtn.clicked.connect(self.reject)
```

* Nous avons une méthode nommée `datagets` qui récupère les données saisies par l'utilisateur dans les champs nommés `nomline`, `prline`, `mailine` et `mdpline` du formulaire. Les données saisies dans le champ `mdpline` sont d'abord encodées en bytes et le module bcrypt est utilisé pour générer un hash de mot de passe en utilisant une clé de hachage de sel. Les données sont stockées dans une liste et renvoyées.


```python
    def datagets(self):
        data = []
        data.append(self.nomline.text())
        data.append(self.prline.text())
        data.append(self.mailine.text())
        hashh = EncryptPass(self.mdpline.text())
        data.append(hashh)
        return data
```

* Nous avons mis en place une fonction de validation de mot de passe dans notre application `PyQt`. Cette fonction vérifie la validité de la saisie de l'utilisateur avant de procéder à l'inscription. Tout d'abord, nous vérifions si l'utilisateur a correctement saisi son nom, son prénom, son adresse e-mail et son mot de passe. Ensuite, nous vérifions si l'adresse e-mail saisie par l'utilisateur est valide en utilisant des expressions régulières. Le mot de passe saisi par l'utilisateur doit comporter au moins 8 caractères et contenir des lettres et des caractères en minuscules. Si toutes les conditions sont remplies, nous procédons à la vérification de l'e-mail en envoyant un code de vérification. Nous appelons une boîte de dialogue nommée `CodeSenderDialog`, qui envoie un code de vérification à l'adresse e-mail de l'utilisateur. Une fois que l'utilisateur saisit le code, nous le comparons à celui généré par notre système. Si les codes correspondent, le processus d'inscription se poursuit et l'utilisateur est ajouté à la base de données. Sinon, un message d'erreur est affiché et le processus d'inscription est interrompu.



```python
    def passwordvalidation(self):
        sipassword = self.mdpline.text()
        siname = self.nomline.text()
        siprenom = self.prline.text()
        simail = self.mailine.text()

        if siname == "":
            msgbox("Error", "last name line is empty")
        elif siprenom == "":
            msgbox("Error", "first name line is empty")
        elif not re.match(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', simail):
            msgbox("Error", "email invalid")
        elif len(sipassword) < 8:
            msgbox("Error", "password has to longer than 7 characters")
        elif sipassword.isdigit():
            msgbox("Error", "password should contain letters")
        elif sipassword.isupper():
            msgbox("Error", "password should contain lower characters")
        else:
            emailveri = CodeSenderDialog(email=simail)
            res = emailveri.exec()
            if res:
                if emailveri.getcode() == emailveri.getcodeentered():
                    self.accept()
                else:
                    msgbox("Error", "Wrong code")
            else:
                self.reject()
```

* la fonction `SignUp` qui stocke les données dans la base de données:

```python
def Signup(db, data):
    cursor = db.cursor()
    query = "INSERT INTO userr (nom,prenom,email,passwordEn) VALUES(%s, %s, %s, %s)"
    cursor.execute(query, data)
    db.commit()
    return cursor.rowcount
```

* `CodeSenderDialog`:

   ![](https://i.imgur.com/7AmoFnQ.png)


* Message d'erreur:

  ![](https://i.imgur.com/CnUhkR1.png)
## Filtrage
![](https://i.imgur.com/pkr6vzp.png)
### le Remplissage des QComboBox
* Pour remplir les QComboBox, nous avons décidé d'utiliser les données de ces champs à travers la base de données afin d'afficher uniquement les options disponibles dans notre base de données. Pour cela, nous avons utilisé une requête SQL `SELECT DISTINCT` pour obtenir toutes les marques présentes dans la base de données en éliminant les doublons.

```python
def getallmarques(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT distinct marque FROM voiture where marque IS NOT NULL")
    return mycursor.fetchall()
```
```python
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
```
* Ce code remplit les options de trois QComboBox à partir des données de la base de données. Les marques, transmissions et carburants disponibles dans la base de données sont récupérés en appelant les méthodes correspondantes sur l'objet "self.db", puis chaque option est ajoutée

### Fonction du Filtrage

* Pour le filtrage ona penser a utiliser une condition pour que le filtrage ne travaille que lorsque l’utilisateur choisir une option dans QComboBox ou taper des specifaction 

```python
if marque == "none" and transmission == "none" and carburant == "none" and prix == "" and place == "" and modele == "":
```

* si non le programme va prendre les donnees saisir par utilisateur est faire le traitement suivant :

```python
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

```
* La fonction se connecte à la base de données en utilisant la connexion fournie (`db.cursor()`), puis construit une requête SQL qui sélectionne des voitures à partir de la table `voiture` en fonction des critères de recherche fournis. La requête commence par la chaîne de caractères `"SELECT id,image,marque,modele,carburant,places,transmission,state,prixParJour FROM voiture WHERE"`, qui sélectionne les colonnes `id`, `image`, `marque`, `modele`, `carburant`, `places`, `transmission`, `state` et `prixParJour` de la table `voiture`.

* Ensuite, la fonction vérifie chaque critère de recherche pour voir s'il est renseigné ou non. Si un critère est renseigné, la fonction ajoute une condition à la requête SQL en utilisant la méthode `lower()` pour mettre en minuscule les valeurs de recherche et la clause `LIKE` pour chercher des correspondances partielles dans les colonnes de la table `voiture`. Si un critère n'est pas renseigné, la fonction ne l'ajoute pas à la requête SQL.

* Enfin, si un prix maximum est fourni, la fonction ajoute une condition supplémentaire pour s'assurer que seules les voitures dont le `prixParJour` est inférieur ou égal à ce prix maximum sont sélectionnées.

* Si la requête SQL se termine par la chaîne de caractères `"AND"`, la fonction la raccourcit en supprimant ces trois derniers caractères avec `sql = sql[:-4]`.

* Enfin, la fonction exécute la requête SQL en utilisant la méthode `execute()` sur le curseur, puis retourne tous les résultats de la requête avec `fetchall()`. 

##  Reservation
* diagramme de sequence:

![](https://i.imgur.com/NXvD684.png)

* Image:

![](https://i.imgur.com/lErxsOO.png)

* Pour réserver une voiture, sélectionnez-la et cliquez sur le bouton Reserve.
```python
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
```

* Cette méthode vérifie si un utilisateur est connecté ou non, et si une voiture a été sélectionnée avant de basculer vers une page de voiture `CarPage` dans une application avec une structure à onglets `QTabWidget`.

* Le cas où un utilisateur n'est pas connecté `self.currentuser == "Guest"` est géré avec un message d'erreur indiquant qu'il doit se connecter pour continuer. Le cas où une voiture n'est pas sélectionnée `self.selected is None` est également géré avec un message d'erreur indiquant qu'une voiture doit être sélectionnée pour continuer.

* Après la verification, le programme affiche les informations de la voiture sélectionnée.


  ![](https://i.imgur.com/LaTwqFh.png)

🏠 BACK BUTTON :

* Ce bouton sert à retourner à la page principale

📝 RESERVE IT :

* Ce buton sert a réserver la voiture sélectionnée 

* Apres le système affiche ce QDialog :

  ![](https://i.imgur.com/E4W8tMf.png)

```python
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

```

```python
def savereservation(db,carid,userid,priceperday,nbrDays):
    cursor = db.cursor()
    prix=calculTotalPrice(int(nbrDays),float(priceperday))
    sql = f"insert into reservations(date,nbrDays,iduser,idvoiture,prix) values(now(),{nbrDays},{userid},{carid},{prix}) "
    cursor.execute(sql)
    db.commit()

```

  ![](https://i.imgur.com/2z9MWSc.png)

* La première ligne de code extrait la statut du voiture et le stocke dans la variable `state`.

* La condition suivante vérifie si la variable `state` est égale à la chaîne de caractères `1`. signifie que la voiture est disponible. Si la voiture est disponible, une boîte de dialogue de réservation `ReservationDialog` est créée et affichée à l'utilisateur.

* Si l'utilisateur clique sur `OK` dans la boîte de dialogue de réservation, la méthode récupère le nombre de jours sélectionnés dans la boîte de dialogue à l'aide de la méthode `getDays()` de l'objet `revdialog`. Ensuite, la méthode utilise les informations stockées dans `currentuser`, ` carID`, et la variable `days` pour ajouter une réservation à la base de données.

* Avant d'ajouter la réservation, une autre boîte de dialogue est affichée pour confirmer le coût total de la réservation `ResCon`. Si l'utilisateur confirme le coût total en cliquant sur `OK`, la méthode ajoute la réservation en appelant la méthode `reservation` de l'objet `self.main.db` avec les informations nécessaires.

* la fonction `savereservation` permet d'ajouter une nouvelle réservation à la base de données en calculant le coût total de la réservation `calculTotalPrice`, en créant une requête SQL et en exécutant cette requête en utilisant un curseur sur la connexion à la base de données.

```python
def reservation(self,carid,userid,priceperday,nbrDays):
    changestate(self.db,carid,True)
    return savereservation(self.db,carid,userid,priceperday,nbrDays)
```

* N'oublions pas le changement de l'état de cette voiture à travers la fonction 'changestate', qui prend en paramètre la variable de la base de données et l'identifiant de la voiture ainsi que l'état à affecter.


```python
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
```

* La fonction commence par créer un curseur pour exécuter des requêtes `SQL` sur la base de données. Ensuite, elle utilise une instruction SQL pour mettre à jour l'état de la voiture dans la table `voiture` de la base de données en fonction de la valeur de `number` : si `number` est ` True ` , la voiture est marquée comme disponible `state = '1'`, sinon elle est marquée comme indisponible `state = '0'`. La fonction exécute ensuite la requête SQL à travers le curseur et committe les modifications apportées à la base de données.


## Verifier les Reservation
* diagramme de sequence:
  ![](https://i.imgur.com/dsknqv5.png)

* Avant chaque consultation des voitures, le système vérifie si toutes les réservations sont valides  a l’aide de :

```python
def loaddata(self):
    self.cars = self.db.getallcars()
    carids = [self.cars[0] for self.cars in self.cars]
    for car in carids:
        self.db.checkCarState(int(car))
    self.cars = self.db.getallcars()
    self.showdata(self.cars)
```

* Ce fragment de code permet de mettre à jour l'état de toutes les voitures dans une base de données a l’aide d’une boucle qui va parcourir tous les identifiants des voitures stockées dans `carids`. `checkCarState` est appelée avec l'identifiant de la voiture `car` en tant qu'argument, ce qui permet de mettre à jour l'état de la voiture dans la base de données. pour chaque voiture stockée dans la base de données, puis de récupérer la liste complète des voitures après la mise à jour. 


```python
def checkCarState(self,carid):
    dateFN=getDayOfResevationEnd(self.db,carid)
    if dateFN :
        currentDate = datetime.now().date()
        if currentDate >= dateFN:
            changestate(self.db,carid,False)
ReservationDelete(self.db,carid)

        else:
            print("car reserved !!!")
```


* La méthode `checkCarState` vérifie si une voiture est réservée ou non en fonction de sa date de fin de réservation `dateFN`. Elle prend en paramètre l'identifiant de la voiture `carid` dont l'état sera vérifié.

* La première étape de la méthode est d'appeler la fonction `getDayOfReservationEnd` pour récupérer la date de fin de réservation de la voiture. 

```python
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
```


* La fonction exécute une requête SQL pour récupérer les informations de réservation associées à la voiture. Si une réservation existe pour cette voiture, la fonction extrait le nombre de jours de location `nbrDays` et la date de début de la réservation `date` à partir du résultat de la requête. Elle calcule ensuite la date de fin de la réservation `newDateFN` en ajoutant le nombre de jours de location à la date de début de la réservation a l’aide de la function ` timedelta `.La fonction retourne la date de fin de la réservation `newDateFN` 

* Si une date de fin de réservation existe, la méthode continue son traitement en vérifiant si cette date est passée ou non.

* Si la date de fin de réservation est passée `c'est-à-dire que la date actuelle est supérieure ou égale à la date de fin de réservation`, la méthode appelle la fonction "changestate"qu’il était déjà mentionner dans la partie Reservation pour mettre à jour l'état de la voiture à indisponible `False` ainsi que la méthode appelle la fonction `ReservationDelete`.


```python
def ReservationDelete(db,carid) :
    cursor = db.cursor()
    sql = f"DELETE FROM reservations WHERE idvoiture={carid}"
    cursor.execute(sql)
    db.commit()
```

* La fonction ReservationDelete  supprime la ligne de la  `reservation` qui est l'identifiant de voiture donné en utilisant une instruction `SQL DELETE`.

* Si la date de fin de réservation n'est pas encore passée, la méthode affiche simplement un message indiquant que la voiture est réservée.
