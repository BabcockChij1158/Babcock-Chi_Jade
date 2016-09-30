print("Do you wish to calculate an average of three numbers?")
num1 = float(input("Please enter number 1:"))
num2 = float(input("Please enter number 2:"))
num3 = float(input("Please enter number 3:"))

def average():
    output = "{:0.5f}".format((num1+num2+num3)/3)
    return output

print("The average of",num1,",",num2,", and",num3,"is",average(),".")
