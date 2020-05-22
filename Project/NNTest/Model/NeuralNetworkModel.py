import matplotlib as mpl
import matplotlib.pyplot as pltG
import numpy as np
import tensorflow as tf
from keras.callbacks import Callback
from tensorflow import keras
from sklearn.cluster import KMeans
from svd import *
from Model.WeightsCallback import *
from svd.svd import *


class NeuralNetworkModel:
    after_epochs_end_callback = Callback

    def __init__(self):
        self.model = None
        self.info = None
        self.activation_function_enum = {
            "RELU": keras.activations.relu,
            "Sigmoid": keras.activations.sigmoid,
            "ELU": keras.activations.elu,
            "Tangh": keras.activations.tanh,
            "Softmax": keras.activations.softmax,
            '': None
        }
        self.initializer_func_enum = {
            "Zeros": keras.initializers.Zeros,
            "Ones": keras.initializers.Ones,
            "RandomNormal": keras.initializers.RandomNormal,
            "RandomUniform": keras.initializers.RandomUniform,
            "TruncatedNormal": keras.initializers.TruncatedNormal,
            "Lecun_uniform": keras.initializers.lecun_uniform,
            "He_normal": 'he_normal',
            "Lecun_normal": 'lecun_normal',
            "He_uniform": keras.initializers.he_uniform,
            "SVD": self.SVD,
            '': None
        }

    def train_ANN(self):
        if self.model is None:
            self.__set_layer_params__()
        self.info = self.__learn_model__()
        return self.info

    def __set_layer_params__(self):
        self.model = keras.models.Sequential()
        i = 1
        self.model.add(keras.layers.Input(self.inputArray.shape[1]))
        while i != self.layer_count:
            self.model.add(keras.layers.Dense(self.neuron_in_layers[i], activation=self.activation_function[i],
                                              kernel_initializer=self.kernel_initializer_func[i]))
            i = i + 1

    def __learn_model__(self):
        self.model.compile(loss=self.loss, optimizer=self.optimizer, metrics=self.metrics)
        info = self.model.fit(self.inputArray, self.realClass, epochs=self.epochs,
                              validation_split=0.1, callbacks=[self.after_epochs_end_callback])
        return info

    # Собственная функция для инициализации весов
    def SVD(self, shape, dtype=None):
        class_array = list()
        real_class_value = self.__class_finder__()
        clustering_classes = list()
        self.__classification_algorithm__(class_array, real_class_value)
        for i in range(np.size(real_class_value)):
            clustering_classes.append(self.__clustering__(data=class_array[i]))
        output_massive = list()
        for i in range(np.shape(self.inputArray)[1]):
            massive = list()
            for j in range(np.size(real_class_value)):
                massive += clustering_classes[j][i]
            output_massive.append(massive)
        return output_massive

    def __class_finder__(self):
        real_class_value = list()
        real_class_value.append(self.realClass[0])
        # Обходим весь массив реальных классов и выбираем из них разные
        # если элемент отличается от нулевого добавляем в список классов, начинаем поиск нового, и т.д.
        for i in range(np.size(self.realClass)):
            for j in range(np.size(real_class_value)):
                if self.realClass[i] in real_class_value:
                    pass
                else:
                    real_class_value.append(self.realClass[i])
        sorted(real_class_value)
        return real_class_value

    def __classification_algorithm__(self, array_of_classes, real_class_value):
        # Разделяем весь набор данный по соответствующим классам
        for i in range(np.size(real_class_value)):
            array_of_classes.append(list())
            for j in range(np.size(self.realClass)):
                if self.realClass[j] == real_class_value[i]:
                    array_of_classes[i].append(self.inputArray[j])

    def __clustering__(self, data):
        mass1 = list()
        mass2 = list()
        mass3 = list()
        mass4 = list()
        mass5 = list()
        mass6 = list()
        mass7 = list()
        mass8 = list()
        cluster = KMeans(random_state=42)
        outClusters = cluster.fit(data)
        for x, i in zip(data, outClusters.labels_):
            if i == 0:
                mass1.append(x)
            elif i == 1:
                mass2.append(x)
            elif i == 2:
                mass3.append(x)
            elif i == 3:
                mass4.append(x)
            elif i == 4:
                mass5.append(x)
            elif i == 5:
                mass6.append(x)
            elif i == 6:
                mass7.append(x)
            elif i == 7:
                mass8.append(x)
        u, s, v = svd(mass1)
        print("Матрица U:",u)
        print("Матрица S:",s)
        print("Матрица V:",v)
        weights1, u, v = svd(mass1)
        weights2, u, v = svd(mass2)
        weights3, u, v = svd(mass3)
        weights4, u, v = svd(mass4)
        weights5, u, v = svd(mass5)
        weights6, u, v = svd(mass6)
        weights7, u, v = svd(mass7)
        weights8, u, v = svd(mass8)

        # weights1 = 2 * ((weights1 - min(weights1)) / (max(weights1) - min(weights1))) - 1
        # weights2 = 2 * ((weights2 - min(weights2)) / (max(weights2) - min(weights2))) - 1
        # weights3 = 2 * ((weights3 - min(weights3)) / (max(weights3) - min(weights3))) - 1
        # weights4 = 2 * ((weights4 - min(weights4)) / (max(weights4) - min(weights4))) - 1
        # weights5 = 2 * ((weights5 - min(weights5)) / (max(weights5) - min(weights5))) - 1
        # weights6 = 2 * ((weights6 - min(weights6)) / (max(weights6) - min(weights6))) - 1
        # weights7 = 2 * ((weights7 - min(weights7)) / (max(weights7) - min(weights7))) - 1
        # weights8 = 2 * ((weights8 - min(weights8)) / (max(weights8) - min(weights8))) - 1
        weights1 = (weights1 / max(weights1) - 0.5) / 0.5
        weights2 = (weights2 / max(weights2) - 0.5) / 0.5
        weights3 = (weights3 / max(weights3) - 0.5) / 0.5
        weights4 = (weights4 / max(weights4) - 0.5) / 0.5
        weights5 = (weights5 / max(weights5) - 0.5) / 0.5
        weights6 = (weights6 / max(weights6) - 0.5) / 0.5
        weights7 = (weights7 / max(weights7) - 0.5) / 0.5
        weights8 = (weights8 / max(weights8) - 0.5) / 0.5
        out = list()
        for x1, x2, x3, x4, x5, x6, x7, x8 in zip(weights1, weights2, weights3, weights4, weights5, weights6, weights7,
                                                  weights8):
            out.append(
                [np.float(x1), np.float(x2), np.float(x3), np.float(x4), np.float(x5), np.float(x6), np.float(x7),
                 np.float(x8)])
        return out

    def set_data_for_learning(self, inputArray, realClass):
        self.inputArray = inputArray[:70000]
        self.realClass = realClass[:70000]
        self.X_test = inputArray[70000:]
        self.y_test = realClass[70000:]

    def set_train_config(self, train_config):
        self.__setEpochs__(train_config.epochs)
        self.__setLoss__(train_config.loss_func)
        self.__setOptimizer__(train_config.optimizer)
        self.__setMetrics__(train_config.metrics)

    def __setEpochs__(self, epoch):
        self.epochs = epoch
        # try:
        #     if epoch > 0:
        #         self.epochs = epoch
        #     else:
        #         raise ValueError(epoch)
        # except ValueError as error:
        #     print("Не верное количество эпох:", error, " количество эпох, должно быть больше нуля.")

    def __setLoss__(self, loss_func):
        try:
            if type(loss_func) == str:
                self.loss = loss_func
            else:
                raise ValueError(loss_func)
        except ValueError as error:
            print("Неверно указанна функция потерь:", error)

    def __setOptimizer__(self, optimizer):
        try:
            if type(optimizer) == str:
                self.optimizer = optimizer
            else:
                raise ValueError(optimizer)
        except ValueError as error:
            print("Неверная функция активации:", error)

    def __setMetrics__(self, metric):
        # TODO Реализовать метод
        self.metrics = metric

    def set_ANN_params(self, layer_count, neuron_counter=[1], activation_function=["sigmoid"],
                       kernel_init=["random_uniform"]):
        self.__setLayer_count__(layer_count)
        self.__set_neuron_in_layers__(neuron_counter)
        self.__set_kernel_initializer__(kernel_init)
        self.__setActivationFunc__(activation_function)

    def __setLayer_count__(self, layer_count):
        if layer_count > 0:
            self.layer_count = layer_count
        else:
            raise ValueError("Не верное количество слоев.", layer_count, "Пропробуйте указать число больше 0.")
        # except ValueError as error:
        #     print("Не верное количество слоев:", error, ". Пропробуйте указать число больше 0.")

    def __set_neuron_in_layers__(self, neuron_count_in_layers):
        counter = np.array(neuron_count_in_layers, dtype=int)
        if counter.size == self.layer_count:
            self.neuron_in_layers = counter
        else:
            raise ValueError("Неверно указано колличество слоев в сети:", neuron_count_in_layers,
                             ". Количество слоев должно совпадать с указынным.")

    def __set_kernel_initializer__(self, kernel_init):
        kernel = np.array(kernel_init, dtype=str)
        self.kernel_initializer_func = []
        for init in kernel:
            try:
                self.kernel_initializer_func.append(self.initializer_func_enum[init])
            except KeyError as e:
                # можно также присвоить значение по умолчанию вместо бросания исключения
                raise ValueError('Undefined unit: {}'.format(e.args[0]))

    def __setActivationFunc__(self, activation_function):
        func_array = np.array(activation_function, dtype=str)
        self.activation_function = []
        for func in func_array:
            try:
                self.activation_function.append(self.activation_function_enum[func])
            except KeyError as e:
                # можно также присвоить значение по умолчанию вместо бросания исключения
                raise ValueError('Неверно указана функция активации: {}'.format(e.args[0]))

    def get_history(self):
        return [self.info.history['loss'], self.info.history['accuracy']]

    def get_metrics(self):
        data = self.model.evaluate(x=self.X_test, y=self.y_test)[1]
        print(data)
        return data

    def save_model(self, path=None):
        self.model.save(path)

    def load_model(self, path=None):
        self.model = keras.models.load_model(path)


