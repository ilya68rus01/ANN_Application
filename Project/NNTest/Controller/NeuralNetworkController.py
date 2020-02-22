from abc import ABC
from View.NeuralNetworkView import *
from  Model.NeuralNetworkModel import *
from Controller.Controller import *


class NeuralNetworkController(Controller, ABC):
    def __init__(self,model,view):
        self.view = NeuralNetworkView()
        self.model = NeuralNetworkModel()
        self.view.show()

    def setModelParams(self,layer_count,neuron_counter,activation_function,kernel_init):
        print("SetParamContr Good")
        self.model.setParams(layer_count=layer_count, neuron_counter=neuron_counter,
                             activation_function=activation_function, kernel_init=kernel_init)

    def setData(self,X,y):
        print("setDatasetContr Good")
        self.model.setDataset(inputArray=X,realClass=y)

    def fitModel(self,epochs,loss_func,metrics,optimizer):
        print("Fit good")
        self.model.setTrainConfig(epochs=epochs,loss_func=loss_func,metrics=metrics,optimizer=optimizer)
        self.model.trainNeuralNetwork()
        data_loss,data_acc = self.model.get_history()
        print(data_loss)
        print(data_acc)
        # print(X_l)
        # print(y_l)
        self.view.plot(data_loss=data_loss,data_acc=data_acc)
        # self.view.plot(data_loss=data_loss)