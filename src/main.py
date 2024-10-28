# main.py

import json
from communication.quantum_communication import QuantumKeyDistribution
from communication.secure_transmission import SecureTransmission
from celestia_sdk import CelestiaClient  # Hypothetical Celestia SDK import

def main():
    # Initialize Celestia client
    celestia_client = CelestiaClient(node_url="http://localhost:26657")  # Example node URL

    # Quantum Key Distribution (QKD) Example
    print("=== Quantum Key Distribution (QKD) ===")
    num_bits = 10  # Number of bits to transmit
    qkd = QuantumKeyDistribution(num_bits)
    
    # Step 1: Generate sender bits and bases
    qkd.generate_sender_bits()
    print("Sender Bits:", qkd.sender_bits)
    print("Sender Bases:", qkd.basis_sender)

    # Step 2: Simulate receiver's measurement
    qkd.simulate_receiver()
    print("Receiver Bits:", qkd.receiver_bits)
    print("Receiver Bases:", qkd.basis_receiver)

    # Step 3: Sift the key
    qkd.sift_key()
    print("Sifted Key:", qkd.get_key())

    # Step 4: Perform error correction
    qkd.error_correction()

    # Step 5: Perform privacy amplification
    qkd.privacy_amplification()

    # Secure Transmission Example
    print("\n=== Secure Transmission ===")
    secure_transmission = SecureTransmission()

    # AES Encryption/Decryption
    message_aes = "This is a secret message for AES."
    encrypted_message_aes = secure_transmission.encrypt_aes(message_aes)
    print("Encrypted AES Message:", encrypted_message_aes)

    decrypted_message_aes = secure_transmission.decrypt_aes(encrypted_message_aes)
    print("Decrypted AES Message:", decrypted_message_aes)

    # RSA Key Generation
    private_key, public_key = secure_transmission.generate_rsa_keys()
    print("Private Key:", private_key.decode('utf-8'))
    print("Public Key:", public_key.decode('utf-8'))

    # RSA Encryption/Decryption
    message_rsa = "This is a secret message for RSA."
    encrypted_message_rsa = secure_transmission.encrypt_rsa(message_rsa, public_key)
    print("Encrypted RSA Message:", encrypted_message_rsa)

    decrypted_message_rsa = secure_transmission.decrypt_rsa(encrypted_message_rsa)
    print("Decrypted RSA Message:", decrypted_message_rsa)

    # Digital Signature
    message_signature = "This is a message to sign."
    signature = secure_transmission.sign_message(message_signature)
    print("Signature:", signature)

    is_valid = secure_transmission.verify_signature(message_signature, signature, public_key)
    print("Signature is valid:", is_valid)

    # Sending encrypted message to Celestia
    print("\n=== Sending Encrypted Message to Celestia ===")
    transaction_data = {
        "message": encrypted_message_rsa,
        "signature": signature,
        "public_key": public_key.decode('utf-8')
    }
    
    # Send transaction to Celestia
    response = celestia_client.send_transaction(json.dumps(transaction_data))
    print("Transaction Response:", response)

if __name__ == "__main__":
    main()
