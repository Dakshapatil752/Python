n = int(input("Enter the value of n: "))
sum_seq = 1.0
fact = 1
for i in range(1, n + 1):
    fact *= i
    sum_seq += 1 / fact
print("Sum of the sequence is:", sum_seq)
