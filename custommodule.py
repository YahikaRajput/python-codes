# write python program to implement custom module
# 1-create two files in the first file implement addition , multiplication, 
# division and substraction. in the second file import the first file and 
# display respective results
# 2-create two files in the first file implement sum of n numbers and 
# factorial function, in the second file import the first file and display
# the respective results

# 1
def add(a,b):
    res = a+b
    print("Addition of two numbers:",res)

def sub(a,b):
    res = a - b 
    print("Subtraction of two numbers:",res)   

def multi(a,b):
    res = a * b
    print("Multiplication of two numbers:",res)

def div(a,b):
    res = a / b
    print("Division of two numbers:",res)

def sumofnnumber(a,sum):
    for i in range(0,a+1):
        sum = sum + i
    print(sum)

def factorial(a, fact):
    for i in range(1,a+1):
        fact =fact * i
    print(fact)
