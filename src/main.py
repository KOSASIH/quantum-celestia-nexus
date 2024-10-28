# main.py

import argparse
import logging
from src.communication.quantum_communication import QuantumKeyDistribution
from src.blockchain.blockchain import Blockchain
from src.ai_model import AIModel
from src.utils import generate_nonce, validate_transaction  # Hypothetical utility functions

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def initialize_blockchain():
    """Initialize the blockchain."""
    logging.info("Initializing the blockchain...")
    blockchain = Blockchain()
    return blockchain

def run_quantum_key_distribution(num_bits):
    """Run Quantum Key Distribution."""
    logging.info("=== Running Quantum Key Distribution ===")
    qkd = QuantumKeyDistribution(num_bits)
    qkd.generate_sender_bits()
    qkd.simulate_receiver()
    qkd.sift_key()
    qkd.error_correction()
    qkd.privacy_amplification()
    final_key = qkd.get_key()
    logging.info("Final Key from QKD: %s", final_key)
    return final_key

def deploy_ai_model():
    """Deploy the AI model."""
    logging.info("=== Deploying AI Model ===")
    model = AIModel()
    model.train()
    model.save("quantum_ai_model")
    logging.info("AI Model deployed and saved.")

def create_transaction(blockchain, sender, receiver, amount, key):
    """Create a transaction on the blockchain."""
    logging.info(f"Creating transaction from {sender} to {receiver} for amount {amount}...")
    nonce = generate_nonce()  # Generate a unique nonce for the transaction
    transaction = blockchain.create_transaction(sender, receiver, amount, key, nonce)
    
    if validate_transaction(transaction):
        blockchain.add_transaction(transaction)
        logging.info("Transaction created and added to the blockchain: %s", transaction)
    else:
        logging.error("Transaction validation failed.")

def main():
    parser = argparse.ArgumentParser(description="Quantum Celestia Nexus Main Application")
    parser.add_argument('--num_bits', type=int, default=10, help="Number of bits for Quantum Key Distribution.")
    parser.add_argument('--deploy_ai', action='store_true', help="Deploy the AI model.")
    parser.add_argument('--sender', type=str, required=True, help="Sender's address.")
    parser.add_argument('--receiver', type=str, required=True, help="Receiver's address.")
    parser.add_argument('--amount', type=float, required=True, help="Amount to transfer.")
    parser.add_argument('--simulate', action='store_true', help="Simulate a transaction without adding to the blockchain.")

    args = parser.parse_args()

    # Initialize the blockchain
    blockchain = initialize_blockchain()

    # Run Quantum Key Distribution
    final_key = run_quantum_key_distribution(args.num_bits)

    # Optionally deploy the AI model
    if args.deploy_ai:
        deploy_ai_model()

    # Create a transaction on the blockchain
    if args.simulate:
        logging.info("Simulating transaction...")
        logging.info("Transaction details: Sender: %s, Receiver: %s, Amount: %s", args.sender, args.receiver, args.amount)
    else:
        create_transaction(blockchain, args.sender, args.receiver, args.amount, final_key)

    logging.info("=== Application Finished ===")

if __name__ == "__main__":
    main()
