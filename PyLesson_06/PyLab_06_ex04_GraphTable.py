repeat = int(input("Enter how often the number will repeat:"))
size = int(input("Enter the size of the table:"))

def calc(xVal, yVal): 
    for i in range(1, size+1):
        print("{:3}\t{:3}".format(xVal, yVal))

calc(repeat, size)
