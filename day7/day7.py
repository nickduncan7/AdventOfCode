expressions = {}
gates = {}

f = open("input.txt","r")

def findValue(variable):
    # some sort of memoization
    try:
        if variable in gates:
            return gates[variable]
    except ValueError:
        pass

    # if not found, hope it's an integer!
    try:
        gates[variable] = int(variable)
        return gates[variable]
    except ValueError:
        pass

    #if we get here... oh no
    operationList = expressions[variable].split(" ")

    if len(operationList) == 3:
        operationList[0] = int(findValue(operationList[0]))
        operationList[2] = int(findValue(operationList[2]))

        if operationList[1] == "AND":
            gates[variable] = operationList[0] & operationList[2]
        elif operationList[1] == "OR":
            gates[variable] = operationList[0] | operationList[2]
        elif operationList[1] == "LSHIFT":
            gates[variable] = operationList[0] << operationList[2]
        elif operationList[1] == "RSHIFT":
            gates[variable] = operationList[0] >> operationList[2]

        return gates[variable]

    elif len(operationList) == 2:
        gates[variable] = ~findValue(operationList[1])
        return gates[variable]

    else:
        return findValue(operationList[0])

for line in f:
    expression, variable = line.strip().split("->")

    expression = expression.strip()
    variable = variable.strip()

    expressions[variable] = expression

print("a: {} (part A)".format(findValue("a")))

expressions["b"] = str(findValue("a"))
gates.clear()

print("a: {} (part B)".format(findValue("a")))
