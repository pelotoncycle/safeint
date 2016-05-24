from unittest import TestCase

import safeint


class TestInt(TestCase):

    def test_10_digits_positive(self):
        num = safeint.int('9' * 10)
        self.assertEqual(num, 9999999999)

    def test_10_digits_negative(self):
        num = safeint.int('-' + '9' * 9)
        self.assertEqual(num, -999999999)

    def test_alternative_bases(self):
        self.assertEqual(safeint.int('10', 16), 16)
        self.assertEqual(safeint.int('10', base=3), 3)

    def test_11_digits(self):
        with self.assertRaises(ValueError) as cm:
            num = safeint.int('9' * 11)
        self.assertEqual(cm.exception.message,
                         "invalid literal with base 10: '9999999999...'")

    def test_num_exceeding_upper_bound(self):
        with self.assertRaises(ValueError) as cm:
            num = safeint.int('9', low=-1, high=8)
        self.assertEqual(cm.exception.message, 'value=9 > high=8')

    def test_num_exceeding_lower_bound(self):
        with self.assertRaises(ValueError) as cm:
            num = safeint.int('-2', low=-1, high=8)
        self.assertEqual(cm.exception.message, 'value=-2 < low=-1')

    def test_empty_values(self):
        self.assertIsNone(safeint.int(''))
        self.assertIsNone(safeint.int(None))

    def test_raises_type_error(self):
        with self.assertRaises(TypeError) as cm:
            safeint.int({})
        self.assertEqual(
            cm.exception.message,
            "int() argument must be a string or a number, not 'dict'")
