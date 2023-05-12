from PyQt5.QtWidgets import QDialog
from UI.emailgetter import Ui_Dialog


class EmailGetterDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def getemail(self):
        return self.ui.emailline.text()
