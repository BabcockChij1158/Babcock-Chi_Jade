r = float(input("What is the radius of the circle?"))
area = ((r**2)*3.14159265359)

def calArea(area):
    output = "{:0.5f}".format(area)
    return output

print("The area of a circle with a radius of", r ,"is", calArea(area),".")
