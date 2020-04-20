from abc import ABC

from PyQt5.QtCore import QRunnable, pyqtSlot, QThreadPool, pyqtSignal, QObject
from sklearn.datasets import make_classification
from Model.config import TrainingConfig
from View.NeuralNetworkView import *
from Model.NeuralNetworkModel import *
from Controller.Controller import *


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
        self.view.show()
        self.neural_model.after_epochs_end_callback = self
        self.thread_pool = QThreadPool()

    def on_start_button_click(self):
        ##TODO Удалить это после реализации загрузки датасета
        X, y = make_classification(n_samples=100000, n_features=20, n_informative=3, n_redundant=2, n_repeated=0,
                                   n_classes=3, n_clusters_per_class=2, weights=None, flip_y=0.01, class_sep=1.0,
                                   hypercube=True, shift=0.0, scale=1.0, shuffle=True, random_state=3)
        ##TODO Удалить это после реализации загрузки датасета
        #############################
        self.neural_model.setDataset(inputArray=X, realClass=y)
        ###################Установка параметров автоматически
        self.neural_model.setParams(layer_count=3,  # int(self.view.ui.LayerCountLineEdit.text()),
                                    neuron_counter=[20, 24, 3],
                                    activation_function=["", "RELU", "Softmax"],
                                    kernel_init=["", "SVD", "He_normal"])


        train_config = TrainingConfig(
            epochs=int(self.view.ui.epoch_SpBox.text()),
            loss_func="sparse_categorical_crossentropy",
            metrics=["accuracy"],
            optimizer="sgd",
        )

        worker = Worker(self.neural_model, self.view)
        self.neural_model.setTrainConfig(train_config)
        self.thread_pool.start(worker)

    def on_load_button_click(self):
        self.neural_model.load_model(path=str(self.view.ui.ann_loader.path_line_edit.text()))
        self.view.ui.ann_loader.close()
        weights = list()
        for layer in range(np.size(self.neural_model.model.layers)):
            weights.append(self.neural_model.model.get_layer(index=layer).get_weights())
        self.view.draw_struct(weights_model=weights)

    def on_save_button_click(self):
        self.neural_model.save_model(path=str(self.view.ui.save_wgt.path_line_edit.text()))
        self.view.ui.save_wgt.close()

    def on_train_end(self, logs={}):
        weights = list()
        for layer in range(np.size(self.model.layers)):
            weights.append(self.model.get_layer(index=layer).get_weights())
        self.view.draw_struct(weights_model=weights)


    def on_epoch_end(self, batch, logs={}):
        weights = list()
        if self.counter == 2:
            for layer in range(np.size(self.model.layers)):
                weights.append(self.model.get_layer(index=layer).get_weights())
            self.view.draw_struct(weights_model=weights)
            self.counter = 0
            self.struct = [self.model.get_layer(index=0).get_weights(), self.model.get_layer(index=1).get_weights()]
            self.flag = True
        else:
            self.counter = self.counter + 1

    def get_struct(self):
        self.flag = False
        return self.struct


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
            # было это, но теперь так не поканает. Посмотри что тебе приходит в конце обучения ожной эпохи
            # может быть оттуда сможешь достать данные. Ну короче поковыряй
            # data_loss, data_acc = self.neural_model.get_history()
            # self.view.plot(data_loss=data_loss, data_acc=data_acc)
            history = self.neural_model.trainNeuralNetwork().history
            metrics = self.neural_model.get_metrics()
            self.view.plot(data_loss=history["loss"], data_acc=history["accuracy"])
            self.view.metrics_vizualization(metric=metrics)
        finally:
            self.signals.finished.emit()


class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
