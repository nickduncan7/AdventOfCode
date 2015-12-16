from itertools import permutations
import sys

cities = {}

def DistanceBetween(city1, city2):
    if city1 not in cities or city2 not in cities:
        return 0
    else:
        distanceDictionary = cities[city1]
        return distanceDictionary[city2]

f = open("input.txt")

for line in f:
    source, _, dest, _, distance = line.split()

    if source not in cities:
        cities[source] = {}

    if dest not in cities:
        cities[dest] = {}

    cities[source][dest] = int(distance)
    cities[dest][source] = int(distance)

shortestDistance = sys.maxsize
longestDistance = 0

for perm in permutations(cities):
    distance = 0

    otherCity = None
    for city in perm:
        if otherCity == None:
            otherCity = city
        else:
            distance += DistanceBetween(city, otherCity)
            otherCity = city

    if distance < shortestDistance:
        shortestDistance = distance
    if distance > longestDistance:
        longestDistance = distance

print("shortest distance = {}".format(shortestDistance))
print("longest distance = {}".format(longestDistance))
