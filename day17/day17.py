from itertools import combinations

containers = []

f = open("input.txt", "r")
for line in f:
    containers.append(int(line.strip()))

ways = 0
minNum = 0
for i in range(len(containers)):
    for combination in combinations(containers, i):
        if sum(combination) == 150:
            ways += 1
    if ways and not minNum:
        minNum = ways


print("There are {} combinations".format(ways))
print("Part 2: {}".format(minNum))
