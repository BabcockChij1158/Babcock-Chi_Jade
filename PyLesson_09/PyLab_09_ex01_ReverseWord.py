words = ["apple", "banana", "kiwi", "pear", "grape"]

def reverse():
    output = ""
    for i in range(len(words)-1, -1, -1):
        output += words[i] + "\n"
    print(output)

print("In order...")

output = ""
j = 0
for i in words:
    output += (i)
    if j < len(words)-1:
        output += ", "
    j+=1
print(output)
print("")
print("Reversed...")

reverse()
#EDIT, user input

