########################################################################
##
## CS 101 Lab
## Program # 3
## Trevor Norton
## tangvv@umsystem.edu
##
## PROBLEM : I had to figure out how to reverse engineer the number from the remainders given.
##
## ALGORITHM : 
##      I took the remainders given by the user and took every number from 1 - 100 and found the number that matched.
## 
## ERROR HANDLING:
##      N/A
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
print("Welcome to the Flarsheim Guesser!")
print("Please think of a number between and including 1 and 100.\n")
num3 = int(input("What is the remainder of your number divided by 3 ?"))
if(0 > num3 > 2):
    print("Your number must have a remainder between and including 0 and 2")
num5 = int(input("What is the remainder of your number divided by 5 ?"))
if(0 > num5 > 4):
    print("Your number must have a remainder between and including 0 and 4")
num7 = int(input("What is the remainder of your number divided by 7 ?"))
if(0 > num7 > 6):
    print("Your number must have a remainder between and including 0 and 6")
for i in range (0,101):
    if (i % 3 == num3) and (i % 5 == num5) and (i % 7 == num7):
        print(i)