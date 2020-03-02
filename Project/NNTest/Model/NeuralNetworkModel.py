import matplotlib as mpl
import matplotlib.pyplot as pltG
import numpy as np
import tensorflow as tf
from keras.callbacks import Callback
from tensorflow import keras
from Model.WeightsCallback import *


class NeuralNetworkModel:
    after_epochs_end_callback = Callback
    # Собственная функция для инициализации весов
    def SVD(self, shape, dtype=None):
        # Не знаю пока как реализовать правильно, но тут я создаю массивы для каждого из классов,
        # тоесть в 1 массиве все атрибуты соответствующие первому(нулевому) классу и т.д.
        # заполняю нулевыми элементами изза того что он ругается если создать пустой массив (np.array())
        massFirstClass = list()
        massSecondClass = list()
        massThirdClass = list()
        for x, i in zip(self.inputArray, self.realClass):
            if i == 0:
                massFirstClass.append(x)
            elif i == 1:
                massSecondClass.append(x)
            elif i == 2:
                massThirdClass.append(x)
            # Произвожу SVD разложение встроенными в numpy средствами
        u, weights1, vh = np.linalg.svd(massFirstClass, full_matrices=False)
        u2, weights2, vh2 = np.linalg.svd(massSecondClass, full_matrices=False)
        u3, weights3, vh3 = np.linalg.svd(massThirdClass, full_matrices=False)
        weights1 = weights1 / max(weights1)
        weights2 = weights2 / max(weights2)
        weights3 = weights3 / max(weights3)
        weights1 = weights1.tolist()
        weights2 = weights2.tolist()
        weights3 = weights3.tolist()
        # Вот на этом этапе имеем 3 вектора с коэфициентами после SVD разложения
        # я думаю что необходимо их объединить в 1 массив причем транспонировав их чтобы из вектора-строки получить вектор-столбец
        # который будет соответствовать связи и весу нейронной сети.
        # Элемент [0][0] соответствует связи первого нейрона первого слоя с первым нейроном второго слоя
        # outputMass = np.vstack([massFirstClass,massSecondClass,massThirdClass])
        outputMass = list()
        for firstClassWheight, secondClassWheight, thirdClassWheight in zip(weights1, weights2, weights3):
            outputMass.append([np.float(firstClassWheight), np.float(secondClassWheight), np.float(thirdClassWheight)])
        # outputMass = [massFirstClass.tolist() ,massSecondClass.tolist(),massThirdClass.tolist()]
        # outputMass = np.transpose(outputMass)
        print(outputMass)
        return outputMass

    def __init__(self):
        self.model = keras.models.Sequential()

    def setParams(self, layer_count, neuron_counter=[1], activation_function=["sigmoid"],
                  kernel_init=["random_uniform"]):
        self.activation_enum = {
            'relu': keras.activations.relu,
            'softmax': keras.activations.softmax,
            'elu': keras.activations.elu,
            'sigmoid': keras.activations.sigmoid,
            'tanh': keras.activations.tanh,
            '': None
        }
        self.init_enum = {
            'zeros': keras.initializers.Zeros,
            'ones': keras.initializers.Ones,
            'randomNormal': keras.initializers.RandomNormal,
            'randomUniform': keras.initializers.RandomUniform,
            'truncatedNormal': keras.initializers.TruncatedNormal,
            'lecun_uniform': keras.initializers.lecun_uniform,
            'lecun_normal': keras.initializers.lecun_normal,
            'he_normal': 'he_normal',
            'he_uniform': keras.initializers.he_uniform,
            'SVD': self.SVD,
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
