# tests/test_communication.py

import unittest
from communication.secure_transmission import SecureTransmission

class TestSecureTransmission(unittest.TestCase):

    def setUp(self):
        self.secure_transmission = SecureTransmission()

    def test_aes_encryption_decryption(self):
        message = "This is a secret message."
        encrypted_message = self.secure_transmission.encrypt_aes(message)
        decrypted_message = self.secure_transmission.decrypt_aes(encrypted_message)
        self.assertEqual(message, decrypted_message)

    def test_rsa_encryption_decryption(self):
        message = "This is a secret message."
        public_key, private_key = self.secure_transmission.generate_rsa_keys()
        encrypted_message = self.secure_transmission.encrypt_rsa(message, public_key)
        decrypted_message = self.secure_transmission.decrypt_rsa(encrypted_message, private_key)
        self.assertEqual(message, decrypted_message)

    def test_digital_signature(self):
        message = "This is a message to sign."
        public_key, private_key = self.secure_transmission.generate_rsa_keys()
        signature = self.secure_transmission.sign_message(message, private_key)
        is_valid = self.secure_transmission.verify_signature(message, signature, public_key)
        self.assertTrue(is_valid)

if __name__ == '__main__':
    unittest.main()
