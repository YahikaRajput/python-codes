# Q1 Write a program to create a menu driven program to see all the built in function od a list 
while True:
    print("Select a number to which built in function you want to see")
    print("1 to see append() function")
    print("2 to see copy() function")
    print("3 to see clear() function")
    print("4 to see count() function")
    print("5 to see extend() function")
    print("6 to see index() function")
    print("7 to see insert() function")
    print("8 to see pop() function")
    print("9 to see remove() function")
    print("10 to see reverse() function")
    print("11 to see sort() function")
    print("12 to exit")

    a= int(input("Choose a number which function you want to see: "))
    list = [10, 20, 30, 40, 30]
    if(a == 1):
        print("Append() function is used to add an element to the end of the list")
        list.append(4)
        print(list)
    elif(a == 2):
        print("copy() function returns a shallow copy of the list")
        b = list.copy()
        print(b)
    elif(a == 3):
        print("clear() function is used to clear the list")
        list.clear()
        print(list)
    elif(a == 4):
        print("count() function will count the occurance of an specific element how many times it is occured ")
        print(list.count(30))
    elif(a == 5):
        print("extend() function is used to extend the list from other list")
        list.extend([7, 8])
        print(list)
    elif(a == 6):
        print("index() function is to find the index of a specific element")
        print(list.index(40))
    elif(a == 7):
        print("insert() function is used to insert an element at a specific position in the list")
        list.insert(1, 5698)
        print(list)
    elif(a == 8):
        print("pop() function is used to pop the last element of the list")
        list.pop()
        print(list)
    elif(a == 9):
        print("remove() function is used to remove the first occurrence of a specified element from the list")
        list.remove(30)
        print(list)
    elif(a == 10):
        print("reverse() function is used to reverse the order of the elements in the list")
        list.reverse()
        print(list)
    elif(a == 11):
        print("sort() function is used to sort the list in ascending order")
        print("before sort(): ", list)
        list.sort()
        print("after sort(): ", list)
    elif(a == 12):
        print(exit)
        break

    else:
        print("Select the correct input the entered number is wrong input")