from abc import ABC

from PyQt5.QtCore import QRunnable, pyqtSlot, QThreadPool, pyqtSignal, QObject
from sklearn.datasets import make_classification
from Model.config import TrainingConfig
from View.NeuralNetworkView import *
from Model.NeuralNetworkModel import *
from Controller.Controller import *
import re


class NeuralNetworkController(Controller, ABC, Callback):
    struct = None
    flag = False
    counter = 0

    def __init__(self, model: NeuralNetworkModel, view: NeuralNetworkView):
        super().__init__()
        self.view = view
        self.neural_model = model
        self.view.set_on_click_listener(lambda: self.on_start_button_click())
        self.view.set_save_click_listener(lambda: self.on_save_button_click())
        self.view.set_on_load_click_listener(lambda: self.on_load_button_click())
        self.view.set_on_validation_listener(lambda: self.on_validation())
        self.view.set_on_clear_button_click_listener(lambda: self.on_clear_button_listner())
        self.view.show()
        self.neural_model.after_epochs_end_callback = self
        self.thread_pool = QThreadPool()

    def on_start_button_click(self):
        dataset = self.view.ui.get_data()
        X = dataset.drop("predict", axis=1)
        X = X.to_numpy()
        y = dataset['predict'].to_numpy()
        try:
            self.neural_model.setDataset(inputArray=X, realClass=y)
            config = self.view.get_config()
            layer_count = int(self.view.ui.LayerCountLineEdit.text())
            neuron_counter = list()
            activation_func = list()
            kernel = list()
            for x, y, z in config:
                neuron_counter.append(int(x))
                activation_func.append(y)
                kernel.append(z)
            #####################################################
            # код для установки параметров из GUI
            self.neural_model.set_ANN_params(layer_count=layer_count,
                                             neuron_counter=neuron_counter,
                                             activation_function=activation_func,
                                             kernel_init=kernel)
            train_config = TrainingConfig(
                epochs=int(self.view.main_window.epoch_SpBox.text()),
                loss_func="sparse_categorical_crossentropy",
                metrics=["accuracy"],
                optimizer="sgd", )
            worker = Worker(self.neural_model, self.view)
            self.neural_model.set_train_config(train_config)
            self.thread_pool.start(worker)
        except ValueError as error:
            self.view.error_value_handler(error.args[0]+str(error.args[1])+error.args[2])

    def on_load_button_click(self):
        self.neural_model.load_model(path=str(self.view.main_window.ann_loader.path_line_edit.text()))
        self.view.main_window.ann_loader.close()
        weights = list()
        for layer in range(np.size(self.neural_model.model.layers)):
            weights.append(self.neural_model.model.get_layer(index=layer).get_weights())
        self.view.draw_ANN_architecture(weights_model=weights)

    def on_save_button_click(self):
        self.neural_model.save_model(path=str(self.view.main_window.save_wgt.path_line_edit.text()))
        self.view.main_window.save_wgt.close()

    def on_train_end(self, logs={}):
        weights = list()
        for layer in range(np.size(self.model.layers)):
            weights.append(self.model.get_layer(index=layer).get_weights())
        self.view.draw_ANN_architecture(weights_model=weights)

    def on_epoch_end(self, batch, logs={}):
        weights = list()
        if self.counter == 2:
            for layer in range(np.size(self.model.layers)):
                weights.append(self.model.get_layer(index=layer).get_weights())
            self.view.draw_ANN_architecture(weights_model=weights)
            self.counter = 0
            self.struct = [self.model.get_layer(index=0).get_weights(), self.model.get_layer(index=1).get_weights()]
            self.flag = True
        else:
            self.counter = self.counter + 1

    def on_validation(self):
        match = re.search('^[1-9]+', self.view.main_window.LayerCountLineEdit.text())
        if match:
            pass
        else:
            self.view.error_value_handler("Неверно указано количество слоев ИНС.")

    def on_clear_button_listner(self):
        self.__init__(model=NeuralNetworkModel(), view=NeuralNetworkView())

class Worker(QRunnable):

    def __init__(self, model: NeuralNetworkModel, view: NeuralNetworkView):
        super().__init__()
        self.neural_model = model
        self.view = view
        self.setAutoDelete(True)
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        try:
            history = self.neural_model.train_ANN().history
            metrics = self.neural_model.get_metrics()
            self.view.plot(data_loss=history["loss"], data_acc=history["accuracy"])
            self.view.metrics_vizualization(metric=metrics)
        finally:
            self.signals.finished.emit()


class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
