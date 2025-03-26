import unittest
from src.palindrome import PalindromeChecker

class TestPalindrome(unittest.TestCase):
    def test_positive_palindrome(self):
        self.assertTrue(PalindromeChecker.is_palindrome(121))
        
    def test_non_palindrome(self):
        self.assertFalse(PalindromeChecker.is_palindrome(123))
        
    def test_negative(self):
        with self.assertRaises(ValueError):
            PalindromeChecker.is_palindrome(-121)
            
    def test_single_digit(self):
        self.assertTrue(PalindromeChecker.is_palindrome(5))
