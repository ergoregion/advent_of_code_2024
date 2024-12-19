import numba
import functools


with (open('data/day19data', 'r') as file):
    lines = file.readlines()

    towels = [s.strip() for s in lines[0].split(',')]
    designs = [s.strip() for s in lines[2:]]


print(towels)
print(designs)


sorted_towels = {'w':[],'u':[],'b':[],'r':[],'g':[]}
for t in towels:
    sorted_towels[t[0]].append(t)

print(sorted_towels)

@numba.jit
def extract_start_with_towel(design, towel):
    l = len(towel)
    if len(design)<l:
        return False, design
    elif design[:l] != towel:
        return False, design
    else:
        return True, design[l:]

@numba.jit
def finish_with_towels(design, towels):
    for t in towels:
        success, remaining_design = extract_start_with_towel(design,t)
        if success:
            if len(remaining_design)==0:
                return True
            elif finish_with_towels(remaining_design, towels):
                return True

    return False

results = [finish_with_towels(d, towels) for d in designs]
print(results)
print(sum(results))



result_cache = {}
def sum_possible_designs_with_towels(design):
    result = 0
    for t in towels:
        success, remaining_design = extract_start_with_towel(design,t)
        if success:
            if len(remaining_design)==0:
                result  += 1
            elif remaining_design in result_cache:
                result += result_cache[remaining_design]
            else:
                s = sum_possible_designs_with_towels(remaining_design)
                result_cache[remaining_design] = s
                result += s

    return result


total = 0
for i, d in enumerate(designs):
    print(f"{i} of {len(designs)}")
    if( results[i]):
        total += sum_possible_designs_with_towels(d)

print(total)