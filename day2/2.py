total = 0
totalRibbon = 0

f = open("input.txt")

for line in f:
	temp = ""
	length = 0
	width = 0
	height = 0
	
	for c in line:
		if c.isdigit():
			temp += c
		else:
			if length == 0:
				length = int(temp)
			elif width == 0:
				width = int(temp)
			elif height == 0:
				height = int(temp)
			temp = ""
		
	area = ( 2 * length * width ) + ( 2 * width * height ) + (2 * height * length)

	smallestSide = length * width

	if ( width * height ) < smallestSide:
		smallestSide = width * height
	if ( height * length ) < smallestSide:
		smallestSide = height * length

	dimensions = sorted([length, width, height])

	ribbonLength = ( 2 * dimensions[0] ) + ( 2 * dimensions[1] ) + ( length * width * height )

	area += smallestSide

	total += area
	totalRibbon += ribbonLength

print("total paper: {size} sq ft".format(size=total))	
print("total ribbon: {size} ft".format(size=totalRibbon))	
