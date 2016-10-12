weight = float(input("Please enter your weight:"))
height = float(input("Please enter your height in inches:"))
bmi = (703*weight)/(height*height)

def calcCond():
    if bmi <= 18.5:
        return "underweight"
    elif bmi <= 24.9:
        return "normal"
    elif bmi <= 29.9:
        return "overweight"
    elif bmi <= 34.9:
        return "obese"
    elif bmi <= 39.9:
        return "very obese"
    elif bmi > 39.9:
        return "morbidly obese"

print("Your BMI is:",bmi)
print("Your are "+calcCond()+".")
