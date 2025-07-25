n = int(input("Enter a positive integer n: "))
num = 2
while num <= n:
    is_prime = True
    i = 2
    while i <= num // 2:
        if num % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(num)
    num += 1
