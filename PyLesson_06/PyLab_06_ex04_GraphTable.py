integer = int(input("Enter an integer:"))
size = int(input("Enter the size of the table:"))

def calc(): 
    print("x-value \ty-value")
    print("_______________________")
    for i in range(1, size+1, 1):
        print(" ", i, "\t|\t", i*integer)
    print("  n\t\t",integer,"n")
calc()

#Do I need to have formal print formatting?
