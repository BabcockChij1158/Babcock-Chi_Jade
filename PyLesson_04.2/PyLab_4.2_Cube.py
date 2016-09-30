side = float(input("Enter the side length:"))

def calcSurf():
    output = "{:0.5f}".format((side**2)*6)
    return output
    
print("The surface area of a cube with a", side ,"side length is", calcSurf(),"units^2.")
