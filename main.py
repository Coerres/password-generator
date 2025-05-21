from password import list_passwords, verify_recent_password_length
from keypair import print_key_logo, gen_keypair, recent_keypairs, key_copy_req, list_keypairs
from ssh_keypair import ssh_setup
from pwd_strenght_tester import password_strength


def print_logo() -> int:
    print("""
     ___        _      _      _  _   ____               
    / _ \ _   _(_) ___| | ___| || |_|  _ \ __ _ ___ ___ 
    | | | | | | | |/ __| |/ /_  ..  _| |_) / _` / __/ __|
    | |_| | |_| | | (__|   <|_      _|  __/ (_| \__ \___
     \__\_\\__,_|_|\___|_|\_\ |_||_| |_|   \__,_|___/___/

======================================================             
                 """)
    return 0


def password_setup():
    select = input("Do you want to generate a password (gen) or see your last three passwords (ls), or check the (s)trenght of an existining password? ")
    match select:
        case "gen":
            verify_recent_password_length()
            main()
        case "ls":
            list_passwords()
            main()
        case "s":
            password = input("Enter a password to check its strength: ")
            password_strength(password)
            main()


def key_setup():
    print_key_logo()
    selection: str = input(
        "Welcome to the Key generation interface, would you like to generate a keypair (gen) or list the most recent keypairs (ls) or return to the (s)election: ")
    match selection:
        case "gen":
            bits = input("Enter the Amount of Bits used for your Keys (minimum default value is 1024): ")
            bits = int(bits)
            if bits < 1024:
                bits = 1024
            generated_Keypair = gen_keypair(bits=bits)
            keypair_name = input("enter a name for your keypair: ")
            generated_Keypair.set_name = keypair_name

            if len(recent_keypairs) >= 3:
                recent_keypairs.pop()
                recent_keypairs.insert(0, generated_Keypair)
                print("case1")
            else:
                recent_keypairs.insert(0, generated_Keypair)
                print("case2")

            copy_req_check = input("Do you want to save your keypair to the clipboard? (y/n): ")
            if copy_req_check == "y":
                key_copy_req(generated_Keypair.get_private_key, generated_Keypair.get_public_key)
                key_setup()
            else:
                key_setup()
        case "ls":
            list_keypairs()
        case "s":
            main()

        # failcase if none of the other cases catch
        case _:
            print("no valid input attempt again")

def setup_dialogue():
    print_logo()
    selection = input("Would you like to generate a password (pwd), generate a keypair (key) or an SSH keypair (ssh) or check the (s)trength of an existing password: ")
    match selection:
        case "pwd":
            password_setup()
        case "key":
            key_setup()
        case "ssh":
            ssh_setup()
        case "s":
            password = input("Enter a password to check its strength: ")
            password_strength(password)
            main()
        # failcase if none of the cases above match
        case _:
            print("You have not entered any valid option, attempt again")
            setup_dialogue()


def main() -> int:
    setup_dialogue()
    return 0



if __name__ == '__main__':
    main()
