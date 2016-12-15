values = []
values.append([1, 2, 3, 4]) #value[0]
values.append([5, 6, 7, 8]) #value[1]
values.append([9, 10, 11, 12]) #value[2]
values.append([13, 14, 15, 16]) #value[3]

print(values)
print(values[0][2]) #--> # goes to value[0] and then prints the position[2] in that list
                        # So this would print '3'

print("using range:")
for i in range(0, len(values)): # outer loop: (columns)there is an index value in the list 'values'
    output = ""
    for j in range(0, len(values[i])): # inner loop: (rows)there is also another index value in that index value bc is a list in a list
        output += str(values[i][j]) + "\t" #each time runs, add value at position j & i
    print(output)

print("enhanced for loop:")
for value in values:
    output = ""
    for num in value:
        output += str(num) + "\t"
    print(output)

print("---------------------------------------------------------------------------------------------")
print("\nSearch the list for multiples of 5")
count = 0
for value in values:
    for number in value:
        if number % 5 == 0:
            count += 1 #adds on more to count for every time it finds a multiple of 5
print("There are", count, "multiples of 5 in the list. \n\n")

print("print the multiples of 5")
count = 0
for value in values:
    for number in value:
        if number % 5 == 0:
            count += str(number) + ", "
print("The numbers," +count+, "are multiples of 5. \n\n")

print("printing the sum of mult of 5")
count = 0
for value in values:
    for number in value:
        if number % 5 == 0:
            count += number
print("There sum of the values in the list is equal to", count)
print("---------------------------------------------------------------------------------------------")

lettersList = []
lettersList.append(["a", "b", "c", "d"])
lettersList.append(["e", "f", "g", "h"])
lettersList.append(["i", "j", "k", "l"])
lettersList.append(["m", "n", "o", "p"])

print("\nHere is a list with letters...")

for letters in lettersList:
   output = ""
   for letter in letters:
       output += str(letter) + "\t" #dont need str
   print(output)

print("\nHere is a list of words using split()...\n")
wordsList = []
go = "father mother eagle house car office coffee make create laugh cry photo"
spList = go.split(" ")#will make each value before/after a space a value in a list
print(spList)
spot = 0 #keeps track of where we are in spList

for i in range(0, 3): #handles the columns
   output = ""
   wordsList.append([])
   for j in range(0, 4):#creates new index
       wordsList[i].append(spList[spot])#adds new list ino the index(rows)
       output += "{:15}".format(wordsList[i][j])
       spot += 1 #skip to the next index, so when print father, can move onto mother and so on...
   print(output)

































   
