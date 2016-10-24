word = input("Please enter in a word:")

def reverse():
    for i in range(len(word), 0, -1):
        print(word[0:i])

reverse()


