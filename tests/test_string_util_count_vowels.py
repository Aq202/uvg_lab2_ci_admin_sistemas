import unittest
import string_utils as su


class TestStringUtilsCountVowels(unittest.TestCase):

    def test_count_vowels_happy_path_simple(self):
        self.assertEqual(su.count_vowels("Hola"), 2)

    def test_count_vowels_happy_path_case_insensitive(self):
        self.assertEqual(su.count_vowels("AEiou"), 5)
        
    def test_count_vowels_with_accents(self):
        self.assertEqual(su.count_vowels("Canción"), 3)

    def test_count_vowels_invalid_type(self):
        with self.assertRaises(TypeError):
            su.count_vowels({"msg": "hola"})  # dict no permitido

    def test_count_vowels_edge_no_vowels(self):
        self.assertEqual(su.count_vowels(7.45), 0)  # borde: número

if __name__ == "__main__":
    unittest.main()
