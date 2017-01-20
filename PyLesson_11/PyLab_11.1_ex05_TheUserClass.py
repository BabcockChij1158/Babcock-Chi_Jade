import random
class User:
    def __init__(self, fName, lName, avat = ""):
        self.firstName = fname
        self.lastName = lname
        self.avatar = avat
        self.userID = random.randint(0, 1000000)
    
    def Modifier(self, fName, lName, avat = ""):
        self.firstName = fname
        self.lastName = lname
        self.avatar = avat
        self.userID = random.randint(0, 1000000)

    def getFirst(self):
        return self.firstName

    def getLast(self):
        return self.lastName
    
    def getAva(self):
        return self.avatar

    def getUserID(self):
        return self.userID

def main():

    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    Question = input("Would you like to use a public avatar? y or n? ")

    user1 = User(firstName, lastName, avatar)

    if Question == "n":
        user1 = User(firstName, lastName)
    if Question == "y":
        blah = input("Enter your desired avatar name: ")
        return blah
        user1 = User(firstName, lastName, avatar)

    def __str__(self):
        return "User Info...\nFirst Name: " + self.firstName + \
                           "\nLast Name: " + self.lastName + \
                           "\nAvatar: " + self.avatar + \
                           "\nUser ID#: " + str(self.userID)

main()
