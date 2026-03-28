#control flow
# if statement
# if condition:
#  block of code
# examples of if..else statements

#ex-1
setflag=True
if setflag:
    print("Hello everyone!!")
    print("Solve the assignments")

setflag=False
if setflag:
    print("Good afternoon everyone!!")
    print("Solve the assignments")
print("Executed false")    

#ex-2
no=3
if no < 5:
    print("Number is less than 5") 

# if condition:
#   block of if
# else:
#   block of else

#no=5
no=int(input("Enter the number:"))
if no % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")        

#if condition:
#    block of if
# elif condition2:
#    block of elif
#eilf condition3:
#    block of eilf
# ..(there can be more eilf)
# else:   
#    block of else

no=3
if no > 0:
    print("Number is positive")
elif no < 0:
    print("Number is negative")
else:
    print("Number is zero")    


#Questions
#1.check whether a person is eligible for voting accept the age from the user
#2.display "Attendence id mandatory for lectures" if the entered number is divisble by 5 otherwise display by " Byee See You"    
#3.display last digit of a number
#4.check whether the last digit of number entered by the user is divisble by 5
#5.check whether the year entered by the user is a leap year or not 

