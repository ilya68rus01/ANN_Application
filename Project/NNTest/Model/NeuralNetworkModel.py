import matplotlib as mpl
import matplotlib.pyplot as pltG
import numpy as np
import tensorflow as tf
from keras.callbacks import Callback
from tensorflow import keras
from sklearn.cluster import KMeans
from Model.WeightsCallback import *


class NeuralNetworkModel:
    after_epochs_end_callback = Callback

    def __init__(self):
        self.model = keras.models.Sequential()

    # Собственная функция для инициализации весов
    def SVD(self, shape, dtype=None):
        array_of_classes = list()  # Что-то вроде массива массивов в,
        # котором первый элемент включает в себя объекты "первого" класса
        class_val = list()  # Реальные значения классов 0,1,2,....
        class_val.append(self.realClass[0])
        # Обходим весь массив реальных классов и выбираем из них разные
        # если элемент отличается от нулевого добавляем в список классов, начинаем поиск нового, и т.д.
        for i in range(np.size(self.realClass)):
            for j in range(np.size(class_val)):
                if self.realClass[i] in class_val:
                    pass
                else:
                    class_val.append(self.realClass[i])
        sorted(class_val)
        # Разделяем весь набор данный по соответствующим классам
        for i in range(np.size(class_val)):  # Количество классов пока не известно и передавать в качесве параметра функции нельзя
            array_of_classes.append(list())
            #    array_of_classes[i] = list()
            for j in range(np.size(self.realClass)):
                if self.realClass[j] == class_val[i]:
                    array_of_classes[i].append(self.inputArray[j])
        clustering_classes = list()
        for i in range(np.size(class_val)):
            clustering_classes.append(self.__clustering__(data=array_of_classes[i]))
        output_massive = list()
        # Все еще не избавился от зависимости трех классов
        for x1, x2, x3 in zip(clustering_classes[0], clustering_classes[1], clustering_classes[2]):
            output_massive.append(x1 + x2 + x3)
        print(output_massive)
        return output_massive

    def __clustering__(self,data):
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
        u, weights1, vh = np.linalg.svd(mass1, full_matrices=False)
        u, weights2, vh = np.linalg.svd(mass2, full_matrices=False)
        u, weights3, vh = np.linalg.svd(mass3, full_matrices=False)
        u, weights4, vh = np.linalg.svd(mass4, full_matrices=False)
        u, weights5, vh = np.linalg.svd(mass5, full_matrices=False)
        u, weights6, vh = np.linalg.svd(mass6, full_matrices=False)
        u, weights7, vh = np.linalg.svd(mass7, full_matrices=False)
        u, weights8, vh = np.linalg.svd(mass8, full_matrices=False)
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

    def setParams(self, layer_count, neuron_counter=[1], activation_function=["sigmoid"],
                  kernel_init=["random_uniform"]):
        self.activation_enum = {
            "RELU" : keras.activations.relu,
            "Sigmoid" : keras.activations.sigmoid,
            "ELU" : keras.activations.elu,
            "Tangh" : keras.activations.tanh,
            "Softmax" : keras.activations.softmax,
            '': None
        }
        self.init_enum = {
            "Zeros": keras.initializers.Zeros,
            "Ones": keras.initializers.Ones,
            "RandomNormal": keras.initializers.RandomNormal,
            "RandomUniform": keras.initializers.RandomUniform,
            "TruncatedNormal": keras.initializers.TruncatedNormal,
            "Lecun_uniform": keras.initializers.lecun_uniform,
            "He_normal": 'he_normal',
            "Lecun_normal": keras.initializers.lecun_normal,
            "He_uniform": keras.initializers.he_uniform,
            "SVD": self.SVD,
            '': None
        }
        self.__setLayer_count__(layer_count)
        self.__setNeuron_counter__(neuron_counter)
        self.__setKernel_init__(kernel_init)
        self.__setActivationFunc__(activation_function)
        self.model = keras.models.Sequential()

    def setDataset(self, inputArray, realClass):
        self.inputArray = inputArray
        self.realClass = realClass

    def __setLayer_count__(self, layer_count):
        if layer_count > 0:
            self.layer_count = layer_count
        else:
            # TODO реализовать какоето событие при неверном количестве слоев ИНС
            print("Не верное количество слоев, пропробуйте еще")

    def __setNeuron_counter__(self, neuron_count):
        counter = np.array(neuron_count, dtype=int)
        if counter.size == self.layer_count:
            self.neuron_counter = counter
        else:
            # TODO Реализовать ошибку инициализации количества нейронов в сети
            print("Error value.")

    def __setKernel_init__(self, kernel_init):
        kernel = np.array(kernel_init, dtype=str)
        self.kernel_init = []
        for init in kernel:
            try:
                self.kernel_init.append(self.init_enum[init])
            except KeyError as e:
                # можно также присвоить значение по умолчанию вместо бросания исключения
                raise ValueError('Undefined unit: {}'.format(e.args[0]))

    def __setActivationFunc__(self, activation_function):
        func_array = np.array(activation_function, dtype=str)
        self.activation_function = []
        for func in func_array:
            try:
                self.activation_function.append(self.activation_enum[func])
            except KeyError as e:
                # можно также присвоить значение по умолчанию вместо бросания исключения
                raise ValueError('Undefined unit: {}'.format(e.args[0]))
        # if func_array.size == self.layer_count :
        #     self.activation_function = func_array
        # else:
        #     #TODO
        #     print("Error value")

    def __setEpochs__(self, epoch):
        if epoch > 0:
            self.epochs = epoch
        else:
            # TODO реализовать какоето событие при неверном количестве слоев ИНС
            print("Не верное количество слоев, пропробуйте еще")

    def __setLoss__(self, loss_func):
        if type(loss_func) == str:
            self.loss = loss_func
        else:
            # TODO
            print("Error loss func")

    def __setOptimizer__(self, optimizer):
        if type(optimizer) == str:
            self.optimizer = optimizer
        else:
            # TODO
            print("Error optimize func")

    def __setMetrics__(self, metric):
        # TODO Реализовать метод
        self.metrics = metric

    def get_history(self):
        return [self.info.history['loss'], self.info.history['accuracy']]

    # Метод для обучения нейронки
    def trainNeuralNetwork(self):
        # Плохой вариант реализации добавдения первого слоя
        # activation=[None,keras.activations.relu,keras.activations.softmax]
        print("GOOD5")
        i = 1
        self.model.add(keras.layers.Input(
            self.inputArray.shape[1]))  # вот это клевый будет вариант, если не задано количество входных нейронов
        while i != self.layer_count:
            self.model.add(keras.layers.Dense(self.neuron_counter[i], activation=self.activation_function[i],
                                              kernel_initializer=self.kernel_init[i]))
            i = i + 1
        # Незнаю тут врядли можно что придумать просто задаю значения параметров по факту
        self.model.compile(loss=self.loss, optimizer=self.optimizer, metrics=self.metrics)
        self.info = self.model.fit(self.inputArray, self.realClass, epochs=self.epochs,
                                   validation_split=0.1, callbacks=[self.after_epochs_end_callback])
        return self.info

    def setTrainConfig(self, train_config):
        self.__setEpochs__(train_config.epochs)
        self.__setLoss__(train_config.loss_func)
        self.__setOptimizer__(train_config.optimizer)
        self.__setMetrics__(train_config.metrics)
