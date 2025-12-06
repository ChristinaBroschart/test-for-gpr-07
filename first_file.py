"""Program to calculate the user's year of birth more accurately.

This module:
- asks the user for their age,
- asks for the month of birth,
- determines whether the birthday has already occurred this year,
- calculates the most probable year of birth.
"""

__author__ = "539839, Broschart"
__credits__ = "Created with support from OpenAI ChatGPT."
__email__ = "s8926052@rz.uni-frankfurt.de"

from datetime import datetime


def read_positive_int(prompt_text):
    """Read a positive integer from user input.

    Args:
        prompt_text: Text displayed to the user.

    Returns:
        A positive integer.
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


def read_month(prompt_text):
    """Read a valid month number (1–12) from user input.

    Args:
        prompt_text: Text displayed to the user.

    Returns:
        Integer month number between 1 and 12.
    """
    while True:
        user_input = input(prompt_text).strip()

        try:
            month = int(user_input)
        except ValueError:
            print("Bitte eine gültige ganze Zahl eingeben.")
            continue

        if 1 <= month <= 12:
            return month

        print("Bitte eine gültige Monatszahl zwischen 1 und 12 eingeben.")


def calculate_birth_year(age, birth_month):
    """Calculate the birth year based on age and birth month.

    Args:
        age: Current age of the user.
        birth_month: Month of birth (1–12).

    Returns:
        Integer representing the calculated year of birth.
    """
    now = datetime.now()
    current_year = now.year
    current_month = now.month

    # If the birthday is still in the future this year,
    # the person is effectively one year younger relative to January 1st.
    if birth_month > current_month:
        return current_year - age - 1

    return current_year - age


def main():
    """Main entry point for interactive use."""
    print("======================================")
    print("   Genauere Berechnung des Geburtsjahres")
    print("======================================")
    print()

    age = read_positive_int("Bitte Ihr Alter eingeben: ")
    birth_month = read_month("Bitte Ihren Geburtsmonat (1-12) eingeben: ")

    birth_year = calculate_birth_year(age, birth_month)

    print(f"Sie wurden vermutlich im Jahr {birth_year} geboren.")


if __name__ == "__main__":
    main()
