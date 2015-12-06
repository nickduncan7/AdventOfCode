class AoCCoordinate:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.gifts = 0

def contains(x, y):
	for item in houses:
		if item.x == x and item.y == y:
			return True
	return False

def getHouse(x, y):
	for item in houses:
		if item.x == x and item.y == y:
			return item


f = open("input.txt", "r")
inStr = f.read()

santaX = 0
santaY = 0

houses = []
firstHouse = AoCCoordinate(0, 0)

houses.append(firstHouse)
firstHouse.gifts += 1

for c in inStr:
	if c == "v":
		santaY -= 1;
	elif c == "^":
		santaY += 1;
	elif c == "<":
		santaX -= 1;
	elif c == ">":
		santaX += 1;
	else:
		continue

	currentX = santaX
	currentY = santaY

	if contains(currentX, currentY):
		currentHouse = getHouse(currentX, currentY)
	else:
		currentHouse = AoCCoordinate(currentX, currentY)
		houses.append(currentHouse)

	currentHouse.gifts += 1

total = 0
for house in houses:
	if house.gifts >= 1:
		total += 1;

print("{x} houses receive at least 1 present from Santa".format(x=total))

santaX = 0
santaY = 0
robotX = 0
robotY = 0

turn = "s"

houses = []
firstHouse = AoCCoordinate(0, 0)

houses.append(firstHouse)
firstHouse.gifts += 1

f = open("input.txt", "r")
inStr = f.read()

for c in inStr:
	currentX = 0
	currentY = 0

	if turn == "s":
		if c == "v":
			santaY -= 1;
		elif c == "^":
			santaY += 1;
		elif c == "<":
			santaX -= 1;
		elif c == ">":
			santaX += 1;
		else:
			continue

		currentX = santaX
		currentY = santaY

		turn = "r"
	else:
		if c == "v":
			robotY -= 1;
		elif c == "^":
			robotY += 1;
		elif c == "<":
			robotX -= 1;
		elif c == ">":
			robotX += 1;
		else:
			continue

		currentX = robotX
		currentY = robotY

		turn = "s"

	if contains(currentX, currentY):
		currentHouse = getHouse(currentX, currentY)
	else:
		currentHouse = AoCCoordinate(currentX, currentY)
		houses.append(currentHouse)

	currentHouse.gifts += 1

total = 0
for house in houses:
	if house.gifts >= 1:
		total += 1;

print("{x} houses receive at least 1 present from Santa and Robo-Santa".format(x=total))
