#%matplotlib inline
#from PySide2.QtCore import Slot
#from sklearn.datasets import load_iris
#import PyQt5 as qt
#import PySide2
import sys
from PyQt5 import QtCore,QtWidgets,QtGui
from sklearn.datasets import make_classification
from NeuralNetworkModel import *
from MainWindow import Ui_MainWindow

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.start_button_clicked)

    def start_button_clicked(self):
        X, y = make_classification(n_samples=100000, n_features=20, n_informative=3, n_redundant=2, n_repeated=0,
                                   n_classes=3, n_clusters_per_class=2, weights=None, flip_y=0.01, class_sep=1.0,
                                   hypercube=True, shift=0.0, scale=1.0, shuffle=True, random_state=42)
        nn = NeuralNetworkModel(X, y, layer_count=int(self.ui.LayerCountLineEdit.text()), neuron_counter=[20, 3, 3],
                                activation_function=["", "relu", "softmax"],
                                kernel_init=["", "SVD", "zeros"])  ## Вернуть SVD
        nn.setTrainConfig(epochs=int(self.ui.spinBox_2.text()) , loss_func="sparse_categorical_crossentropy", optimizer="sgd", metrics=["accuracy"])
        nn.trainNeuralNetwork()


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())



# app = QtWidgets.QApplication(sys.argv)
# MainWindow = QtWidgets.QMainWindow()
# ui = Ui_MainWindow()
# ui.setupUi(MainWindow)
# ui.pushButton.clicked.connect()
# #print(nn.model.get_layer(index=0).get_weights())
# MainWindow.show()
# sys.exit(app.exec_())


