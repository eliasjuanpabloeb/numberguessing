"""Provides validation functions."""
from constants import NUMBER_SIZE


def validate(provided_value=''):
    """Validates provided value.
    Args:
        provided_value (str): value to be validated.

    Raises:
        AssertionError if value is invalid.
    """
    try:
        # prevent None and make sure it is a number
        int(str(provided_value))
    except ValueError:
        raise AssertionError('You must provide a number.')

    assert len(provided_value) == NUMBER_SIZE, \
        "Number should have {} digits.".format(NUMBER_SIZE)

    assert all(provided_value.count(digit) == 1 for digit in provided_value), \
        "Digits shouldn't be repeated."
