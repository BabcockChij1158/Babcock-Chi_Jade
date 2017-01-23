import random
class Item:
    def __init__(self, m, n, c, p)
        self.manufacturer = m
        self.name = n
        self.category = c
        self.price = p
        self.UPCcode = random.randint(1000000000, 10000000000)

    def Modifier(self, m, n, c, p)
        self.manufacturer = m
        self.name = n
        self.category = c
        self.price = p
        self.UPCcode = random.randint(1000000000, 10000000000)

    def getManu(self):
        return self.manufacturer

    def getName(self):
        return self.name

    def getCate(self):
        return self.category

    def getPrice(self):
        return self.price

    def getUPC(self):
        return self.UPCcode

def main():

    item1 = Item()

    name = input("Name of the product: ")
    manufacturer = input("Name of the manufacturer: ")
    Question = input("Would you like to enter category and price information? y or n?" )

    if Question == "n":
        item1 = Item(name, manufacturer)
    if Question == "y":
        cat = input("Enter the item's category: ")
        return cat
        pri = input("Entet the item's price: ")
        return pri
        item1 = Item(name, manufacturer, category, price)


    













    
    
    

