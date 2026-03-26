# Libraries to use 
import hashlib 
import re 
import sys 
import secrets

"""
Putting something else here later 

"""


def introMessage():
    print("Password Checker")
    print("Enter 1 for password verification\n"
    "or enter 2 to exit.")
    

def passwordAnalyzer():
    password = input("Enter your password: ")
    results = [] # analyze password and return results based on its nature
    if re.search(r'[\\",<>&:]', password):
        results.append(f"'{password} contains an invalid character (ex. '\, &, <>, etc.) Please remove it.")

    if len(password) < 16: # check if password is less than 16 (reccomended length)
        results.append(f"'{password}' is too short, make it at least 16 characters.\n")
    else: 
        results.append(f"'{password}' is of adequate length.")

    if not re.search(r'[A-Z]', password): # look for capital letters in password 
        results.append("Missing uppercase letter(s), add one to make your password more secure.\n") 
    else:
        results.append("Goos use of uppercase letter(s) detected.")

    if not re.search(r'[0-9]', password): # look for numbers 0-9 in password string 
        results.append("You don't have a number in this password, be sure to add one.\n")
    else:
        results.append("Number(s) detected. Be sure to add multiple to increase entropy.")
    
    if not re.search(r'[\D\W]', password):
        results.append(f"There's no special character in this password, add one.")
    else: 
        results.append(f"Good use of special characters.")

    header = f"\n--- Password Analysis: '{password}' ---\n" # Setup for a pretty return function
    footer = "-" * len(header)
    return f"{header}\n" + "\n".join(results) + f"\n{footer}\n"


def main(): # main function 
    introMessage()
    choice = input("> ")
    if choice == "1":
        passwordAnalyzer()
    if choice == "2": 
        sys.exit()

if __name__ == "__main__":
    main()