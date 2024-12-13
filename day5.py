from functools import cmp_to_key

def testrule(line, rule):
    try:
        index1 = line.index(rule[0])
        index2 = line.index(rule[1])
    except ValueError:
        return True

    if index1 >= index2:
        return False
    return True
def test(line, rules):

    for rule in rules:

        if not testrule(line, rule):
            return False
    return True

def reorder(l,rules):

    def correct(x, y):
        for r in rules:
            if y==r[0] and x == r[1]:
                return 1
        return -1

    return sorted(l, key=cmp_to_key(correct))



file = open('data/day5data1','r')

rules =[]


for i in file.readlines():
    l=i.split('|')
    rules.append([int(l[0]), int(l[1])])

print(rules)

file.close()

file2 = open('data/day5data2','r')

result =0
for i in file2.readlines():
    l = [int(j) for j in i.split(',')]
    if(test(l,rules)):
        result += l[int(len(l)/2)]

print(result)


file2.seek(0)
result =0
for i in file2.readlines():
    l = [int(j) for j in i.split(',')]
    if(not test(l,rules)):
        newl=reorder(l,rules)
        result += newl[int(len(l)/2)]
print(result)
file2.close()
