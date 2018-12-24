import unittest

from src.stack import Stack

class TestStack(unittest.TestCase):
    def test_stack(self):
        s = Stack()

        s.push("hello")
        self.assertEquals(
            "hello",
            s.pop()
        )



