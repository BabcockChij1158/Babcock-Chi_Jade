#problem 1
item1 = float(input("Please enter the cost of the first item:"))
item2 = float(input("Please enter the cost of the second item:"))

def Format(one, two):
    print("The total cost of your order is ${:7.2f}".format(one+two))

Format(item1, item2)

#problem 2
#skip, see receipt lab

#problem 3
num1 = 5
num2 = 7
num3 = 9

numPrint(num1, num2, num3)

def calcAvg(one, two, three):
    return(one + two + three)/3

def numPrint(one, two, three):
    avg = calcAvg(one, two, three)
    print("The average of", one, two,"and",three,"is",avg)
#error message

#problem 4
