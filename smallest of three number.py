num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))
if num1<num2 and num1<num3:
    print("num1 is smaller than num2 and num3")
elif num2<num1 and num2<num3:
    print("num2 is smaller than num1 and num3")
else:
    print("num3 is smaller than num1 and num3")