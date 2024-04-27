def is_palindrome(s):
    
    s = s.lower().replace(" ", "")
    
    
    return s == s[::-1]


string_to_check = "Gadag"
if is_palindrome(string_to_check):
    print(f"'{string_to_check}' is a palindrome.")
else:
    print(f"'{string_to_check}' is not a palindrome.")