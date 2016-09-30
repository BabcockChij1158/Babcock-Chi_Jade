def subwoof(number):
    output = "{:<20.4}".format(number)
    return output

l = float(input("Enter the length of your subwoofer in inches:"))
w = float(input("Enter the width of your subwoofer in inches:"))
h = float(input("Enter the height of your subwoofer in inches:"))
V = (l*w*h)
cubicfeet = V/(12**3)
print("There are" ,cubicfeet,"ft^3 in your subwoofer.")
