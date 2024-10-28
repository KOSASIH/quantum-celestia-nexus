# run_experiments.py

import argparse
from ai_module import AIModel  # Hypothetical AI module
from communication.quantum_communication import QuantumKeyDistribution

def run_ai_experiment():
    print("=== Running AI Experiment ===")
    model = AIModel()
    model.train()
    accuracy = model.evaluate()
    print(f"Model Accuracy: {accuracy}")

def run_quantum_experiment(num_bits=10):
    print("=== Running Quantum Experiment ===")
    qkd = QuantumKeyDistribution(num_bits)
    qkd.generate_sender_bits()
    qkd.simulate_receiver()
    qkd.sift_key()
    qkd.error_correction()
    qkd.privacy_amplification()
    print("Final Key:", qkd.get_key())

def main():
    parser = argparse.ArgumentParser(description="Run experiments and simulations.")
    parser.add_argument('--experiment', choices=['ai', 'quantum'], required=True,
                        help="Specify the type of experiment to run.")
    parser.add_argument('--num_bits', type=int, default=10,
                        help="Number of bits for quantum experiment (default: 10).")
    
    args = parser.parse_args()

    if args.experiment == 'ai':
        run_ai_experiment()
    elif args.experiment == 'quantum':
        run_quantum_experiment(args.num_bits)

if __name__ == "__main__":
    main()
