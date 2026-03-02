# Libraries to use 
import hashlib 

"""
A Python script to help verify the strength of passwords 
I tried this in C but then I realized Python is probably
the better language for this 

Not doing anything low-level (yet)

"""


def introMessage():
    print("\nAstolica's password helper (^__^) ")
    print("Give me a password for me to check!\n")\
    
def countCase(x):
    count = 0
    for letter in x:
        if letter.isupper():
            count+=1
    return count 

def passwordAnalyzer(a):
    if len(a) <= 16:
            print(f"'{a}' is too short, make it at least 16 characters\n")
    else: 
         print(f"'{a}' is lengthy! Good!")
    if countCase(a) < 1:
         print("You need at least one uppercase letter for your password\n")
    else:
         print(f"{a} has capital letters, good!")
        
        

def main():
    introMessage()
    givenPassword = str(input())
    print(f"Your password was '{givenPassword}', let's check it shall we? (o_O)\n")
    passwordAnalyzer(givenPassword)
    


if __name__ == "__main__":
    main()