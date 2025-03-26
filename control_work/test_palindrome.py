import unittest
from palindrome import PalindromeChecker

class TestPalindrome(unittest.TestCase):
    def test_valid_inputs(self):
        self.assertTrue(PalindromeChecker.is_palindrome(121))
        self.assertFalse(PalindromeChecker.is_palindrome(123))
        self.assertTrue(PalindromeChecker.is_palindrome(0))
    
    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            PalindromeChecker.is_palindrome(-121)
        with self.assertRaises(ValueError):
            PalindromeChecker.is_palindrome(1.5)
