f = open("input.txt", "r")
inStr = f.read()

tally = 0
total = 0

for c in inStr:
	total += 1
	if c == "(":
		tally += 1
	elif c == ")":
		tally -= 1
	if tally == -1:
		print(total)

print(tally)
