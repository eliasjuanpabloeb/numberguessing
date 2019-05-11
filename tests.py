from unittest import main, TestCase
from validation import validate


class ValidationTests(TestCase):
    def test_validate(self):
        invalid_type = ['', ' ', None, 'hola']
        for elem in invalid_type:
            with self.assertRaises(AssertionError) as cm:
                validate(elem)
            self.assertEqual(cm.exception.args[0],
                             "You must provide a number.")

        invalid_size = ['12', '0', '432', '22', '112442']
        for elem in invalid_size:
            with self.assertRaises(AssertionError) as cm:
                validate(elem)
            self.assertEqual(cm.exception.args[0],
                             "Number should have 4 digits.")

        invalid_repeated = ['1111', '1231', '3212', '4442', '1123']
        for elem in invalid_repeated:
            with self.assertRaises(AssertionError) as cm:
                validate(elem)
            self.assertEqual(cm.exception.args[0],
                             "Digits shouldn't be repeated.")

        validate('4321')


if __name__ == '__main__':
    main(verbosity=2)
