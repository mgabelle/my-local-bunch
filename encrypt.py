# External Imports
import os
import base64

from cryptography.fernet import Fernet
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


# Open file with data
with open("data.txt","rb") as f:
    password = f.read()

salt = os.urandom(16)

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=10**5,
    backend=default_backend()
)

key = base64.urlsafe_b64encode(kdf.derive(password))

f = Fernet(key)

text = input("enter text : ").encode()