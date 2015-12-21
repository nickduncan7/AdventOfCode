alphabet = "abcdefghijklmnopqrstuvwxyz"

def rule1(password):
    for i in range(len(password) - 2):
        try:
            if password[i:i + 3] in alphabet:
                return True
        except IndexError:
            continue
    return False

def rule2(password):
    if 'i' in password or 'o' in password or 'l' in password:
        return False
    else:
        return True

def rule3(password):
    count = 0
    usedIndices = []
    for i in range(len(password) - 1):
        try:
            if password[i] == password[i + 1] and not (i in usedIndices or i + 1 in usedIndices):
                count += 1
                usedIndices.append(i)
                usedIndices.append(i + 1)
        except IndexError:
            continue

    return count > 1

def validPassword(password):
    if rule1(password) and rule2(password) and rule3(password):
        return True
    else:
        return False

# test cases
assert rule1('hijklmmn')
assert not rule2('hijklmmn')
assert rule3('abbceffg')
assert not rule1('abbceffg')
assert not rule3('abbcegjk')
assert validPassword('abcdffaa')
assert validPassword('ghjaabcc')

def incrementString(string):
        try:
            return string[0:-1] + alphabet[alphabet.index(string[-1]) + 1]
        except IndexError:
            return incrementString(string[0:-1]) + 'a'

password = "vzbxkghb"

while (not validPassword(password)):
    password = incrementString(password)

print("Part 1:", password)

password = incrementString(password)
while (not validPassword(password)):
    password = incrementString(password)

print("Part 2:", password)
