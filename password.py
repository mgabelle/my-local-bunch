import getpass
import re

isPassword = False

capitalLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def checkNumber(text):
    if re.search(r"\d", text):
        return True
    else:
        return False
    
def checkCapitalLetters(text):
    if re.search(r"[A-Z]",text):
        return True
    else:
        return False

def checkSpecialCharacters(text):
    if re.search(r"\W", text):
        return True
    else:
        return False 

def checkPassword(password):
    isCorrectPassword = (len(password) >= 8) 
    isCorrectPassword &= checkCapitalLetters(password)
    isCorrectPassword &= checkNumber(password)
    isCorrectPassword &= checkSpecialCharacters(password)
    return isCorrectPassword
     

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
        
        
        # Input && Check password once and twice
        print("Enter your main password.")

        while True:
            password = getpass.getpass(prompt='Password :', stream=None)

            # Check once
            if checkPassword(password):
                secondPassword = getpass.getpass(prompt='Enter your password a second time :', stream=None)
                # Check Twice
                if secondPassword == password:
                    break
                print("Incorrect : Your second password is not the same as the first one.")
                continue
            print("It's an invalid password.")

        return password