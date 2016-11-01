number = int(input("Enter in an integer:"))
Sum = 0
num = number

def sumDigits(num, Sum):
    while num > 0:
        Sum = Sum +(num %10)
        num = int(num / 10)
    return Sum

print("The sum of the digits in", number,"is", sumDigits(num, Sum))
