from View.MainWindow import *


class NeuralNetworkView(QtWidgets.QMainWindow):

    def __init__(self, ):
        super(NeuralNetworkView, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def plot(self, data_loss, data_acc):
        self.ui.plot_history(data_loss=data_loss, data_acc=data_acc)
        # self.ui.draw_model()

    def set_on_click_listener(self, action):
        self.ui.Start_Button.clicked.connect(action)

    def draw_struct(self,weights_model):
        self.ui.draw_model(weights=weights_model)
