def loan(number):
    output = "{:<10.2f}".format(number)
    return output

P = float(input("Enter your principal, the starting amount:"))
r = float(input("Enter your interest rate in decimal:"))
n = int(input("Enter the number of times the loan is compunded per year:"))
t = int(input("Enter the life of the loan, in years:"))
number = P*((1+r/n)**(n*t))

print("$",loan(number))
