# API Reference

This document provides a detailed reference for the APIs available in the Quantum Celestia Nexus project.

## Quantum Module

### `quantum_circuits.py`

#### `create_circuit(qubits: int) -> QuantumCircuit`
Creates a quantum circuit with the specified number of qubits.

**Parameters:**
- `qubits`: The number of qubits in the circuit.

**Returns:**
- A QuantumCircuit object.

#### `simulate_circuit(circuit: QuantumCircuit) -> List[float]`
Simulates the given quantum circuit and returns the measurement results.

**Parameters:**
- `circuit`: The QuantumCircuit object to simulate.

**Returns:**
- A list of measurement results.

## AI Module

### `neural_networks.py`

#### `build_model(input_shape: Tuple[int], num_classes: int) -> Model`
Builds a neural network model with the specified input shape and number of output classes.

**Parameters:**
- `input_shape`: The shape of the input data.
- `num_classes`: The number of output classes.

**Returns:**
- A compiled Keras Model object.

## Data Module

### `data_loader.py`

#### `load_data(file_path: str) -> Tuple[np.ndarray, np.ndarray]`
Loads data from the specified file path.

**Parameters:**
- `file_path`: The path to the data file.

**Returns:**
- A tuple containing the features and labels as NumPy arrays.

## Communication Module

### `quantum_communication.py`

#### `send_message(message: str, recipient: str) -> bool`
Sends a quantum message to the specified recipient.

**Parameters:**
- `message`: The message to send.
- `recipient`: The recipient's address.

**Returns:**
- A boolean indicating success or failure.
