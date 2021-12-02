print("Welcome to the LAB grade calculator!")
name = input("Who are we calculating grades for?\n")
labs = int(input("Enter the Labs Grade\n"))
if labs < 0:
    print("Value too low. Lab grade has been set to 0")
    labs = 0
elif labs > 100:
    print("Value too high. Lab grade has been set to 100")
    labs = 100
exams = int(input("Enter the Exams grade\n"))
if exams < 0:
    print("Value too low. Exam grade has been set to 0")
    exams = 0
elif exams > 100:
    print("Value too high. Exam grade has been set to 100")
    exams = 100
attn = int(input("Enter the Attendance grade\n"))
if attn < 0:
    print("Value too low. Attn. grade has been set to 0")
    attn = 0
elif attn > 100:
    print("Value too high. Attn. grade has been set to 100")
    attn = 100

weight = (labs*0.7) + (exams*0.2) + (attn*0.1)
if weight >= 90:
    grade = "A"
elif 80 <= weight < 90:
    grade = "B"
elif 70 <= weight < 80:
    grade = "C"
elif 60 <= weight < 70:
    grade = "D"
elif weight < 60:
    grade = "F"
print("The weighted grade for", name, "is:", weight)
print(name, "has a letter grade of", grade)