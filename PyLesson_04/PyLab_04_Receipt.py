def printf(item, price):
    print("*{:>16} ........ {:>8.2f}".format(item, price))

#input item1
item1 = input("Please enter item 1:")
price1 = float(input("Please enter the price:"))

#input item2
item2 = input("Please enter item 2:")
price2 = float(input("Please enter the price:"))

#input item3
item3 = input("Please enter item 3:")
price3 = float(input("Please enter the price:"))

#calculate subtotal
subtotal = (price1+price2+price3)

#calculate the tax
tax = (subtotal*0.08)

#calculate the Total
total = (subtotal + tax)


print("<<<<<<<<<<<<<<<__Receipt__>>>>>>>>>>>>>>>")
print("")
printf(item1, price1)
printf(item2, price2)
printf(item3, price3)
print("")
printf("Subtotal:", subtotal)
printf("Tax:", tax)
printf("Total:", total)
#same thing for tax, and total
print("_________________________________________")
#Print thank you message
print("     * Thank you for your support *")

