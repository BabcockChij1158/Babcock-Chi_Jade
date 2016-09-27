length = float(input("What is the length of the rectangle?"))
width = float(input("What is the width of the rectangle?"))
perimeter = ((length*2)+(width*2))

def calcPerim(perimeter):
    print("{:12.5}".format(perimeter))

print("Your rectangle is",perimeter, "square ft around.")
