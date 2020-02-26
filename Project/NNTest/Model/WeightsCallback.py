from tensorflow import keras
from Model.NeuralNetworkModel import *

class WeightsCallback(keras.callbacks.Callback):
    counter = 0
    flag = False
    struct = None


    def on_train_end(self, logs={}):
        # print(self.model.get_layer(index=0).get_weights())
        # print(self.model.get_layer(index=1).get_weights())
        self.struct = [self.model.get_layer(index=0).get_weights(), self.model.get_layer(index=1).get_weights()]

    def on_epoch_end(self, batch, logs={}):
        if self.counter == 5:
            # for layer in range(np.size(self.model.layers)):
                # print(self.model.get_layer(index=layer).get_weights())
            self.counter = 0
            self.struct = [self.model.get_layer(index=0).get_weights(),self.model.get_layer(index=1).get_weights()]
            self.flag = True
        else:
            self.counter = self.counter + 1

    def get_struct(self):
        self.flag = False
        return self.struct
