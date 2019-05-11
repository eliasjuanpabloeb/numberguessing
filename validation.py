"""Provides validation functions."""

def validate(number):
    """Validates provided number.
    
    Args:
        number (int): number to be validated.

    Raises:
        AssertionError if number is invalid.
    """
    number = str(number).strip()

    assert len(number) == 4, \
        "Number should have 4 digits."

    assert all(number.count(digit) == 1 for digit in number), \
        "Digits shouldn't be repeated."
        
