# -------- LIST FUNCTIONS --------
def listfunctions():
    while True:
        print("\nSelect a number to see list function")
        print("1. append()")
        print("2. copy()")
        print("3. clear()")
        print("4. count()")
        print("5. extend()")
        print("6. index()")
        print("7. insert()")
        print("8. pop()")
        print("9. remove()")
        print("10. reverse()")
        print("11. sort()")
        print("12. exit")

        try:
            a = int(input("Enter your choice: "))
        except:
            print("Invalid input!")
            continue

        my_list = [10, 20, 30, 40, 30]

        if a == 1:
            print("append(): Adds element at end")
            my_list.append(4)
            print(my_list)

        elif a == 2:
            print("copy(): Returns copy of list")
            b = my_list.copy()
            print(b)

        elif a == 3:
            print("clear(): Clears list")
            my_list.clear()
            print(my_list)

        elif a == 4:
            print("count(): Counts occurrences of 30")
            print(my_list.count(30))

        elif a == 5:
            print("extend(): Adds another list")
            my_list.extend([7, 8])
            print(my_list)

        elif a == 6:
            print("index(): Finds index of 40")
            print(my_list.index(40))

        elif a == 7:
            print("insert(): Inserts at position")
            my_list.insert(1, 999)
            print(my_list)

        elif a == 8:
            print("pop(): Removes last element")
            my_list.pop()
            print(my_list)

        elif a == 9:
            print("remove(): Removes first 30")
            my_list.remove(30)
            print(my_list)

        elif a == 10:
            print("reverse(): Reverses list")
            my_list.reverse()
            print(my_list)

        elif a == 11:
            print("sort(): Sorts list")
            my_list.sort()
            print(my_list)

        elif a == 12:
            break

        else:
            print("Invalid choice!")


# -------- SET FUNCTIONS --------
def setfunctions():
    while True:
        print("\nSelect a number to see set function")
        print("1. add()")
        print("2. discard()")
        print("3. remove()")
        print("4. pop()")
        print("5. clear()")
        print("6. exit")

        try:
            a = int(input("Enter your choice: "))
        except:
            print("Invalid input!")
            continue

        my_set = {10, 20, 30, 40}

        if a == 1:
            print("add(): Adds element")
            my_set.add(50)
            print(my_set)

        elif a == 2:
            print("discard(): Removes element")
            my_set.discard(20)
            print(my_set)

        elif a == 3:
            print("remove(): Removes element")
            my_set.remove(30)
            print(my_set)

        elif a == 4:
            print("pop(): Removes element")
            my_set.pop()
            print(my_set)

        elif a == 5:
            print("clear(): Clears set")
            my_set.clear()
            print(my_set)

        elif a == 6:
            break

        else:
            print("Invalid choice!")


# -------- DICTIONARY FUNCTIONS --------
def dictionaryfunctions():
    while True:
        print("\nSelect a number to see dictionary function")
        print("1. clear()")
        print("2. get()")
        print("3. items()")
        print("4. keys()")
        print("5. update()")
        print("6. values()")
        print("7. pop()")
        print("8. popitem()")
        print("9. exit")

        try:
            a = int(input("Enter your choice: "))
        except:
            print("Invalid input!")
            continue

        my_dict = {'Name': 'ikaa', 'Age': 23, 'Country': 'India'}

        if a == 1:
            my_dict.clear()
            print(my_dict)

        elif a == 2:
            print(my_dict.get('Name'))

        elif a == 3:
            print(my_dict.items())

        elif a == 4:
            print(my_dict.keys())

        elif a == 5:
            dict2 = {'Name': 'xyz'}
            my_dict.update(dict2)
            print(my_dict)

        elif a == 6:
            print(my_dict.values())

        elif a == 7:
            my_dict.pop('Age')
            print(my_dict)

        elif a == 8:
            my_dict.popitem()
            print(my_dict)

        elif a == 9:
            break

        else:
            print("Invalid choice!")


# -------- STRING FUNCTIONS --------
def stringfunctions():
    while True:
        print("\nSelect a number to see string function")
        print("1. upper()")
        print("2. lower()")
        print("3. title()")
        print("4. swapcase()")
        print("5. capitalize()")
        print("6. exit")

        my_str = "my nAme iS yashika"

        try:
            a = int(input("Enter your choice: "))
        except:
            print("Invalid input!")
            continue

        if a == 1:
            print(my_str.upper())

        elif a == 2:
            print(my_str.lower())

        elif a == 3:
            print(my_str.title())

        elif a == 4:
            print(my_str.swapcase())

        elif a == 5:
            print(my_str.capitalize())

        elif a == 6:
            break

        else:
            print("Invalid choice!")


# -------- TUPLE FUNCTIONS --------
def tuplefunctions():
    while True:
        print("\nSelect a number to see tuple function")
        print("1. len()")
        print("2. max()")
        print("3. min()")
        print("4. sum()")
        print("5. sorted()")
        print("6. exit")

        my_tuple = (10, 30, 20)

        try:
            a = int(input("Enter your choice: "))
        except:
            print("Invalid input!")
            continue

        if a == 1:
            print(len(my_tuple))

        elif a == 2:
            print(max(my_tuple))

        elif a == 3:
            print(min(my_tuple))

        elif a == 4:
            print(sum(my_tuple))

        elif a == 5:
            print(sorted(my_tuple))

        elif a == 6:
            break

        else:
            print("Invalid choice!")


# -------- MAIN MENU --------
def main():
    while True:
        print("\n===== MAIN MENU =====")
        print("1. List")
        print("2. Set")
        print("3. Dictionary")
        print("4. String")
        print("5. Tuple")
        print("6. Exit")

        try:
            ch = int(input("Enter your choice: "))
        except:
            print("Invalid input!")
            continue

        if ch == 1:
            listfunctions()
        elif ch == 2:
            setfunctions()
        elif ch == 3:
            dictionaryfunctions()
        elif ch == 4:
            stringfunctions()
        elif ch == 5:
            tuplefunctions()
        elif ch == 6:
            print("Program Ended")
            break
        else:
            print("Invalid choice!")


# RUN PROGRAM
main()
