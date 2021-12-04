### Trevor Norton
### Assignment 9
### tangvv@umsystem.edu

import csv

def month_from_number(num):
    year = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    while True:
        if (num > 12) or (num < 0):
            print("Number must be between 1 and 12")
            num = int(input("Try Again"))
        else:
            return (year[num + 1])

def read_in_file(fname):
    crime = []
    while True:
        try:
            with open(fname) as crimef:
                for line in crimef:
                    crime.append([i for i in line.split(",")])
                return crime
                break
        except FileNotFoundError:
            print("File Not Found, Please Try Again")
            fname = str(input("Enter File Name"))

def create_reported_date_dict(list):
    keylist = []
    for i in list:
        keylist.append(list[i][1])
    key_count = {}
    for key in keylist:
        try:
            key_count[key] = key_count[key] + 1
        except KeyError:
            key_count[key] = 1
    return key_count

def create_offense_dict(list):
    keylist = []
    for i in list:
        keylist.append(list[i][7])
    key_count = {}
    for key in keylist:
        try:
            key_count[key] = key_count[key] + 1
        except KeyError:
            key_count[key] = 1
    return key_count

def create_offense_by_zip(list):
    keylist = []
    for i in list:
        keylist.append(list[i][13])
    key_count = {}
    for key in keylist:
        try:
            key_count[key].append(list[i][7])
        except KeyError:
            key_count[key] = []
            key_count[key].append(list[i][7])
    return key_count


# if __name__ == “__main__”:

fname = str(input("Enter name of file to open."))
crime = read_in_file(fname)
offense = create_offense_dict(crime)
zip_offense = create_offense_by_zip(crime)
show_offense = str(input("Input offense you would like to view data for."))
for i in offense:
    if i == show_offense:
        print(offense[i])
zip = str(input("Enter the zip code you would like to see the crime report of."))
for i in zip_offense:
    if i == zip:
        print(zip_offense[i])



