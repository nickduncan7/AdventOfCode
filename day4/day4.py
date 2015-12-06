import md5

test = 1
found = False

while found == False:
    m = md5.new()
    m.update("iwrupvqb{number}".format(number = test))

    hexDump = m.hexdigest()[:5]

    zeroes = True
    charCount = 0
    for c in hexDump:
        if zeroes == False:
            continue
        else:
            if c == "0":
                zeroes = True
            else:
                zeroes = False

    if zeroes == True:
        found = True
        continue
    else:
        test += 1

print("lowest number (five zeroes): {num}".format(num = test))

test = 1
found = False

while found == False:
    m = md5.new()
    m.update("iwrupvqb{number}".format(number = test))

    hexDump = m.hexdigest()[:6]

    zeroes = True
    charCount = 0
    for c in hexDump:
        if zeroes == False:
            continue
        else:
            if c == "0":
                zeroes = True
            else:
                zeroes = False

    if zeroes == True:
        found = True
        continue
    else:
        test += 1

print("lowest number (six zeroes): {num}".format(num = test))
