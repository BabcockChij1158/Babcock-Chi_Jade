number = ((0.01/24+1)**12*5)
print(number)

num = 4
num2 = 5
total = 0

def calcSum():
    global total, num, num2
    total = num + num2

def printf():
    print(num,"plus",num2,"is",total)

calcSum()
printf()
