import rsa
from rsa import PublicKey, PrivateKey
import pyperclip

recent_keypairs = []


def print_ssh_logo():
    print("""\
 _  __           ____ _____ _   _ 
| |/ /___ _   _ / ___| ____| \ | |
| ' // _ \ | | | |  _|  _| |  \| |
| . \  __/ |_| | |_| | |___| |\  |
|_|\_\___|\__, |\____|_____|_| \_|
          |___/                      
    """)


def key_setup():
    print(recent_keypairs)
    print_ssh_logo()
    selection: str = input(
        "Welcome to the Key generation interface, would you like to generate a keypair (gen) or list the most recent keypairs (ls)")
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
        # failcase if none of the other cases catch
        case _:
            pass

def list_keypairs():
    counter = 1
    for keypair in recent_keypairs:
        print(f"{counter}. {keypair._name}")
        counter += 1
    interaction = input("Do you want to (co)py a keypair, (d)elete or (cl)ear all keypairs")
    match interaction:
        case "co":
            copy_keypair()
        case "d":
            delete_keypair()
        case "cl":
            delete_all_keypairs()

# Helper functions for ls case
def copy_keypair():
    selected_choice = input(f"Select a password to copy: ")
    selected_choice = int(selected_choice)
    if selected_choice <= len(recent_keypairs) and selected_choice >= 1:
        selected_index = selected_choice - 1
        selected_keypair: KeyPair = recent_keypairs[selected_index]
        key_copy_req(selected_keypair.get_private_key, selected_keypair.get_public_key)
        print("keypair copied to clipboard")
        list_keypairs()

def delete_keypair():
    selected_choice = input(f"Select a password to delete: ")
    selected_choice = int(selected_choice)
    if selected_choice <= len(recent_keypairs) and selected_choice >= 1:
        selected_index = selected_choice - 1
        del recent_keypairs[selected_index]
        print("keypair deleted")
        list_keypairs()

def delete_all_keypairs():
    for keypair in recent_keypairs:
        del keypair
    print("All keypairs deleted")
    list_keypairs()

class KeyPair:
    def __init__(self, public_key: PublicKey | None = None, private_key: PrivateKey | None = None, name: str = "unset"):
        self.__private_key = private_key
        self.__public_key = public_key
        self._name = name

    @property
    def get_private_key(self) -> PrivateKey:
        return self.__private_key

    @get_private_key.deleter
    def delete_private_key(self):
        del self.__private_key

    @property
    def get_public_key(self) -> PublicKey:
        return self.__public_key

    @get_public_key.deleter
    def delete_public_key(self):
        del self.__public_key

    @property
    def get_name(self) -> str:
        return self._name

    @get_name.setter
    def set_name(self, name: str):
        self._name = name
        


def gen_keypair(bits: int = 1024) -> KeyPair:
    public_key, private_key = rsa.newkeys(bits)
    return KeyPair(public_key=public_key, private_key=private_key)


def key_copy_req(private_key, public_key):
    export_string = str(public_key) + " , " + str(private_key)
    pyperclip.copy(export_string)
