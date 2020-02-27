# External Imports
import os
import base64

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Create Salt
def setSalt():
    return os.urandom(16) #16-bytes salt

# Get Key from a password
def getKdf(salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=10**5,
        backend=default_backend()
    )
    return(kdf)

def getKey(password,salt):
    kdf = getKdf(salt)
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return(key)

def getFernet(password,salt):
    key = getKey(password,salt)
    return(Fernet(key))

def encrypt(text,password,salt):
    f = getFernet(password,salt)
    return(f.encrypt(text))

def decrypt(text,password,salt):
    f = getFernet(password,salt)
    return(f.decrypt(text))