# Create a sample list
my_list = [1, 2, 3, 4, 5]

# Append method - Adds an element to the end of the list
my_list.append(6)
print("Append:", my_list)

# Extend method - Extends the list by appending elements from the iterable
my_list.extend([7, 8, 9])
print("Extend:", my_list)

# Insert method - Inserts an element at the specified index
my_list.insert(0, 0)
print("Insert:", my_list)

# Remove method - Removes the first occurrence of the specified value
my_list.remove(0)
print("Remove:", my_list)

# Pop method - Removes and returns the element at the specified index (default is the last element)
popped_element = my_list.pop(4)
print("Pop:", my_list, "Popped Element:", popped_element)

# Clear method - Removes all elements from the list
my_list.clear()
print("Clear:", my_list)

# Index method - Returns the index of the first occurrence of the specified value
my_list = [1, 2, 3, 4, 5, 4]
index = my_list.index(4)
print("Index:", index)

# Count method - Returns the number of occurrences of the specified value
count = my_list.count(4)
print("Count:", count)

# Sort method - Sorts the elements of the list in place
my_list.sort()
print("Sort:", my_list)

# Reverse method - Reverses the elements of the list in place
my_list.reverse()
print("Reverse:", my_list)

# Copy method - Returns a shallow copy of the list
copied_list = my_list.copy()
print("Copied List:", copied_list)
