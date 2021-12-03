### Trevor Norton
### Project 8
### tangvv@umsystem.edu
import math

def print_menu():
    print("{:^}".format("Grade Menu"))
    print("1 - Add Test")
    print("2 - Remove Test")
    print("3 - Clear Tests")
    print("4 - Add Assignment")
    print("5 - Remove Assignment")
    print("6 - Clear Assignments")
    print("D - Display Scores")
    print("Q - Quit\n")

def new_check(new):
    while True:
        if (new > 100.0) or (new < 0.0):
            print("Score must be between 0 and 100.\n")
            new = float(input("Enter the new score 0-100 ==> "))
        else:
            return new
            break

def display(tests, ass):
    print("{:<18}{:<8}{:<10}{:<10}{:<5}{:>5}".format("Type", "#", "min", "max", "avg", "std"))
    print("========================================================")
    print("{:<18}{:<8}{:<10}{:<10}{:<5}{:>5}".format("Tests", len(tests), min(tests), max(tests), avg(tests), std(tests, (avg(tests)))))
    print("{:<18}{:<8}{:<10}{:<10}{:<5}{:>5}".format("Assignments", len(ass), min(ass), max(ass), avg(ass), std(ass, (avg(ass)))))
    print("Weighted Grade is:", weight(tests, ass))

def sum(list):
    sum = 0
    for i in range(0, len(list)):
        sum += float(list[i])
    return sum

def avg(list):
    sum = 0
    for i in range(0, len(list)):
        sum += float(list[i])
    return (sum / len(list))

def std(list, avg):
    add = 0
    for i in range(0, len(list)):
        add += float(list[i]) - avg
    std = math.sqrt(add / len(list))
    return std

def weight(tests, ass):
    sumt = 0
    suma = 0
    weight = 0
    for i in range(0, len(tests)):
        sumt += float(tests[i])
    for i in range(0, len(ass)):
        suma += float(ass[i])
    weight += ((sumt / (len(tests)*100)) * 0.6)
    weight += ((suma / (len(ass)*100)) * 0.4)
    return weight

tests = []
assignments = []
running = True
while running == True:
    print_menu()
    choice = input("==> ")
    if choice == "1":
        new = float(input("Enter the new Test score 0-100 ==> "))
        new = new_check(new)
        tests.append(new)
        print("Test Score", new, "has been added.")
    elif choice == "2":
        remove = int(input("Enter the number of the test you would like to remove."))
        tests.pop(remove + 1)
    elif choice == "3":
        tests = []
        print("Tests have been cleared.")
    elif choice == "4":
        new = float(input("Enter the new Assignment score 0-100 ==> "))
        new = new_check(new)
        assignments.append(new)
        print("Assignment Score", new, "has been added.")
    elif choice == "5":
        remove = int(input("Enter the number of the assignment you would like to remove."))
        assignments.pop(remove + 1)
    elif choice == "6":
        assignments = []
    elif choice == "d" or "D":
        display(tests, assignments)
    elif choice == "q" or "Q":
        running = False
