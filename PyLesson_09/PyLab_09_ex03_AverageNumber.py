import random
numbers = []

for i in range(0,10):
    numbers.append(random.randint(1, 101))
print(numbers)

output = "" #make this string?

for i in numbers:
    i += " "
    print(output)

print("")

def average(numbers):
    average = 0
    for i in (0, len(numbers)):
        Sum += numbers[i]
        return Sum / len(numbers)
print("The average of the above numbers is...", average(numbers))
