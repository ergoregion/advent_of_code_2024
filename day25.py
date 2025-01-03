

things = []




with open('data/day25data', 'r') as file:
    lines = file.readlines()
    number_of_lines = len(lines)
    number_of_problems = (number_of_lines+1)//8
    for i in range(number_of_problems):

        l= lines[8*i:8*i+7]
        things.append(l)

def n(t):
  result = [0,0,0,0,0]
  for i in range(1,6):
      for j in range(0,5):
        if t[i][j]=='#':
            result[j] += 1
  return result




locks = []
keys = []
for t in things:
    print(t[0][:])
    if t[0].count('#') ==5:
        locks.append(t)
    elif t[0].count('.')==5:
        keys.append(t)

locks = [n(l) for l in locks]
keys = [n(l) for l in keys]

print(locks)
print(keys)

print(len(locks))
print(len(keys))
def overlap(lock,key):
    x = ((lock[i]+key[i])>5 for i in range(5))
    return any(x)

result =0
for l in locks:
    for k in keys:
        if not overlap(l,k):
            result +=1
print(result)
