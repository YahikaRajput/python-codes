# Q1 - create a dictionary of bca sem 4 subjects the key should a string and the values should be the names of the subjects 
# aceess the second key and replace its value with mini project after this display the entire dictionary
# pop third key from the dictionary and display its value 

dict = {'First': 'Java', 'Second': 'python', 'Third': 'coding block'}
print(dict)

print(dict['Second']) == 'Mini Project'
print(dict)

pop = dict.pop('Third')
print('poped:', pop)
print("Dictionay", dict)