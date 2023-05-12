from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog
from Helpers.EmailSender import SendEmail
from Helpers.CodeGenerator import get_random_string



class CodeSenderDialog(QDialog):
    def __init__(self, email, parent=None):
        super().__init__(parent)
        loadUi("./UI/sendcode_D.ui", self)
        self.code = get_random_string(8)
        self.email = email
        self.sendcode()
        self.resend.clicked.connect(self.sendcode)

    def sendcode(self):
        self.resend.setEnabled(False)
        SendEmail(self.email, "Verification code to reset password", '<strong>Your Code Is: ' + self.code + '</strong>')
        self.resend.setEnabled(True)

    def getcode(self):
        return self.code

    def getcodeentered(self):
        return self.codelab.text()
