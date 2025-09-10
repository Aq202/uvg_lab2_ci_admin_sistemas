import unittest
from string_utils import reverse


class TestStringUtilsReverse(unittest.TestCase):

    def test_reverse_happy_path_text(self):
        self.assertEqual(reverse("Python"), "nohtyP")

    def test_reverse_happy_path_number(self):
        self.assertEqual(reverse(12345), "54321")

    def test_reverse_invalid_type(self):
        with self.assertRaises(TypeError):
            reverse([1, 2, 3])  # lista no permitida

    def test_reverse_edge_empty_string(self):
        self.assertEqual(reverse(""), "")  # borde: cadena vacía

if __name__ == "__main__":
    unittest.main()
