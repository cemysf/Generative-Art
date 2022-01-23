from functools import partial
import sys
import random
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QShortcut
from PyQt5.QtGui import QKeySequence

from examples import draw_flow_field, draw_delta_body, draw_white_noise, draw_perlin, draw_vectors, draw_perlin_rounding

#####
GUI_WIDTH = 800
GUI_HEIGHT = 600
FUNC_TO_USE = partial(draw_flow_field, GUI_WIDTH, GUI_HEIGHT)
#####

class Canvas(QLabel):
    def mousePressEvent(self, event):
        self.parentWidget().generateArtwork()
        self.parentWidget().showArtwork()

    def keyPressEvent(self, event):
        print("key press", event)

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.width = GUI_WIDTH
        self.height = GUI_HEIGHT
        self.left = 10
        self.top = 10
        self.initUI()
    
    def generateArtwork(self):
        self.artwork = FUNC_TO_USE(seed=random.randint(0, 100000000), color=random.randint(0,360))

    def showArtwork(self):
        pixmap = self.artwork.getImage()
        self.canvas.setPixmap(pixmap)

    def initUI(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        # Create widget
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
    ex = App()
    sys.exit(app.exec_())