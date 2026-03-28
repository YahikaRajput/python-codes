# factorial
def factorial(n):
    if n == 1:
        return 1
    else:
        return(n * factorial(n - 1))
    
n = 5
print("The factorial of the number is: ", factorial(n))

#write python program to implement recursion display sum of n numbers

def sum(n):
    if(n == 1):
        return 1
    else:
        return (n + sum(n - 1))
    
n = int(input("Enter a number to see the sum of n numbers: "))
print("The sum of n numbers is: ", sum(n))

#fibonacci series
# def fib(n):
    
    
# n = 7
# print(fib(n))