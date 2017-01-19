class Human:
    #Constructor
    def __init__(self, h, e, s):
        self.hair = h
        self.eyes = e
        self.skin = s

    #Modifier
    def setHES(self, h, e, s):
        self.hair = h
        self.eyes = e
        self.skin = s

    #Accessors
    def getHair(self):
        return self.hair

    def getEyes(self):
        return self.eyes

    def getSkin(self):
        return self.skin

def main():
    hair = input("Enter your hair color: ")
    eyes = input("Enter your eye color: ")
    skin = input("Enter your skin color: ")

    print("My info...")
    human1 = Human(hair, eyes, skin)
    print("Hair:     ", human1.getHair())
    print("Eyes:     ", human1.getEyes())
    print("Skin:     ", human1.getSkin())

    print("\nFriend's Info...")
    human1.setHES("blonde", "blue", "white")
    print("Hair:     ", human1.getHair())
    print("Eyes:     ", human1.getEyes())
    print("Skin:     ", human1.getSkin())    

main()

