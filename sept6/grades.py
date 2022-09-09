#Gather Grades
assignments = float(input("Assignments Grade: "))
excercises = float(input("Excercises Grade: "))
midterm = float(input("Midterm Grade: "))
final = float(input("Final Grade: "))
letterGrade = ""
finalGrade = assignments * .5 + excercises * .2 + midterm * .15 + final * .15

print(f"final grade is {finalGrade}")

if finalGrade >= 90:
    letterGrade = "A"
elif finalGrade >= 80:
    letterGrade = "B"
elif finalGrade >= 70:
    letterGrade = "C"
elif finalGrade >= 60:
    letterGrade = "D"
else: finalGrade = "F"

print(f"Letter Grade is {letterGrade}")