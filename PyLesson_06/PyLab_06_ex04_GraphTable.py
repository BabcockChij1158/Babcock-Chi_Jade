integer = int(input("Enter an integer:"))
size = int(input("Enter the size of the table:"))

def calc(x, y): 
    print("{:2}\t{:3}".format(x, y)

for i in range(1, size+1):
    print(i, i*integer)

calc(integer, size)
