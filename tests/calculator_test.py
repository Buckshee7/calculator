import unittest
from src.calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(3, add(1,2))

    def test_subtract(self):
        self.assertEqual(3, subtract(5,2))

    def test_multiply(self):
        self.assertEqual(12, multiply(3, 4))

    def test_divide(self):
        self.assertEqual(3, divide(12, 4))