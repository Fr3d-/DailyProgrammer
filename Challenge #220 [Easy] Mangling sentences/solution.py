#!/usr/bin/python3.4
# NOT DONE
s = "This challenge doesn't seem so hard."
words = s.split()

sentence = []

for i, word in enumerate(words):
	wordList = []
	for j, c in enumerate(word):
		if ord(c) > 64 and ord(c) < 91:
			wordList.append(j)

	#uppercaseList.append(wordList)
	sortedWord = ''.join(sorted(words[i].lower()))

	for i in wordList:
		sortedWord[i].upper()

	sentence.append(sortedWord)

print(" ".join(sentence))

print(s)
