########################################################################
##
## CS 101 Lab
## Program # 5
## Trevor Norton
## tangvv@umsystem.edu
##
########################################################################

import string

def character_value(char : str) -> int:
    ''' Returns 0 for A, 1 for B, etc. '''
    value = []
    x = ord(char)
    value.append[x]
    return value
    

def get_check_digit(idnumber : str) -> int:
    ''' Returns the check digit for the name and sid. '''
    card = []
    for i in (idnumber):
        card.append[i]

def is_valid(idnumber : str) -> tuple:
    ''' returns 2 values bool and a string with errors if bool is False '''
    card = []
    for i in (idnumber):
        card.append[i]
    

def verify_check_digit(idnumber : str) -> tuple:
    card = []
    for i in (idnumber):
        card.append[i]
    ''' returns True if the check digit is valid, False if not '''

def get_school(idnumber : str) -> str:
    ''' Returns the school the 5th index or 6th character is for. '''
    card = []
    for i in (idnumber):
        card.append[i]
    if(card[5] == 1):
        school = 
  

def get_grade(idnumber : str) -> str:
   '''Returns the grade for index 6'''
   card = []
   for i in (idnumber):
        card.append[i]
   if(card[6] == 1):
        grade = "Freshman"
   elif(card[6] == 2):
        grade = "Sophomore"
   elif(card[6] == 3):
       grade = "Junior"
   elif(card[6] == 4):
       grade = "Senior"
   else:
       grade = "Invalid Grade"
   return grade
    

if __name__ == "__main__":

    print("{:^60}".format("Linda Hall"))
    print("{:^60}".format("Library Card Check"))
    print("="*60)

    while True:

        print()
        card_num = input("Enter Libary Card.  Hit Enter to Exit ==> ").upper().strip()
        if card_num == "":
            break
        result, error = verify_check_digit(card_num)
        if result == True:
            print("Library card is valid.")
            print("The card belongs to a student in {}".format(get_school(card_num)))
            print("The card belongs to a {}".format(get_grade(card_num)))
        else:
            print("Libary card is invalid.")
            print(error)
        