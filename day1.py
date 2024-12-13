file = open('data/day1data','r')

list1 =[]
list2 =[]

for i in file.readlines():
    s= i.split()
    list1.append(int(s[0]))
    list2.append(int(s[1]))

list1.sort()
list2.sort()

result =0

for i,j in zip(list1,list2):
    diff = abs(i-j)
    result += diff

print(result)

result =0
for a in list1:
    result += a * list2.count(a)

print(result)