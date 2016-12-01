start = int(input("Please enter your starting number:"))
size = int(input("Please enter your sequence size:"))

seq = []

for i in range(0, size):
    if i is 0 or 1:
        seq.append(start)
        seq[i] = start
    else:
        seq[i] = sum([i-1]+[i-2])
print(str(seq[i]) + " ")
