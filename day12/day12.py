import re
from json import loads

f = open("input.txt","r").read()

sumNumbers = 0

# Regex the positive and negative numbers
numbers = re.findall(r'[-\d]+', f)
for num in numbers:
    sumNumbers += int(num)
print("Sum (Part 1):", sumNumbers)

# Skip over anything containing "red"
def hook(jsonObject):
  if "red" in jsonObject.values():
       return {}
  else:
      return jsonObject

sumTwo = 0
f2 = str(loads(f, object_hook = hook))

# Regex the positive and negative numbers
numbersTwo = re.findall(r'[-\d]+', f2)
for num in numbersTwo:
    sumTwo += int(num)

print("Sum (Part 2):", sumTwo)
