from itertools import permutations

with (open('data/day24data', 'r') as file):
    lines = file.readlines()

wires = dict([(s[0:3], bool(int(s[5]))) for s in lines])

xs =[]
i = 0
l = "x{:02d}".format(i)
while(l in wires):
    xs.append(wires[l])
    i = i+1
    l = "x{:02d}".format(i)
x=''.join(['1' if item else '0' for item in reversed(xs)])
print(x)
print(int(x,2))


ys =[]
i = 0
l = "y{:02d}".format(i)
while(l in wires):
    ys.append(wires[l])
    i = i+1
    l = "y{:02d}".format(i)
y=''.join(['1' if item else '0' for item in reversed(ys)])
print(y)
print(int(y,2))



with (open('data/day24data2', 'r') as file):
    lines = file.readlines()

switchables=[k.split()[4] for k in lines]
print(switchables)

switcher = {
    switchables[0]:switchables[0],
    switchables[2]:switchables[2],
    switchables[4]:switchables[4],
    switchables[6]:switchables[6],
    switchables[1]:switchables[1],
    switchables[3]:switchables[3],
    switchables[5]:switchables[5],
    switchables[7]:switchables[7],
}

def interpret(s, switcher, wires):
    k = s.split()

    if(k[0] in switcher):
        a = switcher[k[0]]
    else:
        a= k[0]

    if(k[2] in switcher):
        b = switcher[k[2]]
    else:
        b= k[2]

    if (a not in wires):
        return False
    if (b not in wires):
        return False
    v1 = wires[a]
    v2 = wires[b]
    if k[1] == 'AND':
        r = v1 and v2
    elif k[1] == 'OR':
        r = v1 or v2
    elif k[1] == 'XOR':
        r = v1.__xor__(v2)
    else:
        raise Exception
    if(k[4] in switcher):
        wires[switcher[k[4]]] = r
    else:
        wires[k[4]] = r
    return True

def result(switcher,xs,ys):

    w={}
    for i,x in enumerate(xs):
        key = "x{:02d}".format(i)
        w[key] = x

    for i, y in enumerate(ys):
        key = "y{:02d}".format(i)
        w[key] = y

    while True:
        changed = [interpret(s,switcher,w) for s in lines]
        if all(changed):
            break
        elif all(not c for c in changed):
            return None

    zs = []
    i = 0
    l = "z{:02d}".format(i)
    while (l in w):
        zs.append(w[l])

        i = i + 1
        l = "z{:02d}".format(i)
    f = ''.join(['1' if item else '0' for item in reversed(zs)])
    r = int(f, 2)
    return zs

def test(switcher,x,y):
    xn = [i=='1' for i in f'{x:{len(xs)}b}']
    yn = [i=='1' for i in f'{y:{len(ys)}b}']
    r = result(switcher,reversed(xn),reversed(yn))
    return r


d = test(switcher, 29869243016611, 26851697606349)
print(d)

def expected(x,y):
    z=x+y
    return [i=='1' for i in reversed(f'{z:{len(d)}b}')]

print(expected(29869243016611, 26851697606349))

def switchers():
   for p in permutations(switchables, 8):
       yield{
    p[0]:p[1],
    p[1]:p[0],
    p[2]:p[3],
    p[3]:p[2],
    p[4]:p[5],
    p[5]:p[4],
    p[6]:p[7],
    p[7]:p[6],
}


#for i,s in enumerate(switchers()):
#    print (f"{i} of {l}")
#    if test(switcher, 29869243016611, 26851697606349) == 29869243016611+26851697606349:
#        print(switcher)
#        break


