from  PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Paint")
        self.setGeometry(100,100,800,600)
        self.image =QImage(self.size(),QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.drawing=False
        self.brushSize=2
        self.brushColor=Qt.black
        self.lastPoint=QPoint()
        mainMenu=self.menuBar()
        fileMenu=mainMenu.addMenu("File")
        b_size=mainMenu.addMenu("Brush Size")
        b_color=mainMenu.addMenu("Brush Color")
        