from .ModelBlock import ModelBlock

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Input
from tensorflow.keras.layers import Dense


class Classifier(ModelBlock):
    def __init__(self, encoder):
        self.encoder_output = encoder.model.output
        self.model = self.make_model()
        self.num_layers = ModelBlock.get_head_num_layers(encoder, self.model)

    def make_model(self):
        """
        This model is responsible for building a keras model
        :return:
            keras model:
        """

        X = Flatten()(self.encoder_output)
        X = Dense(3, activation='softmax')(X)

        return X
