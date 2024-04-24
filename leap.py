def is_leap_year(year):
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Test the function
input_year = int(input("Enter a year: "))
if is_leap_year(input_year):
    print("Yes, it's a leap year.")
else:
    print("No, it's not a leap year.")
