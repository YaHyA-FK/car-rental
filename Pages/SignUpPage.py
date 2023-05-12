import re
import bcrypt
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtWidgets
from Helpers.MessageBox import msgbox
from Dialogs.CodeSender import CodeSenderDialog


class SignupWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("./UI/Singup.ui", self)
        self.mdpline.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Sibtn.clicked.connect(self.passwordvalidation)
        self.Cnclbtn.clicked.connect(self.reject)

    def datagets(self):
        data = []
        data.append(self.nomline.text())
        data.append(self.prline.text())
        data.append(self.mailine.text())
        bytess = self.mdpline.text().encode('utf-8')
        salt = bcrypt.gensalt()
        hashh = bcrypt.hashpw(bytess, salt)
        data.append(str(hashh)[2:-1])
        return data

    def passwordvalidation(self):
        sipassword = self.mdpline.text()
        siname = self.nomline.text()
        siprenom = self.prline.text()
        simail = self.mailine.text()

        if siname == "":
            msgbox("Erreur", "nom vide")
        elif siprenom == "":
            msgbox("Erreur", "prenom vide")
        elif not re.match(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', simail):
            msgbox("Erreur", "forme email invalid")
        elif len(sipassword) < 8:
            msgbox("Erreur", "mot de passe moin de 8 car")
        elif sipassword.isdigit():
            msgbox("Erreur", "mot de passe doit contenir lettres")
        elif sipassword.isupper():
            msgbox("Erreur", "mot de passe doit contenir des miniscules")
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

