# src/ai/training.py

import tensorflow as tf
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from .neural_networks import FeedforwardNN, ConvolutionalNN, TransferLearningModel

class DataLoader:
    def __init__(self, train_dir, val_dir, img_size=(224, 224), batch_size=32):
        self.train_dir = train_dir
        self.val_dir = val_dir
        self.img_size = img_size
        self.batch_size = batch_size
        self.train_datagen = ImageDataGenerator(
            rescale=1.0/255,
            rotation_range=20,
            width_shift_range=0.2,
            height_shift_range=0.2,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True,
            fill_mode='nearest'
        )
        self.val_datagen = ImageDataGenerator(rescale=1.0/255)

    def load_data(self):
        train_generator = self.train_datagen.flow_from_directory(
            self.train_dir,
            target_size=self.img_size,
            batch_size=self.batch_size,
            class_mode='sparse',
            shuffle=True
        )
        val_generator = self.val_datagen.flow_from_directory(
            self.val_dir,
            target_size=self.img_size,
            batch_size=self.batch_size,
            class_mode='sparse',
            shuffle=False
        )
        return train_generator, val_generator

class ModelTrainer:
    def __init__(self, model, train_data, val_data):
        self.model = model
        self.train_data = train_data
        self.val_data = val_data

    def train(self, epochs=50, batch_size=32):
        checkpoint = ModelCheckpoint('best_model.h5', save_best_only=True, monitor='val_loss', mode='min')
        early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
        reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=3, min_lr=1e-6)

        history = self.model.fit(self.train_data,
                                  validation_data=self.val_data,
                                  epochs=epochs,
                                  batch_size=batch_size,
                                  callbacks=[checkpoint, early_stopping, reduce_lr])
        return history

    def load_model(self, model_path='best_model.h5'):
        self.model.load_weights(model_path)

    def evaluate(self, test_data):
        loss, accuracy = self.model.evaluate(test_data)
        return {'loss': loss, 'accuracy': accuracy}

    def plot_training_history(self, history):
        import matplotlib.pyplot as plt

        plt.figure(figsize=(12, 4))
        plt.subplot(1, 2, 1)
        plt.plot(history.history['accuracy'], label='Train Accuracy')
        plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
        plt.title('Model Accuracy')
        plt.xlabel('Epoch')
        plt.ylabel('Accuracy')
        plt.legend()

        plt.subplot(1, 2, 2)
        plt.plot(history.history['loss'], label='Train Loss')
        plt.plot(history.history['val_loss'], label='Validation Loss')
        plt.title('Model Loss')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.legend()

        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Define paths to your training and validation data directories
    train_dir = 'path/to/train_data'
    val_dir = 'path/to/val_data'

    # Load data
    data_loader = DataLoader(train_dir, val_dir)
    train_data, val_data = data_loader.load_data()

    # Initialize and compile model
    model = ConvolutionalNN(input_shape=(224, 224, 3), num_classes=10)  # Example for a CNN
    model.compile_model(learning_rate=0.001)

    # Train the model
    trainer = ModelTrainer(model.model, train_data, val_data)
    history = trainer.train(epochs=50)

    # Plot training history
    trainer.plot_training_history(history)

    # Evaluate the model on validation data
    evaluation_results = trainer.evaluate(val_data)
    print(f"Validation Loss: {evaluation_results['loss']}, Validation Accuracy: {evaluation_results['accuracy']}")
