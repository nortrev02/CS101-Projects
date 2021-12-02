userFL = input("Please enter the full name of the file you would like to check.\n")
try:
    with open(userFL) as fl:
        ls = []
        for line in fl:
            ls.extend(i.upper() for i in line.split(" "))
    d = {}
    for i in ls:
        if i not in d:
            d[i] = ""
    for i in d:
        num = 0
        for j in range(0, len(ls)):
            if i == ls[j]:
                num += 1
        d[i] = num
    print("{:<10} {:<10} {:<10}".format("#", "Word", "Frequency"))
    print("===============================")
except(FileNotFoundError):
    print("File Not Found. Please enter valid file.")