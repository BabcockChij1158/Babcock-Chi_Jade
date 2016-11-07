sentence = input("Enter in a sentence:")

def replace(sentence):
    if sentence.count(" ") == 0:
        return sentence
    else:
        return sentence[0 : sentence.index(" ")] +"_"+ sentence[sentence.index(" ")+1: len(sentence)]

print(replace(sentence))

#EDIT this because it will only put an underscore at the first space...
