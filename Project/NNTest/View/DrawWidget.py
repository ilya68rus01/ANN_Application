import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen, QPixmap
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
        if self.mModified:
            pixmap = QPixmap(self.size())
            pixmap.fill(Qt.white)
            painter = QPainter(pixmap)
            painter.drawPixmap(0, 0, self.mPixmap)
            self.drawBackground(painter)
            self.mPixmap = pixmap
            self.mModified = False
        self.painter = QPainter(self)
        self.painter.drawPixmap(0, 0, self.mPixmap)

    def drawBackground(self, qp):
        func, kwargs = self.func
        if func is not None:
            kwargs["qp"] = qp
            func(**kwargs)

    def drawLines(self):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        self.painter.setPen(pen)
        self.painter.drawEllipse(100,100,self.x,self.x)
        self.x = self.x + 25
