



def printf(word, number):
    print("{:<6}\t{:10.2f}".format(word, number))

    
word = "blah!"
number = 92744.234

printf(word, number)

word = "ohboy!"
number = 927474.456

printf(word, number)


text = "Yay!"
number = 846.234
print("*" *20)
print("{:<10}{:10.2f}".format(text, number))
#add up the number of spaces (10+10) then perform the appropriate opperation.
