#%matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as pltG
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.datasets import load_iris
from sklearn.datasets import make_classification

class MyNeuralNetwork:
    def my_init(self,shape,dtype = None):
        # Не знаю пока как реализовать правильно, но тут я создаю массивы для каждого из классов,
        # тоесть в 1 массиве все атрибуты соответствующие первому(нулевому) классу и т.д.
        # заполняю нулевыми элементами изза того что он ругается если создать пустой массив (np.array())
        massFirstClass = list()
        massSecondClass = list()
        massThirdClass = list()
        for x,i in zip(self.inputArray,self.realClass):
            if i == 0:
                massFirstClass.append(x)
            elif i == 1:
                massSecondClass.append(x)
            elif i == 2:
                massThirdClass.append(x)
            # Произвожу SVD разложение встроенными в numpy средствами
        u,weights1,vh = np.linalg.svd(massFirstClass,full_matrices=False)
        u2,weights2,vh2 = np.linalg.svd(massSecondClass,full_matrices=False)
        u3,weights3,vh3 = np.linalg.svd(massThirdClass,full_matrices=False)
        weights1 = weights1/max(weights1)
        weights2 = weights2/max(weights2)
        weights3 = weights3/max(weights3)
        weights1 = weights1.tolist()
        weights2 = weights2.tolist()
        weights3 = weights3.tolist()
        # Вот на этом этапе имеем 3 вектора с коэфициентами после SVD разложения
        # я думаю что необходимо их объединить в 1 массив причем транспонировав их чтобы из вектора-строки получить вектор-столбец
        # который будет соответствовать связи и весу нейронной сети.
        #Элемент [0][0] соответствует связи первого нейрона первого слоя с первым нейроном второго слоя
        #outputMass = np.vstack([massFirstClass,massSecondClass,massThirdClass])
        outputMass= list()
        for firstClassWheight,secondClassWheight,thirdClassWheight in zip(weights1,weights2,weights3):
            outputMass.append([np.float(firstClassWheight),np.float(secondClassWheight),np.float(thirdClassWheight)])
        #outputMass = [massFirstClass.tolist() ,massSecondClass.tolist(),massThirdClass.tolist()]
        #outputMass = np.transpose(outputMass)
        print(outputMass)
        return outputMass
    def __init__(self,inputArray,realClass):
        self.inputArray = inputArray
        self.realClass = realClass
    def trainNeuralNetwork(self):
        model2 = keras.models.Sequential()
        model2.add(keras.layers.Input(20))
        model2.add(keras.layers.Dense(3, activation="relu", kernel_initializer=self.my_init))
        model2.add(keras.layers.Dense(3,activation="softmax",kernel_initializer='he_normal'))
        model2.compile(loss='sparse_categorical_crossentropy', optimizer='sgd', metrics=["accuracy"])
        self.info = model2.fit(self.inputArray, self.realClass, epochs=25, validation_split=0.1)
    # def plot(self):
    #     pltG.plot(self.info.history['loss'])
    #     pltG.plot(self.info.history['acc'])
    #     pltG.title('Model loss')
    #     pltG.ylabel('Loss')
    #     pltG.xlabel('Epoch')
    #     pltG.legend(['Loss', 'Accuracy'], loc='upper left')
    #     pltG.show()
    #     pltG.plot(self.info.history['val_loss'])
    #     pltG.plot(self.info.history['val_acc'])
    #     pltG.title('Modelvalid loss')
    #     pltG.ylabel('Loss')
    #     pltG.xlabel('Epoch')
    #     pltG.legend(['Val_Loss', 'Val_Accuracy'], loc='upper left')
    #     pltG.show()
X,y = make_classification(n_samples=100000, n_features=20, n_informative=3, n_redundant=2, n_repeated=0, n_classes=3, n_clusters_per_class=2, weights=None, flip_y=0.01, class_sep=1.0, hypercube=True, shift=0.0, scale=1.0, shuffle=True, random_state=42)
nn=MyNeuralNetwork(X,y)
nn.trainNeuralNetwork()
#nn.plot()