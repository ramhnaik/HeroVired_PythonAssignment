
"""
Python script to check the password strength.
"""

import re
import string


def extract_letters_from_string(usr_pwd):
    """
   To extract letters from password entered by user
    Parameters:-
        usr_pwd : str
                Password entered by user.
    Return: str
            Concatenated letters which makes string
    """
    return "".join(re.findall("[a-zA-Z]", usr_pwd))


def extract_special_chars_from_string(usr_pwd):
    """
    To extract special characters from password entered by user
    Parameters:-
        usr_pwd : str
                Password entered by user.
    Return: str
            Concatenated special characters which makes string
    """
    spec_chars_list = list(string.punctuation)
    spec_chars_common = [x for x in usr_pwd if x in spec_chars_list]
    return spec_chars_common


def extract_numbers_from_string(usr_pwd):
    """
    To extract numbers from password entered by user
    Parameters:-
        usr_pwd : str
                Password entered by user.
    Return: str
            Concatenated numbers/characters which makes string

    """
    return "".join(re.findall("[0-9]", usr_pwd))


def check_password_strength(usr_pwd):

    """
        Function to check user entered meets all required criteria or not.
        Parameters:
            usr_pwd : str
                Password entered by user.
        Returns:
            True/False -> Boolean value indicating whether the password meets the criteria or not.
    """

    user_pwd_list = list(usr_pwd)
    letters_in_password = extract_letters_from_string(usr_pwd)
    numbers_in_password = extract_numbers_from_string(usr_pwd)
    special_chars_in_password = extract_special_chars_from_string(usr_pwd)
    if len(user_pwd_list) < 8:
        print("Entered password is not 8 characters long.")
        return False

    elif letters_in_password.isupper() or letters_in_password.islower():
        print("Entered password didn't contain both uppercase and lowercase letters.")
        return False

    elif len(numbers_in_password) < 1:
        print("Entered password didn't have digit.")
        return False

    elif len(special_chars_in_password) < 1:
        print("Entered password didn't have special character.")
        return False

    else:
        print("Strength of Password: Excellent")
        return True


if __name__ == "__main__":
    password = input("Enter the password: ")
    if not check_password_strength(password):
        print("""Entered password should meet below criteria:
        1. The password should be at least 8 characters long.
        2. Contains both uppercase and lowercase letters.
        3. Contains at least one digit (0-9).
        4. Contains at least one special character (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~).""")
