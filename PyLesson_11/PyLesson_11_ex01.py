class MilesPerHour:
    #Constructor
    def ___init___(self, d, h, m):
        self.distance = d
        self.hours = h
        self.minutes = m
        self.mph = 0

    #Modifier
    def SetDistance(self, d):
        self.distance = d

    def SetHours(self, h):
        self.hours = h

    def SetMinutes(self, m):
        self.minutes = m

    def SetMPH(self):
        self.mph = 0

    #acccesor
    def getDistance(self):
        return self.calcDistance
        mph = distance/ ((hours + (minutes / 60.0))
        
def main():
    distance = input("Enter the distance:")
    hours = input("Enter the hours:")
    minutes = input("Enter the number of minutes:")

    user1 = MilesPerHour(distance, hours, minutes, mph)

print("__________Miles Per Hour__________")
print(user1.SetDistance(), "miles in", user1.SetHours(),"and", user1.SetMinutes(), "minutes = ", user1.SetMPH(),"mph.")
