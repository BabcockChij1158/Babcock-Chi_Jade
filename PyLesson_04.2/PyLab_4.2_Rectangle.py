length = float(input("What is the length of the rectangle?"))
width = float(input("What is the width of the rectangle?"))

def calcPerim():
    output = "{:.5f}".format((length*2)+(width*2))
    return output

print("Your rectangle is",calcPerim(), "square ft around.")
