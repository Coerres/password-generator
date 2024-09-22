import random
import string
import pyperclip

def generate_password(min_Length: int, numbers: bool = True, special_characters: bool = True) -> str:
    characters: str = string.ascii_letters
    digits: str = string.digits
    special: str = string.punctuation

    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_Length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True

        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd


def input_dialogue():
    min_length: int = int(input("Enter the minimum lenth: "))
    has_number: bool = input("Do you want to have numbers  (y/n)?").lower() == "y"
    has_special: bool = input("Do you want to have special characters (y/n)?").lower() == "y"
    pwd = generate_password(min_Length=min_length, numbers=has_number, special_characters=has_special)
    return pwd


def copy_req(pwd: str) -> int:
    copy = input("Would you like to copy the generated password to your clipboard (y/n)? ").lower() == "y"
    if copy:
        pyperclip.copy(pwd)
        print("Password has been copied")
        return 0
    else:
        print("password wont be copied")
        return 0

def main() -> int:
    pwd: str = input_dialogue()
    print(f"Your generated password is: {pwd}")
    copy_req(pwd=pwd)
    return 0

if __name__ == '__main__':
    main()