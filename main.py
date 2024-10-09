from password import list_passwords, verify_recent_password_length
from keypair import key_setup
from ssh_keypair import ssh_setup


def print_logo() -> int:
    print("""=====================================================
     ___        _      _      _  _   ____               
    / _ \ _   _(_) ___| | ___| || |_|  _ \ __ _ ___ ___ 
    | | | | | | | |/ __| |/ /_  ..  _| |_) / _` / __/ __|
    | |_| | |_| | | (__|   <|_      _|  __/ (_| \__ \___
     \__\_\\__,_|_|\___|_|\_\ |_||_| |_|   \__,_|___/___/

    ======================================================             
                 """)
    return 0


def password_setup():
    select = input("Do you want to generate a password (gen) or see your last three passwords (ls)?")
    if select == "gen":
        verify_recent_password_length()
        main()
    elif select == "ls":
        list_passwords()
        main()


def setup_dialogue():
    print_logo()
    selection = input("Would you like to generate a password (pwd), generate a keypair (key) or an SSH keypair (ssh): ")
    match selection:
        case "pwd":
            password_setup()
        case "key":
            key_setup()
        case "ssh":
            ssh_setup()
        # failcase if none of the cases above match
        case _:
            print("You have not entered any valid option, attempt again")
            setup_dialogue()


def main() -> int:
    setup_dialogue()
    return 0


if __name__ == '__main__':
    main()
