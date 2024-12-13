import re

import numpy
import numpy as np
class Problem:
    def __init__(self, a, b, target):
        self.a = np.array(a)
        self.b = np.array(b)
        self.target = np.array(target)

        self.mat = np.array([a,b]).transpose()

    def solve(self, offset=np.array([0,0])):
        if(np.linalg.det(self.mat)==0):
            raise Exception("SINGULAR")
        self.pushes =  (np.rint(np.linalg.solve(self.mat, self.target+offset))).astype(int)

    def is_solved(self, offset=np.array([0,0])):
        return all(numpy.matmul(self.mat, self.pushes)==self.target+offset)

    def cost(self):
        return 3*self.pushes[0]+self.pushes[1]

    def __str__(self):
        return f'A: {self.a} B: {self.b} target:{self.target}'

problems = []


with open('data/day13data', 'r') as file:
    lines = file.readlines()
    number_of_lines = len(lines)
    number_of_problems = (number_of_lines-3)//4 + 1
    for i in range(number_of_problems):
        a_values = re.findall(r"\d+", lines[4*i])
        a= [int(a_values[0]), int(a_values[1])]
        b_values = re.findall(r"\d+", lines[4*i+1])
        b= [int(b_values[0]), int(b_values[1])]
        prize_lines = re.findall(r"\d+", lines[4*i+2])
        target=[int(prize_lines[0]), int(prize_lines[1])]

        problems.append(Problem(a,b, target))
print([str(p) for p in problems])

for p in problems:
    p.solve()

result =0
for p in problems:
    if p.is_solved():
        result += p.cost()

print(result)

offset =np.array([10000000000000,10000000000000])
for p in problems:
    p.solve(offset)

result =0
for p in problems:
    if p.is_solved(offset):
        result += p.cost()

print(result)
