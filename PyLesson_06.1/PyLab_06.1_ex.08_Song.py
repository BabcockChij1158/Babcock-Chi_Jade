
def song(word, number):
    output = ""
    for i in range(number): #you can just have the range as a number, there is a shortcut where it defaults to 0 and 1 for the other two values, so you can put them in but not need to.
        output = output + word + " "
    print(output)

song("Na",4)
song("Na",4)
song("Hey",3)
song("Goodbye!",1)
