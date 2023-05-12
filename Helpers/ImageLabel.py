from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets


def getImageLabel(self, image):
    imageLabel = QtWidgets.QLabel(self)
    imageLabel.setText("")
    imageLabel.setScaledContents(True)
    pixmap = QPixmap()
    pixmap.loadFromData(image, 'jpg')
    imageLabel.setPixmap(pixmap)
    return imageLabel
