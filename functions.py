# Function
def gm(name): #name is called as the parameter
    print("Good morning", name)
gm("Yashika")#actual value argument
gm("AAAAAAAAA")

#maethod passing arguments
def add(a, b):
    res = a + b
    print("The addition of two number is: ", res)
add(5, 6)

#use of return value
def add1(a, b):
    res1 = a + b
    return res1
res1 = add1(4,8)
print("The addition of the two number is: ", res1)

#use of pass statement inside function
def greet():
    pass
print("Pass a function")

#function argument with default values in python we can provide default values to the function arguments for this we use = symbol 
#keyword arugument: in keyword arguments the arguments are assigned based on the name of the arguments in the position of the arguments doest matter 
#function with arbitrary arguments sometimes we do not know in advance the number of argumnets that will be passes into a function to handle this kind of a situation we use arbitrary arguments this arguments allow us to pass different number of values during a funnction call we use * symbol before the parameter name to denote this argument

#function with default arguments 
def add2(a= 9, b= 10):
    res2 = a + b
    print("The addition of two numbers with default values: ", res2)

#function call with two arguments
add2(11, 13)
#function call with one arguments
add2(27)
#function call with no arguments
add2()

    
#use of keyword arguments 
def display(fname, lname):
    print("First name: ", fname)
    print("last name: ", lname)

display(fname="Yashika", lname="Rajput")

#use of arbitrary argument
def add3(*numbers):
    result = 0
    for num in numbers:
        result = result + num
    print("Addition = ", result)

#function with 3 arguments
add3(11, 22, 33)
#function with 5 aruguments
add3(1, 2, 3, 4, 5)
#function with 0 arguments
add3()
#function with negative argumenets
add3(-99, -1)

