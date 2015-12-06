grid = [[0 for _ in xrange(1000)] for _ in xrange(1000)]

# Initialize grid
for x in range(0, 1000):
    for y in range(0, 1000):
        grid[x][y] = 0

f = open("input.txt", "r")
for line in f:
    command, start, _, end = line.strip().rsplit(" ", 3)
    startCoords = start.split(",")
    endCoords = end.split(",")

    startCoords[0] = int(startCoords[0])
    startCoords[1] = int(startCoords[1])
    endCoords[0] = int(endCoords[0])
    endCoords[1] = int(endCoords[1])

    if "on" in command:
        for x in range(startCoords[0], endCoords[0] + 1):
            for y in range(startCoords[1], endCoords[1] + 1):
                grid[x][y] = 1
    elif "off" in command:
        for x in range(startCoords[0], endCoords[0] + 1):
            for y in range(startCoords[1], endCoords[1] + 1):
                grid[x][y] = 0
    else:
        for x in range(startCoords[0], endCoords[0] + 1):
            for y in range(startCoords[1], endCoords[1] + 1):
                if grid[x][y] == 0:
                    grid[x][y] = 1
                else:
                    grid[x][y] = 0

onLights = 0
for x in range(0, 1000):
    for y in range(0, 1000):
        if grid[x][y] == 1:
            onLights += 1

print("{} lights are turned on".format(onLights))

grid = [[0 for _ in xrange(1000)] for _ in xrange(1000)]

# Initialize grid
for x in range(0, 1000):
    for y in range(0, 1000):
        grid[x][y] = 0

f = open("input.txt", "r")
for line in f:
    command, start, _, end = line.strip().rsplit(" ", 3)
    startCoords = start.split(",")
    endCoords = end.split(",")

    startCoords[0] = int(startCoords[0])
    startCoords[1] = int(startCoords[1])
    endCoords[0] = int(endCoords[0])
    endCoords[1] = int(endCoords[1])

    if "on" in command:
        for x in range(startCoords[0], endCoords[0] + 1):
            for y in range(startCoords[1], endCoords[1] + 1):
                grid[x][y] += 1
    elif "off" in command:
        for x in range(startCoords[0], endCoords[0] + 1):
            for y in range(startCoords[1], endCoords[1] + 1):
                grid[x][y] -= 1
                if grid[x][y] < 0:
                    grid[x][y] = 0
    else:
        for x in range(startCoords[0], endCoords[0] + 1):
            for y in range(startCoords[1], endCoords[1] + 1):
                    grid[x][y] += 2

brightness = 0
for x in range(0, 1000):
    for y in range(0, 1000):
            brightness += grid[x][y]

print("{} total brightness".format(brightness))
