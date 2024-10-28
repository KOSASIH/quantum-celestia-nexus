# src/ai/neural_networks.py

import tensorflow as tf
from tensorflow.keras import layers, models, regularizers
from tensorflow.keras.applications import VGG16, ResNet50
from tensorflow.keras.utils import plot_model

class CustomDenseLayer(layers.Layer):
    def __init__(self, units, activation='relu', kernel_regularizer=None, **kwargs):
        super(CustomDenseLayer, self).__init__(**kwargs)
        self.units = units
        self.activation = activation
        self.kernel_regularizer = regularizers.get(kernel_regularizer)

    def build(self, input_shape):
        self.w = self.add_weight(shape=(input_shape[-1], self.units),
                                 initializer='random_normal',
                                 regularizer=self.kernel_regularizer,
                                 trainable=True)
        self.b = self.add_weight(shape=(self.units,),
                                 initializer='zeros',
                                 trainable=True)

    def call(self, inputs):
        z = tf.matmul(inputs, self.w) + self.b
        return tf.keras.activations.get(self.activation)(z)

class FeedforwardNN:
    def __init__(self, input_shape, num_classes):
        self.model = self.build_model(input_shape, num_classes)

    def build_model(self, input_shape, num_classes):
        model = models.Sequential()
        model.add(layers.Input(shape=input_shape))
        model.add(CustomDenseLayer(128, activation='relu', kernel_regularizer='l2'))
        model.add(CustomDenseLayer(64, activation='relu'))
        model.add(layers.Dense(num_classes, activation='softmax'))
        return model

    def compile_model(self, learning_rate=0.001):
        self.model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate),
                           loss='sparse_categorical_crossentropy',
                           metrics=['accuracy'])

    def visualize_model(self, filename='model.png'):
        plot_model(self.model, to_file=filename, show_shapes=True, show_layer_names=True)

class ConvolutionalNN:
    def __init__(self, input_shape, num_classes):
        self.model = self.build_model(input_shape, num_classes)

    def build_model(self, input_shape, num_classes):
        model = models.Sequential()
        model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Flatten())
        model.add(layers.Dense(64, activation='relu'))
        model.add(layers.Dense(num_classes, activation='softmax'))
        return model

    def compile_model(self, learning_rate=0.001):
        self.model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate),
                           loss='sparse_categorical_crossentropy',
                           metrics=['accuracy'])

    def visualize_model(self, filename='cnn_model.png'):
        plot_model(self.model, to_file=filename, show_shapes=True, show_layer_names=True)

class TransferLearningModel:
    def __init__(self, base_model_name, num_classes, input_shape=(224, 224, 3)):
        self.model = self.build_model(base_model_name, num_classes, input_shape)

    def build_model(self, base_model_name, num_classes, input_shape):
        if base_model_name == 'VGG16':
            base_model = VGG16(weights='imagenet', include_top=False, input_shape=input_shape)
        elif base_model_name == 'ResNet50':
            base_model = ResNet50(weights='imagenet', include_top=False, input_shape=input_shape)
        else:
            raise ValueError("Unsupported base model. Choose 'VGG16' or 'ResNet50'.")

        model = models.Sequential()
        model.add(base_model)
        model.add(layers.Flatten())
        model.add(layers.Dense(256, activation='relu'))
        model.add(layers.Dense(num_classes, activation='softmax'))

        # Freeze the base model
        base_model.trainable = False
        return model

    def compile_model(self, learning_rate=0.001):
        self.model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate),
                           loss='sparse_categorical_crossentropy',
                           metrics=['accuracy'])

    def unfreeze_base_model(self):
        for layer in self.model.layers[0].layers:
            layer.trainable = True

    def visualize_model(self, filename='transfer_model.png'):
        plot_model(self.model, to_file =filename, show_shapes=True, show_layer_names=True)
