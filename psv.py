word = input("Gimme a word: ")

wordLength = len(word)
print (wordLength)

if wordLength < 3:
    print (word)
elif wordLength >= 3 and word[-3:] == "ing":
    print (word + "ly")
elif wordLength >= 3 and word[-3:] != "ing":
    print (word + "ing")
