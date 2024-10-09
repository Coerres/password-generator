import rsa
from rsa import PublicKey, PrivateKey
import pyperclip



recent_keypairs = []


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


def print_key_logo():
    print("""\
 _  __           ____ _____ _   _ 
| |/ /___ _   _ / ___| ____| \ | |
| ' // _ \ | | | |  _|  _| |  \| |
| . \  __/ |_| | |_| | |___| |\  |
|_|\_\___|\__, |\____|_____|_| \_|
          |___/                      
    """)





def list_keypairs():
    counter = 1
    for keypair in recent_keypairs:
        print(f"{counter}. {keypair._name}")
        counter += 1
    interaction = input(
        "Do you want to (co)py a keypair, (d)elete, (cl)ear all keypairs: ")
    match interaction:
        case "co":
            copy_keypair()
        case "d":
            delete_keypair()
        case "cl":
            delete_all_keypairs()

        # failcase if nothing valid is entered
        case _:
            print("No valid option selected, attempt again")
            list_keypairs()


# Helper functions for ls case
def copy_keypair():
    selected_choice = input(f"Select a keypair to copy: ")
    selected_choice = int(selected_choice)
    if selected_choice <= len(recent_keypairs) and selected_choice >= 1:
        selected_index = selected_choice - 1
        selected_keypair: KeyPair = recent_keypairs[selected_index]
        key_copy_req(selected_keypair.get_private_key, selected_keypair.get_public_key)
        print("keypair copied to clipboard")
        list_keypairs()


def delete_keypair():
    selected_choice = input(f"Select a keypair to delete: ")
    selected_choice = int(selected_choice)
    if selected_choice <= len(recent_keypairs) and selected_choice >= 1:
        selected_index = selected_choice - 1
        del recent_keypairs[selected_index]
        print("keypair deleted")
        list_keypairs()


def delete_all_keypairs():
    # [:] indicates the iteration is over a copy of  the list size changes
    for keypair in recent_keypairs[:]:
        print(f"Keypair {keypair._name} was deleted")
        recent_keypairs.remove(keypair)
        del keypair

    print("All keypairs deleted")
    list_keypairs()


def gen_keypair(bits: int = 1024) -> KeyPair:
    public_key, private_key = rsa.newkeys(bits)
    return KeyPair(public_key=public_key, private_key=private_key)


def key_copy_req(private_key, public_key):
    export_string = str(public_key) + " , " + str(private_key)
    pyperclip.copy(export_string)

