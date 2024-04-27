import re

def is_valid_password(password):
    
    if len(password) < 8 or len(password) > 20:
        return False
    
    
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[!@#$%^&*()-+]", password):
        return False
    
    return True

# Example usage
password = input("Enter the password to validate: ")
if is_valid_password(password):
    print("Valid password")
else:
    print("Invalid password")