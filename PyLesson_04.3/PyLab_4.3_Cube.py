
def calcSurf():
    global side, sa 
    side = float(input("Enter the length of one of the sides of the cube:"))
    sa = (side**2)*6 #how do you format without return
def printf():
    print("The surface area of a cube whose sides are",side,"in length is {:0.5f}.".format(sa))

calcSurf()
printf()
