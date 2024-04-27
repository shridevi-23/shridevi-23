# Define a sample string
sample_string = "Hello, World!"

# capitalize method - Converts the first character to uppercase
capitalized_string = sample_string.capitalize()
print("capitalize:", capitalized_string)

# casefold method - Converts the string to lowercase
casefolded_string = sample_string.casefold()
print("casefold:", casefolded_string)

# center method - Returns a centered string
centered_string = sample_string.center(20, '*')
print("center:", centered_string)

# count method - Returns the number of occurrences of a substring
count = sample_string.count('l')
print("count:", count)

# encode method - Returns the encoded version of the string
encoded_string = sample_string.encode()
print("encode:", encoded_string)

# endswith method - Returns True if the string ends with the specified suffix
endswith = sample_string.endswith('World!')
print("endswith:", endswith)

# expandtabs method - Sets the tab size of the string
expanded_string = "Hello\tWorld".expandtabs(4)
print("expandtabs:", expanded_string)

# find method - Returns the lowest index of a substring
index = sample_string.find('World')
print("find:", index)

# format method - Formats the string
formatted_string = "My name is {name}".format(name="John")
print("format:", formatted_string)

# index method - Returns the index of a substring
index = sample_string.index('World')
print("index:", index)

# isalnum method - Returns True if all characters in the string are alphanumeric
isalnum = sample_string.isalnum()
print("isalnum:", isalnum)

# isalpha method - Returns True if all characters in the string are alphabetic
isalpha = sample_string.isalpha()
print("isalpha:", isalpha)

# isdecimal method - Returns True if all characters in the string are decimals
isdecimal = sample_string.isdecimal()
print("isdecimal:", isdecimal)

# isdigit method - Returns True if all characters in the string are digits
isdigit = sample_string.isdigit()
print("isdigit:", isdigit)

# isidentifier method - Returns True if the string is a valid identifier
isidentifier = sample_string.isidentifier()
print("isidentifier:", isidentifier)

# islower method - Returns True if all characters in the string are lowercase
islower = sample_string.islower()
print("islower:", islower)

# isnumeric method - Returns True if all characters in the string are numeric
isnumeric = sample_string.isnumeric()
print("isnumeric:", isnumeric)

# isprintable method - Returns True if all characters in the string are printable
isprintable = sample_string.isprintable()
print("isprintable:", isprintable)

# isspace method - Returns True if all characters in the string are whitespace
isspace = sample_string.isspace()
print("isspace:", isspace)

# istitle method - Returns True if the string follows the rules of a title
istitle = sample_string.istitle()
print("istitle:", istitle)

# isupper method - Returns True if all characters in the string are uppercase
isupper = sample_string.isupper()
print("isupper:", isupper)

# join method - Joins the elements of an iterable to create a string
joined_string = '-'.join(['Hello', 'World'])
print("join:", joined_string)

# ljust method - Returns a left-justified string
left_justified_string = sample_string.ljust(20, '*')
print("ljust:", left_justified_string)

# lower method - Converts all characters in the string to lowercase
lowercase_string = sample_string.lower()
print("lower:", lowercase_string)

# lstrip method - Removes leading characters from the string
stripped_string = "    Hello, World!    ".lstrip()
print("lstrip:", stripped_string)

# partition method - Returns a tuple containing the string before the specified separator
partitioned_string = sample_string.partition(',')
print("partition:", partitioned_string)

# replace method - Replaces a specified substring with another substring
replaced_string = sample_string.replace('World', 'Universe')
print("replace:", replaced_string)

# rfind method - Returns the highest index of a substring
index = sample_string.rfind('o')
print("rfind:", index)

# rindex method - Returns the highest index of a substring
index = sample_string.rindex('o')
print("rindex:", index)

# rjust method - Returns a right-justified string
right_justified_string = sample_string.rjust(20, '*')
print("rjust:", right_justified_string)

# rpartition method - Returns a tuple containing the string before the specified separator
partitioned_string = sample_string.rpartition(',')
print("rpartition:", partitioned_string)

# rsplit method - Splits the string at the specified separator, starting from the right
split_string = "Hello, World!".rsplit(',', 1)
print("rsplit:", split_string)

# rstrip method - Removes trailing characters from the string
stripped_string = "    Hello, World!    ".rstrip()
print("rstrip:", stripped_string)

# split method - Splits the string at the specified separator
split_string = sample_string.split(',')
print("split:", split_string)

# splitlines method - Splits the string at line breaks
split_lines = "Hello\nWorld".splitlines()
print("splitlines:", split_lines)

# startswith method - Returns True if the string starts with the specified prefix
startswith = sample_string.startswith('Hello')
print("startswith:", startswith)

# strip method - Removes leading and trailing characters from the string
stripped_string = "    Hello, World!    ".strip()
print("strip:", stripped_string)

# swapcase method - Swaps case of the string
swapped_case_string = sample_string.swapcase()
print("swapcase:", swapped_case_string)

# title method - Converts the string to title case
title_string = sample_string.title()
print("title:", title_string)

# upper method - Converts all characters in the string to uppercase
uppercase_string = sample_string.upper()
print("upper:", uppercase_string)

# zfill method - Fills the string with zeros to make it a specified length
zfilled_string = "42".zfill(5)
print("zfill:", zfilled_string)
