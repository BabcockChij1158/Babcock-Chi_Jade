go = input("Enter in 16 words...")
splitList = go.split(" ")
wordsList = []
spot = 0

for i in range(0, 4):
    output = ""
    wordsList.append([])
    for j in range(0, 4):
        wordsList[i].append(splitList[spot])
        output += "{:8}".format(wordsList[i][j])
        spot += 1
    print(output)
