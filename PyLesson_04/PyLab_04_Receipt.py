

print("<<<<<<<<<<<<<<<__Receipt__>>>>>>>>>>>>>>>")


def printf(item, price):
    print("{:18}.\t{3.2f}".format(item, price))


item = input("Please enter item 1:")
price = input("Please enter the price:")

printf(item, price)

item = input("Please enter item 2:")
price = input("Please enter the price:")

printf(item, price)

item = input("Please enter item 3:")
price = input("Please enter the price:")

printf(item, price)
