# data structures
# 3. dictionary

dict1 = {}
print(dict1)
dict1 = {1 : 'AI' , 2: 'Microserveices using Java' , 3: 'Cloud Computing'}
print(dict1)

dict1[3] = 'Cloud'# change the value
print(dict1)

dict1 = {'First': 'Lab on Python', 'Second': 'Lab on Microservices', 'Third': 'Lab on Art'}
print(dict1)

dict1['Second'] = 'Next Generation Database'
print(dict1)

# Accessing
print(dict1['First'])
print(dict1.get('Second'))
print(dict1.keys())
print(dict1.values())
print(dict1.items())

# Deleting
popedvalue = dict1.pop('Third')
print('Value:', popedvalue)
print('Dictionary:', dict1)

popKeyvalue = dict1.popitem()
print('Key, value pair:', popKeyvalue)
print('Dictionary', dict1)

dict1.clear()
print('ndict', dict1)

 
