# Tutorial 1: Getting Started with Quantum Circuits

In this tutorial, you will learn how to create and simulate a simple quantum circuit using the Quantum Celestia Nexus framework.

## Prerequisites
- Ensure you have installed the required dependencies as outlined in the [installation instructions](../README.md).

## Step 1: Create a Quantum Circuit

```python
1 from src.quantum.quantum_circuits import create_circuit
```

# Create a quantum circuit with 2 qubits

circuit = create_circuit(2)

## Step 2: Simulate the Circuit

```python
1 from src.quantum.quantum_circuits import simulate_circuit
2 
3 # Simulate the circuit and get results
4 results = simulate_circuit(circuit)
5 print("Simulation Results:", results)
```


# Conclusion
You have successfully created and simulated a quantum circuit! For more advanced topics, check out the next tutorials.
