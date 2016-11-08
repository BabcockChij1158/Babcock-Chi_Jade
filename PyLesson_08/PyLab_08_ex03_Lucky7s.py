number = int(input("Please enter an integer:"))

def luck(number):
    if number > 0:
        if number % 10 == 7:
            return 1 + luck(int(number/10))
        else:
            return 0 + luck(int(number/10))
    else:
        return 0

print("The number of 7's in your number is" ,luck(number))
    
