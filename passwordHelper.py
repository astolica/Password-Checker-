# Libraries to use 
import hashlib 
import re 
import sys 

"""
A Python script to help verify the strength of passwords 
I tried this in C but then I realized Python is probably
the better language for this 

Not doing anything low-level (yet)

"""


def introMessage():
    print("Welcome to astolica's password helper (^__^)")
    print("Give me a password for me to check!")\
    

def passwordAnalyzer(password):
    results = [] # analyze password and return results based on its nature
    if re.search(r'[\\",<>&:]', password):
        results.append()

    if len(password) < 16: # check if password is less than 16 (reccomended length)
        results.append(f"'{password}' is too short, make it at least 16 characters. (-_-)\n")
    else: 
        results.append(f"'{password}' is lengthy! Good! (¬‿¬ )")

    if not re.search(r'[A-Z]', password): # look for capital letters in password 
        results.append("Missing uppercase letter(s), add one to make your password more secure.\n") 
    else:
        results.append("Uppercase letter(s) detected, good! (¬‿¬ )")

    if not re.search(r'[0-9]', password): # look for numbers 0-9 in password string 
        results.append("You don't have a number in this password, be sure to add one.\n")
    else:
        results.append("Number(s) detected, good. Add multiple to increase entropy.(¯▿¯)")
    
    if not re.search(r'[\D\W]', password):
        results.append(f"There's no special character in this password, add one now! (#`Д´)")
    else: 
        results.append(f"Good use of special characters")


        
    header = f"\n--- Password Analysis: '{password}' ---\n" # Setup for a pretty return function
    footer = "-" * len(header)
    return f"{header}\n" + "\n".join(results) + f"\n{footer}\n"

def main(): # main function 
    introMessage()
    givenPassword = input("> ")
    print(f"Your password was '{givenPassword}', let's check it shall we? (o_O)\n")
    print(passwordAnalyzer(givenPassword))
    
    


if __name__ == "__main__":
    main()