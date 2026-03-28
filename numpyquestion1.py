#write pyhton program to implement numpy library to do the following 
#1)create an array which stores number from 1 to 1000 stepup by 100
#2)create an empty array of 10 numbers
#3)create a 2d array which stores 20 numbers 


#1)
import numpy as np
array = np.arange(1, 1000, 100)
print(array)

#2)
array = np.empty(10)
print(array)

#3)
array = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],[11 ,12, 13, 44, 55, 66 ,77 ,88 ,99 ,00]])
print(array)