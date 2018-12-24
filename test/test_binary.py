import unittest

from src.binary import to_binary, to_decimal

class TestBinary(unittest.TestCase):
    def test_to_binary(self):
        self.assertEqual(
            11,
            to_binary(3)
        )

    def test_to_decimal(self):
        self.assertEqual(
            3,
            to_decimal(11)
        )
