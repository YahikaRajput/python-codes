# Q4 write a menu driven program to see all the built in function of a string 
while True:
    print("Select a number to see what function you want to see")
    print("1 to see upper() function")
    print("2 to see lower() function")
    print("3 to see title() function")
    print("4 to see swapcase() function")
    print("5 to capitalize() function")
    print("6 to exit")

    str = 'my nAme iS AbhiShek'
    a = int(input("Choose a number which function you want to see: "))

    if(a == 1):
        print("upper() function is used to convert the string into uppercase")
        print("Before: ", str)
        print(str.upper())

    elif(a == 2):
        print("lower() function is used to convert the string into lowercase")
        print("Before: ", str)
        print(str.lower())

    elif(a == 3):
        print("title() function is used to convert the first character to upparcase")
        print("Before: ", str)
        print(str.title())

    elif(a == 4):
        print("swapcase() function is used to convert all string in lower to upper and viceversa ")
        print("Before: ", str)
        print(str.swapcase())

    elif(a == 5):
        print("capitalize() function is used to convert the first character into uppercase")
        print("Before: ", str)
        print(str.capitalize())

    elif(a == 6):
        print(exit)
        break

    else:
        print("Enter the correct number")