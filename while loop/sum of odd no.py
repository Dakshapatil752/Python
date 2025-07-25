n = int(input("Enter a positive integer n: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 2
print(f"Sum of odd numbers up to {n} is {sum}")
