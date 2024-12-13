
with open('data/day9data', 'r') as file:
    txt = file.read()

arr = [list(x) for x in txt.splitlines()][0]

print(arr)

is_data= True
data_int = 0
strn = []
dot_locations =[]
for item in arr:
    if is_data:
        for _ in range(int(item)):
            strn.append((data_int))
        data_int = data_int+1
    else:
        for _ in range(int(item)):
            dot_locations.append(len(strn))
            strn.append(('.'))
    is_data = not is_data

for i in dot_locations:
    while len(strn)-1 in dot_locations:
        strn.pop()
    if len(strn)<= i:
        break
    strn[i] = strn.pop()

print(strn)

result =0
for i,v in enumerate(strn):
    result += i*v

print(result)


is_data= True
data_int = 0
index_int = 0
r = []
for item in arr:
    if is_data:
        r.append([int(item),index_int, data_int])
        data_int = data_int+1
        index_int+=int(item)
    else:
        r.append([int(item),index_int, '.'])
        index_int+=int(item)
    is_data = not is_data







def rearange(r):
    for i,item in enumerate(r):
        if item[2]=='.' and item[0]>0:
            for possible_to_move in reversed(r[i:]):
                if(possible_to_move[2]=='.'):
                    pass
                elif(possible_to_move[1]<= item[1]):
                    pass
                elif(possible_to_move[0]>item[0]):
                    pass
                else:
                    possible_to_move[1] = item[1]
                    item[0] = item[0]-possible_to_move[0]
                    item[1] = item[1]+possible_to_move[0]
                    return True
    return False

may_still_need_rearange=True

while may_still_need_rearange:
    may_still_need_rearange = rearange(r)
print(r)

result =0
for item in r:
    if (item[2] != '.'):
        for i in range(item[0]):
            result += (item[1]+i)*item[2]
print(result)
