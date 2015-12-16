f = open("input.txt")

lines = []

countLiteral = 0
countString = 0
newEncodeCount = 0

for line in f:
    line = line.strip()
    lines.append(line)

    for c in line:
        countLiteral += 1

        # Reencode count
        if c == '"' or c == '\\':
            newEncodeCount += 2
        else:
            newEncodeCount += 1

    #evaluate the literal string
    newLine = eval(line)
    countString += len(newLine)

    # account for "new" quotes
    newEncodeCount += 2

print("{} characters in literal string".format(countLiteral))
print("{} valid evaluated characters".format(countString))
print("answer (part 1): {} characters".format(countLiteral - countString))
print("{} newly encoded characters".format(newEncodeCount))
print("answer (part 2): {} characters".format(newEncodeCount - countLiteral))
