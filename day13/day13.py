from itertools import permutations
me = "Me"

table = {}

def happinessCalc(personA, personB):
    if personA not in table or personB not in table:
        return 0
    else:
        return table[personA][personB]

f = open("input.txt")

for line in f:
    personA, happiness, personB = line.split()

    if personA not in table:
        table[personA] = {}

    if personB not in table:
        table[personB] = {}

    if me not in table:
        table[me] = {}

    table[personA][personB] = int(happiness)

    #Including "me"
    table[personA][me] = 0
    table[me][personA] = 0

bestHappiness = 0

for perm in permutations(table):
    happiness = 0

    for i in range(len(perm) - 1):
        happiness += happinessCalc(perm[i], perm[i + 1])
        happiness += happinessCalc(perm[i + 1], perm[i])

    happiness += happinessCalc(perm[0], perm[-1])
    happiness += happinessCalc(perm[-1], perm[0])

    if happiness > bestHappiness:
        bestHappiness = happiness

print("Total happiness:", bestHappiness)
