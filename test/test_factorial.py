import unittest

from src.factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(
            120,
            factorial(5)
        )

        self.assertEqual(
            479001600,
            factorial(12)
        )
