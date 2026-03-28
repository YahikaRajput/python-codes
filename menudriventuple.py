# Q2 write a menu driven program to imlpliment all bulti - in functions of tuple.

while True:
    print("Select which build in function you want to see in tuple")
    print("1 to see len() function")
    print("2 to see max() function")
    print("3 to see min() function")
    print("4 to see sum() function")
    print("5 to see sorted() function")
    print("6 to exit")

    tuple = (10, 30, 20)
    a = int(input("Choose which function you want to see: "))

    if(a == 1):
        print("len() function is used to find the number of elements in the tuple")
        print(len(tuple))

    elif(a == 2):
        print("max() function is used to find the maximum element in the tuple")
        print(max(tuple))

    elif(a == 3):
        print("min() function is used to find the minimum element in the list")
        print(min(tuple))

    elif(a == 4):
        print("sum() function is used to find the sum of all the elements present in the tuple")
        print(sum(tuple))
    
    elif(a == 5):
        print("sorted() function is used to sort the elements in the tuple in ascending order")
        print(sorted(tuple))

    elif(a == 6):
        print(exit)
        break

    else:
        print("Choose the correct number")