import random
from unittest import main, mock, TestCase
from games import HumanGuessingGame, CPUGuessingGame
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


class HumanGuessingGameTest(TestCase):
    def setUp(self):
        self.game = HumanGuessingGame()

    def test_get_secret_value(self):
        secret_number = self.game.get_secret_value()
        validate(secret_number)

    def test_get_guess(self):
        INPUT_VALUE = '123'
        guess = None
        with mock.patch('builtins.input', return_value=INPUT_VALUE):
            guess = self.game.get_guess()
            self.assertEqual(guess, INPUT_VALUE)

    def test_check_guess(self):
        # Guesses perfectly
        result = self.game.check_guess(self.game.secret_value)
        self.assertEqual(result, {'good': 4, 'regular': 0})

        # 1 good and 1 regular
        self.game.secret_value = '1234'
        result = self.game.check_guess('1526')
        self.assertEqual(result, {'good': 1, 'regular': 1})

        # All wrong
        self.game.secret_value = '1234'
        result = self.game.check_guess('4321')
        self.assertEqual(result, {'good': 0, 'regular': 4})

    def test_play_wins_on_first_try(self):
        SECRET_VALUE = '1234'
        self.game.secret_value = SECRET_VALUE
        with mock.patch('builtins.input', return_value=SECRET_VALUE):
            with mock.patch('builtins.print') as mocked_print:
                self.game.play()
        mocked_print.assert_any_call('Good: 4\nRegular: 0\n')
        mocked_print.assert_any_call('You win! Game over')

    def test_play_tries_different_numbers(self):
        SECRET_VALUE = '1234'
        self.game.secret_value = SECRET_VALUE
        INPUT_VALUES = ['0123', '3120', '0124', '1234']
        PRINT_CALLS = [
            mock.call('Good: 0\nRegular: 3\n'),
            mock.call('Good: 0\nRegular: 3\n'),
            mock.call('Good: 1\nRegular: 2\n'),
            mock.call('Good: 4\nRegular: 0\n'),
            mock.call('You win! Game over'),
        ]

        with mock.patch('builtins.input', side_effect=INPUT_VALUES):
            with mock.patch('builtins.print') as mocked_print:
                self.game.play()
        mocked_print.assert_has_calls(PRINT_CALLS)


class CPUGuessingGameTest(TestCase):
    def setUp(self):
        self.game = CPUGuessingGame()

    def test_get_guess(self):
        guess = self.game.get_guess()
        validate(guess)

    def test_check_guess(self):
        HUMAN_ANSWER = '1,2'

        with mock.patch('builtins.input', return_value=HUMAN_ANSWER) as mocked_input:
            with mock.patch('builtins.print') as mocked_print:
                guess = self.game.get_guess()
                result = self.game.check_guess(guess)
        mocked_print.assert_called_with('My guess is {}'.format(guess))
        mocked_input.assert_called_with('Score: ')

        self.assertEqual(result, {'good': 1, 'regular': 2})

    def test_play(self):
        random.seed(123)
        self.game.choices = self.game.get_possible_permutations()
        INPUT_VALUES = ['1,3', '1,3', '0,4', '0,4', '0,4', '4,0']
        PRINT_CALLS = [
            mock.call('My guess is 0834'),
            mock.call('My guess is 4803'),
            mock.call('My guess is 8304'),
            mock.call('My guess is 3840'),
            mock.call('My guess is 0483'),
            mock.call('My guess is 4038'),
            mock.call('Game over'),
        ]

        with mock.patch('builtins.input', side_effect=INPUT_VALUES):
            with mock.patch('builtins.print') as mocked_print:
                self.game.play()

        mocked_print.assert_has_calls(PRINT_CALLS)


if __name__ == '__main__':
    main(verbosity=2)
