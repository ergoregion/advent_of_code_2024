with (open('data/day24data', 'r') as file):
    lines = file.readlines()


wires = dict([(s[0:3], bool(int(s[5]))) for s in lines])
print(wires)

with (open('data/day24data2', 'r') as file):
    lines = file.readlines()


def interpret(s):
    k = s.split()
    if (k[0] not in wires):
        return False
    if (k[2] not in wires):
        return False
    v1 = wires[k[0]]
    v2 = wires[k[2]]
    if k[1] == 'AND':
        r = v1 and v2
    elif k[1] == 'OR':
        r = v1 or v2
    elif k[1] == 'XOR':
        r = v1.__xor__(v2)
    else:
        raise Exception
    wires[k[4]] = r
    return True

finished = False
while not finished:
    finished = True
    for s in lines:
        finished = interpret(s) and finished
    print(wires)

print(wires)

zs =[]
i = 0
l = "z{:02d}".format(i)
print(l)
while(l in wires):
    print(l)
    zs.append(wires[l])

    i = i+1
    l = "z{:02d}".format(i)
f=''.join(['1' if item else '0' for item in reversed(zs)])
print(f)
print(int(f,2))

