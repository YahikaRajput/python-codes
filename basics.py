#basics
#here we store a value in variable
num1 = 5
num2 = 10.5

#this is to print the value
print("The Type is",type(num1))
print("The Type is",type(num2))

#to  display a value in other ways 
print('The value of num1 is {} and num2 is {}'.format(num1,num2))
str1="Good Morning"
print("The type of str1 is",type(str1))

#Input the data from user
num3 = int(input("Please enter the value"))
print(type(num3))

#Assiging multiple values to multiple variables
num11,num12,num13=10,11,12
print("The values of multiple variables are:")
print(num11,num12,num13)

number1=4
number2=7
#sum=number1+number2
print("The addition of two number is:", number1+number2)

#python literals
#Types of literal
#1.Numeric 2.Floating-point 3.complex literals 4.string 5.boolean 6.character literals 
# 7.special literals 8.list literals 

compl=6+9j
print("The complex literal is:",compl)

is_pass = True
print("The boolean literal:",is_pass)

str2='Hello World'
str3="Hello "
print("The string literal is:",str2)
print("The string literals= :",str2,str3)

ch = '@'
print('charcter literals is:',ch)

value = None
print("The special literal is:",value)

#python data types
number1 = 10
print(number1,'is of type',type(number1))

number2 =3.3
print(number2,'is of type',type(number2))

number3 = 3+5j
print(number3,'is of type',type(number3))

#operators in python
#1.arithmetic operators
num11 = 12
num12 = 7

#addition
print("Addition:",num11 + num12)
#subtraction
print("Subtraction:",num11 - num12)
#multiplication
print("Multiplication:",num11 * num12)
#division
print("Division:",num11 / num12)
#floor division
print("Floor Division:",num11 // num12)
#moduluo
print("Moduluo:",num11 % num12)
#num11 to the power num12
print("Power:",num11 ** num12)

#2.assignment operators
# assign 10 to Num1
Num1 = 10
#assign 6 to Num2
Num2 = 6
#assign the sum of Num1 and Num2 to Num1
Num1 += Num2 
#Num1 = Num1 + Num2
print(Num1)
Num1 -= 3
print(Num1)

#3.comparison operators 
Num1 = 8
Num2 = 10
print(Num1 > Num2)

#4.logiacl opeators (and,or,not)
Num1 = 7
Num2 = 4
print(Num1>2)and(Num2>=5)

#5.bitwise operators 

...