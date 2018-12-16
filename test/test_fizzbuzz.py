import unittest

from src.fizzbuzz import fizzbuzz

f = lambda x: "fizzbuzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else x
class TestFizzbuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(
            [f(x) for x in range(0, 100)],
            fizzbuzz(100)
        )

        self.assertEqual(
            [f(x) for x in range(0, 150)],
            fizzbuzz(150)
        )
