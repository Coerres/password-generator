import random
import string

def generate_password(min_Length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    print(letters, digits, special)