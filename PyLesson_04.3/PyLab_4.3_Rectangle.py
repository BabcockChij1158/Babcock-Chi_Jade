
def calcPerim():
    global length, width, perimeter
    length = float(input("Enter the length of the rectangle:"))
    width = float(input("Enter the width of the rectangle:"))
    perimeter = ((length*2)+(width*2))#how do you format without return
def printf():
    print("Your rectangle is {:0.5f} feet around.".format(perimeter))

calcPerim()
printf()
