from View.MainWindow import *


class NeuralNetworkView(QtWidgets.QMainWindow):

    def __init__(self):
        super(NeuralNetworkView, self).__init__()
        self.main_window = Ui_MainWindow(self)

    def plot(self, data_loss, data_acc):
        self.main_window.plot_history(data_loss=data_loss, data_acc=data_acc)

    def draw_ANN_architecture(self, weights_model):
        self.main_window.draw_model(weights=weights_model)

    def metrics_vizualization(self, metric):
        self.main_window.write_metrics(data=metric)

    def set_on_click_listener(self, action):
        self.main_window.Start_Button.clicked.connect(action)

    def set_save_click_listener(self, action):
        self.main_window.save_wgt.open_button.clicked.connect(action)

    def set_on_load_click_listener(self, action):
        self.main_window.ann_loader.open_button.clicked.connect(action)

    def set_on_clear_button_click_listener(self, action):
        self.main_window.Clear_Button.clicked.connect(action)

    def set_on_validation_listener(self, action):
        self.main_window.epoch_SpBox.editingFinished.connect(action)
        self.main_window.LayerCountLineEdit.editingFinished.connect(action)

    def error_value_handler(self, message):
        self.main_window.dialog_window_error_value(message)

