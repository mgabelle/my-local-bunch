import getpass
import re

isPassword = False

capitalLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def checkNumber(text):
    if re.search(r"\d", text):
        return True
    else:
        return False
    

def newPassword():
    global isPassword

    if isPassword:
        print("A password already exists")
    else:
        print('''
        Choose a main password
        At least : 
            - 8 characters
            - 1 capital letter
            - 1 number
            - 1 special character
        ''')
        password = getpass.getpass(prompt='Main password: ', stream=None)

        isPassword = True
