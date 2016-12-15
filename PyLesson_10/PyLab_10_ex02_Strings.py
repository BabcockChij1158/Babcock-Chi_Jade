go = input("Enter in 6 words...")
splitList = go.split(" ")
wordsList = []
spot = 0

for i in range(0, 2):
    output = ""
    wordsList.append([])
    for j in range(0, 3):
        wordsList[i].append(splitList[spot])
        output += "{:8}".format(wordsList[i][j])
        spot += 1
    print(output)
