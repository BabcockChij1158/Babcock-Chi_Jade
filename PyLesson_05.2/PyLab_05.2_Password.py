name = "joe.schmoe"
secret = "rainyday123"

def passCheck():
    username = input("Username:")
    password = input("Password:")
    if username == name and password == secret:
        print("You are granted access!")
    if username == name and password != secret:
        print("Your password is incorrect! Try again!")
        passCheck()
    if username != name and password == secret:
        print("Your username is incorrect! Try again!")
        passCheck()
    if username != name and password != secret:
        print("Your username and password are incorrect! Try again.")
        passCheck()

passCheck()
