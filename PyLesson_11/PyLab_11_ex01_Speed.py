class MilesPerHour:
    #Constructor
    def __init__(self, d=0, h=0, m=0):
        self.distance = d
        self.hours = h
        self.minutes = m
        self.mph = 0

    #Modifier
    def SetValues(self, d, h, m):
        self.distance = d
        self.hours = h
        self.minutes = m
        self.mph = 0

    #Acccesor
    def getDist(self):
        return self.distance

    def getHours(self):
        return self.hours        

    def getMins(self):
        return self.minutes

    def getMPH(self):
        self.mph = self.distance/ (self.hours + (self.minutes / 60.0))
        return self.mph
    
def main():
    distance = int(input("Enter the distance:"))
    hours = int(input("Enter the hours:"))
    minutes = int(input("Enter the number of minutes:"))

    print("Using the constructor...")
    calc1 = MilesPerHour(distance, hours, minutes)
    print("If you travel", calc1.getDist(), "miles in", calc1.getHours(),"hours and", calc1.getMins(), "minutes, your speed will be ", calc1.getMPH(),"mph.")

    print("\nUsing the Modifier/Setter...")
    calc1.SetValues(500, 5, 50)
    print("If you travel", calc1.getDist(), "miles in", calc1.getHours(),"and", calc1.getMins(), "minutes, your speed will be ", calc1.getMPH(),"mph.")

main()

