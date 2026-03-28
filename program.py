# python program to input number from the user (1,2,3,4,5,6,7) 
# if the number is 1- display sunday till saturday .. 
# if the user inputs any other number display invalid number

num = int(input("Enter the number (1-7):"))
if num ==1:
    print("Sunday")
elif num ==2:
    print("Monday")
elif num ==3:
    print("Tuesday")
elif num ==4:
    print("Wednesday")      
elif num ==5:
    print("Thursday")
elif num ==6:
    print("Friday")
elif num ==7:
    print("Saturday")
else :
    print("Invalid number")                            