# examples/communication_example.py

from communication.secure_transmission import SecureTransmission

def main():
    print("=== Communication Protocols Example ===")
    
    # Initialize the secure transmission module
    secure_transmission = SecureTransmission()

    # Example message for AES encryption
    message_aes = "This is a secret message for AES."
    encrypted_message_aes = secure_transmission.encrypt_aes(message_aes)
    decrypted_message_aes = secure_transmission.decrypt_aes(encrypted_message_aes)
    print("Original AES Message:", message_aes)
    print("Encrypted AES Message:", encrypted_message_aes)
    print("Decrypted AES Message:", decrypted_message_aes)

    # Example message for RSA encryption
    message_rsa = "This is a secret message for RSA."
    public_key, private_key = secure_transmission.generate_rsa_keys()
    encrypted_message_rsa = secure_transmission.encrypt_rsa(message_rsa, public_key)
    decrypted_message_rsa = secure_transmission.decrypt_rsa(encrypted_message_rsa, private_key)
    print("Original RSA Message:", message_rsa)
    print("Encrypted RSA Message:", encrypted_message_rsa)
    print("Decrypted RSA Message:", decrypted_message_rsa)

    # Digital signature example
    message_signature = "This is a message to sign."
    signature = secure_transmission.sign_message(message_signature, private_key)
    is_valid = secure_transmission.verify_signature(message_signature, signature, public_key)
    print("Signature:", signature)
    print("Is the signature valid?", is_valid)

if __name__ == "__main__":
    main()
