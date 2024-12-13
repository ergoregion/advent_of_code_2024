def is_increasing(l):
    n=int(l[0])
    for k in l[1:]:
        m=int(k)
        if m<=n or m-n>3:
            return False
        n=m

    return True


def is_decreasing(l):
    n = int(l[0])
    for k in l[1:]:
        m= int(k)
        if m >= n or n - m > 3:
            return False
        n = m

    return True




file = open('data/day2data','r')

list1 =[]
list2 =[]

safe_count =0

for i in file.readlines():
    l=i.split()
    if is_increasing(l) or is_decreasing(l):
        safe_count += 1

print(safe_count)


def safe_line_with_omission(l,index):
    m=l[:index] + l[index+1 :]
    return is_increasing(m) or is_decreasing(m)


def safe_line(l):
    for j in range(len(l)):
        if safe_line_with_omission(l, j):
            return True



safe_count =0
file.seek(0)
for i in file.readlines():
    l=i.split()
    if is_increasing(l) or is_decreasing(l) or safe_line(l):
        safe_count += 1

print(safe_count)

file.close()


