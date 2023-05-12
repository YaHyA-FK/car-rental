from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from Dialogs.CodeSender import CodeSenderDialog
from Dialogs.EmailGetter import EmailGetterDialog
from Helpers.MessageBox import msgbox
from Dialogs.ChangePassPage import ChangePassDialog


# class dyal login dialog
class LoginDialog(QDialog):
    def __init__(self, db, parent=None):
        super().__init__(parent)
        loadUi("./UI/login_D.ui", self)
        self.passline.setEchoMode(QtWidgets.QLineEdit.Password)  # password kaywli kayban haka ****
        self.forgotbtn.clicked.connect(self.forgotpass)
        self.user = None
        self.db = db

    # hado katjib bihom data l window lkhra
    def getemail(self):
        return self.emailline.text()

    def getpassword(self):
        return self.passline.text()

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
