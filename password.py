'''You can use the following Python program to check the validity of passwords input by the user. The program checks the following criteria for a valid password:

Length should be between 6 and 20 characters.
Should contain at least one uppercase letter.
Should contain at least one lowercase letter.
Should contain at least one digit.
Should contain at least one special character from !@#$%^&*().'''



import re

def check_password(password):
    # Length should be between 6 and 20 characters
    if len(password) < 6 or len(password) > 20:
        return False
    
    # Should contain at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return False

    # Should contain at least one lowercase letter
    if not re.search(r"[a-z]", password):
        return False

    # Should contain at least one digit
    if not re.search(r"\d", password):
        return False

    # Should contain at least one special character
    if not re.search(r"[!@#$%^&*()]", password):
        return False

    return True

# Get password input from user
password = input("Enter your password: ")

# Check password validity
if check_password(password):
    print("Password is valid.")
else:
    print("Password is invalid.")
