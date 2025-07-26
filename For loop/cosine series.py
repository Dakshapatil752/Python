import math

x = float(input("Enter the value of x in radians: "))
n = int(input("Enter the number of terms: "))

cos_x = 1.0
sign = -1
for i in range(1, n):
    term = (x ** (2 * i)) / math.factorial(2 * i)
    cos_x += sign * term
    sign *= -1

print("cos(x) approximation:", cos_x)
