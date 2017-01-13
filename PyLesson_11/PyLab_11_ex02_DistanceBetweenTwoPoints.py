import math
class Distance:
    def __init__(self, x1, y1, x2, y2):
        self.xOne = x1
        self.yOne = y1
        self.xTwo = x2
        self.yTwo = y2
        self.distance = 0

    def selfValues(self, x1, y1, x2, y2):
        self.xOne = x1
        self.yOne = y1
        self.xTwo = x2
        self.yTwo = y2
        self.distance = 0

    def getDist(self):
        self.distance = math.sqrt((self.xTwo-self.xOne)*(self.xTwo-self.xOne)+(self.yTwo-self.yOne)*(self.yTwo-self.yOne))
        return self.distance

    def Resetx1(self):
        return self.xOne 

    def Resety1(self):
        return self.yOne 

    def Resetx2(self):
        return self.xTwo

    def Resety2(self):
        return self.yTwo
        
def main():
    xOne = int(input("Enter the first x-coordinate:"))
    yOne = int(input("Enter the first y-coordinate:"))
    xTwo = int(input("Enter the second x-coordinate:"))
    yTwo = int(input("Enter the second y-coordinate:"))

    calc1 = Distance(xOne, yOne, xTwo, yTwo)

    print("The distance between (",calc1.Resetx1(),",",calc1.Resety1(),") and (",calc1.Resetx2(),",",calc1.Resety2(),") is", calc1.getDist())
main()


        
