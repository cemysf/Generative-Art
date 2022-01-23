import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QShortcut
from PyQt5.QtGui import QKeySequence

from gui_experiments import FUNCTION_IN_USE

GUI_WIDTH = 800
GUI_HEIGHT = 600

class Canvas(QLabel):
    def mousePressEvent(self, event):
        self.parentWidget().generateArtwork()
        self.parentWidget().showArtwork()

class App(QWidget):
    def __init__(self, artFunc):
        super().__init__()
        self.width = GUI_WIDTH
        self.height = GUI_HEIGHT
        self.left = 10
        self.top = 10
        self.artFunc = artFunc
        self.initUI()
    
    def generateArtwork(self):
        self.artwork = self.artFunc.use(GUI_WIDTH, GUI_HEIGHT)

    def showArtwork(self):
        pixmap = self.artwork.getImage()
        self.canvas.setPixmap(pixmap)

    def initUI(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.canvas = Canvas(self)
        self.generateArtwork()
        self.showArtwork()
        # self.resize(pixmap.width(),pixmap.height())
        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q:
            self.close()


def printInfo():
    print(
"""
##### GUI #####
print q to exit
mouse click: create new image
###############
""")

if __name__ == '__main__':
    printInfo()
    app = QApplication(sys.argv)
    ex = App(FUNCTION_IN_USE)
    sys.exit(app.exec_())
