
def calcArea():
    global r, area
    r = float(input("Enter the radius of the circle:"))
    area = (r**2)*3.14159265359 #how do you format without return
def printf():
    print("The area of a circle with a radius of",r,"is {:0.5f}.".format(area))

calcArea()
printf()
