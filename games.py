import random
from validation import validate


class HumanGuessingGame:
    """Game where CPU generates a secret number and human tries to guess it."""
    def __init__(self):
        self.is_over = True
        self.secret_value = self.get_secret_value()

    def get_secret_value(self):
        """Generates a random valid value and returns it."""
        digits = [str(x) for x in range(10)]
        secret_value = ''.join(random.sample(digits, k=4))
        return secret_value

    def get_guess(self):
        """Gets the player's guess and returns it."""
        guess = input('Guess my number: ')
        return guess

    def check_guess(self, guess):
        """Checks whether the player's guess is correct."""
        results = {'good': 0, 'regular': 0}
        secret_digits = list(self.secret_value)
        guess_digits = list(guess)
        for secret_digit, guess_digit in zip(secret_digits, guess_digits):
            if guess_digit == secret_digit:
                results['good'] += 1
            elif guess_digit in secret_digits:
                results['regular'] += 1

        return results

    def show_results(self, results):
        print('Good: {0}\nRegular: {1}\n'.format(results['good'], results['regular']))

    def play(self):
        """Starts the game and checks if it finished."""
        self.is_over = False
        while not self.is_over:
            guess = self.get_guess()
            try:
                validate(guess)
            except AssertionError as e:
                print('Oops! ', e.args[0])
                continue
            results = self.check_guess(guess)
            self.show_results(results)
            if results['good'] == 4:
                print('You win! Game over')
                self.is_over = True


if __name__ == '__main__':
    game = HumanGuessingGame()
    game.play()
