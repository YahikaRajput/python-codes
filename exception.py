# num=10/0
# display bulit-in exceptions
# print(dir(locals()['__builtins__']))

# exception handling in python
try:
    num = 10
    denom = 0
    divresult = num/denom
    print(divresult)
except:
    print("denominator cannot be 0")    

