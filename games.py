import random
from validation import validate


class HumanGuessingGame:
    """CPU generates a secret number and human tries to guess it."""
    def __init__(self):
        self.secret_value = self.get_secret_value()

    def get_secret_value(self):
        """Generates a random valid value and returns it."""
        secret_value = None
        while True:
            secret_value = str(random.randint(1000, 9999))
            try:
                validate(secret_value)
                break
            except AssertionError:
                continue
        return secret_value

    def get_guess(self):
        """Gets the player's guess and returns it."""
        guess = input('Guess my number: ')
        return guess

    def check_guess(self, guess):
        """Checks whether the player's guessing is correct."""
        result = {'good': 0, 'regular': 0}
        secret_digits = list(self.secret_value)
        guess_digits = list(guess)
        for secret_digit, guess_digit in zip(secret_digits, guess_digits):
            if guess_digit == secret_digit:
                result['good'] += 1
            elif guess_digit in list(self.secret_value):
                result['regular'] += 1

        return result

    def play(self):
        """Starts the game."""
        pass
