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

class Block:
    def __init__(self, p):
        self.p = np.array(p)

def is_a_block(c):
    return c == '#'

blocks = np.zeros((len(arr), 2*len(arr[0])))
barrels = []

for i, l in enumerate(arr):
    for j, c in enumerate(l):
        if c == '@':
            start_position = np.array([i, 2*j])
        elif c == 'O':
            barrels.append(Barrel(np.array([i,2*j])))
        elif c =='#':
            blocks[i,2*j]=1
            blocks[i,2*j+1]=1

robot = Robot(start_position)
print(robot.p)
print(len(barrels))

def printa(i):

    result = np.copy(blocks)

    for b in barrels:
        result[b.p[0],b.p[1]] = 2
        result[b.p[0],b.p[1]+1] = 2
    result [ robot.p[0],robot.p[1]] =3
    matplotlib.image.imsave(f'c:/temp/images/robot_output_b{i}.png', result)

printa("initial")


with open('data/day15datab', 'r') as file:
    txt = file.read()


def block_at(position):
    return blocks[position[0],position[1]]
def barrel_at(position):
    for b in barrels:
        if all(b.p == position):
            return b
        elif all(b.p+np.array([0,1]) == position):
            return b
    return None

class NoPushEx(Exception):
    def __init__(self):
        # Call the base class constructor with the parameters it needs
        super().__init__()


def subbarrels_to_push(bar, delta):
    result =[]
    len_r = 0
    if(block_at(bar.p+delta)):
        raise NoPushEx()
    barrel = barrel_at(bar.p+delta)
    if barrel is not None and barrel is not bar:
        result.append(barrel)
        result.extend(subbarrels_to_push(barrel,delta))
    if(block_at(bar.p+np.array([0,1])+delta)):
        raise NoPushEx()
    barrel = barrel_at(bar.p+np.array([0,1])+delta)
    if barrel is not None and barrel is not bar:
        result.append(barrel)
        result.extend(subbarrels_to_push(barrel,delta))
    return result

def barrels_to_push(position, delta):
    result =[]
    len_r = 0
    if(block_at(position+delta)):
        raise NoPushEx()
    barrel = barrel_at(position+delta)
    if barrel is None:
        return result
    result.append(barrel)
    result.extend(subbarrels_to_push(barrel,delta))
    return result



def step(delta):
    one_ahead = robot.p+delta
    if(block_at(one_ahead)):
        return
    if(barrel_at(one_ahead) is None):
        robot.p = one_ahead
        return

    try:
        bp = barrels_to_push(robot.p, delta)
    except NoPushEx:
        return

    for b in set(bp):
        b.p=b.p+delta

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
