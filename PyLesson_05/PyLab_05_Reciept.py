def printf(item, price):
    print("*{:>16} ........ {:>8.2f}".format(item, price))
    
item1 = input("Please enter item 1:")
price1 = float(input("Please enter the price:"))
item2 = input("Please enter item 2:")
price2 = float(input("Please enter the price:"))
item3 = input("Please enter item 3:")
price3 = float(input("Please enter the price:"))
item4 = input("Please enter item 4:")
price4 = float(input("Please enter the price:"))

subtotal = (price1+price2+price3+price4)
tax = (subtotal*0.08)
discount = subtotal*0.15

def calcdiscount():
    if subtotal >= 2000:
        discount = 0.15

    if not subtotal >= 2000:
        discount = 0.00

total = subtotal - discount + tax


print("<<<<<<<<<<<<<<<__Receipt__>>>>>>>>>>>>>>>")
print("")
printf(item1, price1)
printf(item2, price2)
printf(item3, price3)
printf(item4, price4)
print("")
printf("Subtotal:", subtotal)
printf("Tax:", tax)
printf("Discount:", discount)
printf("Total:", total)
#same thing for tax, and total
print("_________________________________________")
#Print thank you message
print("     * Thank you for your support *")
