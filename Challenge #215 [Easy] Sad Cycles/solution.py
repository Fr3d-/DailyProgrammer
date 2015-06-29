#!/usr/bin/python3.4

b = input()
n = input()

l = []
loops = 0

while True:
	n = sum([int(x)**int(b) for x in str(n)])
	if n in l:
		break

	l.append(n)
	loops = loops + 1
	
#     join strings for every converted str in l[i.index(n):loops]
print(", ".join([str(x) for x in l[l.index(n):loops]]), end="")