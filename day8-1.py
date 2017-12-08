import re
from collections import defaultdict

opmap = {
    ">": lambda x, y : x > y,
    "<": lambda x, y : x < y,
    "<=": lambda x, y : x <= y,
    ">=": lambda x, y: x >= y,
    "==": lambda x, y : x == y,
    "!=": lambda x, y : x != y
}


registers = defaultdict(lambda: 0)


with open("input8.txt") as fh:
    for line in fh:
        name, opcode, opvalue, _, condname, condop, condvalue = re.split(" ", line)
    
        if opmap[condop](registers[condname], int(condvalue)):

            if opcode == "inc":
                registers[name] += int(opvalue)
            elif opcode == "dec":
                registers[name] -= int(opvalue)
            else:
                raise RuntimeError()


print max(registers.values())


