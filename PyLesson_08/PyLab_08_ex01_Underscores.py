sentence = input("Enter in a sentence:")

def replace(sentence):
    if sentence.count(" ") == 0:
        return sentence
    else:
        sentence = sentence[0 : sentence.index(" ")] +"_"+ sentence[sentence.index(" ")+1: len(sentence)]
        return replace(sentence)
print(replace(sentence))

