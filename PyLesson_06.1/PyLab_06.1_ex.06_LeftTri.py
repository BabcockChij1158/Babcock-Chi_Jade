word = input("Enter in a word:")

def reverse():
    for i in range(0,len(word),1):
        print(word[i:len(word)])

reverse()
