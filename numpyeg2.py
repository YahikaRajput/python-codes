import numpy as np
# create a list named list1
list1 = (11,22,33,44)
# create numpy array using list1
arrayvar = np.array(list1)
print(arrayvar)

arrayvar1 = np.array([11,22,33,44])
print(arrayvar1)
# create an array with 5 elements filled with zeros
array1 = np.zeros(5)
print(array1)

# create an array with values from 1 to 8 with a #step of 2
array2 = np.arrange(1,9,2)
print("Using np.arrange(1,9,2):",array2)

# generate an a5rray of 5 random numbers
array1 = np.random.rand(5)
print(array1)

# create an empty array of length 4
array1 =np.empty(4)
print(array1)

# create a 2d array with 2 rows and 2 columns 
array1 = np.array([[1,2,3,4],[5,6,7,8]])
print(array1)

# in pandas we can explicity specify
# the data type of array elements
#creating a pandas.array of integers

array_int =np.array([1,2,3,4,5],dtype='int')
print(array_int)
print()

# create a pandas.array of floating-point numbers
array_float =np.array([1.1,2.2,3.3,4.4,5.5],dtype='int')
print(array_float)
print()

# creating a pandas.array of strings
array_string = np.array(['apple','banana','cherry','date'],dtype='str')
print(array_string)
print()

# creating a pandas.array of boolean values
array_boolean = np.array([true,false,true,false],dtype='bool')
print(array_boolean)
print()

# create a pandas array 
arrayp = np.array([18,20,19,21,22])

# create a pandas series from the panda array
series_array = np.series(arrayp)
print(series_array)
