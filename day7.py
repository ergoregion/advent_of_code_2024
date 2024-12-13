import itertools

import numba

with open('data/day7data', 'r') as file:
    txt = file.read()

add = lambda a,b : a+b
times = lambda a,b : a*b
conc = lambda a,b : int(str(a) + str(b))

operations = [add,times,conc]
def check(value, current, remaining_options):
    if(len(remaining_options)==0 and value==current):
        return True
    elif len(remaining_options)==0:
        return False
    else:
        for o in operations:
            if check(value,o(current,remaining_options[0]), remaining_options[1:]):
                return True
    return False

def check_permutation(value, options):
    return check(value,options[0], options[1:])



operations = [add,times]


result =0
for i,x in enumerate(txt.splitlines()):
    n= x.split(':')
    value = int(n[0])
    options = [int(b) for b in n[1].split()]

    if check_permutation(value, options):
        result += value

print(result)

operations = [add,times,conc]

result =0
for i,x in enumerate(txt.splitlines()):
    n= x.split(':')
    value = int(n[0])
    options = [int(b) for b in n[1].split()]

    if check_permutation(value, options):
        result += value

print(result)


