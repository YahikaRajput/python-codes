# Data Structures in Python
# 1.list
# create a list

list_ds = [] #create empty list
print(list_ds)

list_ds = [5,6,7,"list-data",5.55] #create list with data
print(list_ds)

# Operations on list
# adding elements in the  list

list_ds = [5,6,7]
print(list_ds)

list_ds.append([123,78]) # add element at the end
print(list_ds)

list_ds.extend([543,'example-extend'])
print(list_ds)

list_ds.insert(5,'example-insert') # add element at specific index
print(list_ds)

# accessing elements from the list
list_ds = [5,6,7,"access-the-elements",5.55,30,22]

# for <variable name> in <sequence>
for value in list_ds:
    print(value)
print(list_ds)
print(list_ds[2])# access element at index 2
print(list_ds[0:3])# access elements from index 0 to 2
print(list_ds[::-1])# display list in reverse order 

# removing / deleting elements from the list
list_ds = [5,6,7,"remove-the-elements",5.55,30,22]

del list_ds[2] # delete element at index 2
print(list_ds)

list_ds.remove('remove-the-elements') # remove specific element
print(list_ds)

poped = list_ds.pop(1) # remove last element and return it
print('poped element:',poped)
print('remaining list:',list_ds)

list_ds.clear() # remove all elements from the list
print(list_ds)

# write a python program to create a list of 20 elements out of which 5 elements are string , 5 elements are
# float and remaining  elements are integers. dislplay  the list element by element 
# access 5th element and replace it with a given character
# acces elements  from index 7 to 10 and display them
# add 5 integers towards the end of the list(original list)
# access 7th element and delete it (index number)
# delete the entire list

elements_list = [12,45.6,'hello',78,90,'world',23.4,56,67,'python',89.0,34,21,'data',11.11,100,200,300,'code',400,500]
for value in elements_list:
    print(value)
print('5th element:',elements_list[4])

elements_list.insert(5,'heloooo')
print(elements_list)

for value in elements_list:
    print(value)
print(elements_list[7:10])    
print(elements_list)

elements_list.extend([11,22,33,44,55])
print(elements_list)

popped = elements_list.pop(7)
print("popped element:",popped)
print("remaining element:",elements_list)

elements_list.clear()
print(elements_list)


