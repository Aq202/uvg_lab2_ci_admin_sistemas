import unittest
import string_utils as su


class TestStringUtils(unittest.TestCase):

    def test_to_upper_happy_path_text(self):
        self.assertEqual(su.to_upper("hola mundo"), "HOLA MUNDO")

    
    def test_to_upper_happy_path_already_upper(self):
        self.assertEqual(su.to_upper("HOLA"), "HOLA")

    def test_to_upper_invalid_type(self):
        with self.assertRaises(TypeError):
            su.to_upper([True, False])

    def test_to_upper_number(self):
        with self.assertRaises(TypeError):
            su.to_upper(3.1416)

if __name__ == "__main__":
    unittest.main()
