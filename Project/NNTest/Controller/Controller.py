from abc import ABCMeta, abstractmethod, abstractproperty

from Model import config


class Controller():
    __metaclass__ = ABCMeta

    @abstractmethod
    def createView(self):
        "Создание View и Model под конкретный тип задачи"
        pass

    @abstractmethod
    def setModelParams(self,layer_count,neuron_counter,activation_function,kernel_init):
        pass

    @abstractmethod
    def setData(self,X,y):
        pass

    @abstractmethod
    def fitModel(self, config: config):
        print("Oppa")
        pass