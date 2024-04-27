# Create a sample dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Clear method - Removes all elements from the dictionary
my_dict.clear()
print("Clear:", my_dict)

# Copy method - Returns a shallow copy of the dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
copied_dict = my_dict.copy()
print("Copied Dictionary:", copied_dict)

# Get method - Returns the value for the specified key, if key is not found returns default value (None by default)
value = my_dict.get('a')
print("Get:", value)

# Items method - Returns a view object that displays a list of dictionary's (key, value) tuple pairs
items = my_dict.items()
print("Items:", items)

# Keys method - Returns a view object that displays a list of all the keys in the dictionary
keys = my_dict.keys()
print("Keys:", keys)

# Values method - Returns a view object that displays a list of all the values in the dictionary
values = my_dict.values()
print("Values:", values)

# Pop method - Removes and returns the value for the specified key, raises KeyError if key is not found
popped_value = my_dict.pop('a')
print("Pop:", my_dict, "Popped Value:", popped_value)

# Popitem method - Removes and returns an arbitrary (key, value) pair, raises KeyError if dictionary is empty
popped_item = my_dict.popitem()
print("Popitem:", my_dict, "Popped Item:", popped_item)

# Setdefault method - Returns the value of the specified key, if key is not found inserts the key with the specified value
value = my_dict.setdefault('d', 4)
print("Setdefault:", my_dict, "Value:", value)

# Update method - Updates the dictionary with the key-value pairs from another dictionary or iterable
my_dict.update({'e': 5, 'f': 6})
print("Update:", my_dict)

# Fromkeys method - Returns a new dictionary with the specified keys and values (default value is None)
new_dict = dict.fromkeys(['g', 'h', 'i'], 7)
print("Fromkeys:", new_dict)
