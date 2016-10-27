word = input("Enter in a word:")

def reverse():
    for i in range(len(word), -1, -1):
        print(word[i:len(word)])

reverse()
