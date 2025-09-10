import unittest
import string_utils as su


class TestStringUtilsIsPalindrome(unittest.TestCase):

    def test_is_palindrome_happy_path_phrase(self):
        self.assertTrue(su.is_palindrome("Anita lava la tina"))

    def test_is_palindrome_happy_path_number(self):
        self.assertTrue(su.is_palindrome(12321))

    def test_is_palindrome_not_palindrome(self):
        self.assertFalse(su.is_palindrome("Python"))

    def test_is_palindrome_invalid_type(self):
        with self.assertRaises(TypeError):
            su.is_palindrome((1, 2, 1))

    def test_is_palindrome_edge_phrase_with_punctuation(self):
        self.assertTrue(su.is_palindrome("A man, a plan, a canal, Panama"))

if __name__ == "__main__":
    unittest.main()
