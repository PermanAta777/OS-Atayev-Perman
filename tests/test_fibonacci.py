import unittest
from src.fibonacci import FibonacciGenerator

class TestFibonacci(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(FibonacciGenerator.generate(5), [0, 1, 1, 2, 3])
        
    def test_zero(self):
        self.assertEqual(FibonacciGenerator.generate(0), [])
        
    def test_negative(self):
        with self.assertRaises(ValueError):
            FibonacciGenerator.generate(-1)
            
    def test_large_number(self):
        with self.assertRaises(ValueError):
            FibonacciGenerator.generate(1001)
