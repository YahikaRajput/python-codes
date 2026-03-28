# finally block
# try:
#     num = 10
#     denom = 2
#     result = num/denom
#     print(result)
# except:
#     print("Denominator cannot be 0")
# finally:
#     print("This is finally block")   

# to print exception in python
# try:
#     res = 10/0
#     print("in try")
# except Exception as e:
#     print(e)

# program to print the number is even or odd
# try:
#     num = int(input("Enter a number:"))
#     assert num % 2 == 1
# except:
#     print("The entered number is even")
# else:
#     print("The entered number is odd")

# write python program to implement try, except, else and assert check whether the entered number is 
# positive or not and display properly
try:
    num = int(input("Enter a number: "))
    assert num > 0
except:
    print("The entered number is not positive")
else:
    print("The entered number is positive")    