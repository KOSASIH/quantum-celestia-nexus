# communication/secure_transmission.py

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import base64

class SecureTransmission:
    def __init__(self):
        """Initialize the Secure Transmission class."""
        self.aes_key = get_random_bytes(16)  # AES key must be either 16, 24, or 32 bytes long
        self.rsa_key = RSA.generate(2048)  # Generate RSA key pair

    def encrypt_aes(self, plaintext: str) -> str:
        """
        Encrypt the plaintext using AES encryption.
        :param plaintext: The plaintext to encrypt.
        :return: Base64 encoded ciphertext.
        """
        cipher = AES.new(self.aes_key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
        iv = base64.b64encode(cipher.iv).decode('utf-8')
        ct = base64.b64encode(ct_bytes).decode('utf-8')
        return iv + ":" + ct

    def decrypt_aes(self, ciphertext: str) -> str:
        """
        Decrypt the ciphertext using AES decryption.
        :param ciphertext: The Base64 encoded ciphertext to decrypt.
        :return: Decrypted plaintext.
        """
        iv, ct = ciphertext.split(":")
        iv = base64.b64decode(iv)
        ct = base64.b64decode(ct)
        cipher = AES.new(self.aes_key, AES.MODE_CBC, iv)
        plaintext = unpad(cipher.decrypt(ct), AES.block_size).decode('utf-8')
        return plaintext

    def generate_rsa_keys(self) -> Tuple[bytes, bytes]:
        """Generate RSA public and private keys."""
        private_key = self.rsa_key.export_key()
        public_key = self.rsa_key.publickey().export_key()
        return private_key, public_key

    def encrypt_rsa(self, message: str, public_key: bytes) -> str:
        """
        Encrypt a message using RSA encryption.
        :param message: The message to encrypt.
        :param public_key: The recipient's public key.
        :return: Base64 encoded ciphertext.
        """
        rsa_key = RSA.import_key(public_key)
        ciphertext = rsa_key.encrypt(message.encode(), None)[0]
        return base64.b64encode(ciphertext).decode('utf-8')

    def decrypt_rsa(self, ciphertext: str) -> str:
        """
        Decrypt a message using RSA decryption.
        :param ciphertext: The Base64 encoded ciphertext to decrypt.
        :return: Decrypted message.
        """
        ciphertext = base64.b64decode(ciphertext)
        plaintext = self.rsa_key.decrypt(ciphertext).decode('utf-8')
        return plaintext

    def sign_message(self, message: str) -> str:
        """
        Sign a message using RSA private key.
        :param message: The message to sign.
        :return: Base64 encoded signature.
        """
        message_hash = SHA256.new(message.encode())
        signature = pkcs1_15.new(self.rsa_key).sign(message_hash)
        return base64.b64encode(signature).decode('utf-8')

    def verify_signature(self, message: str, signature: str, public_key: bytes) -> bool:
        """
        Verify a message signature using RSA public key.
        :param message: The original message.
        :param signature: The Base64 encoded signature to verify.
        :param public_key: The public key to verify against.
        :return: True if the signature is valid, False otherwise.
        """
        message_hash = SHA256.new(message.encode())
        rsa_key = RSA.import_key(public_key)
        try:
            pkcs1_15.new(rsa_key).verify(message_hash, base64.b64decode(signature))
            return True
        except (ValueError, TypeError):
            return False

# Example usage
if __name__ == "__main__":
    secure_transmission = SecureTransmission()

    # AES Encryption/Decryption
    message_aes = "This is a secret message for AES."
    encrypted_message_aes = secure_transmission.encrypt_aes(message_aes)
    print("Encrypted AES Message:", encrypted_message_aes)

    decrypted_message_aes = secure_transmission.decrypt_aes(encrypted_message_aes)
    print("Decrypted AES Message:", decrypted_message_aes)

    # RSA Key Generation
    private_key, public_key = secure_transmission.generate_rsa _keys()
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
