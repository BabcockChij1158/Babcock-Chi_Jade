class MilesPerHour:
    #Constructor
    def ___init___(self, d, h, m):
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
        return mph
    
def main():
    distance = input("Enter the distance:")
    hours = input("Enter the hours:")
    minutes = input("Enter the number of minutes:")

    calc1 = MilesPerHour(distance, hours, minutes)

    print("If you travel", calc1.getDist(), "miles in", calc1.getHours(),"and", calc1.getMins(), "minutes, your speed will be ", calc1.getMPH(),"mph.")

    calc1.getDist(distance)
    calc1.getHours(hours)
    calc1.getMinutes(minutes)

    print("If you travel", calc1.getDist(), "miles in", calc1.getHours(),"and", calc1.getMins(), "minutes, your speed will be ", calc1.getMPH(),"mph.")

main()

