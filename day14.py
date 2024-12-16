import numpy as np
import re
import math
from PIL import Image
import matplotlib.image
def savetxt_compact(fname, x, delimiter=' '):
    with open(fname, 'w') as fh:
        for row in x:
            line = delimiter.join(" " if value == 0 else '#' for value in row)
            fh.write(line + '\n')

class Robot:
    def __init__(self, p,v):
        self.p = np.array(p)
        self.v = np.array(v)
    def positon_after_steps(self, steps, extents):
        p = (self.p+steps*self.v)
        p2 = np.remainder(p,extents)
        return p2

robots =[]
with open('data/day14data', 'r') as file:
    lines = file.readlines()
    for line in lines:
        a_values = re.findall(r"[-+]?[0-9]+", line)
        print(a_values)
        assert (len(a_values)==4)
        p= [int(a_values[0]), int(a_values[1])]
        v= [int(a_values[2]), int(a_values[3])]
        robots.append(Robot(p,v))
print(len(robots))

#extents = np.array([11,7])
extents=np.array([101,103])

count = np.zeros(extents, dtype=np.int32)
steps =100
for r in robots:
    k=r.positon_after_steps(steps, extents)
    count[k[0],k[1]] +=1
print(count.transpose())

m0a=math.floor(extents[0]/2.0)
m0b=math.ceil(extents[0]/2.0)
m1a=math.floor(extents[1]/2.0)
m1b=math.ceil(extents[1]/2.0)

quad_1_count = count[:m0a,:m1a]
quad_2_count = count[:m0a,m1b:]
quad_3_count = count[m0b:,:m1a]
quad_4_count = count[m0b:,m1b:]

print(quad_1_count.sum())
print(quad_2_count.sum())
print(quad_3_count.sum())
print(quad_4_count.sum())
print(quad_1_count.sum()*quad_2_count.sum()*quad_3_count.sum()*quad_4_count.sum())

np.set_printoptions(threshold=np.inf)
for i in range(103*101):
    count = np.zeros(extents, dtype=np.int32)
    for r in robots:
        k = r.positon_after_steps(i, extents)
        count[k[0], k[1]] += 1
    if(count.max() ==1):
        print(i)
        matplotlib.image.imsave(f'c:/temp/images/output{i}.png', count)



