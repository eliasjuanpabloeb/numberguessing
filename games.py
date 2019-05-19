import random
import itertools
from validation import validate
from constants import NUMBER_SIZE


def calculate_score(guess, expected):
    results = {'good': 0, 'regular': 0}
    for guess_digit, expected_digit in zip(guess, expected):
        if guess_digit == expected_digit:
            results['good'] += 1
        elif guess_digit in expected:
            results['regular'] += 1

    return results


class HumanGuessingGame:
    """Game where CPU generates a secret number and human tries to guess it."""
    def __init__(self):
        self.is_over = True
        self.secret_value = self.get_secret_value()

    def get_secret_value(self):
        """Generates a random valid value and returns it."""
        digits = [str(x) for x in range(10)]
        secret_value = ''.join(random.sample(digits, k=NUMBER_SIZE))
        return secret_value

    def get_guess(self):
        """Gets the player's guess and returns it."""
        guess = input('Guess my number: ')
        return guess

    def check_guess(self, guess):
        """Checks whether the player's guess is correct."""
        return calculate_score(guess, self.secret_value)

    def show_results(self, results):
        print('Good: {0}\nRegular: {1}\n'
              .format(results['good'], results['regular']))

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
            if results['good'] == NUMBER_SIZE:
                print('You win! Game over')
                self.is_over = True


class CPUGuessingGame:
    def __init__(self):
        self.is_over = True
        self.choices = self.get_possible_permutations()

    def get_possible_permutations(self):
        """Gets a shuffled list of all possible valid permutations."""
        digits = [str(x) for x in range(10)]
        result = list(itertools.permutations(digits, NUMBER_SIZE))
        random.shuffle(result)
        return result

    def get_guess(self):
        """Gets the first possible guess."""
        return ''.join(self.choices[0])

    def check_guess(self, guess):
        """Asks the human the guess score."""
        print('My guess is {}'.format(guess))
        response = input('Score: ')
        good, regular = [int(x) for x in response.split(',')]
        return {'good': good, 'regular': regular}

    def play(self):
        """Starts the game and checks if it finished."""
        self.is_over = False
        while not self.is_over:
            guess = self.get_guess()
            results = self.check_guess(guess)
            if results['good'] == NUMBER_SIZE:
                print('Game over')
                self.is_over = True
            self.choices = [x for x in self.choices if calculate_score(x, guess) == results]


if __name__ == '__main__':
    game = None
    game_type = None
    message = """
    Welcome to Guess The Number!
    Please select a game mode:
        [0] You guess the CPU's secret number.
        [1] The CPU guesses yours.

    Your choice: """

    while game_type not in (0, 1):
        game_type = int(input(message))
    if game_type == 0:
        game = HumanGuessingGame()
    elif game_type == 1:
        game = CPUGuessingGame()
    game.play()
