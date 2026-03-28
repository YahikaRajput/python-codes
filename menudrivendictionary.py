# Q3 write a menu driven program to see all built in function of a dictionary
while True:
    print("Select a number to which function you want to see")
    print("1 to see clear() function")
    print("2 to see get() function")
    print("3 to see items() function")
    print("4 to see keys() function")
    print("5 to see update() function")
    print("6 to see values() function")
    print("7 to see pop() function")
    print("8 to see popitem() function")
    print("9 to exit")

    dict = {'Name' : 'ikaa', 'Age' : 23, 'Country':'India'}
    a = int(input("Choose a number: "))

    if(a == 1):
        print("clear() function is used to clear the dictionary")
        dict.clear()
        print(dict)

    elif(a == 2):
        print("get() function help to obtain the value linked to a particular key in the dictionary")
        print(dict.get('Name'))
        print(dict.get('Country'))

    elif(a == 3):
        print("items() function is used that retrieves a view object containing a list of tuples")
        print(list(dict.items())[1][0])
        print(list(dict.items())[1][1])

    elif(a == 4):
        print("keys() function is used return a view object with dictionary keys")
        print(dict.keys())

    elif(a == 5):
        print("update() function is used to update  the elements in the dictionary from other dictionary")
        dict2 = {'Name' : 'xyz', 'Age':56}
        dict.update(dict2)
        print(dict)

    elif(a == 6):
        print("values() function is used to return a view object containing all dictionary values")
        print(dict.values())

    elif(a == 7):
        print("pop() function is used to pop the value using its key")
        dict.pop('Age')
        print(dict)

    elif(a == 8):
        print("popitem() function is used to pop the last inserted key value")
        dict.popitem()
        print(dict)
        dict.popitem()
        print(dict)

    elif(a == 9):
        print(exit)
        break

    else:
        print("Enter the correct number")