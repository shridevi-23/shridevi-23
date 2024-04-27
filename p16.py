# Create a sample set
my_set = {1, 2, 3, 4, 5}

# Add method - Adds an element to the set
my_set.add(6)
print("Add:", my_set)

# Update method - Updates the set with elements from another iterable or set
my_set.update({7, 8, 9})
print("Update:", my_set)

# Remove method - Removes the specified element from the set; Raises KeyError if element is not found
my_set.remove(1)
print("Remove:", my_set)

# Discard method - Removes the specified element from the set if present
my_set.discard(2)
print("Discard:", my_set)

# Pop method - Removes and returns an arbitrary element from the set
popped_element = my_set.pop()
print("Pop:", my_set, "Popped Element:", popped_element)

# Clear method - Removes all elements from the set
my_set.clear()
print("Clear:", my_set)

# Union method - Returns a new set with elements from the set and all others
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union:", union_set)

# Intersection method - Returns a new set with elements that are common to the set and all others
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# Difference method - Returns a new set with elements in the set that are not in the others
difference_set = set1.difference(set2)
print("Difference:", difference_set)

# Symmetric Difference method - Returns a new set with elements in either the set or other but not both
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_difference_set)

# Copy method - Returns a shallow copy of the set
copied_set = set1.copy()
print("Copied Set:", copied_set)

# Subset method - Returns True if all elements of a set are present in another set
subset = {1, 2}.issubset(set1)
print("Subset:", subset)

# Superset method - Returns True if all elements of another set are present in the set
superset = set1.issuperset({1, 2})
print("Superset:", superset)

# Disjoint method - Returns True if the set has no elements in common with another set
disjoint = set1.isdisjoint(set2)
print("Disjoint:", disjoint)
