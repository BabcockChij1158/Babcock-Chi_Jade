user = input("Enter a list of 5 words separated by a space:")
words = user.split(" ")

print("In order...")

for i in range(0, len(words), 1):
    print(words[i])

print("")
print("Reversed...")

for i in range(len(words)-1, -1, -1):
    print(words[i])


















    
