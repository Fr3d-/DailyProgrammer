consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

s = input()

def encode(s):
	for consonant in consonants:
		if consonant in s:
			l = s.split(consonant)
			s = (consonant + "o" + consonant.lower()).join(l)

	return s

def decode(s):
	for consonant in consonants:
		if consonant in s:
			l = s.split(consonant + "o" + consonant.lower())
			s = consonant.join(l)

	return s

print(encode(s))