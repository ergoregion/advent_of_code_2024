import numpy as np
import matplotlib.image

with open('data/day15data', 'r') as file:
    txt = file.read()

arr = [list(x) for x in txt.splitlines()]
print(arr)


class Robot:
    def __init__(self, p):
        self.p = np.array(p)
class Barrel:
    def __init__(self, p):
        self.p = np.array(p)

def is_a_block(c):
    return c == '#'


blocks = np.array([[is_a_block(y) for y in x] for x in arr])

print(blocks)

barrels = []

for i, l in enumerate(arr):
    for j, c in enumerate(l):
        if c == '@':
            start_position = np.array([i, j])
        elif c == 'O':
            barrels.append(Barrel(np.array([i,j])))
robot = Robot(start_position)
print(robot.p)
print(len(barrels))


with open('data/day15datab', 'r') as file:
    txt = file.read()

def printa(i):

    result = np.array([[(1 if is_a_block(y) else 0) for y in x] for x in arr])

    for b in barrels:
        result[b.p[0],b.p[1]] = 2
    result [ robot.p[0],robot.p[1]] =3
    matplotlib.image.imsave(f'c:/temp/images/robot_output{i}.png', result)

def block_at(position):
    return blocks[position[0],position[1]]
def barrel_at(position):
    for b in barrels:
        if all(b.p == position):
            return b
    return None


def step(delta):
    one_ahead = robot.p+delta
    if(block_at(one_ahead)):
        return
    if(barrel_at(one_ahead) is None):
        robot.p = one_ahead
        return

    spaces_to_push=1
    while barrel_at(robot.p+spaces_to_push*delta) is not None:
        spaces_to_push += 1
    if(block_at(robot.p+spaces_to_push*delta)):
        return
    else:
        barrel_at(one_ahead).p = robot.p+spaces_to_push*delta

        robot.p = one_ahead




for i, rule in enumerate(txt):
    if(rule == '\n'):
        pass
    elif(rule == '^'):
        step(np.array([-1,0]))
    elif(rule == 'v'):
        step(np.array([1,0]))
    elif(rule == '>'):
        step(np.array([0,1]))
    elif(rule == '<'):
        step(np.array([0,-1]))

printa("final")

result =0
for b in barrels:
    result += 100*b.p[0]+b.p[1]
print(result)




