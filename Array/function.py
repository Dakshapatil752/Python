"""
Examples: Common functions and methods for arrays (lists) in Python
"""

arr = [10, 20, 30, 40]

# 1. append() - Add an element to the end
arr.append(50)
print("After append(50):", arr)

# 2. insert() - Insert an element at a specific index
arr.insert(2, 25)
print("After insert(25, 2):", arr)

# 3. remove() - Remove first occurrence of a value
arr.remove(20)
print("After remove(20):", arr)

# 4. pop() - Remove and return element at index (default last)
popped = arr.pop()
print("After pop():", arr, "Popped element:", popped)

# 5. index() - Get index of first occurrence
print("Index of 30:", arr.index(30))

# 6. count() - Count occurrences of a value
print("Count of 10:", arr.count(10))

# 7. sort() - Sort the array
arr.sort()
print("After sort():", arr)

# 8. reverse() - Reverse the array
arr.reverse()
print("After reverse():", arr)

# 9. extend() - Add elements from another list
arr.extend([60, 70])
print("After extend([60, 70]):", arr)

# 10. clear() - Remove all elements
arr.clear()
print("After clear():", arr)

# 11. len() - Get length of array
arr2 = [1, 2, 3]
print("Length of arr2:", len(arr2))

# 12. sum() - Get sum of array elements
print("Sum of arr2:", sum(arr2))
