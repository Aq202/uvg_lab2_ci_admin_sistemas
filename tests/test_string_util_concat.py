import unittest
import string_utils as su


class TestStringUtilsConcat(unittest.TestCase):

    def test_concat_texts(self):
        self.assertEqual(su.concat("Hola", " Mundo"), "Hola Mundo")

    def test_concat_number_and_text(self):
        self.assertEqual(su.concat("Edad: ", 25), "Edad: 25")

    def test_concat_invalid_type(self):
        with self.assertRaises(TypeError):
            su.concat("Hola", {"a": 1})

    def test_concat_float_values(self):
        self.assertEqual(su.concat(3.1, 4.2), "3.14.2")


if __name__ == "__main__":
    unittest.main()
