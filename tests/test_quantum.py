# tests/test_quantum.py

import unittest
from communication.quantum_communication import QuantumKeyDistribution

class TestQuantumKeyDistribution(unittest.TestCase):

    def setUp(self):
        self.qkd = QuantumKeyDistribution(num_bits=10)

    def test_generate_sender_bits(self):
        self.qkd.generate_sender_bits()
        self.assertEqual(len(self.qkd.sender_bits), 10)
        self.assertTrue(all(bit in [0, 1] for bit in self.qkd.sender_bits))

    def test_simulate_receiver(self):
        self.qkd.generate_sender_bits()
        self.qkd.simulate_receiver()
        self.assertEqual(len(self.qkd.receiver_bits), 10)
        self.assertTrue(all(bit in [0, 1] for bit in self.qkd.receiver_bits))

    def test_sift_key(self):
        self.qkd.generate_sender_bits()
        self.qkd.simulate_receiver()
        self.qkd.sift_key()
        self.assertIsNotNone(self.qkd.get_key())

    def test_error_correction(self):
        self.qkd.generate_sender_bits()
        self.qkd.simulate_receiver()
        self.qkd.sift_key()
        original_key = self.qkd.get_key()
        self.qkd.error_correction()
        self.assertNotEqual(original_key, self.qkd.get_key())

    def test_privacy_amplification(self):
        self.qkd.generate_sender_bits()
        self.qkd.simulate_receiver()
        self.qkd.sift_key()
        original_key = self.qkd.get_key()
        self.qkd.privacy_amplification()
        self.assertNotEqual(original_key, self.qkd.get_key())

if __name__ == '__main__':
    unittest.main()
