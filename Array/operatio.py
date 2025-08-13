"""
Examples: Operations on arrays in Python
"""

# Using list as array
arr = [10, 20, 30, 40, 50]

# Accessing elements
print("First element:", arr[0])
print("Last element:", arr[-1])

# Slicing
print("Elements from index 1 to 3:", arr[1:4])

# Length of array
print("Length:", len(arr))

# Adding an element
arr.append(60)
print("After appending 60:", arr)

# Inserting an element
arr.insert(2, 25)
print("After inserting 25 at index 2:", arr)

# Removing an element
arr.remove(30)
print("After removing 30:", arr)

# Popping an element
popped = arr.pop()
print("After popping last element:", arr, "Popped element:", popped)

# Finding index of an element
print("Index of 40:", arr.index(40))

# Counting occurrences of an element
print("Count of 20:", arr.count(20))

# Sorting the array
arr.sort()
print("Sorted array:", arr)

# Reversing the array
arr.reverse()
print("Reversed array:", arr)
