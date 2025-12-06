"""Simple program to calculate the birth year from the user's age.

This module:
- asks the user for their current age,
- validates the input,
- calculates the birth year based on the current calendar year.
"""

__author__ = "539839, Broschart"
__credits__ = "Created with support from OpenAI ChatGPT."

from datetime import datetime


def read_positive_int(prompt_text):
    """Read a positive integer from user input.

    Args:
        prompt_text: The text displayed to the user.

    Returns:
        A positive integer entered by the user.
    """
    while True:
        user_input = input(prompt_text).strip()

        try:
            value = int(user_input)
        except ValueError:
            print("Bitte eine gültige ganze Zahl eingeben.")
            continue

        if value <= 0:
            print("Die Zahl muss positiv sein.")
            continue

        return value


def calculate_birth_year(age):
    """Calculate the birth year based on the current year.

    Args:
        age: The age of the person as an integer.

    Returns:
        The calculated birth year as an integer.
    """
    current_year = datetime.now().year
    return current_year - age


def main():
    """Main entry point for interactive use."""
    print("======================================")
    print("      Berechnung des Geburtsjahres     ")
    print("======================================")
    print()

    age = read_positive_int("Bitte Ihr Alter eingeben: ")
    birth_year = calculate_birth_year(age)

    print(f"Sie wurden vermutlich im Jahr {birth_year} geboren.")


if __name__ == "__main__":
    main()
