words = ["apple", "banana", "kiwi", "pear", "grape"]

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

output = ""
j = 0
def reverse():
    for i in range(len(words) - 1, -1, -1):
        output += words[i]
        
    print(output)

