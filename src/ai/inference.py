# src/ai/inference.py

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import os

class ModelInference:
    def __init__(self, model_path):
        self.model = load_model(model_path)

    def predict(self, input_data):
        """
        Make predictions on the input data.
        :param input_data: Numpy array of shape (num_samples, height, width, channels)
        :return: Predicted class indices
        """
        predictions = self.model.predict(input_data)
        return np.argmax(predictions, axis=1)

    def evaluate(self, test_data, test_labels):
        """
        Evaluate the model on test data.
        :param test_data: Numpy array of test images
        :param test_labels: Numpy array of true labels
        :return: Dictionary containing loss and accuracy
        """
        loss, accuracy = self.model.evaluate(test_data, test_labels)
        return {'loss': loss, 'accuracy': accuracy}

    def visualize_predictions(self, input_data, true_labels, num_images=5):
        """
        Visualize predictions made by the model.
        :param input_data: Numpy array of input images
        :param true_labels: Numpy array of true labels
        :param num_images: Number of images to visualize
        """
        predictions = self.predict(input_data)

        plt.figure(figsize=(15, 5))
        for i in range(num_images):
            plt.subplot(1, num_images, i + 1)
            plt.imshow(input_data[i])
            plt.title(f'True: {true_labels[i]}, Pred: {predictions[i]}')
            plt.axis('off')
        plt.show()

    def batch_predict(self, image_dir, img_size=(224, 224)):
        """
        Predict classes for a batch of images in a directory.
        :param image_dir: Directory containing images
        :param img_size: Size to which images will be resized
        :return: Dictionary of image filenames and their predicted classes
        """
        from tensorflow.keras.preprocessing.image import load_img, img_to_array

        predictions = {}
        for filename in os.listdir(image_dir):
            if filename.endswith(('.png', '.jpg', '.jpeg')):
                img_path = os.path.join(image_dir, filename)
                img = load_img(img_path, target_size=img_size)
                img_array = img_to_array(img) / 255.0  # Normalize
                img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

                pred = self.predict(img_array)
                predictions[filename] = pred[0]

        return predictions

# Example usage
if __name__ == "__main__":
    model_path = 'best_model.h5'  # Path to your trained model
    inference = ModelInference(model_path)

    # Example for evaluating on test data
    test_data = np.random.rand(10, 224, 224, 3)  # Replace with actual test data
    test_labels = np.random.randint(0, 10, size=(10,))  # Replace with actual labels
    evaluation_results = inference.evaluate(test_data, test_labels)
    print(f"Test Loss: {evaluation_results['loss']}, Test Accuracy: {evaluation_results['accuracy']}")

    # Example for visualizing predictions
    inference.visualize_predictions(test_data, test_labels, num_images=5)

    # Example for batch prediction
    image_dir = 'path/to/image_directory'  # Replace with your image directory
    predictions = inference.batch_predict(image_dir)
    for filename, pred in predictions.items():
        print(f"{filename}: Predicted Class: {pred}")
