# Q1.write python program to accept two list from the user and display it
# Q2. create two list with 10 elements each combine both the lsit and store it in the
#  third list and display it.
# Q3. create a tuple of five elements , accees second index store a value at that index and 
# display the entire tuple.

#Q1
a = list(input("Enter the first list: "))
print(a)

b = list(input("Enter the second list: "))
print(b)

#Q2
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [20,30,40,50,60,70,80,90,100,110]
list3 = []
list3.extend(list1)
list3.extend(list2)
print(list3)

#Q3
tuple_ds=()
type(tuple_ds)
tuple_ds=(1,2,3,4,5)
print(tuple_ds)

 



