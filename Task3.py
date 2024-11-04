#TASK 3 : Password Generator...

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

try:
    length = int(input("Enter the desired length of the password: "))
    if length < 1:
        print("Password length should be at least 1.")
    else:
        print("Generated Password:", generate_password(length))
except ValueError:
    print("Invalid input. Please enter a number.")
