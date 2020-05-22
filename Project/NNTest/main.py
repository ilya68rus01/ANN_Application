import sys

from PyQt5.QtWidgets import QApplication
from View.NeuralNetworkView import NeuralNetworkView
from Controller.NeuralNetworkController import NeuralNetworkController, NeuralNetworkModel


def main():
    app = QApplication(sys.argv)
    # Инициализация контроллера с заданием модели и представления
    NeuralNetworkController(model=NeuralNetworkModel(), view=NeuralNetworkView())
    app.exec()


if __name__ == '__main__':
    sys.exit(main())
