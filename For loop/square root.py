import math

num = int(input("Enter a number: "))
sqrt_num = math.isqrt(num)
print("Square root:", sqrt_num)

if sqrt_num < 2:
    print("Square root is not prime.")
else:
    is_prime = True
    for i in range(2, int(math.sqrt(sqrt_num)) + 1):
        if sqrt_num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Square root is prime.")
    else:
        print("Square root is not prime.")
