from abc import ABCMeta, abstractmethod, abstractproperty

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
    def fitModel(self,epochs,loss_func,metrics,optimizer):
        print("Oppa")
        pass