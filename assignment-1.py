# .Write python program to accept a month number from the user and display it in words./
month = int(input("Enter a number: "))
if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else: 
    print("Invalid number.") 

#factorial of number
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact =fact * i
    print("Factorial of the  number is:",fact)    
num = int(input("Enter a number:"))
factorial(num)

#.Write a user define function to display Armstrong of a number      
def armstrong(a):
    temp = a
    sum = 0

    while temp > 0 :
        digit = temp % 10
        sum = sum + digit * digit * digit
        temp = temp // 10

    if sum == a:
        print(" The number is Armstrong Number")
    else:
        print("The number is not a Armstrong Number")    
a = int(input("Enter a number :"))
armstrong(a)

#Write user to display reverse of a number
def reverse(a):
    reverse = 0

    while a > 0:
        digit = a % 10
        reverse = reverse * 10 + digit
        a = a // 10
    print("reversed number is:",reverse)
a = int(input("Enter a number: "))
reverse(a)    

#Write a user define function to check whether the no. is prime or not
def prime(a):
    if(a < 1):
        print("not prime")
        return
    
    flag = 0
    for i in range(2, a):
        if a % 2 == 0:
            flag = 1
            break
         
    if flag == 0:
        print("prime") 
    else:
        print("is not prime")       

a = int(input("Enter a number: "))
prime(a)                  

