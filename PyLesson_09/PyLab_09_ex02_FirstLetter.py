user = input("Enter a list of 5 words separated by a space:")
words = user.split(" ")

def first(words):
    output = ""
    for word in words:
        output += word[0] + " "
    print(output)


first(words)
