import unittest
from validation import validate


class ValidationTests(unittest.TestCase):
    def test_validate(self):
        with self.assertRaises(AssertionError) as cm:
            validate(123)
        self.assertEqual(cm.exception.args[0], "Number should have 4 digits.")

        with self.assertRaises(AssertionError) as cm:
            validate(1122)
        self.assertEqual(cm.exception.args[0], "Digits shouldn't be repeated.")

        validate(4321)


if __name__ == '__main__':
    unittest.main(verbosity=2)
