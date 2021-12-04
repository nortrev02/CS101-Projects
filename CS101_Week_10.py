
wordict = {}
while True:
    x = input("Please enter the full name of the file you would like to check.\n")
    try:
        with open(x) as inp:
            print("{:<10} {:<10} {:<10}".format("#", "Word", "Frequency"))
            print("===============================")
            for line in inp:
                raw_string = line.replace("\n", ",").replace("'", ",").replace("\t", ",").split(",")
                exclusive_string = []
                for i in raw_string:
                    if len(i) > 3:
                        if i not in exclusive_string:
                            exclusive_string.append(i) 
                    for i in range(0, len(exclusive_string) -1):
                        wordict[exclusive_string[i]] = raw_string.count(exclusive_string[i])
            break
    except FileNotFoundError:
        print("File Not Found. Please enter valid file.")

num = 1
for i in sorted(wordict.keys()):
    if num < 10:
        print("{:<10}{:<10}{:<10}".format(num, i, wordict[i]))
        num += 1

once = 0
for i in wordict:
    if wordict[i] == 1:
        once += 1

print("There are", once, "unique words that appear only once in this document.")
