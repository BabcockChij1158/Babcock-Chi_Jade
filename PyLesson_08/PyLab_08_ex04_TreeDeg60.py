word = input("Enter in a word:")
stop = len(word)
start = 0

def tree(word, start, stop):
    if start <= stop:
        print("{:>12}".format(word[0:start]))
#I just set the print formatting to 12, but how do you set it to the length of the word?
        start = start + 1
        return tree(word, start, stop)
    else:
        return "ERROR"
    
tree(word, start, stop)
