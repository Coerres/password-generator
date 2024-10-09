import random
import string
import pyperclip

recent_passwords = []
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


def list_passwords() -> int:
    counter = 1
    for password in recent_passwords:
        print(f"{counter}. {password}")
        counter += 1
    selected_choice =input(f"Select a password to copy: ")
    selected_choice =int(selected_choice)
    if selected_choice <= len(recent_passwords) and selected_choice >= 1:
        selected_index = selected_choice - 1
        selected_password = recent_passwords[selected_index]
        copy_req(selected_password)


    else:
        print("Select a valid password")
        list_passwords()
    return 0


def verify_recent_password_length():
    pwd: str = input_dialogue()
    print(f"Your generated password is: {pwd}")
    if len(recent_passwords) >= 3:
        recent_passwords.pop()
        recent_passwords.insert(0, pwd)
    elif len(recent_passwords) < 3:
        recent_passwords.insert(0, pwd)
    else:
        pass
    copy_req(pwd=pwd)



def copy_req(pwd: str) -> int:
    copy = input("Would you like to copy the generated password to your clipboard (y/n)? ").lower() == "y"
    if copy:
        pyperclip.copy(pwd)
        print("Password has been copied")
        return 0
    else:
        print("password wont be copied")
        return 0

def input_dialogue():
    min_length: int = int(input("Enter the minimum lenth: "))
    has_number: bool = input("Do you want to have numbers  (y/n)?").lower() == "y"
    has_special: bool = input("Do you want to have special characters (y/n)?").lower() == "y"
    pwd = generate_password(min_Length=min_length, numbers=has_number, special_characters=has_special)
    return pwd

