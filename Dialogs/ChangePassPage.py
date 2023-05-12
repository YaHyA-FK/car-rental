from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QLineEdit
from Helpers.MessageBox import msgbox
import bcrypt


class ChangePassDialog(QDialog):
    def __init__(self, db, email, parent=None):
        super().__init__(parent)
        loadUi("./UI/changepass_D.ui", self)
        self.db = db
        self.email = email
        self.passline.setEchoMode(QLineEdit.Password)
        self.conline.setEchoMode(QLineEdit.Password)
        self.changep.clicked.connect(self.changepass)
        self.cancelp.clicked.connect(self.reject)

    def changepass(self):
        password = self.passline.text()
        if password != self.conline.text():
            msgbox("Error", "The pass and confirmation are not the same")
        elif len(password) < 7:
            msgbox("Error", "Password has to be at least 8 chars long")
        else:
            bytess = password.encode('utf-8')
            salt = bcrypt.gensalt()
            hashh = bcrypt.hashpw(bytess, salt)
            res = self.db.changepass(self.email, str(hashh))
            self.db.commit()
            if res > 0:
                self.accept()
