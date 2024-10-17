from typing import Tuple

from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend
def ssh_setup():
    print_ssh_logo()
    keys = gen_ssh_key()
    print(f" your keys are: {keys}")


def print_ssh_logo():
    print("""\
==================
 ____ ____  _   _ 
/ ___/ ___|| | | |
\___ \___ \| |_| |
 ___) |__) |  _  |
|____/____/|_| |_|
==================
            """)
def gen_ssh_key() -> tuple[bytes, bytes]:


    key_size = input("Enter your desired keysize: ")
    key_size = int(key_size)
    while not key_size or type(key_size) != int:
        print("invalid entry try again")
        key_size = input("Enter your desired keysize: ")
        key_size = int(key_size)



    # the keygen code here is from Dave Halter, gotta give the credit
    key = rsa.generate_private_key(
        backend=crypto_default_backend(),
        public_exponent=65537,
        key_size=key_size
    )

    private_key = key.private_bytes(
        crypto_serialization.Encoding.PEM,
        crypto_serialization.PrivateFormat.PKCS8,
        crypto_serialization.NoEncryption()
    )

    public_key = key.public_key().public_bytes(
        crypto_serialization.Encoding.OpenSSH,
        crypto_serialization.PublicFormat.OpenSSH
    )
    return public_key, private_key

