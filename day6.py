import numba
import numpy as np

with open('data/day6data', 'r') as file:
    txt = file.read()

arr = [list(x) for x in txt.splitlines()]
print(arr)


def is_a_block(c):
    return c == '#'


blocks = np.array([[is_a_block(y) for y in x] for x in arr])
visited = np.array([[0 for y in x] for x in arr])

print(blocks)

for i, l in enumerate(arr):
    for j, c in enumerate(l):
        if c == '^':
            start_position = np.array([i, j])
position = start_position
print(position)


up = np.array([-1,0])
right = np.array([0,1])
down = np.array([1,0])
left = np.array([0,-1])


start_delta = up
delta = start_delta
@numba.jit
def rotate_right(delta):
    if (delta == up).all():
        return right
    if (delta == right).all():
        return down
    if (delta == down).all():
        return left
    if (delta == left).all():
        return up


while True:
    visited[position[0]][position[1]] = 1
    possible_new_position = position+delta
    if not (possible_new_position[0] >= 0 and possible_new_position[1] >= 0 and possible_new_position[0] < len(arr) and
            possible_new_position[1] < len(arr[0])):
        break
    if blocks[possible_new_position[0]][possible_new_position[1]] == 1:
        delta = rotate_right(delta)
    else:
        position = possible_new_position

result = 0

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if visited[i][j] == 1:
            result += 1

print(result)

position = start_position
delta = start_delta


@numba.jit
def has_hit_loop(position, delta, visited):
    for v in visited:
        if position[0] == v[0][0] and position[1] == v[0][1] and delta[0] == v[1][0] and delta[1] == v[1][1]:
            return True
    return False


@numba.jit
def is_looping(extra_block, position, delta):
    visited = []
    while True:

        visited.append((position, delta))

        possible_new_position = position+delta
        if not (possible_new_position[0] >= 0 and possible_new_position[1] >= 0 and possible_new_position[0] <
                blocks.shape[0] and possible_new_position[1] < blocks.shape[1]):
            return False
        if blocks[possible_new_position[0]][possible_new_position[1]] == 1:
            delta = rotate_right(delta)
        elif possible_new_position[0] == extra_block[0] and possible_new_position[1] == extra_block[1]:
            delta = rotate_right(delta)
        else:
            position = possible_new_position
        if has_hit_loop(position, delta, visited):
            return True


result = 0
for i in range(len(arr)):
    print(f"{int(i*100.0/len(arr))}%")
    for j in range(len(arr[0])):
        if blocks[i][j] == 1:
            pass
        elif not visited[i][j] == 1:
            pass
        elif (is_looping(np.array([i, j]), start_position, start_delta)):
            result += 1
print(result)
