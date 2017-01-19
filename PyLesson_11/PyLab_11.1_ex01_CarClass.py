class Car:
    #Constructor
    def __init__(self, p, i, e, t):
        self.paint = p
        self.interior = i
        self.engine = e
        self.tires = t

    #Modifier
    def setCustom(self, p, i, e, t):
        self.paint = p
        self.interior = i
        self.engine = e
        self.tires = t

    #Accessors
    def getPaint(self):
        return self.paint

    def getInterior(self):
        return self.interior

    def getEngine(self):
        return self.engine

    def getTires(self):
        return self.tires

def main():
    paint = input("Enter the paint color:")
    interior = input("Enter the interior material:")
    engine = input("Enter the type of engine:")
    tires = input("Enter the type of tires:")

    print("Your vehicle is ready...")
    car1 = Car(paint, interior, engine, tires)
    print("Paint:      ",         car1.getPaint())
    print("Interior:   ",      car1.getInterior())
    print("Engine:     ",        car1.getEngine())
    print("Tires:      ",         car1.getTires())


main()
