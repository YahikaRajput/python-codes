# functions of list
# Q1. write a menu driven python program to  increment all build-in functions of list 
#  (example-len(),reverse()-build-in functions)

print("menu driven of the list functions")
print("select 1 to len()")
print("select 2 for max() of the list")
print("select 3 for min() of the list")
print("select 4 for sum() of the list")
print("select 5 for sorted() of the list")
print("select 6 for list() of the list")

a = int(input("Enter a number to see list functions:"))
if(a == 1):
    print("The function len() tells the number of element in the")
    list1 = [1,2,3,4]
    print(list1)
    print(len(list1))
elif(a == 2):
    print("The function max() to find the max in the list")
    list2 = [5,6,7,88]
    print(list2)
    print(max(list2))
elif(a == 3):
    print("The function min() to find the min element in the list")
    list3 = [5,6,7,88]
    print(list3)
    print(min(list3))
elif(a == 4):
    print("The function sum() does the sum of all elements persent in the list")
    list4 = [1,2,4]
    print(list4)
    print(sum(list4))
elif(a == 5):
    print("The function sorted() sorts the element in the list in ascending order")
    list5 = [1,4,2,5]
    print(list5)
    print(sorted(list5))
elif(a == 6):
    print("The function list() converts other data types into a list")
    s = "abc"
    print(s)
    print(list(s))
else:
    print("Wrong number enter the number btw 1 to 6 to see all the functions")


