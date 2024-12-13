
with open('data/day11data', 'r') as file:
    txt = file.read()

arr = [int(a) for a in txt.split()]
print(arr)

blinks =25
results = [arr]
for i in range(blinks):
    last_line = results[i]
    new_line =[]
    for a in last_line:
        str_a = str(a)
        l_str_a = len(str_a)
        half_l_str_a = l_str_a//2
        if a==0:
            new_line.append(1)
        elif l_str_a%2 == 0:
            new_line.append(int(str_a[:half_l_str_a]))
            new_line.append(int(str_a[half_l_str_a:]))
        else:
            new_line.append(2024*a)

    results.append(new_line)
print(results[blinks])
print(len(results[blinks]))


def new_numbers(a):
    result =[]
    str_a = str(a)
    l_str_a = len(str_a)
    half_l_str_a = l_str_a//2
    if a==0:
            result.append(1)
    elif l_str_a%2 == 0:
            result.append(int(str_a[:half_l_str_a]))
            result.append(int(str_a[half_l_str_a:]))
    else:
            result.append(2024*a)
    return result


cache_of_count = {}
def number_count(a, steps):
    if ((a,steps) in cache_of_count):
        return cache_of_count.get((a,steps))
    if steps == 0:
        return 1
    else:
        nn = new_numbers(a)
        r = sum([number_count(b,steps-1) for b in nn])
        cache_of_count[(a,steps)] = r
        return r

steps =75


print(sum([number_count(b,steps) for b in arr] ))
pass