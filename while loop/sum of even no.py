n = int(input("Enter a positive integer n: "))
sum = 0
i = 2
while i <= n:
    sum += i
    i += 2
print(f"Sum of even numbers up to {n} is {sum}")
