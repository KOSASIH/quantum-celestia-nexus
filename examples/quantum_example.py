# examples/quantum_example.py

from communication.quantum_communication import QuantumKeyDistribution

def main():
    print("=== Quantum Key Distribution Example ===")
    
    # Initialize QKD with a specified number of bits
    num_bits = 10
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
    print("Key after Error Correction:", qkd.get_key())

    # Step 5: Perform privacy amplification
    qkd.privacy_amplification()
    print("Final Key after Privacy Amplification:", qkd.get_key())

if __name__ == "__main__":
    main()
