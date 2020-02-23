#%matplotlib inline
#from PySide2.QtCore import Slot
#from sklearn.datasets import load_iris
#import PyQt5 as qt
#import PySide2
import sys
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtWidgets import QApplication
from Controller.NeuralNetworkController import *

def main():
    app = QApplication(sys.argv)

    # создаём модель
    model = NeuralNetworkModel()
    # Создаем представление
    view = NeuralNetworkView()

    # создаём контроллер и передаём ему ссылку на модель и отображение
    controller = NeuralNetworkController(model=model,view=view)
    view.setController(controller=controller)
    app.exec()


if __name__ == '__main__':
    sys.exit(main())
