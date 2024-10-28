# Tutorial 2: Building a Neural Network

In this tutorial, you will learn how to build and train a neural network using the Quantum Celestia Nexus framework.

## Prerequisites
- Ensure you have installed the required dependencies as outlined in the [installation instructions](../README.md).

## Step 1: Load Your Data

```python
1 from src.data.data_loader import load_data
2 
3 # Load your dataset
4 features, labels = load_data('path/to/your/data.csv')
```

## Step 2: Build the Neural Network

```python
1 from src.ai.neural_networks import build_model
2 
3 # Build the model
4 model = build_model(input_shape=(features.shape[1],), num_classes=10)
```

## Step 3: Train the Model

```python
1 model.fit(features, labels, epochs=10, batch_size=32)
```

# Conclusion

You have successfully built and trained a neural network! Explore more advanced techniques in the following tutorials. 
