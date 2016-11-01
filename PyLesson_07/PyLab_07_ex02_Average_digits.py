number = int(input("Enter in an integer:"))
digits = 0
average = 0
num = number

def avDigits(num, average, digits):
    while num > 0:
        digits += 1
        average += num % 10
        num = int(num / 10)
    average /= digits
#the /= and += mean variable = variable * or + the number or variable after it, it is a shortcut
    return average

print("The average of the digits in", number,"is" ,avDigits(num, average, digits))

