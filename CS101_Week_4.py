########################################################################
##
## CS 101 Lab
## Program #
## Name
## Email
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#import modules needed
import random

def play_again(reply) -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    valid = False
    while(valid == False):
        if(reply == "N" or "n" or "no" or "NO"):
            valid = True
            return False
        elif(reply == "Y" or "y" or "yes" or "YES"):
            valid = True
            return True
        else:
            valid = False 
            print("You must enter in N/NO/Y/YES")
     
def get_wager(bank) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    wager = int(input("How much would you like to wager?"))
    while True:
        if(wager > bank or wager < 0):
            wager = int(input("Wager must be a positive amount that is less than or equal to the amount of money you have in the bank.\n How much would you like to wager?"))
        else:
            return wager          

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    a = random.randint(0,10)
    b = random.randint(0,10)
    c = random.randint(0,10)
    return a, b, c

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if(reela == reelb and reelb == reelc):
        matches = 3
    elif(reela == reelb or reela == reelc or reelb == reelc):
        matches = 2
    else:
        matches = 0
    return matches

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    while True:
        value = int(input("Value must be between 0 and 100.\n How many chips would you like to start with?"))
        if(value > 100 or value < 0):
            print("Try again")
        else:
            return value

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if(matches == 3):
        payout = wager * 10
    elif(matches == 2):
        payout = wager * 3
    else:
        payout = wager * -1
    return payout


if __name__ == "__main__":

    playing = True
    while (playing == True):
        spins = 0
        bank_max = []
        bank = get_bank()

        while(bank > 0):  # Replace with condition for if they still have money.
            
            wager = get_wager(bank)
            bank_max.append(bank)
            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
            spins += 1
           
        print("You lost all in", spins, "spins")
        print("The most chips you had was", max(bank_max))
        playing = play_again(input("You must enter Y/YES/N/NO to continue."))