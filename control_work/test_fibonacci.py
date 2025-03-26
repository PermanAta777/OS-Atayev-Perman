import unittest
from fibonacci import FibonacciGenerator

class TestFibonacci(unittest.TestCase):
    def test_valid_inputs(self):
        self.assertEqual(FibonacciGenerator.generate_fibonacci(0), [])
        self.assertEqual(FibonacciGenerator.generate_fibonacci(1), [0])
        self.assertEqual(FibonacciGenerator.generate_fibonacci(5), [0, 1, 1, 2, 3])
    
    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            FibonacciGenerator.generate_fibonacci(-1)
        with self.assertRaises(ValueError):
            FibonacciGenerator.generate_fibonacci(1.5)
