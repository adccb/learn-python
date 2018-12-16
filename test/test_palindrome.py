import unittest

from src.palindrome import palindrome

class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(palindrome("tacocat"))
        self.assertFalse(palindrome("burrito dog"))
