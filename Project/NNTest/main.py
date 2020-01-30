#%matplotlib inline
import numpy as np
from sklearn.datasets import load_iris
from sklearn.datasets import make_classification
from NeuralNetworkModel import *

X,y = make_classification(n_samples=100000, n_features=20, n_informative=3, n_redundant=2, n_repeated=0, n_classes=3, n_clusters_per_class=2, weights=None, flip_y=0.01, class_sep=1.0, hypercube=True, shift=0.0, scale=1.0, shuffle=True, random_state=42)
nn=NeuralNetworkModel(X,y,layer_count=3,neuron_counter=[20,3,3],activation_function=["","relu","softmax"],kernel_init=["","SVD","he_normal"]) ## Вернуть SVD
nn.setTrainConfig(epochs=5,loss_func="sparse_categorical_crossentropy",optimizer="sgd",metrics=["accuracy"])
nn.trainNeuralNetwork()
#nn.plot()