import random
numbers = []

for i in range(0,10):
    numbers.append(random.randint(1, 101))


print("Before... ")
output = ""
for i in numbers:
    output += str(i) + " "  
print(output)

def average(numbers):
    average = 0
    for number in numbers:
        average += number
    return average / len(numbers)

print("")

print("The average of the above numbers is...", average(numbers))




