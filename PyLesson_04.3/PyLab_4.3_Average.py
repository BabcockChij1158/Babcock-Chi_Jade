
def average():
    global num1, num2, num3, average
    num1 = float(input("Enter the value of number 1:"))
    num2 = float(input("Enter the value of number 2:"))
    num3 = float(input("Enter the value of number 3:"))
    average = (num1 + num2 + num3)/3 #how do you format without return
def printf():
    print("The average of",num1,",",num2,", and",num3,"is {:0.5f}.".format(average))

average()
printf()
