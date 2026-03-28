num = int(input("Enter a number: "))
b = num % 10

if b % 5 == 0:
    print("The last digit is divisible by 5", b)
else:
    print("The last digit is not divisible by 5", b)    