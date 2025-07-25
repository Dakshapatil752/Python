n = int(input("Enter how many numbers: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    i = 1
    smallest = float('inf')
    while i <= n:
        num = float(input(f"Enter number {i}: "))
        if num < smallest:
            smallest = num
        i += 1
    print(f"The smallest number is {smallest}")
