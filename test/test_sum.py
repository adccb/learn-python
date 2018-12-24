import unittest

from src.sum import sum

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(
            15,
            sum([1, 2, 3, 4, 5])
        )

        self.assertEqual(
            180,
            sum([12, 24, 36, 48, 60])
        )
