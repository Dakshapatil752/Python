"""
Examples: Various methods on arrays (lists) in Python
"""

arr = [5, 10, 15, 20]

# append() - Add an element to the end
arr.append(25)
print("After append(25):", arr)

# insert() - Insert an element at a specific index
arr.insert(2, 12)
print("After insert(12, 2):", arr)

# remove() - Remove first occurrence of a value
arr.remove(10)
print("After remove(10):", arr)

# pop() - Remove and return element at index (default last)
popped = arr.pop()
print("After pop():", arr, "Popped element:", popped)

# index() - Get index of first occurrence
print("Index of 15:", arr.index(15))

# count() - Count occurrences of a value
print("Count of 5:", arr.count(5))

# sort() - Sort the array
arr.sort()
print("After sort():", arr)

# reverse() - Reverse the array
arr.reverse()
print("After reverse():", arr)

# extend() - Add elements from another list
arr.extend([30, 35])
print("After extend([30, 35]):", arr)
