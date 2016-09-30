r = float(input("What is the radius of the circle?"))

def calArea():
    output = "{:0.5f}".format((r**2)*3.14159265359)
    return output

print("The area of a circle with a radius of", r ,"is", calArea(),".")
