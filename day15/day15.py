f = open("input.txt", "r")

ingredients = []

for line in f:
    temp = []
    _, _, capacity, _, durability, _, flavor, _, texture, _, calories = line.split()
    temp.append(int(capacity.strip(',')))
    temp.append(int(durability.strip(',')))
    temp.append(int(flavor.strip(',')))
    temp.append(int(texture.strip(',')))
    temp.append(int(calories.strip(',')))
    ingredients.append(temp)


highestScore = 0
highest500Cal = 0

for i in range(0, 100):
    for j in range(0, 100 - i):
        for k in range(0, 100 - i - j):
            h = 100 - i - j - k
            capScore = (ingredients[0][0] * i) + (ingredients[1][0] * j) + (ingredients[2][0] * k) + (ingredients[3][0] * h)
            durScore = (ingredients[0][1] * i) + (ingredients[1][1] * j) + (ingredients[2][1] * k) + (ingredients[3][1] * h)
            flvScore = (ingredients[0][2] * i) + (ingredients[1][2] * j) + (ingredients[2][2] * k) + (ingredients[3][2] * h)
            texScore = (ingredients[0][3] * i) + (ingredients[1][3] * j) + (ingredients[2][3] * k) + (ingredients[3][3] * h)
            calories = (ingredients[0][4] * i) + (ingredients[1][4] * j) + (ingredients[2][4] * k) + (ingredients[3][4] * h)

            if capScore <= 0 or durScore <= 0 or flvScore <= 0:
                continue

            score = capScore * durScore * flvScore * texScore
            if calories == 500:
                if score > highest500Cal:
                    highest500Cal = score
            else:
                if score > highestScore:
                    highestScore = score


print("Highest score possible:", highestScore)
print("Highest 500 calorie cookie:", highest500Cal)
