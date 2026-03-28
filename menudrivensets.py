# Q5 write a menu driven program to see all built in function of sets
while True:
    print("Select a number to see which function you want to perform")
    print("1 to see add() function")
    print("2 to see discard() function")
    print("3 to see remove() function")
    print("4 to see pop() function")
    print("5 to see clear() function")
    print("6 to exit")

    set = {1, 2, 3, 4, 5}
    a = int(input("Enter your choice: "))

    if(a == 1):
        print("add() function is used to add a element in the set")
        set.add(50)
        print(set)

    elif(a == 2):
        print("discard() function is used to discard an element from the set")
        set.discard(4)
        print(set)

    elif(a == 3):
        print("remove() function is used to remove a element from the set")
        set.remove(5)
        print(set)

    elif(a == 4):
        print("pop() function is used to pop an element from the set")
        set.pop()
        print(set)

    elif(a == 5):
        print("clear() functon is used to clear the set")
        set.clear()
        print(set)

    elif(a == 6):
        print(exit)
        break

    else:
        print("Enter the correct number")