from unittest import main, mock, TestCase
from validation import validate
from games import HumanGuessingGame, CPUGuessingGame


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


class HumanGuessingGameTest(TestCase):
    def test_get_secret_value(self):
        game = HumanGuessingGame()
        secret_number = game.get_secret_value()
        validate(secret_number)

    def test_get_guess(self):
        INPUT_VALUE = '123'
        game = HumanGuessingGame()
        guess = None
        with mock.patch('builtins.input', return_value=INPUT_VALUE):
            guess = game.get_guess()
            self.assertEqual(guess, INPUT_VALUE)

    def test_check_guess(self):
        game = HumanGuessingGame()

        # Guesses perfectly
        result = game.check_guess(game.secret_value)
        self.assertEqual(result, {'good': 4, 'regular': 0})

        # 1 good and 1 regular
        game.secret_value = '1234'
        result = game.check_guess('1526')
        self.assertEqual(result, {'good': 1, 'regular': 1})

        # All wrong
        game.secret_value = '1234'
        result = game.check_guess('4321')
        self.assertEqual(result, {'good': 0, 'regular': 4})

    def test_play(self):
        pass


class CPUGuessingGameTest(TestCase):
    def test_get_guess(self):
        game = CPUGuessingGame()
        guess = game.get_guess()
        validate(guess)

    @mock.patch('builtins.print')
    @mock.patch('builtins.input', return_value='1')
    def test_check_guess(self, mocked_input, mocked_print):
        game = CPUGuessingGame()
        guess = game.get_guess()
        result = game.check_guess(guess)

        mocked_print.assert_called_with('My guess is {}'.format(guess))
        mocked_input.assert_any_call('Good: ')
        mocked_input.assert_any_call('Regular: ')

        self.assertEqual(result, {'good': 1, 'regular': 1})

    def test_play(self):
        pass


if __name__ == '__main__':
    main(verbosity=2)
