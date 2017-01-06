xAndo = []
import random

for i in range(0, 4):
    xAndo.append([])
    for j in range(0, 4):
        switch = random.randint(0, 2)
        if switch == 1:
            xAndo[i].append("X")
        else:
            xAndo[i].append("O")

for values in xAndo:
    output = ""
    for value in values:
        output += str(value) + " "
    print(output)
