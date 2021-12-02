### Trevor Norton CS101L
### Program 6
### Tangvv@umsystem.edu
while True:
    mpgfind = (input("Enter the minimum MPG\n"))
    try:
        float(mpgfind)
        break
    except ValueError:
        print("You must enter a number for the fuel economy")
    if 0 > int(mpgfind) > 100:
        print("Fuel Economy must be between 0 and 100")

while True:
    x = input("\nEnter the name of the input vehicle file\n")
    try:
        with open(x):
            break
    except FileNotFoundError:
        print("Enter a valid file name.")

while True:
    y = input("\nEnter the name of the output file.")
    try: 
        with open(y):
            break
    except IOError:
        print("There is an IOError")
    except FileNotFoundError:
        print("Enter a valid file name.")

with open(x) as opened:
    with open(y) as f:
        for line in opened:
            lst = [i for i in line.split("\t")]
            try:
                f.write("{:<40}{:>10}".format((lst[0], lst[1], lst[2]), int(lst[7])))
            except ValueError:
                print("Could not convert value for", lst[0], lst[1], lst[2])
