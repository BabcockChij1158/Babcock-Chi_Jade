
def calcPoints(grade):
    if grade == "A":
        return 4.0
    if grade == "B":
        return 3.0
    if grade == "C":
        return 2.0
    if grade == "D":
        return 1.0
    if grade == "F":
        return 0.0


name = input("What is your name?")
math = input("What is your letter grade in math?")
science = input("What is your letter grade in science?")
english = input("What is your letter grade in english?")
history = input("What is your letter grade in history?")
elective1 = input("What is your letter grade in your 1st elective?")
elective2 = input("What is your letter grade in your 2nd elective?")
elective3 = input("What is your letter grade in your 3rd elective?")

points = calcPoints(math)+calcPoints(science)+calcPoints(english)+calcPoints(history)+calcPoints(elective1)+calcPoints(elective2)+calcPoints(elective3)
gpa = points/7
print(name+", your GPA is a",gpa,".")
