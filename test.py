# basic questions

# hello world
# print("hello world")

# take input from user and display it
# a = int(input("enter a number:"))
# print(a)

# addition of two numbers entered by user
# a = int(input("enter first number:"))
# b = int(input("enter second number:"))
# c = a+b
# print(c)

# swap two numbers
# a = 8
# b = 5
# print("before swapping {} and {}" .format(a,b))
# temp = a
# a = b
# b = temp
# print("after swapping {} and {}".format(a,b))

# area of circle
# r = int(input("enter the radius: "))
# pie = 3.14
# area = pie* r * r
# print(area)

# area of rectangle
# l = 7
# w = 4
# area = l * w
# print(area)

# celcius into frehenreit
# c = int(input("enter celcius: "))
# f = (c * 9 / 5) + 32
# print(f)

# simple intrest
# p = float(input("enter the principle: "))
# r = float(input("enter the rate: "))
# t = float(input("enter the time: "))
# si = (p * r* t)/100
# print(si)

# find sqaure and cube of a number
# a = int(input("Enter a number: "))
# square = a * a
# cube = a * a * a
# print("Square of the number is:", square)
# print("Cube of the number is:", cube)

# find average of three numbers
# a = int(input("enter a number: "))
# b = int(input("enter the second number :"))
# c = int(input("enter the third number :"))
# av = (a+b+c)/3
# print(av)

# conditional statement programs

# # even or odd
# a = int(input("enter a number"))
# if a % 2 == 0:
#     print("The number is Even")
# else:
#     print("The number is Odd")

# number is positive and negative
# a = int(input("enter a number: "))
# if(a > 0):
#     print("positive")
# else:
#     print("negative")    

# largest three number
# Program to find the largest of three numbers
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# if a >= b and a >= c:
#     largest = a
# else b >= a and b >= c:
#     largest = b
# else:
#     largest = c
# print("The largest number is:", largest) 

# number divisible by 5 AND 11
# a = int(input("enter a number: "))
# if(a % 5 == 0 and a % 11 == 0):
#     print("entered number is divisible")
# else:
#     print("not divisible")

# leap year or not
# year = int(input("Enter a year: "))
# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) :
#     print(" is a leap year") 
# else:
#     print(" is not a leap year")

# check whether a character is vowel or not
# ch = input("enter a number: ")
# if(ch in('a', 'e' , 'i', 'o', 'u')):
#     print("character is vowel")
# else:
#     print("charcter are consonent")

# whether the num is prime or not
# a = int(input("enter a number: "))
# flag = 0
# if(a <= 1):
#     print("not prime")
# else:
#     for i in range(2,a):
#         if(a % 2 == 0):
#             flag = 1
#             break    
#     if(flag == 0):
#         print("number is prime")
#     else:
#         print("not prime")    

# loop programs

# 1 to 10 using for loop
# for i  in range(1, 10+1):
#     print(i)
    
# 1 to n using while loop
# i = 1
# while(i <= 10):
#     print(i)
#     i = i+1

# sum of  first n number
# a = int(input("Enter a number: "))
# sum = 0
# for i in range(1, a+1):
#     sum = sum + i
#     print(sum)

# factorial
# a = int(int(input("enter a number: ")))
# fact = 1
# for i in range(1 , a+1):
#     fact = fact*i
# print(fact)    

# Write a Python program to print multiplication table of a number.
# a = int(input("enter a number: "))
# for i in range(1, 10+1):
#     b = a * i
#     print("{} * {} = {}".format(a,i,b))

# print even from 1 to 10
# for i in range(2 , 10+1, 2):
#     print(i)

# print odd from 1 to 10
# for i in range(1 , 10+1, 2):
#     print(i)

# reverse a number
# a = int(input("enter a number:"))
# rev = 0
# while a > 0:
#     digit = a % 10 
#     rev = rev * 10 +digit
#     a = a// 10
# print(rev)    

# Write a Python program to count digits in a number.
# a = int(input("enter a number: "))
# count = 0
# while a > 0:
#     a = a // 10
#     count = count +1
# print(count)    

# Write a Python program to check palindrome number.
# a = int(input("enter a number: "))
# temp = a
# rev = 0
# while a > 0:
#     digit = a % 10
#     rev = rev * 10 + digit
#     a = a // 10
# if temp == rev:
#     print("Is a palindorme")
# else:
#     print("Is not a plaindrome")

# Write a Python program to print Fibonacci series.
# n = int(input("enter a number:"))
# a = 0
# b = 1
# for i in range(n):
#     print(a)
#     c = a + b
#     a = b
#     b = c

# Write a Python program to find sum of digits of a number.
# num = int(input("enter a number: "))
# sum = 0
# while num > 0:
#     digit = num % 10
#     sum = sum +digit
#     num = num // 10
# print(sum)    

# function programs

# Write a Python program to create a function to add two numbers.
# def add(a, b):
#     res = a + b
#     return res
# num1 = int(input("enter first number: "))
# num2 = int(input("enter seconf number: "))
# sum = add(num1, num2)
# print(sum)

# Write a Python program to create a function to find factorial.
# def factorial(n):
#     fact = 1
#     for i in range( 1 , n+1):
#         fact = fact * i
#     return fact
# num = int(input("enter a number: "))
# res = factorial(num)
# print(res)

# Write a Python program to create a function to check prime number
# def check_prime(n):
#     if n <= 1:
#         return " not prime"
#     for i in range(2 , n):
#         if n % i == 0:
#             return "not prime"
#     return " prime"
# num= int(input("enter a number: "))
# res = check_prime(num)
# print(res)

# Write a Python program to create a function to find largest of three numbers.
# def largest(a, b, c):
#     if a >= b and a >= c :
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c
# num1 = int(input("enter first number: "))
# num2 = int(input("enter second number: "))
# num3 = int(input("enter third number: "))
# res= largest(num1,num2,num3)
# print(res)

# Write a Python program to return square of a number using function.
# def square(a):
#     return a * a
# num = int(input("enter a number: "))
# res= square(num)
# print(res)

# recursion programs

# factorial using recursion
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# num= int(input("enter a number:"))
# res = factorial(num)
# print(res)

# Fibonacci series using recursion.
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# n = int(input("enter a number: "))
# for i in range(n):
#     print(fibonacci(i))   

# lambda programs 

# using lambda function to add two numbers
# add = lambda a, b: a + b
# num1 = int(input("enter first number: "))
# num2 = int(input("enter second number: "))
# res = add(num1, num2)
# print(res)

# using lambda function find square of a number
# square = lambda a: a * a
# num = int(input("enter a number"))
# res = square(num)
# print(res)
