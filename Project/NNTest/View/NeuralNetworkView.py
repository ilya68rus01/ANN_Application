from sklearn.datasets import make_classification
from Controller import Controller
import pyqtgraph as pg
from Controller.NeuralNetworkController import *
from View.MainWindow import *

class NeuralNetworkView(QtWidgets.QMainWindow):
    controller = Controller

    def __init__(self,):
        super(NeuralNetworkView, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Start_Button.clicked.connect(self.start_button_clicked)

    def start_button_clicked(self):
        X, y = make_classification(n_samples=100000, n_features=20, n_informative=3, n_redundant=2, n_repeated=0,
                                   n_classes=3, n_clusters_per_class=2, weights=None, flip_y=0.01, class_sep=1.0,
                                   hypercube=True, shift=0.0, scale=1.0, shuffle=True, random_state=42)
        print("Good 1")
        self.controller.setData(X=X,y=y)
        print("Good 2")
        self.controller.setModelParams(layer_count=int(self.ui.LayerCountLineEdit.text()),
                                       neuron_counter=[20, 3, 3],
                                       activation_function=["", "relu", "softmax"],
                                       kernel_init=["", "SVD", "zeros"])
        print("Good 3")
        self.controller.fitModel(epochs=int(self.ui.epoch_SpBox.text()),loss_func="sparse_categorical_crossentropy",metrics=["accuracy"],optimizer="sgd")
        print("Good 4")

    def plot(self,data_loss,data_acc):
        self.ui.plot_history(data_loss=data_loss,data_acc=data_acc)
        self.ui.drow_model()


    def setController(self,controller):
        self.controller = controller
