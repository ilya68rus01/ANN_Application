import sys

from PyQt5.QtWidgets import QApplication
from View.NeuralNetworkView import NeuralNetworkView
from Controller.NeuralNetworkController import NeuralNetworkController, NeuralNetworkModel


def main():
    app = QApplication(sys.argv)

    # создаём контроллер и передаём ему ссылку на модель и отображение
    NeuralNetworkController(model=NeuralNetworkModel(), view=NeuralNetworkView())
    app.exec()


if __name__ == '__main__':
    sys.exit(main())
