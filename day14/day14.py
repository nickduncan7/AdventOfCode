class Reindeer:
    def __init__(self, name, speed, burst, resttime):
        self.Name = name
        self.Speed = speed
        self.Burst = burst
        self.RestTime = resttime
        self.remainingBurst = burst
        self.remainingRest = 0
        self.Distance = 0
        self.Score = 0

    def isResting(self):
        return self.remainingRest >= 1

f = open("input.txt", "r")

reindeers = []

for line in f:
    name, _, _, speed, _, _, burst, _, _, _, _, _, _, resttime, _ = line.split()
    reindeers.append(Reindeer(name, int(speed), int(burst), int(resttime)))

seconds = 2503
highestDistance = None
highestScore = None
for i in range(0, seconds):
    leaders = []
    for reindeer in reindeers:
        if reindeer.isResting():
            reindeer.remainingRest -= 1
            if (reindeer.remainingRest == 0):
                reindeer.remainingBurst = reindeer.Burst

        else:
            reindeer.Distance += reindeer.Speed
            reindeer.remainingBurst -= 1

            if (reindeer.remainingBurst == 0):
                reindeer.remainingRest = reindeer.RestTime

        if highestDistance == None:
            highestDistance = reindeer
        else:
            if reindeer.Distance > highestDistance.Distance:
                highestDistance = reindeer

    for reindeer in reindeers:
        if reindeer.Distance == highestDistance.Distance:
            leaders.append(reindeer)

    for leader in leaders:
        leader.Score += 1

for reindeer in reindeers:
    if highestScore == None:
        highestScore = reindeer
    else:
        if reindeer.Score > highestScore.Score:
            highestScore = reindeer

print("{} has traveled the furthest distance at {} km.".format(highestDistance.Name, highestDistance.Distance))
print("{} scored the highest with {} points.".format(highestScore.Name, highestScore.Score))
