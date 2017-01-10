class MilesPerHour:
    #Constructor
    def ___init___(self, d, h, m):
        self.distance = d
        self.hours = h
        self.minutes = m
        mph = 0

    #Modifier
    def SetValues(self, Distance, Hour, Minutes):
        self.distance = Distance
        self.hours = Hours 
        self.minutes = Minutes
        mph = 0

    #Acccesor
    def getDist(self):
        return self.distance

    def getHours(self):
        return self.hours        

    def getMins(self):
        return self.minutes

    def getMPH(self):
        mph = distance/ (hours + (minutes / 60.0))
        return mph
    
def main():
    distance = input("Enter the distance:")
    hours = input("Enter the hours:")
    minutes = input("Enter the number of minutes:")

    calculation = MilesPerHour(distance, hours, minutes, mph)

    print("If you travel", user1.getDist(), "miles in", user1.getHours(),"and", user1.getMins(), "minutes, your speed will be ", user1.getMPH(),"mph.")

    
    
    print("If you travel", user1.getDist(), "miles in", user1.getHours(),"and", user1.getMins(), "minutes, your speed will be ", user1.getMPH(),"mph.")









    #user1.getDist(distance)
    #user1.getHours(hours)
    #user1.getMinutes(minutes)

    #print("__________Miles Per Hour__________")
    #print("If you travel", user1.SetDistance(), "miles in", user1.SetHours(),"and", user1.SetMinutes(), "minutes, your speed will be ", user1.SetMPH(),"mph.")

