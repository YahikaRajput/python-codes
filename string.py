# data structures in python
# 4.strings.

# create a string using double quotes
string1 = "Python Programming"

# create  a string using single quotes
string1 = 'Python Programming'

# create string using variables
name = "string"
print(name)
message = "I Love Python"
print(message)

# access string characters in python
# 1. indexing
message = "hello"

# access  1st index element
print(message[1]) #"e"

# 2. use of negative index
message = 'hello'

# access 4th last element
print(message[-4]) #"e"

# 3.slicing
message = 'hello'

# access character  from the 1st index to 3rd index
print(message[1:4]) #"ell"

# strings are immutable (single character cannot be changed)
# message = 'Hello Everyone'
# message[0] = 'M'
# print(message)    (this gives error) 

# we can use variable name
message = 'Good Morning'
# assign new string to message variable
message = 'Hello Everyone'
print(message); #prints "Hello everyone"

# multiline stirng
message = """ basics is very important .
     it forms the foundation for placement """
print(message)

# operations on string --- compare two strings
str1 = "Hello .world"
str2 = "I Love You"
str3 = "Hello World!"
# compare str1 and str2
print(str1 == str2)
# compare str1 and str3
print(str1 == str3)

str1 = "Python Language"
print(len(str1))
print(str1.lower())
print(str1.upper())

str1 = "Java is object-oriented and Java is portable"
# calling function
str2 = str1.replace("Java","python")
# replaces all the occurances
# ḍisplaying result
print("Old String: \n ",str1)
print("New String: \n ",str2)

str3 = str1.replace("Java","python",1)
# replaces first occurances only
# displaying result
print(" Old String: \n",str1)
print("New String: \n",str2)

str1 = ":" #string
str2 = "HELLO" #iterable object
str3 = str1.join(str2)
print(str3)

