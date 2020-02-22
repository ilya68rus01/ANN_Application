import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 280, 270)
        self.setWindowTitle('Pen styles')
        self.painter = QPainter()
        self.x = 5
        self.show()


    def paintEvent(self, e):
        self.painter.begin(self)
        self.drawLines()
        self.painter.end()


    def drawLines(self):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        self.painter.setPen(pen)
        self.painter.drawEllipse(100,100,self.x,self.x)
        self.x = self.x + 25
