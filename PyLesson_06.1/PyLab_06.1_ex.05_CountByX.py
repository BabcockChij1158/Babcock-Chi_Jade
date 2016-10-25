number = int(input("Enter a small integer:"))
repeat = int(input("How much will you count up by each time?"))
output = ""

for i in range(number, 20, repeat):
    output = output + str(i) + "\t"
print(output)
