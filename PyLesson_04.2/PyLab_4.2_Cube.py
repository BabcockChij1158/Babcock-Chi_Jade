side = float(input("Enter the side length:"))
sa = ((side**2)*6)

def calcSurf(sa):
    output = "{:0.5f}".format(sa)
    return output
    
print("The surface area of a cube with a", side ,"side length is", calcSurf(sa),"units^2.")
