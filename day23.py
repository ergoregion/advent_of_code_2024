import functools
with (open('data/day23data', 'r') as file):
    lines = file.readlines()


connections = [(s[0:2],s[3:5]) for s in lines]
print(connections)
computers_a = set(s[0] for s in connections)
computers_b = set(s[1] for s in connections)
computers = computers_a.union(computers_b)
computers = sorted(computers)
print(computers)


@functools.cache
def connected(comp1,comp2):
    return (comp1,comp2) in connections or (comp2,comp1) in connections


def triply_connected(comp1,comp2, comp3):
    return connected(comp1,comp2) and connected(comp3,comp2) and connected(comp1,comp3)

triplets =[]
print(len(computers))
for i,comp1 in enumerate(computers):
    print(f"i ={i}")
    for j in range(i, len(computers)):
        comp2= computers[j]
        for k in range(j, len(computers)):
            comp3= computers[k]
            if(triply_connected(comp1,comp2,comp3)):
                triplets.append((comp1,comp2,comp3))

print(triplets)
print(len(triplets))

result =0
for t in triplets:
    if(t[0][0] =='t' or t[1][0] =='t' or t[2][0]=='t'):
        result += 1
print(result)

groups = []

def add_computer(c):
    for g in groups:
        if (all([connected(c, item) for item in g])):
            g.append(c)
            return
    groups.append([c])

for c in computers:
    add_computer(c)

print([len(g) for g in groups])

biggest_group = sorted(groups, key=len)[-1]

print(biggest_group)
print(','.join(biggest_group))
