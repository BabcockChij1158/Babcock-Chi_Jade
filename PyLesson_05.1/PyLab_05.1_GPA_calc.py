def calcPoints(grade):
    if grade == A:
        return 4.0
    if grade == B:
        return 3.0
    if grade == C:
        return 2.0
    if grade == D:
        return 1.0
    if grade == F:
        return 0.0

gPoints = calcPoints(math) + calPoints(science) 

gpa = gPoints/7

name = input("What is your name?")
math = input("what is your letter grade in math?")
science = input("what is your letter grade in science?")
english = input("what is your letter grade in english?")
history = input("what is your letter grade in history?")
elective1 = input("what is your letter grade in your 1st elective?")
elective2 = input("what is your letter grade in your 2nd elective?")
elective3 = input("what is your letter grade in your 3rd elective?")

print(name+", your GPA is",gpa,".")
