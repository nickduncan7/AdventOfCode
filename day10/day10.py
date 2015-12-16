from itertools import groupby

def lookandsay(inStr):
    return ''.join(str(len(list(v))) + k for k, v in groupby(inStr))

start = "3113322113"

for _ in range(40):
    start = lookandsay(start)

print("length (40):", len(start))

for _ in range(10):
    start = lookandsay(start)

print("length (50):", len(start))
