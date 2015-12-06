f = open("input.txt", "r")

niceTotal = 0
vowels = ["a","e","i","o","u"]

for string in f:
    nice = True
    hasDouble = False
    vowelCount = 0

    charIndex = 0

    if "ab" in string or "cd" in string or "pq" in string or "xy" in string:
        nice = False

    else:
        for c in string:
            if c in vowels:
                vowelCount += 1
            try:
                if string[charIndex + 1] == c:
                    hasDouble = True
            except IndexError:
                continue

            charIndex += 1

    if not hasDouble:
        nice = False

    if vowelCount < 3:
        nice = False

    if nice:
        niceTotal += 1

print("there are {} nice strings (using the old rules)".format(niceTotal))

niceTotal = 0

f = open("input.txt", "r")
for string in f:
    ruleOnePassed = False
    ruleTwoPassed = False

    charIndex = 0
    for c in string:
        try:
            if string.count(str(string[charIndex] + string[charIndex + 1])) >= 2:
                ruleOnePassed = True
            if string[charIndex] == string[charIndex + 2]:
                ruleTwoPassed = True
        except IndexError:
            continue

        charIndex += 1

    if ruleOnePassed and ruleTwoPassed:
        niceTotal += 1

print("there are {} nice strings (using the new rules)".format(niceTotal))
