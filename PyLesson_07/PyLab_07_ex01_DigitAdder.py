number = int(input("Enter in an integer:"))

Sum = 0
num = number

def sumDigits():
    while num > 0:
        #Sum = Sum + 1 you need to fix this
        num = int(num / 10)

print("The sum of the digits in", number,"is", Sum)
