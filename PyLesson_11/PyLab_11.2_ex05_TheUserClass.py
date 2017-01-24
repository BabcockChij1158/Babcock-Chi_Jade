import random
class User:
    def __init__(self, fName, lName, avat = ""):
        self.firstName = fName
        self.lastName = lName
        self.avatar = avat
        self.userID = random.randint(0, 1000000)
    
    def Modifier(self, fName, lName, avat = ""):
        self.firstName = fName
        self.lastName = lName
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

    def __str__(self):
        return "User Info...\nFirst Name: " + self.firstName + \
                           "\nLast Name: " + self.lastName + \
                           "\nAvatar: " + self.avatar + \
                           "\nUser ID#: " + str(self.userID)

def main():

    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")
    Question = input("Would you like to use a public avatar? y or n? ")

    if Question == "n":
        user1 = User(firstName, lastName)
    else:
        avatar = input("Enter your desired avatar name: ")
        user1 = User(firstName, lastName, avatar)
    print(user1)
    

main()
